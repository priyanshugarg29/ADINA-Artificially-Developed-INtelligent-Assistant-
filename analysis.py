from accessUserAttributes import accessUserAttributes
user_attributes = accessUserAttributes()
print(user_attributes)
total_searches = 0
for i in range (0, int(len(user_attributes))):
    total_searches = total_searches + user_attributes[i][1]
print(total_searches)
diff = total_searches/3
point = []
point.append(diff/2)

point.append(diff/2+diff)

point.append(diff/2 + 2*diff)
# what analysis
what_scene = user_attributes[0][1]

distance = []
for i in point:
    distance.append(abs(what_scene - i))
print(distance)
x = distance.index(min(distance))

if (x == 0):
    print("low what")
if (x == 1):
    print("medium what")
if (x == 2):
    print("high what")

#why analysis
why_scene = user_attributes[1][1]
distance = []
for i in point:
    distance.append(abs(why_scene-i))
x = distance.index(min(distance))

if (x == 0):
    print("low why")
if (x == 1):
    print("medium why")
if (x == 2):
    print("high why")

#how analysis
how_scene = user_attributes[2][1]
distance = []
for i in point:
    distance.append(abs(how_scene-i))
x = distance.index(min(distance))

if (x == 0):
    print("low how")
if (x == 1):
    print("medium how")
if (x == 2):
    print("high how")

#does analysis
does_scene = user_attributes[3][1]
distance = []
for i in point:
    distance.append(abs(does_scene-i))
x = distance.index(min(distance))

if (x == 0):
    print("low does")
if (x == 1):
    print("medium does")
if (x == 2):
    print("high does")

