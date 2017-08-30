#Write a function last letter that returns the last letter of a string.
#Make sure to use Retrun and not print in your function.
#Eg: last_letter('rishyjee')--->e

def last_letter(my_string):
     count=0
     for letter in my_string:
          count+=1
     return my_string[count-1]
def test_last_letter():
     assert last_letter('rishyjee')=='e'
     assert last_letter('Mayuri')=='i'
     assert last_letter('Rishabh')=='h'
     assert last_letter('Amir')=='r'
     assert last_letter('Sandip')=='p'
     assert last_letter('Vivek')=='k'
     print('YOUR CODE IS CORRECT SIRJEE')

test_last_letter()     
     
