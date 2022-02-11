"""
InfoSec, Python Programming beginner (version, 3.9+) Data proccessing.

This code might now tbe the most user friendly, but it sure is quite effiencent and scalable.

Date Creation: 2021-06-05
Author: Christopher Ek (chrome91)
Estimated Work Time: 2 hours (Took a while to figure out classes on python from C#)
"""

# Data proccessing.
import os
from datetime import datetime
from collections import defaultdict

# Creates a simple dict for scalablility. This is where you enter 
exts = {'.horse', '.katt'}
grouped_files = defaultdict(int)
cat_list = []
horse_list = []
combined_list = []

# These two classes are created as object storage.
# We use this method to easily access variables insides the objects.


class Horse:

    def __init__(self, name, weight, height, date):
        self.name = name
        self.weight = weight
        self.height = height
        self.date = date


class Cat:

    def __init__(self, name, weight, height, date):
        self.name = name
        self.weight = weight
        self.height = height
        self.date = date


def weight_height_score(lists):
    total_weight_score = 0
    avg_weigth_score = 0
    total_height_score = 0
    avg_height_score = 0
    enteries = 0

    least_height = 99999999999
    most_height = 0
    for i in lists:
        # print(i.weight)
        total_weight_score += int(i.weight)
        total_height_score += int(i.height)
        enteries += 1
        if int(i.height) > most_height:
            most_height = int(i.height)
        else:
            print("Debugging.")

        if int(i.height) < least_height:
            least_height = int(i.height)
            # print(least_height)

    avg_weight_score = total_weight_score / enteries
    avg_height_score = total_height_score / enteries

    return avg_weight_score, avg_height_score, least_height, most_height


def date_sort(lists):
    date_sorted = []
    # Creating a new list with the date only.
    for i in lists:
        date_sorted.append(i.date)

    date_sorted.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d'))
    return date_sorted


def name_matching(name):
    for i in cat_list:
        if name == i.name:
            print(i.weight)

    for i in horse_list:
        if name == i.name:
            print(i.weight)


def main():

    for f in os.listdir("."):
        name, ext = os.path.splitext(os.path.join(".", f))
        # print(f)
        if ext in exts:
            grouped_files[name] += 1

    for name in grouped_files:
        # print(grouped_files[name])
        if grouped_files[name] == len(exts):
            with open('{}.katt'.format(name)) as katt_file,\
                    open('{}.horse'.format(name)) as horse_file:

                # We use these to store information that we later input into object.
                temp_storage = []
                count = 0
                # process files
                for i in katt_file:
                    try:
                        i2 = i.replace("\n", "")
                        # print(i2)
                        temp_storage.append(i2)
                        count += 1
                    except Exception as e:
                        print("Incorrect file formating. \n", e)

                if count == 4:
                    cat_list.append(Cat(temp_storage[0],
                                        temp_storage[1],
                                        temp_storage[2],
                                        temp_storage[3]))
                    combined_list.append(Cat(temp_storage[0],
                                             temp_storage[1],
                                             temp_storage[2],
                                             temp_storage[3]))
                    temp_storage.clear()
                    count = 0
                else:
                    print("Incorrect file formating 13. \n")

                # Handling for horse files. Could create def for optimziation
                for i in horse_file:
                    try:
                        i2 = i.replace("\n", "")
                        temp_storage.append(i2)
                        count += 1
                    except Exception as e:
                        print("Incorrect file formating. \n", e)

                if count == 4:
                    horse_list.append(Horse(temp_storage[0],
                                            temp_storage[1],
                                            temp_storage[2],
                                            temp_storage[3]))
                    combined_list.append(Cat(temp_storage[0],
                                             temp_storage[1],
                                             temp_storage[2],
                                             temp_storage[3]))
                    temp_storage.clear()
                    count = 0
                else:
                    print("Incorrect file formating 133. \n")

    try:
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
