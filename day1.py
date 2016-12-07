# http://adventofcode.com/2016/day/1
# Answer Should be the absolute value of x + y.

input="R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"
array = input.split(", ")
x = 0
y = 0

# Directions:
#  1
# 4 2
#  3

direction = 1

for turn in array:
    print(turn)
    direct = turn[0]
    count = turn[1:]

    #Make the turn.
    if direction == 4 and direct == "R":
        direction = 1
    elif direction == 1 and direct == "L":
        direction = 4
    elif direct == "R":
        direction += 1
    elif direct == "L":
        direction -= 1

    #Take the steps
    if direction == 1:
        y += int(count)
    if direction == 2:
        x += int(count)
    if direction == 3:
        y -= int(count)
    if direction == 4:
        x -= int(count)

#Answer 
print(str(abs(x)+abs(y)))
