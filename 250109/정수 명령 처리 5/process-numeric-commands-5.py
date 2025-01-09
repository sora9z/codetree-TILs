N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Write your code here!
result = []

for i in command:
    n = num.pop(0)
    if i == 'push_back':
        result.append(n)
    elif i == 'pop_back':
        result.pop()
    elif i == 'size':
        print(len(result))
    elif i == 'get':
        print(result[n-1])
