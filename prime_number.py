

prime_list = []

for i in range(0,50):
    if i == 0 or i == 1:
        continue
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            break
    else:
        prime_list.append(i)

print(prime_list)