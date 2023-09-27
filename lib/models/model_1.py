from models.__init__ import CURSOR, CONN


class Player:

    all = {}

    def __init__(self, player_name, scene_id, id=None):
        self.id = id
        self.player_name = player_name
        self.scene_id = scene_id

    def __repr__(self):
        return f"<Player {self.id}: {self.player_name}, {self.scene_id}>"

    @property
    def player_name(self):
        return self._player_name

    @player_name.setter
    def player_name(self, player_name):
        if isinstance(player_name, str) and len(player_name) >= 3:
            self._player_name = player_name
        else:
            raise ValueError(
                "player_name must have at least 3 characters."
            )

    def save(self):
        """ Insert a new row with the player_name and scene_id values of the current Player instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO players (player_name, scene_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.player_name, self.scene_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, player_name, scene_id):
        """ Initialize a new Department instance and save the object to the database """
        player = cls(player_name, scene_id)
        player.save()
        return player

    def update(self):
        """Update the table row corresponding to the current Player instance."""
        sql = """
            UPDATE players
            SET player_name = ?, scene_id = ?
            WHERE player_id = ?
        """
        CURSOR.execute(sql, (self.player_name, self.scene_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Player instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM players
            WHERE player_id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Player object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        player = cls.all.get(row[0])
        if player:
            # ensure attributes match row values in case local instance was modified
            player.player_name = row[1]
            player.scene_id = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            player = cls(row[1], row[2])
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def get_all(cls):
        """Return a list containing a Player object per row in the table"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, player_id):
        """Return a Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE player_id = ?
        """

        row = CURSOR.execute(sql, (player_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
