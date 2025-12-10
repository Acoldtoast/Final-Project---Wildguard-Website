PRAGMA foreign_keys = ON;

-- Conservation statuses
CREATE TABLE conservation_status (
  status_id INTEGER NOT NULL,
  status_name VARCHAR(50) NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY (status_id),
  UNIQUE (status_name)
);

-- Core species table
CREATE TABLE species (
  id INTEGER NOT NULL,
  name VARCHAR(100) NOT NULL,
  scientific_name VARCHAR(100) NOT NULL,
  population_estimate VARCHAR(100) NOT NULL,
  description TEXT NOT NULL,
  image_file VARCHAR(100),
  status_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (status_id) REFERENCES conservation_status (status_id)
);

-- Locations (islands, regions, reserves)
CREATE TABLE location (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_name TEXT NOT NULL UNIQUE
);

-- Habitat types (forest, grassland, mangrove, etc.)
CREATE TABLE habitat_type (
  habitat_type_id INTEGER NOT NULL,
  habitat_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (habitat_type_id),
  UNIQUE (habitat_name)
);

-- Junction table: species -> (location, habitat_type)
CREATE TABLE species_habitat (
  habitat_id INTEGER NOT NULL,
  species_id INTEGER NOT NULL,
  location_id INTEGER NOT NULL,
  habitat_type_id INTEGER NOT NULL,
  PRIMARY KEY (habitat_id),
  UNIQUE (
    species_id,
    location_id,
    habitat_type_id
  ),
  FOREIGN KEY (species_id) REFERENCES species (id) ON DELETE CASCADE,
  FOREIGN KEY (location_id) REFERENCES location (location_id) ON DELETE CASCADE,
  FOREIGN KEY (habitat_type_id) REFERENCES habitat_type (habitat_type_id) ON DELETE CASCADE
);

-- Threats and junction table
CREATE TABLE threat (
  threat_id INTEGER NOT NULL,
  threat_name VARCHAR(150) NOT NULL,
  PRIMARY KEY (threat_id),
  UNIQUE (threat_name)
);

CREATE TABLE species_threats (
  species_threat_id INTEGER NOT NULL,
  species_id INTEGER NOT NULL,
  threat_id INTEGER NOT NULL,
  PRIMARY KEY (species_threat_id),
  UNIQUE (species_id, threat_id),
  FOREIGN KEY (species_id) REFERENCES species (id) ON DELETE CASCADE,
  FOREIGN KEY (threat_id) REFERENCES threat (threat_id) ON DELETE CASCADE
);

-- Species fun facts
CREATE TABLE species_funfacts (
  fact_id INTEGER NOT NULL,
  species_id INTEGER NOT NULL,
  fact_detail TEXT NOT NULL,
  PRIMARY KEY (fact_id),
  FOREIGN KEY (species_id) REFERENCES species (id) ON DELETE CASCADE
);

-- Organizations and support mapping
CREATE TABLE organization (
  org_id INTEGER NOT NULL,
  name VARCHAR(150) NOT NULL,
  about TEXT NOT NULL,
  website VARCHAR(200) NOT NULL,
  donate_link VARCHAR(200),
  PRIMARY KEY (org_id),
  UNIQUE (name)
);

CREATE TABLE organization_supports (
  ogs_id INTEGER NOT NULL,
  org_id INTEGER NOT NULL,
  species_id INTEGER NOT NULL,
  support_type VARCHAR(100) NOT NULL,
  PRIMARY KEY (ogs_id),
  UNIQUE (org_id, species_id, support_type),
  FOREIGN KEY (org_id) REFERENCES organization (org_id) ON DELETE CASCADE,
  FOREIGN KEY (species_id) REFERENCES species (id) ON DELETE CASCADE
);

-- Users
CREATE TABLE user (
  user_id INTEGER NOT NULL,
  username VARCHAR(150) NOT NULL,
  password_hash VARCHAR(256) NOT NULL,
  is_admin BOOLEAN NOT NULL,
  PRIMARY KEY (user_id)
);

-- Help tips and actions
CREATE TABLE help_tip (
  help_id INTEGER NOT NULL,
  title VARCHAR(100) NOT NULL,
  reason TEXT NOT NULL,
  PRIMARY KEY (help_id)
);

CREATE TABLE help_tip_action (
  action_id INTEGER NOT NULL,
  tip_id INTEGER NOT NULL,
  action_text TEXT NOT NULL,
  PRIMARY KEY (action_id),
  FOREIGN KEY (tip_id) REFERENCES help_tip (help_id) ON DELETE CASCADE
);

-- Related articles and news
CREATE TABLE related_article (
  article_id INTEGER NOT NULL,
  title VARCHAR(300) NOT NULL,
  description TEXT NOT NULL,
  link VARCHAR(500) NOT NULL,
  category VARCHAR(50) NOT NULL,
  PRIMARY KEY (article_id)
);

CREATE TABLE news (
  news_id INTEGER NOT NULL,
  title VARCHAR(300) NOT NULL,
  summary TEXT NOT NULL,
  link VARCHAR(500) NOT NULL,
  category VARCHAR(50) NOT NULL,
  published_date DATE,
  PRIMARY KEY (news_id)
);

-- Indexes (helpful for lookups)
CREATE INDEX IF NOT EXISTS idx_species_name ON species(name);
CREATE INDEX IF NOT EXISTS idx_location_name ON location(location_name);
CREATE INDEX IF NOT EXISTS idx_habitat_name ON habitat_type(habitat_name);
