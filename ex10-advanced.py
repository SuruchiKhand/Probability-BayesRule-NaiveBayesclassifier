import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] #normal die
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5] #loaded die

def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    sequence = np.random.choice(6, size=10, p=p) + 1
    for roll in sequence:
        print("rolled %d" % roll)
    return sequence
        
def bayes(sequence):
    odds = 1.0
    for roll in sequence:
        i = roll - 1
        r = p2[i] / p1[i]
        odds *= r
    return odds > 1

sequence = roll(True)
if bayes(sequence):
    print("I think loaded.")
else:
    print("I think normal")

