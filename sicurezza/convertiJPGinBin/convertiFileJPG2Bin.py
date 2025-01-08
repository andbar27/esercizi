# Apri il file immagine in modalità binaria (lettura)
with open('./pitone.jpeg', 'rb') as file:
    image_data = file.read()

with open('pitone.txt', 'w') as file:
    for i in range(len(image_data)):
        #print(chr(image_data[i]]))
        file.write(chr(image_data[i]))

with open('pitoneHEX.txt', 'w') as file:
    for i in range(len(image_data)):
        if(len(hex(image_data[i]))<4):
            file.write("0")
            file.write(hex(image_data[i])[2:])
        else:
            file.write(hex(image_data[i])[2:])


import base64
with open('pitoneB64.txt', 'w') as file:
    file.write(base64.b64encode(image_data).decode("ascii"))

with open('pitoneB64.txt', 'r') as file:
    txtb64 = file.read()

with open('pitoneB64.jpeg', 'wb') as file:
    file.write(base64.b64decode(txtb64))