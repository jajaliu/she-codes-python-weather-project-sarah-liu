import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    d = datetime.fromisoformat(iso_string)
    date = d.strftime("%A %d %B %Y")

    return date


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    celcius = ((float(temp_in_farenheit)-32)*5)/9

    return round(celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data_int = [float(x) for x in weather_data]
    mean = sum(weather_data_int)/len(weather_data_int)

    return float(mean)



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []

    with open(csv_file) as csv_data:
        reader = csv.reader(csv_data)
        next(csv_data)
        
        for line in reader:
            if line != []:
                data.append([line[0],int(line[1]), int(line[2])])
    
    return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    weather_data_float = [float(x) for x in weather_data]

    if weather_data_float != []:
        min_temp = ()
        for i, temp in enumerate(weather_data_float):
            if (min_temp == ()):
                min_temp = (temp, i)
                continue
            
            if (temp <= min_temp[0]):
                min_temp = (temp, i)

        return min_temp

    else:
        return ()
    


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    weather_data_float = [float(x) for x in weather_data]

    if weather_data_float != []:
        max_temp = ()
        for i, temp in enumerate(weather_data_float):
            if (max_temp == ()):
                max_temp = (temp, i)
                continue
            
            if (temp >= max_temp[0]):
                max_temp = (temp, i)

        return max_temp

    else:
        return ()


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #   5 Day Overview
    #   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
    #   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
    #   The average low this week is 12.2°C.
    #   The average high this week is 17.8°C.
    
    # find title 

    title = f"{len(weather_data)} Day Overview\n"

    # find lowest temperature

    weather_data_min = [min[1] for min in weather_data]
    min_temp_c = convert_f_to_c(find_min(weather_data_min)[0])

   

    min_temp_date = convert_date(weather_data[find_min(weather_data_min)[1]][0])

    lowest_temp_str = f"  The lowest temperature will be {format_temperature(min_temp_c)}, and will occur on {min_temp_date}.\n"

    # find highest temperature

    weather_data_max = [max[2] for max in weather_data]
    max_temp_c = convert_f_to_c(find_max(weather_data_max)[0])
    max_temp_date = convert_date(weather_data[find_max(weather_data_max)[1]][0])

    highest_temp_str = f"  The highest temperature will be {format_temperature(max_temp_c)}, and will occur on {max_temp_date}.\n"

   # find average low

    avg_low = convert_f_to_c(calculate_mean(weather_data_min))

    avg_low_str = f"  The average low this week is {format_temperature(avg_low)}.\n"

    # find average high
    avg_high = convert_f_to_c(calculate_mean(weather_data_max))

    avg_high_str = f"  The average high this week is {format_temperature(avg_high)}.\n"

  
    return title + lowest_temp_str + highest_temp_str + avg_low_str + avg_high_str



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # ---- Friday 02 July 2021 ----
    # Minimum Temperature: 9.4°C
    # Maximum Temperature: 19.4°C

    summary = ""

    for day in weather_data:
        date = convert_date(day[0])
        min_temp = convert_f_to_c(day[1])
        max_temp = convert_f_to_c(day[2])

        summary += f"---- {date} ----\n  Minimum Temperature: {format_temperature(min_temp)}\n  Maximum Temperature: {format_temperature(max_temp)}\n\n"

    return summary