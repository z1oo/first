x = (1, 2, 3, 4, "war")
y = [x[0], x[4]]
y[0] += 10
print(y, len(y), type(y))
print(x, len(x), type(x))
print("end of program")