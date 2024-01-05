a = []
b = []


fn = int(input("Input first n\n"))
sn = int(input("Input second n\n"))

for i in range(fn):
    a[i] = int(input("Input first array elem\n"))

for i in range(sn):
    b[i] = int(input("Input second array elem\n"))

set_a = set(a)
set_b = set(b)

intersect = sorted(list(set_a.intersection(set_b)))

print(intersect)
