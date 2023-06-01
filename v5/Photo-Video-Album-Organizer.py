from SmartConsole import *
import os
from datetime import datetime
from PIL import Image, ExifTags

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("Photo Video Album Organizer", "5.0")

        # set-up main memu
        self.sc.main_menu["RUN"] = self.run

        # get settings
        self.get_settings()

        # test all paths
        self.sc.test_path(self.new_photos)
        self.sc.test_path(self.my_photo_album)
        self.sc.test_path(self.my_video_album)

        self.sc.start()
    
    def get_settings(self):
        # get settings
        self.new_photos = self.sc.get_setting("New files location")
        self.my_photo_album = self.sc.get_setting("My photo-album location")
        self.my_video_album = self.sc.get_setting("My video-album location")

    def run(self):
        self.get_settings()
        # go over new music folder
        SN = 0
        for root, dirs, files in os.walk(self.new_photos):
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
                    album = self.my_photo_album
                else:
                    album = self.my_video_album
                dist_fold = "%s/%s/%s.%s" % (album,YYYY,MM,YYYY)
                new_name = "%s/%s%s" % (dist_fold, tmp_name, file_extension)
                
                if not os.path.isdir(dist_fold):
                    self.sc.print("New folder created: "+dist_fold)
                    os.makedirs(dist_fold)
                
                if not os.path.exists(new_name):
                    # self.sc.print("From: "+file_name)
                    self.sc.print(new_name)
                    os.rename(file_name, new_name)
                SN += 1

        # restart
        self.sc.restart()

main()