import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    city = input("Please enter chicago, washington, or new york city: ").lower()
    print("You've entered {}.".format(city))


    while city not in cities:
        city = input("Oops! You've entered an invalid response. Please try again: ")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    month = input("Please enter a month between january and june, or all: ").lower()

    while month not in months:
        month = ("You've entered an invalid response. Please try again: ")
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input("Please enter a day of the week, or all: ").lower()

    while day not in days:
        day = ("You've entered an invalid response. Please try again: ")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

        # TO DO: display the most common month


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("The most common month is {}.".format(popular_month))



    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day is {}.".format(popular_day))


        # TO DO: display the most common day of week

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is {}.".format(popular_hour))

        # TO DO: display the most common start hour
    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')


        # TO DO: display most commonly used start station

    common_start_station = df["Start Station"].mode()
    print("The most common start station is {}.".format(common_start_station))
        # TO DO: display most commonly used end station

    common_end_station = df["End Station"].mode()
    print("The most common end station is {}.".format(common_end_station))

        # TO DO: display most frequent combination of start station and end station trip

    df["most_frequent_combo"] = df["Start Station"] + df["End Station"]
    print("The most frequent start and stop startion combination is {}.".format(df['most_frequent_combo'].mode()))

    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')


        # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {}".format(total_travel_time))

        # TO DO: display mean travel time

    average_travel_time = df['Trip Duration'].mean()
    print("Average travel time: {}".format(average_travel_time))

    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types

    user_type_count = df['User Type'].value_counts()
    print('User type count: \n{}'.format(user_type_count))

        # TO DO: Display counts of gender

    try:
        gender_counts = df['Gender'].value_counts()
        print('Gender counts: \n{}'.format(gender_counts))
    except:
        print('Washington does not have gender data.')


        # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_birth_year = df['Birth Year'].min()
        print('The earliest birth year is: {}'.format(int(min_birth_year)))
        max_birth_year = df['Birth Year'].max()
        print('The most recent birth year is: {}'.format(int(max_birth_year)))
        common_birth_year = df['Birth Year'].mode()
        print('The most common birth year is: {}'.format(int(common_birth_year)))
    except:
        print('Washington does not have birth year data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """ Asks user if they'd like to see raw data.
        Prints data 5 rows at a time if yes"""
    i = 0
    raw = input("Would you like to see 5 rows of raw data? Answer yes or no: ").lower()
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5])
            raw = input("\nWould you like to see the next five rows? Answer yes or no: ").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
