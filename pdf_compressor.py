#!/usr/bin/env python3
# Author: Theeko74
# Contributor(s): skjerns
# Oct, 2021
# MIT license -- free to use as you want, cheers.

"""
Simple python wrapper script to use ghoscript function to compress PDF files.

Compression levels:
    0: default - almost identical to /screen, 72 dpi images
    1: prepress - high quality, color preserving, 300 dpi imgs
    2: printer - high quality, 300 dpi images
    3: ebook - low quality, 150 dpi images
    4: screen - screen-view-only quality, 72 dpi images

Dependency: Ghostscript.
On MacOSX install via command line `brew install ghostscript`.
"""

import argparse
import os.path
import shutil
import subprocess
import sys
import tkinter.messagebox


def compress(input_file_path, output_file_path, power=4):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: "/default",
        1: "/prepress",
        2: "/printer",
        3: "/ebook",
        4: "/screen"
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        tkinter.messagebox.showerror("Error", f"Error: invalid path for input PDF file. {input_file_path}")
        return

    # Check compression level
    if power < 0 or power > len(quality) - 1:
        tkinter.messagebox.showerror("Error", f"Error: invalid compression level, run pdfc -h for options. {power}")
        return
    
    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        tkinter.messagebox.showerror("Error", f"Error: input file is not a PDF. {input_file_path}")
        return

    gs = get_ghostscript_path()
    # print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(
        [
            gs,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS={}".format(quality[power]),
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            # "-dColorConversionStrategy=/LeaveColorUnchanged",  # this line is added to prevent GhostScript 9.50 from converting all text to black (see https://stackoverflow.com/questions/58203881/ghostscript-9-50-makes-text-black-when-compressing-pdf)
            # "-dEncodeColorImages=false",  # this line is added to prevent GhostScript 9.50 from converting all text to black (see https://stackoverflow.com/questions/58203881/ghostscript-9-50-makes-text-black-when-compressing-pdf)
            "-sOutputFile={}".format(output_file_path),
            input_file_path,
        ]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    return ("Compression by {0:.0%}.".format(ratio) + "\n" + "Final file size is {0:.5f}MB".format(final_size / 1000000) + "\n" + "Done.\n")


def get_ghostscript_path():
    gs_names = ["gswin64", "gswin32", "gs"]
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(
        f"No GhostScript executable was found on path ({'/'.join(gs_names)})"
    )

