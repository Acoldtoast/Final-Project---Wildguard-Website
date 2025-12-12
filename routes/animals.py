# wildguard/routes/animals.py

from flask import Blueprint, render_template, current_app, flash, redirect, url_for, jsonify
from models import (
    db,
    Species,
    SpeciesFunFact,
    Location,
    HabitatType,
    Threat,
    ConservationStatus,
    SpeciesThreat,
    SpeciesHabitat,
)
from types import SimpleNamespace
from sqlalchemy.orm import joinedload
from sqlalchemy import func

animals = Blueprint('animals', __name__)


def get_site_stats():
    try:
        # Species by conservation status
        by_status_q = (
            db.session.query(
                ConservationStatus.status_name,
                func.count(Species.id).label('species_count'),
            )
            .outerjoin(Species, ConservationStatus.status_id == Species.status_id)
            .group_by(ConservationStatus.status_name)
            .order_by(func.count(Species.id).desc())
        )
        by_status = [(r[0], r[1]) for r in by_status_q.all()]

        # Top threatened species
        top_threats_q = (
            db.session.query(Species.name, func.count(SpeciesThreat.species_threat_id).label('threat_count'))
            .join(SpeciesThreat, Species.id == SpeciesThreat.species_id)
            .group_by(Species.id, Species.name)
            .order_by(func.count(SpeciesThreat.species_threat_id).desc())
            .limit(5)
        )
        top_threats = [(r[0], r[1]) for r in top_threats_q.all()]

        # Total number of species
        total_species = db.session.query(func.count(Species.id)).scalar() or 0

        # Top locations with endangered species
        endangered_names = ['Critically Endangered', 'Endangered']
        top_locations_q = (
            db.session.query(Location.location_name, func.count(func.distinct(Species.id)).label('species_count'))
            .join(SpeciesHabitat, Location.location_id == SpeciesHabitat.location_id)
            .join(Species, Species.id == SpeciesHabitat.species_id)
            .join(ConservationStatus, Species.status_id == ConservationStatus.status_id)
            .filter(ConservationStatus.status_name.in_(endangered_names))
            .group_by(Location.location_name)
            .order_by(func.count(func.distinct(Species.id)).desc())
            .limit(5)
        )
        top_locations = [(r[0], r[1]) for r in top_locations_q.all()]

        # Average threats per species using AVG over subquery (includes zeros)
        subq = (
            db.session.query(
                Species.id.label('species_id'),
                func.count(SpeciesThreat.species_threat_id).label('threat_count'),
            )
            .outerjoin(SpeciesThreat, Species.id == SpeciesThreat.species_id)
            .group_by(Species.id)
            .subquery()
        )
        avg_val = db.session.query(func.avg(subq.c.threat_count)).scalar()
        avg_threats_per_species = round(float(avg_val), 2) if avg_val is not None else 0

        # Location with the fewest distinct species using MIN()
        # 1) compute species counts per location as a subquery
        counts_subq = (
            db.session.query(
                Location.location_name.label('location_name'),
                func.count(func.distinct(SpeciesHabitat.species_id)).label('species_count'),
            )
            .outerjoin(SpeciesHabitat, Location.location_id == SpeciesHabitat.location_id)
            .group_by(Location.location_name)
            .subquery()
        )

        # 2) get the minimum species_count value
        min_count = db.session.query(func.min(counts_subq.c.species_count)).scalar()

        # 3) select a location that has that minimum count
        if min_count is not None:
            fewest_loc_row = db.session.query(counts_subq.c.location_name, counts_subq.c.species_count).filter(counts_subq.c.species_count == min_count).first()
            location_with_fewest_species = (fewest_loc_row[0], fewest_loc_row[1]) if fewest_loc_row else (None, 0)
        else:
            location_with_fewest_species = (None, 0)


        # Total number of habitats assigned across all species using SUM() over per-species counts
        try:
            hab_counts_subq = (
                db.session.query(
                    SpeciesHabitat.species_id.label('species_id'),
                    func.count(SpeciesHabitat.habitat_id).label('habitat_count'),
                )
                .group_by(SpeciesHabitat.species_id)
                .subquery()
            )

            total_habitat_links = db.session.query(func.sum(hab_counts_subq.c.habitat_count)).scalar() or 0
            total_habitat_links = int(total_habitat_links)
        except Exception:
            total_habitat_links = 0

        # Most common habitat type using MAX() over counts subquery
        habitat_counts_subq = (
            db.session.query(
                HabitatType.habitat_name.label('habitat_name'),
                func.count(func.distinct(SpeciesHabitat.species_id)).label('species_count'),
            )
            .join(SpeciesHabitat, HabitatType.habitat_type_id == SpeciesHabitat.habitat_type_id)
            .group_by(HabitatType.habitat_name)
            .subquery()
        )

        max_count = db.session.query(func.max(habitat_counts_subq.c.species_count)).scalar()
        if max_count is not None:
            most_common_row = (
                db.session.query(habitat_counts_subq.c.habitat_name, habitat_counts_subq.c.species_count)
                .filter(habitat_counts_subq.c.species_count == max_count)
                .first()
            )
            most_common_habitat = (most_common_row[0], most_common_row[1]) if most_common_row else (None, 0)
        else:
            most_common_habitat = (None, 0)

    except Exception as e:
        current_app.logger.error(f'Error computing site stats: {e}')
        by_status = []
        top_threats = []
        total_species = 0
        top_locations = []
        avg_threats_per_species = 0
        total_habitat_links = 0
        location_with_fewest_species = (None, 0)
        most_common_habitat = (None, 0)

    return {
        'by_status': by_status,
        'top_threats': top_threats,
        'total_species': total_species,
        'top_locations': top_locations,
        'avg_threats_per_species': avg_threats_per_species,
        'total_habitat_links': total_habitat_links,
        'location_with_fewest_species': location_with_fewest_species,
        'most_common_habitat': most_common_habitat,
    }


@animals.route('/site-stats.json')
def site_stats_json():
    try:
        return jsonify(get_site_stats())
    except Exception as e:
        current_app.logger.error(f'Error returning JSON stats: {e}')
        return jsonify({}), 500

@animals.route("/wildlife")
def list_animals():
    try:
        all_species = Species.query.options(joinedload(Species.status)).order_by(Species.name).all()

        if not all_species:
            flash('No species found in the database. Please check back later.', 'info')

        return render_template('animals.html', title='Wildlife Directory', species_list=all_species)

    except Exception as e:
        current_app.logger.error(f'Error loading species list: {str(e)}')
        flash('An error occurred while loading the wildlife directory.', 'danger')
        return redirect(url_for('pages.home'))


@animals.route("/wildlife/<int:species_id>")
def animal_detail(species_id):
    try:
        current_species = Species.query.get_or_404(species_id)
        threat_list = []
        for t in current_species.threats.all():
            th = Threat.query.get(t.threat_id)
            threat_list.append(SimpleNamespace(threat_name=(th.threat_name if th else '')))

        habitat_list = []
        for h in current_species.habitats.all():
            loc = Location.query.get(h.location_id)
            hab = HabitatType.query.get(h.habitat_type_id)
            habitat_list.append(SimpleNamespace(habitat_location=(f"{loc.location_name} | {hab.habitat_name}" if loc and hab else '')))
        fact_list = current_species.fun_facts.order_by(SpeciesFunFact.__table__.c.fact_id).all()

        current_app.logger.info(f'Species detail page viewed: {current_species.name}')

        return render_template(
            'animal_page.html', 
            title=current_species.name, 
            species=current_species,
            threats=threat_list,
            habitats=habitat_list,
            facts=fact_list
        )

    except Exception as e:
        current_app.logger.error(f'Error loading species detail {species_id}: {str(e)}')
        flash('An error occurred while loading species details.', 'danger')
        return redirect(url_for('animals.list_animals'))