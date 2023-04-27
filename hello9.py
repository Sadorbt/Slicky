next_leap_year = 2024
no_of_leap_years = 20
# the last leap year was in 2020
# function
def is_leap_year(year):
    if year % 4 > 0:
        return False
    else: 
        return True

def print_next_leap_years(next_leap_year, no_of_leap_years):
    no_of_leap_years_found = 0
    while no_of_leap_years_found < no_of_leap_years:
        if is_leap_year(next_leap_year):
            no_of_leap_years_found += 1
            print(next_leap_year)
        next_leap_year += 1
# def print_next_leap_years_repeatly(next_leap_year, no_of_leap_years, no_of_leap_years_found = 0):
#     if is_leap_year(next_leap_year):
#         no_of_leap_years_found += 1
#         print(next_leap_year)
#     if no_of_leap_years_found < no_of_leap_years:
#         print_next_leap_years_repeatly(next_leap_year + 1, no_of_leap_years, no_of_leap_years_found)
print_next_leap_years(next_leap_year, no_of_leap_years)
# print_next_leap_years_repeatly(next_leap_year, no_of_leap_years)