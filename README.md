# pdf-compression-application
A tkinter (customtkinter) based application for pdf compression.

## Installation
Install all the required dependencies using requirement.txt file

You will also need to install something called [GhostScript](https://www.ghostscript.com/).<br>
Please make sure that you add the bin folder of GhostScript to system environment path.

To create the executable, run
```bash
pyinstaller --name PDFTool --onefile --windowed --noconsole --icon=icon.ico pdftool.py
```
    Note: You can modify the exe making according to you preference.

## Working
Run the application.py file using the command
```
python pdftool.py
```
then select a pdf file using "Upload" button and then press "Compress"

## Making a standalone GUI
In order to make GUI standalone application, make sure to follow these steps
1. Download [GhostScript](https://www.ghostscript.com/)
2. Navigate to Program Files and locate folder named "gs"
3. Navigate to bin folder in gs and add the path to environment variables
4. Run the command for executable as shown in the [Installation](#installation) tab
5. You will get you exe generated in the dist folder.

## Conclusion
This application was made as a hoppy project using GhostScript open-source license, feel free to make changes, and make the experience friendly.

~ with love from whenOUI