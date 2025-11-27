# VERSION 1.0 TODOs

### 1. Core Architecture (The Skeleton)
- [ ] Implement `LLM` class with `**kwargs` support (forward args to `AutoModelForCausalLM`).
- [ ] Implement `device_map="auto"` logic to automatically handle CUDA/MPS/CPU.
- [ ] Implement `Tokenizer` logic with mandatory **Batching** (`padding=True`, `return_tensors="pt"`).

### 2. The Benchmark Engine (The Brains)
- [ ] Create Base `Benchmark` class.
- [ ] Implement **"Mode" differentiation**:
  - [ ] Mode A: **LogProbability** (for MMLU, ARC, HellaSwag) -> Returns token probabilities.
  - [ ] Mode B: **Generative** (for GSM8K) -> Returns generated string.
- [ ] Create `PromptManager` / Template Dictionary (separate from logic).
- [ ] **Implement "Scoring" Logic:**
  - [ ] Exact Match (for Multiple Choice).
  - [ ] Regex Extraction + Equivalence (for GSM8K Math).

### 3. The Tasks (The Big 4)
- [ ] Implement ARC Challenge (Start here - Easiest LogProb task).
- [ ] Implement HellaSwag (LogProb).
- [ ] Implement MMLU (Complex LogProb prompts).
- [ ] Implement GSM8K (Generative + Regex Parsing).

### 4. Resilience & Performance
- [ ] Implement **Caching / State Saving**:
  - [ ] Check for existing `.jsonl` results file before running a sample.
  - [ ] Append new results to file immediately after processing.
  - [ ] Logic to skip already-processed IDs (Resume functionality).
- [ ] Feature: Configure Zero-shot vs. Few-shot (n-shot) prompts.

### 5. User Experience (UX)
- [ ] Progress Bar (Rich/tqdm) showing:
  - [ ] Progress %
  - [ ] Time Elapsed / Time Remaining
  - [ ] Current Running Average Score (optional).
- [ ] CLI Entry Point (`benchmark-tool --model ...`).
- [ ] **Final Report Generation:** Export a clean `summary.json` or print a final table with the score.