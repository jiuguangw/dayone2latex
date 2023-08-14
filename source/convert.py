#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 by Jiuguang Wang (www.robo.guru)
# All rights reserved.
# This file is released under the MIT License.
# Please see the LICENSE file that should have been included as part of
# this package.

# Parts adapted from https://github.com/elkrause/convert_dayone_json_2_markdown_files

import json
import os
import re

# Setup
dayone_export_json = "Journal.json"  # name of the DayOne JSON export file
target_folder = "../content/"

# Read JSON file
with open(dayone_export_json, encoding="utf8") as f:
    dayone_entries = json.load(f)

# Loop through each entry
for entry in dayone_entries["entries"]:
    # Formatting
    str_entry_creationDate = entry["creationDate"]
    str_entry_creationDate = str_entry_creationDate.replace("T", " ")
    slice_object = slice(-1)
    str_entry_creationDate = str_entry_creationDate[slice_object]
    slice_object = slice(-9)  # remove time, keep only date
    str_entry_creationDate_heading = str_entry_creationDate.replace(":", ".")
    str_entry_folder = target_folder + str_entry_creationDate_heading[:4]
    str_entry_creationDate_heading = str_entry_creationDate_heading[
        slice_object
    ]

    # DayOne entry text content
    str_entry_text = entry["text"]

    # Tex file name
    str_entry_creationDate_filename = (
        str_entry_folder + "/" + str_entry_creationDate_heading + ".tex"
    )

    print("Converting Day One entry: ", str_entry_creationDate_heading)

    # Create folder if it does not exists already
    if not os.path.exists(str_entry_folder):
        os.makedirs(str_entry_folder)

    # Day One added characters
    str_entry_text = str_entry_text.replace("\\", "")

    # Issues
    str_entry_text = str_entry_text.replace("’", "'")
    str_entry_text = str_entry_text.replace("#", "\\#")

    # Standard LaTeX special characters
    str_entry_text = str_entry_text.replace("&", "\\&")
    str_entry_text = str_entry_text.replace("%", "\\%")
    str_entry_text = str_entry_text.replace("$", "\\$")
    str_entry_text = str_entry_text.replace("_", "\\_")
    str_entry_text = str_entry_text.replace("{", "\\{")
    str_entry_text = str_entry_text.replace("}", "\\}")
    str_entry_text = str_entry_text.replace("~", "\\~")
    str_entry_text = str_entry_text.replace("^", "\\^")

    # Other issues
    str_entry_text = str_entry_text.replace("“", "``")
    str_entry_text = str_entry_text.replace("”", "''")

    # Convert first line to chapter title
    # Currently assumes line starts with Markdown heading "#"
    str_entry_text = re.sub(
        r"# (.*)",
        r"\\section{\1}\n\\label{sec:"
        + str_entry_creationDate_heading
        + "}\n",
        str_entry_text,
    )
    str_entry_text = str_entry_text.replace("\\\\", "\\")

    # Remove sub heading
    str_entry_text = re.sub(r" - .*?\}", r"}", str_entry_text)

    # Remove photo reference
    str_entry_text = re.sub(r"!\[\]\(.*\)", "", str_entry_text)

    # Write Tex files
    with open(str_entry_creationDate_filename, "w", encoding="utf-8") as file:
        file.write(
            "% Texted generated from Day One journal app, do not edit"
            " directly.\n"
        )
        file.write("% ")
        file.write(str_entry_creationDate_heading)
        file.write("\n\n")
        file.write(str_entry_text)
        file.write("\n\n")
        file.write("\\smallskip \n\n")
        if entry.get("location"):
            entry_location = entry["location"]
            file.write("\\begin{footnotesize}\n")
            file.write("\\faLocationArrow \\quad ")
            if entry_location.get("placeName"):
                file.write(entry_location["placeName"])
            if (
                entry_location.get("localityName")
                and entry_location.get("administrativeArea")
                and entry_location.get("country")
            ):
                file.write(", ")
                file.write(entry_location["localityName"])
                file.write(", ")
                file.write(entry_location["administrativeArea"])
                file.write(", ")
                file.write(entry_location["country"])
                file.write(" \n")
            file.write("\\end{footnotesize}\n\n")
            file.write("\\vspace{-5 mm}\n")
        if entry.get("weather"):
            entry_weather = entry["weather"]
            file.write("\\begin{footnotesize}\n")
            file.write("\\faThermometerThreeQuarters \\quad\\enspace")
            if entry_weather.get("temperatureCelsius") and entry_weather.get(
                "conditionsDescription"
            ):
                file.write(str(int(entry_weather["temperatureCelsius"])))
                file.write(" \\textdegree{}C, ")
                file.write(entry_weather["conditionsDescription"])
                file.write(" \n")
            file.write("\\end{footnotesize}\n")
        # file.write('\\pagebreak')
        file.write("\n")
    file.close()

print("Done!")
