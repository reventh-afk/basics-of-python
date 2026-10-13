size = 10
hash_table = [None] * size

def insert(roll, name):
    index = roll % size

    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is None:
            hash_table[pos] = (roll, name)
            print("Student record inserted")
            return
    print("Hash table is full")

def search(roll):
    index = roll % size

    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is None:
            break
        if hash_table[pos][0] == roll:
            print("Student found:", hash_table[pos])
            return
    print("Student not found")

def delete(roll):
    for i in range(size):
        pos = (roll % size + i) % size
        if hash_table[pos] is not None and hash_table[pos][0] == roll:
            hash_table[pos] = "DELETED"
            print("Student record deleted")
            return
    print("Student not found")

def display():
    print("\nHash Table:")
    for i, record in enumerate(hash_table):
        print(i, ":", record)

while True:
    print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        roll = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        insert(roll, name)
    elif choice == '2':
        roll = int(input("Enter roll number: "))
        search(roll)
    elif choice == '3':
        roll = int(input("Enter roll number: "))
        delete(roll)
    elif choice == '4':
        display()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
