
for i in range(20):         # Això recorre del 0 al 19
    print(i)
    if i<10:
        continue
    if i%2==0:
        print("Es parell")
    if i>=15:
        break

print("Final del bucle")