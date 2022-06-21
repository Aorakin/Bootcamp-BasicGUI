import csv

def writecsv(data):
    #data = ['Time',10,500]
    with open ('data.csv','a',newline='',encoding='utf-8')as file:
        fw = csv.writer(file)#fw = file writer
        fw.writerow(data)
        print('Success')

# d = ['2022-06-14 18:25:40',50,5000]
# writecsv(d)

def readcsv():
    with open('data.csv',newline='',encoding='utf-8')as file :
        fr = csv.reader(file)
        #print(list(fr))
        data=list(fr)
    return data


def sumdata ():
    #ฟังก์ชันใช้รวมค่าที่ได้จากcsvไฟล์สรุปออกมาเป็น2อย่าง
    result = readcsv()
    sumlist_quan = []
    sumlist_total =[]
    for d in result :
        sumlist_quan.append(float(d[1]))
        sumlist_total.append(float(d[2]))
    sumquan = sum(sumlist_quan)
    sumtotal = sum(sumlist_total)

    return (sumquan,sumtotal)

result=sumdata()
print(result)


result = readcsv()
#print(result)


sumlist_quan = []
for d in result :
    sumlist_quan.append(float(d[1]))
print(sumlist_quan,sum(sumlist_quan))

sumquan = sum([float(d[1])  for d in result])
print(sumquan)
