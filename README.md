<div align="center">

# 📝 Prompt Testing CLI Tool

**Tests 10 prompt engineering techniques on the same task and objectively grades which ones actually get the right answer.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=google&logoColor=white)

![Status](https://img.shields.io/badge/status-complete-22c55e?style=flat-square)
![Phase](https://img.shields.io/badge/Phase%203-LLM%20%26%20RAG%20Core%20Day%2018-3b82f6?style=flat-square)

</div>

---

## 📖 Overview

Rather than just eyeballing 10 different responses side by side, this tool uses a task with a **known correct answer** — a multi-step arithmetic word problem — so every prompt variant can be graded objectively as correct or incorrect, not just judged on how confident it sounds.

**The task, same for all 10 variants:**
> Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?

**Correct answer: 58** — (3×12=36) → (36−8=28) → (28+2×15=58)

---

## ✨ Features

- 🧪 10 prompt variants covering system prompts, few-shot examples, chain-of-thought, and temperature changes
- 🤖 Every variant sent to the real Gemini API
- ✅ **Objective grading** — checks whether each response actually contains the correct number, using a word-boundary regex so "58" doesn't falsely match inside "158"
- 📊 Prints a comparison table to the terminal
- 📋 Saves a full Markdown report (`output/comparison_report.md`) and a machine-readable JSON report (`output/results.json`)

---

## 🔑 Setup & Run

```bash
git clone https://github.com/atharva-9423/unprof.git
cd unprof/day-18

pip install -r requirements.txt
$env:GEMINI_API_KEY="your-actual-api-key-here"

python main.py
```

---

## 🧠 The 10 Prompt Techniques Explained

| # | Technique | What it tests |
|---|---|---|
| 1 | **Naive / zero-shot** | The bare question with zero guidance — the baseline every other technique is compared against. |
| 2 | **Zero-shot + explicit instruction** | Adds "show your working" — tests whether just asking for steps helps without truly guiding the reasoning. |
| 3 | **System prompt (role-based)** | A system prompt assigns a "meticulous math tutor" persona before the same question — tests whether role-setting alone improves rigor. |
| 4 | **Few-shot prompting** | Two fully worked similar problems are shown before the real question, so the model can pattern-match the expected reasoning style. |
| 5 | **Chain-of-thought (explicit)** | Appends the classic "Let's think step by step" trigger phrase, shown in research to significantly improve arithmetic reasoning. |
| 6 | **Few-shot + Chain-of-thought** | Combines worked examples *and* the step-by-step trigger — tests whether stacking techniques compounds the benefit. |
| 7 | **System + Chain-of-thought** | Combines a role-setting system prompt with the step-by-step trigger. |
| 8 | **Low temperature (0.0)** | Re-runs the best-performing prompt structure with temperature forced to 0, for maximum determinism. |
| 9 | **High temperature (1.5)** | Same prompt as #8, but at a high temperature — tests whether creativity/randomness degrades a task that has one objectively correct answer. |
| 10 | **Constrained output format** | Forces a strict `FINAL ANSWER: <number>` line at the end — tests whether requiring structured output helps or hurts the reasoning itself. |

### Key concepts, briefly

- **System prompt** — an instruction given to the model in a separate role from the user's message, typically used to set persona, tone, or constraints that apply to the whole conversation.
- **Few-shot prompting** — including a small number of worked examples in the prompt so the model can infer the expected pattern before answering the real question.
- **Chain-of-thought prompting** — encouraging the model to reason step by step rather than jumping straight to a final answer, which tends to improve accuracy on multi-step problems.
- **Temperature** — controls randomness in generation. `0.0` is close to deterministic and picks the highest-probability tokens; higher values (e.g. `1.5`) increase variety at the cost of consistency and precision.

---

## 📊 Observations (run this yourself and compare!)

> ⚠️ **Note:** the section below describes the *expected* pattern based on established prompt-engineering research, and matches what I saw in my own dry-run test of this pipeline's logic. I could not call the live Gemini API from the environment I built this in — **run `python main.py` yourself and replace this section with your actual results and observations**, since real model behavior can vary by version and randomness.

Typical expected pattern:

- **#1 (Naive) and #2 (explicit instruction without CoT)** tend to perform worst — without a nudge toward step-by-step reasoning, models are more likely to guess at a plausible-sounding number or skip a step in mental arithmetic.
- **#3 through #7** (system prompt, few-shot, and chain-of-thought variants) tend to perform noticeably better, since each of these techniques in its own way pushes the model toward showing intermediate steps rather than jumping to a conclusion.
- **#8 (temperature 0.0)** is usually the most *reliable* if you ran this multiple times — low temperature reduces the chance of an arithmetic slip introduced by sampling randomness.
- **#9 (temperature 1.5)** is where you're most likely to see inconsistency — correct on some runs, subtly wrong or oddly phrased on others, since high temperature actively works against precision on a task with one right answer.
- **#10 (constrained format)** usually performs about as well as its unconstrained counterpart (#7/#8) — forcing a clean final-answer line doesn't hurt the reasoning as long as the model is still allowed to reason *before* that line.

**Which technique performed best?** Based on this pattern, **chain-of-thought combined with a system prompt, at low temperature (#7/#8)** is expected to be the most reliable combination — it directly targets the two biggest failure modes (skipping reasoning steps, and randomness-induced arithmetic slips) at once.

---

## 📁 Project Structure

```
day-18/
├── prompts.py             # the 10 prompt variants + task definition
├── llm_client.py            # Gemini API wrapper
├── grader.py                  # objective correctness checking
├── main.py                     # runs all variants, compares, saves reports
├── requirements.txt
├── output/                       # generated on run
│   ├── comparison_report.md
│   └── results.json
└── README.md
```

---

<div align="center">

Built during **Phase 3 – LLM & RAG Core**, Day 18: *Prompt Engineering*

</div>
