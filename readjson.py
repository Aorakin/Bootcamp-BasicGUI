#readjson

import json

def readjson():
    with open ('data.json',encoding='utf-8')as file:
        data = json.load(file)
        print(type(data))
        print(data[0]['point'])
    return data


def writejson(data):
    jsonobject = json.dumps(data,ensure_ascii=False,indent=4)
    with open ('fruit.json','w',encoding='utf-8')as file :
        file.write(jsonobject)


data =  {'10332240':['Banana',100,5],
        '10332241':['Durian',150,99],
        '10332242':['Apple',200,10],
        '10332243':['แก้วมังกร',300,20] }

writejson(data)