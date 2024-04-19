# InjamTanvir(INJAM UL HAQUE)


# Part 1
class Star_Cinema:
    _hall_list = []  # Private class attribute for hold list of halls

    def entry_hall(self, hall):
        """Add a hall to the cinema."""
        Star_Cinema._hall_list.append(hall)


# Part 2
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        cinema = Star_Cinema()
        cinema.entry_hall(self)

    # Part 3 --> extra made by me authentication to add show
    def __authenticate_manager(self):
        password = input("Enter manager password(pass--> admin123): ")
        return password == "admin123"

    def add_show(self):
        if self.__authenticate_manager():
            show_id = input("Enter show ID: ")
            movie_name = input("Enter movie name: ")
            show_time = input("Enter show time: ")
            if show_id in self.__seats:
                print("Show ID already exists.")
                return
            self.__show_list.append((show_id, movie_name, show_time))
            self.__seats[show_id] = [["Free" for _ in range(self.__cols)] for _ in range(self.__rows)]
            print("Show added successfully.")
        else:
            print("Authentication failed. Access denied.")

    def remove_show(self):
        if self.__authenticate_manager():
            show_id = input("Enter show ID to remove: ")
            if any(show_id == show[0] for show in self.__show_list):
                self.__show_list = [show for show in self.__show_list if show[0] != show_id]
                del self.__seats[show_id]
                print("Show removed successfully.")
            else:
                print("Show ID not found.")
        else:
            print("Authentication failed. Access denied.")

    # Part 4
    def book_seats(self, show_id, seats_to_book):
        if show_id not in self.__seats:
            raise ValueError("Show ID not found")
        for row, col in seats_to_book:
            if not (0 <= row < self.__rows) or not (0 <= col < self.__cols):
                raise ValueError("Seat position out of capacity")
            if self.__seats[show_id][row][col] != "Free":
                raise ValueError("Seat already booked")
            self.__seats[show_id][row][col] = "Booked"
        print("Seats booked successfully.")

    # Part 5 and 6
    def view_show_list(self):
        """Return the list of all shows in the hall."""
        return self.__show_list

    def view_available_seats(self, show_id):
        """Show available seats for a particular show."""
        if show_id not in self.__seats:
            raise ValueError("Show ID not found")
        available_seats = [(row, col) for row in range(self.__rows) for col in range(self.__cols)
                           if self.__seats[show_id][row][col] == "Free"]
        return available_seats
    
print("################################################################")
print("----------------------------------------------------------------")
print("###############   WELCOME TO STAR CINEMA    ####################")
print("----------------------------------------------------------------")
print("################################################################")

# Error handeling and Part 7 to 9
def main_interface(hall):
    user_type = None
    while user_type not in ('M', 'C'):
        user_type = input("Are you a Manager (M) or a Customer (C)? ").upper()
        
        if user_type == 'M':
            while True:
                print("\n1. Add Show")
                print("2. Remove Show")
                print("3. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    hall.add_show()
                elif choice == "2":
                    hall.remove_show()
                elif choice == "3":
                    print("Exiting...")
                    break
                else:
                    print("Invalid option, please try again.")
        
        elif user_type == 'C':
            while True:
                print("\n1. View all shows")
                print("2. View available tickets")
                print("3. Book ticket")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    shows = hall.view_show_list()
                    for show in shows:
                        print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
                elif choice == "2":
                    show_id = input("Enter show ID to check available seats: ")
                    try:
                        available_seats = hall.view_available_seats(show_id)
                        print("Available seats:", available_seats)
                    except ValueError as e:
                        print(e)
                elif choice == "3":
                    show_id = input("Enter show ID to book seats for: ")
                    seats_raw = input("Enter seats to book (row,col): ")
                    seats_to_book = [(int(row), int(col)) for row, col in (seat.split(',') for seat in seats_raw.split())]
                    try:
                        hall.book_seats(show_id, seats_to_book)
                    except ValueError as e:
                        print(e)
                elif choice == "4":
                    print("Exiting...")
                    break
                else:
                    print("Invalid option, please try again.")


if __name__ == "__main__":
    hall = Hall(10, 10, 1)  # Initializing the Hall Size 
    while True:
        main_interface(hall) 

