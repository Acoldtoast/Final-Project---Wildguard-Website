
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS conservation_status (
    status_name TEXT PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS species (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    scientific_name TEXT NOT NULL,
    population_estimate TEXT NOT NULL,
    description TEXT NOT NULL,
    image_file TEXT DEFAULT 'default_species.jpg',
    status_name TEXT NOT NULL,
    FOREIGN KEY (status_name) REFERENCES conservation_status(status_name)
);

CREATE INDEX IF NOT EXISTS idx_species_name ON species(name);

CREATE TABLE IF NOT EXISTS species_habitat (
    habitat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER NOT NULL,
    habitat_location TEXT NOT NULL,
    UNIQUE(species_id, habitat_location),
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS species_threats (
    threat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER NOT NULL,
    threat_name TEXT NOT NULL,
    UNIQUE(species_id, threat_name),
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS species_funfacts (
    fact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER NOT NULL,
    fact_detail TEXT NOT NULL,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS organization (
    org_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    about TEXT NOT NULL,
    website TEXT NOT NULL,
    donate_link TEXT
);

CREATE TABLE IF NOT EXISTS organization_supports (
    ogs_id INTEGER PRIMARY KEY AUTOINCREMENT,
    org_id INTEGER NOT NULL,
    species_id INTEGER NOT NULL,
    support_type TEXT NOT NULL,
    UNIQUE(org_id, species_id, support_type),
    FOREIGN KEY (org_id) REFERENCES organization(org_id) ON DELETE CASCADE,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_user_username ON user(username);

CREATE TABLE IF NOT EXISTS help_tip (
    help_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    reason TEXT NOT NULL,
    action TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS related_article (
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    link TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT 'General'
);

CREATE TABLE IF NOT EXISTS news (
    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    summary TEXT NOT NULL,
    link TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT 'General',
    published_date DATE
);
