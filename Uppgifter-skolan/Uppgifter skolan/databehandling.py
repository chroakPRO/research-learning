"""
InfoSec, Python Programming beginner (version, 3.9+) Data processing.

[*]This code might now tbe the most user friendly, but it sure is quite effiencent and scalable.
[*]The code is not developed for eternal use only internal.
[*]Any function only works with class object that matches with self props.
[*]It is very tailored made and not that open.

Date Creation: 2021-06-05
Author: Christopher Ek (chrome91)
Estimated Work Time: 2 hours (Took a while to figure out classes on python from C#)
"""

# Data processing.
import os
from datetime import datetime
from collections import defaultdict

# Creates a simple dict for scalability. This is where you enter
file_exts = {'.horse', '.katt'}
grouped_files = defaultdict(int)
animal_list = []

# List created for efficiency.
combined_list = []

# These two classes are created as object storage.
# We use this method to easily access variables insides the objects.

class Animal:
    """
    Animal Class.
    """

    def __init__(self, atype, weight, height, date):
        self.atype = type
        self.name = name
        self.weight = weight
        self.height = height
        self.date = date

def weight_height_score(lists):
    """
    Score table.
    :param x: object list of Class Horse or Cat.
    :return: avg_weight_score, avg_height_score, least_height, most_height in a tuple.
    """
    # I am aware that two of these vars are not being used.
    # This is only for future scalability.
    total_weight_score = 0
    avg_weigth_score = 0
    total_height_score = 0
    avg_height_score = 0
    enteries = 0

    # low and upper height vars
    least_height = None
    most_height = 0

    for i in lists:
        # print(i.weight)
        total_weight_score += int(i.weight)
        total_height_score += int(i.height)
        enteries += 1
        if int(i.height) > most_height:
            most_height = int(i.height)
        # Implementation to avoid upper & low bounds.
        if least_height is None:
            least_height = int(i.height)
        elif int(i.height) < least_height:
            least_height = int(i.height)
            # print(least_height)

    # This just creates the average score of both animals or any other provided objects list.
    avg_weight_score = total_weight_score / enteries
    avg_height_score = total_height_score / enteries

    # Returns all the information, some tuple should be created here using (x,y,z,c) vars for read friendly.
    return avg_weight_score, avg_height_score, least_height, most_height


def date_sort(lists):
    """
    Date sorting (Should have coded my own implementation, like quick sort but .sort is fine and fast.)
    :param x: object list of Class Horse or Cat. (Only formarted date with 2021-07-24)
    :return: sorted list:

    """
    date_sorted = []
    # Creating a new list with the date only.
    for i in lists:
        date_sorted.append(i.date)

    # Sorting the dates.
    date_sorted.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d'))
    # Returning list of sorted dates, not any objects.
    return date_sorted


def name_matching(name):
    """
    Name matching,
    :param x: name :datatype: string
    :return: Animal weight.
    """

    for i in animal_list:
        if i.type = "cat":
            if name == i.name:
                print(i.weight)

        if i.type == "horse":
            if name == i.name:
                print(i.weight)
def main():
    """
    Main functionality.
    :param: empty
    :return: None
    """
    # Listing all the directories.
    for f in os.listdir("."):
        # Could use further development. Didnt really have time to focus on the open part.
        if f.endswith(".katt"):
            # print(12)
            with open('{}'.format(f)) as katt_file:
                # Let's read the data and process is.
                data = katt_file.readlines()
                # Essence of OOP is Encapsulation, Polymorphism, Inheritance, Abstraction
                # The part of Abstraction is not me. I do develop more closed in/specific programs.

                animal_list.append(Animal("cat",
                                    data[0],
                                    data[1],
                                    data[2],
                                    data[3]))

        # We taking care of hast files.
        if f.endswith(".hast"):
            with open("{}".format(f)) as horse_file:
                # Data
                data = horse_file.readlines()
                animal_list.append(Animal("horse",
                                        data[0],
                                        data[1],
                                        data[2],
                                        data[3]))

    try:
        # This just printing stuff, super boring and ugly.
        cat_avg_weight_score, cat_avg_height_score, cat_least_height, cat_most_height = weight_height_score(
            cat_list)
        horse_avg_weight_score, horse_avg_height_score, horse_least_height, horse_most_height = weight_height_score(
            horse_list)
        print("\n[*]Average Horse height {}\n[*]Average Horse weight {}\n[*]Average Cat height: {}\n[*]Average Cat weight: {}".format(
            horse_avg_height_score, horse_avg_weight_score, cat_avg_height_score, cat_avg_weight_score))
        print("\n[*]Least Horse height {}\n[*]Most Horse height: {}\n[*]Least Cat height {}\n[*]Most Cat height: {}".format(
            horse_least_height, horse_most_height, cat_least_height, cat_most_height))

        oldest_cat_date = date_sort(cat_list)
        oldest_horse_date = date_sort(horse_list)

        print("\n[*]Oldest Cat Date: {}".format(oldest_cat_date))
        print("[*]Oldest Horse Date: {}".format(oldest_horse_date))
        user_input = input("Please Write Your Name: ")
        for i in combined_list:
            if i.name == user_input:
                print(i.weight)
    except Exception as e:
        print("There is something wrong.")


if __name__ == "__main__":
    main()
