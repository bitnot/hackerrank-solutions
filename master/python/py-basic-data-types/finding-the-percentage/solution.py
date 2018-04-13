n = int(input())
averages={}

for i in range(n):
    (name, maths, physics, chemistry) = input().split( )
    (maths, physics, chemistry) = (float(maths), float(physics), float(chemistry))
    averages[name] = (maths + physics + chemistry) / 3.0

name = input()
print("{:0.2f}".format(averages[name]))
