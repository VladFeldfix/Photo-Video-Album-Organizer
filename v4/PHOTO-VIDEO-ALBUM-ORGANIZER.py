from FoxyFunctions import ff
import os
from PIL import Image, ExifTags

class main:
    def __init__(self):
        # activate GUI
        main_menu = (("RUN", self.run),)
        self.ff = ff("PHOTO & VIDEO ORGANIZER", "4.0", main_menu)

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
            # set global variables
            NEWFILES = self.ff.settings_get("New files location")
            PHOTOALBUM = self.ff.settings_get("Photo Album")
            VIDEOALBUM = self.ff.settings_get("Video Album")
            for root, folders, files in os.walk(location):
                for file in files:
                    # display workload
                    steps_done += 1
                    percent = steps_done / steps
                    self.ff.progress_bar_value_set(percent*100)
                    
                    # READ INFO FROM FILE
                    file_name = root+"/"+file
                    file_type = file[0:3]
                    year = file[4:8]
                    month = file[8:10]
                    day = file[10:12]
                    hour = file[13:15]
                    minute = file[15:17]
                    seconds = file[17:19]
                    newname = year+"-"+month+"-"+day+" "+hour+minute+seconds+" "+str(SN).zfill(4)
                    # PHOTOS
                    if file_type == "IMG":
                        newname += ".jpg"
                        self.ff.write(newname)
                        destanation_folder = PHOTOALBUM+"/"+year+"/"+month+"."+year
                        if not os.path.isdir(destanation_folder):
                            os.makedirs(destanation_folder)
                        newname = destanation_folder+"/"+newname

                        if not os.path.isfile(newname):
                            os.rename(file_name, newname)
                            pass
                        else:
                            self.ff.error(newname+" Already exists!")

                    # VIDEOS
                    elif file_type == "VID":
                        newname += ".mp4"
                        self.ff.write(newname)
                        destanation_folder = VIDEOALBUM+"/"+year+"/"+month+"."+year
                        if not os.path.isdir(destanation_folder):
                            os.makedirs(destanation_folder)
                        newname = destanation_folder+"/"+newname

                        if not os.path.isfile(newname):
                            os.rename(file_name, newname)
                            pass
                        else:
                            self.ff.error(newname+" Already exists!")
                    SN += 1
                self.ff.write("Done!")
        else:
            self.ff.error("There is no such location: "+location)

main()