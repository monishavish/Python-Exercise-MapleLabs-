#count number of trailing zeros in factorial

def count_zeros (number):
    i = 5
    zeros = 0
    while number >= i:
        zeros += number // i
        i *= 5
    return zeros

if __name__ == "__main__":
    number = int(input("Enter number: "))
    result = count_zeros(number)
    print("Number of zero's" , result)

#OUTPUT
#Enter number: 5
#Number of zero's 1
