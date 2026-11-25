from manim import *
from pathlib import Path
import json

BG = '#0B1020'
INK = '#F4F7FB'
MUTED = '#AAB5C8'
CYAN = '#55D6E8'
GOLD = '#FFC857'
PINK = '#FF6B8A'
GREEN = '#73E2A7'
ROOT = Path(__file__).resolve().parents[1]

class LectureScene(Scene):
    def setup(self):
        self.camera.background_color = BG
    def start_voice(self, number):
        """Start the scene's narration at the opening animation cue."""
        self._voice_started_at = self.time
        self._voice_number = number
        audio = ROOT / 'assets' / f'scene{number}.mp3'
        if audio.exists() and audio.stat().st_size > 5000:
            self.add_sound(str(audio))
    def finish_voice(self, number):
        """Hold the final teaching visual through the full narration clip."""
        durations = {}
        p = ROOT / 'assets' / 'durations.json'
        if p.exists():
            durations = json.loads(p.read_text())
        estimated = {1:34.3, 2:54.4, 3:51.0, 4:60.9, 5:93.4, 6:45.0}
        target = float(durations.get(f'scene{number}', estimated[number]))
        elapsed = self.time - self._voice_started_at
        if elapsed < target:
            self.wait(target - elapsed)
    def header(self, section, title):
        tag = Text(section.upper(), font_size=18, color=CYAN, weight=BOLD)
        heading = Text(title, font_size=34, color=INK, weight=BOLD)
        group = VGroup(tag, heading).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        group.to_corner(UL, buff=0.45)
        rule = Line(LEFT*6.5, RIGHT*6.5, color='#28334B', stroke_width=1).next_to(group, DOWN, buff=0.2)
        self.play(FadeIn(group, shift=DOWN*0.15), Create(rule), run_time=0.7)
        return VGroup(group, rule)
