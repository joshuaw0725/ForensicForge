from core.case_manager import create_case

def display_menu():
    print("\nMain Menu")
    print("1. Create new case")
    print("2. Open existing case")
    print("3. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        create_case()
        """
        Create a new forensic investigation case directory.

        Prompts the user for a case name, validates it, and creates a corresponding folder in the 'cases' directory.
        """
    elif choice == "2":
        print("\n[+] Open existing case - Coming soon!")
    elif choice == "3":
        print("\nExiting ForensicForge. Goodbye!")
        exit(0)
    else:
        print("\nInvalid option. Please try again.")
        display_menu()