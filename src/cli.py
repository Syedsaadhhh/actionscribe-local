import argparse
import json
from extractor import extract_actions
from summarizer import summarize


def main():
    parser = argparse.ArgumentParser(
        description="ActionScribe Local CLI – Extract summaries and action items from transcripts"
    )

    parser.add_argument("file", help="Path to transcript file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        text = f.read()

    summary = summarize(text)
    actions = extract_actions(text)

    if args.json:
        print(json.dumps({"summary": summary, "actions": actions}, indent=2))
        return

    print("\nSummary:\n")
    print(summary)

    print("\nAction Items:\n")

    for action in actions:
        owner = action.get("owner", "Unknown")
        task = action.get("task", action.get("raw"))
        deadline = action.get("deadline", "unspecified")

        print(f"• {owner} → {task} (deadline: {deadline})")


if __name__ == "__main__":
    main()
