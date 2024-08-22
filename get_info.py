from datetime import datetime

# get depart + arrive airports
def get_depart_arrival():
    while True:
        depart = input("Departure airport code('DEN'): ")
        if len(depart) == 3:
            print(f'Departure airport {depart} accepted!')
            break
        else:
            print('Code must be 3 letters.')
            
    while True:
        arrival = input('Departure airport code("LON"): ')
        if len(arrival) == 3:
            print(f'Arrival airport {arrival} accepted')
            break
        else:
            print('Code must be 3 letters.')     

# get date
def get_flight_date():
    while True:
        
        date_str = input('estimated date of trip(yyyymmdd): ')
        try:
            d = datetime.strptime(date_str, '%Y%m%d')
            print('Valid Date')
            break
        except ValueError:
            print('Incorrect date format, should be YYYY-MM-DD')


