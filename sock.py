import os
clear = lambda: os.system("cls")
ar = []
br = []    
n = int(input())
i = count = j = 0
ar = input().strip().split(" ")
for p in ar:
    if p not in br:
        br.insert(j,p)
        j = j + 1
        
for i in br:
    ch = ar.count(i)
    if(ch % 2)== 0:
        count += ch // 2;
    elif(ch > 1) and (ch % 2) != 0:
        ch = ch - 1;
        count += ch // 2;
clear()
print(count)

    

