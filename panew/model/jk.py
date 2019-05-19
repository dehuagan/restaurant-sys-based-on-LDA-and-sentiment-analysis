#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db


class jk(db.Model):
    __tablename__ = 'jk'
    res_name = db.Column(db.Text, primary_key=True)

    good = db.Column(db.Float)
    sushi = db.Column(db.Float)
    salmon = db.Column(db.Float)
    fresh = db.Column(db.Float)
    flavor = db.Column(db.Float)
    environment = db.Column(db.Float)
    shrimp_crab = db.Column(db.Float)
    eel_rice = db.Column(db.Float)
    roll = db.Column(db.Float)
    rice = db.Column(db.Float)
    avocado = db.Column(db.Float)
    sukiyaki = db.Column(db.Float)
    tuna = db.Column(db.Float)
    mixed_rice = db.Column(db.Float)
    pork_chop = db.Column(db.Float)
    beef = db.Column(db.Float)
    fruit = db.Column(db.Float)
    hotpot = db.Column(db.Float)
    sashimi = db.Column(db.Float)
    urchin = db.Column(db.Float)
    buffet = db.Column(db.Float)
    shrimp = db.Column(db.Float)
    service = db.Column(db.Float)

    def __repr__(self):
        return "res_name:`{}`,  good :`{}`,sushi:`{}`,salmon:`{}`,fresh:`{}`,flavor:`{}`, environment:`{}`,shrimp_crab:`{}`, eel_rice:`{}`,roll:`{}`,rice:`{}`, avocado:`{}`,sukiyaki:`{}`,tuna:`{}`,mixed_rice:`{}`, pork_chop:`{}`,beef:`{}`,fruit:`{}`,hotpot:`{}`,sashimi:`{}`,urchin:`{}`,buffet:`{}`,shrimp:`{}`,service:`{}`".format(self.res_name, self.good, self.sushi, self.salmon, self.fresh, self.flavor, self.environment, self.shrimp_crab, self.eel_rice, self.roll, self.rice, self. avocado, self.sukiyaki, self.tuna, self.mixed_rice, self.pork_chop, self.beef, self.fruit, self.hotpot, self.sashimi, self.urchin, self.buffet, self.shrimp, self.service)