from tkinter import *
import backend                 #backend script to read dictionary from
 
bookf = Tk()                   #create window 
bookf.wm_title("BOOK-STORE")
 
def get_selected_row(event): 
    global selected_tuple  
    if not list1.curselection():
        return                           
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)   
    Ent1.delete(0, END)
    Ent1.insert(END, selected_tuple[1])
    Ent2.delete(0, END)
    Ent2.insert(END, selected_tuple[3])
    Ent3.delete(0, END)
    Ent3.insert(END, selected_tuple[2])
    Ent4.delete(0, END)
    Ent4.insert(END, selected_tuple[4])
    return (selected_tuple)
 
def view_command():  
    list1.delete(0, END)      
    for row in backend.view():  
        list1.insert(END, row) 
 
def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(),author_text.get(), year_text.get(),isbn_text.get()):
        list1.insert(END, row)
 
def Add_command():
    list1.delete(0, END)
    backend.insert(title_text.get(),author_text.get(), year_text.get(),isbn_text.get())
    list1.insert(title_text.get(),author_text.get(), year_text.get(),isbn_text.get())
                                  
                                    
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def Update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(), year_text.get(),isbn_text.get())
    view_command()
    
    

def Clear_command():
    Ent1.delete(0, END) 
    Ent2.delete(0, END) 
    Ent3.delete(0, END) 
    Ent4.delete(0, END) 

 
 
#Text labels
Label1 = Label(bookf, text = "Title")
Label1.grid(row = 0, column = 0)
Label2 = Label(bookf, text = "Year")
Label2.grid(row = 1, column = 0)
Label3 = Label(bookf, text = "Author")
Label3.grid(row = 0, column = 2)
Label4 = Label(bookf, text = "ISBN")
Label4.grid(row = 1, column = 2)
 
#buttons
but1 = Button(bookf, text = "View All", width = 20, command = view_command)
but1.grid(row = 2, column = 3,)
but2 = Button(bookf, text = "Search Entry", width = 20, command = search_command)
but2.grid(row = 3, column = 3)
but3 = Button(bookf, text = "Add Entry", width = 20, command = Add_command)
but3.grid(row = 4, column = 3)
but4 = Button(bookf, text = "Update Selected", width = 20 ,command = Update_command)
but4.grid(row = 5, column = 3)
but5 = Button(bookf, text = "Delete Selected", width = 20, command = delete_command)
but5.grid(row = 6, column = 3)
but6 = Button(bookf, text = "Close", width = 20 ,command=bookf.destroy)
but6.grid(row = 8, column = 3)
but6 = Button(bookf, text = "Clear_textbox", width = 20 , command=Clear_command )
but6.grid(row = 7, column = 3)
 
#Listbox AND scrollbar
list1 = Listbox(bookf, height = 9, width = 45)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
 
sb1 = Scrollbar(bookf)
sb1.grid(row = 2, column = 2, rowspan = 6)
list1.configure(yscrollcommand = sb1)
sb1.configure(command = list1.yview)
 
list1.bind('<<ListboxSelect>>', get_selected_row)
 
 
#EntryWindows
title_text = StringVar()
Ent1 = Entry(bookf,textvariable = title_text)
Ent1.grid(row = 0, column = 1)
 
year_text = StringVar()
Ent2 = Entry(bookf, textvariable = year_text)
Ent2.grid(row = 1, column = 1)
 
author_text = StringVar()
Ent3 = Entry(bookf, textvariable = author_text)
Ent3.grid(row = 0, column = 3)
 
isbn_text = StringVar()
Ent4 = Entry(bookf,textvariable = isbn_text)
Ent4.grid(row = 1, column = 3)
 
 
 
 
bookf.mainloop()
