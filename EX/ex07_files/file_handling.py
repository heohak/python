import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.
    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    f = open(filename, "r")
    return f.read()


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    result = []
    with open(filename) as file:
        for line in file.readlines():
            line1 = line.strip()
            result.append(line1)
    return result


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            result.append(row)

    return result


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as f:
        f.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        for word in lines:
            if word == lines[-1]:
                file.write(word)
            else:
                file.write(word + "\n")


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    datelist = read_file_contents_to_list(dates_filename)
    newdatelist = []
    for element in datelist:
        newelement = element.split(":")
        newdatelist.append(newelement)
    townlist = read_file_contents_to_list(towns_filename)
    newtownlist = []
    for element1 in townlist:
        newtowelement = element1.split(":")
        newtownlist.append(newtowelement)

    finalresult = [["name", "town", "date"]]
    name_list = []

    for date in newdatelist:
        if date[0] not in name_list:
            name_list.append(date[0])
            finalresult.append([date[0], "-", date[1]])
    for town in newtownlist:
        if town[0] not in name_list:
            finalresult.append([town[0], town[1], "-"])
        elif town[0] in name_list:
            for e in finalresult:
                for date in newdatelist:
                    if date[0] == town[0] == e[0]:
                        e[1] = town[1]
    write_csv_file(csv_output_filename, finalresult)


if __name__ == '__main__':
    print(merge_dates_and_towns_into_csv("test.txt", "towns.txt", "output.txt"))
