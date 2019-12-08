CREATE TABLE _user (
    id SERIAL PRIMARY KEY ,
    create_at TEXT,
    username TEXT,
    password TEXT,
    password_salt TEXT,
    first_name TEXT,
    last_name TEXT,
    access_token TEXT
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY ,
    created_at TEXT,
    created_by INTEGER REFERENCES _user(id),
    title TEXT,
    content TEXT,
    upvote INTEGER DEFAULT 0
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY ,
    created_at TEXT,
    created_by INTEGER REFERENCES _user(id),
    post_id INTEGER REFERENCES post(id),
    content TEXT,
    upvote INTEGER DEFAULT 0
);