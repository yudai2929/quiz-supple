import csv
test_file = open('files/test.csv')
test_data = csv.reader(test_file)

for row in test_data:
    print(row)
