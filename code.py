#importing all the required modules

from chatterbot import ChatBot #import chatterbot library
from chatterbot.trainers import ListTrainer #to train the chatbot
from tkinter import *
import pyttsx3 as pt
import speech_recognition as s
import threading
from PIL import ImageTk,Image



#create mybot object from ChatBot Class
mybot=ChatBot("Stufo")


#providing conversation to chatbot so that it get trained
conversation_demo =[
    'hello Stufo',
    'hello dear!!',
    'what is your name ?',
    'My name is Stufo..',
     'How are you?',
    'I am good..what about you?',
     'I am cool',
     'That is great',
    'what you do?',
    'Stufo is here for your help..Do you have any query?',
    'what is the last date of fees deposition?',
    'It is 15 december..',
    'could you please tell me more about this college?',
    'Arya Group of Colleges Jaipur was established under the aegis of All India Arya Samajis Society for Higher & Technical Education in the year 1999 by the founder chairman Er. Shri T.K. Agarwal, a great visionary, from Roorkee University always believed that engineers builds Nation. In his quest for glory and pride, he established the first private Engineering College in the Rajasthan state. His vision ushered the establishment of over 150 private engineering colleges & his efforts developed the state of Rajasthan into a IT hub of North India.',
    'How many faculties are there in college?',
    'The faculties are very trained in their respective domain and highly skilled.There are about 100 teachers are there in college',
    'when my second midterm exams start?',
    'It is from next week..',
    'Is, there any placement drive next month?',
    'yes, amigoz company will be having there drive..',
     'Thank you',
     'Always Welcome',
     

]



#creating object of ListTrainer Class trainer by providing the reference of bot
trainer = ListTrainer(mybot)

#now we are training the stufobot with the help of trainer object previously created via using train variable
trainer.train(conversation_demo)


#create the window using TK class 
main = Tk()

main.geometry("500x650") #give the size to main window
main.title("StufoBot ") #Give title
main.configure(bg='black') #background color set to black of window


#to put image in window
width = 130
height =130
img = Image.open("bot3.jpg")
img = img.resize((width,height), Image.ANTIALIAS) #resize the photo
photoImg =  ImageTk.PhotoImage(img) #create image object using PhotoImage class

#create Label using Label class and giving it to parent window  and giving image object 
photo = Label(main, image=photoImg)
photo.pack(pady=5)


#crate frame giving main  windows as parent window
frame = Frame(main)

#create scrollbar
sc=Scrollbar(frame) 


#create listbox  and give frame as parent window
#to active scrollbar using yscrollcommand property by giving set reference function
msgs=Listbox(frame, width=80, height=20, yscrollcommand=sc.set)


#now pack these all
sc.pack(side=RIGHT, fill=Y) 
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()



#creating text field and put in main window using font tuple.
textF = Entry(main, font=("Verdana",12))
textF.pack(fill=X , pady=10)



engine = pt.init() #initilize the pyttsx3 module,it returns a pyttsx3.Engine instance store it in engine variable.
voices = engine.getProperty('voices') #returns a list   
engine.setProperty('voice', voices[0].id) #here key is voice and value is id of male voice ,voices[0] will be for male.



#for speaking the word argument  giving to speak function.
def speak(word):
    engine.say(word)
    engine.runAndWait()
    

    
#Take audio as a input from user and convert it into string..
def takeQuery():
    sr=s.Recognizer() #create object sr of Recognizer class 
    sr.pause_threshold = 1 #oause_threshold property by using sr object
    
    print("Stufo is listening to you...Try to speak")
    
    #create object of Microphone class m
    #Take audio via using the system's microphone 
    with s.Microphone() as m:
        try:
            audio=sr.listen(m) #use listen function of sr and pass this audio to it to listen the audio
            
            #query variable will be having user's question  
            query=sr.recognize_google(audio,language='eng-in') #convert your audio or speech into text
            
            #clear the textfiled
            textF.delete(0,END)
            
            #insert the data in textfield also whatever user asking
            textF.insert(0,query)
            
            #now call the function to take response as input
            ask_from_bot()
                
        except Exception as e:
            print(e)
            print("Not Recognized")
        
    
    

#give now above generated 
def ask_from_bot():
    query=textF.get() #taking quering from textfield w
    answer_from_bot = mybot.get_response(query) #take response from bot using get_response
    
    #insert in the msgs in GUI part your query
    msgs.insert(END,"You : "+query)
    
    #insert the the response of bot
    msgs.insert(END, "Stufo : "+str(answer_from_bot))
    
    #now speak the response of bot
    speak(answer_from_bot)
    
    #delete the text in textfield
    textF.delete(0,END)
    
    #to end y view means if the text till ends it will go the till end 
    msgs.yview(END) 
    
    

#create Button and call the funtion ask_from_bot from this function.
btn = Button(main, text="Ask from Stufo", font=("Verdana",12) , command=ask_from_bot)
btn.pack()


#creating a function to press the ask button via program,
def enter_function(event):
    btn.invoke()
    
#going to bind main window with enter key...means if we enter the function will be call
#we are giving funtion reference here only
main.bind('<Return>', enter_function)

def repeatlisten():
    while True:
        takeQuery()


# create a thread and giving function reference in target
#To handle the audio 
t = threading.Thread(target=repeatlisten)

#start the thread
t.start()
main.mainloop()

