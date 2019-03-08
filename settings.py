from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'social_norms',
        'display_name': 'Old Social Norms Experiment',
        'num_demo_participants': 6,
        'app_sequence': ['social_norms'],
        'treatment': 'public',  # choose either "public" or "private"
        'advice': 'C'  # choose one of the options in the table.
    },
    {
        'name': 'sn_advisors',
        'display_name': "SN - Advisors",
        'num_demo_participants': 2,
        'app_sequence': ['sn_advisors'],
    },
    {
        'name': 'sn_intro',
        'display_name': "SN - Intro",
        'num_demo_participants': 2,
        'app_sequence': ['sn_intro'],
    },
    {
        'name': 'sn_decisions',
        'display_name': "SN - Decisions",
        'num_demo_participants': 4,
        'app_sequence': ['sn_decisions'],
    },
    {
        'name': 'sn_results',
        'display_name': "SN - Results",
        'num_demo_participants': 4,
        'app_sequence': ['sn_results'],
    },
    {
        'name': 'sn_outro',
        'display_name': "SN - Survey",
        'num_demo_participants': 2,
        'app_sequence': ['sn_outro'],
    }
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'f^35@(6l-h1x4*1vppflz$l5op=adf5(eo4&z!)ru8(zsa=42j'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
EXTENSION_APPS  = ['otree_mturk_utils']