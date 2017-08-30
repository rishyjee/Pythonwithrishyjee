#Write a function string_length that takes in a string
#and returns its length.
#Hints:
#Question:What do you mean by length?
#Answer:The character count of a string.
#Ex. string_length('rishyjee')--->8
#Explanation: calling string_length() function on the
# string 'rishyjee' should give me back 8
##def string_length(my_string):
##     return len(my_string)
##def test_string_length():
##     assert string_length('rishyjee')==8
##     assert string_length('Sushil')==6
##     assert string_length('Mayuri')==6
##     assert string_length('Amir')==4
##     assert string_length('Surendra')==8
##     print('THE CODE IS CORRECT SIRJEE')
##
##test_string_length()     
def string_length(my_string):
     count=0
     for letter in my_string[:]:
          count+=1 #increment count by 1
          #print(my_string)
     return count

def test_string_length():
     assert string_length('rishyjee')==8
     assert string_length('Sushil')==6
     assert string_length('Mayuri')==6
     assert string_length('Amir')==4
     assert string_length('Surendra')==8
     print('THE CODE IS CORRECT SIRJEE')
     
test_string_length()
