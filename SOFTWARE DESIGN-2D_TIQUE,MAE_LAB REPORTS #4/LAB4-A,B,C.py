def lab():
    print("lab: activity 4a")

lab()

def max_elemnt(gven_lst, len_lst):

    if len_lst == 1:
        return gven_lst[0]

    return max(gven_lst[len_lst - 1], max_elemnt(gven_lst, len_lst - 1))

def min_elemnt(gven_lst, len_lst):
    if len_lst == 1:
        return gven_lst[0]
    return min(gven_lst[len_lst-1], min_elemnt(gven_lst, len_lst-1))

gven_lst = [4,6,8,3,9,8]
len_lst = len(gven_lst)
print("The Maximum element in a given list",
      gven_lst, "=", max_elemnt(gven_lst, len_lst))
print("The Minimum element in a given list",
      gven_lst, "=", min_elemnt(gven_lst, len_lst))

def lab():
    print("lab: activity 4b")

lab()

#LAB4-b
def product(num1,num2):
    if(num1<num2):
        return product(num2,num1)
    elif(num2!=0):
         return(num1+product(num1,num2-1))
    else:
         return 0
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("product is: ",product(num1,num2))

def lab():
    print("lab: activity 4c")

lab()

any_string = "pots&pans"

rev_string = any_string[::-1]

print(rev_string)