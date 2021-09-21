#https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
def domain_name(url):
    result_arr = url.split('.')
    result_arr[0] = result_arr[0].replace("http://", "")
    result_arr[0] = result_arr[0].replace("https://", "")
    for i in result_arr:
        if i != 'www':
            return i
