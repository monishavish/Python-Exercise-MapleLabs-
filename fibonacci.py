#program to display fibonacci series for user given range

def fibonacci_series(num):
    if num<=1:
        return num
    else:
        return (fibonacci_series(num-1)+fibonacci_series(num-2))

if __name__ == "__main__":
    start = int(input("Enter start range: "))
    stop = int(input("Enter stop range: "))
    for i in range(start+1,stop+1):
        print(fibonacci_series(i))

#OUTPUT
#Enter start range: 20
#Enter stop range: 30
#10946
#17711
#28657
#46368
#75025
#121393
#196418
#317811
#514229
#832040