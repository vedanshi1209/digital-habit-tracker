activities = []

def add_activity():
    name = input("Enter activity (e.g., Instagram, Study): ")
    time = float(input("Enter time spent (in hours): "))

    if name.lower() in ["study", "coding", "learning"]:
        category = "Productive"
    else:
        category = "Unproductive"

    activities.append((name, time, category))
    print("Activity added!\n")

def show_summary():
    total = 0
    productive = 0
    unproductive = 0

    for act in activities:
        total += act[1]
        if act[2] == "Productive":
            productive += act[1]
        else:
            unproductive += act[1]

    print("\n--- Summary ---")
    print("Total Time:", total)
    print("Productive Time:", productive)
    print("Unproductive Time:", unproductive)

    if unproductive > productive:
        print("⚠️ Try reducing unproductive activities!")
    else:
        print("✅ Good job! Keep it up!")

def main():
    while True:
        print("\n1. Add Activity")
        print("2. Show Summary")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_activity()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()