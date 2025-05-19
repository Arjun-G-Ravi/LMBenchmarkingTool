# LMBenchmarkingTool
A benchmarking tool for Language models


This library is made for easy bemchmarking of language models on popular benchmarks.

# Initial Setup
-run on different huggingface models
- run on popular benchmarks like MMLU, GLUE, SuperGLUE, SQuAD, etc.
- run on popular metrics like F1, Accuracy, etc.
- properly visualize the results(matplotlib)
- Right now, you will be able to run only one benchmark on one model at a time.

# Future plans
- run on my own custom models
- run on multiple benchmarks at a time
- run on multiple models at a time


I want to  be able to do:

```python
from LMBenchmarkingTool import Benchmark
model = huggingface-model()
benchmark = Benchmark('benchmark_name', 'subset_name', 'metric_name')
benchmark.run(model)
```

# Benchmarks

### Knowledge
- [x] MMLU (Massive Multitask Language Understanding) 
- [ ] SQuAD (Stanford Question Answering Dataset) 
- [ ] OpenBookQA

### Coding
- [ ] SuperGLUE
- [ ] HumanEval
- [ ] CodeXGLUE
- [ ] SWE Benchmark
- [ ] Codeforces

### Reasoning, Common sense
- [x] Hellaswag
- [ ] BIG-bench (also knowledge)
- [ ] HELM(Holistic Evaluation of Language Models)
- [ ] TruthfulQA
- [ ] PIQA (Physical Interaction Question Answering)
- [ ] StoryCloze
- [ ] GLUE (General Language Understanding Evaluation) 


### English Language Understanding
- [ ] LAMBADA

### Other Languages
- [ ] TyDi QA

### Math
- [ ] MATH (Mathematics Dataset)
- [ ] GSM8K (Grade School Math 8K)

More
- Codeforces
- LiveCodeBench
- AIME 2024
- GPTQ Diamond
