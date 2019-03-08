from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#class GroupingWaitPage(CustomMTurkWaitPage):
#    pass

# must be custom mturk wait page
class Decision(Page):
    pass

page_sequence = [
    # GroupingWaitPage
    Decision,
]
