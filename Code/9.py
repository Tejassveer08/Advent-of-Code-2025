from itertools import tee, combinations

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

red = list(map(eval, open('D9Input.txt')))

area = lambda x,y, u,v: (u-x+1) * (v-y+1)

pairs, lines = [
    sorted(
        ((min(a,c), min(b,d), max(a,c), max(b,d)) for (a,b),(c,d) in P),
        key=lambda p: area(*p),
        reverse=True
    )
    for P in (combinations(red, r=2), pairwise(red + [red[0]]))
]

print('p1:', area(*pairs[0]))

for x,y, u,v in pairs:
    for p,q, r,s in lines:
        if p<u and q<v and r>x and s>y:
            break
    else:
        print('p2:', area(x,y, u,v))
        break
