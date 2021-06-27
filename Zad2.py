import collections

def count_char (word):
  """Return the number of letters occurring more than once."""
  c = collections.Counter(word.lower())
  over_two = {x: count for x, count in c.items() if count >= 2}

  key_list = [key for key in over_two.keys()]
  print(len(over_two), tuple(key_list))
  
  return(len(over_two)) 

print(count_char('aBcbA'))
print(count_char('RabarbArka'))