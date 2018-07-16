l = []

for x in range (1, 6): 
    for y in range (20, 51): 
        if y % x == 0:
            l.append(True)
        else: 
            l.append(False)
# print(l)

nl = []
for i in range(0, 20):
    if i % 3 == 0: 
        nl.append(i)
# print(nl)

#List comprehension (same result as code above)
lc = [y%x == 0 for x in range(1, 6) for y in range (20, 51)]
# print(lc)

nnl = [i for i in range (0, 20) if i % 3 == 0]
# print(nnl)

words = ["hello", "world", "this", "is", "a", "tough", "challenge"]
new_words = [x.upper() for x in words if x[0] != "t"]
# new_words = [x.upper() for x in words if not x.startswith("t")]

# print(new_words)

number_dict = {x: x%4 == 0 for x in range(10, 31)}
print(number_dict)