def reverse(text): 
  reversed_text = ""
  for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]
  return reversed_text
pass

 # My approach ----->
 # initialising empty string to hold reversed text
 # iterating through string in reverse order
 # appending each char from end to beginning