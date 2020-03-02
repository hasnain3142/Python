def replace(SecretWord,guess,table):
      ind = SecretWord.index(guess)
      table[ind] = guess
      for i in range(1,SecretWord.count(guess)):
          table[SecretWord.index(guess,ind+1)] = guess
          ind = SecretWord.index(guess, ind+1)
