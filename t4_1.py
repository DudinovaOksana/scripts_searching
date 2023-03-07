import re
import sys


def sc_runtime(file_path):
    first_line_pattern = re.compile("info: Slot to run: \d+")
    numbers_pattern = re.compile('\d+')
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)-1):
            first_result = first_line_pattern.search(lines[i])
            if first_result is not None:
                id = re.findall(numbers_pattern, lines[i])[-1]
                second_line_pattern = re.compile(f'info: Slot to run: {id}\n')

                for j in range(i+1, len(lines)):
                    second_result = second_line_pattern.search(lines[j])
                    if second_result is not None:
                        print(f"First line #{i+1}: {lines[i]}Second line #{j+1}: {lines[j]}\n")
                        with open(r'out_4_1.txt', 'a') as file_out:
                            file_out.write(f"First line #{i+1}: {lines[i]}Second line #{j+1}: {lines[j]}\n") #вывод в файл
                        break
                    else:
                        with open(r'out_4_1.txt', 'a') as file_out:
                            file_out.write(f"First line #{i+1}: {lines[i]}Second line not found\n")


if __name__ == "__main__":
    sc_runtime(sys.argv[1])


