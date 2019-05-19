#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db

class dessert(db.Model):
    __tablename__ = 'dessert'
    res_name = db.Column(db.Text, primary_key=True)
    # res_name = db.Column(db.text)


    cake = db.Column(db.Float)
    good = db.Column(db.Float)
    mango = db.Column(db.Float)
    flavor = db.Column(db.Float)
    cream = db.Column(db.Float)
    stratiform_cake = db.Column(db.Float)
    cheese_cake = db.Column(db.Float)
    cheese = db.Column(db.Float)
    cheap = db.Column(db.Float)
    milktea = db.Column(db.Float)
    good_drink = db.Column(db.Float)
    pearl_milktea = db.Column(db.Float)
    group_purchase = db.Column(db.Float)
    convenience = db.Column(db.Float)
    milk_cover = db.Column(db.Float)
    tea = db.Column(db.Float)
    matcha = db.Column(db.Float)
    durian = db.Column(db.Float)
    puff = db.Column(db.Float)


    def __repr__(self):
        return "res_name:`{}`, cake:`{}`,good:`{}`,mango:`{}`,flavor:`{}`,cream:`{}`,stratiform_cake:`{}`,cheese_cake:`{}`,cheese:`{}`,cheap:`{}`,milktea:`{}`,good_drink:`{}`,pearl_milktea:`{}`,group_purchase:`{}`,convenience:`{}`,milk_cover:`{}`,tea:`{}`,matcha:`{}`,durian:`{}`,puff:`{}`".format(self.res_name, self.cake, self.good, self.mango, self.flavor, self.cream, self.stratiform_cake, self.cheese_cake, self.cheese, self.cheap, self.milktea, self.good_drink, self.pearl_milktea, self.group_purchase, self.convenience, self.milk_cover, self.tea, self.matcha, self.durian, self.puff)