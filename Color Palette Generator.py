import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import ctypes

def round_corner(radius, fill):
    #Draw a round corner
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=fill)
    return corner
 
def round_rectangle(size, radius, fill):
    #Draw a rounded rectangle
    width, height = size
    rectangle = Image.new('RGBA', size, fill)
    corner = round_corner(radius, fill)
    rectangle.paste(corner, (0, 0))
    rectangle.paste(corner.rotate(90), (0, height - radius)) # Rotate the corner and paste it
    rectangle.paste(corner.rotate(180), (width - radius, height - radius))
    rectangle.paste(corner.rotate(270), (width - radius, 0))
    return rectangle

def placing_images(path):
    img2 = Image.open(path, 'r')
    img2_w, img2_h = img.size
    background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img2_w) // 2, (bg_h - img2_h) // 3)
    background.paste(img, offset)
    return background

def convert_to_rgb(path):
	png = Image.open(path)
	png.load() # required for png.split()

	background = Image.new("RGB", png.size, (255, 255, 255))
	background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
	return background

def write_text(path, catcode12, catName):
	img = Image.open(path)
	draw = ImageDraw.Draw(img)
	fontSize = 50
	font = ImageFont.truetype("calibri.ttf", fontSize)
	
	textKiri = catcode12 #kode cat
	textKanan = catName #nama cat
	
	posisiKanan = (500, 750) #Nama Warna
	posisiKiri = (199, 750) #Kode Cat
	
	lebar, tinggi = img.size
	draw = ImageDraw.Draw(img)
	
	lebarBaru, tinggiBaru = draw.textsize(textKanan, font=font)
	
	offsetWidthRight = 200
	a1 = lebar - offsetWidthRight - lebarBaru
	
	draw.text((a1, 750), textKanan, fill=000000 ,font=font, align="right") #posisiKanan #NamaWarna
	if catcode12 != "0": #Jika kode cat bukan "Nol":
		draw.text(posisiKiri, textKiri, fill=000000 ,font=font, align="left") #posisiKiri #KodeWarna
	return img

master_dir = "C:\\Users\\yuri\\Documents\\Yuri's work\\0. Assorted\\_Script\\_image processing\\Python\\3. Color Pallete Generator"
text_dir = master_dir + "_text\\"
img_dir = master_dir + "_img\\"

f = open(text_dir + "hex code color.txt", 'r+', encoding='utf-8-sig')
hexCode = [line for line in f.read().splitlines()]
f.close()

f = open(text_dir + "Nama cat.txt", 'r+', encoding='utf-8-sig')
namaCat = [line for line in f.read().splitlines()]
f.close()

f = open(text_dir + "cat code.txt", 'r+', encoding='utf-8-sig')
kodeCat123 = [line for line in f.read().splitlines()]
f.close()

f = open(text_dir + "saveName.txt", 'r+', encoding='utf-8-sig')
saveName = [line for line in f.read().splitlines()]
f.close()

if len(hexCode) == len(namaCat) & len(hexCode) == len(kodeCat123):
	hitung = range(len(hexCode))
	
	for i in hitung:
		img = round_rectangle((1200, 1100), 50, hexCode[i])
		img = img.resize((600, 550),Image.ANTIALIAS)
		img.save(img_dir + saveName[i] + '.png', quality=100, subsampling=0)

		img = convert_to_rgb(img_dir + saveName[i] + '.png')
		img.save(img_dir + saveName[i] + '.png', quality=100, subsampling=0)

		img = placing_images(img_dir + saveName[i] + '.png')
		img.save(img_dir + saveName[i] + '.png', quality=100, subsampling=0)

		img = convert_to_rgb(img_dir + saveName[i] + '.png')
		img.save(img_dir + saveName[i] + '.jpg', quality=100, subsampling=0)

		img = write_text(img_dir + saveName[i] + '.jpg', kodeCat123[i], namaCat[i])
		img.save(img_dir + saveName[i] + '.jpg', quality=100, subsampling=0)
		
		os.remove(img_dir + saveName[i] + '.png')