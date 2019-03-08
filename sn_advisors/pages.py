from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Instructions(Page):
    pass


page_sequence = [
    Introduction,
    Instructions
]
