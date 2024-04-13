# AND MAYBE ADD THE STORYLINE, ADD A DIFFERENCE IN THE BOTTOM (MAYBE SOUND,
# AND ROOM IS BLACKED OUT), ALSO ADD A SOUND WHEN NOTICE CHANGES,
# ROOM IN THE LIBRARY TO HAVE A DIFFERENCE BEFORE THE BOOKS IS FILLED IN AND
# AFTER IT IS FILLED, CAN'T FIND THE ICON PROBLEM RENAME TO HAVING __ AT THE
#  START TO MAKE IT AT THE TOP OF THE FOLDER, NOTICE WHEN AN ITEM IS RECEIVED
# OR AN ITEM IS USED, MAYBE ADD ANIMATION AFTER START SCREEN FOR STORYLINE
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import sys, os.path

Window.fullscreen = 'auto'
adap_path = os.path.dirname(os.path.realpath(sys.argv[0]))
id_file = os.path.join(adap_path, 'isfgcon.txt')
game_id = open(id_file, 'r')
ID = game_id.read()
if ID == '':
    raise Exception("Game ID not filled")
game_id.close()
cfg_file = os.path.join(adap_path, 'gstcfgmg.txt')
gstcfg = open(cfg_file, 'r')
CFG = gstcfg.readlines()
AT = CFG[-1].split()
gstcfg.close()


class StartScreen(Screen):
    def on_enter(self):
        self.label.text = "Thanks for signing up to the cultural " \
                          "hackathon!\n" \
                          "The 3 fastest first attempt clear times will get " \
                          "Gong cha vouchers!\n\nIMPORTANT!!! PRESSING ESC " \
                          "CLOSES THE GAME and make your attempt INVALID if " \
                          "the game has started! (The game starts on the " \
                          "next screen, so feel free to press ESC now, not" \
                          " later!) Remember to take a " \
                          "photo of the end screen of your first " \
                          "attempt because next attempts won't be valid for" \
                          " the rewards (the end screen shows the attempt " \
                          "number, attempts greater than 1 won't be valid " \
                          "for prizes but feel free to replay the game as " \
                          "many times as you want :D). Send the screenshot" \
                          " to culturalhackathonsubmissions@gmail.com\n\n" \
                          "Please turn your volume on as there are clues " \
                          "that has sound. Press left click to interact with" \
                          " objects, when wanting to use an object, just" \
                          " click on the thing you want to use it on. You " \
                          "can right click to put a mark, and left clicking" \
                          " on the mark will make it disappear. You will be" \
                          " playing as a student at Rangi trying to learn " \
                          "about different cultures, their traditions and " \
                          "myths. You even have a book lying on your table " \
                          "*hint* *hint* on this topic! However, some pages" \
                          " are not finished, and one of the pages is " \
                          "missing... Find the missing page and complete " \
                          "your book! Type 'I am ready for those Gong cha " \
                          "vouchers' in the box and hit submit to start the " \
                          "game. Your clear time will start counting right " \
                          "after submitting. Good luck, have fun! " \
                          "- Globalisation Committee" \


    def start_game(self):
        if self.ready_input.text.strip() == \
                "I am ready for those Gong cha vouchers":
            if NOTIFICATION.state == 'play':
                NOTIFICATION.stop()
                NOTIFICATION.play()
            else:
                NOTIFICATION.play()
            StartScreen.start_time(self)
        else:
            Notice.change_text(self.notice, "Please check for typos")

    def start_time(self):
        HackathonApp.time_start = Clock.schedule_interval(StartScreen.add_time,
                                                          .1)
        HackathonApp.game[0].current = 'game'
        self.start.disabled = True

    @staticmethod
    def add_time(dt):
        HackathonApp.time += 0.1


class Inventory(Widget):
    def open_inventory(self):
        if HackathonApp.rooms[1].ids.inventory.ids.inventory_button.source == \
                'inventorywithnotif.png':
            for room in HackathonApp.rooms[1:]:
                room.ids.inventory.ids.inventory_button.source = \
                    'inventory_button.png'
        if self.inventory_button.y == 0:
            animate = Animation(y=self.parent.height * 0.2, duration=0.2)
            self.inventory_button.source = 'inventory_button_down.png'
            animate.start(self.inventory_button)
            animate2 = Animation(top=self.parent.height * 0.2, duration=0.2)
            animate2.start(self.inventory_background)
        if self.inventory_button.y == self.parent.height * 0.2:
            animate = Animation(y=0, duration=0.2)
            self.inventory_button.source = 'inventory_button.png'
            animate.start(self.inventory_button)
            animate2 = Animation(top=0, duration=0.2)
            animate2.start(self.inventory_background)

    @staticmethod
    def is_item_there(item_list):
        if item_list[0] in \
                HackathonApp.rooms[
                    1].ids.inventory.ids.inventory_space.children:
            return True
        else:
            return False

    @staticmethod
    def add_item(item_list):
        already_have_item = Inventory.is_item_there(item_list)
        if not already_have_item:
            if NOTIFICATION.state == 'play':
                NOTIFICATION.stop()
                NOTIFICATION.play()
            else:
                NOTIFICATION.play()
            for room in HackathonApp.rooms[1:]:
                room.ids.inventory.ids.inventory_space.add_widget(
                    item_list[HackathonApp.rooms.index(room) - 1])
                if room.ids.inventory.ids.inventory_button.y == 0:
                    room.ids.inventory.ids.inventory_button.source = \
                        'inventorywithnotif.png'

    @staticmethod
    def remove_item(item_list):
        already_have_item = Inventory.is_item_there(item_list)
        if already_have_item:
            if NOTIFICATION.state == 'play':
                NOTIFICATION.stop()
                NOTIFICATION.play()
            else:
                NOTIFICATION.play()
            for room in HackathonApp.rooms[1:]:
                room.ids.inventory.ids.inventory_space.remove_widget(
                    item_list[HackathonApp.rooms.index(room) - 1])
                if room.ids.inventory.ids.inventory_button.y == 0:
                    room.ids.inventory.ids.inventory_button.source = \
                        'inventorywithnotif.png'


class BackToMenuButton(Widget):
    pass


class Notice(Label):
    def change_text(self, new_text):
        if NOTIFICATION.state == 'play':
            NOTIFICATION.stop()
            NOTIFICATION.play()
        else:
            NOTIFICATION.play()
        self.text = new_text
        animate = Animation(opacity=1,
                            duration=0) + Animation(
            opacity=1, duration=2.5) + Animation(opacity=0, duration=1.2)
        animate.cancel_all(self)
        animate.start(self)


class Room1(Screen):
    def on_enter(self):
        ROOM_1_MUSIC.play()

    @staticmethod
    def on_leave():
        if HackathonApp.game[0].current not in ['cave_book_event',
                                                'myth_page1', 'poster_event']:
            ROOM_1_MUSIC.stop()


class CaveBookItem(Image):
    pass


class CaveBookEvent(Screen):
    def check_cave_answer(self):
        if self.cave_input.text.strip().lower() in ANSWERS['largest cave']:
            self.cave_input.disabled = True
            self.submit_button.disabled = True
            self.cave_input.opacity = 0
            self.background.source = 'cavebookend.png'
            Notice.change_text(self.notice,
                               "Obtained cave book")
            HackathonApp.rooms[1].ids.cavebook.ids.cavebook_button.disabled \
                = True
            Inventory.add_item(ROOM1_BOOK)
            if HackathonApp.myth_book[0].ids.page_input.disabled \
                    and HackathonApp.myth_book[1].ids.page_input.disabled \
                    and HackathonApp.myth_book[2].ids.page_input.disabled \
                    and HackathonApp.myth_book[3].ids.page_input.disabled\
                    and HackathonApp.myth_book[4].ids.page_input.disabled:
                HackathonApp.rooms[1].ids.background.source = 'bedroomopen.png'
                HackathonApp.rooms[0].ids.room_1.background_normal = \
                    'bedroomopen.png'
                DOOR_OPEN.play()
                HackathonApp.rooms[0].ids.room_2.disabled = False
                HackathonApp.rooms[0].ids.room_3.disabled = False
            else:
                HackathonApp.rooms[1].ids.background.source = \
                    'bedroomnoitems.png'
                HackathonApp.rooms[0].ids.room_1.background_normal = \
                    'bedroomnoitems.png'
        else:
            Notice.change_text(self.notice, 'Wrong answer.')


class CaveBook(Widget):
    pass


class Door(Widget):
    @staticmethod
    def door_click():
        if HackathonApp.rooms[1].ids.background.source == 'bedroomopen.png':
            HackathonApp.game[0].current = 'game'
        else:
            Notice.change_text(HackathonApp.rooms[1].ids.notice,
                               "It's late, I shouldn't go outside")


class Poster(Widget):
    pass


class Bed(Widget):
    @staticmethod
    def bed_click():
        if HackathonApp.rooms[1].ids.background.source != 'bedroomopen.png':
            Notice.change_text(HackathonApp.rooms[1].ids.notice,
                               "I'm not sleepy yet, maybe I should fix "
                               "some of my books.")


class PosterEvent(Screen):
    pass


class BedCrystal1(Widget):
    @staticmethod
    def bed_crystal1():
        if BEDCRYSTAL1.state == 'play':
            BEDCRYSTAL1.stop()
            BEDCRYSTAL1.play()
        else:
            BEDCRYSTAL1.play()


class BedCrystal2(Widget):
    @staticmethod
    def bed_crystal2():
        if BEDCRYSTAL2.state == 'play':
            BEDCRYSTAL2.stop()
            BEDCRYSTAL2.play()
        else:
            BEDCRYSTAL2.play()


class BedCrystal3(Widget):
    @staticmethod
    def bed_crystal3():
        if BEDCRYSTAL3.state == 'play':
            BEDCRYSTAL3.stop()
            BEDCRYSTAL3.play()
        else:
            BEDCRYSTAL3.play()


class MythPage1(Screen):
    def check_page1_answer(self, index):
        if self.page_input.text.strip().lower() in ANSWERS[index]:
            self.page_input.disabled = True
            self.submit_button.disabled = True
            if NOTIFICATION.state == 'play':
                NOTIFICATION.stop()
                NOTIFICATION.play()
            else:
                NOTIFICATION.play()
            if HackathonApp.myth_book[0].ids.page_input.disabled \
                    and HackathonApp.myth_book[1].ids.page_input.disabled \
                    and HackathonApp.myth_book[2].ids.page_input.disabled \
                    and HackathonApp.myth_book[3].ids.page_input.disabled\
                    and HackathonApp.myth_book[4].ids.page_input.disabled:
                Animation.stop_all(HackathonApp.myth_book[0].ids.notice)
                Animation.stop_all(HackathonApp.myth_book[1].ids.notice)
                Animation.stop_all(HackathonApp.myth_book[2].ids.notice)
                Animation.stop_all(HackathonApp.myth_book[3].ids.notice)
                Animation.stop_all(HackathonApp.myth_book[4].ids.notice)
                Animation.stop_all(HackathonApp.myth_book[5].ids.notice)
                HackathonApp.myth_book[0].ids.notice.text = \
                    HackathonApp.myth_book[1].ids.notice.text = \
                    HackathonApp.myth_book[2].ids.notice.text = \
                    HackathonApp.myth_book[3].ids.notice.text = \
                    HackathonApp.myth_book[4].ids.notice.text = \
                    HackathonApp.myth_book[5].ids.notice.text = \
                    "Find the missing page to finish the book."
                HackathonApp.myth_book[0].ids.notice.opacity = \
                    HackathonApp.myth_book[1].ids.notice.opacity = \
                    HackathonApp.myth_book[2].ids.notice.opacity = \
                    HackathonApp.myth_book[3].ids.notice.opacity = \
                    HackathonApp.myth_book[4].ids.notice.opacity = \
                    HackathonApp.myth_book[5].ids.notice.opacity = 1
                if HackathonApp.rooms[1].ids.background.source == \
                        'bedroomnoitems.png':
                    HackathonApp.rooms[
                        1].ids.background.source = 'bedroomopen.png'
                    HackathonApp.rooms[0].ids.room_1.background_normal = \
                        'bedroomopen.png'
                    DOOR_OPEN.play()
                    HackathonApp.rooms[0].ids.room_2.disabled = False
                    HackathonApp.rooms[0].ids.room_3.disabled = False
            else:
                Notice.change_text(self.notice, "You've finished this page.")
        else:
            Notice.change_text(self.notice, 'Wrong answer.')


class MythPage2(Screen):
    def check_page2_answer(self):
        MythPage1.check_page1_answer(self.ids.page_input.parent.parent,
                                     'myth 2')


class MythPage3(Screen):
    def check_page3_answer(self):
        MythPage1.check_page1_answer(self.ids.page_input.parent.parent,
                                     'myth 3')


class MythPage4(Screen):
    def check_page4_answer(self):
        MythPage1.check_page1_answer(self.ids.page_input.parent.parent,
                                     'myth 4')


class MythPage5(Screen):
    def check_page5_answer(self):
        MythPage1.check_page1_answer(self.ids.page_input.parent.parent,
                                     'myth 5')


class MythPage6(Screen):
    pass


class MythBook(Widget):
    pass


class Room2(Screen):
    def on_enter(self):
        DrippingWater.water_animation(self.water_drop, False)
        ROOM_2_MUSIC.play()
        Notice.change_text(self.ids.notice, "Mysterious Cave")

    def on_leave(self):
        DrippingWater.water_animation(self.water_drop, True)
        ROOM_2_MUSIC.stop()


class DrippingWater(Widget):
    def water_animation(self, cancel):
        animate = Animation(y=self.parent.height * 0.1722, duration=0.2) + \
                  Animation(y=self.parent.height * 0.6, size_hint=(0, 0),
                            disabled=True, duration=0) + \
                  Animation(y=self.parent.height * 0.6, disabled=False,
                            duration=1) + \
                  Animation(size_hint=(1, 1), duration=1)
        animate.repeat = True
        animate.start(self.water_drop)
        animate.start(self.water_button)
        if cancel:
            animate.cancel_all(self.water_drop)
            animate.cancel_all(self.water_button)

    @staticmethod
    def get_water():
        have_bucket = Inventory.is_item_there(BUCKET_ITEM)
        if not HackathonApp.got_water:
            if have_bucket:
                Inventory.remove_item(BUCKET_ITEM)
                Inventory.add_item(WATER_BUCKET)
                Notice.change_text(HackathonApp.rooms[2].ids.notice,
                                   "Obtained water bucket")
                HackathonApp.got_water = True
            elif not have_bucket:
                Notice.change_text(HackathonApp.rooms[2].ids.notice,
                                   "A bucket could collect the water...")


class CaveCrystal1(Widget):
    @staticmethod
    def sound_cave_1():
        if CRYSTAL1.state == 'play':
            CRYSTAL1.stop()
            CRYSTAL1.play()
        else:
            CRYSTAL1.play()
        if not HackathonApp.sound_puzzle_solved:
            HackathonApp.sound_sequence.append('1')
            if HackathonApp.sound_sequence == SOUND_SEQUENCE_ANSWER:
                Vines.release_book(HackathonApp.rooms[2].ids.vines)
            elif len(HackathonApp.sound_sequence) >= \
                    len(SOUND_SEQUENCE_ANSWER):
                HackathonApp.sound_sequence.pop(0)


class CaveCrystal2(Widget):
    @staticmethod
    def sound_cave_2():
        if CRYSTAL2.state == 'play':
            CRYSTAL2.stop()
            CRYSTAL2.play()
        else:
            CRYSTAL2.play()
        if not HackathonApp.sound_puzzle_solved:
            HackathonApp.sound_sequence.append('2')
            if HackathonApp.sound_sequence == SOUND_SEQUENCE_ANSWER:
                Vines.release_book(HackathonApp.rooms[2].ids.vines)
            elif len(HackathonApp.sound_sequence) >= \
                    len(SOUND_SEQUENCE_ANSWER):
                HackathonApp.sound_sequence.pop(0)


class CaveCrystal3(Widget):
    @staticmethod
    def sound_cave_3():
        if CRYSTAL3.state == 'play':
            CRYSTAL3.stop()
            CRYSTAL3.play()
        else:
            CRYSTAL3.play()
        if not HackathonApp.sound_puzzle_solved:
            HackathonApp.sound_sequence.append('3')
            if HackathonApp.sound_sequence == SOUND_SEQUENCE_ANSWER:
                Vines.release_book(HackathonApp.rooms[2].ids.vines)
            elif len(HackathonApp.sound_sequence) >= \
                    len(SOUND_SEQUENCE_ANSWER):
                HackathonApp.sound_sequence.pop(0)


class VineBookItem(Image):
    pass


class Vines(Widget):
    def release_book(self):
        if not HackathonApp.sound_puzzle_solved:
            HackathonApp.rooms[2].ids.background.source = 'cavenovine.png'
            HackathonApp.rooms[0].ids.room_2.background_normal = \
                'cavenovine.png'
            animate = Animation(
                opacity=1, disabled=False, duration=0
                                ) + Animation(
                y=self.parent.height * 0.1522, duration=0.2) + Animation(
                x=self.parent.width*0.88833,
                size=(self.parent.width * 0.119,
                      self.parent.height * 0.03357), duration=0)
            animate.start(self.vines)
            if self.vines.width == self.vines.parent.width * 0.119:
                self.vines.background_normal = 'vinebookend.png'
            HackathonApp.sound_puzzle_solved = True

    def get_vine_book(self):
        self.vines.opacity = 0
        self.vines.disabled = True
        Inventory.add_item(ROOM2_BOOK)
        Notice.change_text(HackathonApp.rooms[2].ids.notice,
                           "Obtained mysterious book covered in vines")


class Treasure(Widget):
    def mine_treasure(self):
        if self.treasure.source == 'treasurestart.png':
            have_shovel = Inventory.is_item_there(SHOVEL_ITEM)
            if have_shovel:
                self.treasure.source = 'treasure.png'
                Inventory.remove_item(SHOVEL_ITEM)
                Notice.change_text(HackathonApp.rooms[2].ids.notice,
                                   "Used shovel")
            else:
                Notice.change_text(HackathonApp.rooms[2].ids.notice,
                                   "Maybe I can find a shovel somewhere...")
        elif self.treasure.source == 'treasure.png':
            self.treasure.source = 'treasureempty.png'
            self.treasure_button.disabled = True
            self.get_bucket()

    @staticmethod
    def get_bucket():
        Inventory.add_item(BUCKET_ITEM)
        Notice.change_text(HackathonApp.rooms[2].ids.notice,
                           "Obtained bucket")


class BucketItem(Image):
    pass


class WaterBucketItem(Image):
    pass


class Room3(Screen):
    def on_enter(self):
        if HackathonApp.rooms[3].ids.background.source != "livetreefinal.png":
            ROOM_3_MUSIC.play()
            Notice.change_text(self.ids.notice, "???")
        else:
            LIVE_TREE_MUSIC.play()
            Notice.change_text(self.ids.notice, "Yggdrasil")

    @staticmethod
    def on_leave():
        if HackathonApp.game[0].current not in ['sign_event']:
            if HackathonApp.rooms[3].ids.background.source != \
                    "livetreefinal.png":
                ROOM_3_MUSIC.stop()
            else:
                LIVE_TREE_MUSIC.stop()


class Shovel(Widget):
    def get_shovel(self):
        self.shovel_head.disabled = True
        self.shovel_body.disabled = True
        self.shovel_tail.disabled = True
        Inventory.add_item(SHOVEL_ITEM)
        Notice.change_text(HackathonApp.rooms[3].ids.notice,
                           "Obtained shovel")
        HackathonApp.rooms[3].ids.background.source = \
            "deadtreenoshovel.png"
        HackathonApp.rooms[0].ids.room_3.background_normal = \
            "deadtreenoshovel.png"


class ShovelItem(Image):
    pass


class SignEvent(Screen):
    pass


class Sign(Widget):
    pass


class Tree(Widget):
    @staticmethod
    def water_tree():
        have_water = Inventory.is_item_there(WATER_BUCKET)
        if have_water:
            HackathonApp.rooms[3].ids.background.source = "livetreefinal.png"
            HackathonApp.rooms[0].ids.room_3.background_normal = \
                "livetreefinal.png"
            HackathonApp.sign_screen[0].ids.background.source =\
                'livesignwall.png'
            ROOM_3_MUSIC.stop()
            LIVE_TREE_MUSIC.play()
            Inventory.remove_item(WATER_BUCKET)
            Notice.change_text(HackathonApp.rooms[3].ids.notice,
                               "Used water bucket")
            HackathonApp.rooms[0].ids.room_4.disabled = False
            HackathonApp.rooms[3].ids.tree.ids.tree1.disabled = True
            HackathonApp.rooms[3].ids.tree.ids.tree2.disabled = True
            HackathonApp.rooms[3].ids.tree.ids.tree3.disabled = True
            HackathonApp.rooms[3].ids.tree.ids.tree4.disabled = True
            HackathonApp.rooms[3].ids.tree.ids.tree5.disabled = True
            HackathonApp.rooms[3].ids.tree.ids.tree6.disabled = True


class Room4(Screen):
    def on_enter(self):
        ROOM_4_MUSIC.play()
        Notice.change_text(self.ids.notice, "Yggdrasil's library?")

    @staticmethod
    def on_leave():
        ROOM_4_MUSIC.stop()


class MissingRoom1Book(Widget):
    def fill_room1_book(self):
        if self.empty_spot.background_normal != 'book1fill.png':
            have_book = Inventory.is_item_there(ROOM1_BOOK)
            if have_book:
                self.empty_spot.background_normal = 'book1fill.png'
                self.empty_spot.opacity = 1
                Inventory.remove_item(ROOM1_BOOK)
                Notice.change_text(HackathonApp.rooms[4].ids.notice,
                                   "Used cave book")


class MissingRoom2Book(Widget):
    def fill_room2_book(self):
        if self.empty_spot2.background_normal != 'book2fill.png':
            have_book = Inventory.is_item_there(ROOM2_BOOK)
            if have_book:
                self.empty_spot2.background_normal = 'book2fill.png'
                self.empty_spot2.opacity = 1
                Inventory.remove_item(ROOM2_BOOK)
                Notice.change_text(HackathonApp.rooms[4].ids.notice,
                                   "Used mysterious book")
            else:
                if self.empty_spot2.opacity != 1:
                    Notice.change_text(
                        HackathonApp.rooms[4].ids.notice,
                        "Another book missing? I remember there's a book "
                        "covered by vines in the cave...")


class ColouredBookRow(Widget):
    @staticmethod
    def crystal_hint():
        if HackathonApp.rooms[4].ids.book_2.empty_spot2.opacity != 1:
            Notice.change_text(HackathonApp.rooms[4].ids.notice,
                               "I've seen these colours somewhere...")


class MissingPage(Widget):
    def get_missing_page(self):
        if HackathonApp.rooms[
            4
        ].ids.book_1.ids.empty_spot.opacity == HackathonApp.rooms[
            4
        ].ids.book_2.ids.empty_spot2.opacity == 1:
            self.missing_page_button.disabled = True
            HackathonApp.game[0].current = 'win'
        else:
            Notice.change_text(HackathonApp.rooms[4].ids.notice,
                               "I can't go inside the room, maybe I need to "
                               "fill in the missing books in the library...")


class EscapeGame(Screen):
    pass


class WinScreen(Screen):
    def on_enter(self):
        for audio in AUDIO:
            if audio.state == 'play':
                audio.stop()
        HackathonApp.time_start.cancel()
        VICTORY_MUSIC.play()
        new_gstcfg = open(cfg_file, 'a')
        new_gstcfg.write(f'\n{int(AT[0]) + 1} {round(HackathonApp.time, 2)}')
        self.time.text = f"Attempt: {int(AT[0]) + 1}\nID: {ID}\nClear time: " \
                         f"" + str(round(HackathonApp.time, 2)) + ' seconds'
        self.thanks.text = "You've beaten the game! Take a screenshot of " \
                           "this screen and send it to " \
                           "culturalhackathonsubmissions@gmail.com\n" \
                           "Special thanks to:\n" \
                           "- Julia Loo\n" \
                           "- Joy Luu\n" \
                           "- Andre Leader\n" \
                           "- Atiya Hossain\n" \
                           "& everyone that supported the game!\n" \
                           "\n" \
                           "Made by Ethan Quach"

    @staticmethod
    def on_leave():
        VICTORY_MUSIC.stop()


class HackathonApp(App):
    game = []
    rooms = []
    myth_book = []
    got_water = False
    sound_sequence = []
    sound_puzzle_solved = False
    sign_screen = []
    time = 0
    time_start = None

    def build(self):
        hackathon = ScreenManager(transition=FadeTransition())
        start_point = StartScreen(name='start')
        room_1 = Room1(name='room1')
        room_2 = Room2(name='room2')
        room_3 = Room3(name='room3')
        room_4 = Room4(name='room4')
        main_room = EscapeGame(name='game')
        poster_event = PosterEvent(name='poster_event')
        cave_book = CaveBookEvent(name='cave_book_event')
        sign_event = SignEvent(name='sign_event')
        myth_page1 = MythPage1(name='myth_page1')
        myth_page2 = MythPage2(name='myth_page2')
        myth_page3 = MythPage3(name='myth_page3')
        myth_page4 = MythPage4(name='myth_page4')
        myth_page5 = MythPage5(name='myth_page5')
        myth_page6 = MythPage6(name='myth_page6')
        victory_screen = WinScreen(name='win')
        # Update list so object properties contains the instance of each rooms
        HackathonApp.rooms = [main_room, room_1, room_2,
                              room_3, room_4]
        HackathonApp.myth_book = [myth_page1, myth_page2,
                                  myth_page3, myth_page4,
                                  myth_page5, myth_page6]
        HackathonApp.sign_screen = [sign_event]
        HackathonApp.rooms[0].ids.room_2.disabled = True
        HackathonApp.rooms[0].ids.room_3.disabled = True
        HackathonApp.rooms[0].ids.room_4.disabled = True
        hackathon.add_widget(start_point)
        hackathon.add_widget(main_room)
        hackathon.add_widget(room_1)
        hackathon.add_widget(room_2)
        hackathon.add_widget(room_3)
        hackathon.add_widget(room_4)
        hackathon.add_widget(myth_page1)
        hackathon.add_widget(myth_page2)
        hackathon.add_widget(myth_page3)
        hackathon.add_widget(myth_page4)
        hackathon.add_widget(myth_page5)
        hackathon.add_widget(myth_page6)
        hackathon.add_widget(victory_screen)
        hackathon.add_widget(cave_book)
        hackathon.add_widget(poster_event)
        hackathon.add_widget(sign_event)
        hackathon.current = 'start'
        HackathonApp.game = [hackathon]
        return hackathon


ANSWERS = {'largest cave': ['vietnam'],
           'myth 1': ['hephaestus', 'hephaistos'],
           'myth 2': ['a giant axe', "pangu's axe", "giant axe", 'axe', 'ax',
                      'a giant ax', "pangu's ax", "giant ax", "his axe",
                      'his ax', 'an axe', 'an ax'],
           'myth 3': ['hanako', 'hanako-san', 'hanako san', 'hanakosan',
                      'toire no hanako san', 'hanako of the toilet',
                      'toire no hanako-san', 'toire no hanakosan'],
           'myth 4': ['jawbone', 'jaw'],
           'myth 5': ['tlalli', 'tlalli çoquitl']}
# Each item requires 4 copies as one copy is required for each room's inventory
ROOM1_BOOK = [CaveBookItem(source='cavebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1)),
              CaveBookItem(source='cavebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1)),
              CaveBookItem(source='cavebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1)),
              CaveBookItem(source='cavebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1))]

ROOM2_BOOK = [VineBookItem(source='vinebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1)),
              VineBookItem(source='vinebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1)),
              VineBookItem(source='vinebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1)),
              VineBookItem(source='vinebook.png', allow_stretch=True,
                           keep_ratio=False, size_hint=(0.1, 1))]

SHOVEL_ITEM = [ShovelItem(source='shovel.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1)),
               ShovelItem(source='shovel.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1)),
               ShovelItem(source='shovel.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1)),
               ShovelItem(source='shovel.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1))]

BUCKET_ITEM = [BucketItem(source='bucket.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1)),
               BucketItem(source='bucket.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1)),
               BucketItem(source='bucket.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1)),
               BucketItem(source='bucket.png', allow_stretch=True,
                          keep_ratio=False, size_hint=(0.1, 1))]

WATER_BUCKET = [WaterBucketItem(source='waterbucket.png', allow_stretch=True,
                                keep_ratio=False, size_hint=(0.1, 1)),
                WaterBucketItem(source='waterbucket.png', allow_stretch=True,
                                keep_ratio=False, size_hint=(0.1, 1)),
                WaterBucketItem(source='waterbucket.png', allow_stretch=True,
                                keep_ratio=False, size_hint=(0.1, 1)),
                WaterBucketItem(source='waterbucket.png', allow_stretch=True,
                                keep_ratio=False, size_hint=(0.1, 1))]


SOUND_SEQUENCE_ANSWER = ['1', '2', '3', '2', '1', '2', '3']

# ===================AUDIO==================
NOTIFICATION = SoundLoader.load('notification.wav')
ROOM_1_MUSIC = SoundLoader.load('room1.wav')
ROOM_1_MUSIC.loop = True
BEDCRYSTAL1 = SoundLoader.load('bedcrystal1.wav')
BEDCRYSTAL2 = SoundLoader.load('bedcrystal2.wav')
BEDCRYSTAL3 = SoundLoader.load('bedcrystal3.wav')
DOOR_OPEN = SoundLoader.load('door_open.wav')
ROOM_2_MUSIC = SoundLoader.load('cave.wav')
ROOM_2_MUSIC.loop = True
CRYSTAL1 = SoundLoader.load('crystal1.wav')
CRYSTAL2 = SoundLoader.load('crystal2.wav')
CRYSTAL3 = SoundLoader.load('crystal3.wav')
ROOM_3_MUSIC = SoundLoader.load('deadtree.wav')
ROOM_3_MUSIC.loop = True
LIVE_TREE_MUSIC = SoundLoader.load('livetree.wav')
LIVE_TREE_MUSIC.loop = True
ROOM_4_MUSIC = SoundLoader.load('room4.wav')
ROOM_4_MUSIC.loop = True
VICTORY_MUSIC = SoundLoader.load('victory.wav')
VICTORY_MUSIC.loop = True
AUDIO = [NOTIFICATION, ROOM_1_MUSIC, BEDCRYSTAL1, BEDCRYSTAL2, BEDCRYSTAL3,
         DOOR_OPEN, ROOM_2_MUSIC, CRYSTAL1, CRYSTAL2, CRYSTAL3, ROOM_3_MUSIC,
         LIVE_TREE_MUSIC, ROOM_4_MUSIC, VICTORY_MUSIC]


if __name__ == '__main__':
    HackathonApp().run()
