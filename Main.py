from IOOperation import *

def main():

    parser = IOOperation()

    content = parser.read_file("./inputs/testfile.csv")

    to_print = []
    for line in content:
        print(line)
        to_print.append(line)

    parser.write_in_file("example.txt", to_print)


if __name__ == '__main__':
    main()