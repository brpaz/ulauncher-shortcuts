""" Main Module """

import logging
import os
import subprocess
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from shortcuts.service import ShortcutsService
from shortcuts.loader import ShortcutsLoader

logger = logging.getLogger(__name__)


class ShortcutsExtension(Extension):
    """ Main Extension Class  """
    def __init__(self):
        """ Initializes the extension """
        super(ShortcutsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.shortcuts_service = ShortcutsService(ShortcutsLoader())

    def show_applications(self, query):
        """ shows the list of available applications known by the extension """
        apps = self.shortcuts_service.get_applications(query)

        if not apps:
            return RenderResultListAction([
                ExtensionSmallResultItem(
                    icon='images/icon.png',
                    name='No applications found matching your criteria',
                    highlightable=False,
                    on_enter=HideWindowAction())
            ])

        items = []
        for app in apps[:15]:
            items.append(
                ExtensionSmallResultItem(icon=app['icon'],
                                         name=app['name'],
                                         on_enter=ExtensionCustomAction({
                                             "action":
                                             "show",
                                             "app":
                                             app,
                                         }),
                                         on_alt_enter=OpenUrlAction(
                                             app['reference_url'])))
        return RenderResultListAction(items)

    def show_shortcuts_window(self, app):
        """ Shows the shortcuts window """
        script_path = os.path.join(os.path.dirname(__file__), 'ui', 'main.py')

        cmd = "python %s --file %s" % (script_path, app["path"])

        result = subprocess.run(cmd,
                                shell=True,
                                stdin=None,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                close_fds=True)

        print(result)
        if result.returncode != 0:
            logger.error("Error Opening shortcuts window: " +
                         str(result.stderr))

    def refresh_shortcuts(self):
        """ Refreshes the shortcuts """
        return RenderResultListAction([
            ExtensionSmallResultItem(
                icon='images/icon.png',
                name='Refresh Shortcuts',
                description='Press enter to refresh shortcuts',
                highlightable=False,
                on_enter=ExtensionCustomAction({"action": "refresh"}))
        ])


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """
    def on_event(self, event, extension):
        """ Handles the event """
        query = event.get_argument() or ""

        if query == "refresh":
            return extension.refresh_shortcuts()

        return extension.show_applications(query)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()

        if data["action"] == "refresh":
            extension.shortcuts_service.load()
            return

        extension.show_shortcuts_window(data["app"])


if __name__ == '__main__':
    ShortcutsExtension().run()
