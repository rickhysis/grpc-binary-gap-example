def count_gap(number):
    try:
        binary = bin(number)
        finalMax = 0
        currentMax = 0

        for i in range(len(binary)) :
            currentMax = 0
            while binary[i] == '0': 
                currentMax += 1 
                i += 1
            finalMax = max(finalMax, currentMax)
        return finalMax   
    except ValueError:
        print("That's not an number!")