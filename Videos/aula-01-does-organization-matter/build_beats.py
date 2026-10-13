"""Build beats.json from script.md (adapted from the Macro videos' build_beats.py).

The spoken text is the script with markdown emphasis and [pause] markers stripped:
Speechify ignores ellipses, so an intra-clip silence cannot be bought. Each beat records its
number of [pause] markers; scenes.py realises them as held frames, and explainer-compile pads
the audio to the longer stream.
"""
import json, re, pathlib

TITLES = {
    "BeatOpen": "Same building, same people, two outcomes",
    "BeatFordFacts": "Ford: twelve and a half hours to ninety-three minutes",
    "BeatScale": "When does a line pay? The threshold q bar",
    "BeatFiveDollar": "The five dollar day and the Solow condition",
    "BeatFordSystem": "Ford's choices as a coherent system",
    "BeatGMFacts": "GM answers a different question",
    "BeatVariety": "How many models? n star equals a q over F",
    "BeatVarietyStatics": "One formula orders three firms",
    "BeatMForm": "Variety needs divisions: the multidivisional form",
    "BeatToyota": "Toyota: five practices that look like mistakes",
    "BeatTwoProblems": "Coordination and motivation",
    "BeatThreeSystems": "Three coherent systems",
    "BeatWrongAttempt": "Best practices, one at a time: the plus sign",
    "BeatIncreasingDiff": "Increasing differences, three ways",
    "BeatCrossPartial": "The cross partial",
    "BeatSubstitutes": "Substitutes, turned upside down",
    "BeatTopkis": "Why complements move together",
    "BeatTwoChoices": "Two choices, solved line by line",
    "BeatMultiplier": "The systems multiplier",
    "BeatEvidence": "Testing complementarity: steel finishing lines",
    "BeatCube": "The cube",
    "BeatValley": "Every road crosses the valley",
    "BeatTwoPeaks": "Two peaks, and why marginal analysis stays put",
    "BeatNUMMI": "Fremont again: a jump, not a walk",
    "BeatClose": "Two lines, and a cube",
}


def spoken(body: str) -> str:
    """Strip markdown and stage directions; return one paragraph of speakable prose."""
    body = re.sub(r"\[pause\]", "", body)
    body = re.sub(r"\*\*(.+?)\*\*", r"\1", body, flags=re.S)
    body = re.sub(r"\*(.+?)\*", r"\1", body, flags=re.S)
    body = body.replace("—", " - ").replace("*", "")
    return re.sub(r"\s+", " ", body).strip()


text = pathlib.Path("script.md").read_text(encoding="utf-8")
beats = []
for m in re.finditer(r"## (Beat\w+) . (\d+) s\n(.*?)(?=\n## |\Z)", text, re.S):
    bid, budget, body = m.group(1), int(m.group(2)), m.group(3)
    beats.append({"id": bid, "title": TITLES[bid], "text": spoken(body),
                  "audio": f"audio/{bid}.mp3", "seconds": 0.0, "budget_seconds": budget,
                  "pauses": body.count("[pause]")})

assert [b["id"] for b in beats] == list(TITLES), "script.md beats and TITLES disagree"
manifest = {"voice": None, "model": "simba-3.2", "total_seconds": 0.0, "beats": beats}
pathlib.Path("beats.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False),
                                      encoding="utf-8")
chars = sum(len(b["text"]) for b in beats)
words = sum(len(b["text"].split()) for b in beats)
pauses = sum(b["pauses"] for b in beats)
print(f"{len(beats)} beats, {chars:,} characters, {words:,} words, {pauses} pauses")
print(f"beats over the 2000-char single-request cap (client chunks them): "
      f"{sum(len(b['text']) > 2000 for b in beats)}")
print(f"projected at 197 wpm + 2.5 s/pause: {words / 197 + pauses * 2.5 / 60:.1f} min")
