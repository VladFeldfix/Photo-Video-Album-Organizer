from FoxyFunctions import ff

class main:
    def __init__(self):
        self.ff = ff("PHOTO-VIDEO ALBUM ORGANIZER", "v2.0")
        self.SETTINGS = self.ff.get_settings()
        self.display_main_menu()
    
    def display_main_menu(self):
        self.ff.display_header()
        menu = (("GET NEW FILES", self.get_new_files), ("SETTINGS", self.settings), ("EXIT", self.ff.exit))
        self.ff.display_menu("MAIN MENU", menu)

    def get_new_files(self):
        self.display_main_menu()

    def settings(self):
        self.ff.display_header()
        self.ff.set_settings(self.SETTINGS)
        self.display_main_menu()

main()