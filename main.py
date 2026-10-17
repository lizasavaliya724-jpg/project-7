import time

from modules import (
    datetime_utils,
    math_utils,
    random_utils,
    uuid_utils,
    file_utils
)


def main():
    while True:
        print("\n===== PROJECT 7 =====")
        print("1. Date and Time")
        print("2. Mathematics")
        print("3. Random Generator")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Modules")
        print("7. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                print("1. Current Date and Time")
                print("2. Date Difference")
                print("3. Formatted Date")
                print("4. Stopwatch")
                print("5. Countdown")

                option = input("Choose option: ")

                if option == "1":
                    print(datetime_utils.current_datetime())

                elif option == "2":
                    d1 = input("First date (YYYY-MM-DD): ")
                    d2 = input("Second date (YYYY-MM-DD): ")
                    print("Days:", datetime_utils.date_difference(d1, d2))

                elif option == "3":
                    print(datetime_utils.formatted_date())

                elif option == "4":
                    input("Press Enter to start")
                    start = time.time()
                    input("Press Enter to stop")
                    print("Seconds:", round(datetime_utils.stopwatch(start), 2))

                elif option == "5":
                    seconds = int(input("Enter seconds: "))
                    if seconds < 0:
                        print("Enter a non-negative number")
                    else:
                        datetime_utils.countdown(seconds)

                else:
                    print("Invalid option")

            elif choice == "2":
                print("1. Factorial")
                print("2. Compound Amount")
                print("3. Circle Area")
                print("4. Rectangle Area")
                print("5. Triangle Area")
                print("6. Trigonometry")

                option = input("Choose option: ")

                if option == "1":
                    n = int(input("Enter number: "))
                    print("Factorial:", math_utils.factorial(n))

                elif option == "2":
                    p = float(input("Principal: "))
                    r = float(input("Rate (%): "))
                    t = float(input("Years: "))
                    print("Amount:", round(math_utils.compound_amount(p, r, t), 2))

                elif option == "3":
                    r = float(input("Radius: "))
                    print("Area:", math_utils.circle_area(r))

                elif option == "4":
                    l = float(input("Length: "))
                    w = float(input("Width: "))
                    print("Area:", math_utils.rectangle_area(l, w))

                elif option == "5":
                    b = float(input("Base: "))
                    h = float(input("Height: "))
                    print("Area:", math_utils.triangle_area(b, h))

                elif option == "6":
                    angle = float(input("Angle in degrees: "))
                    print("Sine:", math_utils.sine(angle))
                    print("Cosine:", math_utils.cosine(angle))
                    print("Tangent:", math_utils.tangent(angle))

                else:
                    print("Invalid option")

            elif choice == "3":
                print("1. Random Number")
                print("2. Random List")
                print("3. Password")
                print("4. OTP")

                option = input("Choose option: ")

                if option == "1":
                    low = int(input("Minimum: "))
                    high = int(input("Maximum: "))
                    print(random_utils.random_number(low, high))

                elif option == "2":
                    count = int(input("Number of items: "))
                    low = int(input("Minimum: "))
                    high = int(input("Maximum: "))
                    print(random_utils.random_list(count, low, high))

                elif option == "3":
                    length = int(input("Password length: "))
                    print(random_utils.password(length))

                elif option == "4":
                    length = int(input("OTP length (4-10): "))
                    print(random_utils.otp(length))

                else:
                    print("Invalid option")

            elif choice == "4":
                print("UUID:", uuid_utils.generate_uuid())

            elif choice == "5":
                print("1. Create File")
                print("2. Write File")
                print("3. Read File")
                print("4. Append File")

                option = input("Choose option: ")

                if option not in ("1", "2", "3", "4"):
                    print("Invalid option")
                    continue

                filename = input("Enter file name: ")

                if option == "1":
                    file_utils.create_file(filename)
                    print("File created")

                elif option == "2":
                    content = input("Enter content: ")
                    file_utils.write_file(filename, content)
                    print("Content written")

                elif option == "3":
                    print(file_utils.read_file(filename))

                elif option == "4":
                    content = input("Enter content: ")
                    file_utils.append_file(filename, content)
                    print("Content appended")

            elif choice == "6":
                print("Datetime:", dir(datetime_utils))
                print("Math:", dir(math_utils))
                print("Random:", dir(random_utils))
                print("UUID:", dir(uuid_utils))
                print("Files:", dir(file_utils))

            elif choice == "7":
                print("Thank you!")
                break

            else:
                print("Invalid choice")

        except (ValueError, OSError, OverflowError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()