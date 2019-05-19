#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db


class western_food(db.Model):
    __tablename__ = 'western_food'
    res_name = db.Column(db.Text, primary_key=True)
    good = db.Column(db.Float)
    environment = db.Column(db.Float)
    flavor = db.Column(db.Float)
    snack = db.Column(db.Float)
    drinks = db.Column(db.Float)
    fried_tofu = db.Column(db.Float)
    rice = db.Column(db.Float)
    steak = db.Column(db.Float)
    service = db.Column(db.Float)
    chips = db.Column(db.Float)
    cake = db.Column(db.Float)
    package = db.Column(db.Float)
    durian_egg = db.Column(db.Float)
    dessert = db.Column(db.Float)
    buffet = db.Column(db.Float)
    fruit = db.Column(db.Float)
    corn_soup = db.Column(db.Float)


    def __repr__(self):
        return "res_name:`{}`, good:`{}`,environment:`{}`,flavor :`{}`,snack :`{}`,drinks:`{}`,fried_tofu:`{}`,rice :`{}`,steak:`{}`,service:`{}`,chips:`{}`,cake:`{}`,package :`{}`,durian_egg:`{}`,dessert:`{}`,buffet:`{}`,fruit:`{}`,corn_soup:`{}`".format(self.res_name, self.good, self.environment, self.flavor, self.snack, self.drinks, self.fried_tofu, self.rice, self.steak, self.service, self.chips, self.cake, self.package, self.durian_egg, self.dessert, self.buffet, self.fruit, self.corn_soup)