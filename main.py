from PIL import Image

image_n=input("Please enter the image name with extension(image.extension): ")


value_r=int(input("Please enter the red value of the pixels you want: "))
value_g=int(input("Please enter the green value of the pixels you want:"))
value_b=int(input("Please enter the blue value of the pixels you want: "))

im=Image.open(image_n)
rgb_im=im.convert('RGB')
pix=im.load()

image_s=im.size

pix_x=0
pix_y=0

correct_counter=0

while pix_x < image_s[1]:
    while pix_y <image_s[0]:
        r, g, b = rgb_im.getpixel((pix_y, pix_x))
        if r == value_r and g ==value_g and b == value_b:
            correct_counter+=1
        pix_y+=1
    pix_x+=1
    pix_y=0
    
print(correct_counter)

input("press enter to quit...")
