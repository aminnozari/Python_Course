class TimeConverter:
    def __init__(self):
        pass

    def correct_time(self, minutes, seconds):
        if seconds >= 60:
            minutes += seconds // 60
            seconds %= 60
        elif seconds < 0:
            minutes -= abs(seconds) // 60 + 1
            seconds += (abs(seconds) // 60 + 1) * 60
        if minutes >= 60:
            minutes %= 60
        elif minutes < 0:
            minutes = abs(minutes) % 60

        return minutes, seconds

    def convert_to_time(self, total_seconds):
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return minutes, seconds

    def convert_to_seconds(self, minutes, seconds):
        total_seconds = minutes * 60 + seconds
        return total_seconds

    def add_time(self):
        print("Enter the first time: ")
        minutes1 = int(input("Minutes: "))
        seconds1 = int(input("Seconds: "))
        print("Enter the second time: ")
        minutes2 = int(input("Minutes: "))
        seconds2 = int(input("Seconds: "))

        total_minutes = minutes1 + minutes2
        total_seconds = seconds1 + seconds2
        total_minutes, total_seconds = self.correct_time(total_minutes, total_seconds)

        return total_minutes, total_seconds

    def subtract_time(self):
        print("Enter the start time: ")
        minutes1 = int(input("Minutes: "))
        seconds1 = int(input("Seconds: "))
        print("Enter the end time: ")
        minutes2 = int(input("Minutes: "))
        seconds2 = int(input("Seconds: "))

        total_minutes = minutes2 - minutes1
        total_seconds = seconds2 - seconds1
        total_minutes, total_seconds = self.correct_time(total_minutes, total_seconds)

        return total_minutes, total_seconds


time_converter = TimeConverter()

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add two times")
    print("2. Subtract two times")
    print("3. Convert seconds to time")
    print("4. Convert time to seconds")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        total_minutes, total_seconds = time_converter.add_time()
        print(f"The total time is {total_minutes} minutes and {total_seconds} seconds.")
    elif choice == '2':
        total_minutes, total_seconds = time_converter.subtract_time()
        print(f"The elapsed time is {total_minutes} minutes and {total_seconds} seconds.")
    elif choice == '3':
        total_seconds = int(input("Enter the number of seconds: "))
        minutes, seconds = time_converter.convert_to_time(total_seconds)
        print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
    elif choice == '4':
        print("Enter the time: ")
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))
        total_seconds = time_converter.convert_to_seconds(minutes, seconds)
        print(f"The total number of seconds is {total_seconds} seconds.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
