from calendar import day_abbr, month
from datetime import datetime as dt
import time
from tracemalloc import start
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york.csv',
              'washington': 'washington.csv'}
cities = ['chicago', 'new york', 'washington']




def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # time.sleep(1)
    print('Hello! Let\'s explore some US bikeshare data!')
    time.sleep(2)
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = ['all','sunday', 'monday', 'tuesday',
    'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        city = input(
            "\nWould you like to explore data for Chicago, New York or Washington?\n").lower()
        if city in cities:
            break
        print('Please enter a valid city!')

    while True:
        print('\nPlease choose month between January and June.\n')
        time.sleep(1)
        print('You can also see data for all months should you decide to.')
        time.sleep(2)
        month = input(
                'Please type "all" if you would like to view data for all months or just select a specific month').lower()
        if month in months:
            break
        print('Please enter the month between January and June!')
    while True:
        print('\nPlease enter the day of the week (e.g Sunday,Monday e.t.c).')
        time.sleep(2)
        day = input(
                    '\nYou can also view data for all days of the week.\nPlease type "all" if you would like to view data by all days.\n').lower()
    
        if day in days:
            break
        print('Please enter a valid day!')
        
    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)

    return city, month, day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # Filter by the month should the user decides to
    if month != 'all':
        #Use the index of to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #Filter by month to get the new dataframe
        df = df[(df['month'] == month)]

    # Filter by the day of the week should the user decides to
    if day != 'all':
        
        #Filter by the day of the week to create the new dataframe
        df = df[(df['day_of_week'] == day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    try:
        common_month = df['month'].mode()[0]
    except:
        print('There is no common month for this filter')
    else:
        print(f'The most common month is: {common_month}')
    # display the most common day of week
    try:
        common_day = df['day_of_week'].mode()[0]
    except:
        print('There is no common day of the week')
    else:
        print(f'The most common day of the week is: {common_day}')
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    try:
        common_start_hour = df['hour'].mode()[0]
    except:
        print('There is no common start hour here')
    else:
        print(f'The most common start hour is: {common_start_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        common_start_station = df['Start Station'].mode()[0]
    except:
        print('There is no common start here')
    else:
        print(f'The most commonly used start station is: {common_start_station}')

    # display most commonly used end station
    try:
        common_end_station = df['End Station'].mode()[0]
    except:
        print('There is no common end station here.')
    else:
        print(f'The most commonly used end station is: {common_end_station}')
    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(
        df['End Station'], sep=' to ')
    try:
        start_to_end = df['Start To End'].mode()[0]
    except:
        print('There is no most frequent combination here.')

    else:
        print(f'The most frequent combination of start station and end station trip is : {start_to_end}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    # Format the time in minutes and seconds
    minute, second = divmod(total_travel_time, 60)
    # Format the time in hours and minutes
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # display mean travel time

    try:
        average_trip_duration = round(df['Trip Duration'].mean())
    except ValueError:
        print('Cannot conver float NaN to integer')
    # Format the average_trip_duration in mins and secs
    else:

        mins, sec = divmod(average_trip_duration, 60)
    # If mins is greater than 60 format it in hour
        if mins <= 60:
            print(
            f"\nThe average trip duration is {mins} minutes and {sec} seconds.")
        else:
            hrs, mins = divmod(mins, 60)
            print(
            f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
       

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'The count of user types is: {user_type}')

    # Display counts of gender
    # Not every file has gender column, hence try and except block are used to catch exceptions should they occur
    try:
        gender_counts = df['Gender'].value_counts()

    except:
        print("\nThere is no 'gender' column in this file.")
    else:
        print(f"\nThe type of users by gender is given below:\n\n{gender_counts}")
    
    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        
    except:
        print("There are no birth year details in this file.")
    else:
        print(f"\nThe earliest year of birth: {earliest}")
        print(f'The most recent year of birth: {recent}')
        print(f'The most common year of birth: {common_year}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Function to display the data frame itself as per user request


def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.

    Args:
        param1 (df): The data frame you wish to work with.

    Returns:
        None.
    """
    user_response = ['yes', 'no']
    response = ''
    
    counter = 0
    while response not in user_response:
        print("\nDo you wish to view the raw data?")
        print("Please enter 'yes' or 'no'")
        response = input().lower()
        #the raw data from the df is displayed should the user decides to
        if response == "yes":
            print(df.head())
        elif response not in user_response:
            print("\nPlease enter a valid input")
            print("\nRestarting...\n")

  
    while response == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        response = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if response == "yes":
             print(df[counter:counter+5])
        elif response != "yes":
             break

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
