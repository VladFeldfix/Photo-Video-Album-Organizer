#PHOTO & VIDEO ALBUM ORGANIZER
import os
from datetime import datetime
from PIL import Image, ExifTags
from tinytag import TinyTag
import shutil
import FoxyFunctions as ff
FF = ff.FoxyFunctions()

class main:
    def __init__(s):
        #version control
        print("Photo & Video Album Organizer Version 1.1")

        #set global variables
        s.NEWFILES = None
        s.PHOTOALBUM = None
        s.VIDEOALBUM = None
        
        #get settings
        s.get_settings()

        #main menu
        s.main_menu()

    def get_settings(s):
        file = open("settings.txt", "a", encoding='utf-8')
        file = open("settings.txt", "r", encoding='utf-8')
        s.NEWFILES = file.readline().replace("\n","")
        s.PHOTOALBUM = file.readline().replace("\n","")
        s.VIDEOALBUM = file.readline().replace("\n","")
        file.close()
    
    def main_menu(s):
        FF.display_settings([
            ("NEW FILES LOCATION", s.NEWFILES),
            ("MY PHOTO ALBUM LOCATION", s.PHOTOALBUM),
            ("MY VIDEO ALBUM LOCATION", s.VIDEOALBUM)
        ])
        FF.display_menu("MAIN MENU:", [
            ("Get new files",s.get_new_files),
            ("Settings",s.settings),
            ("Exit",FF.exit)])

    def get_new_files(s,n):
        print("GETTING NEW FILES:")
        SN = 0
        for root, dirs, files in os.walk(s.NEWFILES):
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
                #except Exception as e:
                    photo = False
                    pass
                    #print("Error: %s" % (e))

                #VIDEOS
                try:
                    if not photo:
                        datetime_stmp = datetime.fromtimestamp(os.path.getmtime(file_name)).strftime('%Y:%m:%d %H:%M:%S')
                except:
                #except Exception as e:
                    pass
                    #print("Error: %s" % (e))
                
                #print(datetime_stmp)
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
                    album = s.PHOTOALBUM
                else:
                    album = s.VIDEOALBUM
                dist_fold = "%s/%s/%s.%s" % (album,YYYY,MM,YYYY)
                new_name = "%s/%s%s" % (dist_fold, tmp_name, file_extension)
                
                if not os.path.isdir(dist_fold):
                    print("New folder created:",dist_fold)
                    os.makedirs(dist_fold)
                
                if not os.path.exists(new_name):
                    print("From:", file_name)
                    print("To:", new_name)
                    os.rename(file_name, new_name)
                SN += 1
        print("DONE!")
        s.main_menu()

    def settings(s,n):
        print("\nSETTINGS:")
        s.NEWFILES = input("Enter New files location: >") or s.NEWFILES
        s.PHOTOALBUM = input("Enter My photos album location: >") or s.PHOTOALBUM
        s.VIDEOALBUM = input("Enter My video album location: >") or s.VIDEOALBUM
        file = open("settings.txt", "w", encoding='utf-8')
        file.write(s.NEWFILES+"\n")
        file.write(s.PHOTOALBUM+"\n")
        file.write(s.VIDEOALBUM+"\n")
        file.close()
        s.main_menu()

main()