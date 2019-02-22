from functools import lru_cache

#PASCALS
def pascal(b):
    a=[]
    

    for i in range(b):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if(b!=0):
            a[i].append(1)
    for i in range(b):
        print("   "*(b-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
        print()




#multiples
def multiples(n,k):
    if n<=1:
        return "The {0} multiple of {1} is {1}".format(1,k)
    mult = n*k
    print("The {0} multiple of {1} is {2}".format(n,k,mult))
    return multiples(n-1,k)
    
#factorials
def factorials(i):
    if i<=1:
        return 1
    return i*factorials(i-1)

#fibonacci
@lru_cache(maxsize=1000)
def fibonacci(j):
    if j<=1 :
        return j
    return fibonacci(j-1) + fibonacci(j-2)
    






#calling pascal
be=int(input("Enter number of rows: "))
print(pascal(be))


#calling multiples
number = int(input("Enter a multiple: "))
base = int(input("Enter a number: "))
print(multiples(number,base))

#calling factorials
numbre = int(input("Enter factorial: "))
print(factorials(numbre))

#calling fibonacci
namba = int(input("Enter fibonacci: "))
print(fibonacci(namba))