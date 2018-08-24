
import requests
import json
import csv
import time

TIME = time.asctime(time.localtime(time.time()))
TIME = TIME.split(" ")
print(TIME)

write_file = open("chen_3_"+TIME[2]+".csv", 'w', newline="")
writer = csv.writer(write_file)
key1 = '8d38fe4408834100ad7fbd9907a64067'
i = 0
info = input('\n我：')
line = []
line.append(info)
while i < 1000:
    url1 = 'http://www.tuling123.com/openapi/api?key='+key1+'&info='+info
    res1 = requests.get(url1)
    res1.encoding = 'utf-8'
    jd1 = json.loads(res1.text)
    print('\nTuling: '+jd1['text'])
    info = jd1['text']
    if i%2 == 0:
        line.append(info)
        if line[0] != line[1]:
            writer.writerow(line)
            line = []
        else:
            print("==============="+line[0])
            info = input("你的回答：")
            line[1] = info
            writer.writerow(line)
            line = []
    else:
        line.append(info)
    i = i+1
