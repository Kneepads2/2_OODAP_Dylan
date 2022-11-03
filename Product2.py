from itertools import product
import math
import time
import random
import re

print("\nWelcome to Dylan's off-brand inventory system!!!!\n")

class ProductInput:
    def __init__(self):
        print("")

    def getCode(self):    
         while True: #Gathering the product code. Using a while loop and valueErrors to make sure that the input received is not letters or below 100 or above 1000
            try:
              self.product_Code = int(input('What is the code of the product?  '))
              if (self.product_Code < 100 or self.product_Code > 1000):
                  raise ValueError       
              break
            except ValueError:
                  print('Please enter the code. It is a number between 100 and 1000.')

    def getName(self):
        self.product_Name = str(input("What is the name of the product? ")) # No need for the loops since we only need string
        if (self.product_Name == ""): # If they enter nothing, it should make the product name 'Unnamed Product'
            self.product_Name = "Unnamed Product"

    def getRetailPrice(self):
        while True: #Gathering the sales price. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
            try:
              self.product_salesPrice = float(input('What is the retail price of the product?  '))
              if (self.product_salesPrice < 0):
                raise ValueError       
              break
            except ValueError:
                print('Please enter the retail price of your product. You cannot charge people negative dollars. ')

    def getManufacturePrice(self):
        while True: #Gathering the manufacture cost. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
            try:
                 self.product_manufactureCost = float(input('What is the manufacture price of the product?  '))
                 if (self.product_manufactureCost < 0):
                        raise ValueError       
                 break
            except ValueError:
                print('Please enter the manufacture price of your product. Nothing can cost negative dollars. ')

    def getStockLevel(self):
        while True: #Gathering the stock level. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
            try:
                  self.stock_Level = int(input('How much stocks of your product do you have right now?  '))
                  if (self.stock_Level < 0):
                        raise ValueError       
                  break
            except ValueError:
                print('There\'s no way you have that amount of stock. Please enter how much stock you have.  ')

    def getEstimatedMonthlyManufactured(self)
        while True: #Gathering the stock level. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
             try:
                 estimated_Monthly_UnitsManufactured = int(input('How many products can you manufacture per month.  '))
                 if (estimated_Monthly_UnitsManufactured < 0):
                    raise ValueError       
                 break
             except ValueError:
                 print('Impossible.  ')

    def getMonths(self):
        while True: #Gathering how many months the user wants to predict
             try:
               months = int(input('How many months would you like for us to predict?  '))
               if (months < 0 or months > 12):
                    raise ValueError       
               break
             except ValueError:
               print('We can only predict for the next 12 months.  ')

print("\n******* Dylan's off-brand inventory system ******\n")
class ProductStockReport:

    def __init__(self,code,name,salesPrice,manufactureCost,stock,monthlyUnitsMade,months,unitsSold,totalSold):
        self.code = code
        self.name = name
        self.salesPrice = salesPrice
        self.manufactureCost = manufactureCost
        self.stock = stock
        self.monthlyUnitsMade = monthlyUnitsMade
        self.months = months
        self.unitsSold = unitsSold
        self.totalSold = totalSold
    
    def getProductCode(self): #to get the product code
        return "Product code:  "+ str(self.code)
    
    def getProductName(self): #to get the product name
        return "Product name: "+ str(self.name)

    def getSalesPrice(self): #to get the sales price per unit
        return "Sales Price: $ {:.2f}".format((self.salesPrice))+" CAD"
    
    def getManufactureCost(self): #to get the manufacture cost per unit
        return "Manufacture cost: $ {:.2f}".format((self.manufactureCost))+" CAD"
    
    def getMonthlyProduction(self): # to get the estimiated monthly production
        return "Monthly Production: "+str(self.monthlyUnitsMade) + " units (Approx.)"

    def predictedStockStatement(self): #this will print perfectly mimic the predicted stock statement shown in the assignment, figure 1
        counterOne = 0
        
        while (counterOne < self.months):

            self.unitsSold = random.randint(0,int(self.monthlyUnitsMade) + int(self.stock))
            self.stock = (int(self.stock) - int(self.unitsSold) + int(self.monthlyUnitsMade))
            self.totalSold += self.unitsSold
            moneyGained = ((int(self.unitsSold) * float(self.salesPrice)) - (int(self.monthlyUnitsMade) * float(self.manufactureCost) ))
            counterOne += 1

            print ("\nMonth "+ str(counterOne)+ ":\n    Manufactured: "+ str(self.monthlyUnitsMade)+ " units\n    Sold: "+str(self.unitsSold)+ " units\n    Stock: " + str(self.stock)+ " units")
            if (moneyGained < 0):
                print("    Net loss: $ {:.2f}".format(moneyGained)+" CAD")
            else: 
                print("    Net profit: $ {:.2f}".format(moneyGained)+" CAD")
            time.sleep(1)
        return "***********************************\n"
            
    def netProfitOrLoss(self,months2): #this will produce the TOTAL net profit/loss
    # (Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacture Cost).”
        moneyGained = ((int(self.totalSold) * float(self.salesPrice)) - (int(self.monthlyUnitsMade) * int(months2) * float(self.manufactureCost) ))
        if (moneyGained < 0):
            
            return("Total Net loss: $ {:.2f}".format(moneyGained)+" CAD")
        else:
            return("Total Net profit: $ {:.2f}".format(moneyGained)+" CAD")

#to be able to print everything
p = ProductStockReport(product_Code,product_Name,product_salesPrice,product_manufactureCost,stock_Level,estimated_Monthly_UnitsManufactured,months,0,0)

print(p.getProductCode())
print(p.getProductName())
print(p.getSalesPrice())
print(p.getManufactureCost())
print(p.getMonthlyProduction())
print(p.predictedStockStatement())# printing everything
print(p.netProfitOrLoss(months))

