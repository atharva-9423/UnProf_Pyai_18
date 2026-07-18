TASK_QUESTION = (
    "Sarah has 3 boxes of apples. Each box contains 12 apples. She gives "
    "away 8 apples, then buys 2 more boxes of 15 apples each. How many "
    "apples does she have now?"
)

EXPECTED_ANSWER = 58

FEW_SHOT_EXAMPLES = """Q: Tom has 4 packs of pencils with 6 pencils each. He loses 5 pencils, then buys 3 more packs of 6. How many pencils does he have now?
A: 4 packs x 6 = 24. 24 - 5 = 19. 3 packs x 6 = 18. 19 + 18 = 37. Tom has 37 pencils.

Q: A bakery has 5 trays of 8 muffins each. They sell 12 muffins, then bake 2 more trays of 8. How many muffins are there now?
A: 5 trays x 8 = 40. 40 - 12 = 28. 2 trays x 8 = 16. 28 + 16 = 44. The bakery has 44 muffins."""


PROMPT_VARIANTS = [
    {
        "id": 1,
        "name": "Naive / Zero-shot",
        "technique": "Bare question, no instructions at all.",
        "system_prompt": None,
        "user_prompt": TASK_QUESTION,
        "temperature": 0.7,
    },
    {
        "id": 2,
        "name": "Zero-shot + explicit instruction",
        "technique": "Adds a direct instruction to show the working.",
        "system_prompt": None,
        "user_prompt": f"{TASK_QUESTION} Show your working and give the final number clearly.",
        "temperature": 0.7,
    },
    {
        "id": 3,
        "name": "System prompt (role-based)",
        "technique": "A system prompt sets a persona/role before the same question.",
        "system_prompt": "You are a meticulous math tutor who never skips a calculation step.",
        "user_prompt": TASK_QUESTION,
        "temperature": 0.7,
    },
    {
        "id": 4,
        "name": "Few-shot prompting",
        "technique": "Two worked examples of similar problems precede the real question.",
        "system_prompt": None,
        "user_prompt": f"{FEW_SHOT_EXAMPLES}\n\nQ: {TASK_QUESTION}\nA:",
        "temperature": 0.7,
    },
    {
        "id": 5,
        "name": "Chain-of-thought (explicit)",
        "technique": "Adds 'Let's think step by step' to trigger explicit reasoning.",
        "system_prompt": None,
        "user_prompt": f"{TASK_QUESTION}\nLet's think step by step.",
        "temperature": 0.7,
    },
    {
        "id": 6,
        "name": "Few-shot + Chain-of-thought combined",
        "technique": "Combines worked examples AND an explicit step-by-step instruction.",
        "system_prompt": None,
        "user_prompt": f"{FEW_SHOT_EXAMPLES}\n\nQ: {TASK_QUESTION}\nA: Let's think step by step.",
        "temperature": 0.7,
    },
    {
        "id": 7,
        "name": "System + Chain-of-thought",
        "technique": "Combines a role-setting system prompt with explicit step-by-step reasoning.",
        "system_prompt": "You are a careful math tutor. Always reason step by step before answering.",
        "user_prompt": f"{TASK_QUESTION}\nLet's think step by step.",
        "temperature": 0.7,
    },
    {
        "id": 8,
        "name": "Low temperature (0.0)",
        "technique": "Same as the best-performing prompt above, but temperature forced to 0 for determinism.",
        "system_prompt": "You are a careful math tutor. Always reason step by step before answering.",
        "user_prompt": f"{TASK_QUESTION}\nLet's think step by step.",
        "temperature": 0.0,
    },
    {
        "id": 9,
        "name": "High temperature (1.5)",
        "technique": "Same prompt as #8, but with a high temperature to test consistency loss.",
        "system_prompt": "You are a careful math tutor. Always reason step by step before answering.",
        "user_prompt": f"{TASK_QUESTION}\nLet's think step by step.",
        "temperature": 1.5,
    },
    {
        "id": 10,
        "name": "Constrained output format",
        "technique": "Forces a strict final-answer-only format to test whether structure hurts reasoning.",
        "system_prompt": "You are a careful math tutor. Always reason step by step before answering.",
        "user_prompt": (
            f"{TASK_QUESTION}\nLet's think step by step. "
            f"End your response with exactly one line formatted as: FINAL ANSWER: <number>"
        ),
        "temperature": 0.0,
    },
]

assert len(PROMPT_VARIANTS) == 10
