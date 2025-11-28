from LMBenchmarkingTool import Benchmark, LLM
model = LLM('Qwen/Qwen2.5-3B-Instruct', device_map='cuda')
benchmark = Benchmark('hellaswag')
benchmark.run(model, num_samples=100) 