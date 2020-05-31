from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root = Tk()
root.title('Temp_Converter')

########################################################################################################################

def action(*args):
    if (box_val['box1'].get() == "celsius") and (box_val['box2'].get() == 'celsius'):
        return cel_to_cel()
    elif (box_val['box1'].get() == 'celsius') and (box_val['box2'].get() == 'fahrenheit'):
        return cel_to_fah()
    elif (box_val['box1'].get() == 'fahrenheit') and (box_val['box2'].get() == 'celsius'):
        return fah_to_cel()
    else:
        return fah_to_fah()
    """
    try:
        num = box_var.get()
        num = int(num)
    except ValueError:
        m_box.showerror(title='Error', message='Only integer value allowed .....')"""

def cel_to_cel():
    given_temp = int(box_var.get())
    output_box.insert(0,given_temp)
    #output_label.configure(text=f'{given_temp}')

def fah_to_fah():
    given_temp = int(box_var.get())
    output_box.insert(0,given_temp)
    #output_label.configure(text=given_temp)

def cel_to_fah():
    temp = int(box_var.get())
    new_temp = 9 / 5 * temp + 32
    output_box.insert(0,new_temp)
    #output_label.configure(text=f"{new_temp}")

def fah_to_cel():
    temp = int(box_var.get())
    new_temp = (temp - 32) * 5 / 9
    output_box.insert(0,new_temp)
    #output_label.configure(text=f"{new_temp}")

def cls():
    entry_box.delete(0,END)
    output_box.delete(0,END)

#----------------------------------------------------------------------------------------------------------------------#

""" message box """
def  quit():
    ans = askquestion(title='Quit', message='Are you sure ?')
    if ans == 'yes':
        root.destroy()

#----------------------------------------------------------------------------------------------------------------------#

box_val = {'box1': StringVar(), 'box2': StringVar()}

count = 0
for i in box_val:
    combo_box = i+"-input"
    box_val[i] = StringVar()
    combo_box = ttk.Combobox(root, state='readonly', textvariable=box_val[i])
    combo_box['values'] = ("celsius","fahrenheit")
    combo_box.grid(row=count, column=0, padx=5, pady=5)
    count+=1
    combo_box.current(0)

#----------------------------------------------------------------------------------------------------------------------#
""" input box """
box_var = StringVar()
entry_box = ttk.Entry(root, width=5, textvariable=box_var)
entry_box.grid(row=0, column=1, padx=5, pady=5)
entry_box.focus()
entry_box.bind('<Return>',action)

""" output box """
output_var = StringVar()
output_box = ttk.Entry(root, width=5, textvariable=output_var)
output_box.grid(row=1, column=1, padx=5, pady=5)


#----------------------------------------------------------------------------------------------------------------------#

#converter_btn = ttk.Button(root, text="Convert", command=action)
#converter_btn.grid(row=2, columnspan=2, padx=5, pady=5)
clr_btn = ttk.Button(root, text='Clear', command=cls)
clr_btn.grid(row=2, columnspan=2, padx=5, pady=5)

#----------------------------------------------------------------------------------------------------------------------#

""" quit window """
root.protocol("WM_DELETE_WINDOW", quit)

########################################################################################################################

root.mainloop()