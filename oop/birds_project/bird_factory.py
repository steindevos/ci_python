from birds.bird import Bird, Seabird, Fowl, Owls  #go to birds directory, find bird file, import Bird class

my_bird2 = Bird("HankyPanky", "bookbookboom")
my_bird = Bird("Kevin", "Chirp")
my_bird3 = Bird("Rita", "what!?")

# print(my_bird2.call)
# print(my_bird2.kind)
# print(my_bird.kind)
# print(my_bird3.call)
# print(my_bird3)
print(my_bird3.get_description())

my_sea_going_bird = Seabird("Gull", "Skraaawwk!", 2)

print(my_sea_going_bird.diving_depth)
print(my_sea_going_bird.get_description())

my_owl = Owls("Little owl", "Screeech!", "mousehair")
my_fowl = Fowl("Chicken", "Pock!", "landfowl")
print(my_fowl.get_description())
print(my_owl.get_description())