<p align="center">
  <h1 align="center">DayOne2LaTeX</h1>
  <p align="center">
    <a href="https://github.com/jiuguangw/dte_calculator/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
  </p>
</p>

## Overview

DayOne2LaTeX converts a journal written in the [Day One](http://dayoneapp.com) app into a LaTeX book.

While Day One has functionalities to export journal entries as a PDF, the functionality is very limited and the user does not have any control over formatting. To get around the limitations, this utility uses Day One's built-in JSON export feature to obtain access to the journal contents (and other bells and whistles such as location and weather data), then converts the Markdown formatted text into a LaTeX document.

See [Main.pdf](Main.pdf) for the example output.

## Getting Started

### Installing Anaconda Python (Recommended)

All perquisites are installed as a part of [Anaconda Python](https://www.anaconda.com/distribution/#download-section).

Supported Configurations:

| OS      | Python version |
| ------- | -------------- |
| MacOS   | 3.7  |
| Ubuntu  | 3.7  |
| Windows | 3.7  |

### Cloning the repo

To checkout the repo:

```bash
git clone git@github.com:jiuguangw/dayone2latex.git
```

### Day One - formatting and export

To achieve the best results, the script assumes the Day One entries are formatted such that the first line contains the title, in the H1 style. See for example:

![Day One](docs/dayone.jpg?raw=true)

To export the entries, go to the gear icon on the top right of the app, "Import / Export", then "Export Day One JSON (.zip)". The exported file can be found in iCloud or AirDropped to a Mac. Unzip the file and place Journal.json inside the "source" directory.

The script also assumes you have assigned a location to the entry and the Day One app has fetched the corresponding weather data for that day.

See [Journal.json](source/Journal.json) for an sample JSON output.


### Running the script
```bash
(dayone2latex)$ cd source
(dayone2latex)$ python convert.py
```
.tex files are then generated inside the "content" directory, one .tex per entry, sorted by year. As Day One does not currently allow exporting specific entries, the script currently export every available entry. The author can make a manual selection during the book layout process in LaTeX.

See [content](content) for sample .tex outputs.

### Formatting the book

At least a few edits are needed to the LaTeX template. In `Main.tex`, your book and author information:

```
\newcommand{\authorname}{William Shakespeare}
\newcommand{\booktitle}{My Day One Journal}
\newcommand{\subtitle}{}
\newcommand{\publisher}{New York, NY}
\newcommand{\editionyear}{2020}
\newcommand{\isbn}{000-0-00-0000-0}
```

In `Journal.sty`, edit the page trim settings:

```
\usepackage[
    paperheight=10in,
    paperwidth=8in,
    top=0.76in,
    bottom=0.76in,
    outer=0.6in,
    inner=0.875in
]{geometry}
```
Currently the book is formatted as a 10x8 book, suitable for printing using [Kindle Direct Publishing](https://kdp.amazon.com/en_US/),

Finally, for every entry you would like to include in the book, edit `Main.tex` to include the file:

```
\input{content/2020/2020-06-08}
```

### Compile the book

A LaTeX TeXLive distribution is recommended. On macOS, it is [MacTeX](https://github.com/jiuguangw/dayone2latex/blob/master/Main.pdf). I also recommend the IDE [TexPad](https://www.texpad.com), although there are many other free alternative IDEs.

To layout the book, fire up your favorite LaTeX IDE and compile `Main.tex`. LuaTeX is recommended for its Unicode and microtype support. If using pdfTeX or XeLaTeX, please remove the following line from Journal.sty:

```
\usepackage[activate={true,nocompatibility},final,tracking=true,factor=1100,stretch=10,shrink=10]{microtype}
```

See [Main.pdf](Main.pdf) for the example output.

### Limitations

Currently, this utility intentionally does not include contents such as photos and hashtags in the entry. While they are easy to include in the script, I believe most users would want to manually insert photos as 1) figure placement in LaTeX is more of an art than a science and 2) Day One embedded photos are downsampled and often not print quality.

## License

### License terms

Everything is released under the MIT license. The full license details can be found in [LICENSE](LICENSE). If you do end up publishing the book, I'd appreciate an acknowledgment.

### Technical contributions

I welcome bug fixes, feature additions, and other ways to improve the project. Please send me pull requests, issues, etc, and contact me if you'd like to be added as a collaborator to the repo.

For others without the time or skills to contribute, I'd also appreciate your help in spreading the word via Facebook, Twitter, etc.

### Donation

Please support the project by making a donation via PayPal or crypto:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=N49BVZZLEXU4G&source=url)

![Bitcoin](https://img.shields.io/badge/Bitcoin-367dGyWPSfSjiP6Nh8oSmdCG9MPkMB58Ad-orange.svg?style=flat-square)
![Ethereum](https://img.shields.io/badge/Ethereum-0x4617f57f8b0e3D09Be50CcB32451A2CD20651262-orange.svg?style=flat-square)
![Bitcoin Cash](https://img.shields.io/badge/Bitcoin%20Cash-qrz4e6n3g7e2q6gqz4wetxlgk5eztskxag7tss982j-orange.svg?style=flat-square)
![Litecoin](https://img.shields.io/badge/Litecoin-MVdpa3uXnqoLkZFoarqNnGB9KHr6TL8xst-orange.svg?style=flat-square)

## Contact

- Jiuguang Wang
- [jw@robo.guru](mailto:jw@robo.guru?subject=DTE)
- [www.robo.guru](https://www.robo.guru)

Please drop me a line!
