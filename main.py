import json
import os
from datetime import datetime, timezone

from llm_client import get_client, ask
from prompts import PROMPT_VARIANTS, TASK_QUESTION, EXPECTED_ANSWER
from grader import grade_results

REPORT_JSON_PATH = "output/results.json"
REPORT_MD_PATH = "output/comparison_report.md"


def run_all_variants(client):
    results = []
    for variant in PROMPT_VARIANTS:
        print(f"\n▶ Running #{variant['id']}: {variant['name']} "
              f"(temperature={variant['temperature']})...")

        response = ask(
            client,
            user_prompt=variant["user_prompt"],
            system_prompt=variant["system_prompt"],
            temperature=variant["temperature"],
        )

        results.append({
            "id": variant["id"],
            "variant": variant["name"],
            "technique": variant["technique"],
            "temperature": variant["temperature"],
            "system_prompt": variant["system_prompt"],
            "user_prompt": variant["user_prompt"],
            "response": response,
        })

    return results


def print_comparison_table(graded_results):
    print("\n" + "=" * 70)
    print("  COMPARISON SUMMARY")
    print("=" * 70)
    print(f"{'#':<3} {'Variant':<38} {'Temp':<6} {'Correct?'}")
    print("-" * 70)
    for r in graded_results:
        mark = "✅" if r["correct"] else "❌"
        print(f"{r['id']:<3} {r['variant']:<38} {r['temperature']:<6} {mark}")
    print("=" * 70)

    correct_count = sum(1 for r in graded_results if r["correct"])
    print(f"\n{correct_count}/{len(graded_results)} variants produced the correct answer "
          f"({EXPECTED_ANSWER}).")


def save_json_report(graded_results):
    os.makedirs("output", exist_ok=True)
    with open(REPORT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "task_question": TASK_QUESTION,
            "expected_answer": EXPECTED_ANSWER,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "results": graded_results,
        }, f, indent=2)


def save_markdown_report(graded_results):
    os.makedirs("output", exist_ok=True)

    lines = [
        "# Prompt Comparison Report",
        "",
        f"**Task:** {TASK_QUESTION}",
        "",
        f"**Expected answer:** {EXPECTED_ANSWER}",
        "",
        "## Summary Table",
        "",
        "| # | Variant | Temperature | Correct? |",
        "|---|---|---|---|",
    ]

    for r in graded_results:
        mark = "✅" if r["correct"] else "❌"
        lines.append(f"| {r['id']} | {r['variant']} | {r['temperature']} | {mark} |")

    lines.append("")
    lines.append("## Full Responses")
    lines.append("")

    for r in graded_results:
        lines.append(f"### #{r['id']} — {r['variant']}")
        lines.append(f"*Technique: {r['technique']}*")
        lines.append("")
        if r["system_prompt"]:
            lines.append(f"**System prompt:** {r['system_prompt']}")
            lines.append("")
        lines.append(f"**User prompt:**\n```\n{r['user_prompt']}\n```")
        lines.append("")
        lines.append(f"**Response:**\n```\n{r['response']}\n```")
        lines.append("")
        lines.append(f"**Correct:** {'✅ Yes' if r['correct'] else '❌ No'}")
        lines.append("\n---\n")

    with open(REPORT_MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    print("📝 Prompt Testing CLI Tool")
    print(f"Task: {TASK_QUESTION}")
    print(f"Expected answer: {EXPECTED_ANSWER}")
    print(f"Testing {len(PROMPT_VARIANTS)} prompt variants against Gemini...\n")

    client = get_client()

    results = run_all_variants(client)
    graded_results = grade_results(results, EXPECTED_ANSWER)

    print_comparison_table(graded_results)

    save_json_report(graded_results)
    save_markdown_report(graded_results)

    print(f"\n✅ Full report saved to {REPORT_MD_PATH} and {REPORT_JSON_PATH}")


if __name__ == "__main__":
    main()
