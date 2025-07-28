import tkinter as tk
from tkinter import messagebox

# Static exchange rates (1 unit of 'from' = ? units of 'to')
# Base currency: USD
exchange_rates = {
    'USD': {'USD': 1, 'INR': 83.2, 'EUR': 0.92, 'JPY': 151.1},
    'INR': {'USD': 1/83.2, 'INR': 1, 'EUR': 0.011, 'JPY': 1.82},
    'EUR': {'USD': 1.09, 'INR': 90.9, 'EUR': 1, 'JPY': 164.0},
    'JPY': {'USD': 0.0066, 'INR': 0.55, 'EUR': 0.0061, 'JPY': 1}
    
}

currencies = list(exchange_rates.keys())

def convert_currency(event=None):
    try:
        amount = float(entry_amount.get())
        from_curr = from_var.get()
        to_curr = to_var.get()

        if from_curr not in exchange_rates or to_curr not in exchange_rates[from_curr]:
            raise ValueError("Invalid currency selected.")

        result = amount * exchange_rates[from_curr][to_curr]
        messagebox.showinfo("Conversion Result", f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")

# GUI setup for currency convertor 
root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

tk.Label(root, text="From currency:").grid(row=1, column=0)
from_var = tk.StringVar(value="USD")
from_menu = tk.OptionMenu(root, from_var, *currencies)
from_menu.grid(row=1, column=1)

tk.Label(root, text="To currency:").grid(row=2, column=0)
to_var = tk.StringVar(value="INR")
to_menu = tk.OptionMenu(root, to_var, *currencies)
to_menu.grid(row=2, column=1)

tk.Button(root, text="Convert", command=convert_currency).grid(row=3, columnspan=2, pady=10)


root.bind("<Return>", convert_currency)


# code for running main file in loop
root.mainloop()
