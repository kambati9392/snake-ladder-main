import random
def die():
    global die_roll
    die_roll=random.randrange(1,6)
    return die_roll
print(die())
pos=0
pos=pos+die_roll
print(pos)
