size = int(input())
f_in = [int(x) for x in input().split()]
s_in = [int(x) for x in input().split()]
out = 0
im = False
for i in range(size):
    if f_in[i] > s_in[i]:
        im = True
    out+= abs(f_in[i] - s_in[i])
if im:
    print(-1)
else:
    print(out)
