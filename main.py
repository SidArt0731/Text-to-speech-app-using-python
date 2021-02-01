from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import tts

kv= """
Screen:
	BoxLayout:
		orientation : "vertical"
		padding: "16dp"
		spacing: "16dp"
		size_hint_y : None
		height : self.minimum_height
		pos_hint : {"center_y": 0.6}
		
		
		MDTextField:
			id : field
			hint_text : "Your Text"
			
			
		MDRaisedButton:
			text : "Text to Speech"
			pos_hint : {"right" : .95 , "center_y": .05}
			on_release : app.speak(field.text)
		
	Image:
		source: f"{images_path}/kivymd_logo.png"
		opacity : .2

"""

class MainApp(MDApp):
	
	def build(self):
		 
		return Builder.load_string(kv)
		
	def speak(self,text):
		tts.speak(text)
		
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		
if __name__ == "__main__":
	MainApp().run()
			
			
			