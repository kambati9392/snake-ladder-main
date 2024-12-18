import random
pos=0
def die():
    # global die_roll
      die_roll=random.randrange(1,6) # die rolls it gives random number
      return die_roll
def chance():
      nls=random.randrange(3)
      return nls
# count =0
while pos<100:
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

    if pos==100:
         print("player wins the game")
    elif pos<0:
        pos=0
   
       



