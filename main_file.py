import system_data
def main():
    while True:
        print("\nMenu:")
        print("1. get cpu info")
        print("2. get memory info")
        print("3. get disk info")
        print("4. Option 4")
        print("5. Option 5")
        print("6. Option 6")
        print("7. Option 7")
        print("8. Option 8")
        print("9. Exit")
        choice = input("Please select an option (1-9): ")
        if choice == '1':
            system_data.get_cpu_info()
        elif choice == '2':
            print(f"{system_data.get_memory_info()}")
        elif choice == '3':
            print(f"{system_data.get_disk_info()}")
        elif choice == '4':
            print("You selected Option 4.")
        elif choice == '5':
            print("You selected Option 5.")
        elif choice == '6':
            print("You selected Option 6.")
        elif choice == '7':
            print("You selected Option 7.")
        elif choice == '8':
            print("You selected Option 8.")
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
