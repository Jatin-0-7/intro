import os,pip
import random
import sys
import time
import names

#os.system('clear')
time.sleep(0.5)
print ("""
+========================+========================+
|               Coded By Naz-R               |
|                                                                      
+========================+========================+

""")
time.sleep(0.5)
print ("""
[*].Choose Which Type of Combo Mail You Want.
1)Mail:pass.
2)User:pass.
3)User:pass matching.
4)Mail.
5)Pass.
6)User.
7)user:pass with numbers 
8)user:with numbers
9)pass:with numbers 
10)pass:birth year
11)user:birth year
12)user:pass:birth year
99)Exit.

""")
menu = input("Enter Option ")
if menu=="1":
	#os.system('clear')
	gmail = input("Which Mail Type ? (Ex:@gmail.com): ")
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,2020)
		all1 = "%s%s%s"%(rname,num,gmail)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s%s"%(rlastname,num,gmail)
		allf = "%s%s%s%s"%(all2,":",rlastname,num) 
		print(alln)
		print(allf)
	x = input("\nPress Enter To Exit...")

if menu=="2":
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1900,2020)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rlastname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rname,num) 
		print(alln)
		print(allf)
	x = input("\nPress Enter To Exit...")


if menu=="3":
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,0)
		all1 = "%s"%(rname)
		alln = "%s%s%s"%(all1,":",rname)
		all2 = "%s"%(rlastname)
		allf = "%s%s%s"%(all2,":",rlastname)
		print(alln)
		print(allf)

if menu=="4":
	#os.system('clear')
	gmail = input("Which Mail Type ? (Ex:@gmail.com): ")
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1500,2020)
		all1 = "%s%s%s"%(rname,num,gmail)
		all2 = "%s%s%s"%(rlastname,num,gmail)
		print(all1)
		print(all2)
	x = input("\nPress Enter To Exit...")

if menu=="5":
	#os.system('clear')
	hwm = int(input("How Many Time (x2): "))
	i=1+1
	for i in range (0,hwm):
		i = 1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,999)
		alln = "%s"%(rname)
		print(alln)
	x = input("\nPress Enter To Exit...")

if menu=="6":
    hwm = int(input("How Many Time (x2): "))
    i=1
    for i in range (0,hwm):
        i = 1+1
        rname = names.get_first_name()
        rlastname = names.get_last_name()
        num = random.randint(0,999)
        all1 = "%s"%(rname)
        all2 = "%s"%(rlastname)
        print(all1)
        print(all2)
    x = input("\nPress Enter To Exit...")
    
if menu=="7":
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,999)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rlastname,num)
		print(alln)
		print(allf)
	x = input("\nPress Enter To Exit...")
	
if menu=="8":
	#os.system('clear')
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,2020)
		alln = "%s%s"%(rname,num)
		print(alln)
	x = input("\nPress Enter To Exit...")

if menu=="9":
    hwm = int(input("How Many Time (x2): "))
    i=1
    for i in range (0,hwm):
        i = 1+1
        rname = names.get_first_name()
        rlastname = names.get_last_name()
        num = random.randint(0,999)
        all1 = "%s%s"%(rname,num)
        all2 = "%s%s"%(rlastname,num)
        print(all1)
        print(all2)
    x = input("\nPress Enter To Exit...")
    
if menu=="10":
	#os.system('clear')
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1900,2023)
		alln = "%s%s"%(rname,num)
		print(alln)
	x = input("\nPress Enter To Exit...")

if menu=="11":
    hwm = int(input("How Many Time (x2): "))
    i=1
    for i in range (0,hwm):
        i = 1+1
        rname = names.get_first_name()
        rlastname = names.get_last_name()
        num = random.randint(1900,2023)
        all1 = "%s%s"%(rname,num)
        all2 = "%s%s"%(rlastname,num)
        print(all1)
        print(all2)
    x = input("\nPress Enter To Exit...")
    
if menu=="12":
	hwm = int(input("How Many Time (x2): "))
	i=1
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1500,2023)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rlastname,num)
		print(alln)
		print(allf)
	x = input("\nPress Enter To Exit...")
	
if menu=="99":
     quit()

	