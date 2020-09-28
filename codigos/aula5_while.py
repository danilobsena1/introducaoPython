i = 0

while i < 10:
    print(i, " ainda é menor que 10")
    i = i + 1

print("Acabou o while: ", i)

# ==========================================================

i = 0
while i < 15:
    if i == 13:
        break
    print(i)
    i = i + 1

print("=====================================================")

j = 0

while j < 20:
    j = j + 1
    if j == 11:
        continue
    print(j)

