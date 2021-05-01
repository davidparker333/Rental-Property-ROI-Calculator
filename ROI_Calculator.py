import tkinter as tk
from PIL import ImageTk, Image


#########################################
##### Class Definitions & Functions #####
#########################################

class Property():

    def __init__(self):
        self.property_value = 0
        self.annualcost = 0
        self.annualprofit = 0
        self.total_investment = 0

    def step1(self):
        #pack values from entry fields
        this_property.Income.rent = rental_var.get()
        this_property.Income.laundry = laundry_var.get()
        this_property.Income.storage = storage_var.get()
        this_property.Income.misc = misc_var.get()
        this_property.Expenses.tax = tax_var.get()
        this_property.Expenses.insurance = insurance_var.get()
        this_property.Expenses.utilities = utilities_var.get()
        this_property.Expenses.hoa = hoa_var.get()
        this_property.Expenses.lawncare = lawn_var.get()
        this_property.Expenses.vacancy = vacancy_var.get()
        this_property.Expenses.repairs = repairs_var.get()
        this_property.Expenses.capex = capex_var.get()
        this_property.Expenses.pm = pm_var.get()
        this_property.Expenses.mortgage = mortgage_var.get()

        #calculate monthly income and expense
        this_property.Income.monthly_income = this_property.Cashflow.sum_income(this_property.Income.rent, this_property.Income.laundry, this_property.Income.storage, this_property.Income.misc)
        this_property.Expenses.monthly_expense = this_property.Expenses.sum_expense(this_property.Expenses.tax, this_property.Expenses.insurance, this_property.Expenses.utilities, this_property.Expenses.hoa, this_property.Expenses.lawncare, this_property.Expenses.vacancy, this_property.Expenses.repairs, this_property.Expenses.capex, this_property.Expenses.pm, this_property.Expenses.mortgage)

        #determine monthly cashflow and update the widget
        this_property.Cashflow.monthly_cashflow = this_property.Cashflow.find_monthly_cashflow(this_property.Income.monthly_income, this_property.Expenses.monthly_expense)
        label_cashflow_result["text"] = "Your cash flow is: $" + str(this_property.Cashflow.monthly_cashflow) + " / month"

        #determine annual values and pack them
        this_property.Income.annual_income = this_property.Income.find_annual_income(this_property.Income.monthly_income)
        this_property.Expenses.annual_cost = this_property.Expenses.find_annual_cost(this_property.Expenses.monthly_expense)
        this_property.Cashflow.annual_cashflow = this_property.Cashflow.find_annual_cashflow(this_property.Cashflow.monthly_cashflow)


    def step2(self):
        #pack values from entry fields
        this_property.ROI.dwnpay = dwnpay_var.get()
        this_property.ROI.closingcost = closingcost_var.get()
        this_property.ROI.repaircost = repaircost_var.get()
        this_property.ROI.misccost = misccost_var.get()

        #calculate total investment
        this_property.Expenses.total_investment = this_property.Expenses.find_total_investment(this_property.ROI.dwnpay, this_property.ROI.closingcost, this_property.ROI.repaircost, this_property.ROI.misccost)

        #calculate ROI
        this_property.ROI.roi = this_property.ROI.find_roi(this_property.Cashflow.annual_cashflow, this_property.Expenses.total_investment)

        #update annual profit label
        label_annualprofit["text"] = "Your annual profit is: $" + str(this_property.Cashflow.annual_cashflow)

        #update the roi label
        label_roi["text"] = "Your cash on cash ROI is: " + str(this_property.ROI.roi) + "%"


    def reset(self):
        #clear the the things and reinstantiate classes
        this_property = Property()
        income = this_property.Income()
        expenses = this_property.Expenses()
        cashflow = this_property.Cashflow()
        roi = this_property.ROI()
        entry_rental.delete(0, tk.END)
        entry_laundry.delete(0, tk.END)
        entry_storage.delete(0, tk.END)
        entry_misc.delete(0, tk.END)
        entry_tax.delete(0, tk.END)
        entry_insurance.delete(0, tk.END)
        entry_utilities.delete(0, tk.END)
        entry_hoa.delete(0, tk.END)
        entry_lawn.delete(0, tk.END)
        entry_vacancy.delete(0, tk.END)
        entry_repairs.delete(0, tk.END)
        entry_capex.delete(0, tk.END)
        entry_propmaintenance.delete(0, tk.END)
        entry_mortgage.delete(0, tk.END)
        entry_dwnpay.delete(0, tk.END)
        entry_closingcost.delete(0, tk.END)
        entry_repaircost.delete(0, tk.END)
        entry_misccost.delete(0, tk.END)
        label_cashflow_result["text"] = "Your cash flow is:"
        label_annualprofit["text"] = "Your annual profit is:"
        label_roi["text"] = "Your cash on cash ROI is:"

    class Income():

        def __init__(self):
            self.rent = 0
            self.storage = 0
            self.laundry = 0
            self.misc = 0
            self.annual_income = 0
            self.monthly_income = 0

        def find_annual_income(income):
            return income * 12
    
    class Expenses():

        def __init__(self):
            self.tax = 0
            self.insurance = 0
            self.utilities = 0
            self.hoa = 0
            self.lawncare = 0
            self.vacancy = 0
            self.repairs = 0
            self.capex = 0
            self.pm = 0
            self.mortgage = 0
            self.annual_cost = 0
            self.total_investment = 0
            self.monthly_expense = 0

        def find_annual_cost(cost):
            return cost * 12

        def find_total_investment(dwnpay, closingcost, repaircost, misccost):
            group = [dwnpay, closingcost, repaircost, misccost]
            for i in range(len(group)):
                if group[i] == "":
                    group[i] = 0
            return float(group[0]) + float(group[1]) + float(group[2]) + float(group[3])

        def sum_expense(tax, insurance, utilities, hoa, lawncare, vacancy, repairs, capex, pm, mortgage):
            group = [tax, insurance, utilities, hoa, lawncare, vacancy, repairs, capex, pm, mortgage]
            for i in range(len(group)):
                if group[i] == "":
                    group[i] = 0
            return float(group[0]) + float(group[1]) + float(group[2]) + float(group[3]) + float(group[4]) + float(group[5]) + float(group[6]) + float(group[7]) + float(group[8]) + float(group[9])

    class Cashflow():

        def __init__(self):
            self.monthly_cashflow = 0
            self.annual_cashflow = 0

        def find_monthly_cashflow(income, expenses):
            return income - expenses

        def find_annual_cashflow(cashflow):
            return cashflow * 12

        def sum_income(rent, laundry, storage, misc):
            group = [rent, laundry, storage, misc]
            for i in range(len(group)):
                if group[i] == "":
                    group[i] = 0
            return float(group[0]) + float(group[1]) + float(group[2]) + float(group[3])

    class ROI():

        def __init__(self):
            self.dwnpay = 0
            self.closingcost = 0
            self.repaircost = 0
            self.misccost = 0
            self.roi = 0

        def find_roi(profit, investment):
            if profit != 0 and investment !=0:
                roi = profit / investment
                roi = round(roi, 2)
                return roi




#########################################
############## Window Control ###########
#########################################

window = tk.Tk()
window.geometry("700x865")
window.title("ROI Calculator")


#########################################
############## Instantiate Class ########
#########################################

this_property = Property()
income = this_property.Income()
expenses = this_property.Expenses()
cashflow = this_property.Cashflow()
roi = this_property.ROI()


#########################################
############## Declare Vars #############
#########################################

rental_var = tk.StringVar()
laundry_var = tk.StringVar()
storage_var = tk.StringVar()
misc_var = tk.StringVar()
tax_var = tk.StringVar()
insurance_var = tk.StringVar()
utilities_var = tk.StringVar()
hoa_var = tk.StringVar()
lawn_var = tk.StringVar()
vacancy_var = tk.StringVar()
repairs_var = tk.StringVar()
capex_var = tk.StringVar()
pm_var = tk.StringVar()
mortgage_var = tk.StringVar()
dwnpay_var = tk.StringVar()
closingcost_var = tk.StringVar()
repaircost_var = tk.StringVar()
misccost_var = tk.StringVar()

#########################################
############## Banner Image #############
#########################################

img = Image.open("Images/banner.png")
banner = ImageTk.PhotoImage(img)
banner_label = tk.Label(image=banner)
banner_label.grid(row = 0, column = 0, columnspan = 2)

#########################################
############## Income Section ###########
#########################################

heading_income = tk.Label(
    text="Income:"
)

label_rental = tk.Label(
    text="Enter rent $ / month:"
)

label_laundry = tk.Label(
    text="Enter laundy $ / month:"
)

label_storage = tk.Label(
    text="Enter storage $ / month:"
)

label_misc = tk.Label(
    text="Enter misc $ / month:"
)

entry_rental = tk.Entry(
    textvariable = rental_var
)

entry_laundry = tk.Entry(
    textvariable = laundry_var
)

entry_storage = tk.Entry(
    textvariable = storage_var
)

entry_misc = tk.Entry(
    textvariable = misc_var
)

heading_income.grid(row = 1, column = 0, sticky="W", pady=20, padx=10)
label_rental.grid(row=2, column = 0, sticky="W", pady=5, padx=25)
label_laundry.grid(row=3, column = 0, sticky="W", pady=5, padx=25)
label_storage.grid(row=2, column = 1, sticky="W", pady=5, padx=25)
label_misc.grid(row=3, column = 1, sticky="W", pady=5, padx=25)
entry_rental.grid(row=2, column = 0, sticky="E", pady=5, padx=25)
entry_laundry.grid(row=3, column = 0, sticky="E", pady=5, padx=25)
entry_storage.grid(row=2, column = 1, sticky="E", pady=5, padx=25)
entry_misc.grid(row=3, column = 1, sticky="E", pady=5, padx=25)


#########################################
############## Expenses Section #########
#########################################

heading_expenses = tk.Label(
    text="Expenses:"
)

label_tax = tk.Label(
    text="Enter tax $ / month:"
)

label_insurance = tk.Label(
    text="Enter insurance $ / month:"
)

label_utilities = tk.Label(
    text="Enter utilities $ / month:"
)

label_hoa = tk.Label(
    text="Enter HOA $ / month:"
)

label_lawn = tk.Label(
    text="Enter lawn care $ / month:"
)

label_vacancy = tk.Label(
    text="Enter vacancy $ / month:"
)

label_repairs = tk.Label(
    text="Enter repairs $ / month:"
)

label_capex = tk.Label(
    text="Enter capital expenditure $ / month:"
)

label_propmaintenance = tk.Label(
    text="Enter property maintenance $ / month:"
)

label_mortgage = tk.Label(
    text="Enter mortgage $ / month:"
)

entry_tax = tk.Entry(
    textvariable = tax_var
)

entry_insurance = tk.Entry(
    textvariable = insurance_var
)

entry_utilities = tk.Entry(
    textvariable = utilities_var
)

entry_hoa = tk.Entry(
    textvariable = hoa_var
)

entry_lawn = tk.Entry(
    textvariable = lawn_var
)

entry_vacancy = tk.Entry(
    textvariable = vacancy_var
)

entry_repairs = tk.Entry(
    textvariable = repairs_var
)

entry_capex = tk.Entry(
    textvariable = capex_var
)

entry_propmaintenance = tk.Entry(
    textvariable = pm_var
)

entry_mortgage = tk.Entry(
    textvariable = mortgage_var
)



heading_expenses.grid(row = 4, column = 0, sticky="W", pady=20, padx=10)
label_tax.grid(row=5, column=0, sticky="W", pady=5, padx=25)
label_insurance.grid(row=6, column=0, sticky="W", pady=5, padx=25)
label_utilities.grid(row=7, column=0, sticky="W", pady=5, padx=25)
label_hoa.grid(row=8, column=0, sticky="W", pady=5, padx=25)
label_lawn.grid(row=9, column=0, sticky="W", pady=5, padx=25)
label_vacancy.grid(row=5, column=1, sticky="W", pady=5, padx=25)
label_repairs.grid(row=6, column=1, sticky="W", pady=5, padx=25)
label_capex.grid(row=7, column=1, sticky="W", pady=5, padx=25)
label_propmaintenance.grid(row=8, column=1, sticky="W", pady=5, padx=25)
label_mortgage.grid(row=9, column=1, sticky="W", pady=5, padx=25)
entry_tax.grid(row=5, column=0, sticky="E", pady=5, padx=25)
entry_insurance.grid(row=6, column=0, sticky="E", pady=5, padx=25)
entry_utilities.grid(row=7, column=0, sticky="E", pady=5, padx=25)
entry_hoa.grid(row=8, column=0, sticky="E", pady=5, padx=25)
entry_lawn.grid(row=9, column=0, sticky="E", pady=5, padx=25)
entry_vacancy.grid(row=5, column=1, sticky="E", pady=5, padx=25)
entry_repairs.grid(row=6, column=1, sticky="E", pady=5, padx=25)
entry_capex.grid(row=7, column=1, sticky="E", pady=5, padx=25)
entry_propmaintenance.grid(row=8, column=1, sticky="E", pady=5, padx=25)
entry_mortgage.grid(row=9, column=1, sticky="E", pady=5, padx=25)



#########################################
############## Cash Flow Section ########
#########################################

heading_cashflow = tk.Label(
    text="Cash Flow:"
)

label_cashflow = tk.Label(
    text="Your cash flow is your rental income - your expenses"
)

label_cashflow_result = tk.Label(
    text="Your cash flow is:"
)

btn_calculate_cashflow = tk.Button(
    text="Step 1: Calculate Cash Flow",
    command=this_property.step1
)

heading_cashflow.grid(row = 10, column = 0, sticky="W", pady=20, padx=10)
label_cashflow.grid(row=11, column=0, columnspan=2, sticky="NEWS")
label_cashflow_result.grid(row=12, column=0, columnspan=2, sticky="NEWS")
btn_calculate_cashflow.grid(row=13, column=0, columnspan=2, sticky="NEWS", padx=10, pady=15)


#########################################
############## ROI Section ##############
#########################################

heading_roi = tk.Label(
    text="Cash on cash ROI:"
)

label_dwnpay = tk.Label(
    text="Enter down payment $:"
)

label_closingcost = tk.Label(
    text="Enter closing costs $:"
)

label_repaircost = tk.Label(
    text="Enter repair costs $:"
)

label_misccost = tk.Label(
    text="Enter misc costs $:"
)

entry_dwnpay = tk.Entry(
    textvariable = dwnpay_var
)

entry_closingcost = tk.Entry(
    textvariable = closingcost_var
)

entry_repaircost = tk.Entry(
    textvariable = repaircost_var
)

entry_misccost = tk.Entry(
    textvariable = misccost_var
)

label_annualprofit = tk.Label(
    text="Your annual profit is:"
)

label_roi = tk.Label(
    text="Your cash on cash ROI is:"
)

btn_calculate_roi = tk.Button(
    text="Step 2: Calculate ROI",
    command=this_property.step2
)

btn_reset = tk.Button(
    text="Reset",
    command=this_property.reset
)

heading_roi.grid(row = 14, column = 0, sticky="W", pady=20, padx=10)
label_dwnpay.grid(row=15, column=0, sticky="W", pady=5, padx=25)
label_closingcost.grid(row=16, column=0, sticky="W", pady=5, padx=25)
label_repaircost.grid(row=15, column=1, sticky="W", pady=5, padx=25)
label_misccost.grid(row=16, column=1, sticky="W", pady=5, padx=25)
entry_dwnpay.grid(row=15, column=0, sticky="E", pady=5, padx=25)
entry_closingcost.grid(row=16, column=0, sticky="E", pady=5, padx=25)
entry_repaircost.grid(row=15, column=1, sticky="E", pady=5, padx=25)
entry_misccost.grid(row=16, column=1, sticky="E", pady=5, padx=25)
label_annualprofit.grid(row=17, column=0, sticky="NEWS", pady=10, padx=25)
label_roi.grid(row=17, column=1, sticky="NEWS", pady=10, padx=25)
btn_calculate_roi.grid(row=18, column=0, columnspan=2, sticky="NEWS", padx=10, pady=10)
btn_reset.grid(row=19, column=0, columnspan=2, sticky="NEWS", padx=10, pady=10)



#########################################
############## Main Loop ################
#########################################

window.mainloop()