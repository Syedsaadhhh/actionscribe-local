import re
from typing import List, Dict

WHATSAPP_LINE_PATTERN = re.compile(
    r"^(?P<date>\d{1,2}/\d{1,2}/\d{2,4}),\s(?P<time>\d{1,2}:\d{2})\s-\s(?P<sender>[^:]+):\s(?P<message>.+)$"
)


def parse_whatsapp_export(file_path: str) -> List[Dict[str, str]]:
    """
    Parse WhatsApp exported chat (.txt) into structured messages.

    Supports standard WhatsApp export format without media attachments.
    Returns list of dicts with sender, timestamp, message.
    """

    parsed_messages = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = WHATSAPP_LINE_PATTERN.match(line.strip())

            if match:
                parsed_messages.append(
                    {
                        "timestamp": f"{match.group('date')} {match.group('time')}",
                        "sender": match.group("sender"),
                        "message": match.group("message"),
                    }
                )

    return parsed_messages


def extract_action_candidates(messages: List[Dict[str, str]]) -> List[str]:
    """
    Extract likely action-oriented messages from WhatsApp conversations.

    Filters messages containing intent verbs.
    """

    keywords = [
        "will",
        "should",
        "need to",
        "please",
        "assign",
        "deadline",
        "send",
        "prepare",
        "submit",
        "schedule",
    ]

    action_messages = []

    for msg in messages:
        text = msg["message"].lower()

        if any(keyword in text for keyword in keywords):
            action_messages.append(f"{msg['sender']}: {msg['message']}")

    return action_messages


if __name__ == "__main__":
    sample_path = "examples/whatsapp_sample.txt"
    parsed = parse_whatsapp_export(sample_path)
    actions = extract_action_candidates(parsed)

    print(actions)
