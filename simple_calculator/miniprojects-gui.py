# # from cProfile import label
# # from tkinter import *
# # from tkinter import IntVar
# # from tkinter.messagebox import showinfo
# #
# # #.....................................traveler form.............................................................
# # r =Tk()
# # def getval():
# #     print('sumbitted')
# #     showinfo('form',f'name:{nameval.get()}, phone:{phoneval.get()} ,gender :{genderval.get() } ,email:{emailval.get()} , payment :{paymentval.get()} , (yes/no):{foodserviceval.get() }')
# #     with open('records.txt','a') as f:
# #         f.write(f'{nameval.get(),phoneval.get(),genderval.get() ,emailval.get() , paymentval.get() ,foodserviceval.get() }')
# #
# #
# # r.title('Travel form')
# # r.geometry('500x350')
# # #label
# # Label(r, text="welcome to osama travels",font='comicsansms 15 bold',pady=20 ,padx=50).grid(row=0,column=3)
# # name = Label(r,text='Name',pady=5)
# # phone = Label(r,text='Phone',pady=5)
# # gender = Label(r,text='Gender',pady=5)
# # email= Label(r,text='Email',pady=5)
# # payment= Label(r,text='Payment Mode',pady=5)
# #
# # name.grid(row=1,column=2)
# # phone.grid(row=2,column=2)
# # gender.grid(row=3,column=2)
# # email.grid(row=4,column=2)
# # payment.grid(row=5,column=2)
# # #var
# # nameval =StringVar()
# # phoneval =StringVar()
# # genderval =StringVar()
# # emailval =StringVar()
# # paymentval =StringVar()
# # foodserviceval =IntVar()
# #
# # #entry
# # nameentry= Entry(r,textvariable=nameval)
# # phoneentry= Entry(r,textvariable=phoneval)
# # genderentry= Entry(r,textvariable=genderval)
# # emailentry= Entry(r,textvariable=emailval)
# # paymententry= Entry(r,textvariable=paymentval)
# #
# # nameentry.grid(row=1,column=3)
# # phoneentry.grid(row=2,column=3)
# # genderentry.grid(row=3,column=3)
# # emailentry.grid(row=4,column=3)
# # paymententry.grid(row=5,column=3)
# #
# # #checkbox
# # foodservice = Checkbutton(text="want to prebook your meals?",variable=foodserviceval)
# # foodservice.grid(row=6,column=3)
# #
# # #button
# # Button(text='submit',command=getval).grid(row=7,column=3)
# #
# # r.mainloop()
#
# #..........................drawing appp....................................
#
# from tkinter import *
# from tkinter import messagebox, IntVar
#
# r = Tk()
# r.geometry('800x700')
# r.title('simple drawing app')
# #canvas
# can= Canvas(r,width=600,height=400,bg='white')
# can.pack(pady=10)
# #shape-width & height
# shw = IntVar(value =100)
# shh =IntVar(value =100)
#
# xposition = IntVar(value =100)
# yposition =IntVar(value =100)
# #width slider
# ws=Scale(r,from_=10 ,to=300,orient='horizontal',label='shape width',variable=shw)
# ws.pack(side='top',pady=5)
# #height slider
# hs=Scale(r,from_=10 ,to=300,orient='horizontal',label='shape height',variable=shh)
# hs.pack(side='top',pady=5)
# #raduibutton -shape
# sh=StringVar(value ='rectangle')
# rb1=Radiobutton(r,text='rectangle',variable=sh,value ='rectangle')
# rb1.pack(side='left',padx=10)
# rb2=Radiobutton(r,text='oval',variable=sh,value ='oval')
# rb2.pack(side='left',padx=10)
#
# #entry foe x,y
# f=Frame(r,bg='white')
# f.pack(pady=10)
# l1=Label(f,text='x position')
# l1.grid(pady=10,row=0,column=0)
# e1=Entry(f,textvariable=xposition,width=5)
# e1.grid(row=0,column=1,padx=5)
#
# l2=Label(f,text='y position')
# l2.grid(pady=10,row=0,column=2)
# e2=Entry(f,textvariable=yposition,width=5)
# e2.grid(row=0,column=3,padx=5)
#
# # Function to draw the selected shape on canvas
# def draw_shape():
#     x =xposition.get()
#     y =yposition.get()
#     shape = sh.get()
#     width = shw.get()
#     height = shh.get()
#
#
#     if shape == "rectangle":
#         can.create_rectangle(x, y, x + width, y + height, fill='blue')
#     elif shape == "oval":
#         can.create_oval(x, y, x + width, y + height, fill='red')
# #button to draw
# b=Button(r, text='Draw',command=draw_shape)
# b.pack(side='top',pady=10)
# # Function to clear the canvas
# def clear_canvas():
#     can.delete("all")
#
# # Function to exit the application
# def exit_app():
#     r.quit()
#
# # Create a menu bar
# menu_bar = Menu(r)
#
# # File Menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Clear Canvas", command=clear_canvas)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=exit_app)
# # Add File menu to the menu bar
# menu_bar.add_cascade(label="File", menu=file_menu)
#
# # Display the menu bar
# r.config(menu=menu_bar)
#
# # Show instructions using a messagebox
# def show_instructions():
#     messagebox.showinfo(
#         "Instructions",
#         "Welcome to the Simple Drawing App!\n\n"
#         "1. Select a shape (Rectangle or Oval).\n"
#         "2. Adjust the shape width and height using the sliders.\n"
#         "3. Set the X and Y position using the input boxes.\n"
#         "4. Click 'Draw' to draw the shape at the specified position.\n"
#         "5. Use the 'File' menu to clear the canvas or exit the app."
#
#     )
#
# # Call this function
# show_instructions()
#
# r.mainloop()
#
