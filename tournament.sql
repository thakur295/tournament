-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- Drop Database if exists

DROP DATABASE IF EXISTS tournament;

-- Create Database

CREATE DATABASE tournament;

-- Connect Database
\c tournament;

-- Create Players Table

CREATE TABLE players(
    id serial PRIMARY KEY,
    p_name text
);


-- Create Matches Table

CREATE TABLE matches(
    id serial PRIMARY KEY,
    winner INTEGER,
    loser INTEGER,
    FOREIGN KEY(winner) REFERENCES players(id),
    FOREIGN KEY(loser) REFERENCES players(id)
);



-- Create view results

CREATE VIEW results AS SELECT players.id, players.p_name,
    coalesce((SELECT count(winner) from matches where players.id = matches.winner),0) as winnings,
    coalesce((SELECT count(*) FROM matches where players.id = matches.winner OR players.id = matches.loser),0) as matches
    FROM players LEFT JOIN matches ON players.id = matches.winner GROUP BY players.id ORDER BY winnings DESC;
