import sys
import textwrap
import os
import re
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class VibeEngine(App):
    def __init__(self, vibe_file):
        super().__init__()
        self.vibe_file = vibe_file
        self.version = "2.0.0 VIP"
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

    def build(self):
        print(f"--- VibeEngine Booting {self.version} ---")
        self.parse_vibe()
        return self.layout

    def parse_vibe(self):
        with open(self.vibe_file, 'r', encoding='utf-8') as f:
            content = f.read()

        ui_match = re.search(r"UI\s*\{(.*?)\}\s*BACKEND", content, re.DOTALL)
        backend_match = re.search(r"BACKEND\s*\{(.*)\}", content, re.DOTALL)

        if ui_match and backend_match:
            self.render_ui(ui_match.group(1).strip())
            self.execute_backend(backend_match.group(1))
        else:
            print("Syntax Error!")

    def render_ui(self, ui_code):
        # UI Components Parser
        lines = ui_code.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith("Label"):
                txt = re.findall(r'"([^"]*)"', line)[0]
                self.layout.add_widget(Label(text=txt, font_size='24sp'))
            
            elif line.startswith("Button"):
                txt = re.findall(r'"([^"]*)"', line)[0]
                btn = Button(text=txt, size_hint=(1, 0.2), background_color=(0, 0.5, 1, 1))
                # Button click ko backend se connect karte hain
                btn.bind(on_press=lambda x: self.on_vibe_click())
                self.layout.add_widget(btn)

            elif line.startswith("Input"):
                self.layout.add_widget(TextInput(hint_text="Type here...", multiline=False))

    def execute_backend(self, logic):
        clean_logic = textwrap.dedent(logic).strip()
        # Scope define karna taake click events kaam karein
        self.exec_scope = {}
        try:
            exec(clean_logic, globals(), self.exec_scope)
        except Exception as e:
            print(f"Backend Error: {e}")

    def on_vibe_click(self):
        if 'on_click' in self.exec_scope:
            self.exec_scope['on_click']()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        VibeEngine(sys.argv[1]).run()
    else:
        print("Usage: python vibe_engine.py app.vibe")