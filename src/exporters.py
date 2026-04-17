import json


def export_markdown(summary: str, actions: list) -> str:
    md = f"## Summary\n{summary}\n\n## Actions\n"

    for a in actions:
        md += f"- {a}\n"

    return md


def export_json(summary: str, actions: list) -> str:
    return json.dumps({"summary": summary, "actions": actions}, indent=2)


def export_whatsapp(actions: list) -> str:
    return "\n".join([f"• {a}" for a in actions])
