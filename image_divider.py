from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def imageDivider(*args):
    for value in args:
        if value is not None:
            print(value)
            inputFilename = value
            im = Image.open(inputFilename)
            pixels = im.load()
            ##### Setup
            x, y = im.size
            outname = inputFilename.split('.')[0]+'_'
            
            numberOfParts_x = 40
            numberOfParts_y = 28
            new_size=(2017,2017)

            print('numberOfParts_x: ', numberOfParts_x, ' numberOfParts_y: ', numberOfParts_y)
            counter = 0
            ##### divide image #####
            for i in range(numberOfParts_x):
                for j in range(numberOfParts_y):
                    if i!=numberOfParts_x and j!=numberOfParts_y:
                        im.crop(box=(x/numberOfParts_x*i, y/numberOfParts_y*j, x/numberOfParts_x*(i+1)-1, y/numberOfParts_y*(j+1)-1)).\
                        resize(new_size).\
                        save('splited_images/{}{}_X{}_Y{}.png'.format(outname, str(counter), str(i), str(numberOfParts_y-j)))
                        print(counter)
                        counter = counter + 1
        else:
            print('value empty!')

def gridDraw(*args):
    for value in args:
        if value is not None:
            print(value)
            inputFilename = value
            im = Image.open(inputFilename)

            ##### setup #####
            width, height = im.size
            outname = '1_GRID_phm_'+inputFilename.split('.')[0].split('_')[-1]

            draw = ImageDraw.Draw(im)
            numberOfParts_x = 40
            numberOfParts_y = 28
            print('numberOfParts_x: ', numberOfParts_x, ' numberOfParts_y: ', numberOfParts_y)

            fnt = ImageFont.truetype(font='Ubuntu_Mono/UbuntuMono-Regular.ttf', size=24)
            fnt2 = ImageFont.truetype(font='Ubuntu_Mono/UbuntuMono-Regular.ttf', size=30)

            counter = 0
            ##### Draw GRID and numbers #####
            for i in range(numberOfParts_x):
                x = int(width/numberOfParts_x * i)
                draw.line((x, 0, x, height))
                for j in range(numberOfParts_y):
                    y = int(height/numberOfParts_y * j)
                    draw.line((0, y, width, y))
                    draw.text((x+15,y+15), str(counter),font=fnt2, fill=(255,0,0,255))
                    counter = counter + 1

            ###### SAVE #####
            im.save('{}.png'.format(outname))
            ##### Draw GRID and numbers #####
            for i in range(numberOfParts_x):
                x = int(width/numberOfParts_x * i)
                draw.line((x, 0, x, height))
                for j in range(numberOfParts_y):
                    y = int(height/numberOfParts_y * j)
                    draw.line((0, y, width, y))
                    draw.text((x+15,y+35), str(i)+' '+str(numberOfParts_y-j),font=fnt2, fill=(0,0,255,255))
                    counter = counter + 1

            ###### SAVE #####
            im.save('{}.png'.format(outname))
        else:
                print('value empty!')



if __name__ == "__main__":
    # while (True):
    #     # inputImage = input('Input image name:\n') #poocha_height_map_1.png
    #     # imageDivider(inputImage)
    
    # imageDivider('poocha_height_map_2.png')
    gridDraw('poocha_height_map_2.png')
