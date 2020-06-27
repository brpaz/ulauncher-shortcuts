# Adding your own shortcuts

There are two ways you can add your own shortcuts to this extension: 

- You can do a PR and add the shortcuts to the extension itself so other users can use it
- Add to your own machine.

If you choose the second option, you can do first by creating the following directory structure on `~/.config/ulauncher/ext_preferences/shortcuts`:

```
.
├── <appname>.json
└── icons
    └── <appname>.png
```

The json file will contain the shortcuts definition and needs to be in the following format:

```json
{
    "name": "Your application name",
    "reference_url": "An url for a reference page with the keyboard shortcuts",
    "sections": [
        {
            "name": "Universal",
            "shortcuts": [
                {
                    "description": "Cancels Blender functions without changes",
                    "keys": [
                        "Esc"
                    ]
                },
                {
                    "description": "Open the toolbox",
                    "keys": [
                        "Space"
                    ]
                }
        }
    ]
}
```

You can have any number of sections to organize your shortcuts. The keys should be an array where is element is a key from the key combination.

For example, if your shortcut is `Ctrl+Shift+A` you would define like this:

```json
"keys": [
    "Ctrl",
    "Shift",
    "A"
]
```

Internally this application, formats the keys to the format supported by GTK but you dont need to worry about it. If you use the known key name or symbol, it should work in most cases. If you found out that same key is not being displayed correctly, please open an issue.

Here is a table of some special keys that you can use:

| Name      |
| --------- |
| Esc       |
| Ctrl      |
| Shift     |
| Space     |
| Enter     |
| Backspace |
| PageUp    |
| PageDown  |
| Home      |
| End       |
| Insert    |
| Delete    |


# Override default shortcuts

It´s normal to modify the default applications shortcuts according to the users preferences.

You can override the default shortcuts for an application, by created a file in ```~/.config/ulauncher/ext_preferences/shortcuts/overrides``` with the name of the original file provided by the extension.

Ex: To override the VS Code shortcuts, create a file ```~/.config/ulauncher/ext_preferences/shortcuts/overrides/vscode.json```.

No need to define an icon as the original will be used.
