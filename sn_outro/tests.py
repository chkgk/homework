from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        # if not dropped out:
        yield (pages.Results)
        yield (pages.Questionnaire)

        # if dropped out:
        yield (pages.Dropouts)
