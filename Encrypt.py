import cv2
import os

img = cv2.imread("mypic.jpg")  # Use a PNG image to avoid compression issues

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}

# Store message length in a pixel
img[0, 0, 0] = len(msg)

n, m, z = 1, 0, 0  # Start from (1,0,0) to avoid overwriting length

for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)  # Save as PNG (Lossless)
os.system("start encryptedImage.png")

with open("key.txt", "w") as f:
    f.write(password)

print("Encryption Done. Use 'decrypt.py' to decrypt.")
