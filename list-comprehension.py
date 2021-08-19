if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
listx = [i for i in range(x+1)]
listy = [i for i in range(y+1)]
listz = [i for i in range(z+1)]
result=[]
for i in listx:
    for j in listy:
        for k in listz:
            if (i+j+k)!=n:
                li=[i,j,k]
                result.append(li)
print(result)
