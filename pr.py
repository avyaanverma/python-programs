n = int(input("Enter the number"))
s = set(map(int,input().split()))
N = int(input(""))

for i in range(N):
    ip = input("INPUT COMMAND").split()
    if ip[0]=='remove':
        s.remove(int(ip[1]))
    elif ip[0]=='discard':
        s.discard(int(i[1]))
    else: 
        s.pop()

print(sum(list(s)))