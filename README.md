# LMBenchmarkingTool
A benchmarking tool for Language models


This library is made for easy bemchmarking of language models on popular benchmarks.

# Initial Setup
- I want it to run on huggingface models
- I want it to run on popular benchmarks like GLUE, SuperGLUE, SQuAD, etc.
- I want it to run on popular metrics like F1, Accuracy, etc.
- I want it to properly visualize the results(matplotlib)

# Future plans
- I want it to run on my own custom


I want to  be able to do:

```python
from LMBenchmarkingTool import Benchmark
model = huggingface-model()
benchmark = Benchmark()
benchmark.run(model)

```