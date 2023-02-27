# kindle-note-to-anki-File

Kindle Note to Anki File
========================

This repository contains a simple Python script to convert the highlight notes from a Kindle device to an Anki file. The script reads a Kindle file and generates an output file that can be imported into Anki.

Installation
------------

To use this script, follow these steps:

1.  Move the Kindle file from the phone to your PC
2.  Clone the repository
3.  Create a virtual environment using the following command:


`virtualenv env`

1.  Activate the virtual environment. If you are on Mac OS, use the following command:


`source env/bin/activate`

If you are on Windows, use the following command instead:

`.\env\Scripts\activate`

1.  Install the required packages by running the following command:

`pip install -r requirements.txt`

Usage
-----

Once you have completed the installation steps, you can use the script as follows:

1.  Start the application by running the following command:

`python app/main.py`

1.  When prompted, enter the full path to the Kindle file.

2.  The script will generate an output file named "output" in the same location as the repository.

3.  Import the "output" file into Anki.

Note
----

This script has been tested with Kindle files format. If your Kindle file is in a different format, this script may not work.
