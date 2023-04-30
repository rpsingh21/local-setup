from math import pow
from sys import argv

r, t = eval(argv[1]), int(argv[2])
Rc = pow((100+r*t) * (100**(t-1)), 1/t) - 100
print(Rc)
