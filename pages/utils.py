def integerToRoman(integer):
    if integer == 0 or integer > 4000:
        raise ValueError("This number can't represtented by a Roman numeral. Try a number within the range 1-3999")
    else:
        list_of_symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(list_of_symbols, numbers):
            result += letter * int(integer / n)
            integer %= n
        return result
