#!/usr/bin/env python
# coding: utf-8




from tkinter import *
import tkinter as tk
from tkinter import ttk
import re

import requests





class currencyconverter():
    def __init__(self,url):
        self.data=requests.get(url).json()
        self.currencies=self.data['rates']
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount
            





class currencyconverterUi(tk.Tk):
    def __init__(self,converter):
            tk.Tk.__init__(self)
            self.title = 'Currency Converter'
            self.currency_converter = converter

            #self.configure(background = 'blue')
            self.geometry("500x200")
            self.intro_label=Label(self,text="Welcome To Real Time Currency Converter",fg="blue",bg="white",borderwidth=3,relief=tk.RAISED)
            self.intro_label.config(font=("Courier",15,'bold'))
            self.intro_label.place(x = 10 , y = 5)
           
            self.date_label = Label(self,width=50,fg="blue", text = f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
            self.date_label.place(x = 70, y= 50)
            
            
            #entry                        
            valid = (self.register(self.restrictNumberOnly), '%d','%P')
            self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
            
            self.convertedamtfieldlabel=Label(self,borderwidth=3,relief=tk.RIDGE,bg='white',fg='black',justify=tk.CENTER,width=17,text='')
            
            #drodown
            self.from_currency_variable=StringVar(self)
            self.to_currency_variable=StringVar(self)
            self.from_currency_variable.set("INR")                        
            self.to_currency_variable.set("USD")
            font=("Courier",12,"bold")
            self.option_add('*TCombobox*Listbox.font',font) 
            self.from_currency_dropdown=ttk.Combobox(self,textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()),font=font,width=12,state='readonly',justify=tk.CENTER)
            
            self.from_currency_dropdown.place(x=30,y=120)
            self.to_currency_dropdown=ttk.Combobox(self,textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()),font=font,width=12,state='readonly',justify=tk.CENTER) 
            
            
            
            self.amount_field.place(x=36,y=150)
            self.to_currency_dropdown.place(x=340,y=120)
            self.convertedamtfieldlabel.place(x=346,y=150)      
            #button
            self.converterbutton=Button(self,text="Convert",fg="white",bg="blue",command=self.perform) 
            self.converterbutton.config(font=("Courier",10,'bold'))
            self.converterbutton.place(x=225,y=135)  
            
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.convertedamtfieldlabel.config(text = str(converted_amount))
                                    
    
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))
              
           
                   
                                    
                                    
                                    





if __name__ == '__main__':
    url='https://api.exchangerate-api.com/v4/latest/USD'

    converter=currencyconverter(url)
    currencyconverterUi(converter)
    mainloop()


# In[ ]:





# In[ ]:




