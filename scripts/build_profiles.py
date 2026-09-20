import json
cities = {c["city"] for c in json.load(open("cities.json"))}
def months(s):
    out = []
    for part in s.split(","):
        a, b = (int(x) for x in (part.split("-") if "-" in part else [part, part]))
        out += list(range(a, b + 1)) if a <= b else list(range(a, 13)) + list(range(1, b + 1))
    return sorted(set(out))
prof = {}
for line in open("scripts/profiles.txt", encoding="utf-8"):
    n, f, c, nat, v, m, tag = line.strip().split("|")
    prof[n] = {"f": int(f), "c": int(c), "n": int(nat), "v": int(v), "m": months(m), "tag": tag}
print("profiles:", len(prof), "missing:", sorted(cities - prof.keys()), "extra:", sorted(prof.keys() - cities))
open("data/profiles.js", "w", encoding="utf-8").write("window.PROFILES=" + json.dumps(prof, ensure_ascii=False) + ";")
