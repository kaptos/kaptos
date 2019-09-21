
-- members -----

CREATE TABLE members (
    id UUID,
    team_id UUID,
    user_id UUID,
    status TEXT,
    roles TEXT
);

CREATE UNIQUE INDEX members_pk ON members ( id );
CREATE INDEX members_teams ON members ( team_id );
CREATE INDEX members_users ON members ( user_id );


-- reports -----

CREATE TABLE reports (
    id UUID,
    task_id UUID,
    station_id UUID,
    time TIMESTAMP WITH TIME ZONE,
    frequency INTEGER,
    modulation TEXT,
    location POINT,
    bearing FLOAT,
    duration INTEGER,
    strength INTEGER,
    nmea TEXT
);

CREATE UNIQUE INDEX reports_pk ON reports ( id );
CREATE INDEX reports_tasks ON reports ( task_id, time );
CREATE INDEX reports_stations ON reports ( station_id, time );


-- signals -----

CREATE TABLE signals (
    id UUID,
    task_id UUID,
    report_ids TEXT,
    time TIMESTAMP WITH TIME ZONE,
    duration INTEGER,
    location POINT,
    cep INTEGER
);

CREATE UNIQUE INDEX signals_pk ON signals ( id );
CREATE INDEX signals_tasks ON signals ( task_id, time );


-- stations -----

CREATE TABLE stations (
    id UUID,
    name TEXT,
    description TEXT,
    owner_id UUID
);

CREATE UNIQUE INDEX stations_pk ON stations ( id );
CREATE INDEX stations_owners ON stations ( owner_id );


-- tasks -----

CREATE TABLE tasks (
    id UUID,
    team_id UUID,
    start_time TIMESTAMP WITH TIME ZONE,
    end_time TIMESTAMP WITH TIME ZONE,
    frequency INTEGER,
    modulation TEXT,
    bandwidth INTEGER
);

CREATE UNIQUE INDEX tasks_pk ON tasks ( id );
CREATE INDEX tasks_teams ON tasks ( team_id, start_time );


-- teams -----

CREATE TABLE teams (
    id UUID,
    name TEXT,
    description TEXT,
    area POLYGON,
    visibility TEXT
);

CREATE UNIQUE INDEX teams_pk ON teams ( id );


-- tokens -----

CREATE TABLE tokens (
    id UUID,
    type TEXT,
    value TEXT,
    subject TEXT,
    created TIMESTAMP WITH TIME ZONE,
    expires TIMESTAMP WITH TIME ZONE
);

CREATE UNIQUE INDEX tokens_pk ON tokens ( id );
CREATE UNIQUE INDEX tokens_type_value ON tokens ( type, value );
CREATE INDEX tokens_subjects ON tokens ( subject );

-- users -----

CREATE TABLE users (
    id UUID,
    email TEXT,
    name TEXT,
    call_sign TEXT,
    status TEXT,
    created TIMESTAMP WITH TIME ZONE,
    failures TEXT
);

CREATE UNIQUE INDEX users_pk ON users ( id );
CREATE UNIQUE INDEX users_email on users ( email );