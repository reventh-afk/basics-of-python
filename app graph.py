def dijkstra(graph, source, destination, n):
    dist = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n

    dist[source] = 0

    for _ in range(n):
        u = -1

        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        if u == -1 or dist[u] == float('inf'):
            break

        visited[u] = True

        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                new_dist = dist[u] + graph[u][v]

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u

    if dist[destination] == float('inf'):
        print("No path exists")
        return

    path = []
    current = destination

    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Shortest path:", " -> ".join(str(x + 1) for x in path))
    print("Shortest distance:", dist[destination])


n = int(input("Enter number of cities: "))

print("Enter adjacency matrix:")
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

source = int(input("Enter source city (1 to n): ")) - 1
destination = int(input("Enter destination city (1 to n): ")) - 1

dijkstra(graph, source, destination, n)
