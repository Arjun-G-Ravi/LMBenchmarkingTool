class Benchmark:
    def __init__(self, benchmark_name, metrics='accuracy', subset=None):
        self.benchmark_name = benchmark_name
        self.metrics = metrics
        self.subset = subset

        assert benchmark_name in ['mmlu', 'hellaswag'], f'{benchmark_name} is not a valid Benchmark name'

        if benchmark_name == 'mmlu':
            from LMBenchmarkingTool.Benchmark import MMLU
            self.benchmark = MMLU(subset=self.subset)
        
        if benchmark_name == 'hellaswag':
            from LMBenchmarkingTool.Benchmark import Hellaswag
            self.benchmark = Hellaswag()
    
    def run(self, model, num_samples=None):
        self.benchmark.run(model, num_samples=num_samples)


if __name__ == '__main__':
    from LMBenchmarkingTool import Benchmark, LLM
    from warnings import filterwarnings
    filterwarnings('ignore')
    print('Loading model...')
    model = LLM('gpt2')
    benchmark = Benchmark('hellaswag')
    benchmark.run(model, num_samples=10)

