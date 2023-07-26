# Program Description: This is a program to allow user to input sales for the year and plot the results on a graph
# Written by:          Bradley Hiscock
# Written on:          July 26th, 2023

# ******* Imported Libraries ***********

import matplotlib.pyplot as plt

# Main Program

janSales = float(input("Enter sales for January: "))
febSales = float(input("Enter sales for February: "))
marSales = float(input("Enter sales for March: "))
aprSales = float(input("Enter sales for April: "))
maySales = float(input("Enter sales for May: "))
junSales = float(input("Enter sales for June: "))
julSales = float(input("Enter sales for July: "))
augSales = float(input("Enter sales for August: "))
sepSales = float(input("Enter sales for September: "))
octSales = float(input("Enter sales for October: "))
novSales = float(input("Enter sales for November: "))
decSales = float(input("Enter sales for December: "))

x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [janSales, febSales, marSales, aprSales, maySales, junSales, julSales, augSales, sepSales, octSales, novSales, decSales]

plt.title("Total Sales for the Year")
plt.scatter(x_axis, y_axis, color='red', marker='x', label="item 1")

plt.xlabel("Month")
plt.ylabel("Total Sales ($)")

plt.grid(True)
plt.legend()

plt.show()