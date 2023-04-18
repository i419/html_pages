import qrcode
from PIL import Image

# Set the URL of the HTML file
url = 'file:///student_details.html'

# Create a QR code object
qr = qrcode.QRCode(version=None, box_size=10, border=4)

# Add the URL to the QR code object
qr.add_data(url)
qr.make(fit=True)

# Generate an image of the QR code
img = qr.make_image(fill_color='black', back_color='white')

# Save the image to a file
img.save('QR_codes/qr_code.png')

# Open the QR code image using PIL
img = Image.open('QR_codes/qr_code.png')

# Show the QR code image
img.show()
