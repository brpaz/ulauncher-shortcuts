import gi
import argparse
import json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # noqa: E402

GTK_KEYS_MAPPER = {
    "Enter": "Return",
    "Esc": "Escape",
    ".": "period",
    ":": "colon",
    ">": "greater",
    "<": "less",
    "~": "dead_circumflex",
    "+": "plus",
    "-": "minus",
    "/": "slash",
    "'": "apostrophe",
    "*": "asterisk",
    "´": "dead_acute",
    "`": "dead_grave",
    ",": "comma",
    "\\": "backslash",
    "[": "bracketleft",
    "]": "bracketright",
    "?": "question",
    ";": "semicolon",
    "PgUp": "Page_Up",
    "PgDown": "Page_Down",
    "PgDn": "Page_Down",
    "PageDown": "Page_Up",
    "PageUp": "Page_Down",
    "Space": "space",
    "Backspace": "BackSpace"
}

MOD_KEYS = ["Ctrl", "Control", "Shift", "Super", "Alt"]


class ShortcutsWindow():
    """ Controls the Shortcuts Window """
    def __init__(self, app, shortcuts):
        """ Constructor method """
        self.app = app
        self.shortcuts = shortcuts

    def show(self):
        """ Shows the shortcuts window """

        win = Gtk.ShortcutsWindow()
        win.set_default_size(800, 600)
        win.set_position(Gtk.WindowPosition.CENTER)
        win.set_keep_above(True)
        win.set_skip_taskbar_hint(True)
        win.set_property("section-name", self.app)
        win.connect("destroy", Gtk.main_quit)
        widgets = self.build_shortcuts_view()

        for widget in widgets:
            win.add(widget)

        win.show_all()

        Gtk.main()

    def build_shortcuts_view(self):
        """ Builds the Shortcuts Section view Widgets """

        widgets = []
        for section in self.shortcuts:

            section_widget = Gtk.ShortcutsSection(title=section['name'],
                                                  section_name=section['name'])

            for i, shortcut in enumerate(section['shortcuts']):

                if i % 10 == 0:
                    group = Gtk.ShortcutsGroup()
                    section_widget.add(group)

                short = Gtk.ShortcutsShortcut(
                    title=shortcut["description"],
                    accelerator=self.parse_accelerator(shortcut['keys']))
                short.show()
                group.add(short)

            section_widget.show()
            widgets.append(section_widget)

        return widgets

    def parse_accelerator(self, keys=[]):
        """ Parses the shortcut into the GTK format """

        accelerator = []
        modifiers = keys[:len(keys) - 1]
        key = keys.pop()

        if key in GTK_KEYS_MAPPER:
            key = GTK_KEYS_MAPPER[key]

        for mod in modifiers:
            if mod in MOD_KEYS:
                accelerator.append("<%s>" % mod)
            else:
                accelerator.append(mod)

        accelerator.append(key)

        return "+".join(accelerator)


parser = argparse.ArgumentParser(description='Shortcuts Overlay')
parser.add_argument('--file',
                    required=True,
                    dest='file',
                    help='the shortcuts file')

args = parser.parse_args()

with open(str(args.file)) as f:
    data = json.load(f)
    ShortcutsWindow(data["name"], data["sections"]).show()
