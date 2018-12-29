# my initial flock
mySheep = [5,7,300,90,24,50,75]
print("Hello, my name is Loc and these are my sheep sizes:")
print(mySheep)

# Function that presents flock after 1 month
def grow_sheep(_month) :
    for grow in range(len(mySheep)):
        mySheep[grow] += 50
    print(_month,"months has passed, now here is my flock",mySheep)
# Finction that finds the biggest sheep and shear it

def shear_sheep() :
    biggest_sheep = max(mySheep)
    print("Now my biggest Sheep has size:",biggest_sheep,"let's shear it")
    for shear in range(len(mySheep)):
        if mySheep[shear] == biggest_sheep:
            mySheep[shear] = 8
    print("After shearing, here is my flock:",mySheep)


# Flock after 1,2,3 month
grow_sheep(1)
shear_sheep()
grow_sheep(2)
shear_sheep()
grow_sheep(3)
shear_sheep()

total_flock = 0
for (grow,val) in enumerate(mySheep):
        total_flock += val
print("My flock has size in total:", total_flock)
print("I would get:",total_flock*2,"$")

