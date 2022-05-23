# -*- coding: utf-8 -*-

# MODULES CREATED AND IMPORTED
from baseFunctions import InputFunctions as bf
from database import Database as db
from API import Weather_API as api

# PRE-BUILT MODULES IMPORTED
from dataclasses import dataclass

@dataclass
class main(bf, db, api):
# =============================================================================
#     THIS METHOD DEFINES THE MAIN FLOW AND LOGIC OF THE PROGRAM. IT INHERITS THE 
#     Database, InputFuctions, AND Weather_API CLASSES FROM THE IMPORTED MODULES, 
#     WHICH WERE ALSO CREATED. 
#     
#     THE API KEY MUST BE PASSED THROUGH THE CLASS AS A STRING. 
#     
#     THE MODULE dataclasses IS ALSO USED.  
# =============================================================================
    
    # SETS THE THE API KEY
    api_key: str
    
    def main(self):
        # CREATES THE TABLES WITHIN THE INVENTORY SYSTEM
        # IF THE FILE DOESN'T EXIST, THEN A FILE IS CREATED
        db()._createTable('inventory_city')
        
        # INFORMS THE USER THAT THE PROGRAM HAS STARTED
        print('INVENTORY SYSTEM')
        
        # PUTS THE USER WITHIN A WHILE LOOP FOR THE MAIN MENU SYSTEM
        while True:
            
            # PRINTS THE OPTIONS FOR THE USER TO CHOOSE FROM
            print(
                '''MENU:
    1. ADD NEW ITEM
    2. UPDATE ITEM
    3. CHANGE CITY
    4. VIEW ITEM/CITY
    5. DELETE ITEM
    6. EXIT''')

            # ASKS THE USER TO CHOOSE AN OPTION            
            menuInput = bf().integerInput('MENU NUMBER')
            
            # MAIN MENU OPTION TO BRING USER TO 'ADD MENU'
            if menuInput == 1:
                
                
                while True:
                    # SHOWS THE USER THE POSSIBLE OPTIONS WITHIN THIS MENU 
                        while True:
                            
                            # ASKS FOR ITEM INFORMATION
                            item = bf().dataInput('ITEM SERIAL NUMBER').upper() 
                            desc = bf().dataInput('ITEM DESCRIPTION').upper()
                            city = bf().dataInput('CITY').capitalize()
                            
                            # SHOWS THE USER THE INFORMATION THAT THEY ENTERED
                            print('INFO ENTERED:')
                            print('ITEM SERIAL NUMBER:', item)
                            print('ITEM DESCRIPTION:', desc)
                            print('CITY:', city)
                            
                            # IF THE USER CONFIRMS THE INFORMATION, THEN THE ITEM IS ADDED
                            if bf().infoConfirmation():
                                cityData = db()._view_location(city, 'inventory_city')
                                
                                # CHECK VALIDITY OF CITY
                                if cityData == None:
                                    # IF CITY DOES NOT EXIST, NOTIFIES USER
                                    print('THIS CITY IS NOT AVAILABLE. IF YOU WISH TO SEE ALL CITIES,'
                                          ' PLEASE GO TO MENU OPTION 4')
                                    
                                    # SENDS USER BACK TO MAIN MENU
                                    break
                                
                                else:
                                    
                                    # FINDS cityID AND ADDS ALONG WITH item AND desc
                                    cityID = cityData[0]
                                    db()._add_item(item, desc, cityID, 'inventory_city')
                               
                                # RETURNS THE USER TO THE MAIN MENU
                                break
                            
                            # IF THE USER DOES NOT WANT TO TRY AGAIN, NOTHING IS ADDED
                            # THE USER IS THEN SENT BACK TO THE MAIN MENU
                            elif not bf().tryAgain():
                                
                                # RETURNS THE USER TO THE MAIN MENU
                                break
                        
                        # RETURNS THE USER TO THE MAIN MENU     
                        break
                        
              
            # MAIN MENU OPTION TO BRING USER TO UPDATE MENU
            elif menuInput == 2:
                # ASKS USER WHICH ITEM'S INFORAMTION THEY WANT TO UPDATE
                item = bf().dataInput('ITEM YOU WISH TO UPDATE').upper()
                
                # CHECKS TO SEE IF THE ITEM EXISTS
                item_check = db()._view_item(item, 'inventory_city')
                if item_check == None:
                    # IF IT DOES NOT EXIST, THE USER IS NOTIFIED AND SENT TO THE MAIN MENU
                    print('THIS ITEM IS NOT ON THE INVENTORY LIST')
                    print('PLEASE ADD THE ITEM FIRST USING MENU OPTION 1')
                    
                
                # IF THE ITEM DOES EXIST, THE INFORMATION IS UPDATED
                else:
                    # ASKS THE USER FOR THE UPDATED ITEM DESCRIPTION
                    desc_updated = bf().dataInput('THE NEW DESCRIPTION')
                    city_updated = bf().dataInput('THE NEW CITY').capitalize()
                    
                    # CHECKS VALIDITY OF CHOSEN NEW CITY
                    cityData = db()._view_location(city_updated, 'inventory_city')
                    if cityData == None:
                                    # IF CITY DOES NOT EXIST, NOTIFIES USER
                                    print('THIS CITY IS NOT AVAILABLE. IF YOU WISH TO VIEW ALL CITIES,'
                                          ' PLEASE GO TO MENU OPTION 4')
                                
                    else:
                        
                        # UPDATES ITEM INFORMATION
                        cityID = cityData[0]
                        print(cityID)
                        db()._update_item(desc_updated, item, cityID, 'inventory_city')
                        
                        # TELLS USER THAT THE ITEM HAS BEEN UPDATED
                        print('THIS ITEM\'S INFORMATION HAS BEEN UPDATED')
           
            # MENU OPTION TO CHANGE A SET CITY
            elif menuInput == 3:
                
                # ASKS THE USER FOR CITY THEY WANT TO CHANGE, THE NEW CITY, AND THE COUNRTY OF THE NEW CITY
                city_change = bf().dataInput('THE CITY YOU WISH TO CHANGE').capitalize()
                city_new = bf().dataInput('THE CITY THAT WILL REPLACE IT').capitalize()
                country_new = bf().dataInput('THE COUNTRY THE CITY IS IN').capitalize()
                
                # WARNS THE USER ABOUT THE EFFECTS OF CHANGING A CITY
                print('WARNING: CHANGING THE CITY WILL AUTOMATICALLY TRANSFER ALL INVENTORY'
                      ' TO THE NEW CITY')
                
                # ASKS THE USER TO CONFIRM WHETHER OR NOT THIS CHANGE IS OK
                while True:
                    askUser = input('IS THIS OK? [Y/N]').upper()
                    
                    # IF THE USER RESPONDS WITH YES, THEN THE PROGRAM CHECKS CITY VALIDITY
                    if askUser == 'Y':
                        cityData = db()._view_location(city_change, 'inventory_city')
                        
                        if cityData == None:
                                        # IF CITY DOES NOT EXIST, NOTIFIES USER
                                        print('THE CITY YOU ARE TRYING TO CHANGE DOES NOT EXIST')
                                        print('TO SEE WHICH CITIES ARE AVAILABLE, PLEASE GO TO MENU OPTION 4')
                                        
                                        # SENDS USER BACK TO MAIN MENU
                                        break
                        
                        # IF THE CHOSEN CITY TO CHANGE IS VALID, THEN THE INFORMATION IS UPDATED         
                        else:
                            
                            # CHANGES CITY INFORMATION
                            cityID = cityData[0]
                            db()._change_city(cityID, city_new, country_new, 'inventory_city')
                       
                            # TELLS USER THAT CITY HAS BEEN CHANGED
                            print('THE CITY HAS BEEN CHANGED!')     
                       
                            # RETURNS THE USER TO THE MAIN MENU
                            break
                    
                    # IF THE USER CHANGES THEIR MIND, THEN THE CHANGE IS CANCELED
                    elif askUser == 'N':
                        print('NOT CHANGING CITY')
                        break
                    
                    # FOR INVALID USER INPUT
                    else:
                        print('INVALID INPUT!')
            
            # MAIN MENU OPTION TO BRING USER TO THE VIEW MENU            
            elif menuInput == 4:
                
                while True:
                    # SHOWS THE USER THE AVAILABLE OPTIONS
                    print(
                '''MENU:
    1. VIEW ITEM
    2. VIEW CITY
    3. VIEW ALL ITEMS
    4. VIEW ALL CITIES
    ''')
                    # ASKS THE USER TO CHOOSE AN OPTION
                    viewInput = bf().integerInput('MENU OPTION')
                    
                    # MENU OPTION TO VIEW AN ITEM IN THE INVENTORY 
                    if viewInput == 1:
                        
                        # ASKS THE USER WHICH ITEM THEY WISH TO VIEW
                        item = bf().dataInput('ITEM YOU WISH TO VIEW').upper()
                        
                        # RETIREVES INFORMATION
                        itemData = db()._view_item(item, 'inventory_city')

                        # IF THE ITEM DOESN'T EXIST, THE USER IF NOTIFIED AND SENT ABCK TO THE MAIN MENU
                        if itemData == None:
                            print('THIS ITEM IS NOT ON THE INVENTORY LIST')
                            print('PLEASE ADD THE ITEM FIRST USING MENU OPTION 1')
                            
                        # ELSE THE CITY THAT BELONGS TO THE ITEM IS FOUND   
                        else:
                            cityID = itemData[3]
                            city = db()._view_itemLocation(cityID, 'inventory_city')
                        
                            print('ITEM SERIAL NUMBER:', itemData[1])
                            print('ITEM DESCRIPTION:', itemData[2])
                            print(f'ITEM CITY: {city[1]}, {city[2]}')
                        
                        # RETURNS USER TO MAIN MENU
                        break
                     
                    # MENU OPTION TO VIEW A CITY
                    elif viewInput == 2:
                        
                        # ASKS USER WHICH LOCATION THEY WISH TO VIEW
                        location = bf().dataInput('CITY YOU WISH TO VIEW').capitalize()
                        
                        # RETRIEVES INFORMATION
                        locationData = db()._view_location(location, 'inventory_city')
                        
                        # IF THE LOCATION DOESN'T EXIST, THE USER IS NOTIFIED
                        # THEN THEY ARE SENT BACK TO THE MAIN MENU
                        if locationData == None:
                            print('THIS CITY IS NOT AVAILABLE')
                            print('PLEASE GO TO MENU OPTION 4 TO SEE ALL AVAILABLE CITIES')
                            
                        # ELSE THE INFORMATION IS DISPLAYED   
                        else:
                            # THE CITY AND COUNTRY INFORMATION NECESSARY FOR THE API IS CREATED
                            city_api = f'{locationData[1]},{locationData[2]}'
                            
                            # THE WEATHER INFORMATION IS SAVED
                            weather = api.get_weather(self.api_key, city_api)
                            
                            # THE INFORMATION ABOUT THE CITY IS DISPLAYED
                            print('CITY:', locationData[1])
                            print('COUNTRY', locationData[2])
                            print('\nCITY WEATHER:', weather[0])
                            print(f'TEMPERATURE: {weather[1]:.1f} C')
                            
                            # ALL AVAILABLE ITEMS IN THE CITY ARE DISPLAYED
                            print('\nITEMS AT LOCATION:')
                            item_list = db()._view_allItemsLocation(locationData[0], 'inventory_city')
                            for i in item_list:
                                print(f' - {i[1]}, {i[2]}')
                        
                        # RETURNS USER TO MAIN MENU
                        break
                    
                    # MENU OPTION TO SEE ALL ITEMS IN THE INVENTORY
                    elif viewInput == 3:
                        
                        # RETRIEVES ALL AVAILABLE INVENTORY INFORMATION
                        all_inventory = db()._view_all_inventory('inventory_city')
                        
                        # IF THE INVENTORY IS EMPTY, THE USER IS NOTIFIED AND SENT BACK TO THE MAIN MENU
                        if all_inventory == []:
                            print('THE DATABASE IS EMPTY')
                        
                        # ELSE THE INFORMATION IS PRINTED
                        else:
                            item_list = [item[1] for item in all_inventory]
                            desc_list = [item[2] for item in all_inventory]
                            city_list = [item[3] for item in all_inventory]
                            
                            for i in range(len(item_list)):
                                city = db()._view_itemLocation(city_list[i], 'inventory_city')
                                print(f'- {item_list[i]}\t\tDESCRIPTION: {desc_list[i]}\t\tCITY: {city[1]}')
                       
                        # RETURNS USER TO MAIN MENU        
                        break

                                
                    # MENU OPTION TO SEE ALL 5 CITIES            
                    elif viewInput == 4:
                        
                        # RETIREVES ALL AVAILABLE LOCATION INFORMATION
                        raw_locationsData = db()._view_all_locations('inventory_city')
                        
                        # CREATES A LOCAL LIST TO HOLD ALL THE LOCATIONS
                        location_list = [item[1] for item in raw_locationsData]
                        
                        # PRINTS ALL LOCATIONS
                        for i in location_list:
                            print(f'- {i}')
                        
                        # SENDS USER BACK TO THE MAIN MENU   
                        break
                                
                    
                    # IF THE USER ENTERS INVALID INPUT
                    else:
                        print('INVALID INPUT! PLEASE ENTER 1, 2, 3, OR 4')
                
            # MAIN MENU OPTION TO BRING USER TO THE DELETE MENU
            elif menuInput == 5:
                 # ASKS USER WHICH ITEM THEY WANT TO DELETE
                 item = bf().dataInput('ITEM SERIAL NUMBER').upper()
                
                 # DELETES ITEM
                 db()._del_item(item, 'inventory_city')
                
                 # NOTIFIES USER
                 print('ITEM HAS BEEN DELETED')
                
                 # RETURNS USER TO MAIN MENU
                    
                
                
            # IF THE USER WISHES TO END THE PROGRAM
            elif menuInput == 6:
                print('EXITING PROGRAM')
                break
            
            # IF THE USER ENTERS INVALID INPUT
            else:
                print('INVALID INPUT, TRY AGAIN')
                        
                        
# TEST OBJECT CREATED 
# API IS THERE FOR TESTING, BUT WILL BE DELETED FOR SECURITY AND PRIVACY REASONS    
test = main('aa47a22022cecde41c5c2f7773388bbf')
test.main()