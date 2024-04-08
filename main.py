# Built-in imports
import string

def reverse(text:str) -> str:
  """
  reverse a given string

  Parameters
  ----------
  text:str
      the string to be reversed

  Returns
  -------
  str
  """
  if len(text) <= 1:
      return text
  else:
      return reverse(text[1:]) + text[0]

def is_palindrome(text:str) -> bool:
  """
  check if a given string is palindrome

  Parameters
  ----------
  text:str
      the string to be checked

  Returns
  -------
  bool
  """
  translator = str.maketrans("", "", string.punctuation)
  text = text.translate(translator).lower().replace(' ','')
  
  if len(text) <= 1:
      return True
  else:
      if text[0] != text[-1]:
          return False
      else:
          return is_palindrome(text[1:-1])

#reverse('hello')

#print(is_palindrome("A man, a plan, a canal: Panama")) 
  