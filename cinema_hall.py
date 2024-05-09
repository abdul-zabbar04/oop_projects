class Star_Cinema:
    hall_list= []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats= {}        # here I don't private seats, rows, cols attributes, because I need to access this attributes outside this class.
        self.__show_list= []    # __show_list: private attribute
        self.rows= rows
        self.cols= cols
        self.__hall_no= hall_no # __hall_no: private attribute
        super().entry_hall(self)

    def entry_show(self, id, name, time):
        newShow= (id, name, time)
        self.__show_list.append(newShow)
        self.seats[id]= [[0 for i in range(self.cols)] for j in range(self.rows)]

    def book_seats(self, id, seats):
        for i, j in seats:
            self.seats[id][i][j]= 1

    def view_show_list(self):
        for hall in Star_Cinema.hall_list:
            for show in hall.__show_list:
                print(f'\'Id: {show[0]}\', \' Movie Name: {show[1]}\', \'Time: {show[2]}\'')

    def view_available_seats(self, show_id):
        x= self.seats.get(show_id, 'no')
        if x!= 'no':
            for i in x:
                print(i)
        else:
            print('invalid Show id!')

hall1= Hall(5, 6, 1)
hall2= Hall(6, 7, 2)
hall1.entry_show('101', 'Tiger', '7.00 PM')
hall1.entry_show('102', 'Jawyan', '10.00 PM')
hall2.entry_show('201', 'Don', '7.00 pm')
hall2.entry_show('202', 'KGF', '10.00 pm')

run= True

while run:
    print('1. VIEW ALL SHOW TODAY: ')
    print('2. VIEW AVAILABLE SEATS: ')
    print('3. BOOK TICKET: ')
    print('4. EXIT: ')
    opt= int(input('Enter an option: '))
    print()

    if opt==1:
        print('\tToday\'s All Shows: ')
        hall1.view_show_list()
        print()

    elif opt==2:
        show_id= input('Enter Show id: ')
        hall= None
        for h in Star_Cinema.hall_list:
            for id in h.seats.keys():
                if id== show_id:
                    hall = h

        if hall!= None:
            print(f'Available seats for show {show_id}')
            hall.view_available_seats(show_id)
            print()
            print('\'1\' means already booked and \'0\' means available seats')
        else:
            print('Invalid show id!')
        print()

    elif opt==3:
        show_id= input('Enter show id: ')
        hall= None
        for h in Star_Cinema.hall_list:
            for id in h.seats.keys():
                if id== show_id:
                    hall= h
        if hall!=None:
            no_of_tickets= int(input('Enter no of ticket: '))
            for i in range(no_of_tickets):
                row= int(input(f'Enter row(0-{hall.rows-1}): '))
                col= int(input(f'Enter col(0-{hall.cols-1}): '))
                if row<0 or row>=hall.rows or col<0 or col>=hall.cols:
                    print('Invalid seat')

                elif hall.seats[show_id][row][col]==1:
                    print('Already booked, try other seat')
                else:
                    seat= [(row, col)]
                    hall.book_seats(show_id, seat)
                    print(f'{row, col} seat booked successfully for {show_id}')
        else:
            print('Invalid show id')
        print()

    elif opt==4:
        run= False
        print('Exited')
        print()

    else:
        print('Invalid option')
        print()

            


