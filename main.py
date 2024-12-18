import random
pos=0
def die():
    # global die_roll
      die_roll=random.randrange(1,6) # die rolls it gives random number
      return die_roll

count =0
def chance():
      nls=random.randrange(3)
      return nls

while pos<100:
    count+=1
    n=chance()
    check=die()
    if pos+check<=100:
      pos=pos+check
    if pos ==100:
       print("current position =",pos)
    if pos<100:
        
        if n==1:
           check=die()
           if pos+check<=100:
             pos=pos+check
        elif n==2:
            pos=pos-die()

        print("current position =",pos)
    if pos<0:
     pos=0
    if pos>100:
       pos=pos
    if pos ==100:
       print("win!!!")
       print("number of dies rolled to win!!---->",count)
       



