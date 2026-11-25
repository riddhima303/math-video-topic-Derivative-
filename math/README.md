# Derivative and Rate of Change

A six-scene, 16:9 Manim lecture designed to teach the derivative from average change through a full limit-definition example. The scenes use a dark lecture palette, labeled graphs, moving points, secants, tangent lines, and stepwise algebra.

## Contents

- `project.py` and `scenes/`: six independent Manim scenes
- `narration/`: scene-by-scene voice-over text and a combined script
- `assets/`: scene narration MP3s and exact duration metadata
- `scripts/build_audio.py`: regenerate Edge Neural narration and timing metadata
- `outputs/storyboard.pdf`: six-page storyboard, one page per scene
- `outputs/derivative_rate_of_change.mp4`: rendered 1080p lecture (5:18)
- `references.md`: source references and AI disclosure

## Requirements

Python 3.10-3.13 is recommended. Install Manim Community Edition and its system dependencies (FFmpeg, Cairo, and Pango) as described in the [official Manim installation guide](https://docs.manim.community/en/stable/installation.html). Formulas use Manim text objects, so a separate LaTeX installation is not required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Generate the optional AI voice-over with Edge Neural TTS (requires internet access):

```bash
python -m pip install -r requirements-audio.txt
python scripts/build_audio.py
```

This creates one MP3 per scene, `assets/durations.json`, and updates the script with exact scene timecodes. The scenes start narration with the opening cue and hold their final visual until each clip finishes. The combined duration is approximately 5 to 6 minutes.

## Render

Render the six scenes at 1080p, in order:

```bash
manim render -r 1920,1080 --fps 30 project.py Scene1Intro Scene2Basics Scene3Visual Scene4Derivative Scene5Example Scene6Summary
```

Manim writes six MP4s under `media/videos/project/1080p30/`. Join them without re-encoding:

```bash
ffmpeg -f concat -safe 0 -i <(printf "file '%s'\n" media/videos/project/1080p30/Scene1Intro.mp4 media/videos/project/1080p30/Scene2Basics.mp4 media/videos/project/1080p30/Scene3Visual.mp4 media/videos/project/1080p30/Scene4Derivative.mp4 media/videos/project/1080p30/Scene5Example.mp4 media/videos/project/1080p30/Scene6Summary.mp4) -c copy outputs/derivative_rate_of_change.mp4
```

If your shell does not support process substitution, create a `concat.txt` with the six `file 'path'` lines and pass that file to `ffmpeg -f concat -safe 0 -i concat.txt`.

The included MP3 assets are added to their corresponding scenes. If you remove them, the animations still use the included per-scene duration metadata but render without narration.

## Mathematical check

For `f(x)=x^2`, the average rate from 2 to 4 is `(16-4)/(4-2)=6`. The limit quotient simplifies to `2x+h`, so `f'(x)=2x` and `f'(2)=4`. The tangent at `(2,4)` is `y-4=4(x-2)`, or `y=4x-4`.

## Output

The rendered video and storyboard are in `outputs/`. The animation source, measured narration MP3s, complete timestamped narration, setup instructions, and references are included in this repository.
