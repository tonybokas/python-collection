import csv

test_file = open('C:/Users/anton/Desktop/test_file.csv', 'a', newline='')
test_file_writer = csv.DictWriter(test_file, ['parse_3', 'parse_4'])
test_file_writer.writeheader()
test_file_writer.writerow({'parse_3': 12, 'parse_4': 67})
test_file_writer.writerow({'parse_3': 23, 'parse_4': 78})
test_file_writer.writerow({'parse_3': 34, 'parse_4': 89})
test_file_writer.writerow({'parse_3': 45, 'parse_4': 90})
test_file_writer.writerow({'parse_3': 56, 'parse_4': 1})

test_file_writer_2 = csv.DictWriter(test_file, ['parse_5', 'parse_6'])
test_file_writer_2.writeheader()

test_file.close()