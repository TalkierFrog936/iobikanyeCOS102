import tkinter as tk
from tkinter import messagebox

# Global variable to store the total price
total_price = 0

def quantity(item_price):
    quantity_window = tk.Toplevel()
    quantity_window.geometry("600x200")
    quantity_label = tk.Label(quantity_window, text="Please enter the amount of portions:")
    quantity_label.pack()
    quantity_entry = tk.Entry(quantity_window)
    quantity_entry.pack()
    next_button = tk.Button(quantity_window, text="Next", command=lambda: cashout(quantity_entry.get(), item_price))
    next_button.pack()

def cashout(quantity, price):
    global total_price
    total_price += calculate_total_price(int(quantity), price)
    messagebox.showinfo("Item added to cart", "Close this window to continue")
    cashbox = tk.Toplevel()
    cashbox.geometry("300x100")
    message_label = tk.Label(cashbox, text="Do you wish to checkout")
    message_label.pack()
    yes_button = tk.Button(cashbox, text="Yes", command=lambda: yes_option(cashbox,name_entry.get()))
    yes_button.pack()
    no_button = tk.Button(cashbox, text="No", command=lambda: no_option(cashbox))
    no_button.pack()

def no_option(box):
    box.destroy()
    PAUcaf.deiconify()

def yes_option(box,name):
    global total_price
    box.destroy()
    messagebox.showinfo("",f"{name}, the total cost of your food is ₦{total_price}")
    # Reset total price for the next transaction
    total_price = 0

def calculate_total_price(quantity, price):
    total = quantity * price
    if total < 2500:
        total_price = total * (1 - 0.1)
    elif 2500 <= total < 5000:
        total_price = total * (1 - 0.15)
    else:
        total_price = total * (1 - 0.25)
    return total_price

 
def rice_pasta():
    prices=[350,350,350]

    rice=tk.Toplevel()
    rice.geometry("600x200")
   

    pasta=tk.Label(rice,text="Please select your choice:")
    pasta.pack()

    Jollof_Rice=tk.Button(rice,text="Jollof Rice - - - - - - - -  ₦350",command=lambda:quantity(prices[0]))
    Jollof_Rice.pack()
    coco_fried_rice=tk.Button(rice,text="Coconut Fried Rice - - - ₦350",command=lambda:quantity(prices[1]))
    coco_fried_rice.pack()
    jollo_spags=tk.Button(rice,text="Jollof Spaghetti - - - - - -  ₦350",command=lambda:quantity(prices[2]))
    jollo_spags.pack()
    
    return  

def proteins():
    prices=[1100,400,400,500,200,200]

    protein=tk.Toplevel()
    protein.geometry("600x200")
 

    protein1=tk.Label(protein,text="Please select your choice:")
    protein1.pack()

    chilli_chicken=tk.Button(protein,text="Sweet Chili Chicken - - - - - - - -  ₦1100",command=lambda:quantity(prices[0]))
    chilli_chicken.pack()
    Grilled_wings=tk.Button(protein,text="Grilled Chicken Wings - - - - - - - - ₦400",command=lambda:quantity(prices[1]))
    Grilled_wings.pack()
    fried_beef=tk.Button(protein,text="Fried Beef - - - - - - - - - - - - - - - ₦400",command=lambda:quantity(prices[2]))
    fried_beef.pack()
    fried_fish=tk.Button(protein,text="Fried Fish - - - - - - - - - - - - - - - ₦500",command=lambda:quantity(prices[3]))
    fried_fish.pack()
    Boiled_egg=tk.Button(protein,text="Boiled Egg - - - - - - - - - - - - - - - ₦200",command=lambda:quantity(prices[4]))
    Boiled_egg.pack()
    sauteed_sausages=tk.Button(protein,text="Sauteed Sausages - - - - - - - - - ₦200",command=lambda:quantity(prices[5]))
    sauteed_sausages.pack()
    
    return

def side_dishes():
    prices=[350,350,350]

    side=tk.Toplevel()
    side.geometry("600x200")


    dishes=tk.Label(side,text="Please select your choice:")
    dishes.pack()

    Savoury_beans=tk.Button(side,text="Savoury Beans - - - - - - - -  ₦350",command=lambda:quantity(prices[0]))
    Savoury_beans.pack()
    potatoes=tk.Button(side,text="Rosted Sweet Potatoes - - - - - - - ₦300",command=lambda:quantity(prices[1]))
    potatoes.pack()
    fried=tk.Button(side,text="Fried Plantains - - - - - - - - - - -  ₦150",command=lambda:quantity(prices[2]))
    fried.pack()
    salad=tk.Button(side,text="Mixed Vegetable Salad - - - - - - - -  ₦150",command=lambda:quantity(prices[3]))
    salad.pack()
    yam=tk.Button(side,text="Boiled Yam - - - - - - - - - - - - - - - ₦150",command=lambda:quantity(prices[4]))
    yam.pack()

    return

def soups_swallows():
    prices=[100,100,100,450,480]

    soups=tk.Toplevel()
    soups.geometry("600x200")
    

    swallow=tk.Label(soups,text="Please select your choice:")
    swallow.pack()

    eba=tk.Button(soups,text="Eba - - - - - - - - - - - - - - - ₦100",command=lambda:quantity(prices[0]))
    eba.pack()
    poundo=tk.Button(soups,text="Poundo Yam - - - - - - - - - - ₦100",command=lambda:quantity(prices[1]))
    poundo.pack()
    semo=tk.Button(soups,text="Semo - - - - - - - - - - - - - - ₦350",command=lambda:quantity(prices[2]))
    semo.pack()
    Atama=tk.Button(soups,text="Atama Soup - - - - - - - - - -  ₦350",command=lambda:quantity(prices[3]))
    Atama.pack()
    egusi=tk.Button(soups,text="Egusi Soup - - - - - - - - - -  ₦350",command=lambda:quantity(prices[4]))
    egusi.pack()
    
    return

def beverages():
    prices=[200,150,300,350,500,600,350,350,350]

    beverage=tk.Toplevel()
    beverage.geometry("600x200")
    

    drink=tk.Label(beverage,text="Please select your choice:")
    drink.pack()

    water=tk.Button(beverage,text="Water - - - - - - - - - - - - - - -  ₦200",command=lambda:quantity(prices[0]))
    water.pack()
    glass=tk.Button(beverage,text="Glass Drink(35cl) - - - - - - - - -  ₦150",command=lambda:quantity(prices[1]))
    glass.pack()
    Pet=tk.Button(beverage,text="PET Drink(35cl) - - - - - - - - - - -  ₦300",command=lambda:quantity(prices[2]))
    Pet.pack()
    pet=tk.Button(beverage,text="PET Drink(50cl) - - - - - - - - - - -  ₦350",command=lambda:quantity(prices[3]))
    pet.pack()
    malt=tk.Button(beverage,text="Glass/Canned Malt - - - - - - - - - - ₦500",command=lambda:quantity(prices[4]))
    malt.pack()
    yo=tk.Button(beverage,text="Fresh Yo - - - - - - - - - - - - - - -  ₦600",command=lambda:quantity(prices[5]))
    yo.pack()
    pine=tk.Button(beverage,text="Pineapple Juice - - - - - - - - - - - ₦350",command=lambda:quantity(prices[6]))
    pine.pack()
    mango=tk.Button(beverage,text="Mango Juice - - - - - - - - - - - - - ₦350",command=lambda:quantity(prices[7]))
    mango.pack()
    zobo=tk.Button(beverage,text="Zobo Drink - - - - - - - - - - - - - - ₦350",command=lambda:quantity(prices[8]))
    zobo.pack()
    return  

#Main Window    
PAUcaf=tk.Tk()
PAUcaf.title("Welcome to PAU Cafeteria")
PAUcaf.geometry("600x200")

#create menu options
name=tk.Label(PAUcaf,text="Please enter your name")
name.pack()
name_entry=tk.Entry(PAUcaf)
name_entry.pack()

menu=tk.Label(PAUcaf,text="Please select your desired category")
menu.pack()

menu1=tk.Button(PAUcaf,text="RICE/PASTA",command=rice_pasta)
menu1.pack()

menu2=tk.Button(PAUcaf,text="PROTEINS",command=proteins)
menu2.pack()

menu3=tk.Button(PAUcaf,text="SIDE DISHES",command=side_dishes)
menu3.pack()

menu4=tk.Button(PAUcaf,text="SOUPS AND SWALLOWS",command=soups_swallows)
menu4.pack()

menu5=tk.Button(PAUcaf,text="BEVERAGES",command=beverages)
menu5.pack()

PAUcaf.mainloop()