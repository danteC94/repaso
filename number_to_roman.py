def number_to_roman(number):
    dict = {'1': "I",'5': "V",'10': "X",'50': "L",'100': "C",'500': "D", '1000':"M"}
    list = ["M", "D", "C", "L", "X", "V", "I"]
    result = ""
    while number>0:
        for letra in list:
            for key in dict:
                if dict[key] == letra:
                    if number - int(key) >= 0:
                        number -= int(key)
                        result += dict[key]    
    return result
numero = 10000
dict = {'M':1000 , 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
list = ["M", "D", "C", "L", "X", "V", "I"]
for letra in list:
    for key in dict:
        if key == letra:
            print key, ":", dict[key]
            numero -= dict[key]
            print numero
