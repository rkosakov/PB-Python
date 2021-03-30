result = int(input())
combination = 0
for i in range(result + 1):
    for j in range(result + 1):
        for k in range(result + 1):
            if i + j + k == result:
                combination += 1
print(combination)
