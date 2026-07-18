# Prompt Comparison Report

**Task:** Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?

**Expected answer:** 58

## Summary Table

| # | Variant | Temperature | Correct? |
|---|---|---|---|
| 1 | Naive / Zero-shot | 0.7 | ✅ |
| 2 | Zero-shot + explicit instruction | 0.7 | ✅ |
| 3 | System prompt (role-based) | 0.7 | ✅ |
| 4 | Few-shot prompting | 0.7 | ✅ |
| 5 | Chain-of-thought (explicit) | 0.7 | ✅ |
| 6 | Few-shot + Chain-of-thought combined | 0.7 | ✅ |
| 7 | System + Chain-of-thought | 0.7 | ❌ |
| 8 | Low temperature (0.0) | 0.0 | ❌ |
| 9 | High temperature (1.5) | 1.5 | ❌ |
| 10 | Constrained output format | 0.0 | ❌ |

## Full Responses

### #1 — Naive / Zero-shot
*Technique: Bare question, no instructions at all.*

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
```

**Response:**
```
Sarah has **58** apples now. 

Here is the step-by-step breakdown:

1. **Initial apples:** 3 boxes × 12 apples = 36 apples
2. **After giving some away:** 36 - 8 = 28 apples
3. **Buying more:** 2 boxes × 15 apples = 30 apples
4. **Total apples:** 28 + 30 = 58 apples
```

**Correct:** ✅ Yes

---

### #2 — Zero-shot + explicit instruction
*Technique: Adds a direct instruction to show the working.*

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now? Show your working and give the final number clearly.
```

**Response:**
```
Here is the step-by-step working to find the total number of apples Sarah has:

1. **Calculate the initial number of apples:**
   Sarah starts with 3 boxes of 12 apples each.
   $$\text{Initial apples} = 3 \times 12 = 36\text{ apples}$$

2. **Subtract the apples she gives away:**
   She gives away 8 apples.
   $$\text{Apples remaining} = 36 - 8 = 28\text{ apples}$$

3. **Calculate the number of new apples she buys:**
   She buys 2 more boxes of 15 apples each.
   $$\text{New apples} = 2 \times 15 = 30\text{ apples}$$

4. **Calculate the final total:**
   Add the new apples to her remaining apples.
   $$\text{Total apples} = 28 + 30 = 58\text{ apples}$$

Sarah now has **58** apples.
```

**Correct:** ✅ Yes

---

### #3 — System prompt (role-based)
*Technique: A system prompt sets a persona/role before the same question.*

**System prompt:** You are a meticulous math tutor who never skips a calculation step.

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
```

**Response:**
```
Hello! I would be absolutely delighted to help you solve this math problem step-by-step. We will break down each part of Sarah's apple journey so we don't miss a single detail. 

Let's go through it step-by-step!

---

### **Step 1: Find the initial number of apples Sarah starts with**
Sarah starts with **3 boxes** of apples, and each box contains **12 apples**. 

To find the total, we need to multiply the number of boxes by the number of apples in each box:
$$\text{Initial Apples} = 3 \times 12$$

Let's calculate $3 \times 12$ by adding 12 three times to be absolutely sure:
1. First, add the first two boxes: 
   $$12 + 12 = 24$$
2. Next, add the third box to that sum: 
   $$24 + 12 = 36$$

So, Sarah starts with **36 apples**.

---

### **Step 2: Subtract the apples she gives away**
Sarah gives away **8 apples**. We need to subtract this from her current total of 36 apples:
$$\text{Remaining Apples} = 36 - 8$$

Let's perform this subtraction step-by-step:
1. First, subtract 6 to get to a friendly tens number: 
   $$36 - 6 = 30$$
2. Since we need to subtract 8 in total, we still need to subtract 2 more (because $8 = 6 + 2$): 
   $$30 - 2 = 28$$

So, after giving away 8 apples, Sarah has **28 apples** left.

---

### **Step 3: Calculate how many new apples she buys**
Sarah then buys **2 more boxes**, and each of these new boxes contains **15 apples**. 

To find out how many new apples she bought, we multiply the number of new boxes by the number of apples in each:
$$\text{New Apples} = 2 \times 15$$

Let's calculate $2 \times 15$ by adding 15 two times:
$$15 + 15 = 30$$

So, Sarah bought **30 new apples**.

---

### **Step 4: Find the final total of apples**
Finally, we add the new apples she bought to the apples she had remaining:
$$\text{Final Total} = 28 \text{ (remaining apples)} + 30 \text{ (new apples)}$$

Let's add these two numbers together:
1. Add the tens place first: 
   $$20 + 30 = 50$$
2. Now, add the remaining 8 from the 28: 
   $$50 + 8 = 58$$

---

### **Conclusion**
Sarah has exactly **58 apples** now!
```

**Correct:** ✅ Yes

---

### #4 — Few-shot prompting
*Technique: Two worked examples of similar problems precede the real question.*

**User prompt:**
```
Q: Tom has 4 packs of pencils with 6 pencils each. He loses 5 pencils, then buys 3 more packs of 6. How many pencils does he have now?
A: 4 packs x 6 = 24. 24 - 5 = 19. 3 packs x 6 = 18. 19 + 18 = 37. Tom has 37 pencils.

Q: A bakery has 5 trays of 8 muffins each. They sell 12 muffins, then bake 2 more trays of 8. How many muffins are there now?
A: 5 trays x 8 = 40. 40 - 12 = 28. 2 trays x 8 = 16. 28 + 16 = 44. The bakery has 44 muffins.

Q: Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
A:
```

**Response:**
```
3 boxes x 12 = 36. 36 - 8 = 28. 2 boxes x 15 = 30. 28 + 30 = 58. Sarah has 58 apples.
```

**Correct:** ✅ Yes

---

### #5 — Chain-of-thought (explicit)
*Technique: Adds 'Let's think step by step' to trigger explicit reasoning.*

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
Let's think step by step.
```

**Response:**
```
Let's think step by step:

1. **Find the initial number of apples:** 
   Sarah starts with 3 boxes of 12 apples each. 
   $$3 \times 12 = 36 \text{ apples}$$

2. **Subtract the apples she gives away:** 
   She gives away 8 apples.
   $$36 - 8 = 28 \text{ apples}$$

3. **Calculate the number of new apples she buys:** 
   She buys 2 more boxes with 15 apples in each.
   $$2 \times 15 = 30 \text{ apples}$$

4. **Add the new apples to her current total:** 
   $$28 + 30 = 58 \text{ apples}$$

Sarah has **58** apples now.
```

**Correct:** ✅ Yes

---

### #6 — Few-shot + Chain-of-thought combined
*Technique: Combines worked examples AND an explicit step-by-step instruction.*

**User prompt:**
```
Q: Tom has 4 packs of pencils with 6 pencils each. He loses 5 pencils, then buys 3 more packs of 6. How many pencils does he have now?
A: 4 packs x 6 = 24. 24 - 5 = 19. 3 packs x 6 = 18. 19 + 18 = 37. Tom has 37 pencils.

Q: A bakery has 5 trays of 8 muffins each. They sell 12 muffins, then bake 2 more trays of 8. How many muffins are there now?
A: 5 trays x 8 = 40. 40 - 12 = 28. 2 trays x 8 = 16. 28 + 16 = 44. The bakery has 44 muffins.

Q: Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
A: Let's think step by step.
```

**Response:**
```
3 boxes x 12 = 36. 36 - 8 = 28. 2 boxes x 15 = 30. 28 + 30 = 58. Sarah has 58 apples.
```

**Correct:** ✅ Yes

---

### #7 — System + Chain-of-thought
*Technique: Combines a role-setting system prompt with explicit step-by-step reasoning.*

**System prompt:** You are a careful math tutor. Always reason step by step before answering.

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
Let's think step by step.
```

**Response:**
```
[ERROR] Request error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3.5-flash\nPlease retry in 33.564812317s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3.5-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '33s'}]}}
```

**Correct:** ❌ No

---

### #8 — Low temperature (0.0)
*Technique: Same as the best-performing prompt above, but temperature forced to 0 for determinism.*

**System prompt:** You are a careful math tutor. Always reason step by step before answering.

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
Let's think step by step.
```

**Response:**
```
[ERROR] Request error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3.5-flash\nPlease retry in 33.332150751s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3.5-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '33s'}]}}
```

**Correct:** ❌ No

---

### #9 — High temperature (1.5)
*Technique: Same prompt as #8, but with a high temperature to test consistency loss.*

**System prompt:** You are a careful math tutor. Always reason step by step before answering.

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
Let's think step by step.
```

**Response:**
```
[ERROR] Request error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3.5-flash\nPlease retry in 33.05950067s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3.5-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '33s'}]}}
```

**Correct:** ❌ No

---

### #10 — Constrained output format
*Technique: Forces a strict final-answer-only format to test whether structure hurts reasoning.*

**System prompt:** You are a careful math tutor. Always reason step by step before answering.

**User prompt:**
```
Sarah has 3 boxes of apples. Each box contains 12 apples. She gives away 8 apples, then buys 2 more boxes of 15 apples each. How many apples does she have now?
Let's think step by step. End your response with exactly one line formatted as: FINAL ANSWER: <number>
```

**Response:**
```
[ERROR] Request error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3.5-flash\nPlease retry in 32.664363307s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3.5-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '32s'}]}}
```

**Correct:** ❌ No

---
