from textblob import TextBlob
from tkinter import *

def correct_spelling():
    # Get text from enter1
    get_data = enter1.get()
    # Create a TextBlob object
    corr = TextBlob(get_data)
    # Correct the spelling
    data = corr.correct()

    # Clear the contents of enter2
    enter2.delete(0, END)
    # Insert the corrected text into enter2
    enter2.insert(0, data)

def main_window():
    global enter1, enter2 
    win = Tk()
    win.geometry("500x370")
    win.resizable(False, False)
    win.config(bg="red")
    win.title("Gaurav sony")
    
    # Label for "Incorrect Spelling"
    label1 = Label(win, text="Incorrect Spelling", font=("Time New Roman ", 25, "bold"), bg="green", fg="white" )
    label1.place(x=100, y=20, height=50, width=300)

    # Entry widget for entering text
    enter1 = Entry(win, font=("Times New Roman", 20))
    enter1.place(x=50, y=80, height=50, width=400)

    # Label for "Correct Spelling"
    label2 = Label(win, text="Correct Spelling", font=("Time New Roman ", 25, "bold"), bg="green", fg="white" )
    label2.place(x=100, y=140, height=50, width=300)

    # Entry widget for displaying corrected text
    enter2 = Entry(win, font=("Times New Roman", 20))
    enter2.place(x=50, y=200, height=50, width=400)
    
    # Button to trigger spelling correction
    button = Button(win, text="Done", font=("Time New Roman ", 25, "bold"), bg="yellow", command=correct_spelling)
    button.place(x=150, y=280, height=50, width=200)

    win.mainloop()
    
main_window()
