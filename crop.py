from PIL import Image

img = Image.open('all.png')
print(img.width, img.height)
for i in range(0, 501, 100):
    for j in range(0, 101, 100):
        pert = 17
        x1 = i + pert
        x2 = i + 100 - pert
        y1 = j + pert + 3
        y2 = j + 100 - pert
        new = img.crop([x1, y1, x2, y2])
        is_white = j > 50
        if is_white:
            label = 'white'
        else:
            label = 'black'
        name = str(i//100 + 1) + label + ".png"
        print(name, 'saved', "  {} * {} ".format(new.width, new.height))
        new.save(name)
        Image.open(name).show()

