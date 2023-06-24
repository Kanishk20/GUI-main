from tkinter import *
from tkinter import ttk


window = Tk()
window.title(" PURE GAS SOLVER ")
label = Label(window,text= " PURE GAS SOLVER" , font=('Arial' , 13 , 'bold'))
#label.place(x=0,y=0)
label.pack()

#create a scrollbar for entire window
main_frame = Frame(window)
main_frame.pack(fill=BOTH , expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side = LEFT, fill=BOTH , expand=1)

my_scrollbar = ttk.Scrollbar(main_frame , orient=VERTICAL , command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>' , lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0) , window= second_frame , anchor="nw")






dimensions_of_the_domain = Label(window , text= "Dimensions of the Domain" , font = ('Arial' , 10 , 'bold'))
dimensions_of_the_domain.place(x=0, y =30)

length = Label(window , text="Enter the length" )
length.place(x=0 , y =53)
length_entry = Entry(window)
length_entry.place(x=0 , y=70)

height = Label(window , text="Enter the height" )
height.place(x=150 , y =53)
height_entry = Entry(window)
height_entry.place(x=150 , y=70)

breadth = Label(window , text="Enter the breadth" )
breadth.place(x=300 , y =53)
breadth_entry = Entry(window)
breadth_entry.place(x=300 , y=70)

Grid_dimensions_of_the_domain = Label(window , text= "Grid dimensions of the Domain" , font = ('Arial' , 10 , 'bold'))
Grid_dimensions_of_the_domain.place(x=0, y =120)

Nx = Label(window , text="Nx" )
Nx.place(x=0 , y =143)
Nx_entry = Entry(window)
Nx_entry.place(x=0 , y=170)

Ny = Label(window , text="Ny" )
Ny.place(x=150 , y =143)
Ny_entry = Entry(window)
Ny_entry.place(x=150 , y=170)

Nz = Label(window , text="Nz" )
Nz.place(x=300 , y =143)
Nz_entry = Entry(window)
Nz_entry.place(x=300 , y=170)

Grid_Type = Label(window , text= "Grid Type" , font = ('Arial' , 10 , 'bold'))
Grid_Type.place(x=0, y =240)
Grid_Type_entry = Entry(window)
Grid_Type_entry.place(x=0 , y=267)

vel_top_1 = Label(window , text= "Wall velocity at top surface" , font = ('Arial' , 10 , 'bold'))
vel_top_1.place(x=0, y =350)
vel_top_1_entry = Entry(window)
vel_top_1_entry.place(x=0 , y=377)
vel_top_2_entry = Entry(window)
vel_top_2_entry.place(x=150 , y=377)

vel_bot_1 = Label(window , text= "Wall velocity at bottom surface" , font = ('Arial' , 10 , 'bold'))
vel_bot_1.place(x=0, y =465)
vel_bot_1_entry = Entry(window)
vel_bot_1_entry.place(x=0 , y=497)
vel_bot_2_entry = Entry(window)
vel_bot_2_entry.place(x=150 , y=497)

vel_left_1 = Label(window , text= "Wall velocity at left surface" , font = ('Arial' , 10 , 'bold'))
vel_left_1.place(x=0, y =590)
vel_left_1_entry = Entry(window)
vel_left_1_entry.place(x=0 , y=617)
vel_left_2_entry = Entry(window)
vel_left_2_entry.place(x=150 , y=617)

vel_right_1 = Label(window , text= "Wall velocity at right surface" , font = ('Arial' , 10 , 'bold'))
vel_right_1.place(x=0, y =705)
vel_right_1_entry = Entry(window)
vel_right_1_entry.place(x=0 , y=732)
vel_right_2_entry = Entry(window)
vel_right_2_entry.place(x=150 , y=732)

Domain_voidage = Label(window , text= "Domain Voidage" , font = ('Arial' , 10 , 'bold'))
Domain_voidage.place(x=0, y =810)
Domain_voi_entry = Entry(window)
Domain_voi_entry.place(x=0 , y=837)

Raceway_voidage = Label(window , text= "Raceway Voidage" , font = ('Arial' , 10 , 'bold'))
Raceway_voidage.place(x=0, y =920)
Raceway_voi_entry = Entry(window)
Raceway_voi_entry.place(x=0 , y=947)

label = Label(window,text= " Gas Details " , font=('Arial' , 13 , 'bold'))
label.place(x= 700 , y=40)

#List Box
my_listbox_1 = Listbox(window , selectmode = MULTIPLE)
#my_listbox_1.pack(pady = 15)
my_listbox_1.place(x=4000 , y= 60)

#item in list box
my_list_1 = ["Condition of gas flow(increasing or decreasing)" , "Gas flow rate(in lpm)" , "Density of the gas" , "Viscosity of the gas"]
for item in my_list_1:
    my_listbox_1.insert(END,item)
    my_listbox_1.pack(pady=5)

def select():
    result = ''
    for item in my_listbox_1.curselection():
        result = result + str(my_listbox_1.get(item)) + '\n'
    my_label_1.config(text= result)     

my_button_2 = Button(window , text= "Select" , command=select)
my_button_2.pack(pady = 5)
#my_button_2.place(x=0 , y = 1000)

global my_label_1
my_label_1 = Label(window , text = '')
my_label_1.pack(pady = 5)    

window.mainloop()
