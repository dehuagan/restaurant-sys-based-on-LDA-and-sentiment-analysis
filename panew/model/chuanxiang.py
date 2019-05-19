#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db


class chuanxiang(db.Model):
    __tablename__ = 'chuanxiang'
    res_name = db.Column(db.Text, primary_key=True)

    good = db.Column(db.Float)
    flavor = db.Column(db.Float)
    chilli_fish_head = db.Column(db.Float)
    pettitoes = db.Column(db.Float)
    spicy = db.Column(db.Float)
    roast_fish = db.Column(db.Float)
    service = db.Column(db.Float)
    qingjiang_fish = db.Column(db.Float)
    pickled_fish = db.Column(db.Float)
    environment = db.Column(db.Float)
    performance = db.Column(db.Float)
    attitude = db.Column(db.Float)
    fish = db.Column(db.Float)
    line = db.Column(db.Float)

    def __repr__(self):
        return "res_name:`{}`, good:`{}`,flavor:`{}`,chilli_fish_head:`{}`,pettitoes:`{}`,spicy:`{}`,roast_fish:`{}`,service:`{}`,qingjiang_fish:`{}`,pickled_fish:`{}`,environment:`{}`,performance:`{}`,attitude:`{}`,fish:`{}`,line:`{}`".format(self.res_name, self.good, self.flavor, self.chilli_fish_head, self.pettitoes, self.spicy, self.roast_fish, self.service, self.qingjiang_fish, self.pickled_fish, self.environment, self.performance, self.attitude, self.fish, self.line)