class Benchmark:
    def __init__(self, benchmark_name, metrics='accuracy', subclass=None):
        assert benchmark_name in ['mmlu'], f'{benchmark_name} not found'
        

