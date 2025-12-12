# wildguard/routes/animals.py

from flask import Blueprint, render_template, current_app, flash, redirect, url_for
from models import Species, SpeciesFunFact, Location, HabitatType, Threat
from types import SimpleNamespace
from sqlalchemy.orm import joinedload

animals = Blueprint('animals', __name__)

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