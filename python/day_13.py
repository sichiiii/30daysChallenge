#https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python
def hex_string_to_RGB(hex_string): 
    hex_string = hex_string.lstrip('#')
    arr_hex = tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))
    result = {'r':'', 'g':'', 'b':''}
    result['r'], result['g'], result['b'] = arr_hex[0], arr_hex[1], arr_hex[2] 
    return result
