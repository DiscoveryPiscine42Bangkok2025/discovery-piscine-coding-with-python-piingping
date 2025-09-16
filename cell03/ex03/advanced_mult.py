i = 0
while (i<=10):
    j = 0
    print(f"Table de {i}: ",end='')
    while (j<=10):
        if j == 10:
            print(i*j)
        else:
            print(i*j,end=' ')
        j+=1
    i+=1
    
