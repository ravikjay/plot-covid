import sys

# Helper functions for covid.py analysis

# get a pretty formatted name w/o a newline
def print_name(name):
    print("\n{}:\n\t".format(name), end="")

def print_first_last_pcents(arr):
    print(get_pcent(arr[0]), "->", get_pcent(arr[-1]), end="")

# get a number with commas
def get_comma(num):
    return f'{num:,}'

# get a number with percent
def get_pcent(num):
    return "{}%".format(num)

def print_range(name, arr):
    last_elem = arr[-1] if type(arr[-1]) == str else get_comma(arr[-1])
    print_name(name)
    print(arr[0], "->", last_elem)

# pretty print the first & last elements of an array of percentage proportions
def print_pcents(name, arr):
    print_name(name)
    print_first_last_pcents(arr)
    print()

# pretty print an array of moving average percentage proportions
def print_moving_pcents(name, arr, N):
    print_name(name)
    for i in range(0,len(arr),N):
        print_first_last_pcents(arr[i:i+N])
        print(" -> ", end="")
    print()

# pretty print an array of scalar statistics
def print_arr_stat(stat_name, arr):
    print_name(stat_name)
    print(get_comma(sum(arr)))

# calculate the average for the last N days 
def moving_average(data, N):
    cum_sum, moving_averages = [0], []

    for index, val in enumerate(data, 1):
        # cumulative sum == running total
        cum_sum.append(cum_sum[index-1] + val)
        if index >= N:
            # running total as of today - running total from a week ago / 7 days
            # i.e. the average for the last week
            moving_average = (cum_sum[index] - cum_sum[index-N])/N
            moving_averages.append(round(moving_average, 2))
        else:
            moving_averages.append(0)

    return moving_averages
