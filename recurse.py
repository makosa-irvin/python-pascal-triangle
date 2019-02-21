def pascal(row,col):
    if (col==1) or (col==row):
        return 1
    top_left = pascal(row-1,col-1)
    top_right = pascal(row-1,col)
    return top_left + top_right
    

num = int(input("Enter number of rows: "))                
for i in range(1,num+1):
   for j in range(1,i+1):
       print(pascal(i,j),end=" ",sep=" ")
       
   print("",sep=" ")

#print(pascal(3))