# seed.py
from app import app
from models import (db, ConservationStatus, Species, Location, HabitatType, 
                    SpeciesHabitat, Threat, SpeciesThreat, SpeciesFunFact, 
                    Organization, OrganizationSupports, HelpTip, HelpTipAction, 
                    RelatedArticle, News)
from datetime import date

print("--- Starting Data Insertion ---")

with app.app_context():
    db.create_all()
    print("Tables created (if they didn't exist).")

    print("1. Inserting Conservation Statuses...")
    statuses = [
        {'status_name': 'Critically Endangered', 'description': 'Species facing an extremely high risk of extinction in the wild.'},
        {'status_name': 'Endangered', 'description': 'Species facing a very high risk of extinction in the wild.'},
        {'status_name': 'Vulnerable', 'description': 'Species facing a high risk of extinction in the wild.'},
        {'status_name': 'Near Threatened', 'description': 'Species that may be considered threatened in the near future.'}
    ]

    for data in statuses:
        if not ConservationStatus.query.filter_by(status_name=data['status_name']).first():
            db.session.add(ConservationStatus(**data))
    db.session.commit()
    print("Conservation statuses inserted.")

    # Helper function to get or create location
    def get_or_create_location(location_name):
        loc = Location.query.filter_by(location_name=location_name).first()
        if not loc:
            loc = Location(location_name=location_name)
            db.session.add(loc)
            db.session.commit()
        return loc

    # Helper function to get or create habitat type
    def get_or_create_habitat_type(habitat_name):
        hab = HabitatType.query.filter_by(habitat_name=habitat_name).first()
        if not hab:
            hab = HabitatType(habitat_name=habitat_name)
            db.session.add(hab)
            db.session.commit()
        return hab

    # Helper function to get or create threat
    def get_or_create_threat(threat_name):
        threat = Threat.query.filter_by(threat_name=threat_name).first()
        if not threat:
            threat = Threat(threat_name=threat_name)
            db.session.add(threat)
            db.session.commit()
        return threat

    print("2. Inserting Species...")
    species_list = [
        {
            'name': 'Philippine Eagle',
            'scientific_name': 'Pithecophaga jefferyi',
            'population_estimate': 'Around 400–500 left in the wild',
            'description': """The Philippine Eagle, the country's national bird, is a powerful raptor found only in the Philippines and depends on large, untouched dipterocarp forests. Known for its shaggy crest and strong talons, it hunts animals like flying lemurs, macaques, civets, and reptiles. Although once called the "Monkey-Eating Eagle," monkeys are only part of its diet. The species recovers slowly because a breeding pair lays just one egg about every two years and spends months caring for the chick. Massive deforestation from logging, land conversion, and mining has destroyed much of its habitat, and hunting still happens. Conservation groups, including the Philippine Eagle Foundation, work on rescue, captive breeding, and education to protect the species and its nesting sites.""",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_eagle.jpg',
            'habitats': [
                {'location': 'Mindanao', 'habitat_type': 'Dense mountain forests'},
                {'location': 'Luzon', 'habitat_type': 'Dense mountain forests'},
                {'location': 'Leyte', 'habitat_type': 'Dense mountain forests'},
                {'location': 'Samar', 'habitat_type': 'Dense mountain forests'}
            ],
            'threats': ['Deforestation', 'Illegal hunting', 'Habitat loss'],
            'fun_fact': 'Known as the "Monkey-Eating Eagle"; has a wingspan of about 2 meters and may live up to 60 years in captivity.'
        },
        {
            'name': 'Tamaraw',
            'scientific_name': 'Bubalus mindorensis',
            'population_estimate': 'About 400 individuals remaining in the wild',
            'description': """The Tamaraw is a rare dwarf buffalo native only to Mindoro and is known for its small, stocky build and V-shaped horns. Its once wide range shrank because of heavy hunting, habitat destruction, and diseases from domestic cattle. With females giving birth only every two years, population growth remains slow. Conservation programs led by the DENR, including anti-poaching patrols, monitoring, and protected-area management, have helped some groups recover, though illegal hunting and continuing habitat loss remain serious challenges.""",
            'status_name': 'Critically Endangered',
            'image_file': 'tamaraw.jpg',
            'habitats': [
                {'location': 'Mindoro Island', 'habitat_type': 'Mountain forests'},
                {'location': 'Mindoro Island', 'habitat_type': 'Grasslands'}
            ],
            'threats': ['Habitat loss', 'Hunting/poaching', 'Disease transmitted by domestic cattle'],
            'fun_fact': 'Found nowhere else on Earth; has V-shaped horns and is more solitary than domestic water buffalo.'
        },
        {
            'name': 'Philippine Tarsier',
            'scientific_name': 'Carlito syrichta',
            'population_estimate': 'Unknown, but declining — believed to be a few thousand in scattered islands',
            'description': """The Philippine Tarsier is one of the smallest primates in the world and is notable for its very large round eyes — each roughly the size of its brain — which provide excellent night vision. It is nocturnal and insectivorous, able to leap several meters between branches using powerful hind legs. Tarsiers require dense, quiet forest habitat and are extremely sensitive to handling and noise, so responsible ecotourism and protected sanctuaries are critical for their survival. Threats include habitat loss, the illegal pet trade and disturbance from tourism; stressed tarsiers may injure themselves or stop feeding. Local sanctuaries and community-led conservation programs provide safe areas and education to reduce harmful interactions.""",
            'status_name': 'Near Threatened',
            'image_file': 'philippine_tarsier.jpg',
            'habitats': [
                {'location': 'Bohol', 'habitat_type': 'Forests'},
                {'location': 'Leyte', 'habitat_type': 'Forests'},
                {'location': 'Samar', 'habitat_type': 'Forests'},
                {'location': 'Mindanao', 'habitat_type': 'Forests'}
            ],
            'threats': ['Habitat loss', 'Illegal pet trade', 'Tourism disturbance'],
            'fun_fact': 'Eyes are as large as its brain; can leap up to 3 meters; completely insectivorous.'
        },
        {
            'name': 'Visayan Warty Pig',
            'scientific_name': 'Sus cebifrons',
            'population_estimate': 'Fewer than 200 individuals remaining in the wild',
            'description': '''The Visayan Warty Pig is a rare wild pig found only in the Philippines, known for the facial "warts" that protect it during fights and the long, mohawk-like mane grown by males during breeding season. Once widespread in the Visayas, its population dropped sharply after more than 95% of forests in Negros and Panay were cleared for farming and settlements. With less forest cover, the pigs are more easily hunted, and many now mix with domestic pigs, causing genetic loss. Conservation efforts include captive-breeding programs in local and international zoos, along with community awareness campaigns. The species highlights the wider struggle of many Philippine animals facing habitat loss and the threat of extinction.''',
            'status_name': 'Critically Endangered',
            'image_file': 'visayan_warty_pig.jpg',
            'habitats': [
                {'location': 'Panay', 'habitat_type': 'Forests'},
                {'location': 'Negros', 'habitat_type': 'Forests'}
            ],
            'threats': ['Habitat loss', 'Hunting for bushmeat', 'Hybridization with domestic pigs'],
            'fun_fact': 'Males grow a distinctive mohawk-like mane during the breeding season.'
        },
        {
            'name': 'Philippine Mouse Deer',
            'scientific_name': 'Tragulus nigricans',
            'population_estimate': 'Unknown, but declining; limited to Palawan (Balabac and nearby islets)',
            'description': "The Philippine Mouse Deer, or Pilandok, is the world's smallest hoofed mammal and is native only to Palawan, especially Balabac Island. It is a shy, nocturnal animal with thin legs, a small body, and large eyes that help it move through dense vegetation. Because it lives in a very limited area, even small habitat changes greatly affect its survival. The species is threatened by illegal hunting for food and the wildlife pet trade, as well as forest clearing for agriculture and development. The Pilandok depends on undisturbed forests and feeds on leaves, fruits, and shoots, playing a role in seed dispersal. Conservation groups like the Katala Foundation and local government units work on education, rescue, and anti-poaching efforts to protect this unique species.",
            'status_name': 'Endangered',
            'image_file': 'philippine_mouse_deer.jpg',
            'habitats': [
                {'location': 'Balabac (Palawan)', 'habitat_type': 'Lowland forests'}
            ],
            'threats': ['Habitat loss', 'Illegal hunting', 'Wildlife trafficking'],
            'fun_fact': 'Despite its name, it is not a mouse — it is the world\'s smallest hoofed mammal.'
        },
        {
            'name': 'Philippine Pangolin',
            'scientific_name': 'Manis culionensis',
            'population_estimate': 'Unknown (believed to be rapidly declining due to poaching)',
            'description': "The Philippine Pangolin, or Balintong, is a shy, nocturnal mammal found only in Palawan and protected by tough keratin scales. When threatened, it curls into a ball, a strategy that works against predators but makes it easy for hunters to capture. It feeds on ants and termites using its long sticky tongue, helping control insect populations. The species is in serious danger because it is heavily targeted in the illegal wildlife trade for its meat and scales, which are wrongly believed to have medicinal value. Habitat loss from forest conversion adds to the decline. Conservation groups like the Katala Foundation work with communities, rescue confiscated pangolins, and help release them back into the wild.",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_pangolin.jpg',
            'habitats': [
                {'location': 'Palawan', 'habitat_type': 'Forests'},
                {'location': 'Palawan', 'habitat_type': 'Grasslands'}
            ],
            'threats': ['Illegal wildlife trade', 'Habitat loss', 'Poaching'],
            'fun_fact': 'Pangolins have no teeth and use a long sticky tongue to feed on ants and termites.'
        },
        {
            'name': 'Philippine Spotted Deer',
            'scientific_name': 'Rusa alfredi',
            'population_estimate': 'Fewer than 2,500 remaining in the wild',
            'description': "The Philippine Spotted Deer, or Visayan Spotted Deer, is the rarest deer species in the Philippines, easily recognized by its white spots on a dark coat that provide camouflage in forests, especially at night. It once lived across several Visayan islands but now survives only in isolated forests in Negros and Panay due to logging, slash-and-burn farming, and sugarcane plantations. With fewer forests to hide in, hunting and the illegal bushmeat trade have become major threats. Slow reproduction makes population recovery difficult. Conservation efforts include breeding programs in Negros Forest Park, international support, forest patrols, community education, and habitat restoration. The deer also plays a key ecological role by dispersing seeds, which helps regenerate forests.",
            'status_name': 'Endangered',
            'image_file': 'philippine_spotted_deer.jpg',
            'habitats': [
                {'location': 'Negros', 'habitat_type': 'Dense rainforests'},
                {'location': 'Negros', 'habitat_type': 'Grasslands'},
                {'location': 'Panay', 'habitat_type': 'Dense rainforests'},
                {'location': 'Panay', 'habitat_type': 'Grasslands'}
            ],
            'threats': ['Habitat loss', 'Illegal hunting', 'Forest conversion for agriculture'],
            'fun_fact': 'The white spots remain visible even in adults.'
        },
        {
            'name': 'Negros Bleeding-Heart Dove',
            'scientific_name': 'Gallicolumba keayi',
            'population_estimate': '70 to 400 individuals left in the wild',
            'description': "The Negros Bleeding-Heart Dove is a striking bird found only in the forests of Negros and Panay, known for the bright red patch on its chest. Unlike many doves, it stays mostly on the forest floor, feeding on fruits, seeds, and insects, while its blue, brown, and green plumage helps it blend with fallen leaves. The species is critically endangered due to extensive logging, charcoal-making, agricultural expansion, and wildlife trapping for the pet trade. Habitat fragmentation makes it hard to find food, nests, and mates, and it survives poorly in captivity. Conservation efforts focus on forest protection, habitat restoration, community education, and captive breeding to help restore populations.",
            'status_name': 'Critically Endangered',
            'image_file': 'negros_bleeding_heart_dove.jpg',
            'habitats': [
                {'location': 'Negros', 'habitat_type': 'Lowland rainforests'},
                {'location': 'Panay', 'habitat_type': 'Lowland rainforests'}
            ],
            'threats': ['Deforestation', 'Habitat fragmentation', 'Illegal trapping'],
            'fun_fact': 'Prefers walking rather than flying; it stays close to the forest floor.'
        },
        {
            'name': 'Philippine Forest Turtle',
            'scientific_name': 'Siebenrockiella leytensis',
            'population_estimate': 'Believed to be fewer than 3,000 individuals',
            'description': "The Philippine Forest Turtle (Palawan Forest Turtle) is one of the rarest and most illegally trafficked turtles in the world. It has a heart-shaped shell with deep grooves and a yellow facial stripe. This species depends on cold, clean freshwater streams shaded by dense forest and is extremely sensitive to environmental change. It was thought extinct until rediscovered in the 2000s, which unfortunately triggered illegal collection for the pet trade.",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_forest_turtle.jpg',
            'habitats': [
                {'location': 'Northern Palawan', 'habitat_type': 'Forested lowlands'},
                {'location': 'Northern Palawan', 'habitat_type': 'Limestone forests'},
                {'location': 'Northern Palawan', 'habitat_type': 'Freshwater streams'},
                {'location': 'Dumaran Island', 'habitat_type': 'Freshwater streams'}
            ],
            'threats': ['Illegal wildlife trade', 'Habitat destruction', 'Deforestation', 'Water pollution'],
            'fun_fact': 'Was once thought to be extinct until rediscovered.'
        },
        {
            'name': 'Panay Monitor Lizard',
            'scientific_name': 'Varanus mabitang',
            'population_estimate': 'Roughly 2,000–3,000 individuals',
            'description': "The Mabitang is a largely herbivorous monitor lizard endemic to Panay Island. It feeds mostly on fruits and leaves and helps disperse seeds across the forest. It is shy and depends on primary, mid- to high-elevation forests.",
            'status_name': 'Endangered',
            'image_file': 'panay_monitor_lizard.jpg',
            'habitats': [
                {'location': 'Panay Island', 'habitat_type': 'Primary forests (mid- to high-elevation)'}
            ],
            'threats': ['Deforestation', 'Poaching for bushmeat', 'Habitat fragmentation'],
            'fun_fact': 'One of the only largely fruit-eating monitor lizards in the world.'
        },
        {
            'name': 'Philippine Cockatoo',
            'scientific_name': 'Cacatua haematuropygia',
            'population_estimate': 'About 500–1,000 individuals',
            'description': "The Philippine Cockatoo, locally called Katala, is a white cockatoo with a bright red undertail patch and an expressive crest. It nests in tree cavities and is heavily targeted by the illegal pet trade; nest poaching and rapid deforestation have driven steep declines.",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_cockatoo.jpg',
            'habitats': [
                {'location': 'Palawan', 'habitat_type': 'Mangroves'},
                {'location': 'Palawan', 'habitat_type': 'Lowland forests'},
                {'location': 'Palawan', 'habitat_type': 'Riverine woodlands'}
            ],
            'threats': ['Illegal wildlife trade', 'Habitat loss', 'Logging', 'Nest poaching'],
            'fun_fact': 'One of the loudest parrots in the Philippines.'
        },
        {
            'name': 'Visayan Hornbill',
            'scientific_name': 'Rhabdotorrhinus waldeni',
            'population_estimate': 'Fewer than 1,000 individuals',
            'description': "The Visayan Hornbill (Walden's Hornbill) is a striking bird with a large casque and glossy black plumage. It survives only in small forest fragments in Negros and Panay and is crucial for seed dispersal of large fruits.",
            'status_name': 'Critically Endangered',
            'image_file': 'visayan_hornbill.jpg',
            'habitats': [
                {'location': 'Negros', 'habitat_type': 'Primary rainforests'},
                {'location': 'Panay', 'habitat_type': 'Primary rainforests'}
            ],
            'threats': ['Habitat loss', 'Hunting', 'Deforestation', 'Nest disturbance'],
            'fun_fact': 'Females seal themselves inside tree cavities while nesting.'
        },
        {
            'name': 'Sulu Hornbill',
            'scientific_name': 'Anthracoceros montani',
            'population_estimate': 'Likely fewer than 50 individuals',
            'description': "The Sulu Hornbill is one of the rarest birds in the Philippines, possibly surviving only on Tawi-Tawi. It has an all-black body and a massive pale bill and casque. Decades of habitat loss and hunting have brought it to the brink of extinction.",
            'status_name': 'Critically Endangered',
            'image_file': 'sulu_hornbill.jpg',
            'habitats': [
                {'location': 'Tawi-Tawi (Sulu Archipelago)', 'habitat_type': 'Forest patches'}
            ],
            'threats': ['Severe habitat loss', 'Illegal hunting', 'Extreme deforestation'],
            'fun_fact': 'Potentially one of the top 10 rarest birds in the world.'
        },
        {
            'name': 'Mindoro Bleeding-heart Dove',
            'scientific_name': 'Gallicolumba platenae',
            'population_estimate': 'Adults possibly under 500',
            'description': "The Mindoro Bleeding-heart Dove is a shy, ground-dwelling bird named for the red patch on its chest. It depends on undisturbed lowland and mid-elevation forests and is threatened by habitat loss and hunting.",
            'status_name': 'Critically Endangered',
            'image_file': 'mindoro_bleeding_heart_dove.jpg',
            'habitats': [
                {'location': 'Mindoro', 'habitat_type': 'Lowland forests'},
                {'location': 'Mindoro', 'habitat_type': 'Mid-elevation forests'}
            ],
            'threats': ['Habitat destruction', 'Hunting', 'Forest conversion'],
            'fun_fact': 'Red chest patch resembles a bleeding wound.'
        },
        {
            'name': 'Golden-Crowned Flying Fox',
            'scientific_name': 'Acerodon jubatus',
            'population_estimate': '10,000–20,000 individuals (declining)',
            'description': "The Golden-Crowned Flying Fox is one of the largest bat species, with a wingspan up to 1.7 m. It feeds on fruit and is vital for pollination and seed dispersal but is threatened by hunting and roost disturbance.",
            'status_name': 'Endangered',
            'image_file': 'golden_crowned_flying_fox.jpg',
            'habitats': [
                {'location': 'Luzon', 'habitat_type': 'Forest canopies'},
                {'location': 'Leyte', 'habitat_type': 'Forest canopies'},
                {'location': 'Mindanao', 'habitat_type': 'Forest canopies'}
            ],
            'threats': ['Hunting', 'Habitat loss', 'Disturbance of roosting sites'],
            'fun_fact': 'One of the world\'s biggest bats.'
        },
        {
            'name': 'Dinagat Bushy-tailed Cloud Rat',
            'scientific_name': 'Crateromys australis',
            'population_estimate': 'Unknown, extremely small',
            'description': "The Dinagat Bushy-tailed Cloud Rat is an elusive nocturnal rodent with a long, fluffy tail. Known from Dinagat Island, it was once thought possibly extinct until rediscovery. Mining and deforestation threaten its tiny range.",
            'status_name': 'Critically Endangered',
            'image_file': 'dinagat_cloud_rat.jpg',
            'habitats': [
                {'location': 'Dinagat Island', 'habitat_type': 'Mossy forests'},
                {'location': 'Dinagat Island', 'habitat_type': 'Lowland forests'}
            ],
            'threats': ['Mining', 'Deforestation', 'Limited distribution'],
            'fun_fact': 'Was thought to be possibly extinct for years.'
        },
        {
            'name': 'Northern Luzon Giant Cloud Rat',
            'scientific_name': 'Phloeomys pallidus',
            'population_estimate': 'Stable but decreasing; exact number unknown',
            'description': "A large, slow-moving rodent found in Northern Luzon forests. It is nocturnal, lives in tree hollows, and is culturally significant in some communities. Hunting and habitat loss are pressures.",
            'status_name': 'Vulnerable',
            'image_file': 'northern_luzon_giant_cloud_rat.jpg',
            'habitats': [
                {'location': 'Northern Luzon (Sierra Madre)', 'habitat_type': 'Forests'}
            ],
            'threats': ['Hunting', 'Habitat loss', 'Forest degradation'],
            'fun_fact': 'Can grow as large as a small cat.'
        },
        {
            'name': 'Southern Luzon Giant Cloud Rat',
            'scientific_name': 'Phloeomys cumingi',
            'population_estimate': 'Declining; no firm numbers',
            'description': "Similar to its northern relative but darker, this nocturnal arboreal rodent inhabits forests in Southern Luzon and relies on tree hollows for shelter.",
            'status_name': 'Vulnerable',
            'image_file': 'southern_luzon_giant_cloud_rat.jpg',
            'habitats': [
                {'location': 'Southern Luzon (Quezon, Bicol)', 'habitat_type': 'Forests'}
            ],
            'threats': ['Habitat loss', 'Hunting', 'Forest fragmentation'],
            'fun_fact': 'Important seed disperser and primarily arboreal.'
        },
        {
            'name': 'Cebu Flowerpecker',
            'scientific_name': 'Dicaeum quadricolor',
            'population_estimate': '100–200 individuals',
            'description': "The Cebu Flowerpecker is a tiny, brightly colored bird rediscovered in 1992 and surviving only in a few forest remnants in central Cebu. It depends on nectar-rich forest plants and is critically endangered due to habitat loss.",
            'status_name': 'Critically Endangered',
            'image_file': 'cebu_flowerpecker.jpg',
            'habitats': [
                {'location': 'Central Cebu (Nug-as Forest)', 'habitat_type': 'Forest remnants'}
            ],
            'threats': ['Habitat loss', 'Extremely limited forest cover'],
            'fun_fact': 'Rediscovered after being believed extinct for almost a century.'
        },
        {
            'name': 'Ilin Island Cloudrunner',
            'scientific_name': 'Crateromys paulus',
            'population_estimate': 'Unknown; possibly fewer than 50 or extinct',
            'description': "The Ilin Island Cloudrunner is known from a single specimen and may be extinct. If any survive, they face severe threats from deforestation and habitat conversion on Ilin Island.",
            'status_name': 'Critically Endangered',
            'image_file': 'ilin_island_cloudrunner.jpg',
            'habitats': [
                {'location': 'Ilin Island (south of Mindoro)', 'habitat_type': 'Forests'}
            ],
            'threats': ['Deforestation', 'Habitat destruction', 'Extremely limited range'],
            'fun_fact': 'Known from only one specimen; possibly already extinct.'
        }
    ]

    for sp in species_list:
        existing = Species.query.filter_by(name=sp['name']).first()
        if existing:
            species_obj = existing
        else:
            # Get status_id from status_name
            status = ConservationStatus.query.filter_by(status_name=sp['status_name']).first()
            if not status:
                print(f"Warning: Status '{sp['status_name']}' not found for {sp['name']}")
                continue
            
            species_obj = Species(
                name=sp['name'],
                scientific_name=sp['scientific_name'],
                population_estimate=sp['population_estimate'],
                description=sp['description'],
                status_id=status.status_id,
                image_file=sp.get('image_file', 'default_species.jpg')
            )
            db.session.add(species_obj)
            db.session.commit()

        # Habitats - now properly normalized
        for habitat_data in sp.get('habitats', []):
            location = get_or_create_location(habitat_data['location'])
            habitat_type = get_or_create_habitat_type(habitat_data['habitat_type'])
            
            existing_habitat = SpeciesHabitat.query.filter_by(
                species_id=species_obj.id,
                location_id=location.location_id,
                habitat_type_id=habitat_type.habitat_type_id
            ).first()
            
            if not existing_habitat:
                db.session.add(SpeciesHabitat(
                    species_id=species_obj.id,
                    location_id=location.location_id,
                    habitat_type_id=habitat_type.habitat_type_id
                ))

        # Threats - now properly normalized
        for threat_name in sp.get('threats', []):
            threat = get_or_create_threat(threat_name)
            
            existing_threat = SpeciesThreat.query.filter_by(
                species_id=species_obj.id,
                threat_id=threat.threat_id
            ).first()
            
            if not existing_threat:
                db.session.add(SpeciesThreat(
                    species_id=species_obj.id,
                    threat_id=threat.threat_id
                ))

        # Fun fact (only one)
        fun_fact_text = sp.get('fun_fact')
        if fun_fact_text and not SpeciesFunFact.query.filter_by(species_id=species_obj.id, fact_detail=fun_fact_text).first():
            db.session.add(SpeciesFunFact(species_id=species_obj.id, fact_detail=fun_fact_text))

    db.session.commit()
    print("Species, habitats, threats, and fun facts inserted.")

    print("3. Inserting Organizations...")
    organizations = [
        {
            'name': 'Philippine Eagle Foundation (PEF)',
            'about': "The Philippine Eagle Foundation in Davao City leads conservation programs for the country's national bird. It runs breeding, forest protection, and education projects across Mindanao.",
            'website': 'https://www.philippineeaglefoundation.org',
            'donate_link': 'https://www.philippineeaglefoundation.org/donate'
        },
        {
            'name': 'Tamaraw Conservation Program (TCP)',
            'about': "A government-led program under the Department of Environment and Natural Resources (DENR). TCP focuses on protecting Tamaraws in Mindoro through anti-poaching patrols, breeding efforts, and community education.",
            'website': 'https://denr.gov.ph/?s=tamaraw',
            'donate_link': 'https://bmb.gov.ph'
        },
        {
            'name': 'Philippine Tarsier Foundation, Inc. (PTFI)',
            'about': "Operates the Tarsier Sanctuary in Corella, Bohol; protects tarsier habitats and educates tourists on ethical viewing.",
            'website': 'http://www.tarsierfoundation.com/',
            'donate_link': 'http://www.tarsierfoundation.com/category/volunteer'
        },
        {
            'name': 'Talarak Foundation',
            'about': 'Runs breeding and rewilding programs for endangered Visayan species, restores degraded forests and operates wildlife rescue centers.',
            'website': 'https://www.talarak.org',
            'donate_link': 'https://www.talarak.org/support'
        },
        {
            'name': 'WWF Philippines',
            'about': 'Protects marine wildlife such as dugongs, sea turtles, and works on coral reef restoration and sustainable fishing.',
            'website': 'https://wwf.org.ph',
            'donate_link': 'https://support.wwf.org.ph/make-a-donation/'
        },
        {
            'name': 'Mabuwaya Foundation',
            'about': 'Community-based conservation programs for the Philippine Crocodile, focusing on habitat protection and education.',
            'website': 'https://www.mabuwaya.org',
            'donate_link': 'https://www.mabuwaya.org/index.cfm?p=0B272505-1DE0-5C8B-DF7CA43A69A2F3CE'
        },
        {
            'name': 'Marine Wildlife Watch of the Philippines (MWWP)',
            'about': 'Monitors and protects marine wildlife such as sea turtles and dugongs, coordinates strandings and rescue operations.',
            'website': 'https://www.mwwphilippines.org',
            'donate_link': 'https://mwwphilippines.org/support-contact/'
        },
        {
            'name': 'Turtle Conservation Society of the Philippines (TCSP)',
            'about': 'Network of researchers and volunteers working to conserve sea turtle nesting sites across the archipelago.',
            'website': 'https://www.wildspiritfund.org/marine-turtle-conservation-and-health/',
            'donate_link': 'https://www.wildspiritfund.org/become-a-member/'
        },
        {
            'name': 'Philippine Biodiversity Conservation Foundation Inc. (PBCFI)',
            'about': 'Conducts biodiversity research and protection programs across various ecosystems, focusing on reptiles, amphibians, and lesser-known species.',
            'website': 'https://www.philbio.org.ph/ourwork/',
            'donate_link': 'mailto:donations@philbio.org.ph'
        },
        {
            'name': 'Oceana Philippines',
            'about': 'Works to protect marine biodiversity through sustainable fishing, plastic reduction campaigns, and habitat protection.',
            'website': 'https://ph.oceana.org',
            'donate_link': 'https://ph.oceana.org/take-action/'
        }
    ]

    for org in organizations:
        existing_org = Organization.query.filter_by(name=org['name']).first()
        if not existing_org:
            db.session.add(Organization(**org))
    db.session.commit()

    supports = [
        { 'org_name': 'Philippine Eagle Foundation (PEF)', 'species_name': 'Philippine Eagle', 'support_type': 'Conservation & research' },
        { 'org_name': 'Tamaraw Conservation Program (TCP)', 'species_name': 'Tamaraw', 'support_type': 'Habitat protection' },
        { 'org_name': 'Philippine Tarsier Foundation, Inc. (PTFI)', 'species_name': 'Philippine Tarsier', 'support_type': 'Habitat protection & education' }
    ]

    for s in supports:
        org = Organization.query.filter_by(name=s['org_name']).first()
        species_obj = Species.query.filter_by(name=s['species_name']).first()
        if org and species_obj:
            exists = OrganizationSupports.query.filter_by(org_id=org.org_id, species_id=species_obj.id).first()
            if not exists:
                db.session.add(OrganizationSupports(org_id=org.org_id, species_id=species_obj.id, support_type=s['support_type']))
    db.session.commit()

    print('Organizations and support links inserted (if not present).')

    print('4. Assigning image files from static/images where available...')
    import os
    images_dir = os.path.join(app.root_path, 'static', 'images')
    updated = 0

    for sp in Species.query.all():
        if sp.image_file:
            candidate_path = os.path.join(images_dir, sp.image_file)
            if os.path.exists(candidate_path):
                continue

        base = sp.name.lower().replace(' ', '_').replace("'", '').replace("'", '')
        found = False
        for ext in ('.jpg', '.jpeg', '.png', '.svg'):
            fname = base + ext
            if os.path.exists(os.path.join(images_dir, fname)):
                sp.image_file = fname
                db.session.add(sp)
                updated += 1
                found = True
                break

    if updated:
        db.session.commit()
    print(f'Assigned image_file for {updated} species where matching files were found.')

    print('5. Inserting Help Tips...')
    help_tips = [
        {
            'title': 'Reduce Paper & Wood Waste',
            'reason': 'Less demand for paper → fewer trees cut down → more forests preserved for animals like the Philippine Eagle, Philippine Deer, and Pangolin.',
            'actions': [
                'Use both sides of paper',
                'Choose digital notes instead of printing',
                'Support products with "Recycled" or "FSC Certified" labels'
            ]
        },
        {
            'title': 'Support Responsible Farming',
            'reason': 'Slash-and-burn farming destroys forests and pushes species like Tamaraw and Warty Pig out of their habitats.',
            'actions': [
                'Buy from local farmers',
                'Choose organic/eco-friendly products',
                'Avoid buying crops linked to illegal land clearing'
            ]
        },
        {
            'title': 'Never Support Wildlife Trade',
            'reason': 'Many species become endangered because of illegal pet trade and hunting (Tarsier, Pangolin, Mouse Deer).',
            'actions': [
                'Don\'t buy exotic pets',
                'Don\'t purchase items made from animal parts (scales, feathers, shells)',
                'Report wildlife trade to DENR / PCSD'
            ]
        },
        {
            'title': 'Plant Native Trees',
            'reason': 'Trees = shelter and food for wildlife. Native trees are better because animals are adapted to them.',
            'actions': [
                'Join tree-planting drives (schools/barangay events)',
                'Choose native species (Narra, Molave, Lauan)',
                'Avoid invasive plants'
            ]
        },
        {
            'title': 'Reduce Waste',
            'reason': 'Trash → pollution → habitat degradation. Non-biodegradable waste harms land animals and clogs rivers, affecting forests.',
            'actions': [
                'Practice 3R\'s (Reduce, Reuse, Recycle)',
                'Bring reusable bags/tumblers',
                'Avoid single-use plastics'
            ]
        },
        {
            'title': 'Support Conservation Organizations',
            'reason': 'Your donations help pay for ranger patrols, rescue operations, captive breeding, and reforestation.',
            'actions': [
                'Donate (even ₱10 helps)',
                'Visit wildlife sanctuaries instead of zoos',
                'Share their work on social media'
            ]
        },
        {
            'title': 'Spread Awareness',
            'reason': 'The more people who know, the more people care.',
            'actions': [
                'Share posts about endangered animals',
                'Educate classmates and family',
                'Choose wildlife-friendly content (no selfies with wildlife)'
            ]
        }
    ]

    for tip_data in help_tips:
        existing = HelpTip.query.filter_by(title=tip_data['title']).first()
        if not existing:
            tip = HelpTip(title=tip_data['title'], reason=tip_data['reason'])
            db.session.add(tip)
            db.session.commit()
            
            # Add actions
            for action_text in tip_data['actions']:
                action = HelpTipAction(tip_id=tip.help_id, action_text=action_text)
                db.session.add(action)
            db.session.commit()
    
    print('Help tips inserted.')

    print('6. Inserting Related Articles...')
    articles = [
        {
            'title': '2,000 Philippine species critically endangered – DENR',
            'description': 'This article provides an extensive overview of the alarming number of species in the Philippines that are classified as critically endangered or vulnerable. It includes insights from government officials, highlighting the scale of biodiversity loss in the country and the urgency for conservation interventions. For anyone looking to understand the current state of Philippine wildlife, the article offers concrete data, official perspectives, and context that can support research, advocacy, or public awareness campaigns.',
            'link': 'https://www.philstar.com/nation/2025/02/22/2423268/2000-philippine-species-critically-endangered-denr',
            'category': 'General'
        },
        {
            'title': 'Study warns up to a quarter of Philippine vertebrates risk extinction',
            'description': 'This scientific study presents a detailed analysis of the risk levels faced by terrestrial vertebrates in the Philippines, indicating that between 15% and 23% are at risk of extinction. The research emphasizes the vulnerability of amphibians and mammals, groups often overlooked in conservation priorities. By highlighting species-specific threats and statistical evidence, the study provides a crucial foundation for policymakers, conservationists, and educators to design targeted protection programs and raise public awareness about the severity of the biodiversity crisis.',
            'link': 'https://news.mongabay.com/2025/10/study-warns-up-to-a-quarter-of-philippine-vertebrates-risk-extinction/',
            'category': 'Scientific'
        },
        {
            'title': 'Biodiversity on the Brink: 30% of PH land vertebrates facing extinction',
            'description': "This article synthesizes recent research findings and presents them in an accessible format for the general public. It emphasizes that nearly a third of land vertebrates in the Philippines are at high risk of extinction, underscoring the urgency for immediate conservation measures. The piece serves as a strong advocacy tool by providing context, expert commentary, and examples, making it an essential resource for understanding the broader implications of habitat loss, climate change, and human activity on Philippine biodiversity.",
            'link': 'https://newsline.ph/biodiversity-on-the-brink-30-of-ph-land-vertebrates-facing-extinction/',
            'category': 'Scientific'
        },
        {
            'title': 'Illegal wildlife trade in Sulu‑Celebes Seas calls for tripartite collaboration',
            'description': "This article sheds light on the large-scale illegal wildlife trade affecting marine and terrestrial species in Philippine waters. It provides detailed accounts of trafficking routes, species affected, and the socio-economic drivers behind this illicit activity. By highlighting the need for tripartite collaboration between government, NGOs, and local communities, it offers actionable insights into combating wildlife crime and strengthening conservation frameworks, making it highly relevant for policy advocacy, environmental planning, and educational initiatives.",
            'link': 'https://archive.wwf.org.ph/resource-center/story-archives-2023/high-wildlife-trafficking-levels-in-the-sulu-celebes-seas-call-for-tripartite-collaboration/',
            'category': 'Policy'
        },
        {
            'title': 'Save wildlife from extinction – PhilStar feature',
            'description': 'This feature article profiles several endangered species in the Philippines, such as the tamaraw, dugong, pawikan, pangolin, and Philippine cockatoo, providing both scientific and anecdotal accounts of their current status. It discusses the main threats these species face, including habitat destruction, poaching, and climate change, giving readers a comprehensive understanding of the challenges involved. The article is particularly useful for education, awareness campaigns, and storytelling purposes, as it combines factual reporting with compelling narratives that illustrate the urgency of wildlife conservation.',
            'link': 'https://qa.philstar.com/business/2024/12/20/2408559/save-wildlife-extinction',
            'category': 'General'
        },
        {
            'title': 'DENR partners with private sector to save 6 endangered PH animals from extinction',
            'description': 'This article highlights a collaborative effort between the Department of Environment and Natural Resources (DENR), private organizations, and NGOs to protect six critically endangered species in the Philippines. It provides detailed examples of joint conservation programs, including habitat restoration, species monitoring, and awareness campaigns. This resource is particularly valuable for understanding how multi-stakeholder partnerships operate in practice and can inspire similar initiatives by demonstrating effective coordination between government, civil society, and the private sector.',
            'link': 'https://mb.com.ph/2024/10/15/denr-partners-with-conservation-groups-private-sector-to-save-6-endangered-ph-animals-from-extinction',
            'category': 'Policy'
        },
        {
            'title': 'Why lesser-studied Philippine species need conservation too',
            'description': 'Based on the 2025 vertebrate extinction-risk study, this article emphasizes the importance of conserving non-charismatic species such as amphibians, small mammals, and island frogs. It explains that these species, despite being lesser-known, play critical roles in their ecosystems and are often at higher risk due to under-documentation and habitat pressures. The piece is especially useful for broadening conservation perspectives, highlighting that effective biodiversity protection requires attention to all species, not just the well-known or popular ones.',
            'link': 'https://news.mongabay.com/2025/10/study-warns-up-to-a-quarter-of-philippine-vertebrates-risk-extinction/',
            'category': 'Scientific'
        },
        {
            'title': 'The Philippines ecosystem: endangered species in the Philippines — causes and threats',
            'description': 'This comprehensive overview examines the biodiversity status in the Philippines, detailing the number of threatened species, main ecosystems, and the range of threats to both terrestrial and marine life. It provides background context for anyone seeking to understand why conservation is critical, linking habitat loss, poaching, and climate change to the decline of Philippine wildlife. The article is an excellent foundational resource for research, educational content, and advocacy, offering both statistical data and narrative explanation of the challenges facing the countrys ecosystems.',
            'link': 'https://www.futurelearn.com/info/futurelearn-international/endangered-species-philippines',
            'category': 'General'
        },
        {
            'title': 'Technology-Driven Biodiversity Conservation in the Philippines',
            'description': 'This piece explains how modern technologies like drones, satellite imaging, and AI-assisted monitoring are helping track wildlife populations and illegal activities. Conservation groups in the Philippines increasingly rely on tech tools for mapping and data collection. The article shows that innovation is becoming essential to protecting endangered ecosystems.',
            'link': 'https://mb.com.ph/2024/5/2/technology-driven-biodiversity-conservation',
            'category': 'Scientific'
        },
        {
            'title': 'Understanding Endangered Species in the Philippines',
            'description': 'This article gives an overview of why many species in the Philippines are endangered, from deforestation to pollution to illegal wildlife trade. It explains basic conservation concepts in simple terms. It\'s designed to help beginners understand the country\'s biodiversity crisis.',
            'link': 'https://www.futurelearn.com/info/futurelearn-international/endangered-species-philippines',
            'category': 'Scientific'
        },
        {
            'title': 'Deforestation & Mining Threats in Mindanao Biodiversity Hotspots',
            'description': 'Mining expansions and logging operations are rapidly eating away at Mindanao\'s remaining forest ecosystems. The article explains how these activities endanger species that rely on undisturbed habitats. It calls for stricter environmental regulations and more sustainable land use planning.',
            'link': 'https://www.rappler.com/environment/57367-illegal-logging-hotspots-reduced/',
            'category': 'General'
        }
    ]

    for article in articles:
        existing = RelatedArticle.query.filter_by(title=article['title']).first()
        if not existing:
            db.session.add(RelatedArticle(**article))
    db.session.commit()
    print('Related articles inserted.')

    print('7. Inserting News Items...')
    news_items = [
        {
            'title': 'Department of Environment and Natural Resources (DENR) & SM Supermalls collaborate to save critically endangered PH species',
            'summary': "This initiative highlights a joint conservation program targeting several critically endangered species — including forest and land animals like Tamaraw, Philippine Eagle, and Palawan Pangolin. The campaign uses SM's retail and fundraising network to raise awareness and funds for habitat protection, anti-poaching, and species recovery efforts.",
            'link': 'https://www.pna.gov.ph/articles/1239874',
            'category': 'Success Story',
            'published_date': date(2024, 12, 12)
        },
        {
            'title': 'Updated population status of Tamaraw — still critically endangered but conservation efforts continuing',
            'summary': 'According to a 2025 report, only about 500–600 Tamaraw remain in the wild, found in select habitats such as mountain sanctuaries in Mindoro. The government allocated a PHP 100‑million biodiversity budget (2024) to support conservation of Tamaraw among other threatened species, aiming to strengthen patrols and habitat protection programs.',
            'link': 'https://www.philstar.com/headlines/2025/04/08/2434337/tamaraw-remains-one-critically-endangered-species',
            'category': 'Update',
            'published_date': date(2025, 4, 8)
        },
        {
            'title': 'Nationwide "Save from Extinction" campaign launched to protect six flagship endangered species',
            'summary': 'In late 2024 the DENR, private sector, and NGOs initiated a campaign to raise funds and public support for critically endangered species in the Philippines. The campaign emphasizes forest‑dwelling animals and land species (e.g. Philippine Eagle, Tamaraw, Pangolin, Cockatoo) — supporting habitat protection, anti-trafficking, and research through donations and awareness drives.',
            'link': 'https://mb.com.ph/2024/10/15/denr-partners-with-conservation-groups-private-sector-to-save-6-endangered-ph-animals-from-extinction',
            'category': 'Alert',
            'published_date': date(2024, 10, 15)
        },
        {
            'title': 'Government & NGOs formal agreement to protect land species including Philippine Eagle, Tamaraw, Pangolin and Cockatoo',
            'summary': 'In 2024 a memorandum of agreement (MOA) was signed among the DENR, private sector, and conservation groups to safeguard several endangered land species native to the Philippines. This formal alliance aims to coordinate habitat protection, anti-poaching enforcement, community engagement, and species‑specific conservation measures — reflecting a structured national effort.',
            'link': 'https://www.pna.gov.ph/index.php/articles/1235590',
            'category': 'Success Story',
            'published_date': date(2024, 10, 15)
        },
        {
            'title': 'Recognition that up to 2,000 species — including many endemic — are critically endangered or vulnerable in the Philippines',
            'summary': 'A 2025 announcement by DENR highlighted that thousands of flora and fauna species are at risk, primarily due to habitat destruction, land use change, climate impacts, and human activity. This serves as a broad wake‑up call about terrestrial biodiversity loss — underlining why land‑focused conservation and ecosystem protection are urgent.',
            'link': 'https://www.philstar.com/nation/2025/02/22/2423268/2000-philippine-species-critically-endangered-denr',
            'category': 'Alert',
            'published_date': date(2025, 2, 22)
        },
        {
            'title': 'Growing awareness in media & public of biodiversity loss and need for habitat protection (feature on endangered Philippine species)',
            'summary': 'A media feature emphasizes that species like Philippine Eagle, Tamaraw, Palawan Pangolin, and forest‑dependent birds are "umbrella species," meaning their protection safeguards entire ecosystems. The article calls for stronger conservation laws, habitat protection, and public support — showing that public awareness is becoming part of the conservation strategy.',
            'link': 'https://qa.philstar.com/business/2024/12/20/2408559/save-wildlife-extinction',
            'category': 'Alert',
            'published_date': date(2024, 12, 20)
        },
        {
            'title': 'Call to Help Protect PH Endangered Species — ABS-CBN Feature',
            'summary': "ABS-CBN's feature emphasizes ongoing threats to species such as the Philippine eagle, tamaraw, and tarsier. It encourages viewers to participate in conservation activities and support programs. The article highlights how media plays a powerful role in raising awareness.",
            'link': 'https://www.abs-cbn.com/news/business/2024/12/20/help-safeguard-ph-s-endangered-species-1708',
            'category': 'Alert',
            'published_date': date(2024, 12, 20)
        },
        {
            'title': 'PH hosts landmark global meeting on migratory waterbird conservation',
            'summary': 'Talarak Foundation, in collaboration with international zoos, releases a second group of captive-bred Visayan Warty Pigs into restored forest habitats in Panay. The reintroduction aims to strengthen genetic diversity in wild populations.',
            'link': 'https://www.talarak.org/',
            'category': 'Success Story',
            'published_date': date(2025, 11, 10)
        },
        {
            'title': 'Palawan Hornbill finds new hope after first successful breeding in captivity',
            'summary': 'First successful captive breeding of the endangered Palawan hornbill — a concrete win for conservation efforts in Palawan.',
            'link': 'https://www.gmanetwork.com/regionaltv/features/111118/palawan-hornbill-finds-new-hope-after-first-successful-breeding-in-captivity/story/',
            'category': 'Success Story',
            'published_date': date(2025, 11, 2)
        },
        {
            'title': 'Campaign to raise ₱100M to save Philippine endangered species from extinction',
            'summary': 'SM and the Department of Environment and Natural Resources (DENR), with BDO Unibank Inc. (BDO) as a major partner, launched the "Save from Extinction" campaign in October 2024 to protect endangered species in the Philippines.',
            'link': 'https://www.philstar.com/lifestyle/pet-life/2025/08/04/2462402/campaign-raise-p100m-save-philippine-endangered-species-extinction/amp',
            'category': 'Success Story',
            'published_date': date(2025, 8, 4)
        },
        {
            'title': 'Biodiversity on the Brink: 30% of PH land vertebrates facing extinction',
            'summary': 'A recent study by University of Southern Mindanao researchers, published in Science of the Total Environment, warns that the Philippines is on the brink of a major biodiversity crisis.',
            'link': 'https://newsline.ph/biodiversity-on-the-brink-30-of-ph-land-vertebrates-facing-extinction/',
            'category': 'Alert',
            'published_date': date(2025, 10, 9)
        }
    ]
    
    for news in news_items:
        existing = News.query.filter_by(title=news['title']).first()
        if not existing:
            db.session.add(News(**news))
    db.session.commit()
    print('News items inserted.')

print('--- Data Insertion Complete ---')
