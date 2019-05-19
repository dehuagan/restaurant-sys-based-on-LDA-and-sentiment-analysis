#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db

class canton(db.Model):
    __tablename__ = 'canton'
    res_name = db.Column(db.Text, primary_key=True)

    good = db.Column(db.Float)
    flavor = db.Column(db.Float)
    chicken_feet = db.Column(db.Float)
    service = db.Column(db.Float)
    shrimp_dumpling = db.Column(db.Float)
    environment = db.Column(db.Float)
    rib = db.Column(db.Float)
    morning_tea = db.Column(db.Float)
    eat_food = db.Column(db.Float)
    group_purchase = db.Column(db.Float)
    fried_noodle = db.Column(db.Float)
    red_rice_roll = db.Column(db.Float)
    dim_sum = db.Column(db.Float)



    def __repr__(self):
        return "res_name:`{}`, good:`{}`,flavor:`{}`,chicken_feet:`{}`,service:`{}`,shrimp_dumpling:`{}`,environment:`{}`,rib:`{}`,morning_tea:`{}`,eat_food:`{}`,group_purchase:`{}`,fried_noodle:`{}`,red_rice_roll:`{}`,dim_sum:`{}`".format(self.res_name, self.good, self.flavor, self.chicken_feet, self.service, self.shrimp_dumpling, self.environment, self.rib, self.morning_tea, self.eat_food, self.group_purchase, self.fried_noodle, self.red_rice_roll, self.dim_sum)