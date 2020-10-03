from random import randint
import requests
import json
import webbrowser
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import TwoLineIconListItem

from screens import HomeScreen, AboutScreen, ResourcesScreen, ContentNavigationDrawer


class CustomThreeLineIconListItem(TwoLineIconListItem):
    pass


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        gui = Builder.load_file('main.kv')
        return gui

    def on_start(self):
        self.screen_manager = self.root.ids.screen_manager
        self.nav_drawer = self.root.ids.nav_drawer
        self.resource_list = self.root.ids.resources_screen.ids.resource_list
        self.icon_list = []
        self.populate_resources()
        # print(self.root.ids.home_screen.ids)

    def populate_resources(self):
        # result = requests.get("https://m-ed-x.firebaseio.com/XXXXXXX")
        # resource_data = json.loads(result.content.decode())
        # resource_list = [resource for resource in resource_data]
        # for resource in resource_list:
        self.icon_list = ["emoticon-outline", "emoticon-confused-outline", "emoticon-cool-outline",
                     "emoticon-cry-outline"
                     "emoticon-devil-outline", "emoticon-excited-outline", "emoticon-happy-outline",
                     "emoticon-kiss-outline", "emoticon-neutral-outline", "emoticon-neutral", "emoticon-poop",
                     "emoticon-sad"]
        for i in range(1,13):
            self.resource_list.add_widget(CustomThreeLineIconListItem(text=f"Section {i}",
                                                                      id=f"{i}",
                                                                      secondary_text=f"{i} could refer to whatever you want",
                                                                      # on_release=self.open_url
                                                                      ))


    def app_description(self):
        return 'This is a description of the app, it can be as long as you like, within reason.\n\nIt ' \
               'can go onto new lines with no problem.\n\nHowever, if you make it too long the text may ' \
               'need to be made smaller! For now, this is ok I think.'

    def change_theme(self):
        color_list = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_palette = color_list[randint(0, len(color_list)-1)]

    def open_nav_drawer(self):
        Clock.schedule_once(lambda dt: self.nav_drawer.set_state('open'), 0.2)

    def close_nav_drawer(self):
        Clock.schedule_once(lambda dt: self.nav_drawer.set_state('close'), 0.4)

    def open_socials(self, social):
        Clock.schedule_once(lambda dt: webbrowser.open(social), 0.2)

    def icon_loop(self):
        icon_list = ["emoticon-outline", "emoticon-confused-outline", "emoticon-cool-outline", "emoticon-cry-outline"
                     "emoticon-devil-outline", "emoticon-excited-outline", "emoticon-happy-outline",
                     "emoticon-kiss-outline", "emoticon-neutral-outline", "emoticon-neutral", "emoticon-poop",
                     "emoticon-sad"]

if __name__ == '__main__':
    MainApp().run()
