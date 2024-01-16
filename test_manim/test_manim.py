from manim import *
class Draw(Scene):
    def construct(self):
        text1 = Text('Disneyland')
        self.play(Create(text1))
        self.play(text1.animate.scale(3))
        self.wait()
