#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db


class fastfood(db.Model):
    __tablename__ = 'fastfood'
    res_name = db.Column(db.Text, primary_key=True)
    flavor = db.Column(db.Float)
    mutton_noodles = db.Column(db.Float)
    mutton = db.Column(db.Float)
    environment = db.Column(db.Float)
    soup = db.Column(db.Float)
    rice_noodles = db.Column(db.Float)
    good = db.Column(db.Float)
    beef_offal = db.Column(db.Float)
    chilli_sauce = db.Column(db.Float)
    beef_offal_noodles = db.Column(db.Float)
    fried_bun = db.Column(db.Float)
    duck_noodles = db.Column(db.Float)
    bean_noodles = db.Column(db.Float)
    cake = db.Column(db.Float)
    bread = db.Column(db.Float)
    group_purchase = db.Column(db.Float)
    convenience = db.Column(db.Float)
    soup_liquid = db.Column(db.Float)
    haggis = db.Column(db.Float)

    def __repr__(self):
        return "res_name:`{}`, flavor:`{}`,mutton_noodles:`{}`,mutton:`{}`,environment:`{}`,soup:`{}`,rice_noodles:`{}`,good:`{}`, beef_offal:`{}`,chilli_sauce:`{}`,beef_offal_noodles:`{}`,fried_bun:`{}`,duck_noodles:`{}`,bean_noodles:`{}`,cake:`{}`,bread:`{}`,group_purchase:`{}`,convenience:`{}`,soup_liquid:`{}`,haggis:`{}`".format(self.res_name, self.flavor, self.mutton_noodles, self.mutton, self.environment, self.soup, self.rice_noodles, self.good, self.beef_offal, self.chilli_sauce, self.beef_offal_noodles, self.fried_bun, self.duck_noodles, self.bean_noodles, self.cake, self.bread, self.group_purchase, self.convenience, self.soup_liquid, self.haggis)