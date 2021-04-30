
import PIL, random, sys
from PIL import Image, ImageDraw

pixel = 1500

ch = lambda: random.randint(0,255)
rgb = lambda: (ch(), ch(), ch())

# Run-length encoding (RLE) is a form of lossless data
# compression in which runs of data (sequences in which
# the same data value occurs in many consecutive data
# elements) are stored as a single data value and count,
# rather than as the original run.
RLE = []

def create_square(pattern, draw, randColor, element, tiles):
  if (element == int(tiles/2)):
    draw.rectangle(pattern, randColor)
  elif (len(RLE) == element+1):
    draw.rectangle(pattern,RLE.pop())
  else:
    RLE.append(randColor)
    draw.rectangle(pattern, randColor)


def create_image(pattern, draw, tiles):
  x0, y0, x1, y1 = pattern
  squareTile = (x1-x0)/tiles
  randColors = [rgb(), rgb(), rgb(), (0,0,0), (0,0,0), (0,0,0)]
  i = 1
  for y in range(0, tiles):
    i *= -1
    element = 0
    for x in range(0, tiles):
      topLeftX = x * squareTile + x0
      topLeftY = y * squareTile + y0
      botRightX = topLeftX + squareTile
      botRightY = topLeftY + squareTile
      create_square((topLeftX, topLeftY, botRightX, botRightY), draw, random.choice(randColors), element, tiles)
      if (element == int(tiles / 2) or element == 0):
        i *= -1;
      element += i


def main(tiles, num_of_img, imgTiles):
  pixel = imgTiles
  newImg = Image.new('RGB', (pixel, pixel))
  draw = ImageDraw.Draw(newImg)
  
  imageTiless = pixel/num_of_img
  padding = imageTiless/tiles
  
  for x in range(0, num_of_img):
    for y in range(0, num_of_img):
      topLeftX = x*imageTiless + padding/2
      topLeftY = y*imageTiless + padding/2
      botRightX = topLeftX + imageTiless - padding
      botRightY = topLeftY + imageTiless - padding
      create_image((topLeftX, topLeftY, botRightX, botRightY), draw, tiles)
  
  newImg.save("Imagine/image-"+str(tiles)+"x"+str(tiles)+"-"+str(num_of_img)+"-"+str(imgTiles)+".jpg")

if __name__ == "__main__":
  main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))