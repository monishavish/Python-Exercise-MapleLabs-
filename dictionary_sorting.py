# sort dictionary by key in descending order

if __name__ == "__main__":
    dic = dict()
    for i in range(4):
        key = int(input("Enter key for dic:")) #considering key to be int
        value = input("Enter value for dic:")
        dic[key] = value
    print("Dictionary before sorting: ",dic)
    sorted_dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)
    print("Dictionary after sorting: ", sorted_dic)

#OUTPUT
#Enter key for dic:56
#Enter value for dic:names
#Enter key for dic:10
#Enter value for dic:address
#Enter key for dic:2
#Enter value for dic:email
#Enter key for dic:40
#Enter value for dic:PhNo
#Dictionary before sorting:  {56: 'names', 10: 'address', 2: 'email', 40: 'PhNo'}
#Dictionary after sorting:  [(56, 'names'), (40, 'PhNo'), (10, 'address'), (2, 'email')]