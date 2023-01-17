import sys
import os
from datetime import datetime
from PIL import Image, ExifTags

sys.path.insert(1, "D:/Users/Vlad/Projects/Applications/FOXY-FUNCTIONS")
from FoxyFunctions import ff

class main:
    def __init__(self):
        # create a foxy object
        self.ff = ff("PHOTO-VIDEO ALBUM ORGANIZER", "2.0")

        # load settings
        self.settings = self.ff.get_settings()

        # display main menu
        self.display_menu()
    
    def display_menu(self):
        # display header
        self.ff.display_header()

        # display main menu
        main_menu = (("START", self.start), ("SETTINGS", self.set_settings), ("HELP", self.help), ("EXIT", self.exit))
        self.ff.display_menu("MAIN MENU", main_menu)
    
    def start(self):
        # set global variables
        NEWFILES = self.settings["NEW FILES LOCATION"]
        PHOTOALBUM = self.settings["PHOTO ALBUM"]
        VIDEOALBUM = self.settings["VIDEO ALBUM"]

        # go over new files folder
        print("GETTING NEW FILES:")
        SN = 0
        for root, dirs, files in os.walk(NEWFILES):
            for file in files:
                file_name = root+"/"+file
                file_extension = os.path.splitext(file_name)[1]
                
                #PHOTOS
                try:
                    with Image.open(file_name) as img:
                        exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
                    datetime_stmp = exif['DateTime']
                    photo = True
                except:
                    photo = False
                    pass
                
                #VIDEOS
                try:
                    if not photo:
                        datetime_stmp = datetime.fromtimestamp(os.path.getmtime(file_name)).strftime('%Y:%m:%d %H:%M:%S')
                except:
                    pass
                
                datetime_stmp = datetime_stmp.split(" ")
                date_stamp = datetime_stmp[0].split(":")
                time_stamp = datetime_stmp[1].split(":")
                YYYY = date_stamp[0]
                MM = date_stamp[1]
                DD = date_stamp[2]
                HO = time_stamp[0]
                MI = time_stamp[1]
                SE = time_stamp[2]
                tmp_name = "%s-%s-%s %s%s%s %s" % (YYYY,MM,DD,HO,MI,SE,str(SN).zfill(4))
                if photo:
                    album = PHOTOALBUM
                else:
                    album = VIDEOALBUM
                dist_fold = "%s/%s/%s.%s" % (album,YYYY,MM,YYYY)
                new_name = "%s/%s%s" % (dist_fold, tmp_name, file_extension)
                
                if not os.path.isdir(dist_fold):
                    self.ff.indexed_print("New folder created: "+dist_fold)
                    os.makedirs(dist_fold)
                
                if not os.path.exists(new_name):
                    # self.ff.indexed_print("From: "+file_name)
                    self.ff.indexed_print(new_name)
                    os.rename(file_name, new_name)
                SN += 1

        # go back to main menu
        input("DONE >")
        self.display_menu()
    
    def edit(self):
        # edit script file
        os.popen("script.txt")
        
        # go back to main menu
        self.display_menu()

    def set_settings(self):
        # set new settings
        self.ff.set_settings(self.settings)

        # go back to main menu
        self.display_menu()
    
    def help(self):
        # display readme file
        self.ff.help()

        # go back to main menu
        self.display_menu()
    
    def exit(self):
        # exit the program
        self.ff.exit()

main()