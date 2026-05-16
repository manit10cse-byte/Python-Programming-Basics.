# QR Code Generator for GitHub Profile

# Import the qrcode library
import qrcode

# Store the GitHub profile link
github_link = "https://github.com/manit10cse-byte"

# Create a QR code object
qr_code = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

# Add the link to the QR code
qr_code.add_data(github_link)

# Generate the QR code
qr_code.make(fit=True)

# Create the image
qr_image = qr_code.make_image(
    fill_color="black",
    back_color="white"
)

# Save the QR code image
qr_image.save("github_qr.png")

# Display success message
print("QR Code created successfully!")
print("File saved as github_qr.png")
