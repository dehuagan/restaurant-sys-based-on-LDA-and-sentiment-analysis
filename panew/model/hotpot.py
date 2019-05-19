#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db

class hotpot(db.Model):
    __tablename__ = 'hotpot'
    res_name = db.Column(db.Text, primary_key=True)

    beef = db.Column(db.Float)
    fresh = db.Column(db.Float)
    good = db.Column(db.Float)
    environment = db.Column(db.Float)
    flavor = db.Column(db.Float)
    convenience = db.Column(db.Float)
    service = db.Column(db.Float)
    meat = db.Column(db.Float)
    fruit = db.Column(db.Float)
    buffet = db.Column(db.Float)
    seafood = db.Column(db.Float)
    shrimp = db.Column(db.Float)
    mutton = db.Column(db.Float)

    def __repr__(self):
        return "res_name:`{}`,  beef:`{}`,fresh:`{}`,good:`{}`,environment:`{}`,flavor:`{}`,convenience:`{}`,service:`{}`,meat:`{}`,fruit:`{}`,buffet:`{}`,seafood:`{}`,shrimp:`{}`,mutton:`{}`".format(self.res_name, self.beef, self.fresh, self.good, self.environment, self.flavor, self.convenience, self.service, self.meat, self.fruit, self.buffet, self.seafood, self.shrimp, self.mutton)