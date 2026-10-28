
# Data you want to encode
data = "https://example.com"

# Generate the QR code
img = qrcode.make(data)

# Save the image to a file
img.save("simple_qr.png")
print("QR Code generated successfully!")
