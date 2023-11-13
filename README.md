<div align = "center">
<pre>
████████╗███████╗██╗  ██╗████████╗  ████████╗ █████╗   ██████╗ ███╗  ██╗ ██████╗ 
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝  ╚══██╔══╝██╔══██╗  ██╔══██╗████╗░██║██╔════╝░
░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░  ░░░██║░░░██║░░██║  ██████╔╝██╔██╗██║██║░░██╗░
░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░  ░░░██║░░░██║░░██║  ██╔═══╝░██║╚████║██║░░╚██╗
░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░  ░░░██║░░░╚█████╔╝  ██║░░░░░██║░╚███║╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░╚══╝░╚═════╝░
---------------------------------------------------------------------------------
python cli program to covert text to png
</pre>
</div>

# String to Image Converter
Installer installation documentation: https://COMMANDO2406.github.io/TextToPng/

Clone installation documentation: https://COMMANDO2406.github.io/TextToPng/pyinstalled.html

This Python script converts a given string into binary format and saves it as a monochrome image using the Python Imaging Library (PIL). It could be useful for simple data encoding or image manipulation projects. This project was inspired by Infinite-Storage-Glitch by https://github.com/DvorakDwarf/Infinite-Storage-Glitch.

# How to Use
Make sure you have PIL installed. You can install it using pip: pip install Pillow

Run the script and enter the string you would like to be converted. The output image will be saved as 'output_image.png' in the same directory as the script.

# How it Works
1. The script reads the input string and converts it to binary format using ASCII encoding.

2. The binary data is converted into a list of pixels, with each pixel represented as a list of eight bits.

3. The script creates a new monochrome image with the dimensions 8xlen(pixels), where len(pixels) is the number of rows needed to represent all the bits.

4. The image is saved as a PNG file with the name 'output_image.png'.

# Customization
You can customize the script to suit your needs by modifying the input file name, the output file name, or the image dimensions. You could also modify the code to include error handling, support different image formats, or use different encoding schemes.

# Dependencies
1. Python 3.x
2. Pillow (Python Imaging Library)
