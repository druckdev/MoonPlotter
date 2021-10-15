# MoonPlotter
A small app which scrapes a persons logbook data from the moonboard website and provides some interesting graphs.


**Setup for development :**
Install 'geckodriver' (driver for firefox) 

Using the aur (which threw a bunch of 404s for me):
`ỳay -S aur/geckodriver-hg`

Using pip:
`pip install get-gecko-driver`

If necessary install 'Selenium' (for scraping).
`pip install selenium`

And also 'kivy' (for UI).
`pip install kivy`

Install 'matplotlib' (for plotting the data).
`pip install "matplotlib<3.3.0"`
and
`garden install matplotlib`

**Building for production :**

Install 'buildozer' for building the app for android.
`pip install buildozer`

Build with
`buildozer android release`
The .apk is then placed in the created bin folder.
First builds take some time because buildozer installs a bunch of tools.

The config file is located in `./buildozer/buildozer.spec`.


**Options for starting MoonPlotter.py :**

| description                     | usage                                  |
----------------------------------------------------------------------------
| username of a moonboard account | -u <username> or --username <username> |
| password to the username        | -p <password> or --password <password> |
| whether to (user) cache data    | -c or --cache                          |
| debug mode shows the browser    | -d or --debug                          |
