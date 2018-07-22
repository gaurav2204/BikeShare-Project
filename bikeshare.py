import pandas as pd
from datetime import datetime
from datetime import timedelta
import time

print("WELCOME Explorer US BikeShare Data Project by Gaurav Gupta")
def select_city_data():
    '''input user requirement for a city and returns
       the filename for that city's bike share data.
    '''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('Please choose one of the following Cities: Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Sorry, your selection is inappropriate.')

def select_time_period():
    '''input user requirement for a time period and returns the specified filter.
    '''
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\nWould you like to choose the data by month, day,'
                            ' or none(No time filter).\n')
        if time_period.lower() not in ['month', 'day', 'none']:
            print('Sorry, I do not understand your selection.')
    return time_period

def select_month():
    '''input user requirement for a month and returns the specified month.
    '''
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nSelect month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, I do not understand your selection. Please choose a '
                  'month in between January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

def select_day():
    '''input user requirement  for a day and returns the specified day.
    '''
    this_month = select_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:
        is_int = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Sorry,Please type your'
                      ' response as an integer.')
                day = input('\nWhich day? Please type your response as an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))

    print('-'*40)
def popular_month(df):
    '''In this function we find out most common month from start time.
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('common month : {}'.format(most_pop_month))
    print('-'*40)
def popular_day(df):
    '''In this function we find out most common day of week from start time.
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('common day of week from start time: {}'.format(most_pop_day))
    print('-'*40)
def popular_hour(df):
    '''Finds and prints the most popular hour of day for start time.
    '''
    popular_hr = int(df['start_time'].dt.hour.mode())
    if popular_hr == 0:
        am_pm = 'am'
        popular_hr_zone = 12
    elif 1 <= popular_hr < 13:
        am_pm = 'am'
        popular_hr_zone = popular_hr
    elif 13 <= popular_hr < 24:
        am_pm = 'pm'
        popular_hr_zone = popular_hr - 12
    print('common hour of day from start time : {}{}'.format(popular_hr_zone, am_pm))

    print('-'*40)
def stations_stats(df):
    '''Finds and prints the most popular start station and most popular end station.
    '''
    start_point = df['start_station'].mode().to_string(index = False)
    end_point = df['end_station'].mode().to_string(index = False)
    print('The most commonly used start station : {}'.format(start_point))
    print('The most commonly used end station : {}'.format(end_point))

    print('-'*40)
def trip_duration_stats(df):
    '''Finds and prints the total trip duration and
        average trip duration in
       hours, minutes, and seconds.
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds .'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))

    print('-'*40)
def popular_trip_stats(df):
    '''Finds and prints the most popular trip.

    '''
    popular_trip = df['total_trip'].mode().to_string(index = False)
    '''  total_trip' column is created in the mean() function.
    '''
    print('Popular trip is {}.'.format(popular_trip))
    print('-'*40)
def users_stats(df):
    '''Finds and prints the counts of each user type.
    '''
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))
    print('-'*40)
def gender_stats(df):
    '''Finds and prints the counts of gender.
    '''
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Female"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))
    print('-'*40)
def birth_year_stats(df):
    ''' Display earliest, most recent, and most common year of birth
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    most_common = int(df['birth_year'].mode())
    print('The earliest (oldest) users are born in {}.\nThe recent(youngest) users are born in {}.'
          '\nThe most common birth year is {}.'.format(earliest, latest, most_common))
    print('-'*40)
def display_stats(df):
    '''in this function we displays twenty five lines of data if the user specifies that
        they would like to.After displaying twenty five lines,
        ask the user if they would like to see twenty five more,
        continuing asking until they say stop.
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 25
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry,Please choose correct type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'total_trip' column created in mean()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry,Please choose correct type 'yes' or"
                          " 'no'.")
            if display_more.lower() == 'yes':
                head += 25
                tail += 25
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break
    print('-'*40)
def main():
    '''Calculates and prints functions about a city and
    time period specified by the user via input .

    '''
    start_time = 0
    # Filter by city (Chicago, New York, Washington)
    city = select_city_data()
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])

    # change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels

    # increases the column width so that the long strings in the 'total_trip'
    # column can be displayed fully
    pd.set_option('max_colwidth', 100)

    # creates a 'total_trip' column that concatenates 'start_station' with
    # 'end_station' for the use popular_trip_stats() function
    df['total_trip'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, none)
    time_period = select_time_period()
    if time_period == 'none':
        df_filtered = df
    elif time_period == 'month' or time_period == 'day':
        if time_period == 'month':
            filter_lower, filter_upper = select_month()
        elif time_period == 'day':
            filter_lower,filter_upper = select_day()
        print('Filtering data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
        print('\nCalculating the common months...')

    if time_period == 'none':
        start_time = time.time()

        # What is the most common month for start time?
        popular_month(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the common day of week...")

    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

    # What is the most common day of week (Monday, Tuesday, etc.) for start time?
    popular_day(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the most common hour for start time...")
    start_time = time.time()

    # What is the most common hour of day for start time?
    popular_hour(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the tota trip & average trip duration...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration_stats(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the most common start & end station...")
    start_time = time.time()

    # What is the most common start station and most common end station?
    stations_stats(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the most common trip ...")
    start_time = time.time()

    # What is the most common trip?
    popular_trip_stats(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the counts of user types....")
    start_time = time.time()

    # What are the counts of each user type?
    users_stats(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        #we take both city data because washington don't have gender column
        print("\nCalculating the counts of genders...")
        start_time = time.time()

        # tota the counts of gender
        gender_stats(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the birth year...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest
        # user), and most popular birth years?
        birth_year_stats(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))

    # Display twenty five lines of data at a time if user specifies that they would like to
    display_stats(df_filtered)

    # Restart?
    restart = input('\nWould you like to restart? Enter \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please Enter 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Enter \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()
