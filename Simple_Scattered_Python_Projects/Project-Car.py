import sys
print("\n*** Welcome to Car Rental Accounting System***")
for retry in range(5):
  rentalCode = input("What type of rental would you like?\n(B)udget, (D)aily, or (W)eekly?\n").upper()
  
  if rentalCode == "W":
    rentalPeriod = input("\nEnter number of Weeks Rented:\n")
    if rentalPeriod.isdigit():
      rentalPeriod = int(rentalPeriod)
      break
    else:
      print("\nYou did not enter a number. Please try again.")
        
  elif rentalCode == "B":
    rentalPeriod = input("\nEnter number of Days Rented:\n")
    if rentalPeriod.isdigit():
      rentalPeriod = int(rentalPeriod)
      break  
    else:
      print("\nYou did not enter a number. Please try again.")
        
  elif rentalCode == "D":
    rentalPeriod = input("\nEnter number of Days Rented:\n")
    if rentalPeriod.isdigit():
      rentalPeriod = int(rentalPeriod)
      break  
    else:
      print("\nYou did not enter a number. Please try again.")
        
  else:
    print ("\nYou have made an invalid choice.")
  
else:
  print ("You have made too many invalid choices. Exiting program.")
  exit()
#*** This is the start of Milestone 3 content ***
# failure handling to avoid zero division in future calculations 
if rentalPeriod == 0:
  print("\nYou entered a rental period of zero.")
  print("This means no rental has occured.")
  print("We at Car Rental Accounting System look forward to meeting your future rental needs.")
  print("Have a great day!\n")
  exit()
  
# get starting odometer reading and save as variable
# add while loop for failure handling to ensure numeric value is entered
while True:
  odoStart = input("\nEnter starting Odometer Reading:\n")
  if odoStart.isdigit():
    odoStart = int(odoStart)
    break
  else:
    print("\nYou did not enter a number. Please try again.")
    continue
# get ending odometer reading and save as variable
# add while loop for failure handling to ensure numeric value is entered
while True:
  odoEnd = input("\nEnter ending Odometer Reading:\n")
  if odoEnd.isdigit():
    odoEnd = int(odoEnd)
    break
  else:
    print("\nYou did not enter a number. Please try again.")
    continue

# create totalMiles variable
totalMiles = odoEnd - odoStart
# charge amount provided
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00    
# created list of all valid selections.
validSelection = ["B", "D", "W"]
#created x variable to be used in following while loop
x = rentalCode
# created while loop to define base charge for each valid selection in validSelection list
while x in validSelection:
  # use if/elif/else logic to calculate baseCharge
  if x == "B":
    baseCharge = rentalPeriod * budgetCharge
    break
  elif x == "D":
    baseCharge = rentalPeriod * dailyCharge
    break
  else:
    baseCharge = rentalPeriod * weeklyCharge
    break

# created nested if/elif/else logic used to calculate additional mileage charge 
if rentalCode == "B":
  mileCharge = "%.2f" % (totalMiles * 0.25)
elif rentalCode == "D":
  averageDayMiles = float(totalMiles / rentalPeriod) #create averageDayMiles variable and make it a float 
  if averageDayMiles < 101:
    extraMiles = 0
  else:
    extraMiles = averageDayMiles - 100.00
  mileCharge = "%.2f" % (extraMiles * 0.25)
else:
  averageWeekMiles = float(totalMiles / rentalPeriod)
  if averageWeekMiles > 900:
    extraMiles = 100.00
    mileCharge = extraMiles
  else:
    extraMiles = 0.00
    mileCharge = extraMiles
# convert charges to float for next calculation/amount variable creation
mileCharge = float(mileCharge)
baseCharge = float(baseCharge)
# create subTotal, and amoutDue variables
subTotal = (mileCharge + baseCharge)
amountDue = (subTotal)
#convert differnt charges and amounts to 2 decimal float for proper display in summary
baseCharge = "%.2f" % (baseCharge)
mileCharge = "%.2f" % (mileCharge)
amountDue = "%.2f" % (amountDue)
# print summary with additional spacing to match required format
# added starting odo, ending odo, miles driven, mileage charge,fields for more detailed itemization
print("\nRental Summary")
print("Rental Code:        " + rentalCode)
print("Rental Period:      " + str(rentalPeriod)) #deleted extra space on rental period to properly align summary printout
print("Starting Odometer:  " + str(odoStart))
print("Ending Odometer:    " + str(odoEnd))
print("Miles Driven:       " + str(totalMiles))
#print("Base Charge:        $" + str(baseCharge))
#print("Mileage Charge:     $" + str(mileCharge))
print("Amount Due:         $" + str(amountDue))
print("\nThank you for Car Rental Accounting System")
print("Have a great day!\n")

