"""
Given a String as input, insert a # after each character in the string. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "Hello12"
Output-> H#e#l#l#o#1#2#
"""

def recur(st):
  ln = len(st)
  if ln == 0:
    return ""
  ch = st[0]
  if (ch == ch):
    return ch + "#" + recur(st[1:])
    
st = "Hello12"
print(recur(st))
    