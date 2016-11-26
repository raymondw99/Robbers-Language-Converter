from tkinter import *

root = Tk()
root.title("Robber's language translator")
root.geometry('410x250')
root.resizable(width=False, height=False)

#More Information command
def moreinfo():
    messagebox.showinfo("What is Robber's Language?", "Robber's language is a Swedish language game, popularised by author Astrid Lindgren. The principle of this cipher is to take a syllable and double every consonant (spelling matters, not pronunciation) while inserting an 'o' in-between, vowels are left intact.It is therefore possible to render the Rövarspråket version of an English word as well.")
    
#Encoding and decoding mechanism
#From Robber's to regular 
def encode():
    encoded = encodeddisplay.get()
    decoded = ''
    i = 0
    consonant = 'bcdfghjklmnpqrstvwxz'
    while i < len(encoded):
        #If a vowel, let it remain
        if (encoded[i].lower() not in consonant):            
            decoded += encoded[i]
            i += 1
        #If a consonant, remove 'o' and the following consonant 
        else:      
            if  ((i + 2) < len(encoded)) and (encoded[i+1] == 'o') and (encoded[i+2].lower() == encoded[i].lower()):
                decoded += encoded[i]
                i += 3
                decodeddisplay.delete(0, END)
                decodeddisplay.insert(INSERT, decoded)
            else:
                decodeddisplay.delete(0, END)
                decodeddisplay.insert(INSERT, "Error")
                break
            
#From regular to Robber's
def decode():
    consonant = 'bcdfghjklmnpqrstvwxz'
    decoded = decodeddisplay.get()
    robber = ''
    for word in decoded:
    #If a consonant, add 'o' and the consonant afterwards.
    #If a vowel, let it remain
        if word.lower() in consonant:
            robber = robber + word + 'o' + word.lower()
        else:
            robber = robber + word
    encodeddisplay.delete(0, END)
    encodeddisplay.insert(INSERT, robber)           
    return robber

#Clear command
def clear():
    decodeddisplay.delete(0,END)
    encodeddisplay.delete(0,END)
  
#Title
Title = Label(root, text= "Robber's Language Translator", font = ('Avenir', 18, 'normal'))
Title.grid(column = 0, columnspan = 7, padx = 5, pady = 5)

#Entry Boxes
Regular = Label(root, text = "Regular Speech:", font = ('Avenir', 15, 'normal'))
Regular.grid(row = 1, sticky = W, padx = 4)
decodeddisplay = Entry(root)
decodeddisplay.grid(row = 1, column = 1, sticky = E, pady = 0, padx = 0)
Translate1 = Button(root, text = "Translate", command = decode, font = ('Avenir', 15, 'normal'))
Translate1.grid(row = 1, column = 3, sticky = E, pady = 0, padx = 0)

Robber = Label(root, text="Robber's Language:", font = ('Avenir', 15, 'normal'))
Robber.grid(row = 2, sticky = W, padx = 4)
encodeddisplay = Entry(root)
encodeddisplay.grid(row = 2, column = 1, sticky = E, pady = 0, padx = 0)
Translate2 = Button(root, text = "Translate", command = encode, font = ('Avenir', 15, 'normal'))
Translate2.grid(row = 2, column = 3, sticky = E, pady = 0, padx = 0)

#Clear
clear = Button(text = "Clear", command = clear, font = ('Avenir', 15, 'normal'))
clear.grid(row = 3, column = 0, columnspan = 15, padx = 10, pady = 5, sticky =  N+S+E+W)

#More Information Button
Moreinfo = Button(text = "What is Robber's language?", command = moreinfo, font = ('Avenir', 15, 'normal'))
Moreinfo.grid(row = 4, column = 0, columnspan = 15, padx = 10, pady = 5, sticky =  N+S+E+W)
       
#Exit Button
Exit = Button(text = 'Exit', command = root.destroy, font = ('Avenir', 15, 'normal'))
Exit.grid(row = 5, column = 0, columnspan = 15, padx = 10, pady = 5, sticky =  N+S+E+W)

#Credits
Credits = Label(root, text = "Raymond Wang 2016 ®", font = ('Avenir', 15, 'italic'))
Credits.grid(row = 6, column = 0, columnspan = 7, pady = 5, padx = 5)

root.mainloop()
