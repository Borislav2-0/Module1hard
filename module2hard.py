import random

left = random.randrange(3, 20)

print(left)
right = ''
for i in range(1, left):
    for j in range(i, left):
        if left % (i + j) == 0:
            if str(i) == str(j):
                continue
            right = right + str(i) + str(j)

print(right)