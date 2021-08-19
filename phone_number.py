#to find missing digit in a given phone number
if __name__ == "__main__":
    number = list(input("Enter phone number: "))
    number = set([int(x) for x in number])
    digits = set([0,1,2,3,4,5,6,7,8,9])
    print( number ^ digits)

#OUTPUT
#Enter phone number: 6845217896
#{0 ,3}

