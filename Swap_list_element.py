#Swap 3rd and 5th element in a list
#considering list of int to demonstrate swap
def swap_function(input_list):
    input_list[2],input_list[4] = input_list[4],input_list[2]
    return input_list

if __name__ == "__main__":
    input_list = list((input("Enter the list")))
    input_list = [int(x) for x in input_list]
    print("List before swapping")
    print(input_list)
    result=swap_function(input_list)
    print("After swapping")
    print(result)

#Enter the list12345
#List before swapping
#[1, 2, 3, 4, 5]
#After swapping
#[1, 2, 5, 4, 3]