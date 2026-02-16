l1 = [i+1 for i in range(7)]
l2 = [j+1 for j in range(4)]


intervalo = min(len(l1),len(l2))
print([(l1[i]+l2[i]) for i in range(intervalo)])