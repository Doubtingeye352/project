from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
import sys

# updates made on 25 sep 2020 friday

screen_helper = """
ScreenManager:
    MenuScreen:
    planets:
    earth:
    mars:
    venus:
    neptune:
    uranus:
    mercury:
    pluto:
    saturn:
    jupiter:
<MenuScreen>:

    name: 'menu'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '/Users/ninaad/Desktop/background.jpeg'



    MDRectangleFlatButton:

        text: 'planet selection'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'planets'



    Label:
        text: "welcome our app teaches to you about pantes in a fun way be sure to look around!"
        pos_hint: {'center_x':0.5,'center_y':0.8}


    Label:
        text: "copyright slash cv © "
        pos_hint: {'center_x':0.5,'center_y':0.1}



<planets>:
    name: 'planets'
    MDRectangleFlatButton:
        text: 'Earth'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'earth'

    MDRectangleFlatButton:
        text: 'pluto'
        pos_hint: {'center_x':0.5,'center_y':0.30}
        on_press: root.manager.current = 'pluto'


    MDRectangleFlatButton:
        text: 'mars'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'mars'

    MDRectangleFlatButton:
        text:'venus'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'venus'


    MDRectangleFlatButton:
        text:'neptune'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'neptune'


    MDRectangleFlatButton:
        text:'uranus'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'uranus'   

    MDRectangleFlatButton:
        text:'mercury'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        on_press: root.manager.current = 'mercury'

    MDRectangleFlatButton:
        text:'saturn'
        pos_hint: {'center_x':0.5,'center_y':0.20}
        on_press: root.manager.current = 'saturn'

    MDRectangleFlatButton:
        text:'jupiter'
        pos_hint: {'center_x':0.5,'center_y':0.10}
        on_press: root.manager.current = 'jupiter'

<earth>:
    name: 'earth'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'
        
    Label:
        text: 'earth is the third farthest planet from the sun and the only planet in our solar system to have life.'
        color: 0, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}


    Label:
        text: 'According to radiometric dating estimation and other evidence, the earth was formed over 4.5 billion years ago'
        color: 0, 0, 0, 1

    Label:
        text: 'Some more information about earth!'
        color: 1, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}

    Label:
        text: "earth is 149.6 million km away from the sun"
        color: 1, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
       
    Label:
        text: " The mass of earth is Mass: 5.972 × 10^24 kg"
        color: 1, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}

    Label:
        text: "earths Radius is: 6,371 km"
        color: 1, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        
    Image:
        source: "/Users/ninaad/Desktop/earth.gif"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}


<venus>:
    name: 'venus'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'
        
    Label:
        text: "venus is the second furthest planet from the sun and is also the hottest planet in our solar system"
        color: 0, 0, 0, 1
        pos_hint: {'center_x':0.5,'center_y':0.7}
        
    Label:
        text: "by now you might be wondering how is venus the hottest planet in the solar system? well the answer to that is..."
        color: 0,0,0,1
        pos_hint: {'center_x':0.5,'center_y':0.6}
        
    Label:
        text: "It is because of venus's greenhouse like atmosphere and heats the surface to the melting point of lead which is"
        color: 0,0,0,1
        
    Label:
        text: "about 880 degrees Fahrenheit (471 degrees Celsius)."
        color: 0,0,0,1
        pos_hint: {'center_x':0.5,'center_y':0.4 }
        
    Label:
        text: "venus fun facts"
        color: 1,0,0,1
        pos_hint: {'center_x':0.5,'center_y':0.3 }

<mars>:
    name: 'mars'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'
<neptune>:
    name: 'neptune'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'


<uranus>:
    name: 'uranus'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'

<mercury>:
    name: 'mercury'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'

<pluto>:
    name: 'pluto'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'

<saturn>:
    name: 'saturn'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'

<jupiter>:
    name: 'jupiter'
    MDRectangleFlatButton:
        text:'back'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press: root.manager.current = 'planets'

"""


class MenuScreen(Screen):
    pass


class planets(Screen):
    pass


class earth(Screen):
    pass


class mars(Screen):
    pass


class venus(Screen):
    pass


class neptune(Screen):
    pass


class uranus(Screen):
    pass


class mercury(Screen):
    pass


class pluto(Screen):
    pass


class saturn(Screen):
    pass


class jupiter(Screen):
    pass




sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(planets(name="planets"))
sm.add_widget(earth(name="earth"))
sm.add_widget(mars(name="mars"))
sm.add_widget(venus(name="venus"))
sm.add_widget(neptune(name='neptune'))
sm.add_widget(uranus(name="uranus"))
sm.add_widget(mercury(name="mercury"))
sm.add_widget(pluto(name="pluto"))
sm.add_widget(saturn(name='saturn'))
sm.add_widget(jupiter(name="jupiter"))


class DemoApp(MDApp):
    icon = '/Users/ninaad/Desktop/app_icon.png'

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.title = 'Planets Pre Download (under Development )'
        return screen
        


DemoApp().run()

