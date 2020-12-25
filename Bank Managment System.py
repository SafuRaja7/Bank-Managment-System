costumerinfo=[]  #created list for customer info
accountinfo=[]   #created list for account details
transaction=[]   #created list for transaction history

import datetime


rec = 0 #for no of records
magain = "y" #declaring again for the main menu loop
again="y"  ##declaring again for the sub menu loop
while magain=="y":
    print("-------------------------------------------")
    print("                   WELCOME")                     #printed welcome
    print("-------------------------------------------")
    print("                   MAIN MENU")                   #printed main menu
    print("1. costumer info \n2. Account info \n3. Transaction \n4. Exit")      #printed the menu

    choice=eval(input("Enter choice : "))      #prompt the user to input choice
    
    while choice <= 0 or choice >= 5:    #check
        choice = eval(input("Wrong choice!!!\n\n Enter choice again : ")) #for invalid input
    if choice == 1:     #condition
        while again=="y":  #check for returning to menu
            print("-------------------------------------------")  
            print("                   MENU")                    #printed MENU
            print("1. Add \n2. View \n3. Search \n4. Edit \n5. Back")  #printed sub menu
            choice=eval(input("Enter choice : "))          #prompt the user to enter choice
            
            while choice<=0 or choice>=6:     #check
                  choice = eval(input("Wrong choice!!!\n\n Enter choice again : ")) #for invalid input
                  
                  
            if choice==1:   #condition
                agn = "y"    #for returning to menu
                while agn == "y":   #check for returning to menu
                    print("-------------------------------------------")
                    rec +=1               #increment in record
                    print ("\n          Costumer Record",rec)   #printed costumer's record
    
                    costumerinfo.append(input("\nEnter the name :"))   #assigned the name
                
    
                    costumerinfo.append(eval(input("\nEnter the CNIC no. :")))   #assigned the CNIC no
                    
    
                    costumerinfo.append(input("\nEnter the Address :"))     #assigned the address
    
                    costumerinfo.append(input("\nEnter the contact :"))     #assigned the contact
    
                    agn = input("\n\nADD ANOTHER RECORD?\n y/n ")  # FOR ADDING ANOTHER RECORD
                            
                            
            
                    
                    
            elif choice == 2:   #to view
                print("-------------------------------------------")
                print ("\n","Name","       ","CNIC no.","       ","Address","       ","Contact")   #printed name,cnic,address,contact
                print("-------------------------------------------")
                for i in range (0,len(costumerinfo),4):    #used range for printing list
        
                    print ("\n\n",costumerinfo[i],"       ",costumerinfo[i+1],"       ",costumerinfo[i+2],"       ",costumerinfo[i+3])    


             
                
            
            elif choice==3:   #to search
                
                norecord = 1   #initial value of record
                search = eval(input("\nEnter the CNIC NO. to search :"))   #prompt the user to enter cnic for searching
                
                for i in range (1,len(costumerinfo),4):    #used range for printing list
                    if search == costumerinfo[i]:   #condition for searching
                        print ("\nName :   ",costumerinfo[i-1], "\n\n  CNIC no. :",costumerinfo[i],"\n\nAddress :",costumerinfo[i+1],"\n\nAccount balance :",costumerinfo[i+2])
                        norecord  += 1    #increment in record
            
                if norecord == 1:    #condition for having no record
                    print ("NO RECORD FOUND")
                    
            elif choice ==4:      #to edit
                
                edit=eval(input("Enter CNIC you want to edit : "))    #prompt the user to enter CNIC
                
                
                for i in range (0,len(costumerinfo),4):    #used range for printing list
                    if  edit== costumerinfo[i+1]:    #condition for editing
                        print("--------------Edit----------")
                        costumerinfo[i]=input("Edit Name : ")   #prompt the user to enter name
                        costumerinfo[i+1]=input("Edit CNIC : ")     #prompt the user to enter CNIC
                        costumerinfo[i+2]=input("Edit Address : ")  #prompt the user to enter Address
                        costumerinfo[i+3]=input("Edit Contact : ")  #prompt the user to enter contact
                        break
                    
                else:     #used else condition
                    print("No CNIC found")
                        
        
                   
                
                
                

            
               
            elif choice == 5:    #to go back to main menu
                break
               
               
               
               
    elif choice ==2:     #to manage account info  
        while again=="y":    #for going back to menu
            print("\n-------------------------------------------")
            print("  \n                 ACCOUNT INFORMATION")
            print("\n\n1. Add Account details \n2. View Account details  \n3. Back")
            choice=eval(input("Enter choice : "))   #prompot the user to enter choice
            
            while choice<=0 or choice>=4:    #check
                  choice = eval(input("Wrong choice!!!\n\n Enter choice again : ")) #for invalid input
                
            if choice == 1:     #to add account
                for x in range (0,len(costumerinfo),4):    #used range for printing list
                    
                    accountinfo.append(costumerinfo[x])    #prompt the user to enter name
                    accountinfo.append(costumerinfo[x+1])   #prompt the user to enter CNIC
                
                    print ("\nENTER Details for")
                    print ("\ncostumer name : ",costumerinfo[x],"      ","CNIC No : ",costumerinfo[x+1])   #printed name and CNIC
                
                    accountinfo.append(eval(input("Enter account no. : ")))        #prompt the user to enter account number
                    accountinfo.append(eval(input("Enter ammount. : ")))          #prompt the user to enter ammount
                    accountinfo.append(input("Enter account type : "))             #prompt the user to enter account type
                
                      

                         

            elif choice == 2:        #to view account details
                print("\n-------------------------------------------------------------------------------------------")
                print ("\n\n                         Account details")
                print("\n-------------------------------------------------------------------------------------------")
                print ("\n\nNAME","       ","CNIC","       ","ACCOUNT NO","       ","AMOUNT","       ","ACCOUNT TYPE")
                print("\n-------------------------------------------------------------------------------------------")
                for x in range(0,len(accountinfo),5):     #used range for printing
                    print(accountinfo[x],"       ",accountinfo[x+1],"       ",accountinfo[x+2],"       ",accountinfo[x+3],"       ",accountinfo[x+4])
            
            elif choice == 3:          #to go back to menu
                break
            
            
            
            #choice 3 for regrestration of account no.
            
    elif choice== 3:        #for regrestration of account no.
        again = "y"     #for returning to menu
        while again == "y":
            print("-------------------------------------------")
            print("                   ACCOUNT INFORMATION")
            print("\n1. Transactions \n\n2. View Transaction Info  \n3. Back")
            choice=eval(input("Enter choice : "))      #prompt the user to enter choice
            
            while choice<=0 or choice>=4:           #check
                  choice = eval(input("Wrong choice!!!\n\n Enter choice again : ")) #for invalid input
                
            if choice == 1:         #to perform transaction
                accno = eval(input("Enter Account no. to perform Transaction : "))     #promot the user to enter account number
                
                i = 2  #for range in while loop below #initially at 2
                
                while i < len(accountinfo):    #check
                    if accno == accountinfo[i]:      #condition for accno equal to account number  
                        print("-------------------------------------------")
                        
                        print("\n1.Deposit \n2. Withdraw")
                        ch=eval(input("Enter choice : "))     #prompt the user to enter choice for deposting or withdrawl
            
                        while ch<=0 or ch>=3:   #check
                            ch = eval(input("Wrong choice!!!\n\n Enter choice again : ")) #for invalid input
                
                        if ch == 1:          #for depositing
                            
                            print("\n                   DEPOSIT")
                            
                            tamount = eval(input("Enter amount of transaction : "))     #prompt the user to enter transaction
                            
                            accountinfo[i+1] += tamount            #adding transaction in amount
                            
                            transaction.append(accountinfo[i-2]) #name
                            
                            transaction.append(accountinfo[i-1]) #cnic
                            
                            transaction.append(accountinfo[i]) #account no
                            
                            transaction.append("deposit")  #indication
                            
                            transaction.append(tamount) #transaction ammount
                            
                            transaction.append(datetime.datetime.now())   #to show current date and time
                            
                            break
                            
                        if ch == 2:     #for withdrawl
                            
                            print("\n                   WITHDRAW")
                            
                            tamount = eval(input("\n\nEnter amount of transaction : "))    #prompt the user to enter transaction
                            while tamount>accountinfo[i+1]:
                                print ("Amount cannot be withdrawed")
                                tamount=eval(input("Enter again"))
                                
                            accountinfo[i+1] -= tamount         #deducting transaction from ammount
                            
                            
                            transaction.append(accountinfo[i-2]) #name
                            
                            transaction.append(accountinfo[i-1]) #cnic
                            
                            transaction.append(accountinfo[i]) #account no
                            
                            transaction.append("withdrawl")  #indication
                            
                            transaction.append(tamount) #transaction
                            
                            transaction.append(datetime.datetime.now())     #for showing current date and time
                            
                            break

                    else:
                        i += 5     #incremnent 
                else:
                    print ("No record found!!!")
                    again = input("Return to menu ?\n\n   y/n")        #enter choice to go back to menu
                
            if choice == 2:            #for transaction details
                print("          \nTRANSACTION DETAILS")
                     
                     
                for x in range(0,len(transaction),6):    #range for printing list
                         
                    print ("\n\nNAME",  transaction[x],"       ","CNIC",transaction[x+1],"       ","ACCOUNT NO",transaction[x+2])
                    print("\nTRANSACTION TYPE",transaction[x+3],"         ","TRANSAACTION AMOUNT",transaction[x+4],"              ","DATE",transaction[x+5])
                
            if choice == 3 :  #choice 3 for returning to main menu
                break
            
        
    else:           
        print("Program Terminates")
        break
            
                              
                   
                   
    


    
