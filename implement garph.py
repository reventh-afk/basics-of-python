n = int(input("Enter the total number of users: "))


adj_matrix = [[0 for _ in range(n)] for _ in range(n)]


adj_list = [[] for _ in range(n)]


connections = int(input("Enter the number of friendships: "))

print("\nEnter the friendships (user numbers from 0 to", n - 1, "):")

for _ in range(connections):
    u, v = map(int, input("Enter two users: ").split())

   
    if 0 <= u < n and 0 <= v < n:
       
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

        adj_list[u].append(v)
        adj_list[v].append(u)
    else:
        print("Invalid user number!")


print("\n--- Adjacency Matrix ---")


print("   ", end="")
for i in range(n):
    print(i, end=" ")
print()

for i in range(n):
    print(i, ":", end=" ")
    for j in range(n):
        print(adj_matrix[i][j], end=" ")
    print()


print("\n--- Adjacency List ---")

for i in range(n):
    print(f"User {i} ->", end=" ")
    if adj_list[i]:
        print(" -> ".join(map(str, adj_list[i])))
    else:
        print("No friends")


print("\n--- Check Friendship ---")

u, v = map(int, input("Enter two users to check friendship: ").split())

if 0 <= u < n and 0 <= v < n:
    if adj_matrix[u][v] == 1:
        print(f"User {u} and User {v} are directly connected (friends).")
    else:
        print(f"User {u} and User {v} are not directly connected.")
else:
    print("Invalid user number!")
