# metadata-remover-app
About The Project
This is a simple yet powerful Python script designed to protect your privacy by removing all EXIF metadata from your image files.When you take a photo, your camera or smartphone embeds a lot of hidden information into the file, such as the location (GPS coordinates), date, time, and the specific model of the device used. This script helps you strip all of that potentially sensitive data, leaving you with a clean, metadata-free image.The core principle of this tool is safety: it never modifies your original file. Instead, it reads the pixel data from your source image and uses it to construct a brand new image from scratch. This new file contains only the visual information, ensuring that all metadata is discarded in the process.
Built With
Python
Pillow
Google Colab
Getting Started
This version of the script is specifically designed to run in a Google Colab environment, so you don't need to install any dependencies locally.
Usage
Open a new Google Colab notebook.
Copy the code from the metadata_remover.py file and paste it into a cell.
Run the cell.
An upload button will appear. Click it to select an image file (.jpg, .png, etc.) from your computer.
The script will process the file, remove the metadata, and automatically trigger your browser to download the cleaned version. The new file will have _bez_metadanych appended to its original name.
License
Distributed under the MIT License. See LICENSE for more information.
