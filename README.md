# Sem-1-project---Python
Different banks provide customers with different interest rates for saving accounts. A saving account states an interest rate and a compounding period. Given that the amount deposited is P, the interest rate is m and the times that the interest is compounded per year is m, the formula for finding the balance in the account after 1 year is:
P* (1+r/m)^m
Although the stated interest rate of two different banks is the same, the compounding time can increase/ decrease the amount in the saving account after 1 year.
For example, if a customer deposits $500 at ABC bank at 4% interest compounded four times per year, the final balance after 1 year will be:
500* (1+0.04/4)^4=500*1.0406=$520.3
If a customer deposits the same amount at XYZ bank at the same interest rate but compounded 3 times per year then the final balance after 1 year will be:
500* (1+0.04/3)^3=500*1.0405=$520.27
Therefore, depending on the stated interest rate is not practical. So, we have the concept of APY (Annual Percentage Yield) which converts different stated interest rates and different compounding periods to an interest rate that is compounded only once per year. This helps to make a comparison of interest rates among different saving accounts. Given that the stated interest rate is r, compounding times is m, the formula to calculate the APY is:
APY= (1+r/m)^m-1
When using the APY as an interest rate to calculate the total balance after a year, the compounding time will be 1.

I have prepared a python program to ask the user the amount that he/ she wants to deposit, and compared the inputted interest rates offered by three different banks to determine the most suitable interest rate for the customer. The names of those 3 banks are already stored in a text file (banks.txt). The final balance after one year, if the amount is deposited at the most suitable bank, is also calculated, and a new text file (bestBank.txt) is created to store the name of the most suitable bank and the balance after 1 year. The most suitable bank name and the final value in that bank after 1 year are also displayed in the GUI.
