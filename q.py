 a = 5
 b = 6
 d = a < b
 e = not a
 if not c or d:
     print("One")
elif not c or not d and e:
    print("Two")
elif not c or d or not e and d:
    print("Three")
else:
    print("Four")