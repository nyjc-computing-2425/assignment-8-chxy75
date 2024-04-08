# Built-in imports
def reverse(text):
  if len(text) <= 1:
      return text
  else:
      return reverse(text[1:]) + text[0]

def is_palindrome(text):
  text =  text.replace('!','').replace('?','').replace(' ','')
  if text[0] == text[-1]:
    while len(text) >= 2:
     is_palindrome(text[1:-1])
    else :
      return True
  else:
    return False