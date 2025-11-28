from LMBenchmarkingTool import Benchmark, LLM
model = LLM('Qwen/Qwen2.5-3B-Instruct')
benchmark = Benchmark('mmlu')
benchmark.run(model, num_samples=100) 