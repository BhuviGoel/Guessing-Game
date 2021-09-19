name = input("Enter a string: ")
word = 0
character = 1
for letter in name: 
      character = character + 1
      if(letter==" "):
            word = word+1
print ("Number of words in the string: ")
print (word)
print ("Number of characters in the string: " )
print (character)
