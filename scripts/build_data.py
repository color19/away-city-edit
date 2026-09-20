import json, re, datetime
cities = json.load(open("cities.json"))
by_code = {c["iata"]: c for c in cities}
# Google Flights Explore, IAD -> Europe, "next 6 months" cheapest 1-week trip, captured 2026-09-19
RAW = """
London LHR|Oct 12 – 20|1|10h25|557
Paris CDG|Nov 12 – 18|1|16h55|483
Madrid MAD|Nov 2 – 11|1|10h55|420
Athens ATH|Feb 6 – 15 2027|2|15h10|490
Rome FCO|Jan 30 – Feb 7 2027|1|16h15|495
Lisbon LIS|Nov 27 – Dec 3|1|9h30|630
Amsterdam AMS|Nov 16 – 24|1|11h45|591
Copenhagen CPH|Nov 12 – 19|0|8h05|396
Dublin DUB|Feb 28 – Mar 9 2027|1|9h35|495
Edinburgh EDI|Oct 12 – 20|1|9h45|770
Barcelona BCN|Nov 2 – 11|1|11h35|633
Venice VCE|Oct 12 – 20|1|15h25|679
Berlin BER|Nov 12 – 19|1|10h20|510
Florence FLR|Nov 30 – Dec 9|1|11h25|595
Prague PRG|Nov 12 – 20|1|10h15|453
Vienna VIE|Oct 11 – 20|1|13h55|1066
Budapest BUD|Nov 9 – 18|1|16h35|503
Milan MXP|Nov 12 – 18|1|16h45|484
Munich MUC|Nov 9 – 18|1|11h45|569
Stockholm ARN|Nov 9 – 18|1|10h30|384
Porto OPO|Nov 16 – 25|1|12h55|556
Seville SVQ|Feb 8 – 16 2027|2|15h05|707
Zurich ZRH|Nov 9 – 18|1|11h45|483
Naples NAP|Nov 29 – Dec 7|1|14h10|590
Krakow KRK|Nov 9 – 18|1|17h20|476
Oslo OSL|Nov 9 – 18|1|10h40|388
Nice NCE|Nov 14 – 20|1|16h15|756
Helsinki HEL|Oct 19 – 28|1|12h00|387
"""
MON = {m:i+1 for i,m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
rows = []
for line in RAW.strip().splitlines():
    name, dates, stops, dur, price = line.split("|")
    code = name.split()[-1]
    first = dates.split("–")[0].split()
    mon = MON[first[0]]; day = int(first[1])
    year = 2027 if "2027" in dates and mon <= 3 else (2026 if mon >= 9 else 2027)
    h, m = dur.split("h")
    rows.append({"code": code, "depart": f"{year}-{mon:02d}-{day:02d}", "label": dates,
                 "stops": int(stops), "minutes": int(h)*60+int(m), "price": int(price)})
missing = [c["city"] for c in cities if c["region"]=="Europe" and c["iata"] not in {r["code"] for r in rows}]
out = {"origin":"IAD","source":"Google Flights Explore","capturedAt":"2026-09-19","currency":"USD",
       "note":"每城市为未来6个月内最低价的一周往返行程（含税，1成人，经济舱）","rows":rows}
open("data/fares.js","w").write("window.FARES="+json.dumps(out,ensure_ascii=False)+";")
open("data/cities.js","w").write("window.CITIES="+json.dumps(cities,ensure_ascii=False)+";")
print(len(rows),"rows; Europe missing:",missing)
