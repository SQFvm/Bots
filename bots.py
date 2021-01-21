import logging

from discord_base import BotBase


logger = logging.getLogger('discord.' + __name__)


class SQFBot(BotBase):
    startup_extensions = [
        'cogs.server',
        'cogs.restart',
    ]

    def __init__(self, bot_data):
        super().__init__(
            command_prefix='!',
            description='SQFBot butler at your service! :)',
            pm_help=True,
        )
        self.bot_data = bot_data
