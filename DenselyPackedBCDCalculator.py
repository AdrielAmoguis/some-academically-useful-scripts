# Densely Packed BCD Calculator

def main():
#    Input packed BCD as a string separated by a space
    packedBcd = input("Enter the packed BCD, separating each grouping with a space: ")

    digitBcd = packedBcd.split(' ')

    # Get the msb of each
    msb = [digbcd[0] for digbcd in digitBcd]
    msb = "".join(msb)

    # Select the pattern to follow based on the msb
    lookupTable = {
        "000": "bcdfgh0jkm",
        "001": "bcdfgh100m",
        "010": "bcdjkh101m",
        "011": "bcd10h111m",
        "100": "jkdfgh110m",
        "101": "fgd01h111m",
        "110": "jkd00h111m",
        "111": "00d11h111m"
    }

    pattern = lookupTable[msb]

    # Place keys on the digitBcd
    keyedBCD = {
        "a": digitBcd[0][0],
        "b": digitBcd[0][1],
        "c": digitBcd[0][2],
        "d": digitBcd[0][3],
        
        "e": digitBcd[1][0],
        "f": digitBcd[1][1],
        "g": digitBcd[1][2],
        "h": digitBcd[1][3],

        "i": digitBcd[2][0],
        "j": digitBcd[2][1],
        "k": digitBcd[2][2],
        "m": digitBcd[2][3],

        "1": "1",
        "0": "0"
    }

    # Construct the string based on the pattern
    answer = ""
    for key in pattern:
        answer += keyedBCD[key]

    # Print the answer
    print(answer)

if __name__ == '__main__':
    main()