import sqlite3

CONN = sqlite3.connect('lib/game.db')
CURSOR = CONN.cursor()
