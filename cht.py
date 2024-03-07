import tkinter as tk
from tkinter import ttk
import csv
import datetime

class App():
    def __init__(self):
        def get_values():
            customer = self.set_customer.get()
            check_number = self.set_check_number.get()
            amount = self.set_amount.get()
            discount = self.set_discount.get()
            invoices = self.set_invoices.get()

            # Add the values to their respective lists
            customers.append(customer)
            check_numbers.append(check_number)
            amounts.append(amount)
            discounts.append(discount)
            invoices_paid.append(invoices)

            # Clear the entry widgets
            self.set_customer.delete(0, tk.END)
            self.set_check_number.delete(0, tk.END)
            self.set_amount.delete(0, tk.END)
            self.set_discount.delete(0, tk.END)
            self.set_invoices.delete(0, tk.END)

            # Update the labels to display the values
            customer_label.config(text="Customers: " + ", ".join(customers))
            check_number_label.config(text="Check Numbers: " + ", ".join(check_numbers))
            amount_label.config(text="Amounts: " + ", ".join(amounts))
            discount_label.config(text="Discounts: " + ", ".join(discounts))
            invoices_label.config(text="Invoices Paid: " + ", ".join(invoices_paid))

        def save_to_csv():
            with open( "deposits.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Customer", "Check Number", "Amount", "Discount", "Invoices Paid"])
                writer.writerows(zip(customers, check_numbers, amounts, discounts, invoices_paid))

        date = datetime.datetime.now()

        self.root = tk.Tk()
        self.root.geometry('960x540')
        self.root.title('Ahner Industrial Deposits')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Todays Deposit', background='white', font=('Brass Mono', 30))
        self.text.grid(row=0, column=0, pady=10, sticky='NWES')

        self.date = ttk.Label(self.mainframe, text=date.strftime("%x"), background='white', font=('Brass Mono', 12))
        self.date.grid(row=1, column=0, pady=10, sticky='NWES')

        self.customer = ttk.Label(self.mainframe, text='Customer: ', background='white', font=('Brass Mono', 12))
        self.customer.grid(row=2, column=0, pady=10, sticky='NWES')

        self.set_customer = ttk.Entry(self.mainframe)
        self.set_customer.grid(row=2, column=1, pady=10, sticky='NWES')

        self.check_number = ttk.Label(self.mainframe, text='Check Number: ', background='white', font=('Brass Mono', 12))
        self.check_number.grid(row=3, column=0, pady=10, sticky='NWES')

        self.set_check_number = ttk.Entry(self.mainframe)
        self.set_check_number.grid(row=3, column=1, pady=10, sticky='NWES')

        self.amount = ttk.Label(self.mainframe, text='Amount: ', background='white', font=('Brass Mono', 12))
        self.amount.grid(row=4, column=0, pady=10, sticky='NWES')

        self.set_amount = ttk.Entry(self.mainframe)
        self.set_amount.grid(row=4, column=1, pady=10, sticky='NWES')

        self.discount = ttk.Label(self.mainframe, text='Discount?: ', background='white', font=('Brass Mono', 12))
        self.discount.grid(row=5, column=0, pady=10, sticky='NWES')

        self.set_discount = ttk.Entry(self.mainframe)
        self.set_discount.grid(row=5, column=1, pady=10, sticky='NWES')

        self.invoices = ttk.Label(self.mainframe, text='Invoices Paid: ', background='white', font=('Brass Mono', 12))
        self.invoices.grid(row=6, column=0, pady=10, sticky='NWES')

        self.set_invoices = ttk.Entry(self.mainframe)
        self.set_invoices.grid(row=6, column=1, pady=10, sticky='NWES')

        self.submit_button = ttk.Button(self.mainframe, text="Submit", command=get_values)
        self.submit_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.finish_button = ttk.Button(self.mainframe, text="Finish", command=save_to_csv)
        self.finish_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Initialize lists to hold values
        customers = []
        check_numbers = []
        amounts = []
        discounts = []
        invoices_paid = []

        # Labels to display the values
        customer_label = ttk.Label(self.mainframe, text="Customers: ", background='white', font=('Brass Mono', 12))
        customer_label.grid(row=9, column=0, pady=5, sticky='NWES')

        check_number_label = ttk.Label(self.mainframe, text="Check Numbers: ", background='white', font=('Brass Mono', 12))
        check_number_label.grid(row=10, column=0, pady=5, sticky='NWES')

        amount_label = ttk.Label(self.mainframe, text="Amounts: ", background='white', font=('Brass Mono', 12))
        amount_label.grid(row=11, column=0, pady=5, sticky='NWES')

        discount_label = ttk.Label(self.mainframe, text="Discounts: ", background='white', font=('Brass Mono', 12))
        discount_label.grid(row=12, column=0, pady=5, sticky='NWES')

        invoices_label = ttk.Label(self.mainframe, text="Invoices Paid: ", background='white', font=('Brass Mono', 12))
        invoices_label.grid(row=13, column=0, pady=5, sticky='NWES')

        self.root.mainloop()

if __name__ == '__main__':
    App()
