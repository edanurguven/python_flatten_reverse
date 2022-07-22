input= [[1, 2], [3, 4], [5, 6, 7]]
input=(input)[::-1]
for i in range(len(input)):
    input[i]=(input[i])[::-1]
print(input)