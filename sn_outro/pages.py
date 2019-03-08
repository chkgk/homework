from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# these all need to become custom mturk wait pages, except for the dropout one

class Results(Page):
    pass

class Questionnaire(Page):
    pass

class Dropouts(Page):
    # def is_displayed(self):
    #     return self.player.participant.vars.get('go_to_the_end', False)
    pass


page_sequence = [
    Results,
    Questionnaire,
    Dropouts
]
