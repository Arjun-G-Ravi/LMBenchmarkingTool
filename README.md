# LMBenchmarkingTool
A benchmarking tool for Language models


This library is made for easy bemchmarking of language models on popular benchmarks.

# Initial Setup
- I want it to run on huggingface models
- I want it to run on popular benchmarks like MMLU, GLUE, SuperGLUE, SQuAD, etc.
- I want it to run on popular metrics like F1, Accuracy, etc.
- I want it to properly visualize the results(matplotlib)
- Right now, you will be able to run only one benchmark on one model at a time.

# Future plans
- I want it to run on my own custom
- I want it to run on multiple benchmarks at a time
- I want it to run on multiple models at a time


I want to  be able to do:

```python
from LMBenchmarkingTool import Benchmark
model = huggingface-model()
benchmark = Benchmark('benchmark_name', 'subset_name', 'metric_name')
benchmark.run(model)
```