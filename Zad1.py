def fun(x):
  words_list = []
  character_even= "".join([y.upper() if i % 2 != 0 else y for i, y in enumerate(x)])
  character_odd = "".join([y.upper() if i % 2 == 0 else y for i, y in enumerate(x)])
  return([character_even, character_odd])    

  

print(fun('abcdef'))