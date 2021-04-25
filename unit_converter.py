from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Unit Converter')
#root.geometry("300x350")

# textvariables for dropdowns menus
base_unit_option = StringVar()
user_input_amount = DoubleVar()
result_output_amount = DoubleVar()
from_unit = StringVar()
to_unit = StringVar()
result_in_text = StringVar()

# metric system for common use
si_prefixes_exponents = {'yotta':10**24, 'zetta':10**21, 'exa':10**18, 'peta':10**15, 'tera':10**12, 
	'giga':10**9, 'mega':10**6, 'kilo':10**3, 'hecto':10**2, 'deca':10**1, '':10**0, 
	'deci':10**-1, 'centi':10**-2, 'milli':10**-3, 'micro':10**-6, 'nano':10**-9, 
	'pico':10**-12, 'femito':10**-15, 'atto':10**-18, 'zepto':10**-21, 'yocto':10**-24,}

# options for units. In case a new unit is added to calculater, update here as well as line 49
base_units_list = ['length', 'data']

# updates prefixes
def update_si_prefixes_exponents(event):
	base_unit = base_unit_option.get()
	global updated_si_prefixes_exponents
	if base_unit == "length":
		updated_si_prefixes_exponents = {}
		for key, value in si_prefixes_exponents.items():
			newKey = key + 'meter'
			updated_si_prefixes_exponents[newKey] = value
		updated_si_prefixes_exponents['feet'] = 0.3048
		updated_si_prefixes_exponents['inch'] = 0.0254

		unitfirst['value'] = list(updated_si_prefixes_exponents.keys())
		unitsecond['value'] = list(updated_si_prefixes_exponents.keys())

	elif base_unit == "data":
		updated_si_prefixes_exponents = {}
		for key, value in si_prefixes_exponents.items():
			newKey = key + "byte"
			updated_si_prefixes_exponents[newKey] = value

		unitfirst['value'] = list(updated_si_prefixes_exponents.keys())
		unitsecond['value'] = list(updated_si_prefixes_exponents.keys())

	# Add elif statement for new base unit. Update base_units_list accordingly line 23

# algoritm does the conversion
def convert_unit():
	amt = user_input_amount.get()
	frm = from_unit.get()
	to = to_unit.get()
	try:
		if not amt or not frm or not to:
			raise ValueError
	except ValueError:
		result_in_text.set("Please check your inputs!")
	else:
		if frm != "":
			amt = amt * updated_si_prefixes_exponents[frm]
			result = amt / updated_si_prefixes_exponents[to]
		else:
			result =  amt / updated_si_prefixes_exponents[to]
		result_in_text.set(result)
		result_output_in_text = str(user_input_amount.get()) + " " + str(from_unit.get()) + "(s) is equal to " + str(result_in_text.get()) + " " + str(to_unit.get()) + "(s)"
		result_in_text.set(result_output_in_text)

# function of reset button
def clear():
	base_unit_option.set("")
	user_input_amount.set("0")
	result_output_amount.set("0")
	from_unit.set("")
	to_unit.set("")
	result_in_text.set("")


head = Label(root, text="Unit Converter", font=('Helvetica', 15))
head.grid(row=0, column=0, columnspan=1)

# userinput the amount 
userinput = Entry(root, textvariable=user_input_amount, font=('Helvetica', 15), width=20)
userinput.grid(row=1, column=0, padx=10, pady=10)

# select base - length or byte
unitbase = ttk.Combobox(root, textvariable=base_unit_option, font=('Helvetica', 10), width=5)
unitbase['value'] = base_units_list
unitbase.grid(row=0, column=1, padx=10, pady=10)
unitbase.bind("<<ComboboxSelected>>", update_si_prefixes_exponents)

# unit convert from
unitfirst = ttk.Combobox(root, textvariable=from_unit, font=('Helvetica', 10), width=10)
unitfirst.grid(row=1, column=1, padx=10, pady=10)

# result int
result = Label(root, textvariable=result_output_amount, font=('Helvetica', 15), width=20)
result.grid(row=2, column=0, padx=10, pady=10)

#result text
resulttext = Label(root, text="", textvariable=result_in_text, font=('Helvetica', 10))
resulttext.grid(row=3, column=0, padx=10, pady=10)

# unit convert to
unitsecond = ttk.Combobox(root, textvariable=to_unit, font=('Helvetica', 10), width=10)
unitsecond.grid(row=2, column=1, padx=10, pady=10)

#submit button
submit = Button(root, text="Submit", font=('Helvetica', 10), command=convert_unit)
submit.grid(row=4, columnspan=2, padx=10, pady=10)

#reset button
reset = Button(root, text="Reset", font=('Helvetica', 10), command=clear)
reset.grid(row=5, columnspan=2, padx=10, pady=10)

root.mainloop()