# LMBenchmarkingTool
A benchmarking tool for Language models.

Mission: This library is made for easy bemchmarking of language models on popular benchmarks. I want to load any huggingface model and run any popular benchmark on it with just a few lines of code.

I want to  be able to do:

```python
from LMBenchmarkingTool import Benchmark, LLM
model = LLM('huggingface-model-name')
benchmark = Benchmark('benchmark_name', 'subset_name', 'metric_name')
benchmark.run(model)
```

# Benchmarks Support for future Versions

### Knowledge
- [x] MMLU (Massive Multitask Language Understanding) 
- [ ] SQuAD (Stanford Question Answering Dataset) 
- [ ] TriviaQA
- [ ] GPQA (Graduate-Level Google-Proof Q&A) 

### Coding
- [ ] SWE Benchmark
- [ ] CodeXGLUE
- [ ] HumanEval
- [ ] MBPP (Mostly Basic Programming Problems) 
- [ ] LiveCodeBench
- [ ] Codeforces (optional)

### Reasoning, Common sense
- [x] Hellaswag
- [ ] BIG-bench (also a test for knowledge)
- [ ] HELM(Holistic Evaluation of Language Models)
- [ ] TruthfulQA
- [ ] HLE (Humanity's Last Exam)    
- [ ] PIQA (Physical Interaction Question Answering)
- [ ] SuperGLUE
- [ ] GLUE (General Language Understanding Evaluation) (optional)
- [ ] Arc 1
- [ ] Arc 2

### English Language Understanding
- [ ] LAMBADA
- [ ] Winograd Schema Challenge

### Multilingual
- [ ] TyDi QA
- [ ] T5 Eval
- [ ] XGLUE (optional)
- [ ] C-Eval (optional)

### Math
- [ ] MATH (Mathematics Dataset)
- [ ] GSM8K (Grade School Math 8K)
- [ ] AIME 2024
- [ ] GSM-Hard (optional)
