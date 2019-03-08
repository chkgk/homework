from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# revelation probably also has to become a custom mturk page for it to be skipped

class RevelationWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        pass


class Revelation(Page):
    pass


page_sequence = [
    RevelationWaitPage,
    Revelation
]
