import re
import sys


def sc_device_v(file_path):
    first_line_pattern = re.compile('info: (grabber|wash|tip|reagents) : Sending command: \d+ .*\n')
    numbers_pattern = re.compile(' \d+ ')
    board_pattern = re.compile("(grabber|wash|tip|reagents)")
    with open(file_path, "r") as file:
        lines_first = file.readlines()
        for i in range(len(lines_first)-1):
            first_result = first_line_pattern.search(lines_first[i])
            if first_result is not None:
                board = re.findall(board_pattern, lines_first[i])[0]
                second_id = int(re.findall(numbers_pattern, lines_first[i])[0]) + 1
                second_line_pattern = re.compile(f'info: {board} : Got reply: {second_id} NAK\n')

                for j in range(i+1, len(lines_first)):
                    second_result = second_line_pattern.search(lines_first[j])
                    if second_result is not None:
                        with open(r'out_3_1.txt', 'a') as file_out:
                            file_out.write(f"First line #{i+1}: {lines_first[i]}Second line #{j+1}: {lines_first[j]}\n") #вывод в файл
                        break


if __name__ == "__main__":
    sc_device_v(sys.argv[1])
