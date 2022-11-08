import matplotlib.pyplot as plt
import pandas as pd
import csv
bill=0
bill1=0
bill2=0
bill3=0
bill4=0
bill5=0
bill6=0
bill7=0
bill8=0
bill9=0
bill10=0
bill11=0
bill12=0
bill13=0
bill14=0
bill15=0
bill16=0
bill17=0
bill18=0
bill19=0
bill20=0
bill21=0
bill22=0
bill23=0
bill24=0 
bill25=0
bill26=0
bill27=0
bill28=0
bill29=0
bill30=0
bill31=0
bill32=0
bill33=0
bill34=0
bill35=0
bill36=0
bill37=0
bill38=0
bill39=0
bill40=0
bill41=0
bill42=0
bill43=0
bill44=0
bill45=0
bill46=0
bill47=0
while True:
    def main_menu():
        print(100*'🔥')
        print()
        print("""
                                                  WELCOME TO OUR DREAM PARK                       
                                                  -------------------------
                                                                                                                  Contact Us: +918290241234
                            ''Our dream is to create the most memorable fun moments of your life!''                           +919876230146
                                                                                                                  Mail ID: dreampark@gmail.com
                                                                                      
        

                                            MAIN MENU
                                            *********

                                           1)Air Slides                                                    ____________________________________________
                                           2)Water Slides                                                 |                PARK TIMINGS                |
                                           3)Ground Slides                                                |    Monday - Friday : 11:00 AM To 8:00 PM   |
                                           4)Admin                                                        |   Saturday - Sunday : 09:00 AM To 8:00 PM  |
                                           5)Data Visualization                                           |____________________________________________|
                                           6)Billing
                                           7)Exit
        """)
        print()
        print(100*'🔥')
        print()
    main_menu()
    print()
    ch=input('Enter Your Wish :- ')
    print()
    print()
    if ch=='1':
        def main_menu_of_airslides():
            print(160*'♦️')
            print()
            print("""                                                 You Are Viewing The Main Menu Of Air Slides
                                                ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖       
                        
                                                    A)Available Air Slides
                                                    B)Search A Slide By Name
                                                    C)Book A Slide 
                                                    D)Back To Main Menu
                        """)
            print()
            print(160*'♦️')
        main_menu_of_airslides()
        print()
        
        while True:
            print()
            a=input('Enter Your Choice :- ')
            print()
            print()
            if a=='A'or a=='a':
                def air_slides(b):
                    print(70*'*')
                    print(b)
                    print(70*'*')
                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                b.set_index('ID',inplace=True)
                air_slides(b)
                print()
                print()
                main_menu_of_airslides()
                
            elif a=='B'or a=='b':
                d=input("Search A Slide By Name:- ")                                                            
                S=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                if S.loc[0,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                   
                elif S.loc[1,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                   
                elif S.loc[2,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                   
                elif S.loc[3,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                    
                elif S.loc[4,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                   
                elif S.loc[5,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                   
                elif S.loc[6,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                    
                elif S.loc[7,'NAME_OF_SLIDES']==d:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                                 
                else:
                    print()
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Not Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_airslides()
                    
            elif a=='C'or a=='c':
                def add_record():
                    k=int(input('Enter ID:- '))
                    m=str(input('Enter Your Name :- '))
                    n=str(input('Enter Your Email Address:- '))
                    o=int(input('Enter Your Contact Number:- '))
                    p=str(input('Enter Your Residential Address:- '))
                    q=str(input('Enter Your City :- '))
                    r=str(input('Enter Your State :- '))
                    with open("E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv",'a')as file:
                        filewriter=csv.writer(file)
                        filewriter.writerow([k,m,n,o,p,q,r])
                add_record()
                print()
                print(50*'*')
                print('Your Details Is Successfully Saved.')
                print(50*'*')
                print()
               
                while True:
                    o=int(input('Enter Your Age :- '))
                    print()
                    if o>=9 and o<18:
                        print(50*'*')
                        print('You Are Eligibile To Ride')
                        print(50*'*')
                        print()
                        print()
                        b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                        print(50*'*')
                        print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                        print(50*'*')
                        print()
                        print(50*'*')
                        print('Write A9 For Go Back To Main Menu Of Air Slides ')
                        print(50*'*')
                        print()
                        while True:    
                            D=input('Enter The ID Of Ride Which You Want To Book :- ')
                            print()
                            
                            if b.loc[0,'ID']==D:
                                bill=b.loc[0,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill=R*bill
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[1,'ID']==D:
                                bill1=b.loc[1,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill1=R*bill1
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[2,'ID']==D:        
                                bill2=b.loc[2,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill2=R*bill2
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[3,'ID']==D:
                                bill3=b.loc[3,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill3=R*bill3
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[4,'ID']==D:
                                bill4=b.loc[4,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill4=R*bill4
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[5,'ID']==D:
                                bill5=b.loc[5,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill5=R*bill5
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[6,'ID']==D:
                                bill6=b.loc[6,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill6=R*bill6
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[7,'ID']==D:
                                bill7=b.loc[7,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                print()
                                bill7=R*bill7
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif D=='A9' or D=='a9':
                                break
                            else:
                                print(50*'*')
                                print('INCORRECT ID')
                                print(50*'*')
                        main_menu_of_airslides()
                        break
                        
                    elif o>=18 and o<45:
                        print(50*'*')
                        print('You Are Eligibile To Ride')
                        print(50*'*')
                        print()
                        b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                        print(50*'*')
                        print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                        print(50*'*')
                        print()
                        print(50*'*')
                        print('Write A9 For Go Back To Main Menu Of Air Slides ')
                        print(50*'*')
                        print()
                        while True:    
                            D=input('Enter The ID Of Ride Which You Want To Book :- ')
                            print()
                            
                            if b.loc[0,'ID']==D:
                                bill8=b.loc[0,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill8=R*bill8
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[1,'ID']==D:
                                bill9=b.loc[1,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill9=R*bill9
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[2,'ID']==D:
                                bill10=b.loc[2,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill10=R*bill10
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[3,'ID']==D:
                                bill11=b.loc[3,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill11=R*bill11
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[4,'ID']==D:
                                bill12=b.loc[4,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill12=R*bill12
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[5,'ID']==D:
                                bill13=b.loc[5,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill13=R*bill13
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[6,'ID']==D:
                                bill14=b.loc[6,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill14=R*bill14
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[7,'ID']==D:
                                bill15=b.loc[7,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill15=R*bill15
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\AIR_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write A9 For Go Back To Main Menu Of Air Slides ')
                                print(50*'*')
                                print()
                            elif D=='A9' or D=='a9' :
                                break
                            else:
                                print(50*'*')
                                print('INCORRECT ID')
                                print(50*'*')
                        main_menu_of_airslides()
                        break
                    else:
                        print(50*'*')
                        print('Sorry!You Are Not Eligible To Ride')
                        print(50*'*')
                    
            elif a=='D'or a=='d':
                
                break
            else:
                print(50*'*')
                print('Invalid Choice')
                print(50*'*')
                print()
                main_menu_of_airslides()
                
    elif ch=='2':
        def main_menu_of_waterslides():
            print(160*'♦️')
            print()
            print("""                                                 You Are Viewing The Main Menu Of Water Slides️️️️️
                                                 ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
                                            
                                                 A)Available Water Slides
                                                 B)Search A Slide By Name
                                                 C)Book A Slide 
                                                 D)Back To Main Menu
                        """)
            print(160*'♦️')
            print()
        main_menu_of_waterslides()
        
        while True:
            print()
            a=input('Enter Your Choice :- ')
            print()
            print()
            if a=='A'or a=='a':
                def water_slides(e):
                    print(70*'*')
                    print(e)
                    print(70*'*')
                e=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                e.set_index('ID',inplace=True)
                print()
                water_slides(e)
                print()
                print()
                main_menu_of_waterslides()
                
            elif a=='B'or a=='b':
                print()
                f=input("Search A Slide By Name :- ") 
                S=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')                                                           
                if S.loc[0,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*') 
                    print()
                    main_menu_of_waterslides()
                    
                elif S.loc[1,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')   
                    print()
                    main_menu_of_waterslides()
                    
                elif S.loc[2,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_waterslides()
                    
                elif S.loc[3,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_waterslides()
                   
                elif S.loc[4,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_waterslides()
                    
                elif S.loc[5,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_waterslides()
                    
                elif S.loc[6,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_waterslides()
                    
                elif S.loc[7,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_waterslides()
                           
                else:
                    print()
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Not Exists :)")
                    print()
                    print(50*'*')
                    print()             
                    main_menu_of_waterslides()
                    
            elif a=='C'or a=='c':
                def add_record():
                    k=int(input('Enter ID:- '))
                    m=str(input('Enter Your Name :- '))
                    n=str(input('Enter Your Email Address:- '))
                    o=int(input('Enter Your Contact Number:- '))
                    p=str(input('Enter Your Residential Address:- '))
                    q=str(input('Enter Your City :- '))
                    r=str(input('Enter Your State :- '))
                    with open("E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv",'a')as file:
                        filewriter=csv.writer(file)
                        filewriter.writerow([k,m,n,o,p,q,r])
                add_record()  
                print()
                print(50*'*')
                print('Your Details Is Successfully Saved.')
                print(50*'*')
                print()
                
                while True:
                    o=int(input('Enter Your Age :- '))
                    print()
                    if o>=9 and o<18:
                        print(50*'*')
                        print('You Are Eligibile To Ride')
                        print(50*'*')
                        print()
                        print()
                        b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                        print(50*'*')
                        print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                        print(50*'*')
                        print()
                        print(50*'*')
                        print('Write W9 For Go Back To Main Menu Of Water Slides ')
                        print(50*'*')
                        print()
                        while True:    
                            D=input('Enter The ID Of Ride Which You Want To Book :- ')
                            print()
                            
                            if b.loc[0,'ID']==D:
                                bill16=b.loc[0,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill16=R*bill16
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[1,'ID']==D:
                                bill17=b.loc[1,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill17=R*bill17
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[2,'ID']==D:
                                bill18=b.loc[2,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill18=R*bill18
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[3,'ID']==D:
                                bill19=b.loc[3,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill19=R*bill19
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[4,'ID']==D:
                                bill20=b.loc[4,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill20=R*bill20
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[5,'ID']==D:
                                bill21=b.loc[5,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill21=R*bill21
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[6,'ID']==D:
                                bill22=b.loc[6,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill22=R*bill22
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[7,'ID']==D:
                                bill23=b.loc[7,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill23=R*bill23
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif D=='W9' or D=='w9':
                                break
                            else: 
                                print()
                                print(50*'*')
                                print('INCORRECT ID')
                                print(50*'*')
                        main_menu_of_waterslides()
                        break
                        
                    elif o>=18 and o<45:
                        print(50*'*')
                        print('You Are Eligibile To Ride')
                        print(50*'*')
                        print()
                        b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                        print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                        print()
                        print(50*'*')
                        print('Write W9 For Go Back To Main Menu Of Water Slides ')
                        print(50*'*')
                        print()
                        while True:    
                            D=input('Enter The ID Of Ride Which You Want To Book :- ')
                            print()
                            
                            if b.loc[0,'ID']==D:
                                bill24=b.loc[0,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill24=R*bill24
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()  
                            elif b.loc[1,'ID']==D:
                                bill25=b.loc[1,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill25=R*bill25
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[2,'ID']==D:
                                bill26=b.loc[2,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill26=R*bill26
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[3,'ID']==D:
                                bill27=b.loc[3,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill27=R*bill27
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[4,'ID']==D:
                                bill28=b.loc[4,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill28=R*bill28
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[5,'ID']==D:
                                bill29=b.loc[5,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill29=R*bill29
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[6,'ID']==D:
                                bill30=b.loc[6,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill30=R*bill30
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[7,'ID']==D:
                                bill31=b.loc[7,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill31=R*bill31
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\WATER_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write W9 For Go Back To Main Menu Of Water Slides ')
                                print(50*'*')
                                print()
                            elif D=='W9'or D=='w9':
                                break
                            else:
                                print()
                                print(50*'*')
                                print('INCORRECT ID')
                                print(50*'*')
                        main_menu_of_waterslides()
                        break
                    else:
                        print(50*'*')
                        print('Sorry!You Are Not Eligible To Ride')
                        print(50*'*')
                        
            elif a=='D' or a=='d':
                break
            
            else:
                print()
                print(50*'*')
                print('Invalid Choice')
                print(50*'*')
                print()
                main_menu_of_waterslides()
                
    elif ch=='3':
        def main_menu_of_groundslides():
            print(160*'♦️')
            print()
            print("""                                                 You Are Viewing The Main Menu Of Ground Slides️️️️️
                                                  ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

                                                    A)Available Ground Slides
                                                    B)Search A Slide By Name
                                                    C)Book A Slide 
                                                    D)Back To Main Menu
                        """)
            print(160*'♦️')
            print()
        main_menu_of_groundslides()
        print()
        
        while True:
            a=input('Enter Your Choice :- ')
            if a=='A' or a=='a':
                def ground_slides(e):
                    print(70*'*')
                    print(e)
                    print(70*'*')
                e=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                e.set_index('ID',inplace=True)
                print()
                ground_slides(e)
                print()
                print()
                main_menu_of_groundslides()
        
            elif a=='B' or a=='b':
                print()
                f=input("Search A Slide By Name :- ")  
                S=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')                                                          
                if S.loc[0,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                    
                elif S.loc[1,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                    
                elif S.loc[2,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                    
                elif S.loc[3,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                   
                elif S.loc[4,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                    
                elif S.loc[5,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                    
                elif S.loc[6,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                    
                elif S.loc[7,'NAME_OF_SLIDES']==f:
                    print('\n')
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Exists :)")
                    print()
                    print(50*'*')
                    print()
                    main_menu_of_groundslides()
                           
                else:
                    print()
                    print(50*'*')
                    print()
                    print(" The Slide Which You Search Above,Is Not Exists :)")
                    print()
                    print(50*'*')
                    print()                   
                    main_menu_of_groundslides()
                    
            elif a=='C' or a=='c':
                def add_record():
                    k=int(input('Enter ID:- '))
                    m=str(input('Enter Your Name :- '))
                    n=str(input('Enter Your Email Address:- '))
                    o=int(input('Enter Your Contact Number:- '))
                    p=str(input('Enter Your Residential Address:- '))
                    q=str(input('Enter Your City :- '))
                    r=str(input('Enter Your State :- '))
                    with open("E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv",'a')as file:
                        filewriter=csv.writer(file)
                        filewriter.writerow([k,m,n,o,p,q,r])
                add_record()
                print()
                print(50*'*')
                print('Your Details Is Successfully Saved.')
                print(50*'*')
                print()
                while True:
                    o=int(input('Enter Your Age :- '))
                    print()
                    if o>=9 and o<18:
                        print(50*'*')
                        print('You Are Eligibile To Ride')
                        print(50*'*')
                        print()
                        b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                        print(50*'*')
                        print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                        print(50*'*')
                        print()
                        print(50*'*')
                        print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                        print(50*'*')
                        print()
                        while True:    
                            D=input('Enter The ID Of Ride Which You Want To Book :- ')
                            print()
                            
                            if b.loc[0,'ID']==D:
                                bill32=b.loc[0,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill32=R*bill32
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[1,'ID']==D:
                                bill33=b.loc[1,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill33=R*bill33
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[2,'ID']==D:
                                bill34=b.loc[2,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill34=R*bill34
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[3,'ID']==D:
                                bill35=b.loc[3,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill35=R*bill35
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[4,'ID']==D:
                                bill36=b.loc[4,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill36=R*bill36
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[5,'ID']==D:
                                bill37=b.loc[5,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill37=R*bill37
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[6,'ID']==D:
                                bill38=b.loc[6,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill38=R*bill38
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[7,'ID']==D:
                                bill39=b.loc[7,'KIDS_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill39=R*bill39
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','KIDS_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif D=='G9'or D=='g9':
                                break
                            else:
                                print()
                                print(50*'*')
                                print('INCORRECT ID')
                                print(50*'*')
                                print()
                        main_menu_of_groundslides()
                        break
                        
                    elif o>=18 and o<45:
                        print(50*'*')
                        print('You Are Eligibile To Ride')
                        print(50*'*')
                        print()
                        b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                        print(50*'*')
                        print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                        print(50*'*')
                        print()
                        print(50*'*')
                        print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                        print(50*'*')
                        print()
                        while True:    
                            D=input('Enter The ID Of Ride Which You Want To Book :- ')
                            print()
                            
                            if b.loc[0,'ID']==D:
                                bill40=b.loc[0,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill40=R*bill40
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[1,'ID']==D:
                                bill41=b.loc[1,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill41=R*bill41
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[2,'ID']==D:
                                bill42=b.loc[2,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill42=R*bill42
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[3,'ID']==D:
                                bill43=b.loc[3,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill43=R*bill43
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[4,'ID']==D:
                                bill44=b.loc[4,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill44=R*bill44
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[5,'ID']==D:
                                bill45=b.loc[5,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill45=R*bill45
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[6,'ID']==D:
                                bill46=b.loc[6,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill46=R*bill46
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif b.loc[7,'ID']==D:
                                bill47=b.loc[7,'ADULT_PRICE(in Rs)']
                                R=int(input('Enter Number Of Tickets - '))
                                bill47=R*bill47
                                print()
                                print(50*'*')
                                print('Your Ticket Has Selected')
                                print()
                                print('Please Visit Billing Section For Getting Your Ticket')
                                print(50*'*')
                                print()
                                b=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\GROUND_SLIDES.csv')
                                print(50*'*')
                                print(b[['ID','NAME_OF_SLIDES','ADULT_PRICE(in Rs)']])
                                print(50*'*')
                                print()
                                print(50*'*')
                                print('Write G9 For Go Back To Main Menu Of Ground Slides ')
                                print(50*'*')
                                print()
                            elif D=='G9' or D=='g9':
                                break
                            else:
                                print()
                                print(50*'*')
                                print('INCORRECT ID')
                                print(50*'*')
                                print()
                        main_menu_of_groundslides()
                        break
                    else:
                        print(50*'*')
                        print('Sorry!You Are Not Eligible To Ride')
                        print(50*'*')
            elif a=='D' or a=='d':   
                break
            else:
                print()
                print(50*'*')
                print('Invalid Choice')
                print(50*'*')
                print()
                main_menu_of_groundslides() 
    elif ch=='4':
        def main_menu_of_admin():
            print()
            print(160*'♦️')
            print()
            print('''                                                          You Are Viewing The Main Menu Of Admin
                                                        ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
                                      
                                                                      1.Admin
                                                                      2.Back to Main Menu       
                  ''')
            print()
            print(160*'♦️')
            print()
        main_menu_of_admin()
        
        while True:
            y=input('Enter Your Choice : ')
            if y=='1':
                print()
                print(50*'*')
                print('You Are Welcome')
                print(50*'*')
                print()
                w=input('Enter Password : ')
                print()
                if w=='richu' or w=='sourabh':
                    def inside_main_menu():
                        print(160*'♦️')
                        print()
                        print('''                                                     You Are Viewing The Sub - Main Menu Of Admin 
                                                      ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
                                      
                                                             1.Update Customer Details
                                                             2.Delete Customer Details
			                                     3.Sorting Customer Details By Name (asc)
   		                                             4.Sorting Customer Details By Name (desc)
				                             5.Back To Main Menu Of Admin          
                            ''')
                        print()
                        print(160*'♦️')
                        print()
                    inside_main_menu()
                    while True:
                        print()
                        z=input('Enter Your Choice:- ')
                        print()
                        if z=='1':
                            while True:
                                DD=input('Do You Want To Update Customer Details(Y/N) : ')
                                print()
                                if DD=='Y' or DD=='y' :
                                    s1=pd.read_csv("E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv",index_col='ID')
                                    print(70*'*')
                                    print(s1[['CUSTOMER NAME','ADDRESS','CITY','STATE']])
                                    print(70*'*')
                                    print()
                                    s2=int(input('Enter ID Which You Want To Update :- '))
                                    print()
                                    s3=input('Enter New Customer Name :- ')
                                    print()
                                    s4=input('Enter New Address:-')
                                    print()
                                    s5=input('Enter New City :- ')
                                    print()
                                    s6=input('Enter New State:- ')
                                    print()
                                    s1.loc[s2,'CUSTOMER NAME']=s3
                                    s1.loc[s2,'ADDRESS']=s4
                                    s1.loc[s2,'CITY']=s5
                                    s1.loc[s2,'STATE']=s6
                                    s1.to_csv("E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv")
                                    print(50*'*')
                                    print('Record Successfully Updated.')
                                    print(50*'*')
                                    print()
                                    inside_main_menu()
                                    print()
                                    break
                                
                                elif DD=='N' or DD=='n' :
                                    print()
                                    inside_main_menu()
                                    print()
                                    break
                                else:
                                    print()
                                    print(50*'*')
                                    print('Invalid Choice ')
                                    print(50*'*')
                                    print()
                                    
                        elif z=='2':
                            while True:
                                print()
                                DD=input('Do You Want To Delete Customer Details(Y/N) : ')
                                print()
                                if DD=='Y'or DD=='y':
                                    l=pd.read_csv("E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv",index_col='ID')
                                    print(70*'*')
                                    print(l[['CUSTOMER NAME','CITY','STATE']])
                                    print(70*'*')
                                    print()
                                    q=int(input('Enter Customer ID:- '))
                                    print()
                                    l.drop([q],inplace=True)
                                    l.to_csv("E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv")
                                    print(50*'*')
                                    print('Deleted Successfully ')
                                    print(50*'*')
                                    print()
                                    inside_main_menu()
                                    print()
                                    break
                            
                                elif DD=='N'or DD=='n':
                                    print()
                                    inside_main_menu()
                                    print()
                                    break
                                else:
                                    print()
                                    print(50*'*')
                                    print('Invalid Choice ')
                                    print(50*'*')
                                    print()
                                    
                        elif z=='3':
                            print()
                            m=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv',index_col='ID')
                            m.sort_values(by='CUSTOMER NAME',ascending=True,inplace=True)
                            print(70*'*')
                            print(m[['CUSTOMER NAME','CITY','STATE']])
                            print(70*'*')
                            print()
                            inside_main_menu()
                            print()
                            
                        elif z=='4':
                            print()
                            n=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\CUSTOMER.csv',index_col='ID')
                            n.sort_values(by='CUSTOMER NAME',ascending=False,inplace=True)
                            print(70*'*')
                            print(n[['CUSTOMER NAME','CITY','STATE']])
                            print(70*'*')
                            print()
                            inside_main_menu()
                            print()
                            
                        elif z=='5':
                            print()
                            main_menu_of_admin()
                            print()
                            break
                        
                        else:
                            print()
                            print(50*'*')
                            print('Invalid Choice')
                            print(50*'*')
                            print()
                            inside_main_menu()
                            print()
                            
                else:
                    print()
                    print(50*'*')
                    print('Wrong password')
                    print(50*'*')
                    print()
                    main_menu_of_admin()
                    print()
                    
            elif y=='2':
                print()
                break
            
            else:
                print()
                print(50*'*')
                print('Invalid Choice')
                print(50*'*')
                print()
                main_menu_of_admin()
                print()
    elif ch=='5':
        def main_menu_of_graph():
            print()
            print(160*'♦️')
            print()
            print("""                                                 You Are Viewing The Main Menu Of Data Visualization
                                               ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

                                                        A)Year Wise Visitors(Last 11 Years)
                                                        B)Year Wise Rating
                                                        C)Age Wise Visitors 
                                                        D)Back To Main Menu
                        """)
            print(160*'♦️')
            print()
        main_menu_of_graph()
        
        
        while True:
            x=input('Enter Your Choice:- ')
            if x=='A' or x=='a' :
                f=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\VISITOR.csv')
                g=f['YEARS']
                h=f['VISITORS'] 
                font={'family':'Showcard Gothic','weight':'bold'}
                plt.plot(g,h,color='blue',linewidth=1,marker='o',markersize=5,markeredgecolor='black',linestyle='dashed')
                plt.xlabel('YEAR',fontdict=font,color='crimson',fontsize=15)
                plt.ylabel('VISITORS',fontdict=font,color='crimson',fontsize=15)
                plt.xticks(g,color='teal',fontfamily='Copperplate Gothic Bold')
                plt.yticks([45000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000],color='teal',fontfamily='Copperplate Gothic Bold')
                plt.title('YEAR_WISE_VISITORS',fontdict=font,color='midnightblue',fontsize=18)
                plt.show()
                main_menu_of_graph()
                
            elif x=='B' or x=='b':
                f=pd.read_csv('E:\\12th PROJECT(DREAM PARK)\\VISITOR.csv')
                i=f['YEARS']
                j=f['RATINGS']
                font={'family':'Showcard Gothic','weight':'bold'}
                plt.barh(i,j,linewidth=2.3,height=0.5,color='gold',edgecolor='k')
                plt.xlabel('RATINGS',fontdict=font,color='crimson',fontsize=15)
                plt.ylabel('YEAR',fontdict=font,color='crimson',fontsize=15)
                plt.yticks(i,color='black',fontfamily='Copperplate Gothic Bold')
                plt.xticks(color='black',fontfamily='Copperplate Gothic Bold')
                plt.title('YEAR_WISE_RATING',fontdict=font,color='navy',fontsize=18)
                plt.show()
                main_menu_of_graph()
                
            elif x=='C' or x=='c':
                age=[9,18,27,36,45]
                visitor=[9,19,28,43]
                font={'family':'Showcard Gothic','weight':'bold'}
                plt.hist(visitor,bins=age,weights=[25000,30000,15000,11500],edgecolor='red',color='tomato',linewidth=2)
                plt.yticks(color='black',fontfamily='Copperplate Gothic Bold')
                plt.xticks(age,color='black',fontfamily='Copperplate Gothic Bold')
                plt.xlabel('AGE_GROUP',fontdict=font,color='crimson',fontsize=15)
                plt.ylabel('NUMBER_OF_VISITORS',fontdict=font,color='crimson',fontsize=10)
                plt.title('AGE_WISE_VISITORS',fontdict=font,color='navy',fontsize=18)
                plt.show()
                main_menu_of_graph()
                
            elif x=='D' or x=='d':
                print()
                break
            
            else:
                print()
                print(50*'*')
                print('Invalid Choice')
                print(50*'*')
                print()
                main_menu_of_graph()
    
    elif ch=='6':
        while True:
            print()
            dd=input('Do You Want To Check Your Bill (Y/N) : ')
            print()
            if dd=='Y' or dd=='y':
                print(140*'*')
                print()
                print('                                                       BILL   ')
                print('                                                      ------')
                print()
                print('                                       Your Total Amount Of Air Slide  ')
                t=bill+bill1+bill2+bill3+bill4+bill5+bill6+bill7+bill8+bill9+bill10+bill11+bill12+bill13+bill14+bill15
                print('                                        RS',t,'(Including GST & All Other Taxes)')
                print()
                print('                                       Your Total Amount Of Water Slide  ')
                M=bill16+bill17+bill18+bill19+bill20+bill21+bill22+bill23+bill24+bill25+bill26+bill27+bill28+bill29+bill30+bill31
                print('                                        RS',M,'(Including GST & All Other Taxes)')
                print()
                print('                                       Your Total Amount Of Ground  Slide  ')
                Q=bill32+bill33+bill34+bill35+bill36+bill37+bill38+bill39+bill40+bill41+bill42+bill43+bill44+bill45+bill46+bill47
                print('                                       RS',Q,'(Including GST & All Other Taxes)')
                print()
                print('                                       Your Total Amount Of Packages ')
                print()
                print('                                       Total Amount')
                print('                                       RS',t+M+Q,'(Including GST & All Other Taxes)')
                print()
                print(140*'*')
                print('Our Employee Call You For Recieving Payment')
                print(140*'*')
                print()
                print(140*'*')
                
            elif dd=='N'or dd=='n':
                print()
                break
                
            else:
                print()
                print(50*'*')
                print('Invalid Choice')
                print(50*'*')
                print()
            
    elif ch=='7':
        print()
        print()
        print('''
                                          ️   ️   ♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️️️
                                                     ♦️                                                          ♦️                          
                                                     ♦️  Thanks  For  Visiting  Us  ,  See  You  Soon  Again  !  ♦️
                                                     ♦️                                                          ♦️
                                                     ♦️                Have  A  Wonderful  Day!                  ♦️
                                                     ♦️                                                          ♦️
                                            ️       ♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦️♦ ♦   ♦️️
            ''')  
        print()
        break
    
    else:
        print()
        print(50*'*')
        print('Please Choose The Coreect Wish')
        print(50*'*')
        print()













    
        
   
    

