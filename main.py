from database import initialize_db
from models import User, Drama

def main():
    initialize_db()

    while True:
        print("\n--- Drama Manager ---")
        print("1. Create user")
        print("2. Add drama")
        print("3. List dramas")
        print("4. Complete drama")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user = User(name, email)
            user.save()
            print(f"User created: {user.name}")

        elif choice == "2":
            users = User.get_all()
            for u in users:
                print(f"{u.id}. {u.name}")
            user_id = int(input("Choose user ID: "))
            title = input("Drama title: ")
            desc = input("Drama description: ")
            due = input("Watch date (YYYY-MM-DD): ")
            drama = Drama(title, desc, due, user_id)
            drama.save()
            print(f"Drama added: {drama.title}")

        elif choice == "3":
            dramas = Drama.get_all()
            for d in dramas:
                status = "Done" if d.completed else "Pending"
                print(f"{d.id}. {d.title} ({status}) - Due {d.watch_date} [User {d.user_id}]")

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            Drama.mark_completed(task_id)
            print("Drama marked as completed!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

