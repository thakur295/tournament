#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    connection, c = connect()
    c.execute("TRUNCATE TABLE matches CASCADE")
    connection.commit()
    connection.close()


def deletePlayers():
    """Remove all the player records from the database."""

    connection, c = connect()
    c.execute("TRUNCATE TABLE players CASCADE")
    connection.commit()
    connection.close()


def countPlayers():
    """Returns the number of players currently registered."""

    connection, c = connect()
    c.execute("select count(*) from players")
    count = c.fetchone()[0]
    connection.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    connection, c = connect()
    query = "INSERT INTO players(p_name) VALUES(%s)"
    c.execute(query, (name, ))
    connection.commit()
    connection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    connection, c = connect()
    c.execute("select * from results")
    results = c.fetchall()
    connection.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    connection, c = connect()
    query = "INSERT INTO matches(winner, loser) VALUES(%s, %s)"
    params = (winner, loser, )
    c.execute(query, params)
    connection.commit()
    connection.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    results = playerStandings()
    total_pairings = []
    count_results = len(results)
    for i in range(0, count_results - 1, 2):
        pairing = (results[i][0], results[i][1],
                   results[i+1][0], results[i+1][1])
        total_pairings.append(pairing)
    return total_pairings
