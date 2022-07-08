# This week we will work with functions. For this week’s assignment, write a program that uses a function to convert
# miles to kilometers. Your program should prompt the user for the number of miles driven, then call a function which
# converts miles to kilometers. The program should then display the total miles and the kilometers.
road_trip = float((input("\033[1;30;44m Hello fellow Road-Tripper! Please enter your the number of miles you will "
                         "drive below: \n\033[1;30;44m")))


def travel(road_trip):
    km = float(1.60934)
    print(f"\033[1;30;44mYour travel distance is:", "{:.2f}".format(road_trip * km), "kilometers.")


if __name__ == '__main__':
    travel(road_trip)
