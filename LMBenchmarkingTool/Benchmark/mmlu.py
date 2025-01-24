# Massive Multitask Language Understanding (MMLU) 
from datasets import load_dataset

class MMLU:
    def __init__(self, subset=None):
        if subset: self.ds = load_dataset("cais/mmlu", subset)
        else: self.ds = load_dataset("cais/mmlu", 'all')
    
    def run(self, model):
        print('Running mmlu')



if __name__ == '__main__':
    benchmark = MMLU('college_computer_science')
