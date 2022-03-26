from tkinter import *
from tkinter import messagebox
import json
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
ingredients = ["flour", "water", "butter", "sugar", "egg", "yeast", "salt", "mustard"]
window = Tk()
window.title("Calculador de panes")
window.config(padx=80, pady=50, bg=YELLOW)
#---------------------------- SAVE RECIPE -------------------
def save_recipe():
    bread = bread_entry.get()
    flour = flour_entry.get()
    water = water_entry.get()
    butter = butter_entry.get()
    sugar = sugar_entry.get()
    egg = egg_entry.get()
    yeast = yeast_entry.get()
    salt = salt_entry.get()
    mustard = mustard_entry.get()
    new_data = {bread: {
        "harina": flour,
        "agua": water,
        "mantequilla": butter,
        "azucar": sugar,
        "huevo": egg,
        "levadura": yeast,
        "sal": salt,
        "mostaza": mustard
    }
                }
    if len(flour) < 1 or len(water) < 1:
        messagebox.showwarning(title="Atención", message="¡Ups! \ncreo que te olvidaste de agregar harina o agua")

    else:
        try:
            with open("breads.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("breads.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("breads.json", "w") as file:
                json.dump(data, file, indent=4)



#----------------------------- SEARCH RECIPE -------------------------

def search_data():
    bread = bread_entry.get()
    try:
        with open("breads.json", "r") as file:
            data = json.load(file)
            for info in [data]:
                bread_info = info[bread]
                harina = bread_info["harina"]
                agua = bread_info["agua"]
                manteca = bread_info["mantequilla"]
                azucar = bread_info["azucar"]
                huevo = bread_info["huevo"]
                levadura = bread_info["levadura"]
                sal = bread_info["sal"]
                mostaza = bread_info["mostaza"]

                messagebox.showinfo(title=f"Receta de: {bread}", message=f"Harina: {harina} gr \nAgua: {agua} gr \n"
                                                         f"Manteca: {manteca} gr \nAzucar: {azucar} gr \n"
                                                         f"Huevo: {huevo} gr \nLevadura: {levadura} gr \n"
                                                         f"Sal: {sal} gr \nMostaza: {mostaza} gr")

    except FileNotFoundError:
        messagebox.showwarning(title="Atención", message="no se encontro el archivo")

    except KeyError:
        add_recipe = messagebox.askyesno(title="Atención", message="No hay registros de este pan. \n"
                                                                   "¿Quieres agregar la receta?")
        if add_recipe:
            num = 3
            num_2 = 3
            for ingredient in ingredients:
                num += 1
                grids = f"{ingredient}_entry.grid(row={num}, column=1, columnspan=2, sticky='W')"
                exec("%s" % grids)
            for ingredient in ingredients:
                num_2 += 1
                grids = f"{ingredient}_label.grid(row={num_2}, column=0, sticky='E')"
                exec("%s" % grids)
            info_label.grid(row=1, column=0, columnspan=2, sticky="N")
            save_button.grid(row=13, column=1, sticky="W")
            bread_label.grid(row=2, column=0, sticky="W")
            bread_entry.grid(row=2, column=1, sticky="W")
            bread_button.grid(row=2, column=2, sticky="W")
            quantity_button.destroy()
            quantity_entry.destroy()
            quantity_label.destroy()



# ---------------------------- CALCULATE ------------------------------- #
def calculate():
    bread = bread_entry.get()
    quantity = int(quantity_entry.get())
    try:
        with open("breads.json", "r") as file:
            data = json.load(file)
            for info in [data]:
                bread_info = info[bread]
                harina = round(bread_info["harina"] * quantity)
                agua = round(bread_info["agua"] * quantity)
                manteca = round(bread_info["mantequilla"] * quantity)
                azucar = round(bread_info["azucar"] * quantity)
                huevo = round(bread_info["huevo"] * quantity)
                levadura = round(bread_info["levadura"] * quantity)
                sal = round(bread_info["sal"] * quantity)
                mostaza = round(bread_info["mostaza"] * quantity)
                messagebox.showinfo(title=bread, message=f"Harina: {harina} \nAgua: {agua} \n"
                                                         f"Manteca: {manteca} \nAzucar: {azucar} \n"
                                                         f"Huevo: {huevo} \nLevadura: {levadura} \n"
                                                         f"Sal: {sal} \nMostaza: {mostaza}")

    except FileNotFoundError:
        messagebox.showwarning(title="Atención", message="no se encontro el archivo")

    except KeyError:
        messagebox.showwarning(title="Atención", message="No hay registros de ese pan")

#------------------- IMAGEN DE PAN ---------------------------------
canvas = Canvas(width=150, height=150, bg=YELLOW, highlightthickness=0)
bread_img = PhotoImage(file="bread.png")
canvas.create_image(75, 75, image=bread_img)
canvas.grid(row=0, column=1, pady=20)

#------------------------- CLASSIC LABELS ---------------------------
bread_label = Label(text="¿Que pan harás?", font=("arial", 10), bg=YELLOW)
bread_label.grid(row=1, column=0, padx=10)
quantity_label = Label(text="¿Cuantos harás?", font=("arial", 10), bg=YELLOW)
quantity_label.grid(row=3, column=0, padx=10)
space_label = Label(text="", bg=YELLOW)
space_label.grid(row=2, column=1)

# -------------------------- RECIPES LABELS -------------------------
info_label = Label(text="Ingrese los ingredientes de la nueva receta:", font=("arial", 13), bg=YELLOW)
flour_label = Label(text="Harina", font=("arial", 10), bg=YELLOW)
water_label = Label(text="Agua", font=("arial", 10), bg=YELLOW)
butter_label = Label(text="Manteca", font=("arial", 10), bg=YELLOW)
sugar_label = Label(text="Azucar", font=("arial", 10), bg=YELLOW)
egg_label = Label(text="Huevo", font=("arial", 10), bg=YELLOW)
yeast_label = Label(text="Levadura", font=("arial", 10), bg=YELLOW)
salt_label = Label(text="Sal", font=("arial", 10), bg=YELLOW)
mustard_label = Label(text="Mostaza", font=("arial", 10), bg=YELLOW)

#----------------------------  CLASSIC ENTRYS -----------------------
bread_entry = Entry(width=33)
bread_entry.grid(row=1, column=1, columnspan=2, sticky="W")
bread_entry.insert(0, "pan de jamon")
bread_entry.focus()
quantity_entry = Entry(width=33)
quantity_entry.grid(row=3, column=1, columnspan=2, sticky="W")

#---------------------------- RECIPES ENTRYS --------------------
flour_entry = Entry(width=16)
water_entry = Entry(width=16)
butter_entry = Entry(width=16)
sugar_entry = Entry(width=16)
egg_entry = Entry(width=16)
yeast_entry = Entry(width=16)
salt_entry = Entry(width=16)
mustard_entry = Entry(width=16)

#------------------------- BUTTONS ----------------------
bread_button = Button(text="Buscar", width=14, command=search_data)
bread_button.grid(row=1, column=2, sticky="W")
quantity_button = Button(text="Calcular", width=14,command=calculate)
quantity_button.grid(row=3, column=2, columnspan=2, sticky="W")
save_button = Button(text="Guardar", width=13, command=save_recipe)


window.mainloop()

