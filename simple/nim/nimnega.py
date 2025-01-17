# compute nim values using negamax and a dictionary
#   that holds values already computed     RBH 2019

def get_piles():
   while True:
       raw = input('nim game pile sizes (eg. 3 5 7)   ')
       try:
          dim = tuple( int(x) for x in raw.split() )
          if len(dim) > 0 and all(d >= 0 for d in dim):
             return dim
       except ValueError:
          pass
       print('invalid, try again')

"""
sd         dictionary(state: boolean), true if player-to-move wins
"""
def winning(nim_psn, sd, depth):  # tuple, dictionary, recursion depth
  #print("here  " , nim_psn,   "   ", sd)
  if nim_psn in sd:
    return sd[nim_psn]
  # nim_psn not in dictionary, so update before we return
  print('  '*depth, nim_psn)
  # check a losing postion (0, 0 ,0) @return False
  if all(p == 0 for p in nim_psn): # we lose if every pile empty
    sd.update({ nim_psn: False })  # update before return
    return False
    
  # remove duplicates, isomorphism
  psn = tuple(sorted(nim_psn))

  # start the sorted psn = ( *1, *2, *3)  *1<=*2<=*3
  for j in range(len(psn)): # each pile
    for k in range(psn[j]): # number of stones that will remain in that pile
      child = tuple(sorted(psn[:j] + (k,) + psn[j+1:]))
      if not winning(child, sd, depth+1): # if the deeper station is losing state, then this state is a winning state.  
        sd.update({ nim_psn: True })   # update before return
        if depth == 0: print('\nwinning: move to ',child)    # show a winning move 
        return True
  
  # current state cannot go to a False state and we set it to a Loosing state
  sd.update({ nim_psn: False })  # update before return
  # if we finish all the loop ans still not finish/end the program then we return a losing postion for the current state
  if depth == 0: print('\nlosing')
  return False

v = get_piles()
S = dict()
w = winning(v,S,0)
