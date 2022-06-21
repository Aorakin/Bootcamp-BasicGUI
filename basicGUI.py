from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv
#################################

def timestamp (thai=True):
    stamp=datetime.now()
    if thai == True :
        stamp = stamp.replace(year=stamp.year+543)#บวกเป็นพศ
        stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    else : 
        stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')  
    return stamp     




def writetext(quantity,total):
    #stamp = datetime.now()
    #stamp = stamp.replace(year=stamp.year+543)#บวกเป็นพศ
    #stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    stamp = timestamp()
    filename = 'dataa.txt'
    with open (filename,'a',encoding='utf-8') as file:
        file.write (('\n'+'วัน-เวลา:{}ทุเรียน :{}กก. ราคาทั้งหมด{:,.2f}บาท'.format(stamp,quantity,total)))



def writecsv(data):
    #data = ['Time',10,500]
    with open ('data.csv','a',newline='',encoding='utf-8')as file:
        fw = csv.writer(file)#fw = file writer
        fw.writerow(data)
        print('Success')





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


####################################


GUI = Tk()
GUI.geometry('500x300')
GUI.title('โปรแกรมของโอ๊ค')

#file = PhotoImage(file='duriann.png')
#IMG = Label(GUI,image= file,text='')
#IMG.pack()
#บรรทัดพวกนี้ไฟล์รูปใช้ไม่ได้

L1= Label(GUI,text = 'โปรแกรมคำนวณทุเรียน',font= ('Harlow Solid',28,'bold'), fg='blue')
L1.pack() #.place(x,y) , .grid(row=o,column=0)

L2= Label(GUI,text = 'กรุณากรอกจำนวนทุเรียน',font= ('Harlow Solid',20))
L2.pack()

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใข้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()

def Calculate(event=None):
    quantity = v_quantity.get()
    price = 100
    print('จำนวน',float(quantity)*price)
    cal = float(quantity)* price

    # writetext(quantity,cal)
    data = [timestamp(),quantity,cal]
    writecsv(data)
    #EN DATE
    #stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')#เรื่องเวลา

    #THAIDATE
    #stamp = datetime.now()
    #stamp = stamp.replace(year=stamp.year+543)#บวกเป็นพศ
    #stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')

     #encoding=utf-8 ทำให้บันทึกภาษาไทยหรืออื่นๆได้บางโปรแกรม
    
    #popup
    sm = sumdata()
    title = 'ยอดที่ลูกค้าต้องจ่าย'
    text = 'ทุเรียนจำนวน{} กิโลกรัม ราคาทั้งหมด :{:,.2f}บาท'.format(quantity,cal)
    messagebox.showinfo(title,text)
    
    v_quantity.set('')#clear data
    E1.focus()

E1.bind('<Return>',Calculate)



B1 = ttk.Button(GUI ,text ='คำนวณ',command=Calculate)
B1.pack(ipadx = 30 , ipady=20,pady=20)

def SummaryData(event):
    #popup
    sm = sumdata ()
    title = 'ยอดสรุปรวมท้ังหมด'
    text = 'จำนวนที่ขายได้ : {} กก. \n ยอดขาย : {:,.2f}บาท'.format(sm[0],sm[1])
    messagebox.showinfo(title,text)


GUI.bind('<F1>',SummaryData)

E1.focus()#ให้cursor ไปตำแหน่งของe1

GUI.mainloop()