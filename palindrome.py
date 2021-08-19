#reverse the digits of a given number and add it to the original,
# If the sum is not a palindrome repeat this procedure

def check_palindrome(n):
  step = 0
  while step<1000:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      n=int(n)
      m = int(k[::-1])
      n += m
      step += 1
  return n


if __name__ == "__main__":
    number = input("Enter number")
    result=check_palindrome(number)
    print(result)

#OUTPUT
#Enter number 54
#99
