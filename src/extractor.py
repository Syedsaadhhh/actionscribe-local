import re
from typing import List, Dict

ACTION_PATTERNS = [
    r"(?P<owner>[A-Z][a-zA-Z]+) (will|should|must|needs to|is going to) (?P<task>.+)",
    r"(?P<task>submit|prepare|send|schedule|review|finish|update|create) (?P<object>.+)"
]

DEADLINE_PATTERN = r"(by|before|on) (?P<deadline>\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|\d{1,2}/\d{1,2}|\d{1,2}-\d{1,2})\b)"


def detect_deadline(text: str) -> str | None:
    match = re.search(DEADLINE_PATTERN, text, re.IGNORECASE)
    if match:
        return match.group("deadline")
    return None


def extract_actions(text: str) -> List[Dict[str, str]]:
    actions = []

    for line in text.split("\n"):
        for pattern in ACTION_PATTERNS:
            match = re.search(pattern, line, re.IGNORECASE)

            if match:
                action = {
                    "raw": line.strip(),
                    "deadline": detect_deadline(line) or "unspecified"
                }

                if "owner" in match.groupdict():
                    action["owner"] = match.group("owner")

                if "task" in match.groupdict():
                    action["task"] = match.group("task")

                actions.append(action)

    return actions


if __name__ == "__main__":
    sample = "Ahmed will prepare slides by Friday"
    print(extract_actions(sample))
