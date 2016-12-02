#task9 - Binary search with divide and conquer

def DivideandConquer(a,low,high,first,last):
    
    if last < first:
        return False
    
    midpoint = (first + last)//2 
    if a[midpoint] > low and a[midpoint]< high:
        
        return True
    if a[midpoint] >= high:
        
        return DivideandConquer(a,low,high,first,midpoint-1)
    else:
        
        return DivideandConquer(a,low,high,midpoint +1,last)

    
    


a=(2,3,5,7,9,13)
low=10
high=14
first = 0
last = len(a)-1

print (DivideandConquer(a,low,high,first,last))


