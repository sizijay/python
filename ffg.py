G= int(input())
GL = []
for i in range(G):
    GL.append(int(input()))

GL.sort()
a = GL[1::2]
b = GL[0::2]

c = a[::-1] + b
k = 0
for j in range(1, len(c)):
    d = abs(c[j-1]-c[j])
    if d > k:
        k = d
print(k)
