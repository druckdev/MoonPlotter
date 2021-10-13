# MoonPlotter
A small app which scrapes a persons logbook data from the moonboard website and provides some interesting graphs.


**Setup :**
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

**Building :**

Install 'buildozer' for building th app for android.
`pip install buildozer`

Build with
`buildozer -v android debug`

The config file is located in `./buildozer/buildozer.spec`.