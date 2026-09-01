#Student Anual Acadamics handler for a class

#Importing and path configuration!!!
import pandas as pd
import plotext as plt
import os
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "student_database.txt")
except:
    print("File not found!")

#Class Decalaration!!!
Students= []
class Student:
    def __init__(self,name,roll,behav,attend,mar1,mar2,mar3,mar4):
        self.name= name
        self.roll= roll
        self.behav= behav
        self.attend= attend
        self.mar1= mar1
        self.mar2= mar2
        self.mar3= mar3
        self.mar4= mar4
    def perform(self):
        sum= 0
        Marks=[self.mar1,self.mar2,self.mar3,self.mar4]
        for n in range(4):
            sum+= Marks[n]
        if sum>= 290:
            grad= 'A'
        if sum>= 245 and sum< 290:
            grad= 'B'
        if sum>= 190 and sum< 245:
            grad= 'C'
        if sum>= 140 and sum<190:
            grad= 'D'
        if sum < 140:
            grad= 'Fail'
        self.grade= grad
#Loading Data
def load():
    file = open(file_path, "r")
    cline=0
    for line in file:
        if cline%8 == 0:
            name= str(line.strip())
        if cline%8 ==1:
            roll=int(line.strip())
        if cline%8 ==2:
            behav=str(line.strip())
        if cline%8 ==3:
            attend=int(line.strip())
        if cline%8 ==4:
            mar1=int(line.strip())
        if cline%8 ==5:
            mar2=int(line.strip())
        if cline%8 ==6:
            mar3=int(line.strip())
        if cline%8 ==7:
            mar4=int(line.strip())
            c= Student(name,roll,behav,attend,mar1,mar2,mar3,mar4)
            c.perform()
            Students.append(c)
        cline+=1
    file.close()
#Displaying the table !!!
def Display():
    shw=pd.DataFrame(columns=['Roll','Name','Behaviour','Attend','Mar1','Mar2','Mar3','Mar4','Grade'])
    for i in range(len(Students)):
        shw.loc[i+1]=[Students[i].roll,Students[i].name,Students[i].behav,Students[i].attend,Students[i].mar1,Students[i].mar2,Students[i].mar3,Students[i].mar4,Students[i].grade]
    print(shw)
#Adding records!!!
def add():
    name= input('Name of the Student: ')
    while True:
        try:
            roll= int(input('Roll. no of the Student: '))
            behav= input('Behaviour of the Student: ')
            attend= int(input('Attendence of the Student (in percentage(%)): '))
            mar1= int(input('Marks of 1st Test: '))
            mar2= int(input('Marks of 2nd Test: '))
            mar3= int(input('Marks of 3rd Test: '))
            mar4= int(input('Marks of 4th Test: '))
        except Exception as e:
            print(e)
            continue
        break
        
    c= Student(name,roll,behav,attend,mar1,mar2,mar3,mar4)
    c.perform()
    Students.append(c)
    print('Student Sucessfully Added! ')
#Edit!!!!
def Edit():
    while True:
        try:
            rolln= int(input('Provide the roll. no of that student: '))
            ch= int(input("""What you want to change:
name=> 1|roll.no=> 2|behav=> 3|attend=> 4|
marks 1=> 5|marks 2=> 6|marks 3=> 7|marks 4=> 8
   : """))
        except Exception as e:
            print(e)
            continue
        break
    if len(Students)==0:
        print('Add a Student first!')
    for t in range(len(Students)):
        x= Students[t]
        if x.roll== rolln:
            if ch== 1:
                new= input('New name: ')
                x.name= new
            if ch== 2:
                try:
                    new= int(input('New Roll.no: '))
                except Exception as e:
                    print(e)
                x.roll= new
            if ch== 3:
                new= input('New Behaviour: ')
                x.behav= new
            if ch== 4:
                new= input('New Attendence: ')
                x.attend= new
            if ch== 5:
                try:
                    new= int(input('New marks 1: '))
                except Exception as e:
                    print(e)
                x.mar1= new
            if ch== 6:
                try:
                    new= int(input('New marks 2: '))
                except Exception as e:
                    print(e)
                x.mar2= new
            if ch== 7:
                try:
                    new= int(input('New marks 3: '))
                except Exception as e:
                    print(e)
                x.mar3= new
            if ch== 8:
                try:
                    new= int(input('New marks 4: '))
                except Exception as e:
                    print(e)
                x.mar4= new
            if ch not in range(1,9):
                print('invalid choice!')
            x.perform()
#extract!!!!
def extract():
    while True:
        try:
            rolln= int(input('Provide the roll. no of that student: '))
            ch= int(input("""What you want to know:
name=> 1|roll.no=> 2|behav=> 3|attend=> 4|marks 1=> 5|marks 2=> 6|
marks 3=> 7|marks 4=> 8|grade=> 9|graphical_analysis=> 10
   : """))
        except Exception as e:
            print(e)
            continue
        break
    if len(Students)==0:
        print('Add a Student first!')
    for t in range(len(Students)):
        x= Students[t]
        if x.roll== rolln:
            if ch== 1:
                print(x.name)
            if ch== 2:
                print(x.roll)
            if ch== 3:
                print(x.behav)
            if ch== 4:
                print(x.attend)
            if ch== 5:
                print(x.mar1)
            if ch== 6:
                print(x.mar2)
            if ch== 7:
                print(x.mar3)
            if ch== 8:
                print(x.mar4)
            if ch== 9:
                print(x.grade)
            if ch== 10:
                exgph(x.roll,x.mar1,x.mar2,x.mar3,x.mar4,x.grade)
            if ch not in range(1,11):
                print('invalid choice!')
#Delete Func!!!!
def delete():
    try:
        rolln= int(input('Provide the roll. no of that student: '))
        if len(Students)==0:
            print('Add a Student first!')
        for t in range(len(Students)):
            x= Students[t]
            if x.roll== rolln:
                Students.pop(t)
                print('Deleted Successfully!')
    except Exception as e:
        print(e)
#Debug purpose(Viewing raw data)!!!
def view_raw():
    file= open('student_database.txt','r')
    print(file.read())
    file.close()
#Saving !!!!!
def Save():
    file = open(file_path, "w")
    for ne in range(len(Students)):
        if ne== 0:
            file.write(str(Students[ne].name))
        else:
            file.write('\n'+str(Students[ne].name))
        file.write('\n'+str(Students[ne].roll))
        file.write('\n'+str(Students[ne].behav))
        file.write('\n'+str(Students[ne].attend))
        file.write('\n'+str(Students[ne].mar1))
        file.write('\n'+str(Students[ne].mar2))
        file.write('\n'+str(Students[ne].mar3))
        file.write('\n'+str(Students[ne].mar4))
    print('Saved Successfully')
    file.close()
    exit()
#Comparision !!!!
def cmpr():
	plt.clear_terminal()
	plt.clear_figure()
	plt.clear_data()
	xxis=[' ','Exam-1','Exam-2','Exam-3','Exam-4']
	yxis=[]
	lbls=[]
	for i in range(len(Students)):
		yvl=[0,Students[i].mar1,Students[i].mar2,Students[i].mar3,Students[i].mar4]
		yxis.append(yvl)
		rvl= Students[i].roll
		lbls.append('Roll.'+str(rvl))

	plt.multiple_bar(xxis,yxis, labels= lbls,width= 0.025,fill= True)
	plt.grid(True)
	plt.title('Comparision!')
	plt.show()
#!!!!Graph!!!		
def exgph(roll,m1,m2,m3,m4,gd):
	plt.clear_terminal()
	plt.clear_figure()
	plt.clear_data()
	xxis=['Exam-1','Exam-2','Exam-3','Exam-4']
	yxis= [m1,m2,m3,m4]
	plt.bar(xxis,yxis)
	plt.tiltle='Academic analysis of Roll: '+str(roll)+' ;Grade: '+str(gd)
	plt.show()

#!!! Main Func!!!!
load()       
while True:
    Display()
    try:
        choice=int(input(""" 
What you want to perform: 
add=> 1|change=> 2|extract=> 3
delete=> 4|comparision=> 5|save and exit=> 6
check(For load/save checking....! not for general public use!....)=> 7
  : """)) 
    except Exception as e:
        print(e)
        continue
    if choice== 1:
        add()
    if choice== 2:
        Edit()
    if choice== 3:
        extract()
    if choice== 4:
        delete()
    if choice== 5:
        cmpr()
    if choice==6:
        Save()
    if choice== 7:
        view_raw()
    if choice not in range(1,8):
        print('invalid choice! ')