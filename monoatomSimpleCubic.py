import periodictable as ptable
from scipy.constants import Avogadro 
from mendeleev import element


#Start from the SC

print("This program can only gives calculation for monoatomic simple cubic lattice")

radius = (float(input("What is the radius of the atom in pm? "))*10**-12)
atom = (str(input("What is the atom "))).capitalize()
#radius = element(atom).atomic_radius

print("What info do you want? ")
print("1. Volume of The lattice")
print("2. Density of the crystal")
userask = int(input("enter a number "))

def calcVol(r):
    return ((2*r)**3)

def calcDensity(y):
    return (getattr(ptable, atom).mass)/(calcVol(y)*Avogadro)

if userask == 1:
    print(calcVol(radius), " metre cubic")
else:
    print(calcDensity(radius)," gram/metre cubic")

'''atom = "Na"

print(getattr(ptable, atom).mass)'''