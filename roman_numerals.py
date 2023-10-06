def to_roman(num):
    output = ""
    roman_numeral_to_arabic = { # dict must be in priortity order
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    
    for key, val in roman_numeral_to_arabic.items():
        if num >= val: # makes code use largest roman numeral first
            evenly_divisible_times = num // val # (// always rounds down) how many times should each roman numeral be added
            output += key * evenly_divisible_times # adds roman numeral to answer correct number of times
            num = num % val # gets leftover amt and then repeat process until num == 0
    
    return output

