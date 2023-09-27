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
        if isinstance(player_name, str) and len(player_name) >= 6:
            self._player_name = player_name
        else:
            raise ValueError(
                "player_name must have at least 6 characters."
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

    # @classmethod
    # def get_all(cls):
    #     """Return a list containing a Player object per row in the table"""
    #     sql = """
    #         SELECT *
    #         FROM players
    #     """

    #     rows = CURSOR.execute(sql).fetchall()

    #     return [cls.instance_from_db(row) for row in rows]
