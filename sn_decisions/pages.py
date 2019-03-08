from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage


class GroupingWaitPage(CustomMturkWaitPage):
    group_by_arrival_time = True
    use_task = False
    startwp_timer = 180
    skip_until_the_end_of = 'experiment'


# must be custom mturk wait page
class Decision(CustomMturkPage):
    pass

page_sequence = [
    # GroupingWaitPage
    Decision,
]
