import random
pos=0
def die():
    # global die_roll
      die_roll=random.randrange(1,6) # die rolls it gives random number
      return die_roll


def chance():
      nls=random.randrange(3)
      return nls
n=chance()
if n==0:
    pos=pos+die()
    print(pos)
elif n==1:
    pos=pos+die()
    print(pos)
else:
     pos-=die()
     print(pos)


print("current position =",pos)

       



