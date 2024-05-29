ONE = int(input())
TWO = int(input())
ROMAN_NUM = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,'C': 100, 'XC': 90, 'L': 50, 'XL': 40,'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

def roman():
    global ONE, TWO
    THREE = ONE + TWO
    romanone = ''
    for letter, value in ROMAN_NUM.items():
        while ONE >= value:
            romanone += letter
            ONE -= value
    romantwo = ''
    for letter, value in ROMAN_NUM.items():
        while TWO >= value:
            romantwo += letter
            TWO -= value
    romanthree = ''
    for letter, value in ROMAN_NUM.items():
        while THREE >= value:
            romanthree += letter
            THREE -= value
    print(romanone, "+", romantwo, "=", romanthree)
    return 0

print(roman())
