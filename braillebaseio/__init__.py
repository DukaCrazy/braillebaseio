import json
import csv
import xml.etree.ElementTree as ET

# 0
def read_file(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        return read_string(f.read())

# 1
def read_string(data: str) -> list:
    data = data.strip()

    if data.startswith("[") or data.startswith("{"):
        return _from_json(data)

    if data.startswith("<?xml") or data.startswith("<"):
        return _from_xml(data)

    return _from_csv(data)


def _from_json(data: str):
    raw = json.loads(data)
    result = []

    for item in raw:
        braille_raw = item.get("braille")

        if isinstance(braille_raw, str):
            braille = [b.strip() for b in braille_raw.split(",")]
        else:
            braille = braille_raw

        result.append((
            item.get("letter"),
            braille,
            int(item.get("pattern"))
        ))

    return result


def _from_csv(data: str):
    result = []
    reader = csv.reader(data.splitlines())

    for row in reader:
        if len(row) < 3:
            continue

        letter, braille_raw, pattern = row
        braille = [b.strip() for b in braille_raw.split(",")]

        result.append((
            letter,
            braille,
            int(pattern)
        ))

    return result


def _from_xml(data: str):
    root = ET.fromstring(data)
    result = []

    for item in root.findall("item"):
        letter = item.findtext("letter")
        braille_raw = item.findtext("braille")
        pattern = item.findtext("pattern")

        braille = [b.strip() for b in braille_raw.split(",")]

        result.append((
            letter,
            braille,
            int(pattern)
        ))

    return result
