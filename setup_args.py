import argparse

parser = argparse.ArgumentParser(description='Process COVID data & choose one or more graphs to render.')

parser.add_argument('--all_graphs', action="store_true",
                    dest="all_graphs", default=False,
                    help='Show all graphs')

parser.add_argument('--all_death_rates', action='store_true',
                    dest='all_death_rates', default=False,
                    help='Show all deaths confirmed by date')

parser.add_argument('--drc', action='store_true',
                    dest='death_rate_confirmed', default=False,
                    help='Show proportion of deaths over total confirmed cases')

parser.add_argument('--dro', action='store_true',
                    dest='death_rate_over', default=False,
                    help='Show proportion of deaths over total complete (dead/recovered) cases')

parser.add_argument('--drcma', action='store_true',
                    dest='death_rate_confirmed_moving_average', default=False,
                    help='Show the average proportion of deaths over total confirmed cases for the last week')

parser.add_argument('--droma', action='store_true',
                    dest='death_rate_over_moving_average', default=False,
                    help='Show the average proportion of deaths over total complete (dead/recovered) cases for the last week')

parser.add_argument('--deaths_prop', action="store_true",
                    dest="deaths_proportion", default=False,
                    help='Show the proportion of deaths by both total confirmed cases AND concluded (dead/recovered) cases')

parser.add_argument('--all_cases_absolute', action="store_true",
                    dest="all_cases_absolute", default=False,
                    help='Show an absolute breakdown of all cases')

parser.add_argument('--all_cases_scaled', action="store_true",
                    dest="all_cases_scaled", default=False,
                    help='Show a relative breakdown of all cases, scaling them to show the proportion of each outcome')

options = parser.parse_args()
print(options)
