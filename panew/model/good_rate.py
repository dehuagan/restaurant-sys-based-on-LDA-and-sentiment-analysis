#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panew import db


class good_rate(db.Model):
    __tablename__ = 'good_rate'
    res_name = db.Column(db.Text, primary_key=True)

    rate = db.Column(db.Float)


    def __repr__(self):
        return "res_name:`{}`,  rate :`{}`".format(self.res_name, self.rate)