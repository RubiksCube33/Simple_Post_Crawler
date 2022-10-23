import os

def fileopen():
    input_raw_nums = "numbers.txt"
    input_raw_names = "names.txt"

    raw_numbers = open(input_raw_nums)
    raw_names = open(input_raw_names)

    raw_numbers = raw_numbers.readlines()
    raw_names = raw_names.readlines()

    numbers_and_names = []

    if (len(raw_numbers) == len(raw_names)):

        print("\n감지된 등기번호 및 수신자 명단 :\n")
        for i in range(0, len(raw_names)):
            raw_names[i] = raw_names[i][5:]
            raw_names[i] = " ".join(raw_names[i].split())
            numbers_and_names.append(raw_numbers[i].strip('\n') + "," + raw_names[i].strip('\n'))
            print(numbers_and_names[i])

        print("\n총 " + str(len(numbers_and_names)) + "개의 우편 송신 목록이 감지되었습니다.")
        return(numbers_and_names)

    else:
        print("등기번호 갯수와 수령인 수가 일치하지 않습니다.")
        return("0")