from PIL import Image, ImageOps, ImageDraw
# from telegram.ext import Updater, MessageHandler, Filters
import os
import shutil
from time import sleep


def indecator(num, rep):
    charr = ""
    if num == 1:
        charr = " "
    elif num == 2:
        charr = "."
    elif num == 3:
        charr = ":"
    elif num == 4:
        charr = "-"
    elif num == 5:
        charr = "="
    elif num == 6:
        charr = "+"
    elif num == 7:
        charr = "*"
    elif num == 8:
        charr = "#"
    elif num == 9:
        charr = "%"
    elif num == 10:
        charr = "@"
    return charr * rep


def get_numbers(dicenum, is_black, complete_file_address):
    img = Image.open(complete_file_address)
    img = ImageOps.grayscale(img)
    img = ImageOps.equalize(img)
    resultlist = []

    dicew = dicenum
    dicesize = int(img.width * 1.0 / dicew)
    diceh = int(img.height * 1.0 / img.width * dicew)

    nimg = Image.new('L', (dicesize * dicew, dicesize * diceh), 'white')
    nimgd = ImageDraw.Draw(nimg)

    for y in range(0, img.height - dicesize, dicesize):
        row = []
        for x in range(0, img.width - dicesize, dicesize):
            this_sector_color = 0
            for dicex in range(dicesize):
                for dicey in range(dicesize):
                    color = img.getpixel((x + dicex, y + dicey))
                    this_sector_color += color
            this_sector_color = int(this_sector_color / (dicesize ** 2))
            nimgd.rectangle([x, y, x + dicesize, y + dicesize], fill=this_sector_color)
            if is_black:
                dice_number = 7 - int((255 - this_sector_color) * 5 // 255 + 1)
            else:
                dice_number = int((255 - this_sector_color) * 5 // 255 + 1)
            # print(indecator(dice_number, rep), end="")
            # print(dice_number, end="")
            row.append(dice_number)
            # print(row)
        # print()
        resultlist.append(row)
    return resultlist


def stick(is_black, dicesarray, name, directory_address):
    if is_black:
        label = 'black'
    else:
        label = 'white'
    dicew = len(dicesarray[0])
    diceh = len(dicesarray)
    print(name + str(dice_num))
    print("number of dices in dice pic", (dicew, diceh))
    images = [Image.open(str(x) + label + ".png") for x in range(1, 7)]
    dicesize = (images[0].width, images[0].height)
    print('dicesize', dicesize)
    newim2 = Image.new('RGB', (dicew * dicesize[0], diceh * dicesize[1]))
    yoffset = 0
    for y in range(diceh):
        xoffset = 0
        for x in range(dicew):
            # print('pointer:', x, y)
            # print('dice number is:', dicesarray[y][x])
            # print('offsets:',xoffset, yoffset)
            dicenumberside = dicesarray[y][x]
            diceimg = images[dicenumberside - 1]
            newim2.paste(diceimg, (xoffset, yoffset))
            xoffset += dicesize[0]
        yoffset += dicesize[1]
    newim2.save(directory_address + "\\" + str(dice_num) + label + "NEW" + name)


def sen_pho(bot, update):
    name = "sala"
    file_id = update.message.photo[-1].file_id
    newFile = bot.getFile(file_id)
    newFile.download(name + ".jpg")
    chat_id = update.message.chat_id

    bot.send_photo(chat_id=chat_id, photo=name + "jpg")


for fileName in os.listdir("D:\\programming\\dice picture\\kasebi"):
    print(fileName)
    directory_address = "D:\\programming\\dice picture\\kasebi\\" + fileName.split(sep=".")[0]
    if os.path.exists(directory_address):
        print(directory_address)
    else:
        print(directory_address + "     not found")
        os.makedirs(directory_address, exist_ok=False)
        src = "D:\\programming\\dice picture\\kasebi" + "\\" + fileName
        dst = directory_address + "\\" + fileName
        shutil.copyfile(src, dst)
        for i in range(2):
            if i:
                iis_black = True
            else:
                iis_black = False
            for dice_num in range(80, 170, 20):
                result = get_numbers(dice_num, iis_black, complete_file_address=src)
                stick(iis_black, result, fileName, directory_address)
        sleep(10)
    """    
    
    """
"""
updater = Updater("965187132:AAH_auDKKOmI0XW6MBi6mpLEZZaOfbPKC3A", use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.photo, sen_pho))
updater.start_polling()
updater.idle()
"""
