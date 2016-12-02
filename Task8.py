Task 8- remove vowels
message = input ("enter message :")
new_message = ""
vowels = ("a","e","i","o","u") # tuple an array 

print ()
for letter in message:
    if letter.lower() not in vowels:
        new_message += letter
print (new_message)


