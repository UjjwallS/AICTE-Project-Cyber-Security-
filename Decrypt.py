import cv2

img = cv2.imread("encryptedImage.png")  # Read from PNG to avoid corruption

c = {i: chr(i) for i in range(255)}

with open("key.txt", "r") as f:
    password = f.read()

pas = input("Enter passcode for Decryption: ")

if password == pas:
    msg_length = img[0, 0, 0]  # Read stored message length
    message = ""
    n, m, z = 1, 0, 0  # Start from (1,0,0) to match encryption

    for _ in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
