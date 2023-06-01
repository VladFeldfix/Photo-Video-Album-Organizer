from SmartConsole import *
from PIL import Image
from PIL.ExifTags import TAGS

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
        for root, dirs, files in os.walk(self.new_photos):
            for file in files:
                try:
                    image = Image.open(file)
                    exifdata = image.getexif()
                    for tag_id in exifdata:
                        # get the tag name, instead of human unreadable tag id
                        tag = TAGS.get(tag_id, tag_id)
                        data = exifdata.get(tag_id)
                        # decode bytes 
                        if isinstance(data, bytes):
                            data = data.decode()
                        print(f"{tag:25}: {data}")
                except:
                    pass

        # restart
        self.sc.restart()

main()