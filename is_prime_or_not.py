#program to check whether the number is prime or not

def check_prime(number):
    if 0<number<1:
        return "Not prime"
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return "Not prime"
            break
    return "Prime"

if __name__ == "__main__":
    number = int(input("Enter the number"))
    result = check_prime(number)
    print(result)

#OUTPUT
#Enter the number63
#Not prime