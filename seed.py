# seed.py
from app import app
from models import db, ConservationStatus, Species, SpeciesHabitat, SpeciesThreat, SpeciesFunFact, Organization, OrganizationSupports, HelpTip, RelatedArticle, News
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
        if not ConservationStatus.query.get(data['status_name']):
            db.session.add(ConservationStatus(**data))
    db.session.commit()
    print("Conservation statuses inserted.")

    print("2. Inserting Species...")
    species_list = [
        {
            'name': 'Philippine Eagle',
            'scientific_name': 'Pithecophaga jefferyi',
            'population_estimate': 'Around 400–500 left in the wild',
            'description': """The Philippine Eagle, the country's national bird, is a powerful raptor found only in the Philippines and depends on large, untouched dipterocarp forests. Known for its shaggy crest and strong talons, it hunts animals like flying lemurs, macaques, civets, and reptiles. Although once called the "Monkey-Eating Eagle," monkeys are only part of its diet. The species recovers slowly because a breeding pair lays just one egg about every two years and spends months caring for the chick. Massive deforestation from logging, land conversion, and mining has destroyed much of its habitat, and hunting still happens. Conservation groups, including the Philippine Eagle Foundation, work on rescue, captive breeding, and education to protect the species and its nesting sites.""",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_eagle.jpg',
            'habitats': ['Dense mountain forests in Mindanao, Luzon, Leyte, Samar'],
            'threats': ['Deforestation, Illegal hunting, Habitat loss'],
            'fun_fact': 'Known as the "Monkey-Eating Eagle"; has a wingspan of about 2 meters and may live up to 60 years in captivity.'
        },
        {
            'name': 'Tamaraw',
            'scientific_name': 'Bubalus mindorensis',
            'population_estimate': 'About 400 individuals remaining in the wild',
            'description': """The Tamaraw is a rare dwarf buffalo native only to Mindoro and is known for its small, stocky build and V-shaped horns. Its once wide range shrank because of heavy hunting, habitat destruction, and diseases from domestic cattle. With females giving birth only every two years, population growth remains slow. Conservation programs led by the DENR, including anti-poaching patrols, monitoring, and protected-area management, have helped some groups recover, though illegal hunting and continuing habitat loss remain serious challenges.""",
            'status_name': 'Critically Endangered',
            'image_file': 'tamaraw.jpg',
            'habitats': ['Mountain forests, Grasslands of Mindoro Island'],
            'threats': ['Habitat loss, Hunting/poaching, Disease transmitted by domestic cattle'],
            'fun_fact': 'Found nowhere else on Earth; has V-shaped horns and is more solitary than domestic water buffalo.'
        },
        {
            'name': 'Philippine Tarsier',
            'scientific_name': 'Carlito syrichta',
            'population_estimate': 'Unknown, but declining — believed to be a few thousand in scattered islands',
            'description': """The Philippine Tarsier is one of the smallest primates in the world and is notable for its very large round eyes — each roughly the size of its brain — which provide excellent night vision. It is nocturnal and insectivorous, able to leap several meters between branches using powerful hind legs. Tarsiers require dense, quiet forest habitat and are extremely sensitive to handling and noise, so responsible ecotourism and protected sanctuaries are critical for their survival. Threats include habitat loss, the illegal pet trade and disturbance from tourism; stressed tarsiers may injure themselves or stop feeding. Local sanctuaries and community-led conservation programs provide safe areas and education to reduce harmful interactions.""",
            'status_name': 'Near Threatened',
            'image_file': 'philippine_tarsier.jpg',
            'habitats': ['Forests of Bohol, Leyte, Samar, parts of Mindanao'],
            'threats': ['Habitat loss, Illegal pet trade, Tourism disturbance'],
            'fun_fact': 'Eyes are as large as its brain; can leap up to 3 meters; completely insectivorous.'
        }
    ]

    # Additional species
    additional_species = [
        {
            'name': 'Visayan Warty Pig',
            'scientific_name': 'Sus cebifrons',
            'population_estimate': 'Fewer than 200 individuals remaining in the wild',
            'description': '''The Visayan Warty Pig is a rare wild pig found only in the Philippines, known for the facial "warts" that protect it during fights and the long, mohawk-like mane grown by males during breeding season. Once widespread in the Visayas, its population dropped sharply after more than 95% of forests in Negros and Panay were cleared for farming and settlements. With less forest cover, the pigs are more easily hunted, and many now mix with domestic pigs, causing genetic loss. Conservation efforts include captive-breeding programs in local and international zoos, along with community awareness campaigns. The species highlights the wider struggle of many Philippine animals facing habitat loss and the threat of extinction.''',
            'status_name': 'Critically Endangered',
            'image_file': 'visayan_warty_pig.jpg',
            'habitats': ['Forests of Panay, Forests of Negros'],
            'threats': ['Habitat loss, Hunting for bushmeat, Hybridization with domestic pigs'],
            'fun_fact': 'Males grow a distinctive mohawk-like mane during the breeding season.'
        },
        {
            'name': 'Philippine Mouse Deer',
            'scientific_name': 'Tragulus nigricans',
            'population_estimate': 'Unknown, but declining; limited to Palawan (Balabac and nearby islets)',
            'description': "The Philippine Mouse Deer, or Pilandok, is the world's smallest hoofed mammal and is native only to Palawan, especially Balabac Island. It is a shy, nocturnal animal with thin legs, a small body, and large eyes that help it move through dense vegetation. Because it lives in a very limited area, even small habitat changes greatly affect its survival. The species is threatened by illegal hunting for food and the wildlife pet trade, as well as forest clearing for agriculture and development. The Pilandok depends on undisturbed forests and feeds on leaves, fruits, and shoots, playing a role in seed dispersal. Conservation groups like the Katala Foundation and local government units work on education, rescue, and anti-poaching efforts to protect this unique species.",
            'status_name': 'Endangered',
            'image_file': 'philippine_mouse_deer.jpg',
            'habitats': ['Lowland forests of Balabac and nearby islets (Palawan)'],
            'threats': ['Habitat loss, Illegal hunting, Wildlife trafficking'],
            'fun_fact': 'Despite its name, it is not a mouse — it is the worlds smallest hoofed mammal.'
        },
        {
            'name': 'Philippine Pangolin',
            'scientific_name': 'Manis culionensis',
            'population_estimate': 'Unknown (believed to be rapidly declining due to poaching)',
            'description': "The Philippine Pangolin, or Balintong, is a shy, nocturnal mammal found only in Palawan and protected by tough keratin scales. When threatened, it curls into a ball, a strategy that works against predators but makes it easy for hunters to capture. It feeds on ants and termites using its long sticky tongue, helping control insect populations. The species is in serious danger because it is heavily targeted in the illegal wildlife trade for its meat and scales, which are wrongly believed to have medicinal value. Habitat loss from forest conversion adds to the decline. Conservation groups like the Katala Foundation work with communities, rescue confiscated pangolins, and help release them back into the wild.",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_pangolin.jpg',
            'habitats': ['Forests and grasslands of Palawan'],
            'threats': ['Illegal wildlife trade, Habitat loss, Poaching'],
            'fun_fact': 'Pangolins have no teeth and use a long sticky tongue to feed on ants and termites.'
        },
        {
            'name': 'Philippine Spotted Deer',
            'scientific_name': 'Rusa alfredi',
            'population_estimate': 'Fewer than 2,500 remaining in the wild',
            'description': "The Philippine Spotted Deer, or Visayan Spotted Deer, is the rarest deer species in the Philippines, easily recognized by its white spots on a dark coat that provide camouflage in forests, especially at night. It once lived across several Visayan islands but now survives only in isolated forests in Negros and Panay due to logging, slash-and-burn farming, and sugarcane plantations. With fewer forests to hide in, hunting and the illegal bushmeat trade have become major threats. Slow reproduction makes population recovery difficult. Conservation efforts include breeding programs in Negros Forest Park, international support, forest patrols, community education, and habitat restoration. The deer also plays a key ecological role by dispersing seeds, which helps regenerate forests.",
            'status_name': 'Endangered',
            'image_file': 'philippine_spotted_deer.jpg',
            'habitats': ['Dense rainforests and grasslands of Negros and Panay'],
            'threats': ['Habitat loss, Illegal hunting, Forest conversion for agriculture'],
            'fun_fact': 'The white spots remain visible even in adults.'
        },
        {
            'name': 'Negros Bleeding-Heart Dove',
            'scientific_name': 'Gallicolumba keayi',
            'population_estimate': '70 to 400 individuals left in the wild',
            'description': "The Negros Bleeding-Heart Dove is a striking bird found only in the forests of Negros and Panay, known for the bright red patch on its chest. Unlike many doves, it stays mostly on the forest floor, feeding on fruits, seeds, and insects, while its blue, brown, and green plumage helps it blend with fallen leaves. The species is critically endangered due to extensive logging, charcoal-making, agricultural expansion, and wildlife trapping for the pet trade. Habitat fragmentation makes it hard to find food, nests, and mates, and it survives poorly in captivity. Conservation efforts focus on forest protection, habitat restoration, community education, and captive breeding to help restore populations.",
            'status_name': 'Critically Endangered',
            'image_file': 'negros_bleeding_heart_dove.jpg',
            'habitats': ['Lowland rainforests of Negros and Panay'],
            'threats': ['Deforestation, Habitat fragmentation, Illegal trapping'],
            'fun_fact': 'Prefers walking rather than flying; it stays close to the forest floor.'
        }
        ,
        {
            'name': 'Philippine Forest Turtle',
            'scientific_name': 'Siebenrockiella leytensis',
            'population_estimate': 'Believed to be fewer than 3,000 individuals',
            'description': "The Philippine Forest Turtle (Palawan Forest Turtle) is one of the rarest and most illegally trafficked turtles in the world. It has a heart-shaped shell with deep grooves and a yellow facial stripe. This species depends on cold, clean freshwater streams shaded by dense forest and is extremely sensitive to environmental change. It was thought extinct until rediscovered in the 2000s, which unfortunately triggered illegal collection for the pet trade.",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_forest_turtle.jpg',
            'habitats': ['Forested lowlands, limestone forests, freshwater streams in northern Palawan and Dumaran Island'],
            'threats': ['Illegal wildlife trade, Habitat destruction, Deforestation, Water pollution'],
            'fun_fact': 'Was once thought to be extinct until rediscovered.'
        },
        {
            'name': 'Panay Monitor Lizard (Mabitang)',
            'scientific_name': 'Varanus mabitang',
            'population_estimate': 'Roughly 2,000–3,000 individuals',
            'description': "The Mabitang is a largely herbivorous monitor lizard endemic to Panay Island. It feeds mostly on fruits and leaves and helps disperse seeds across the forest. It is shy and depends on primary, mid- to high-elevation forests.",
            'status_name': 'Endangered',
            'image_file': 'panay_monitor_lizard.jpg',
            'habitats': ['Primary forests of Panay Island (mid- to high-elevation zones)'],
            'threats': ['Deforestation, Poaching for bushmeat, Habitat fragmentation'],
            'fun_fact': 'One of the only largely fruit-eating monitor lizards in the world.'
        },
        {
            'name': 'Philippine Cockatoo (Katala)',
            'scientific_name': 'Cacatua haematuropygia',
            'population_estimate': 'About 500–1,000 individuals',
            'description': "The Philippine Cockatoo, locally called Katala, is a white cockatoo with a bright red undertail patch and an expressive crest. It nests in tree cavities and is heavily targeted by the illegal pet trade; nest poaching and rapid deforestation have driven steep declines.",
            'status_name': 'Critically Endangered',
            'image_file': 'philippine_cockatoo.jpg',
            'habitats': ['Mangroves, lowland forests and riverine woodlands in Palawan'],
            'threats': ['Illegal wildlife trade, Habitat loss, Logging, Nest poaching'],
            'fun_fact': 'One of the loudest parrots in the Philippines.'
        },
        {
            'name': 'Visayan Hornbill',
            'scientific_name': 'Rhabdotorrhinus waldeni',
            'population_estimate': 'Fewer than 1,000 individuals',
            'description': "The Visayan Hornbill (Walden’s Hornbill) is a striking bird with a large casque and glossy black plumage. It survives only in small forest fragments in Negros and Panay and is crucial for seed dispersal of large fruits.",
            'status_name': 'Critically Endangered',
            'image_file': 'visayan_hornbill.jpg',
            'habitats': ['Primary rainforests of Negros and Panay'],
            'threats': ['Habitat loss, Hunting, Deforestation, Nest disturbance'],
            'fun_fact': 'Females seal themselves inside tree cavities while nesting.'
        },
        {
            'name': 'Sulu Hornbill',
            'scientific_name': 'Anthracoceros montani',
            'population_estimate': 'Likely fewer than 50 individuals',
            'description': "The Sulu Hornbill is one of the rarest birds in the Philippines, possibly surviving only on Tawi-Tawi. It has an all-black body and a massive pale bill and casque. Decades of habitat loss and hunting have brought it to the brink of extinction.",
            'status_name': 'Critically Endangered',
            'image_file': 'sulu_hornbill.jpg',
            'habitats': ['Remaining forest patches in the Sulu Archipelago (Tawi-Tawi)'],
            'threats': ['Severe habitat loss, Illegal hunting, Extreme deforestation'],
            'fun_fact': 'Potentially one of the top 10 rarest birds in the world.'
        },
        {
            'name': 'Mindoro Bleeding-heart Dove',
            'scientific_name': 'Gallicolumba platenae',
            'population_estimate': 'Adults possibly under 500',
            'description': "The Mindoro Bleeding-heart Dove is a shy, ground-dwelling bird named for the red patch on its chest. It depends on undisturbed lowland and mid-elevation forests and is threatened by habitat loss and hunting.",
            'status_name': 'Critically Endangered',
            'image_file': 'mindoro_bleeding_heart_dove.jpg',
            'habitats': ['Lowland and mid-elevation forests of Mindoro'],
            'threats': ['Habitat destruction, Hunting, Forest conversion'],
            'fun_fact': 'Red chest patch resembles a bleeding wound.'
        },
        {
            'name': 'Golden-Crowned Flying Fox',
            'scientific_name': 'Acerodon jubatus',
            'population_estimate': '10,000–20,000 individuals (declining)',
            'description': "The Golden-Crowned Flying Fox is one of the largest bat species, with a wingspan up to 1.7 m. It feeds on fruit and is vital for pollination and seed dispersal but is threatened by hunting and roost disturbance.",
            'status_name': 'Endangered',
            'image_file': 'golden_crowned_flying_fox.jpg',
            'habitats': ['Forest canopies of Luzon, Leyte, Mindanao, and nearby islands'],
            'threats': ['Hunting, Habitat loss, Disturbance of roosting sites'],
            'fun_fact': 'One of the world\'s biggest bats.'
        },
        {
            'name': 'Dinagat Bushy-tailed Cloud Rat',
            'scientific_name': 'Crateromys australis',
            'population_estimate': 'Unknown, extremely small',
            'description': "The Dinagat Bushy-tailed Cloud Rat is an elusive nocturnal rodent with a long, fluffy tail. Known from Dinagat Island, it was once thought possibly extinct until rediscovery. Mining and deforestation threaten its tiny range.",
            'status_name': 'Critically Endangered',
            'image_file': 'dinagat_cloud_rat.jpg',
            'habitats': ['Mossy and lowland forests of Dinagat Island'],
            'threats': ['Mining, Deforestation, Limited distribution'],
            'fun_fact': 'Was thought to be possibly extinct for years.'
        },
        {
            'name': 'Northern Luzon Giant Cloud Rat',
            'scientific_name': 'Phloeomys pallidus',
            'population_estimate': 'Stable but decreasing; exact number unknown',
            'description': "A large, slow-moving rodent found in Northern Luzon forests. It is nocturnal, lives in tree hollows, and is culturally significant in some communities. Hunting and habitat loss are pressures.",
            'status_name': 'Vulnerable',
            'image_file': 'northern_luzon_giant_cloud_rat.jpg',
            'habitats': ['Forests of Northern Luzon including the Sierra Madre'],
            'threats': ['Hunting, Habitat loss, Forest degradation'],
            'fun_fact': 'Can grow as large as a small cat.'
        },
        {
            'name': 'Southern Luzon Giant Cloud Rat',
            'scientific_name': 'Phloeomys cumingi',
            'population_estimate': 'Declining; no firm numbers',
            'description': "Similar to its northern relative but darker, this nocturnal arboreal rodent inhabits forests in Southern Luzon and relies on tree hollows for shelter.",
            'status_name': 'Vulnerable',
            'image_file': 'southern_luzon_giant_cloud_rat.jpg',
            'habitats': ['Forests of Southern Luzon (Quezon, Bicol, nearby provinces)'],
            'threats': ['Habitat loss, Hunting, Forest fragmentation'],
            'fun_fact': 'Important seed disperser and primarily arboreal.'
        },
        {
            'name': 'Cebu Flowerpecker',
            'scientific_name': 'Dicaeum quadricolor',
            'population_estimate': '100–200 individuals',
            'description': "The Cebu Flowerpecker is a tiny, brightly colored bird rediscovered in 1992 and surviving only in a few forest remnants in central Cebu. It depends on nectar-rich forest plants and is critically endangered due to habitat loss.",
            'status_name': 'Critically Endangered',
            'image_file': 'cebu_flowerpecker.jpg',
            'habitats': ['Forest remnants of Central Cebu (Nug-as Forest)'],
            'threats': ['Habitat loss, Extremely limited forest cover'],
            'fun_fact': 'Rediscovered after being believed extinct for almost a century.'
        },
        {
            'name': 'Ilin Island Cloudrunner',
            'scientific_name': 'Crateromys paulus',
            'population_estimate': 'Unknown; possibly fewer than 50 or extinct',
            'description': "The Ilin Island Cloudrunner is known from a single specimen and may be extinct. If any survive, they face severe threats from deforestation and habitat conversion on Ilin Island.",
            'status_name': 'Critically Endangered / Possibly Extinct',
            'image_file': 'ilin_island_cloudrunner.jpg',
            'habitats': ['Forests of Ilin Island, south of Mindoro'],
            'threats': ['Deforestation, Habitat destruction, Extremely limited range'],
            'fun_fact': 'Known from only one specimen; possibly already extinct.'
        }
    ]

    species_list.extend(additional_species)

    for sp in species_list:
        existing = Species.query.filter_by(name=sp['name']).first()
        if existing:
            species_obj = existing
        else:
            species_obj = Species(
                name=sp['name'],
                scientific_name=sp['scientific_name'],
                population_estimate=sp['population_estimate'],
                description=sp['description'],
                status_name=sp['status_name'],
                image_file=sp.get('image_file', 'default_species.jpg')
            )
            db.session.add(species_obj)
            db.session.commit()

        # Habitats
        for habitat in sp.get('habitats', []):
            if not SpeciesHabitat.query.filter_by(species_id=species_obj.id, habitat_location=habitat).first():
                db.session.add(SpeciesHabitat(species_id=species_obj.id, habitat_location=habitat))

        # Threats
        for threat in sp.get('threats', []):
            if not SpeciesThreat.query.filter_by(species_id=species_obj.id, threat_name=threat).first():
                db.session.add(SpeciesThreat(species_id=species_obj.id, threat_name=threat))

        # Fun fact (only one)
        fun_fact_text = sp.get('fun_fact')
        if fun_fact_text and not SpeciesFunFact.query.filter_by(species_id=species_obj.id, fact_detail=fun_fact_text).first():
            db.session.add(SpeciesFunFact(species_id=species_obj.id, fact_detail=fun_fact_text))

    db.session.commit()
    print("Species and related data inserted.") 