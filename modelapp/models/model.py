from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer)
    en = db.Column(db.String(200))
    ad = db.Column(db.String(200))
    ga = db.Column(db.String(200))
    ba = db.Column(db.String(200))

    def __init__(self, eid, en, ad, ga, ba):
        self.eid = eid
        self.en = str(en)
        self.ad = str(ad)
        self.ga = str(ga)
        self.ba = str(ba)
        self.yogi = en

    def json(self):
        return {'name': type(self.yogi) }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()