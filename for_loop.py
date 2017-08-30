#for loop is used when you want to do something alot of times
#for i in range(5):
 #    print('rishyjee')
#print(list(range(5)))
#for number in range(20,81):
 #    print(number)
     
#range[Start,stop)--->Mathematically
     
#
#There are two types of competents
#1.Concious competents and inconcious competents
#Concious competents:-You thinking about something and then being good at it
#inconcious competents:-You get so damn good what you do that don't even think about it and then do it.
#So how do we go from concious competents is, you are looking at your notes and really thinking about it and how function works, and like you just writing the code is prictice!!!


# write a function that sums all the elements of a list and returns them
def sum_list(my_list):
     count=0
     for number in my_list:
          count=count+number
     return count
     print(count)
#assert sum_list([1,2,3,4])==10
#assert sum_list([1,2,3,4,5])==15
     
print(sum_list([1,2,3,4,5,6,7,8]))
