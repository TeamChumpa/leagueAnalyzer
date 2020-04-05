from flask_mongoalchemy import MongoAlchemy
from LOLAnalyser import app
from scripts.config import DATABASE_NAME

app.config['MONGOALCHEMY_DATABASE'] = DATABASE_NAME
db = MongoAlchemy(app)

class Champion(db.Document):
    name = db.StringField()
    championId = db.IntField()

class Summoner(db.Document):
    id = db.StringField()
    accountId =  db.StringField()
    profileIconId = db.IntField()
    summonerLevel = db.IntField()

class Match(db.Document):
    gameId = db.IntField()
    champion = db.DocumentField(Champion)
    role = db.StringField()
    lane = db.StringField()