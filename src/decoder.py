from PIL import Image

try:
    img = Image.open('output_image.png')
except FileNotFoundError:
    print("Error: File 'output_image.png' does not exist.")
    input("Press Enter to exit...")

width, height = img.size

binary_str = []
for y in range(height):
    for x in range(width):
        pixel = img.getpixel((x, y))
        binary_str.append(str(pixel//255))
print(binary_str)

temp = ""

for i in range(len(binary_str)):
    if i % 8 == 0.00:
        temp += " "
    temp += binary_str[i]

print(temp)

binary_list = temp.split()
print(binary_list)

ascii_list = [int(i, 2) for i in binary_list]
decoded_str = ''.join([chr(i) for i in ascii_list])
print(decoded_str)

input("Press Enter to exit...")
