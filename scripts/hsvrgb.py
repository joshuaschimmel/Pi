

# https://en.wikipedia.org/wiki/HSL_and_HSV#From_HSV
# Hue: [0°,360°], Saturation: [0,1], Value: [0,1]
def hsvtorgb(hue, sat = 1, val = 1):
    # chroma is constant 100 i guess
    chroma = 255 #val * sat
    # some different h value
    h = hue / 60
    # some intermediate value x for the second largest component
    x = round(chroma * (1 - abs((h % 2) -1)))

    output = (0,0,0)

    # yey ifs, TODO dichromationaries
    if(0 <= h < 1): output = (chroma, x, 0)
    elif(1 <= h < 2): output = (x, chroma, 0)
    elif(2 <= h < 3): output = (0, chroma, x)
    elif(3 <= h < 4): output = (0, x, chroma)
    elif(4 <= h < 5): output = (x, 0, chroma)
    elif(5 <= h <= 6): output = (chroma, 0, x)

    return output

hue = input("hue: ")
print(hsvtorgb(int(hue)))
