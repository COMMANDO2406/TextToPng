from PIL import Image

try:
    with open('data.txt', 'r') as file:
        test_str = file.read().replace('\n', '')
except FileNotFoundError:
    print("Error: File 'data.txt' does not exist.")
    exit(1)

print("The original string is : " + str(test_str))
res = ''.join(format(ord(i), '08b') for i in test_str)
print("The string after binary conversion : " + str(res))

pixels = []

for i in range(0, len(res), 8):
    pixels.append(list(map(int, res[i:i+8])))

print(pixels)
print(len(res))

img = Image.new('1', (8, len(pixels)))
img.putdata([pixel for row in pixels for pixel in row])
img.save('output_image.png')

input("Press Enter to exit...")
