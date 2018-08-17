def my_mov_avg(list,N):
    lst1=[]
    lst2=[0]
    for i,x in enumerate(list, 1):
        lst2.append(lst2[i-1]+x)
        if i>=N:
            movave= round(((lst2[i]-lst2[i-N])/N),2)
            lst1.append(movave)
            
    print("Moving average values list: ", lst1)
    print("Length of the list l-N+1: ", len(lst1))


list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
N = 4

my_mov_avg(list,N)

Moving average values list:  [25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0]
Length of the list l-N+1:  7


list =[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
N = 3

my_mov_avg(list,N)



Moving average values list:  [5.0, 4.67, 5.67, 6.67, 9.67, 28.67, 49.33, 72.67, 84.0, 93.33, 116.33]
Length of the list l-N+1:  11