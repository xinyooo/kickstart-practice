T = int(input())

for i in range(T):
    A, B = list(map(int, input().split()))
    N = int(input())
    for j in range(N):
        GUESS = (A+B)//2
        print(GUESS, flush=True)
        s = input()
        if s == 'TOO_BIG':
            B = GUESS-1
        elif s == 'TOO_SMALL':
            A = GUESS+1
        elif s == 'CORRECT':
            break