from FoxyFunctions import ff
import os
from PIL import Image, ExifTags

class main:
    def __init__(self):
        # activate GUI
        main_menu = (("RUN", self.run),)
        self.ff = ff("PHOTO & VIDEO ORGANIZER", "3.0", main_menu)

        # run gui
        self.ff.run()
    
    def run(self):
        location = self.ff.settings_get("New files location")
        SN = 0
        if os.path.isdir(location):
            
            # calculate workload
            steps = 0
            for root, folders, files in os.walk(location):
                for file in files:
                    steps += 1
            # run
            steps_done = 0
            for root, folders, files in os.walk(location):
                for file in files:
                    """
                    """
                    steps_done += 1
                    percent = steps_done / steps
                    self.ff.progress_bar_value_set(percent*100)
                    #self.ff.write(root+"/"+file)
                    
                    file_name = root+"/"+file
                    file_extension = os.path.splitext(file_name)[1]
                    
                    # set global variables
                    NEWFILES = self.ff.settings_get("New files location")
                    PHOTOALBUM = self.ff.settings_get("Photo Album")
                    VIDEOALBUM = self.ff.settings_get("Video Album")
                    
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
                            datetime_stmp = self.ff.today()
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
                        self.ff.write("New folder created: "+dist_fold)
                        os.makedirs(dist_fold)
                    
                    if not os.path.exists(new_name):
                        # self.ff.indexed_print("From: "+file_name)
                        self.ff.write(new_name)
                        os.rename(file_name, new_name)
                    SN += 1
        else:
            self.ff.error("There is no such location: "+location)

main()