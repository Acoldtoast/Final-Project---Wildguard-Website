-- seed.sql (full normalized - corrected for SQLite)
PRAGMA foreign_keys = ON;

-- 1) Conservation statuses
INSERT INTO conservation_status (status_id, status_name, description) VALUES
(1, 'Critically Endangered', 'Species facing an extremely high risk of extinction in the wild.'),
(2, 'Endangered', 'Species facing a very high risk of extinction in the wild.'),
(3, 'Vulnerable', 'Species facing a high risk of extinction in the wild.'),
(4, 'Near Threatened', 'Species that may be considered threatened in the near future.');

-- 2) Locations (unique location names)
INSERT INTO location (location_name) VALUES
('Mindanao'),('Luzon'),('Leyte'),('Samar'),('Mindoro Island'),('Bohol'),('Panay'),('Negros'),('Balabac (Palawan)'),('Palawan'),('Northern Palawan'),('Dumaran Island'),('Panay Island'),('Tawi-Tawi (Sulu Archipelago)'),('Mindoro'),('Dinagat Island'),('Northern Luzon (Sierra Madre)'),('Southern Luzon (Quezon, Bicol)'),('Central Cebu (Nug-as Forest)'),('Ilin Island (south of Mindoro)');

-- 3) Habitat types (unique habitat names)
INSERT INTO habitat_type (habitat_name) VALUES
('Dense mountain forests'),('Mountain forests'),('Grasslands'),('Forests'),('Lowland forests'),('Dense rainforests'),('Lowland rainforests'),('Forested lowlands'),('Limestone forests'),('Freshwater streams'),('Primary forests (mid- to high-elevation)'),('Mangroves'),('Riverine woodlands'),('Primary rainforests'),('Forest patches'),('Mid-elevation forests'),('Forest canopies'),('Mossy forests'),('Forest remnants');

-- 4) Threats (complete list - FIXED)
INSERT INTO threat (threat_name) VALUES
('Deforestation'),
('Illegal hunting'),
('Habitat loss'),
('Hunting/poaching'),
('Disease transmitted by domestic cattle'),
('Illegal pet trade'),
('Tourism disturbance'),
('Hunting for bushmeat'),
('Hybridization with domestic pigs'),
('Wildlife trafficking'),
('Illegal wildlife trade'),
('Poaching'),
('Forest conversion for agriculture'),
('Habitat fragmentation'),
('Illegal trapping'),
('Habitat destruction'),
('Water pollution'),
('Poaching for bushmeat'),
('Logging'),
('Nest poaching'),
('Hunting'),
('Nest disturbance'),
('Severe habitat loss'),
('Extreme deforestation'),
('Forest conversion'),
('Disturbance of roosting sites'),
('Mining'),
('Limited distribution'),
('Forest degradation'),
('Forest fragmentation'),
('Extremely limited forest cover'),
('Extremely limited range');

-- 5) Species (20 entries)
INSERT INTO species (id, name, scientific_name, population_estimate, description, image_file, status_id) VALUES
(1, 'Philippine Eagle', 'Pithecophaga jefferyi', 'Around 400–500 left in the wild', 'The Philippine Eagle, the country''s national bird, is a powerful raptor found only in the Philippines and depends on large, untouched dipterocarp forests. Known for its shaggy crest and strong talons, it hunts animals like flying lemurs, macaques, civets, and reptiles. Although once called the "Monkey-Eating Eagle," monkeys are only part of its diet. The species recovers slowly because a breeding pair lays just one egg about every two years and spends months caring for the chick. Massive deforestation from logging, land conversion, and mining has destroyed much of its habitat, and hunting still happens. Conservation groups, including the Philippine Eagle Foundation, work on rescue, captive breeding, and education to protect the species and its nesting sites.', 'philippine_eagle.jpg', 1),
(2, 'Tamaraw', 'Bubalus mindorensis', 'About 400 individuals remaining in the wild', 'The Tamaraw is a rare dwarf buffalo native only to Mindoro and is known for its small, stocky build and V-shaped horns. Its once wide range shrank because of heavy hunting, habitat destruction, and diseases from domestic cattle. With females giving birth only every two years, population growth remains slow. Conservation programs led by the DENR, including anti-poaching patrols, monitoring, and protected-area management, have helped some groups recover, though illegal hunting and continuing habitat loss remain serious challenges.', 'tamaraw.jpg', 1),
(3, 'Philippine Tarsier', 'Carlito syrichta', 'Unknown, but declining — believed to be a few thousand in scattered islands', 'The Philippine Tarsier is one of the smallest primates in the world and is notable for its very large round eyes — each roughly the size of its brain — which provide excellent night vision. It is nocturnal and insectivorous, able to leap several meters between branches using powerful hind legs. Tarsiers require dense, quiet forest habitat and are extremely sensitive to handling and noise, so responsible ecotourism and protected sanctuaries are critical for their survival. Threats include habitat loss, the illegal pet trade and disturbance from tourism; stressed tarsiers may injure themselves or stop feeding. Local sanctuaries and community-led conservation programs provide safe areas and education to reduce harmful interactions.', 'philippine_tarsier.jpg', 4),
(4, 'Visayan Warty Pig', 'Sus cebifrons', 'Fewer than 200 individuals remaining in the wild', 'The Visayan Warty Pig is a rare wild pig found only in the Philippines, known for the facial "warts" that protect it during fights and the long, mohawk-like mane grown by males during breeding season. Once widespread in the Visayas, its population dropped sharply after more than 95% of forests in Negros and Panay were cleared for farming and settlements. With less forest cover, the pigs are more easily hunted, and many now mix with domestic pigs, causing genetic loss. Conservation efforts include captive-breeding programs in local and international zoos, along with community awareness campaigns. The species highlights the wider struggle of many Philippine animals facing habitat loss and the threat of extinction.', 'visayan_warty_pig.jpg', 1),
(5, 'Philippine Mouse Deer', 'Tragulus nigricans', 'Unknown, but declining; limited to Palawan (Balabac and nearby islets)', 'The Philippine Mouse Deer, or Pilandok, is the world''s smallest hoofed mammal and is native only to Palawan, especially Balabac Island. It is a shy, nocturnal animal with thin legs, a small body, and large eyes that help it move through dense vegetation. Because it lives in a very limited area, even small habitat changes greatly affect its survival. The species is threatened by illegal hunting for food and the wildlife pet trade, as well as forest clearing for agriculture and development. The Pilandok depends on undisturbed forests and feeds on leaves, fruits, and shoots, playing a role in seed dispersal. Conservation groups like the Katala Foundation and local government units work on education, rescue, and anti-poaching efforts to protect this unique species.', 'philippine_mouse_deer.jpg', 2),
(6, 'Philippine Pangolin', 'Manis culionensis', 'Unknown (believed to be rapidly declining due to poaching)', 'The Philippine Pangolin, or Balintong, is a shy, nocturnal mammal found only in Palawan and protected by tough keratin scales. When threatened, it curls into a ball, a strategy that works against predators but makes it easy for hunters to capture. It feeds on ants and termites using its long sticky tongue, helping control insect populations. The species is in serious danger because it is heavily targeted in the illegal wildlife trade for its meat and scales, which are wrongly believed to have medicinal value. Habitat loss from forest conversion adds to the decline. Conservation groups like the Katala Foundation work with communities, rescue confiscated pangolins, and help release them back into the wild.', 'philippine_pangolin.jpg', 1),
(7, 'Philippine Spotted Deer', 'Rusa alfredi', 'Fewer than 2,500 remaining in the wild', 'The Philippine Spotted Deer, or Visayan Spotted Deer, is the rarest deer species in the Philippines, easily recognized by its white spots on a dark coat that provide camouflage in forests, especially at night. It once lived across several Visayan islands but now survives only in isolated forests in Negros and Panay due to logging, slash-and-burn farming, and sugarcane plantations. With fewer forests to hide in, hunting and the illegal bushmeat trade have become major threats. Slow reproduction makes population recovery difficult. Conservation efforts include breeding programs in Negros Forest Park, international support, forest patrols, community education, and habitat restoration. The deer also plays a key ecological role by dispersing seeds, which helps regenerate forests.', 'philippine_spotted_deer.jpg', 2),
(8, 'Negros Bleeding-Heart Dove', 'Gallicolumba keayi', '70 to 400 individuals left in the wild', 'The Negros Bleeding-Heart Dove is a striking bird found only in the forests of Negros and Panay, known for the bright red patch on its chest. Unlike many doves, it stays mostly on the forest floor, feeding on fruits, seeds, and insects, while its blue, brown, and green plumage helps it blend with fallen leaves. The species is critically endangered due to extensive logging, charcoal-making, agricultural expansion, and wildlife trapping for the pet trade. Habitat fragmentation makes it hard to find food, nests, and mates, and it survives poorly in captivity. Conservation efforts focus on forest protection, habitat restoration, community education, and captive breeding to help restore populations.', 'negros_bleeding_heart_dove.jpg', 1),
(9, 'Philippine Forest Turtle', 'Siebenrockiella leytensis', 'Believed to be fewer than 3,000 individuals', 'The Philippine Forest Turtle (Palawan Forest Turtle) is one of the rarest and most illegally trafficked turtles in the world. It has a heart-shaped shell with deep grooves and a yellow facial stripe. This species depends on cold, clean freshwater streams shaded by dense forest and is extremely sensitive to environmental change. It was thought extinct until rediscovered in the 2000s, which unfortunately triggered illegal collection for the pet trade.', 'philippine_forest_turtle.jpg', 1),
(10, 'Panay Monitor Lizard', 'Varanus mabitang', 'Roughly 2,000–3,000 individuals', 'The Mabitang is a largely herbivorous monitor lizard endemic to Panay Island. It feeds mostly on fruits and leaves and helps disperse seeds across the forest. It is shy and depends on primary, mid- to high-elevation forests.', 'panay_monitor_lizard.jpg', 2),
(11, 'Philippine Cockatoo', 'Cacatua haematuropygia', 'About 500–1,000 individuals', 'The Philippine Cockatoo, locally called Katala, is a white cockatoo with a bright red undertail patch and an expressive crest. It nests in tree cavities and is heavily targeted by the illegal pet trade; nest poaching and rapid deforestation have driven steep declines.', 'philippine_cockatoo.jpg', 1),
(12, 'Visayan Hornbill', 'Rhabdotorrhinus waldeni', 'Fewer than 1,000 individuals', 'The Visayan Hornbill (Walden''s Hornbill) is a striking bird with a large casque and glossy black plumage. It survives only in small forest fragments in Negros and Panay and is crucial for seed dispersal of large fruits.', 'visayan_hornbill.jpg', 1),
(13, 'Sulu Hornbill', 'Anthracoceros montani', 'Likely fewer than 50 individuals', 'The Sulu Hornbill is one of the rarest birds in the Philippines, possibly surviving only on Tawi-Tawi. It has an all-black body and a massive pale bill and casque. Decades of habitat loss and hunting have brought it to the brink of extinction.', 'sulu_hornbill.jpg', 1),
(14, 'Mindoro Bleeding-heart Dove', 'Gallicolumba platenae', 'Adults possibly under 500', 'The Mindoro Bleeding-heart Dove is a shy, ground-dwelling bird named for the red patch on its chest. It depends on undisturbed lowland and mid-elevation forests and is threatened by habitat loss and hunting.', 'mindoro_bleeding_heart_dove.jpg', 1),
(15, 'Golden-Crowned Flying Fox', 'Acerodon jubatus', '10,000–20,000 individuals (declining)', 'The Golden-Crowned Flying Fox is one of the largest bat species, with a wingspan up to 1.7 m. It feeds on fruit and is vital for pollination and seed dispersal but is threatened by hunting and roost disturbance.', 'golden_crowned_flying_fox.jpg', 2),
(16, 'Dinagat Bushy-tailed Cloud Rat', 'Crateromys australis', 'Unknown, extremely small', 'The Dinagat Bushy-tailed Cloud Rat is an elusive nocturnal rodent with a long, fluffy tail. Known from Dinagat Island, it was once thought possibly extinct until rediscovery. Mining and deforestation threaten its tiny range.', 'dinagat_cloud_rat.jpg', 1),
(17, 'Northern Luzon Giant Cloud Rat', 'Phloeomys pallidus', 'Stable but decreasing; exact number unknown', 'A large, slow-moving rodent found in Northern Luzon forests. It is nocturnal, lives in tree hollows, and is culturally significant in some communities. Hunting and habitat loss are pressures.', 'northern_luzon_giant_cloud_rat.jpg', 3),
(18, 'Southern Luzon Giant Cloud Rat', 'Phloeomys cumingi', 'Declining; no firm numbers', 'Similar to its northern relative but darker, this nocturnal arboreal rodent inhabits forests in Southern Luzon and relies on tree hollows for shelter.', 'southern_luzon_giant_cloud_rat.jpg', 3),
(19, 'Cebu Flowerpecker', 'Dicaeum quadricolor', '100–200 individuals', 'The Cebu Flowerpecker is a tiny, brightly colored bird rediscovered in 1992 and surviving only in a few forest remnants in central Cebu. It depends on nectar-rich forest plants and is critically endangered due to habitat loss.', 'cebu_flowerpecker.jpg', 1),
(20, 'Ilin Island Cloudrunner', 'Crateromys paulus', 'Unknown; possibly fewer than 50 or extinct', 'The Ilin Island Cloudrunner is known from a single specimen and may be extinct. If any survive, they face severe threats from deforestation and habitat conversion on Ilin Island.', 'ilin_island_cloudrunner.jpg', 1);

-- 6) species_habitat — all habitat mappings
-- Philippine Eagle
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(1, (SELECT location_id FROM location WHERE location_name='Mindanao'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Dense mountain forests')),
(1, (SELECT location_id FROM location WHERE location_name='Luzon'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Dense mountain forests')),
(1, (SELECT location_id FROM location WHERE location_name='Leyte'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Dense mountain forests')),
(1, (SELECT location_id FROM location WHERE location_name='Samar'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Dense mountain forests'));

-- Tamaraw
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(2, (SELECT location_id FROM location WHERE location_name='Mindoro Island'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Mountain forests')),
(2, (SELECT location_id FROM location WHERE location_name='Mindoro Island'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Grasslands'));

-- Philippine Tarsier
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(3, (SELECT location_id FROM location WHERE location_name='Bohol'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests')),
(3, (SELECT location_id FROM location WHERE location_name='Leyte'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests')),
(3, (SELECT location_id FROM location WHERE location_name='Samar'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests')),
(3, (SELECT location_id FROM location WHERE location_name='Mindanao'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests'));

-- Visayan Warty Pig
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(4, (SELECT location_id FROM location WHERE location_name='Panay'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests')),
(4, (SELECT location_id FROM location WHERE location_name='Negros'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests'));

-- Philippine Mouse Deer
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(5, (SELECT location_id FROM location WHERE location_name='Balabac (Palawan)'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Lowland forests'));

-- Philippine Pangolin
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(6, (SELECT location_id FROM location WHERE location_name='Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests')),
(6, (SELECT location_id FROM location WHERE location_name='Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Grasslands'));

-- Philippine Spotted Deer
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(7, (SELECT location_id FROM location WHERE location_name='Negros'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Dense rainforests')),
(7, (SELECT location_id FROM location WHERE location_name='Negros'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Grasslands')),
(7, (SELECT location_id FROM location WHERE location_name='Panay'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Dense rainforests')),
(7, (SELECT location_id FROM location WHERE location_name='Panay'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Grasslands'));

-- Negros Bleeding-Heart Dove
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(8, (SELECT location_id FROM location WHERE location_name='Negros'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Lowland rainforests')),
(8, (SELECT location_id FROM location WHERE location_name='Panay'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Lowland rainforests'));

-- Philippine Forest Turtle
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(9, (SELECT location_id FROM location WHERE location_name='Northern Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forested lowlands')),
(9, (SELECT location_id FROM location WHERE location_name='Northern Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Limestone forests')),
(9, (SELECT location_id FROM location WHERE location_name='Northern Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Freshwater streams')),
(9, (SELECT location_id FROM location WHERE location_name='Dumaran Island'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Freshwater streams'));

-- Panay Monitor Lizard
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(10, (SELECT location_id FROM location WHERE location_name='Panay Island'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Primary forests (mid- to high-elevation)'));

-- Philippine Cockatoo
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(11, (SELECT location_id FROM location WHERE location_name='Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Mangroves')),
(11, (SELECT location_id FROM location WHERE location_name='Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Lowland forests')),
(11, (SELECT location_id FROM location WHERE location_name='Palawan'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Riverine woodlands'));

-- Visayan Hornbill
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(12, (SELECT location_id FROM location WHERE location_name='Negros'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Primary rainforests')),
(12, (SELECT location_id FROM location WHERE location_name='Panay'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Primary rainforests'));

-- Sulu Hornbill
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(13, (SELECT location_id FROM location WHERE location_name='Tawi-Tawi (Sulu Archipelago)'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forest patches'));

-- Mindoro Bleeding-heart Dove
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(14, (SELECT location_id FROM location WHERE location_name='Mindoro'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Lowland forests')),
(14, (SELECT location_id FROM location WHERE location_name='Mindoro'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Mid-elevation forests'));

-- Golden-Crowned Flying Fox
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(15, (SELECT location_id FROM location WHERE location_name='Luzon'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forest canopies')),
(15, (SELECT location_id FROM location WHERE location_name='Leyte'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forest canopies')),
(15, (SELECT location_id FROM location WHERE location_name='Mindanao'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forest canopies'));

-- Dinagat Bushy-tailed Cloud Rat
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(16, (SELECT location_id FROM location WHERE location_name='Dinagat Island'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Mossy forests')),
(16, (SELECT location_id FROM location WHERE location_name='Dinagat Island'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Lowland forests'));

-- Northern Luzon Giant Cloud Rat
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(17, (SELECT location_id FROM location WHERE location_name='Northern Luzon (Sierra Madre)'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests'));

-- Southern Luzon Giant Cloud Rat
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(18, (SELECT location_id FROM location WHERE location_name='Southern Luzon (Quezon, Bicol)'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests'));

-- Cebu Flowerpecker
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(19, (SELECT location_id FROM location WHERE location_name='Central Cebu (Nug-as Forest)'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forest remnants'));

-- Ilin Island Cloudrunner
INSERT INTO species_habitat (species_id, location_id, habitat_type_id) VALUES
(20, (SELECT location_id FROM location WHERE location_name='Ilin Island (south of Mindoro)'), (SELECT habitat_type_id FROM habitat_type WHERE habitat_name='Forests'));

-- 7) species_threats — all threat mappings (FIXED)
INSERT INTO species_threats (species_id, threat_id) VALUES
(1, (SELECT threat_id FROM threat WHERE threat_name='Deforestation')),
(1, (SELECT threat_id FROM threat WHERE threat_name='Illegal hunting')),
(1, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(2, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(2, (SELECT threat_id FROM threat WHERE threat_name='Hunting/poaching')),
(2, (SELECT threat_id FROM threat WHERE threat_name='Disease transmitted by domestic cattle')),
(3, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(3, (SELECT threat_id FROM threat WHERE threat_name='Illegal pet trade')),
(3, (SELECT threat_id FROM threat WHERE threat_name='Tourism disturbance')),
(4, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(4, (SELECT threat_id FROM threat WHERE threat_name='Hunting for bushmeat')),
(4, (SELECT threat_id FROM threat WHERE threat_name='Hybridization with domestic pigs')),
(5, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(5, (SELECT threat_id FROM threat WHERE threat_name='Illegal hunting')),
(5, (SELECT threat_id FROM threat WHERE threat_name='Wildlife trafficking')),
(6, (SELECT threat_id FROM threat WHERE threat_name='Illegal wildlife trade')),
(6, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(6, (SELECT threat_id FROM threat WHERE threat_name='Poaching')),
(7, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(7, (SELECT threat_id FROM threat WHERE threat_name='Illegal hunting')),
(7, (SELECT threat_id FROM threat WHERE threat_name='Forest conversion for agriculture')),
(8, (SELECT threat_id FROM threat WHERE threat_name='Deforestation')),
(8, (SELECT threat_id FROM threat WHERE threat_name='Habitat fragmentation')),
(8, (SELECT threat_id FROM threat WHERE threat_name='Illegal trapping')),
(9, (SELECT threat_id FROM threat WHERE threat_name='Illegal wildlife trade')),
(9, (SELECT threat_id FROM threat WHERE threat_name='Habitat destruction')),
(9, (SELECT threat_id FROM threat WHERE threat_name='Deforestation')),
(9, (SELECT threat_id FROM threat WHERE threat_name='Water pollution')),
(10, (SELECT threat_id FROM threat WHERE threat_name='Deforestation')),
(10, (SELECT threat_id FROM threat WHERE threat_name='Poaching for bushmeat')),
(10, (SELECT threat_id FROM threat WHERE threat_name='Habitat fragmentation')),
(11, (SELECT threat_id FROM threat WHERE threat_name='Illegal wildlife trade')),
(11, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(11, (SELECT threat_id FROM threat WHERE threat_name='Logging')),
(11, (SELECT threat_id FROM threat WHERE threat_name='Nest poaching')),
(12, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(12, (SELECT threat_id FROM threat WHERE threat_name='Hunting')),
(12, (SELECT threat_id FROM threat WHERE threat_name='Deforestation')),
(12, (SELECT threat_id FROM threat WHERE threat_name='Nest disturbance')),
(13, (SELECT threat_id FROM threat WHERE threat_name='Severe habitat loss')),
(13, (SELECT threat_id FROM threat WHERE threat_name='Illegal hunting')),
(13, (SELECT threat_id FROM threat WHERE threat_name='Extreme deforestation')),
(14, (SELECT threat_id FROM threat WHERE threat_name='Habitat destruction')),
(14, (SELECT threat_id FROM threat WHERE threat_name='Hunting')),
(14, (SELECT threat_id FROM threat WHERE threat_name='Forest conversion')),
(15, (SELECT threat_id FROM threat WHERE threat_name='Hunting')),
(15, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(15, (SELECT threat_id FROM threat WHERE threat_name='Disturbance of roosting sites')),
(16, (SELECT threat_id FROM threat WHERE threat_name='Mining')),
(16, (SELECT threat_id FROM threat WHERE threat_name='Deforestation')),
(16, (SELECT threat_id FROM threat WHERE threat_name='Limited distribution')),
(17, (SELECT threat_id FROM threat WHERE threat_name='Hunting')),
(17, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(17, (SELECT threat_id FROM threat WHERE threat_name='Forest degradation')),
(18, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(18, (SELECT threat_id FROM threat WHERE threat_name='Hunting')),
(18, (SELECT threat_id FROM threat WHERE threat_name='Habitat fragmentation')),
(19, (SELECT threat_id FROM threat WHERE threat_name='Habitat loss')),
(19, (SELECT threat_id FROM threat WHERE threat_name='Extremely limited forest cover')),
(20, (SELECT threat_id FROM threat WHERE threat_name='Deforestation')),
(20, (SELECT threat_id FROM threat WHERE threat_name='Habitat destruction')),
(20, (SELECT threat_id FROM threat WHERE threat_name='Extremely limited range'));

-- 8) Fun facts
INSERT INTO species_funfacts (species_id, fact_detail) VALUES
(1, 'Known as the "Monkey-Eating Eagle"; has a wingspan of about 2 meters and may live up to 60 years in captivity.'),
(2, 'Found nowhere else on Earth; has V-shaped horns and is more solitary than domestic water buffalo.'),
(3, 'Eyes are as large as its brain; can leap up to 3 meters; completely insectivorous.'),
(4, 'Males grow a distinctive mohawk-like mane during the breeding season.'),
(5, 'Despite its name, it is not a mouse — it is the world''s smallest hoofed mammal.'),
(6, 'Pangolins have no teeth and use a long sticky tongue to feed on ants and termites.'),
(7, 'The white spots remain visible even in adults.'),
(8, 'Prefers walking rather than flying; it stays close to the forest floor.'),
(9, 'Was once thought to be possibly extinct until rediscovery.'),
(10, 'One of the only largely fruit-eating monitor lizards in the world.'),
(11, 'One of the loudest parrots in the Philippines.'),
(12, 'Females seal themselves inside tree cavities while nesting.'),
(13, 'Potentially one of the top 10 rarest birds in the world.'),
(14, 'Red chest patch resembles a bleeding wound.'),
(15, 'One of the world''s biggest bats.'),
(16, 'Was thought to be possibly extinct for years.'),
(17, 'Can grow as large as a small cat.'),
(18, 'Important seed disperser and primarily arboreal.'),
(19, 'Rediscovered after being believed extinct for almost a century.'),
(20, 'Known from only one specimen; possibly already extinct.');

-- 9) Organizations
INSERT INTO organization (org_id, name, about, website, donate_link) VALUES
(1, 'Philippine Eagle Foundation (PEF)', 'The Philippine Eagle Foundation in Davao City leads conservation programs for the country''s national bird. It runs breeding, forest protection, and education projects across Mindanao.', 'https://www.philippineeaglefoundation.org', 'https://www.philippineeaglefoundation.org/donate'),
(2, 'Tamaraw Conservation Program (TCP)', 'A government-led program under the Department of Environment and Natural Resources (DENR). TCP focuses on protecting Tamaraws in Mindoro through anti-poaching patrols, breeding efforts, and community education.', 'https://denr.gov.ph/?s=tamaraw', 'https://bmb.gov.ph'),
(3, 'Philippine Tarsier Foundation, Inc. (PTFI)', 'Operates the Tarsier Sanctuary in Corella, Bohol; protects tarsier habitats and educates tourists on ethical viewing.', 'http://www.tarsierfoundation.com/', 'http://www.tarsierfoundation.com/category/volunteer'),
(4, 'Talarak Foundation', 'Runs breeding and rewilding programs for endangered Visayan species, restores degraded forests and operates wildlife rescue centers.', 'https://www.talarak.org', 'https://www.talarak.org/support'),
(5, 'WWF Philippines', 'Protects marine wildlife such as dugongs, sea turtles, and works on coral reef restoration and sustainable fishing.', 'https://wwf.org.ph', 'https://support.wwf.org.ph/make-a-donation/'),
(6, 'Mabuwaya Foundation', 'Community-based conservation programs for the Philippine Crocodile, focusing on habitat protection and education.', 'https://www.mabuwaya.org', 'https://www.mabuwaya.org/index.cfm?p=0B272505-1DE0-5C8B-DF7CA43A69A2F3CE'),
(7, 'Marine Wildlife Watch of the Philippines (MWWP)', 'Monitors and protects marine wildlife such as sea turtles and dugongs, coordinates strandings and rescue operations.', 'https://www.mwwphilippines.org', 'https://mwwphilippines.org/support-contact/'),
(8, 'Turtle Conservation Society of the Philippines (TCSP)', 'Network of researchers and volunteers working to conserve sea turtle nesting sites across the archipelago.', 'https://www.wildspiritfund.org/marine-turtle-conservation-and-health/', 'https://www.wildspiritfund.org/become-a-member/'),
(9, 'Philippine Biodiversity Conservation Foundation Inc. (PBCFI)', 'Conducts biodiversity research and protection programs across various ecosystems, focusing on reptiles, amphibians, and lesser-known species.', 'https://www.philbio.org.ph/ourwork/', 'mailto:donations@philbio.org.ph'),
(10, 'Oceana Philippines', 'Works to protect marine biodiversity through sustainable fishing, plastic reduction campaigns, and habitat protection.', 'https://ph.oceana.org', 'https://ph.oceana.org/take-action/');

-- 10) Organization supports
INSERT INTO organization_supports (org_id, species_id, support_type) VALUES
(1, 1, 'Conservation & research'),
(2, 2, 'Habitat protection'),
(3, 3, 'Habitat protection & education');

-- 11) Help tips and actions
INSERT INTO help_tip (title, reason) VALUES
('Reduce Paper & Wood Waste', 'Less demand for paper → fewer trees cut down → more forests preserved for animals like the Philippine Eagle, Philippine Deer, and Pangolin.'),
('Support Responsible Farming', 'Slash-and-burn farming destroys forests and pushes species like Tamaraw and Warty Pig out of their habitats.'),
('Never Support Wildlife Trade', 'Many species become endangered because of illegal pet trade and hunting (Tarsier, Pangolin, Mouse Deer).'),
('Plant Native Trees', 'Trees = shelter and food for wildlife. Native trees are better because animals are adapted to them.'),
('Reduce Waste', 'Trash → pollution → habitat degradation. Non-biodegradable waste harms land animals and clogs rivers, affecting forests.'),
('Support Conservation Organizations', 'Your donations help pay for ranger patrols, rescue operations, captive breeding, and reforestation.'),
('Spread Awareness', 'The more people who know, the more people care.');

INSERT INTO help_tip_action (tip_id, action_text) VALUES
((SELECT help_id FROM help_tip WHERE title='Reduce Paper & Wood Waste'), 'Use both sides of paper'),
((SELECT help_id FROM help_tip WHERE title='Reduce Paper & Wood Waste'), 'Choose digital notes instead of printing'),
((SELECT help_id FROM help_tip WHERE title='Reduce Paper & Wood Waste'), 'Support products with "Recycled" or "FSC Certified" labels'),
((SELECT help_id FROM help_tip WHERE title='Support Responsible Farming'), 'Buy from local farmers'),
((SELECT help_id FROM help_tip WHERE title='Support Responsible Farming'), 'Choose organic/eco-friendly products'),
((SELECT help_id FROM help_tip WHERE title='Support Responsible Farming'), 'Avoid buying crops linked to illegal land clearing'),
((SELECT help_id FROM help_tip WHERE title='Never Support Wildlife Trade'), 'Don''t buy exotic pets'),
((SELECT help_id FROM help_tip WHERE title='Never Support Wildlife Trade'), 'Don''t purchase items made from animal parts (scales, feathers, shells)'),
((SELECT help_id FROM help_tip WHERE title='Never Support Wildlife Trade'), 'Report wildlife trade to DENR / PCSD'),
((SELECT help_id FROM help_tip WHERE title='Plant Native Trees'), 'Join tree-planting drives (schools/barangay events)'),
((SELECT help_id FROM help_tip WHERE title='Plant Native Trees'), 'Choose native species (Narra, Molave, Lauan)'),
((SELECT help_id FROM help_tip WHERE title='Plant Native Trees'), 'Avoid invasive plants'),
((SELECT help_id FROM help_tip WHERE title='Reduce Waste'), 'Practice 3R''s (Reduce, Reuse, Recycle)'),
((SELECT help_id FROM help_tip WHERE title='Reduce Waste'), 'Bring reusable bags/tumblers'),
((SELECT help_id FROM help_tip WHERE title='Reduce Waste'), 'Avoid single-use plastics'),
((SELECT help_id FROM help_tip WHERE title='Support Conservation Organizations'), 'Donate (even ₱10 helps)'),
((SELECT help_id FROM help_tip WHERE title='Support Conservation Organizations'), 'Visit wildlife sanctuaries instead of zoos'),
((SELECT help_id FROM help_tip WHERE title='Support Conservation Organizations'), 'Share their work on social media'),
((SELECT help_id FROM help_tip WHERE title='Spread Awareness'), 'Share posts about endangered animals'),
((SELECT help_id FROM help_tip WHERE title='Spread Awareness'), 'Educate classmates and family'),
((SELECT help_id FROM help_tip WHERE title='Spread Awareness'), 'Choose wildlife-friendly content (no selfies with wildlife)');

-- 12) Related Articles
INSERT INTO related_article (title, description, link, category) VALUES
('2,000 Philippine species critically endangered – DENR', 'This article provides an extensive overview of the alarming number of species in the Philippines that are classified as critically endangered or vulnerable. It includes insights from government officials, highlighting the scale of biodiversity loss in the country and the urgency for conservation interventions. For anyone looking to understand the current state of Philippine wildlife, the article offers concrete data, official perspectives, and context that can support research, advocacy, or public awareness campaigns.', 'https://www.philstar.com/nation/2025/02/22/2423268/2000-philippine-species-critically-endangered-denr', 'General'),
('Study warns up to a quarter of Philippine vertebrates risk extinction', 'This scientific study presents a detailed analysis of the risk levels faced by terrestrial vertebrates in the Philippines, indicating that between 15% and 23% are at risk of extinction. The research emphasizes the vulnerability of amphibians and mammals, groups often overlooked in conservation priorities. By highlighting species-specific threats and statistical evidence, the study provides a crucial foundation for policymakers, conservationists, and educators to design targeted protection programs and raise public awareness about the severity of the biodiversity crisis.', 'https://news.mongabay.com/2025/10/study-warns-up-to-a-quarter-of-philippine-vertebrates-risk-extinction/', 'Scientific'),
('Biodiversity on the Brink: 30% of PH land vertebrates facing extinction', 'This article synthesizes recent research findings and presents them in an accessible format for the general public. It emphasizes that nearly a third of land vertebrates in the Philippines are at high risk of extinction, underscoring the urgency for immediate conservation measures. The piece serves as a strong advocacy tool by providing context, expert commentary, and examples, making it an essential resource for understanding the broader implications of habitat loss, climate change, and human activity on Philippine biodiversity.', 'https://newsline.ph/biodiversity-on-the-brink-30-of-ph-land-vertebrates-facing-extinction/', 'Scientific'),
('Illegal wildlife trade in Sulu‑Celebes Seas calls for tripartite collaboration', 'This article sheds light on the large-scale illegal wildlife trade affecting marine and terrestrial species in Philippine waters. It provides detailed accounts of trafficking routes, species affected, and the socio-economic drivers behind this illicit activity. By highlighting the need for tripartite collaboration between government, NGOs, and local communities, it offers actionable insights into combating wildlife crime and strengthening conservation frameworks, making it highly relevant for policy advocacy, environmental planning, and educational initiatives.', 'https://archive.wwf.org.ph/resource-center/story-archives-2023/high-wildlife-trafficking-levels-in-the-sulu-celebes-seas-call-for-tripartite-collaboration/', 'Policy'),
('Save wildlife from extinction – PhilStar feature', 'This feature article profiles several endangered species in the Philippines, such as the tamaraw, dugong, pawikan, pangolin, and Philippine cockatoo, providing both scientific and anecdotal accounts of their current status. It discusses the main threats these species face, including habitat destruction, poaching, and climate change, giving readers a comprehensive understanding of the challenges involved. The article is particularly useful for education, awareness campaigns, and storytelling purposes, as it combines factual reporting with compelling narratives that illustrate the urgency of wildlife conservation.', 'https://qa.philstar.com/business/2024/12/20/2408559/save-wildlife-extinction', 'General'),
('DENR partners with private sector to save 6 endangered PH animals from extinction', 'This article highlights a collaborative effort between the Department of Environment and Natural Resources (DENR), private organizations, and NGOs to protect six critically endangered species in the Philippines. It provides detailed examples of joint conservation programs, including habitat restoration, species monitoring, and awareness campaigns. This resource is particularly valuable for understanding how multi-stakeholder partnerships operate in practice and can inspire similar initiatives by demonstrating effective coordination between government, NGOs, and the private sector.', 'https://mb.com.ph/2024/10/15/denr-partners-with-conservation-groups-private-sector-to-save-6-endangered-ph-animals-from-extinction', 'Policy'),
('Why lesser-studied Philippine species need conservation too', 'Based on the 2025 vertebrate extinction-risk study, this article emphasizes the importance of conserving non-charismatic species such as amphibians, small mammals, and island frogs. It explains that these species, despite being lesser-known, play critical roles in their ecosystems and are often at higher risk due to under-documentation and habitat pressures. The piece is especially useful for broadening conservation perspectives, highlighting that effective biodiversity protection requires attention to all species, not just the well-known or popular ones.', 'https://news.mongabay.com/2025/10/study-warns-up-to-a-quarter-of-philippine-vertebrates-risk-extinction/', 'Scientific'),
('The Philippines ecosystem: endangered species in the Philippines — causes and threats', 'This comprehensive overview examines the biodiversity status in the Philippines, detailing the number of threatened species, main ecosystems, and the range of threats to both terrestrial and marine life. It provides background context for anyone seeking to understand why conservation is critical, linking habitat loss, poaching, and climate change to the decline of Philippine wildlife. The article is an excellent foundational resource for research, educational content, and advocacy, offering both statistical data and narrative explanation of the challenges facing the country''s ecosystems.', 'https://www.futurelearn.com/info/futurelearn-international/endangered-species-philippines', 'General'),
('Technology-Driven Biodiversity Conservation in the Philippines', 'This piece explains how modern technologies like drones, satellite imaging, and AI-assisted monitoring are helping track wildlife populations and illegal activities. Conservation groups in the Philippines increasingly rely on tech tools for mapping and data collection. The article shows that innovation is becoming essential to protecting endangered ecosystems.', 'https://mb.com.ph/2024/5/2/technology-driven-biodiversity-conservation', 'Scientific'),
('Understanding Endangered Species in the Philippines', 'This article gives an overview of why many species in the Philippines are endangered, from deforestation to pollution to illegal wildlife trade. It explains basic conservation concepts in simple terms. It''s designed to help beginners understand the country''s biodiversity crisis.', 'https://www.futurelearn.com/info/futurelearn-international/endangered-species-philippines', 'Scientific'),
('Deforestation & Mining Threats in Mindanao Biodiversity Hotspots', 'Mining expansions and logging operations are rapidly eating away at Mindanao''s remaining forest ecosystems. The article explains how these activities endanger species that rely on undisturbed habitats. It calls for stricter environmental regulations and more sustainable land use planning.', 'https://www.rappler.com/environment/57367-illegal-logging-hotspots-reduced/', 'General');

-- 13) News
INSERT INTO news (title, summary, link, category, published_date) VALUES
('Department of Environment and Natural Resources (DENR) & SM Supermalls collaborate to save critically endangered PH species', 'This initiative highlights a joint conservation program targeting several critically endangered species — including forest and land animals like Tamaraw, Philippine Eagle, and Palawan Pangolin. The campaign uses SM''s retail and fundraising network to raise awareness and funds for habitat protection, anti-poaching, and species recovery efforts.', 'https://www.pna.gov.ph/articles/1239874', 'Success Story', '2024-12-12'),
('Updated population status of Tamaraw — still critically endangered but conservation efforts continuing', 'According to a 2025 report, only about 500–600 Tamaraw remain in the wild, found in select habitats such as mountain sanctuaries in Mindoro. The government allocated a PHP 100‑million biodiversity budget (2024) to support conservation of Tamaraw among other threatened species, aiming to strengthen patrols and habitat protection programs.', 'https://www.philstar.com/headlines/2025/04/08/2434337/tamaraw-remains-one-critically-endangered-species', 'Update', '2025-04-08'),
('Nationwide "Save from Extinction" campaign launched to protect six flagship endangered species', 'In late 2024 the DENR, private sector, and NGOs initiated a campaign to raise funds and public support for critically endangered species in the Philippines. The campaign emphasizes forest‑dwelling animals and land species (e.g. Philippine Eagle, Tamaraw, Pangolin, Cockatoo) — supporting habitat protection, anti-trafficking, and research through donations and awareness drives.', 'https://mb.com.ph/2024/10/15/denr-partners-with-conservation-groups-private-sector-to-save-6-endangered-ph-animals-from-extinction', 'Alert', '2024-10-15'),
('Government & NGOs formal agreement to protect land species including Philippine Eagle, Tamaraw, Pangolin and Cockatoo', 'In 2024 a memorandum of agreement (MOA) was signed among the DENR, private sector, and conservation groups to safeguard several endangered land species native to the Philippines. This formal alliance aims to coordinate habitat protection, anti-poaching enforcement, community engagement, and species‑specific conservation measures — reflecting a structured national effort.', 'https://www.pna.gov.ph/index.php/articles/1235590', 'Success Story', '2024-10-15'),
('Recognition that up to 2,000 species — including many endemic — are critically endangered or vulnerable in the Philippines', 'A 2025 announcement by DENR highlighted that thousands of flora and fauna species are at risk, primarily due to habitat destruction, land use change, climate impacts, and human activity. This serves as a broad wake‑up call about terrestrial biodiversity loss — underlining why land‑focused conservation and ecosystem protection are urgent.', 'https://www.philstar.com/nation/2025/02/22/2423268/2000-philippine-species-critically-endangered-denr', 'Alert', '2025-02-22'),
('Growing awareness in media & public of biodiversity loss and need for habitat protection (feature on endangered Philippine species)', 'A media feature emphasizes that species like Philippine Eagle, Tamaraw, Palawan Pangolin, and forest‑dependent birds are "umbrella species," meaning their protection safeguards entire ecosystems. The article calls for stronger conservation laws, habitat protection, and public support — showing that public awareness is becoming part of the conservation strategy.', 'https://qa.philstar.com/business/2024/12/20/2408559/save-wildlife-extinction', 'Alert', '2024-12-20'),
('Call to Help Protect PH Endangered Species — ABS-CBN Feature', 'ABS-CBN''s feature emphasizes ongoing threats to species such as the Philippine eagle, tamaraw, and tarsier. It encourages viewers to participate in conservation activities and support programs. The article highlights how media plays a powerful role in raising awareness.', 'https://www.abs-cbn.com/news/business/2024/12/20/help-safeguard-ph-s-endangered-species-1708', 'Alert', '2024-12-20'),
('PH hosts landmark global meeting on migratory waterbird conservation', 'Talarak Foundation, in collaboration with international zoos, releases a second group of captive-bred Visayan Warty Pigs into restored forest habitats in Panay. The reintroduction aims to strengthen genetic diversity in wild populations.', 'https://www.talarak.org/', 'Success Story', '2025-11-10'),
('Palawan Hornbill finds new hope after first successful breeding in captivity', 'First successful captive breeding of the endangered Palawan hornbill — a concrete win for conservation efforts in Palawan.', 'https://www.gmanetwork.com/regionaltv/features/111118/palawan-hornbill-finds-new-hope-after-first-successful-breeding-in-captivity/story/', 'Success Story', '2025-11-02'),
('Campaign to raise ₱100M to save Philippine endangered species from extinction', 'SM and the Department of Environment and Natural Resources (DENR), with BDO Unibank Inc. (BDO) as a major partner, launched the "Save from Extinction" campaign in October 2024 to protect endangered species in the Philippines.', 'https://www.philstar.com/lifestyle/pet-life/2025/08/04/2462402/campaign-raise-p100m-save-philippine-endangered-species-extinction/amp', 'Success Story', '2025-08-04'),
('Biodiversity on the Brink: 30% of PH land vertebrates facing extinction', 'A recent study by University of Southern Mindanao researchers, published in Science of the Total Environment, warns that the Philippines is on the brink of a major biodiversity crisis.', 'https://newsline.ph/biodiversity-on-the-brink-30-of-ph-land-vertebrates-facing-extinction/', 'Alert', '2025-10-09');
