#!/usr/bin/env python3
"""Render a Cap Matin episode from a script.

Usage:
  python3 tools/make_episode.py <script.txt> <out.mp3> [YYYY-MM-DD]

Script format: sections separated by a line containing only ###.
  Section 1 = opening (+ family birthdays/name days when there are any)
  Section 2 = express weather
  Then one section per segment, last section = closing.
Inside a section, each non-empty line is read as one paragraph.

Sound design (chosen by Nicolas):
  - Breton-style music at the start (assets/intro.wav) and end (assets/outro.wav)
  - no sound between the opening and the weather
  - a wave (assets/vague.wav) right after the weather
  - harp or soft piano, picked at random, between the other sections
  - short pauses only (no long silences)
Voice: one Microsoft neural voice per day, chosen by weekday (VOICES below).
"""
import datetime, os, random, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "assets")

# Monday=0 ... Sunday=6 — one single voice per episode, never mixed.
VOICES = {
    0: "fr-FR-VivienneMultilingualNeural",  # lundi : Vivienne
    1: "fr-FR-HenriNeural",                 # mardi : Henri
    2: "fr-FR-DeniseNeural",                # mercredi : Denise
    3: "fr-FR-RemyMultilingualNeural",      # jeudi : Rémy
    4: "en-US-AvaMultilingualNeural",       # vendredi : Ava
    5: "fr-CH-ArianeNeural",                # samedi : Ariane
    6: "fr-FR-RemyMultilingualNeural",      # dimanche : Rémy
}
PITCH = "+2Hz"  # a touch brighter; NEVER speed up the rate ("dynamique" ≠ "plus vite")


def sh(cmd):
    subprocess.run(cmd, shell=True, check=True, executable="/bin/bash")


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip()
    return float(out or 0)


def load_pron():
    rules = []
    p = os.path.join(ROOT, "prononciation.txt")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=>" in line:
                a, b = [x.strip() for x in line.split("=>", 1)]
                rules.append((a, b))
    rules.sort(key=lambda r: -len(r[0]))
    return rules


def apply_pron(text, rules):
    for a, b in rules:
        text = re.sub(r"(?<!\w)" + re.escape(a) + r"(?!\w)", b, text)
    return text


def tts(text, voice, mp3):
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    base = ["edge-tts"] + (["--proxy", proxy] if proxy else []) + ["--voice", voice, f"--pitch={PITCH}"]
    for attempt in range(6):
        subprocess.run(base + ["--text", text, "--write-media", mp3], check=True, capture_output=True)
        d = duration(mp3)
        # guard against truncated audio (the service sometimes returns a fragment)
        if d > 0 and len(text) / d < 24:
            return
        print(f"  retry ({attempt + 1}): {d:.1f}s for {len(text)} chars", flush=True)
    raise SystemExit(f"TTS kept returning truncated audio for: {text[:60]}…")


def main():
    script, out = sys.argv[1], sys.argv[2]
    date = sys.argv[3] if len(sys.argv) > 3 else datetime.date.today().isoformat()
    voice = VOICES[datetime.date.fromisoformat(date).weekday()]
    print("voice:", voice)
    rules = load_pron()
    sections = [s.strip() for s in open(script, encoding="utf-8").read().split("###") if s.strip()]
    w = tempfile.mkdtemp(prefix="capmatin_")
    sh(f'cd {w} && ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=24000:cl=mono -t 0.2 sil.wav '
       f'&& ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=24000:cl=mono -t 0.1 gap.wav')
    for x in ["vague", "harpe", "piano"]:
        sh(f'cp "{A}/{x}.wav" {w}/t_{x}.wav')
    items, k = [], 0
    for si, sec in enumerate(sections):
        if si == 2:
            items += ["gap.wav", "t_vague.wav", "gap.wav"]
        elif si > 2:
            items += ["gap.wav", f"t_{random.choice(['harpe', 'piano'])}.wav", "gap.wav"]
        elif si == 1:
            items += ["sil.wav"]
        for para in [l.strip() for l in sec.split("\n") if l.strip()]:
            mp3 = f"{w}/p{k:03d}.mp3"
            tts(apply_pron(para, rules), voice, mp3)
            sh(f'ffmpeg -y -loglevel error -i {mp3} -af "silenceremove=start_periods=1:start_threshold=-50dB,'
               f'areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse" -ar 24000 -ac 1 {w}/p{k:03d}.wav')
            items += [f"p{k:03d}.wav", "sil.wav"]
            k += 1
    with open(f"{w}/list.txt", "w") as f:
        f.writelines(f"file '{it}'\n" for it in items)
    sh(f'cd {w} && ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -ar 24000 -ac 1 voice.wav')
    sh(f'ffmpeg -y -loglevel error -i "{A}/intro.wav" -i {w}/voice.wav -i "{A}/outro.wav" -filter_complex '
       f'"[1]adelay=200[b];[0][b][2]concat=n=3:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11" '
       f'-ar 44100 -ac 1 -b:a 96k -metadata title="Cap Matin {date}" -metadata artist="Cap Matin" "{out}"')
    print(f"OK {out}: {duration(out) / 60:.1f} min, {k} paragraphs")


if __name__ == "__main__":
    main()
