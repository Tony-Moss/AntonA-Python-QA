import os
import sys
import csv
import json

usersjson = 'users.json'
bookscsv = 'books.csv'
resultjson = 'result.json'
resultdict = []
books = []


def read_json():
    with open(os.path.join(sys.path[0], usersjson), "r") as openjson:
        return json.load(openjson)


def read_csv():
    with open(os.path.join(sys.path[0], bookscsv), "r") as opencsv:
        reader = csv.reader(opencsv)
        next(reader)
        for row in reader:
            books.append({"title": row[0],
                          "author": row[1],
                          "height": row[3]})


def write_json():
    with open(os.path.join(sys.path[0], resultjson), "w") as combined:
        json.dump(resultdict, combined, indent=4)


read_csv()
for line in read_json():
    resultdict.append({"name": line['name'],
                       "gender": line['gender'],
                       "address": line['address'],
                       "books": books})

write_json()
