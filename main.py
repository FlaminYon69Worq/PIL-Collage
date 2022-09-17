#!/bin/python3
# Assignment: PIL Collage
# Use any image from url and import onto new png titled "collage.png"

#imports
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

#global vars
#urls for all the images I am using
url_philippines = "https://www.pngkit.com/png/full/78-788329_philippine-flag-png-pictures-philippines-flag-with-name.png"
url_manny = "https://www.premierboxingchampions.com/sites/default/files/styles/fighter_last_fight/public/PacPage.jpg?itok=nksEmwMc"
url_jotaro = "https://static.wikia.nocookie.net/jjba/images/a/ad/JotaroWStarPlatinum.png/revision/latest/top-crop/width/300/height/300?cb=20140404183317"
url_boxing_ring = "https://pbs.twimg.com/media/DfTF9PLU0AAM9F5.jpg"

#function definitions

#get images from web
def get_web_image(url):
  resp = requests.get(url)
  img = Image.open(BytesIO(resp.content))
  return img


#paste image function
def paste_image(source, destination, x, y, omit_color="None"):
  #source is the same as image
  #get image dimensions
  w, h = source.size 
  if omit_color == "None":
    for i in range(w):
      for j in range(h):
        new_source = source.getpixel((i, j))
        destination.putpixel((i + x, j + y), (new_source))
  #omit transparent background of png pictures
  elif omit_color == "Transparent":
    for i in range(w):
      for j in range(h):
        r, g, b, a = source.getpixel( (i, j) )
        if a != 0:      
          destination.putpixel((i + x, j + y), (r,g,b))
  return destination


#strengthens either the red, green, or blue pixels on the image
def more_intense(image, color_band, percentage_increase):
  # the (w,h = image.size) means get image dimensions 
  w, h = image.size
  #intensifies a color  
  color_change = int(percentage_increase*100)  
  if image.mode == "RGB":
    img_new = Image.new("RGB", (w,h))
    #apply color change
    for x in range(w):
      for y in range(h):
        #gets all pixels
        #adjust r, g, b for each color       
        if color_band == "red":
          r, g, b= image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r*color_change, g, b))       
        elif color_band == "green":
          r, g, b = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g*color_change, b))        
        elif  color_band == "blue":
          r, g, b = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g, b*color_change))
  else:
    img_new = Image.new("RGBA", (w,h))
    #apply color change
    for x in range(w):
      for y in range(h):
        #gets all pixels
        #adjust r, g, b for each color
        if color_band == "red":        
          r, g, b, a= image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r*color_change, g, b,a))        
        elif color_band == "green":
          r, g, b, a = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g*color_change, b, a))       
        elif  color_band == "blue":
          r, g, b, a = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g, b*color_change,a))
  return img_new  


#weakens the red, green, or blue pixels on an image
def less_intense(image, color_band, percentage_decrease):
  w, h = image.size
  #weakens a color 
  colour_change = int(percentage_decrease/100)   
  if image.mode == "RGB":
    img_new = Image.new("RGB", (w,h))
    #apply color change
    for x in range(w):
      for y in range(h):
        #gets all pixels
        #adjust r, g, b for each color       
        if color_band == "red":
          r, g, b= image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r*colour_change, g, b))        
        elif color_band == "green":
          r, g, b = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g*colour_change, b))        
        elif  color_band == "blue":
          r, g, b = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g, b*colour_change))
  else:
    img_new = Image.new("RGBA", (w,h))
    #apply color change
    for x in range(w):
      for y in range(h):
        #gets all pixels
        #adjust r, g, b for each color
        if color_band == "red":        
          r, g, b, a= image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r*colour_change, g, b,a))        
        elif color_band == "green":
          r, g, b, a = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g*colour_change, b, a))       
        elif  color_band == "blue":
          r, g, b, a = image.getpixel((x,y)) 
          img_new.putpixel((x, y),(r, g, b*colour_change,a))
  return img_new         


#negative colors function/invert_colors function
def invert_colors(image):  
  w, h = image.size 
  if image.mode == "RGB":
    #invert in RGB
    img_new = Image.new("RGB", (w,h))
    for x in range(w):
      for y in range(h):        
        r, g, b = image.getpixel( (x,y) )        
        img_new.putpixel((x, y), (255-r, 255-g, 255-b))  
  else:
    #invert in RGBA
    img_new = Image.new("RGBA", (w,h))
    for x in range(w):
      for y in range(h):        
        r, g, b, a = image.getpixel( (x,y) )        
        img_new.putpixel((x, y), (255-r, 255-g, 255-b, a))
  return img_new


#flip the image either horizontally or vertically. Over the x axis or over the y axis.
def flip (image, axis): 
  w, h =image.size
  img_mirror=Image.new("RGB", (w,h)) 
  #flip image over horizontally 
  if axis == "horizontal": 
    for x in range (w):      
      for y in range (0,int(h)):
        source=image.getpixel((x,y))
        target_y=(h-1)-y        
        img_mirror.putpixel((x,target_y), source) 
  #flip image over vertically      
  elif axis == "vertical":
    for x in range (0,int(w)):      
      for y in range (h):       
        source=image.getpixel((x,y))
        target_x=(w-1)-x        
        img_mirror.putpixel((target_x,y), source)
  return img_mirror  

#function definitions done

# main loop, creating the collage
def main():
  #make the background
  background = Image.new("RGB", (1200,800), "blue")
  background = get_web_image(url_boxing_ring)
  #the first background set up the foundation of the background, but I found it creative to make an image as the background to my collage, so I called the get_web_image function to retrieve my boxing ring picture.

  #reads the data.txt file
  f = open("data.txt", "r")
  #set the x and y coordinates for the writing of the data.txt file
  x_cor = 400
  y_cor = 0
  data = f.readlines()
  for line in data:
    #implement where to draw the text
    draw_text=ImageDraw.Draw(background)   
    #set the font
    font = ImageFont.truetype("Roboto-Bold.ttf", 40)
    #set the spacing for words
    spacing = 75

    #draw the text in the font and specific color on the rgb scale
    draw_text.text((x_cor,y_cor), line, font=font, spacing=spacing, fill=(800,300,500))
    #spacing line by line
    y_cor += 50
  #Done with text
  f.close()

#get manny image from the web and alter it
  manny = get_web_image(url_manny)
  #resize image to fit within the 1200x800 frame
  manny_pacquiao = manny.resize((400,300))
  #call a flip fucntion to create a new image
  new_manny = flip(manny_pacquiao,"vertical")
  
#get jotaro image from the web and alter it
  jotaro = get_web_image(url_jotaro)
  
  #resize image differently to fit within the 1200x800 frame because the second jotaro image, is his power, and his power is another figure who is taller than him.
  star_plat = jotaro.resize((250, 450))
  star_platinum = more_intense(star_plat, "blue", 130)

#get philippines flag image from web, invert colors
  phil = get_web_image(url_philippines)
  #resize image to fit within the 1200x800 frame
  philippines = phil.resize((350, 200))

#invert the colors of the philippines flag
  phil_invert = invert_colors(phil)
  #resize image to fit within the 1200x800 frame
  philippines_invert = phil_invert.resize((350, 200))
  


#call the paste functions to paste each picture at different coordinates
  paste_image(jotaro, background, 300, 200, "None")
  paste_image(star_platinum, background, 50, 100, "None")
  paste_image(manny_pacquiao, background, 700, 200, "None")
  paste_image(new_manny, background, 700, 500, "None")
  paste_image(philippines, background, 800, 10, "Transparent")
  paste_image(philippines_invert, background, 50, 600, "Transparent")


  #save collage file
  background.save("collage.jpg")
  
  #Done
main()