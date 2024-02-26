from manim import *

class MyScene(Scene):
    def construct(self):
        # Create a Text object with the desired text
        # Display the text on the screen
        intro_text = Text("Pointers!", color=BLUE)
        self.play(Write(intro_text))
        self.wait(3)
    
        svg_image = SVGMobject("path to svg")
        self.play(FadeIn(svg_image))
        self.wait(3)


# To render the scene, run:
# manim -p -ql your_script_name.py MyScene
