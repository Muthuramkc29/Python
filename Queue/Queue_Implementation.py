from collections import deque

que = deque()
for i in range(1,11):
    que.append(bin(i)[2:])
    print(que.popleft())

#while not len(que) == 0:
 #   print(que.popleft())
