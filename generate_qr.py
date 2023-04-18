import qrcode
import webbrowser
import os

# Read the HTML data from a file
with open('student.html', 'r') as f:
    data = f.read()

# Write the HTML data to a file with a .html extension
with open('student_details.html', 'w') as f:
    f.write(data)

# Generate a QR code containing a URL to the HTML file
url = 'file://' + os.path.abspath('student_details.html')
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
img.save('QR_codes/student_details_qr.png')

# # Open the HTML file in the default web browser
# webbrowser.open('file://' + os.path.abspath('student.html'))
