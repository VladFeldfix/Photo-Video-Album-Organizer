#######################################################################################################################################################

"""
FOXY FUNCTIONS v2.3

To add FoxyFunctions to your code put the file FoxyFunxtions.py in the same folder as your file and write: 
    from FoxyFunctions import ff
Then initialize foxyfunctions as following 
    ff("your program name", "your program version")

function you can interact with:
1. ff(program_name, program_ver) initialization
    when initializing foxy-functions specify the name and revision of you app

2. display_menu(header, menu)
    the header is the name of the menu (for example: MAIN MENU, SETTINGS ect...)
    the menu is a list of tuples that specify the menu text and the function it is activating. (for example: [('f', f), ('g', g)])

3. display_header()
    displays the name and verstion of your program + the version of foxy functions you are using at the moment. no arguments needed
    
4. display_line(line, leng)
    for example: line="hello world", leng=20 hello_world_________ where _ is an empty space not underscore

5. exit()
    finishes the program
    
6. error(text)
    displays an error message
    
7. get_input(text, type)
    text = input text for the user
    type = foxy functions in making sure that it gets legal input STR, INT, FLOAT

8. indexed_print(text)
    displays output with a line number

9. csv_to_list(filename)
    returns a list object made from all the lines in a csv file
    [[row1col1, row1col2, row1col3] , [row2col1, row2col2, row2col3] , [row3col1, row3col2, row3col3]]
"""

import sys
import os

class ff():
    def __init__(self, program_name, program_ver):
        self.version = "2.3"
        self.program_name = program_name
        self.program_ver = str(program_ver)
        self.LINE_NUMBER = 1

    # header for example: MAIN MENU, menu structure exmple: [('start', start), ('edit', edit), ('exit', exit)]
    def display_menu(self, header, menu):
        print(header)
        i = 0
        
        # display main menu items
        valid_selections = []
        for item in menu:
            i += 1
            num = str(i)
            valid_selections.append(num)
            print(num+". "+item[0])
        
        # get user input
        err = True
        while err:
            user_input = input("> ")
            if user_input in valid_selections:
                err = False
                call_function = menu[int(user_input)-1][1]
                call_function()
            else:
                self.error("INVALID INPUT")
    
    def display_header(self):
        os.system('cls') # clear screen
        display_expression = "-- "+self.program_name+" v"+self.program_ver+" ff"+self.version+" --"
        print("-"*len(display_expression))
        print(display_expression)
        print("-"*len(display_expression))
        
    def display_line(self, line, leng):
        spaces = leng - len(line)
        return line+" "*spaces
      
    def exit(self):
        input("DONE >")
    
    def error(self, text):
        input("ERROR! "+text+" >")
        sys.exit()
    
    def get_input(self, text, type):
        inp = input(text+" >")
        type = type.upper()
        if type == "INT":
            try:
                inp = int(inp)
            except:
                self.error("INVALID INPUT")
                self.get_input(text, type)
        elif type == "FLOAT":
            try:
                inp = float(inp)
            except:
                self.error("INVALID INPUT")
                self.get_input(text, type)
        return inp
    
    def indexed_print(self, text):
        print(str(self.LINE_NUMBER)+". "+text)
        self.LINE_NUMBER += 1

    def csv_to_list(self, filename):
        result = []
        filename = filename+".csv"
        try:
            file = open(filename, 'r', encoding="utf-8")
            lines = file.readlines()
            for line in lines:
                line = line.replace("\n", "")
                line = line.split(",")
                result.append(line)
            file.close()
            return result
        except:
            self.error("CAN'T OPEN FILE "+filename)
    
    def get_settings(self):
        result = {}
        try:
            file = open("settings.txt", "r", encoding='utf-8')
            lines = file.readlines()
            file.close()
            for line in lines:
                line = line.replace("\n", "")
                line = line.split(":")
                result[line[0]] = line[1]
        except:
            self.error("CAN'T OPEN FILE settings.txt")      
        return result
    
    def set_settings(self, settings):
        # display
        self.display_settings(settings)

        # get new
        print("\nCHANGE SETTINGS (OR LEAVE EMPTY TO AVOID CHNAGEING):")
        for key, value in settings.items():
            value = input(str(key)+" >") or value
            settings[key] = value
        
        # save to file
        file = open("settings.txt", "w", encoding='utf-8')
        for key, value in settings.items():
            file.write(str(key)+":"+str(value)+"\n")
        file.close()
    
    def display_settings(self, settings):
        print("SETTINGS:")
        # display
        for key, value in settings.items():
            print(str(key)+" --> "+str(value))

#######################################################################################################################################################