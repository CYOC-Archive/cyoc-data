CREATE TABLE "user" (
    user_id     INTEGER PRIMARY KEY,
    username    VARCHAR(255) NOT NULL UNIQUE,
    email       VARCHAR(255) UNIQUE,
    password    VARCHAR(255), -- hashed password
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chapter (
    chapter_id              INTEGER PRIMARY KEY,
    chapter_date            TIMESTAMP,
    user_id                 INTEGER,
    username                VARCHAR(255),
    parent_chapter_id       INTEGER,
    tags                    TEXT,
    chapter_title           TEXT,
    chapter_text_base64     TEXT
);

CREATE TABLE chapter_option (
    parent_id      INTEGER,
    chapter_id     INTEGER,
    option_id      INTEGER,
    option_title   TEXT
);
