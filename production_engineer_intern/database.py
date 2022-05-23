# -*- coding: utf-8 -*-


import sqlite3 
from dataclasses import dataclass

# =============================================================================
# THIS MODULE DEFINES THE CLASSES THAT INTERACT WITH THE SQlite3 DATABASE SYSTEM
# =============================================================================

@dataclass
class Database:
# =============================================================================
#     THIS CLASS DEFINES HOW THE MAIN FILE WILL INTERACT WITH THE DATABASE
#     USING THE SQlite3 MODULE.
#
#     THE commit() COMMAND ISN'T NEEDED WITH THE PYTHON COMMAND with TO STORE
#     INFORMATION WITHIN THE DATABASE.
#     
#     THE CONNECTIONS ARE OPEN AND CLOSED LOCALLY WITHIN THE FUNCTIONS FOR 
#     BETTER PRIVACY AND SECURITY.
#
#     ADDITIONALLY, ALL THE METHODS ARE PROTECTED SO THAT THEY CANNOT BE ACCESSED
#     FROM OUTSIDE THE METHOD, BUT CAN STIL BE INHERITED.
# =============================================================================

    
    
    def _createTable(self, databaseName):       
# =============================================================================
#         THIS METHOD DEFINES HOW THE MODULE CREATES THE TABLES WITHIN THE DATABASE.
#         
#         THREE TABLES ARE CREATED: 
#             - THE inventory TABLE HOLDS THE ITEM SERIAL NUMBER AND THE
#             ITEM DESCRIPTION. ALL ITEMS MUST BE UNIQUE, SO serial IS THE 
#             PRIMARY KEY
#             - THE locations TABLE HOLDS THE AVAILABLE LOCATIONS, AND A DESCRIPTION
#             OF THE LOCATION. ALL LOCATIONS MUST BE UNIQUE, SO location IS THE
#             PRIMARY KEY 
#             - THE stocks TABLE CARRIES HOLDS THE AVAILABLE LOCATIONS AND THE 
#             CORRESPONDING ITEMS, AND VICE VERSA. IT ALSO HOLDS THE AMOUNT OF 
#             ITEMS ARE AT THE CORRESPONDING LOCATION. BOTH serial AND location
#             ARE FOREIGN KEYS, CORRESPONDING TO THE inventory AND locations
#             TABLES RESPECTIVELY
# =============================================================================
        
        
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()

        with conn:            
            
            # CREATES THE locations TABLE WITHIN THE DATABASE
            try:
                c.execute('''CREATE TABLE cities(        
                                cityID integer,            
                                city text,
                                country text,
                                PRIMARY KEY(cityID)
                                )''')
                
                # WHEN FIRST CREATING THE DATABASE, THESE ARE THE 5 DEFAULT CITIES
                c.execute('''INSERT INTO cities(city, 
                                                country) 
                              VALUES('Toronto','Canada'), 
                                  ('Amsterdam','Netherlands'),
                                 ('Berlin', 'Germany'), 
                                 ('Rome', 'Italy'), 
                                 ('Boston', 'US')
                                 
                              ''')
            
            # IF THE TABLE ALREADY EXISTS, THEN THE USER WILL BE NOTIFIED
            except sqlite3.OperationalError:
                print('THE locations DATABASE TABLE ALREADY EXISTS')   
            
            # IF THE TABLE CANNOT BE CREATED, THEN THE USER IS NOTIFIED
            except:
                print('AN ERROR OCCURED WHEN CREATING THE cities DATABASE TABLE')
                print('PLEASE ASK FOR HELP')
                
            # CREATES THE serial TABLE WITHIN THE DATABASE
            try:
                c.execute('''CREATE TABLE inventory(        
                            itemID integer,
                            item text,
                            desc text,
                            cityID integer,
                            PRIMARY KEY(itemID),
                            FOREIGN KEY(cityID) REFERENCES cities(cityID)
                            )''')
            
            # IF THE TABLE ALREADY EXISTS, THEN THE USER WILL BE NOTIFIED
            except sqlite3.OperationalError:
                print('THE inventory DATABASE TABLE ALREADY EXISTS')   
            
            # IF THE TABLE CANNOT BE CREATED, THEN THE USER IS NOTIFIED
            except:
                print('AN ERROR OCCURED WHEN CREATING THE inventory DATABASE TABLE')
                print('PLEASE ASK FOR HELP')
               
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
    
    
    
    def _add_item(self, item, desc, cityID, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW THE Database CLASS ADDS A NEW ITEM TO THE inventory
#         TABLE WITHIN THE SPECIFIED DATABASE.
#         
#         THREE VALUES ARE SAVED IN THE TABLE: 
#             - THE ITEM'S SERIAL NUMBER/NAME
#             - THE ITEM'S DESCRIPTION
#             - THE ITEM'S CORRESPONDING cityID
#             
#         THE ARGUMENTS PASSED THROUGH SHOULD ALL BE IN STRING FORMAT.
#         THE itemID UPDATES AUTOMATICALLY.
# =============================================================================

        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        
        with conn:
            # ADDS THE PASSED VALUES INTO THE inventory TABLE
            c.execute('''INSERT INTO inventory(item, desc, cityID) 
                        VALUES(
                        :item,
                        :desc,
                        :cityID
                        )''', {
                        'item': item,
                        'desc': desc,
                        'cityID': cityID
                        })
    
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
          
                 
    def _update_item(self, desc, item, cityID, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW THE Database CLASS UPDATES ITEM INFORMATION.
#         
#         THE INFORMATION THAT CAN BE UPDATED IS THE ITEM'S DESCRIPTION AND CITY.
#         
#         ALL ARGUMENTS SHOULD BE PASSED AS STRINGS.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            # UPDATES THE inventory TABLE WITHIN THE SPECIFIED DATABASE
            c.execute('''UPDATE inventory SET desc = :desc, cityID = :cityID 
                      WHERE item = :item''', {
                                'desc': desc,
                                'cityID': cityID,
                                'item': item
                                })
                      
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
    
    def _change_city(self, cityID, city, country, databaseName):
# =============================================================================
#         THIS METHOD ALLOWS THE USER TO CHANGE ONE OF THE 5 PRESET CITIES.
#         
#         ALL ARGUMENTS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
# CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            # UPDATES THE cities TABLE WITHIN THE SPECIFIED DATABASE
            c.execute('''UPDATE cities SET city = :city, country = :country 
                      WHERE cityID = :cityID''', {
                                'city': city,
                                'country': country, 
                                'cityID': cityID})
                      
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
    
    def _view_item(self, item, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW A USER CAN VIEW A SPECIFIC ITEM'S INFORMATION.
#         THIS METHOD CAN ALSO BE USED TO VERIFY IF THE ITEM IS WITHIN THE 
#         DATABASE'S INVENTORY.
#         
#         THE METHOD RETURNS THE INFORMATION IN THE FORM OF A TUPLE.
#         IF NO ITEM IS FOUND, THEN THE DATA TYPE None IS RETURNED. 
#         
#         ALL THE PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS THE DATASET
        c.execute('''SELECT * FROM inventory 
                  WHERE item = :item 
                  ''',
                  {'item': item})
        
        # SAVES THE TUPLE LOCALLY
        dataSet =  c.fetchone()
    
        # CLOSES CONNECTION TO THE DATABASE
        conn.close()
        
        # IF A DATASET IS FOUND, THE dataSet RETURNS A TUPLE
        # ELSE IT RETURNS None
        return dataSet
    
    def _view_itemLocation(self, cityID, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW A USER CAN FIND AN ITEM'S LOCATION.
#         THIS METHOD CAN ALSO BE USED TO VERIFY IF THE LOCATION IS WITHIN THE 
#         DATABASE'S cities TABLE. THIS USES THE CityID, INSTEAD OF city NAME.
#         
#         THE METHOD RETURNS THE INFORMATION IN THE FORM OF A TUPLE.
#         IF NO ITEM IS FOUND, THEN THE DATA TYPE None IS RETURNED. 
#         
#         ALL THE PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS THE DATASET
        c.execute('''SELECT * FROM cities 
                  WHERE cityID = :cityID 
                  ''',
                  {'cityID': cityID})
        
        # SAVES THE TUPLE LOCALLY
        dataSet =  c.fetchone()
    
        # CLOSES CONNECTION TO THE DATABASE
        conn.close()
        
        # IF A DATASET IS FOUND, THE dataSet RETURNS A TUPLE
        # ELSE IT RETURNS AN EMPTY LIST 
        return dataSet
    
    def _view_allItemsLocation(self, cityID, databaseName):
# =============================================================================
#         THIS METHOD IS USED TO RETURN ALL INVENTORY INFORMATION WITHIN THE inventory TABLE.
#         THE INFORMATION IS SORTED WITHIN THE FUNCTION, AND IS RETURNED AS
#         TUPLES NESTED WITHIN A LIST. 
#         
#         FOR EXAMPLE: [('ITEM1', 'DESC1'), ('ITEM2', 'DESC2')]
#         
#         IF THERE IS NO INVENTORY, THEN AN EMPTY LIST IS RETURNED. 
#         
#         ALL PARAMETERS SHOULD BE IN STRING FORMAT, EXCEPT cityID, WHICH MUST BE AN INTEGER 
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS THE DATASET
        c.execute('''SELECT * FROM inventory 
                  WHERE cityID = :cityID 
                  ''',
                  {'cityID': cityID})
        
        # SAVES THE LIST LOCALLY
        dataSet =  c.fetchall()
    
        # CLOSES CONNECTION TO THE DATABASE
        conn.close()
        
        # IF A DATASET IS FOUND, THE dataSet RETURNS A LIST
        # ELSE IT RETURNS AN EMPTY LIST
        return dataSet
    
    def _view_location(self, location, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW A USER CAN VIEW A SPECIFIC LOCATION'S INFORMATION.
#         THIS METHOD CAN ALSO BE USED TO VERIFY IF THE LOCATION IS WITHIN THE 
#         DATABASE'S cities TABLE.
#         
#         THE METHOD RETURNS THE INFORMATION IN THE FORM OF A TUPLE.
#         IF NO ITEM IS FOUND, THEN THE DATA TYPE None IS RETURNED. 
#         
#         ALL THE PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS THE DATASET
        c.execute('''SELECT * FROM cities 
                  WHERE city = :city 
                  ''',
                  {'city': location})
        
        # SAVES THE TUPLE LOCALLY
        dataSet =  c.fetchone()
    
        # CLOSES CONNECTION TO THE DATABASE
        conn.close()
        
        # IF A DATASET IS FOUND, THE dataSet RETURNS A TUPLE
        # ELSE IT RETURNS None
        return dataSet
    
    
    
    def _view_all_inventory(self, databaseName):
# =============================================================================
#         THIS METHOD IS USED TO RETURN ALL INVENTORY INFORMATION WITHIN THE inventory TABLE.
#         THE INFORMATION IS SORTED WITHIN THE FUNCTION, AND IS RETURNED AS
#         TUPLES NESTED WITHIN A LIST. 
#         
#         FOR EXAMPLE: [('ITEM1', 'DESC1'), ('ITEM2', 'DESC2')]
#         
#         IF THERE IS NO INVENTORY, THEN AN EMPTY LIST IS RETURNED. 
#         
#         ALL PARAMETERS SHOULD BE IN STRING FORMAT. 
# =============================================================================
        
        
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS ALL ITEMS IN THE inventory TABLE AND SORTS THEM 
        # ALPHABETICALLY ACCORDING TO ITEM SERIAL NUMBER
        c.execute('''SELECT * FROM inventory 
                  ORDER BY item''')
        
        # SAVES THE LIST LOCALLY
        dataSet =  c.fetchall()
        
        # RETURNS THE DATASET. IF THERE ARE NO ITEMS, THEN AN EMPTY LIST IS RETURNED
        return dataSet
    
    
    def _view_all_locations(self, databaseName):
# =============================================================================
#         THIS METHOD IS USED TO RETURN ALL LOCATION INFORMATION WITHIN THE locations TABLE.
#         THE INFORMATION IS SORTED WITHIN THE FUNCTION, AND IS RETURNED AS
#         TUPLES NESTED WITHIN A LIST. 
#         
#         FOR EXAMPLE: [('LOCATION1', 'DESC1'), ('LOCATION2', 'DESC2')]
#         
#         IF THERE ARE NO AVAILABLE LOCATIONS, THEN None IS RETURNED. 
#         
#         ALL PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        
        # FINDS ALL ITEMS IN THE locations TABLE AND SORTS THEM 
        # ALPHABETICALLY ACCORDING TO LOCATION
        c.execute('''SELECT * FROM cities 
                  ORDER BY cityID''')
        
        # SAVES THE LIST LOCALLY
        dataSet =  c.fetchall()
        
        # RETURNS THE DATASET. IF THERE ARE NO LOCATIONS, THEN AN EMPTY LIST IS RETURNED
        return dataSet
                      
    
        
    def _del_item(self, item, databaseName):
# =============================================================================
#         THIS METHOD DELETES A SPECIFIED ITEM WITHIN THE DATABASE IN BOTH THE 
#         inventory AND stock TABLES. 
#         
#         ALL PARAMETERS SHOULD BE PASSED AS STRINGS.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            
            # DELETES THE item FROM THE inventory TABLE
            c.execute('''DELETE FROM inventory WHERE item = :item''', 
                                                      {'item': item})
            
        
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
        
