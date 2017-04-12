from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from django import forms
import time
import datetime
author = 'Filipp Chapkovskii, UZH, chapkovski@gmail.com'

doc = """
ebay auction example
"""


class Constants(BaseConstants):
    name_in_url = 'ebay'
    players_per_group = 2
    num_rounds = 1
    # starting_time = 30
    # extra_time = 20
    endowment = 100
    prize = 200
    num_others = players_per_group - 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for g in self.get_groups():
            g.price = 0


class Group(BaseGroup):
    price = models.IntegerField()
    winner = models.IntegerField()


    def set_payoffs(self):
        ...

class Player(BasePlayer):
    price = models.IntegerField()
