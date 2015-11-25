# create_stego_zip_jpg.py - Hide a zip file inside a JPEG

import sys

# Start with a jpeg file
with open(sys.argv[1], 'rb') as jpg_file:  # Path to JPG file
	jpg_data = jpg_file.read()
	
# And the zip file to embed in the jpeg
with open(sys.argv[2], 'rb') as zip_file:  # Path to ZIP file
	zip_data = zip_file.read()
	
# Combine the files
with open('special_image.jpg', 'wb') as out_file: # Output file
	out_file.write(jpg_data)
	out_file.write(zip_data)

# The resulting output file appears like a normal jpeg but can also be
# unzipped and used as an archive.