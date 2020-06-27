"""
Shortcuts Loader
"""
import os
import json
import logging

logger = logging.getLogger(__name__)

DEFAULT_IMAGE_PATH = 'images/icons/default.png'

USER_SHORTCUTS_PATH = os.path.join(os.path.expanduser("~"), '.config',
                                   'ulauncher', 'ext_preferences', 'shortcuts')

OVERRIDE_FILES_PATH = os.path.join(os.path.expanduser("~"), '.config',
                                   'ulauncher', 'ext_preferences', 'shortcuts',
                                   'overrides')


class ShortcutsLoader():
    """ Loads and parses the shortcuts files """
    def load(self):
        """ Parses the shortcuts definition files and load the appplications into memory """
        default_apps = self.__load_default_apps()
        user_apps = self.__load_user_apps()
        return sorted(default_apps + user_apps, key=lambda x: x["name"])

    def __load_default_apps(self):
        """ Loads the shortcuts for default applications that are provided by the extension """
        folder = os.path.join(os.path.dirname(__file__), '..', 'data')
        return self.__process_shorctus_files(folder, False)

    def __load_user_apps(self):
        """ Loads any custom shortcuts for the user """
        if not os.path.isdir(USER_SHORTCUTS_PATH):
            return []

        return self.__process_shorctus_files(USER_SHORTCUTS_PATH, True)

    def __get_override_file(self, app):
        """ Checks if the application have an override file by the user and load that instead """
        file_path = os.path.join(OVERRIDE_FILES_PATH, "%s.json" % app)

        if os.path.isfile(file_path):
            return file_path

        return None

    def __process_shorctus_files(self, folder, is_user=False):
        """ Processes the shortcuts files and load the defined shortcuts to memory """
        items = []
        for filename in os.listdir(folder):

            if not filename.endswith(".json"):
                continue

            app_code = filename.split(".")[0]

            full_path = self.__get_override_file(app_code) or os.path.join(
                folder, filename)

            with open(full_path) as f:
                try:
                    data = json.load(f)
                    data["path"] = full_path
                    data["icon"] = DEFAULT_IMAGE_PATH
                    if is_user:
                        icon_file = os.path.join(folder, 'icons',
                                                 "%s.png" % app_code)
                        if os.path.isfile(icon_file):
                            data["icon"] = icon_file
                    else:
                        data["icon"] = 'images/icons/%s.png' % app_code

                    items.append(data)
                except json.JSONDecodeError as e:
                    logger.warn("Cannot parse shortcuts file %s - %s" %
                                (filename, e))
        return items
