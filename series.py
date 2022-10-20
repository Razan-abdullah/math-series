from re import A


def fibonacci(nterms):
    
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
       print("Please enter a positive integer")

    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)

    else:
       print("Fibonacci sequence:")
    
    c=[]
   
    while count < nterms:
       c.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
    return(c)  
       
       
       
       
       
       
       
       
def lucas(nterms):
    n1, n2 = 2, 1
    count = 0
    c=[]

    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("lucas sequence ",nterms,":")
    
   
    while count < nterms:

       c.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
    return(c) 



def sum_series(func):
    a=func
    c=0
    for i in a:
        c+=i
    return f"sum of this series is :{c}"    
           
# print(lucas(1))
print(fibonacci(3)) 
# print(sum_series(lucas(3)))
print(sum_series(fibonacci(3)))