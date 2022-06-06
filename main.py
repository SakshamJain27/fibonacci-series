sequence = [1,2]
for i in range(1, 99):
    sequence.append(sequence[-1]+sequence[-2])

print(sequence)
