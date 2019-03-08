from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage

class RevelationWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        pass


class Revelation(CustomMturkPage):
    timeout_seconds = 20


page_sequence = [
    RevelationWaitPage,
    Revelation
]
