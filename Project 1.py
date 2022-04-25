# Author: Dippal Adhikari
# Date created: 14 April 2022
# Date last changed: 24 April 2022
# This program compares compound interest rates of 3 different banks and helps user to find the best bank.
# Input: banks.txt
# Output: bestBank.txt

from tkinter import *  # for GUI
from tkinter import messagebox as m_box  # to display error message

window = Tk()
window.title("Comparison of banks")
window.geometry("500x400")
window.configure(background="#FFFDE7")  # to change the background colour of whole GUI

# declaring variables to store value later on
lblHead = Label(window)
lblAmount = Label(window)
entRate = Entry(window)
entAmount = Entry(window)
entResult1 = Entry(window)
entResult2 = Entry(window)
btnExit = Button(window)
btnCalculate = Button(window)
btnNext = Button(window)
btnAgain = Button(window)
btnExit2 = Button(window)

# initializing variables
NO_OF_BANKS = 0
bankList = []
apyList = []
listCompound = 0
rate = 0
index = 0
highestRate = 0
balance = 0
amount = 0

OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]  # list for dropdown menu options


def main():
    # globalizing variables to store the calculated/ new data outside the function
    global bankList
    global apyList
    global entAmount
    global amount
    global NO_OF_BANKS
    global lblAmount

    # reading a file and containing its contents in a list
    # use of try except statement to handle errors
    try:
        infile = open("banks.txt", "r")
        bankList = [line.strip() for line in infile]
        infile.close()
        if len(bankList) == 0:
            m_box.showerror("Error", "File banks.txt has no information.\nPlease check your file")
            # Error message box shown as the file can have no information
            close()  # to close the program if no file is found to start the program

    except FileNotFoundError:  # 'ValueError' used as an unacceptable string could be entered by the user
        m_box.showerror("Error", "File banks.txt doesn't exist.\nPlease check your file")
        close()

    NO_OF_BANKS = len(bankList)  # used to store a constant value
    apyList = [0] * NO_OF_BANKS  # initializing list for storing APYs
    lblAmount = Label(window, text="Please enter the amount that needs to be deposited:", bg="#FFFDE7")
    lblAmount.grid(row=0, column = 0, pady=20, sticky=W)
    amount = StringVar()
    entAmount = Entry(window, width=20, textvariable=amount, state="normal")
    entAmount.grid(row=0, column=1, sticky=W)

    bankDetails(0)


def bankDetails(i):
    # function to input the bank details
    global lblHead
    global entRate
    global lblAmount
    global btnExit
    global btnCalculate
    global btnNext
    global btnAgain
    global listCompound
    global entAmount
    global amount
    global rate

    # using destroy and forget element to remove widgets for another loop
    btnCalculate.destroy()
    btnNext.destroy()
    btnExit.destroy()
    lblHead.grid_forget()

    lblHead = Label(window, text="Please enter the details of " + bankList[i], font="Helvetica 10 bold", bg="#FFFDE7")
    lblHead.grid(row = 1, pady=3, columnspan=5)

    rate = StringVar()
    lblRate = Label(window, text="Stated Interest Rate:", bg="#FFFDE7")
    lblRate.grid(row = 2, column = 0, pady=3)
    entRate = Entry(window, width=20, textvariable=rate)  # entry to input rate
    entRate.grid(row = 2, column = 1, sticky=W, pady=3)

    lblCompound = Label(window, text="Compounding time(s) per year:", bg="#FFFDE7")
    lblCompound.grid(row = 3, column = 0, pady=3)
    listCompound = StringVar()
    listCompound.set(OPTIONS[0])  # default value for drop down menu
    menu = OptionMenu(window, listCompound, *OPTIONS)  # dropdown menu to input compounding times
    menu.grid(row = 3, column = 1, sticky=W, pady=3)

    # exit button to close the program anytime
    btnExit = Button(window, text="Exit", bg="red", fg="white", command=close)
    btnExit.grid(row = 5, column = 0, pady=3)

    # code to display next button and to replace it with calculate button in the last loop
    if i != NO_OF_BANKS - 1:
        btnNext = Button(window, text="Next", bg="blue", fg="white", command=lambda: calculateAPY(i))
        btnNext.grid(row = 5, column = 1, sticky=W, pady=3)
    else:
        btnCalculate = Button(window, text="Calculate", bg="green", fg="white", command=lambda: calculateAPY(i))
        btnCalculate.grid(row = 5, column = 1, sticky=W, pady=3)

    # created a blank label for proper spacing in the GUI
    lblSpace = Label(window, bg="#FFFDE7")
    lblSpace.grid(pady = 5)


def calculateAPY(i):
    # function to calculate APYs of banks and to store it in a list
    global rate
    global apyList
    global entAmount
    global amount
    global index
    global highestRate
    global balance

    btnExit.destroy()
    btnNext.destroy()

    amountCheck = entAmount.get()
    if amountCheck == "":
        m_box.showerror("Error", "Deposit amount cannot be empty.")  # Error message box shown as user can leave the field empty
        bankDetails(i)
    else:
        # use of try except statement to handle errors
        try:
            amountCheck = int(amountCheck)  # to check if the input is a valid number or not
            if amountCheck == 0:
                m_box.showerror("Error", "Deposit amount cannot be zero.")  # Error message box shown as user could enter zero as a value
                entAmount.destroy()  # clearing previous clipboard of the variable
                amount = StringVar()
                entAmount = Entry(window, width=20, textvariable=amount, state="normal")
                entAmount.grid(row=0, column=1, sticky=W)
                bankDetails(i)

            elif amountCheck < 0:
                m_box.showerror("Error", "Deposit amount cannot be negative.")  # Error message box shown as user could enter a negative value
                entAmount.destroy()  # clearing previous clipboard of the variable
                amount = StringVar()
                entAmount = Entry(window, width=20, textvariable=amount, state="normal")
                entAmount.grid(row=0, column=1, sticky=W)
                bankDetails(i)

        except ValueError:
            m_box.showerror("Error", "Please enter a valid number in amount field.")  # 'ValueError' used as an unacceptable string could be entered by the user
            entAmount.destroy()  # clearing previous clipboard of the variable
            amount = StringVar()
            entAmount = Entry(window, width=20, textvariable=amount, state="normal")
            entAmount.grid(row=0, column=1, sticky=W)
            bankDetails(i)

        else:
            # if/else used to loop the program if except element was not run
            # otherwise, whole else code of try/ except would run
            if amountCheck <= 0:
                bankDetails(i)
            else:
                rateCheck = entRate.get()
                if rateCheck == "":
                    m_box.showerror("Error", "Rate cannot be empty.")  # Error message box shown as user can leave the field empty
                    bankDetails(i)
                else:
                    try:
                        rateCheck = float(rateCheck)
                        if rateCheck == 0:
                            m_box.showerror("Error", "Rate cannot be zero.")  # Error message box shown as user could enter zero as a value
                            bankDetails(i)

                        elif rateCheck < 0:
                            m_box.showerror("Error", "Rate cannot be negative.")  # Error message box shown as user could enter a negative value
                            bankDetails(i)

                    except ValueError:  # 'ValueError' used as an unacceptable string could be entered by the user
                        m_box.showerror("Error", "Please enter a valid number in rate field.")
                        bankDetails(i)

                    else:
                        # if/else used to terminate the function and start it again
                        # since if try runs,
                        if rateCheck <= 0:
                            bankDetails(i)
                        else:
                            entAmount = Entry(window, width=20, textvariable=amount, state="readonly")
                            entAmount.grid(row=0, column=1, sticky=W)

                            compound = eval(listCompound.get())
                            apyList[i] = ((1 + (rateCheck/100) / compound) ** compound) - 1

                            i += 1
                            if i < NO_OF_BANKS:
                                bankDetails(i)
                            else:
                                result()


def highestAPY(apyList):
    # function to find the highest rate among three APYs
    pointer1 = 0  # pointer for while loop
    pointer2 = 0
    global index
    global highestRate
    loopIndicator: bool = True  # loop indicator for while loop
    while loopIndicator:
        if apyList[pointer1] >= apyList[pointer2]:
            highestRate = apyList[pointer1]
            index = pointer1
        else:
            highestRate = apyList[pointer2]
            index = pointer2
            pointer1 = pointer2

        pointer2 += 1
        if pointer2 == NO_OF_BANKS:
            loopIndicator = False
    return index, highestRate


def calculateBalance(highestRate):
    # function to calculate balance using the formula for calculating balance after 1 year, using the APY as the interest rate with only one compound time
    global balance
    amount1 = eval(entAmount.get())
    balance = amount1 * ((1 + highestRate / 1) ** 1)
    return balance


def result():
    # function to display the results in GUI and to write a file
    global index
    global highestRate
    global balance
    global btnAgain
    global btnExit2
    global entResult1
    global entResult2

    btnCalculate.destroy()  # to remove the calculate button

    btnExit2 = Button(window, text="Exit", bg="red", fg="white", command=close)
    btnExit2.grid(row = 9, column= 0)

    btnAgain = Button(window, text="Compare again", bg="blue", fg="white", command=again)
    btnAgain.grid(row = 9, column= 1)

    Result1 = StringVar()
    entResult1 = Entry(window, width=67, textvariable=Result1, state = "readonly", bg="#FFFDE7")
    entResult1.grid(row = 7, columnspan=2, padx = 10, pady=3, sticky=W)

    Result2 = StringVar()
    entResult2 = Entry(window, width=67, textvariable=Result2, state = "readonly", bg="#FFFDE7")
    entResult2.grid(row = 8, columnspan=2, padx = 10, pady=3, sticky=W)

    index, highestRate = highestAPY(apyList)
    balance = calculateBalance(highestRate)

    Result1.set(bankList[index] + " has the highest APY.")
    Result2.set("The balance in your account after 1 year will be $" + str(balance) + ".")

    # creating a text-file for storing the details of the best bank
    outfile = open("bestBank.txt", "w")
    outfile.writelines(str(bankList[index]) +  " has the highest APY.")
    outfile.writelines(" The balance in that account after 1 year will be $" + str(balance) + ".")


def again():
    # function to delete all widgets if exit button is pressed
    global entAmount
    global amount
    btnAgain.destroy()
    btnExit.destroy()
    btnNext.destroy()
    btnExit2.destroy()
    entResult1.destroy()
    entResult2.destroy()
    amount = StringVar()
    entAmount = Entry(window, width=20, textvariable=amount)
    entAmount.grid(row=0, column=1, sticky=W)
    bankDetails(0)


def close():
    # function to close the program
    window.destroy()

    # another tkinter window for exit message
    exitWindow = Tk()
    exitWindow.configure(background="#FFFDE7")
    exitWindow.title("Closing...")
    exitWindow.geometry("400x200")

    # use of after element to automatically destroy the tkinter window after certain time
    exitWindow.after(1400, lambda: exitWindow.destroy())

    lblExit = Label(exitWindow, text="Thanks for using my program.", font = "Century 17", bg = "#FFFDE7")
    lblExit.place(relx = 0.5, rely = 0.5, anchor = CENTER)

main()  # calling the main function


window.mainloop()
