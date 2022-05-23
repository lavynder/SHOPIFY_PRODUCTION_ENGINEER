# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class BaseFunctions:
    
# =============================================================================
#     THIS CLASS DEFINES THE MOST BASIC FUNCTIONS THAT THE CLASS InputFunctions 
#     WILL INHERIT
# =============================================================================
    
    def baseInput(self, data):
# =============================================================================
#         ASKS  FOR USER INPUT, THE DATA REQUESTED SHOULD BE PASSED INTO THE 
#         FUNCTION AS A STRING. THIS WILL AUTOMATICALLY BE PUT INTO THE PRINT
#         STATEMENT THAT WILL ASK THE USER FOR THE DATA. 
# =============================================================================
        
        userData = input('PLEASE ENTER '+data+': ')
        
        # RETURNS THE ENTERED DATA AS A STRING
        return userData

    def blankInput_check(self, inputData):
# =============================================================================
#         THIS FUNCTION CHECKS WHETHER OR NOT THE USER TYPED ANYTHING IN.
# =============================================================================
        
        # IF THE USER DID NOT TYPE ANYTHING IN, RETURNS False, ELSE RETURN True
        if inputData == '':
            return False
        else:
            return True
        
    def infoConfirmation(self):
# =============================================================================
#         THIS FUNCTION ASKS THE USER TO CONFIRM WHETHER OR NOT THE INFORMATION 
#         THEY ENTERED IS CORRECT.
# =============================================================================
        
        # KEEPS THE USER IN A LOOP TO ENSURE VALID USER INPUT
        while True:
            
            # CAPITALIZES AND REMOVES LEADING AND TRAILING SPACES TO ACCOUNT
            # FOR VARIABILITY IN USER INPUT
            userCheck = input('IS THIS INFORMATION CORRECT[Y/N]? :').upper().strip()
            
            # IF USER CONFIRMS DATA RETURNS True, IF USER DENIES DATA RETURNS False
            # ELSE NOTIFIES USER ABOUT WRONG INPUT AND GOES BACK TO THE START OF THE LOOP
            if userCheck == 'Y':
                return True
            elif userCheck == 'N':
                print('PLEASE RE-ENTER THE REQUIRED INFORMATION')
                return False
            else:
                print('INVALID INPUT! PLEASE ENTER Y OR N')
            
        
        
    def tryAgain(self):
# =============================================================================
#         THIS FUNCTION CHECKS FOR ERRORS WITHIN THE USER'S INPUT
# =============================================================================
    
        # KEEPS THE USER IN A LOOP TO ENSURE VALID USER INPUT
        while True:
            # CAPITALIZES AND REMOVES LEADING AND TRAILING SPACES TO ACCOUNT
            # FOR VARIABILITY IN USER INPUT
            userCheck = input('WOULD YOU LIKE TO TRY AGAIN? [Y/N]? :').upper().strip()
            
            # IF USER WANTS TO RE-ENTER THE INFORMATION, RETURNS True 
            # IF USER WANTS TO GO BACK TO MENU, RETURNS False
            # ELSE NOTIFIES USER ABOUT WRONG INPUT AND LOOPS BACK
            if userCheck == 'Y':
                return True
            elif userCheck == 'N':
                return False
            else:
                print('INVALID INPUT! PLEASE ENTER Y OR N')
        
class InputFunctions(BaseFunctions):
    
    def dataInput(self, data):     
# =============================================================================
#         THIS FUNCTION GETS USER INPUT AND ENSURES THAT THE USER'S INPUT IS NOT
#         BLANK. IF THE USER'S INPUT IS BLANK, THEN THE USER IS ASKED TO 
#         RE-ENTER THEIR ANSWER.
#          
#         THE data PARAMETER IS THE INFORMATION THAT IS REQUIRED, AND WILL BE PUT
#         INTO THE PROMPT WHEN ASKING FOR USER INPUT. data SHOULD BE A STRING.
# =============================================================================

        
        # KEEPS THE USER IN A WHILE LOOP TO ENSURE A VALID USER INPUT
        while True:
            # STRIPS THE LEADING AND TRAILING SPACES TO ACCOUNT FOR USER INPUT VARIABLITY
            inputData = BaseFunctions().baseInput(data).strip()
            
            # IF THE USER INPUT IS VALID, THEN THE FUNCTION RETURNS inputData
            # ELSE NOTIFIES THE USER AND GOES BACK TO THE START OF THE LOOP
            if BaseFunctions().blankInput_check(inputData):
                return inputData
            else:
                print('YOU HAVEN\'T ENTERED ANTHING!')
                
    def integerInput(self, num):
# =============================================================================
#         THIS FUNCTION GETS USER INPUT AND CONVERTS IT INTO AN INTEGER.
#         IT ALSO ENSURES THAT THE USER'S INPUT IS NOT BLANK, AND MAKES SURE THAT
#         THE USER'S INPUT IS IN A VALID FORMAT TO BE CONVERTED. 
#         
#         THE num PARAMETER IS THE INFORMATION THAT IS REQUIRED, AND WILL BE PUT
#         INTO THE PROMPT WHEN ASKING FOR USER INPUT. num SHOULD BE A STRING.
# =============================================================================
        
        # KEEPS THE USER IN A WHILE LOOP TO ENSURE A VALID USER INPUT
        while True:
            # STRIPS THE LEADING AND TRAILING SPACES TO ACCOUNT FOR USER INPUT VARIABLITY
            inputNum = BaseFunctions().baseInput(num).strip()
            
            # IF THE USER INPUT IS NOT BLANK, THEN IT TRIES TO CONVERT IT INTO A DATETIME FORMAT
            # ELSE NOTIFIES THE USER AND GOES BACK TO THE START OF THE LOOP
            if BaseFunctions().blankInput_check(inputNum):
                
                # CONVERTS THE USER INPUT INTO AN INTEGER, AND RETURN THE CONVERTED INTEGER
                # ELSE IT NOTIFIES THAT THE INPUT WAS NOT VALID, AND IT GOES BACK
                # TO THE START OF THE LOOP                
                try:
                    num_converted = int(inputNum)
                    return num_converted
                except:
                    print('PLEASE ENTER THE NUMBER AS AN INTEGER')
            else:
                print('YOU HAVEN\'T ENTERED ANTHING!')