if __name__ == '__main__':
    xs = []
    N = int(raw_input())
    for _ in range(N):
        comand = raw_input().strip().split()
        if comand[0] == 'insert':
            xs.insert(int(comand[1]), int(comand[2]))
        elif comand[0] == 'append':
            xs.append(int(comand[1]))
        elif comand[0] == 'remove':
            xs.remove(int(comand[1]))
        elif comand[0] == 'pop':
            xs.pop()
        elif comand[0] == 'sort':
            xs.sort()
        elif comand[0] == 'reverse':
            xs.reverse()
        elif comand[0] == 'print':
            print(xs)

