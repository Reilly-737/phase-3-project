

from peewee import *


database = SqliteDatabase('game.db')


class BaseModel(Model):
    class Meta:
        database = database


class Players(BaseModel):
    player_id = AutoField(primary_key=True)
    player_name = CharField(null=False, unique=True)
    scene_id = IntegerField(null=True)


class Scenes(BaseModel):
    scene_id = AutoField(primary_key=True)
    scene_name = CharField(null=False)
    scene_description = TextField(null=True)


class Options(BaseModel):
    option_id = AutoField(primary_key=True)
    scene_id = ForeignKeyField(Scenes, backref='options')
    next_scene_id = ForeignKeyField(
        Scenes, backref='previous_options', null=True)
    option_description = TextField(null=False)


class Prophecy(BaseModel):
    prophecy_id = AutoField(primary_key=True)
    prophecy_name = CharField(null=True)
    prophecy_description = TextField(null=True)

# Connect the models to the database
