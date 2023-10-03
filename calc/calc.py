from tkinter import *
import math
from pygame import mixer #pip install pygame
mixer.init()
import speech_recognition #pip install speechrecognition,pyaudio


def click(value):
   # entryField.insert(value)
    ex=entryField.get()
    answer=''

    try:
        if value=='C':
            ex=ex[0:len(ex)-1]
            entryField.delete(0,END)
            entryField.insert(0,ex)
            return 
        elif value=='CE':
            entryField.delete(0,END)
        elif value=='x^(1/2)':
            answer=math.sqrt(eval(ex))#using eval to convert any string datatype to its respective int or float
        elif value=='pie':
            answer=math.p1
        elif value=='cos':
            answer=math.cos(math.radians(eval(ex)))#string to int , int to radians
        elif value=='sin':
            answer=math.sin(math.radians(eval(ex)))#string to int , int to radians
        elif value=='tan':
            answer=math.tan(math.radians(eval(ex)))#string to int , int to radians
        elif value=='2pie':
            answer=2*math.p1
        elif value=='cosh':
            answer=math.cosh(math.radians(eval(ex)))
        elif value=='sinh':
            answer=math.sinh(math.radians(eval(ex)))
        elif value=='tanh':
            answer=math.tanh(math.radians(eval(ex)))    
        elif value=='x^(1/3)':
            answer=eval(ex)**(1/3)
        elif value=='x^y':
            entryField.insert(END,'**')
            return
        elif value=='x^3':
            answer=eval(ex)**(3)
        elif value=='x^2':
            answer=eval(ex)**(2)
        elif value=='deg':
            answer=math.degrees(eval(ex))
        elif value=='rad':
            answer=math.radians(eval(ex))
        elif value=='e':
            answer=math.e
        elif value=='ln':
            answer=math.log10(eval(ex))
        elif value=='x!':
            answer=math.factorial(eval(ex))
        elif value=='/':
            entryField.insert(END,"/")
            return
        elif value=='%':
            answer=(eval(ex))/100
            
        elif value=='=':
            answer=eval(ex)
        else:
            entryField.insert(END,value)
            return                        #if this is not present , control directly goes to next two lines and clear screen
        entryField.delete(0,END)
        entryField.insert(0,answer)
    except:#try n accept for syntax errors like +12+11=23
        pass

def findnumbers(t):
    ld=[]
    for num in t:
        try:
            ld.append(float(num))
        except valueError:
            pass
    return ld

def audio():
    mixer.music.load('music1.opus')
    mixer.music.play()
    sr=speech_recognition.Recognizer()#creating object of sr
    with speech_recognition.Microphone() as m:#creating mic object and also assigning exceptions of unclear voice
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)
            
            mixer.music.load('music2.opus')
            mixer.music.play()
            text_list=text.split('') #separating letters
            for word in text_list:
                if word.upper() in operations.keys():
                    ld=findnumbers(text_list)
                    print(ld)
                    reslt=operations[word.upper()](l[0],l[1])
                    entryField.delete(0,END)
                    entryField.insert(END,reslt)
                else:#this runs when u speak something that wont be in operations
                    pass
                
        except:
            pass
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    l=math.lcm(a,b)
    return l
def hcf(a,b):
    h=math.gcd(a,b)
    return h

oprations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
           'SUBSTRACTION':sub,'DIFFERENCE':sub,'SUBSTRACT':sub,'MINUS':sub,
           'MULTIPLY':mul,'PRODUCT':mul,'MULTIPLICATION':mul,
           'DIVISION':div,'DIVIDE':div,'LCM':lcm,'HCF':hcf,'MOD':mod,'REMAINDER':mod,'MODULUS':mod}


        
    
    
    
    
root = Tk()  #creating window object
root.title('calc')
root.config(bg='#3C4048')
root.geometry('700x486+50+100')#resolution + distance from y + distance from x while opening

logo=PhotoImage(file='calc1.png')
logolabel=Label(root,image=logo,height=50,width=50)#label class
logolabel.grid(row=0,column=0)

micImage=PhotoImage(file='calc1.png')
micbutton=Button(root,image=micImage,height=50,width=50,command=audio)
micbutton.grid(row=0,column=7)

entryField=Entry(root,font=('arial',20,'bold'),bg='white',fg='dodgerblue3',bd=4,relief=SUNKEN,width=10)#creating entry field object
entryField.grid(row=0,column=0,pady=10,padx=30,columnspan=8)#positioning of entryfield

button_text_list =["C","CE","x^(1/2)","+","pie","cos","sin","tan",
                  "1","2","3","-","2pie","cosh","sinh","tanh",
                   "4","5","6","*","x^(1/3)","x^y","x^3","x^2",
                   "7","8","9","+","In","deg","rad","e",
                   ".","0","%","=","log","(",")","x!"]
rowvalue=1
colvalue=0
for variableidhi in button_text_list:
    button=Button(root,width=3,height=-1,bd=1,relief=SUNKEN,text=variableidhi,font=('arial',30),bg='#00ABB3',activebackground='#B2B2B2',command=lambda button=variableidhi:click(button))
    button.grid(row=rowvalue,padx=4,pady=4,column=colvalue)
    colvalue+=1
    if colvalue>7:
         rowvalue+=1
         colvalue=0
root.mainloop()
