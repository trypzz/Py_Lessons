b = int(input())
q = list()
if int(b) > 0:
    for i in range(0, b+1):
        for _ in range(0, i):
            if len(q) >= b:
                break
            else:
                q.append(str(i))

    for r in q:
        print(r, end=' ')
