from src.extractor import extract_actions


def test_basic_action_detection():
    text = "Ahmed will prepare slides by Friday. Sara should send dataset."

    actions = extract_actions(text)

    assert len(actions) >= 1


def test_deadline_detection():
    text = "Ali will submit report by Monday"

    actions = extract_actions(text)

    assert any(a.get("deadline") == "Monday" for a in actions)
