# library imports
import csv
import sys
import argparse

# my helper file imports
import helper
import setup_args
import colors

# 3rd party imports
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

### TODO
# ask aashna about better names for the argument variables
# ask uma about the kind of data we want to be showing
# what statistical insights should we be aiming to get from the data?
###

file_confirmed = 'time_series_covid19_confirmed_global.csv'
file_deaths = 'time_series_covid19_deaths_global.csv'
file_recovered = 'time_series_covid19_recovered_global.csv'

state_idx = 0
country_idx = 1
lat_idx = 2
lon_idx = 3
first_date_idx = 4

with open(file_confirmed) as csv_file:
    r = list(csv.reader(csv_file))

    # Set up dates index
    dates = [''] * (len(r[0]) - first_date_idx)
    short_dates = [''] * (len(r[0]) - first_date_idx)
    for i in range(first_date_idx, len(r[0])):
        date = r[0][i]
        dates[i-first_date_idx] = date

        short_date = r[0][i][:-3]
        short_dates[i-first_date_idx] = short_date

with open(file_confirmed) as csv_file:
    r = list(csv.reader(csv_file))

    confirmed = [0] * len(dates)

    for row in r[1:]:
        state = row[state_idx]
        country = row[country_idx]

        for i in range(first_date_idx, len(r[0])):
            val = int(row[i])
            confirmed[i-first_date_idx] = confirmed[i-first_date_idx] + val

with open(file_deaths) as csv_file:
    r = list(csv.reader(csv_file))

    deaths = [0] * len(dates)

    for row in r[1:]:
        state = row[state_idx]
        country = row[country_idx]

        for i in range(first_date_idx, len(r[0])):
            val = int(row[i])
            deaths[i-first_date_idx] = deaths[i-first_date_idx] + val

with open(file_recovered) as csv_file:
    r = list(csv.reader(csv_file))

    recovered = [0] * len(dates)

    for row in r[1:]:
        state = row[state_idx]
        country = row[country_idx]

        for i in range(first_date_idx, len(r[0])):
            val = int(row[i])
            recovered[i-first_date_idx] = recovered[i-first_date_idx] + val



print("\nCOVID-19 ANALYSIS\n")
helper.print_range("date range", dates)
helper.print_arr_stat("total confirmed cases", confirmed)
helper.print_arr_stat("total deaths", deaths)
helper.print_arr_stat("total recovered", confirmed)

death_rate_confirmed = [0] * len(confirmed)
death_rate_over = [0] * len(confirmed)
recovery_rate = [0] * len(confirmed)
active_cases = [0] * len(confirmed)


for i in range(len(confirmed)):
    death_rate_confirmed[i] = round((deaths[i] / confirmed[i]) * 100.0, 2)
    death_rate_over[i] = round((deaths[i] / (deaths[i] + recovered[i])) * 100.0, 2)
    recovery_rate[i] = round((recovered[i] / (deaths[i] + recovered[i])) * 100.0, 2)
    active_cases[i] = confirmed[i] - recovered[i] - deaths[i]

helper.print_pcents("[deaths/confirmed] cases change", death_rate_confirmed)
helper.print_pcents("[deaths/completed] cases change", death_rate_over)
helper.print_pcents("[recovered/completed] cases change", recovery_rate)
helper.print_range("active cases change", active_cases)

# track how the death average (curve) flattens after the first 7 days
moving_average_death_rate_confirmed = helper.moving_average(death_rate_confirmed, 7)
moving_average_death_rate_over = helper.moving_average(death_rate_over, 7)

helper.print_moving_pcents("weekly average of [deaths/confirmed] cases change", moving_average_death_rate_confirmed[6:], 7)
helper.print_moving_pcents("weekly average of [deaths/completed] cases change", moving_average_death_rate_over[6:], 7)



####### GRAPHS #######


# proportion of deaths over confirmed cases
# (--drc | --all_death_rates | --all_graphs)
if setup_args.options.death_rate_confirmed or setup_args.options.all_death_rates or setup_args.options.all_graphs:
    drc = pd.DataFrame(dict(Date=short_dates, Percentage=death_rate_confirmed))
    y_label = "% of Deaths / Confirmed"

    tidy_drc = drc.melt(id_vars="Date", value_name=y_label)
    fig = px.bar(tidy_drc, x='Date', y=y_label, labels=['Date', 'Percent'], color='variable', barmode='group')

    fig.update_traces(marker_color=colors.red)
    fig.update_layout(xaxis_tickangle=-45)
    fig.show()


# proportion of deaths over completed (i.e. "over" --> dead/recovered) cases
# (--dro | --all_death_rates | --all_graphs)
if setup_args.options.death_rate_over or setup_args.options.all_death_rates or setup_args.options.all_graphs:
    dro = pd.DataFrame(dict(Date=short_dates, Percentage=death_rate_over))
    y_label = "% of Deaths / (Dead or Recovered)"

    tidy_dro = dro.melt(id_vars="Date", value_name=y_label)
    fig = px.bar(tidy_dro, x='Date', y=y_label, labels=['Date', 'Percent'], color='variable', barmode='group')

    fig.update_traces(marker_color=colors.red)
    fig.update_layout(xaxis_tickangle=-45)
    fig.show()


# average proportion of deaths over confirmed cases for the last week
# (--drcma | --all_death_rates | --all_graphs)
if setup_args.options.death_rate_confirmed_moving_average or setup_args.options.all_death_rates or setup_args.options.all_graphs:
    drcma = pd.DataFrame(dict(Date=short_dates, Weekly_Average_Percentage=moving_average_death_rate_confirmed))
    y_label = "% of Deaths / Confirmed - averaged over last week"

    tidy_drcma = drcma.melt(id_vars="Date", value_name=y_label)
    fig = px.bar(tidy_drcma, x='Date', y=y_label, labels=['Date', 'Percent'], color='variable', barmode='group')

    fig.update_traces(marker_color=colors.orange)
    fig.update_layout(xaxis_tickangle=-45)
    fig.show()


# average proportion of deaths over completed cases for the last week
# (--droma | --all_death_rates | --all_graphs)
if setup_args.options.death_rate_over_moving_average or setup_args.options.all_death_rates or setup_args.options.all_graphs:
    droma = pd.DataFrame(dict(Date=short_dates[7:], Weekly_Average_Percentage=moving_average_death_rate_over[7:]))
    y_label = "% of Deaths / (Dead or Recovered) - averaged over last week"

    tidy_droma = droma.melt(id_vars="Date", value_name=y_label)
    fig = px.bar(tidy_droma, x='Date', y=y_label, labels=['Date', 'Percent'], color='variable', barmode='group')

    fig.update_traces(marker_color=colors.orange)
    fig.update_layout(xaxis_tickangle=-45)
    fig.show()


# Deaths proportionally (--deaths_prop)
if setup_args.options.deaths_proportion or setup_args.options.all_graphs:
    # Deaths (side-by-side)
    fig = go.Figure(data=[
        go.Bar(name="Deaths/Total", x=short_dates, y=death_rate_confirmed, marker_color=colors.purple),
        go.Bar(name="Deaths/Deaths+Recovered", x=short_dates, y=death_rate_over, marker_color=colors.orange),
    ])
    fig.update_layout(
        xaxis_tickangle=-45,
        yaxis=dict(title='%')
    )
    fig.show()

# All cases absolute breakdown (--all_cases_absolute)
if setup_args.options.all_cases_absolute or setup_args.options.all_graphs:
    N = 40
    fig = go.Figure(data=[
        go.Bar(name="Deaths", x=short_dates[N:], y=deaths[N:], marker_color=colors.red),
        go.Bar(name="Recovered", x=short_dates[N:], y=recovered[N:], marker_color=colors.green),
        go.Bar(name="Active", x=short_dates[N:], y=active_cases[N:], marker_color=colors.purple),
        # go.Bar(name="Confirmed", x=short_dates[N:], y=confirmed[N:], marker_color=colors.light_blue),
    ])
    fig.update_layout(
        # barmode='stack',
        xaxis_tickangle=-45,
        yaxis=dict(title='Cases')
    )
    fig.show()

# All cases relative (scaled) breakdown (--all_cases_scaled)
if setup_args.options.all_cases_scaled or setup_args.options.all_graphs:
    fig = go.Figure(data=[
        go.Bar(name="Deaths", x=short_dates, y=[round(deaths[i] / confirmed[i] * 100, 2) for i in range(len(confirmed))], marker_color=colors.red),
        go.Bar(name="Recovered", x=short_dates, y=[round(recovered[i] / confirmed[i] * 100, 2) for i in range(len(confirmed))], marker_color=colors.green),
        go.Bar(name="Active", x=short_dates, y=[round(active_cases[i] / confirmed[i] * 100, 2) for i in range(len(confirmed))], marker_color=colors.purple),
    ])
    fig.update_layout(
        barmode='stack',
        xaxis_tickangle=-45,
        yaxis=dict(title='Proportion of Completed / Total cases')
    )
    fig.show()
