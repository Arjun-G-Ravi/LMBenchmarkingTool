
class Benchmark:
    def __init__(self, benchmark_name, metrics='accuracy', subset=None):
        self.benchmark_name = benchmark_name
        self.metrics = metrics
        self.subset = subset

        assert benchmark_name in ['mmlu'], f'{benchmark_name} not found'

        if benchmark_name == 'mmlu':
            from LMBenchmarkingTool.Benchmark import MMLU
            self.benchmark = MMLU(subset=self.subset)
    
    def run(self, model):
        self.benchmark.run(model)


# if __name__ == '__main__':

    
        

