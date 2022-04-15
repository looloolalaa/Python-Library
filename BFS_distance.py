"""
4 6
101111
101010
101011
111011
"""

from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]

    visited = [[False for _ in range(m)] for _ in range(n)]
    dis = [[float('inf') for _ in range(m)] for _ in range(n)]

    move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isvalid(p):
        return 0 <= p[0] < n and 0 <= p[1] < m and maze[p[0]][p[1]] == '1'

    def bfs(s):
        que = deque()

        que.append(s)
        visited[s[0]][s[1]] = True
        dis[s[0]][s[1]] = 0
        while que:
            now = que.popleft()
            for m in move:
                a = (now[0]+m[0], now[1]+m[1])
                if isvalid(a) and not visited[a[0]][a[1]]:
                    que.append(a)
                    visited[a[0]][a[1]] = True
                    dis[a[0]][a[1]] = dis[now[0]][now[1]] + 1


    bfs((0, 0))
    for d in dis:
        print(d)
