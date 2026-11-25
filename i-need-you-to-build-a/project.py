"""Entry point: render all six 1080p Manim scenes in order."""
from scenes.scene1_intro import Scene1Intro as _Scene1Intro
from scenes.scene2_basics import Scene2Basics as _Scene2Basics
from scenes.scene3_visual import Scene3Visual as _Scene3Visual
from scenes.scene4_derivative import Scene4Derivative as _Scene4Derivative
from scenes.scene5_example import Scene5Example as _Scene5Example
from scenes.scene6_summary import Scene6Summary as _Scene6Summary

# Thin local subclasses let Manim discover all scene classes from this entry point.
class Scene1Intro(_Scene1Intro):
    pass

class Scene2Basics(_Scene2Basics):
    pass

class Scene3Visual(_Scene3Visual):
    pass

class Scene4Derivative(_Scene4Derivative):
    pass

class Scene5Example(_Scene5Example):
    pass

class Scene6Summary(_Scene6Summary):
    pass
