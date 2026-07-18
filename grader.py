import re


def response_contains_answer(response_text, expected_answer):
    if response_text.startswith("[ERROR]"):
        return False

    pattern = r"(?<!\d)" + re.escape(str(expected_answer)) + r"(?!\d)"
    return re.search(pattern, response_text) is not None


def grade_results(results, expected_answer):
    for r in results:
        r["correct"] = response_contains_answer(r["response"], expected_answer)
    return results
