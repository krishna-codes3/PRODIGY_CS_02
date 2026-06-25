from PIL import Image
import os

def encrypt_decrypt(image_path, key):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    return img

print("=== Image Encryption Tool ===")
choice = input("1. Encrypt  2. Decrypt\nChoose: ")
path = input("Image path: ")
key = int(input("Key (1-255): "))

result = encrypt_decrypt(path, key)

if choice == "1":
    out = "encrypted_output.jpg"
else:
    out = "decrypted_output.jpg"

result.save(out)
print(f"Done! Saved as: {out}")