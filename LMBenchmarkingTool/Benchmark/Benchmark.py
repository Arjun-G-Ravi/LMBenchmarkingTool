class Benchmark:
    def __init__(self, benchmark_name, metrics='accuracy', subset=None):
        self.benchmark_name = benchmark_name
        self.metrics = metrics
        self.subset = subset

        assert benchmark_name in ['mmlu'], f'{benchmark_name} not found'

        if benchmark_name == 'mmlu':
            from LMBenchmarkingTool.Benchmark import MMLU
            self.benchmark = MMLU(subset=self.subset)
    
    def run(self, model, num_samples=None):
        self.benchmark.run(model, num_samples=num_samples)


if __name__ == '__main__':
    from LMBenchmarkingTool import Benchmark, LLM
    from warnings import filterwarnings
    filterwarnings('ignore')
    model = LLM('gpt2')
    benchmark = Benchmark('mmlu', subset='all')
    benchmark.run(model, num_samples=30)
