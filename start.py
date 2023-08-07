def main():
    while True:
        print("Welcome to the Time Tracker Application")
        print("Please select an option:")
        print("1. Time Tracking")
        print("2. Reporting")
        print("3. Maintenance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            # Start the Time Tracking part
            import tt_main

            tt_main.main()
        elif choice == "2":
            # Start the Reporting part
            import report_main

            report_main.main()
        elif choice == "3":
            # Start the Maintenance part
            import maintain_main

            maintain_main.main()
        elif choice == "4":
            print("Thank you for using the Time Tracker Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
