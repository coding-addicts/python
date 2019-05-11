def is_isogram(string):
  if not string: return True

  treated_string = string.replace(' ', '').replace('-', '').lower()
  for index, char in enumerate(treated_string, start = 1):
    if char in treated_string[:index - 1]: return False

  return True