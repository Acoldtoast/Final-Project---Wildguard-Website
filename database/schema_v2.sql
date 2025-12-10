PRAGMA foreign_keys = ON;

-- Schema v2: normalized tables for WildGuard

-- Conservation statuses
CREATE TABLE conservation_status (
  status_id INTEGER NOT NULL,
  status_name VARCHAR(50) NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY (status_id),
  UNIQUE (status_name)
)
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
)

-- Locations (islands, regions, reserves)
CREATE TABLE location (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_name TEXT NOT NULL UNIQUE
);

-- Habitat types (forest, grassland, mangrove, etc.)
CREATE TABLE habitat_type (
    habitat_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    habitat_name TEXT NOT NULL UNIQUE
);

-- Junction table: species -> (location, habitat_type)
CREATE TABLE species_habitat (
    habitat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    habitat_type_id INTEGER NOT NULL,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES location(location_id) ON DELETE CASCADE,
    FOREIGN KEY (habitat_type_id) REFERENCES habitat_type(habitat_type_id) ON DELETE CASCADE,
    UNIQUE (species_id, location_id, habitat_type_id)
);

-- Threats and junction table
CREATE TABLE threat (
    threat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    threat_name TEXT NOT NULL UNIQUE
);

CREATE TABLE species_threats (
    species_threat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER NOT NULL,
    threat_id INTEGER NOT NULL,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE,
    FOREIGN KEY (threat_id) REFERENCES threat(threat_id) ON DELETE CASCADE,
    UNIQUE (species_id, threat_id)
);

-- Species fun facts
CREATE TABLE species_funfacts (
    fact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER NOT NULL,
    fact_detail TEXT NOT NULL,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE
);

-- Organizations and support mapping
CREATE TABLE organization (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    about TEXT NOT NULL,
    website TEXT NOT NULL,
    donate_link TEXT
);

CREATE TABLE organization_supports (
    ogs_id INTEGER PRIMARY KEY AUTOINCREMENT,
    org_id INTEGER NOT NULL,
    species_id INTEGER NOT NULL,
    support_type TEXT NOT NULL,
    FOREIGN KEY (org_id) REFERENCES organization(org_id) ON DELETE CASCADE,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE,
    UNIQUE (org_id, species_id, support_type)
);

-- Users
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    is_admin INTEGER NOT NULL DEFAULT 0
);

-- Help tips and actions
CREATE TABLE help_tip (
    help_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    reason TEXT NOT NULL
);

CREATE TABLE help_tip_action (
    action_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tip_id INTEGER NOT NULL,
    action_text TEXT NOT NULL,
    FOREIGN KEY (tip_id) REFERENCES help_tip(help_id) ON DELETE CASCADE
);

-- Related articles and news
CREATE TABLE related_article (
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    link TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT 'General'
);

CREATE TABLE news (
    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    summary TEXT NOT NULL,
    link TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT 'General',
    published_date DATE
);

-- Indexes (helpful for lookups)
CREATE INDEX IF NOT EXISTS idx_species_name ON species(name);
CREATE INDEX IF NOT EXISTS idx_location_name ON location(location_name);
CREATE INDEX IF NOT EXISTS idx_habitat_name ON habitat_type(habitat_name);
