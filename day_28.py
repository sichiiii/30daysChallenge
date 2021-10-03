#https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
def color(RGB):
    if RGB < 0:
        RGB = 0
    elif RGB > 255:
        RGB = 255
    RGB = hex(RGB)[2:].upper()
    if len(RGB)<2:
        RGB = '0'+RGB
    return RGB    

def rgb(r, g, b):
    return color(r)+color(g)+color(b)
