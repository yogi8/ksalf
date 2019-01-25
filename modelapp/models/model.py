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
        self.en = en
        self.ad = ad
        self.ga = ga
        self.ba = ba

    def json(self):
        return {'name': self.en }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()