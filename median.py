# to find median of three numbers

def median(numbers):
    numbers.sort()
    return numbers[1]
if __name__ == "__main__":
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    result = median([a,b,c])
    print("Median: " ,result)

#OUTPUT
#First number: 63
#Second number: 41
#Third number: 56
#Median:  56


