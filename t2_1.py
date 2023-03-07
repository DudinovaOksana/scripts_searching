import re
import sys


def tttt_in_grabber(tttt, file_path):
    find_line = 'grabber : ntc reply = NTC,0000,0370,'
    pattern = re.compile(find_line + '\d\d\d\d')
    with open(file_path, "r") as file:

        for i in file:
            if find_line in i:
                result = pattern.findall(i)[0]
                tttt_in_line = int(result[-4:])
                if tttt_in_line >= tttt:
                    print(result + " - OK")
                else:
                    print(result + " - ERR")


if __name__ == "__main__":
    tttt_in_grabber(int(sys.argv[1]), sys.argv[2])

