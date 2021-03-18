''''
Challenges:

Need to have minimum age at 12 and max age at 130

Completed challenges:
5/03/2021: Fixed the issue where the boxes were the incorrect size. Made it using both frame and grid.

We have to add a popup window that will open when "click me for instructions"

10/3/2021: The buttons used to cattlculate the number of snacks can go into NEGATIVE numbers. Must work on stopping it from going into negative.
FIXED: Buttons have been changed to a click

10/3/2021 Trying to fix the live updating display for the snacks

FIXED: Needed to call on values, then use the text function to display the values of snacks
'''
# ------------------------  Imports  ------------------------------------
import tkinter as tk
import tkinter.font as font
import tkinter.messagebox

# ------------------------  Functions  ------------------------------------
#Buttons for snacks
# 
snack_cost = 0
popcorn_count = 0
mnm_count = 0
pita_chips_count = 0
orange_juice_count = 0
water_count = 0

def age_calculate():
  global age_user
  age_user = int(age.get())

# Snack total adding when clicked
def popcorn_up():
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  global snack_cost
  popcorn_count = popcorn_count + 1
  snack_cost = ((2.5*popcorn_count) + (3*mnm_count) + (4.5*pita_chips_count) + (3.25*orange_juice_count) + (2*water_count))
  updateSnackDisplay()

def mm_up():
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  global snack_cost
  mnm_count = mnm_count + 1
  snack_cost = ((2.5*popcorn_count) + (3*mnm_count) + (4.5*pita_chips_count) + (3.25*orange_juice_count) + (2*water_count))
  updateSnackDisplay()
  

def pitachips_up():
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  global snack_cost
  pita_chips_count = pita_chips_count + 1
  snack_cost = ((2.5*popcorn_count) + (3*mnm_count) + (4.5*pita_chips_count) + (3.25*orange_juice_count) + (2*water_count))
  updateSnackDisplay()

def orange_juice_up():
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  global snack_cost
  orange_juice_count = orange_juice_count + 1
  snack_cost = ((2.5*popcorn_count) + (3*mnm_count) + (4.5*pita_chips_count) + (3.25*orange_juice_count) + (2*water_count))
  updateSnackDisplay()
  
def water_up():
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  global snack_cost
  water_count = water_count + 1
  snack_cost = ((2.5*popcorn_count) + (3*mnm_count) + (4.5*pita_chips_count) + (3.25*orange_juice_count) + (2*water_count))
  updateSnackDisplay()


# Code to reset snack numbers
def reset_all():
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  global snack_cost

  popcorn_count = 0
  mnm_count = 0
  pita_chips_count = 0
  orange_juice_count = 0
  water_count = 0
  snack_cost = 0
  updateSnackDisplay()
# Code to display snack amount
def updateSnackDisplay():
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  global snack_cost

  snacksdisplay['text'] = f"Snacks: Popcorn x {popcorn_count}, M&M's x {mnm_count}, Pita Chips x {pita_chips_count}, Orange Juice x {orange_juice_count}, Water x {water_count}"

  lbl_snackcost['text'] = f"Snack Cost: ${snack_cost}"
  
def get_cost():
  global age_user
  global popcorn_count
  global mnm_count
  global pita_chips_count
  global orange_juice_count
  global water_count
  
  lbl_snackcost['text'] = f"Snack Cost: ${()}"
  

# Message box for instructions
def instructions():
  tk.messagebox.showinfo('Instructions Window','To help with our fundraiser we have decided to make a program to store data of everyone who is joining. 1.Enter first and last name. 2.Enter age. 3.Chose the amount of snacks you want. 4.Chose payment method.')

# Message box for payment method
def credit_card_total():
  tk.messagebox.showinfo('Total pay amount!')

def cash_total():
  tk.messagebox.showinfo('Total pay amount!')

# ------------------------  Main GUI  ------------------------------------
window = tk.Tk(className="Movie Fundraising Program")
window.geometry("500x300")

#Define font
myFont = font.Font(size=10)

#Create button for instructions
button = tk.Button(window,
    text='Click me for instructions',
    bg='#0052cc',
    fg='#ffffff',
    command=instructions)
#Apply font to the button label
button['font'] = myFont
#Add button to gui window
button.grid(column=1, row=0, sticky="nsew")
#Max showed us how to use .grid
#Entry data for entering First name
label = tk.Label(text="First Name")
label['font'] = myFont
label.grid(column=0, row=2, sticky="nsew")

fname = tk.Entry(window)
fname.grid(column=1, row=2, sticky="nsew")
#Entry data fr entering Last name
label2 = tk.Label(text="Last Name")
label2['font'] = myFont
label2.grid(column=0, row=3, sticky="nsew")

lname = tk.Entry(window)
lname.grid(column=1, row=3, sticky="nsew")


#Entry data for entering age
label3 = tk.Label(text="Age")
label3['font'] = myFont
label3.grid(column=0, row=4, sticky="nsew")

age = tk.Entry(window)
age.grid(column=1, row=4, sticky="nsew")

fr_buttons = tk.Frame(master = window)
#Create buttons for amount of snacks that the want
popcorn = tk.Button(text="Popcorn", master=fr_buttons, command=popcorn_up)
popcorn['font'] = myFont
popcorn.grid(column=0, row=0, sticky="nsew")

mnms = tk.Button(text="M&M'S", master=fr_buttons, command=mm_up)
mnms['font'] = myFont
mnms.grid(column=1, row=0, sticky="nsew")

pitachips = tk.Button(text="Pita Chips", master=fr_buttons, command=pitachips_up)
pitachips['font'] = myFont
pitachips.grid(column=2, row=0, sticky="nsew")

orange = tk.Button(text="Orange Juice", master=fr_buttons, command=orange_juice_up)
orange['font'] = myFont
orange.grid(column=0, row=1, sticky="nsew")

water = tk.Button(text="Water", master=fr_buttons, command=water_up)
water['font'] = myFont
water.grid(column=1, row=1, sticky="nsew")

# Reset Button
reset = tk.Button(text="Reset", master=fr_buttons, command=reset_all)
reset['font'] = myFont
reset.grid(column=2, row=1, sticky="nsew")

fr_buttons.grid(column=1, row=5)

snacksdisplay = tk.Label(text=f"Snacks: Popcorn x {popcorn_count}, M&M's x {mnm_count}, Pita Chips x {pita_chips_count}, Orange Juice x {orange_juice_count}, Water x {water_count}")

snacksdisplay.grid(column=1, row =6)

lbl_snackcost = tk.Label(text=f"Snack Cost: ${snack_cost}")
lbl_snackcost.grid(column=1, row=8)


button = tk.Button(window,
    text='Credit Card Payment Total',
    bg='#0052cc',
    fg='#ffffff',
    command=credit_card_total)

button['font'] = myFont
button.grid(column=1, row=9, sticky="nsew")

button = tk.Button(window,
    text='Cash Payment Total',
    bg='#0052cc',
    fg='#ffffff',
    command=cash_total)

button['font'] = myFont
button.grid(column=1, row=10, sticky="nsew")