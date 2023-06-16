# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 00:02:38 2020

@author: Peter
"""

def my_time_table(num, n, multiplicator):
    n = int(n)
    num = int(num)
    multiplicator = int(multiplicator)
    while(n <= num):
        print(n, " x ", num, " = ", n*num)
        n=n+multiplicator
        


num = input("Enter the number we multiply to ")
n =   input("\nEnter the number we multiply from ")
multiplicator = input("\nEnter the multiplicator ")



my_time_table(num, n, multiplicator)