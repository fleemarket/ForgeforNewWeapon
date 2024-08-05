import sys

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
cnt = 1

for i in range(len(H)):
    if i > 0:
        if H[i-1]<=H[i]:
            cnt += 1


print(cnt)