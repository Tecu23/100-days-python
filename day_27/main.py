# Tkinter

import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    new_text = this_input.get()
    my_label.config(text=new_text)
    
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
this_input = tkinter.Entry(width=10)
this_input.pack()
print(this_input.get())


# Place -> Exact Position
# Grid -> Exact Postion in a grid matrix

window.mainloop()
