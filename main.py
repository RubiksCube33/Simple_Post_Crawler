import post_crawler as pc
import os
import time
#import pywinmacro as pw
import inputfile_making as filemaking
import pandas as pd

feed_csv = "feed.csv"
out_dir = "output_without_masking"

if out_dir not in os.listdir():
    os.mkdir(out_dir)

receiver_name = ""
csv = filemaking.fileopen()

print("작업을 시작하려면 1을 입력하세요.")
start = input()

if(start != "1"):
    exit("프로그램을 종료합니다.")
else:print("변환을 시작합니다.")

done_list = []
temp = os.listdir(out_dir)

crawler = pc.crawler()

for el in temp:
    if ".png" in el:
        done_list.append(el)

for line in csv:
    line_split = line.strip().split(",")
    if len(line_split) != 2:
        continue

    querry = line_split[0].strip()
    key2 = line_split[1].strip()
    receiver_name = key2
    if len(key2) < 2:
        continue
    key2 = key2[1]
    key1 = "구"
    if len(key2) != 1:
        continue

    if "-" in querry:
        splt = querry.split("-")
        querry = ""
        for el in splt:
            querry = querry + el

    if len(querry) != 13 or not querry.isdigit():
        print("등기번호가 13자리가 아닙니다. 등기번호 오류")
        print("오류 등기번호 및 수신인: ",querry,",",receiver_name)
        continue

    crawler.save_screenshot_withhout_masking(querry, out_dir, key1, key2, receiver_name)
    print("변환 중 : ",querry,",",receiver_name)

print("변환이 끝났습니다.")
crawler.kill()
