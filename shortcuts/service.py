"""
Handles Shortcuts
"""
import logging

logger = logging.getLogger(__name__)


class ShortcutsService:
    """ Service that manages the shortcuts """
    def __init__(self, loader):
        """ Constructor method """
        self.apps = []
        self.loader = loader

        self.load()

    def load(self):
        """ Loads the shortcuts """
        self.apps = self.loader.load()

    def get_applications(self, query):
        """ Returns a list of registered applications """

        if not query:
            return self.apps

        return list(
            filter(lambda item: query.lower() in item['name'].lower(),
                   self.apps))
