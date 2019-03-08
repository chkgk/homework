from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage

class Results(CustomMturkPage):
    pass

class Questionnaire(CustomMturkPage):
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
