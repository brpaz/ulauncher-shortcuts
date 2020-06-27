# ulauncher-shortcuts

> View your favorite applications shortcuts directly from Ulauncher

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-shortcuts/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-shortcuts)
[![license](https://img.shields.io/github/license/brpaz/ulauncher-shortcuts.svg?style=for-the-badge)](LICENSE)


## Demo

![demo](demo.gif)

## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) > 5.0
* Python >= 3

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-shortcuts
```

## Usage

Type the keyword `shortcuts` to display a list of applications. Press `enter` on one of the results to display a window with the application shortcuts.

The following applications are included by default (PRs welcome to add more):

* Blender
* Discord
* Firefox
* Gimp
* Google Chrome
* Gmail
* Jetbrains
* Notion
* Slack
* VS Code


### Refresh the shortcuts

This extension loads the shortcuts on startup. If you change them or added a new file, you can force the shortcuts reload with command:

```shortcuts refresh```

Or by restarting Ulauncher.

### Add your own or override default application shortcuts

You can add your own shortcuts or override the default ones. Please see [this](docs/add-your-shortcuts.md) guide.

## Development

```
git clone https://github.com/brpaz/ulauncher-shortcuts
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

## Contributing

All contributions are welcome. Just open an issue and/or create a PR.

If you like my work, feel free to "Buy me a Coffee"

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## Credits

* [UseTheKeyboard](https://usethekeyboard.com/) - for some shortcuts lists

## License

MIT &copy; [Bruno Paz]
