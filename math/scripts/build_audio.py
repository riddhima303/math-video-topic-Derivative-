"""Generate synchronized per-scene narration using Edge Neural TTS."""
from pathlib import Path
import asyncio, json, re, subprocess
import edge_tts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
VOICE = "en-US-JennyNeural"
RATE = "-6%"

async def main():
    OUT.mkdir(exist_ok=True)
    durations = {}
    for i in range(1, 7):
        audio = OUT / f"scene{i}.mp3"
        script = ROOT / "narration" / f"scene{i}.txt"
        text = script.read_text(encoding="utf-8").strip()
        await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(audio))
        info = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(audio)], capture_output=True, text=True, check=True)
        duration = float(json.loads(info.stdout)["format"]["duration"]) + 0.4
        durations[f"scene{i}"] = round(duration, 2)
    (OUT / "durations.json").write_text(json.dumps(durations, indent=2) + "\n")
    total = sum(durations.values())
    def stamp(seconds):
        s = round(seconds)
        return f"{s // 60:02d}:{s % 60:02d}"
    full = ["DERIVATIVE AND RATE OF CHANGE", "Complete narration with synchronized audio timestamps", f"Voice: {VOICE} (AI text-to-speech; disclosed in credits)", ""]
    start = 0.0
    for i in range(1, 7):
        full.extend([f"SCENE {i}  [{stamp(start)} - {stamp(start + durations[f'scene{i}'])}]", (ROOT / "narration" / f"scene{i}.txt").read_text(encoding="utf-8").strip(), ""])
        start += durations[f"scene{i}"]
    (ROOT / "narration" / "full_script.txt").write_text("\n".join(full), encoding="utf-8")
    (ROOT / "narration" / "timing.txt").write_text(f"Exact audio runtime: {stamp(total)}. Voice: {VOICE}. Timestamps in full_script.txt are measured from generated scene clips.\n", encoding="utf-8")
    print(json.dumps(durations, indent=2))
    print(f"Total narration: {total:.2f} sec ({total / 60:.2f} min)")

if __name__ == "__main__":
    asyncio.run(main())
