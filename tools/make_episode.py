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
Voice: Kyutai TTS 1.6B en_fr (free, CC-BY 4.0), voice "L" — the same voice as Petit Matin Good Vibes.
  Rendering runs on CPU and takes about 7-8x the audio length (≈45 min for 6 min).
  Rendered paragraphs are kept in the work folder, so a re-run resumes where it stopped.
"""
import datetime, os, random, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "assets")

def sh(cmd):
    subprocess.run(cmd, shell=True, check=True, executable="/bin/bash")


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip()
    return float(out or 0)


def main():
    script, out = sys.argv[1], sys.argv[2]
    date = sys.argv[3] if len(sys.argv) > 3 else datetime.date.today().isoformat()
    w = sys.argv[4] if len(sys.argv) > 4 else f"/tmp/capmatin_{date}"
    os.makedirs(w, exist_ok=True)
    sections = [s.strip() for s in open(script, encoding="utf-8").read().split("###") if s.strip()]
    layout, paras = [], []          # layout: list of (section index, paragraph index)
    for si, sec in enumerate(sections):
        for para in [l.strip() for l in sec.split("\n") if l.strip()]:
            layout.append((si, len(paras)))
            paras.append(para)
    flat = f"{w}/flat.txt"
    open(flat, "w", encoding="utf-8").write("\n\n".join(paras) + "\n")
    print(f"voice: Kyutai L — {len(paras)} paragraphs to render", flush=True)
    # Python 3.13: torch.compile is not supported, so it must be switched off or the voice crashes
    sh(f'NO_TORCH_COMPILE=1 python3 -I "{ROOT}/tools/kyutai_paras.py" {flat} {w}/paras')
    sh(f'cd {w} && ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=24000:cl=mono -t 0.2 sil.wav '
       f'&& ffmpeg -y -loglevel error -f lavfi -i anullsrc=r=24000:cl=mono -t 0.1 gap.wav')
    for x in ["vague", "harpe", "piano"]:
        sh(f'cp "{A}/{x}.wav" {w}/t_{x}.wav')
    items, prev = [], -1
    for si, k in layout:
        if si != prev:
            if si == 1:
                items += ["sil.wav"]
            elif si == 2:
                items += ["gap.wav", "t_vague.wav", "gap.wav"]
            elif si > 2:
                items += ["gap.wav", f"t_{random.choice(['harpe', 'piano'])}.wav", "gap.wav"]
            prev = si
        sh(f'ffmpeg -y -loglevel error -i {w}/paras/p{k:03d}.wav -af "silenceremove=start_periods=1:start_threshold=-50dB,'
           f'areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse" -ar 24000 -ac 1 {w}/c{k:03d}.wav')
        items += [f"c{k:03d}.wav", "sil.wav"]
    with open(f"{w}/list.txt", "w") as f:
        f.writelines(f"file '{it}'\n" for it in items)
    sh(f'cd {w} && ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -ar 24000 -ac 1 voice.wav')
    sh(f'ffmpeg -y -loglevel error -i "{A}/intro.wav" -i {w}/voice.wav -i "{A}/outro.wav" -filter_complex '
       f'"[1]adelay=200[b];[0][b][2]concat=n=3:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11" '
       f'-ar 44100 -ac 1 -b:a 96k -metadata title="Cap Matin {date}" -metadata artist="Cap Matin" "{out}"')
    print(f"OK {out}: {duration(out) / 60:.1f} min, {len(paras)} paragraphs")


if __name__ == "__main__":
    main()
