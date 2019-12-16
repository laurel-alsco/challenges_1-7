# Author: Laurel Miller
def num_to_word(n):
    # convert an integer number n into a string of english words
    # break the number into groups of 3 digits using slicing each group representing hundred, thousand, million, billion, ...
    n3 = []
    r1 = ""
    # create numeric string
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
        # break if end of ns has been reached
        if q < -2:
            break
        else:
            if q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r

    # break each group of 3 digits into ones, tens/twenties, hundreds and form a string
    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100) // 10
        b3 = (x % 1000) // 100
        if x == 0:
            continue  # skip
        else:
            t = thousands[i]
        if b2 == 0:
            nw = ones[b1] + t + nw
        elif b2 == 1:
            nw = tens[b1] + t + nw
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw
        if b3 > 0:
            nw = ones[b3] + "Hundred " + nw
    return nw


ones = ["", "One ", "Two ", "Three ", "Four ", "Five ",
        "Six ", "Seven ", "Eight ", "Nine "]
tens = ["Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ",
        "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
twenties = ["", "", "Twenty ", "Thirty ", "Forty ",
            "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
thousands = ["", "Thousand ", "Million ", "Billion ", "Trillion ",
             "Quadrillion ", "Quintillion ", "Sextillion ", "Septillion ", "Octillion ",
             "Nonillion ", "Decillion ", "Undecillion ", "Duodecillion ", "Tredecillion ",
             "Quattuordecillion ", "Quindecillion", "Sexdecillion ", "Septendecillion ",
             "Octodecillion ", "Novemdecillion ", "Vigintillion "]



