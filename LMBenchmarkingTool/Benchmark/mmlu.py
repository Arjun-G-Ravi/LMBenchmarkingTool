# Massive Multitask Language Understanding (MMLU) 
from datasets import load_dataset

class MMLU:
    def __init__(self, subset=None):
        if subset: self.ds = load_dataset("cais/mmlu", subset)
        else: self.ds = load_dataset("cais/mmlu", 'all')
    
    def run(self, model, num_samples=10):
        print('Running mmlu...')
        from LMBenchmarkingTool import prompting_template1
        score = 0
        mapping = {0:'A', 1:'B', 2:'C', 3:'D'}
        if model.return_loss == False:
            print('Set model.return_loss to be True') # warning
            raise 'Error'
        for i in range(min(num_samples, len(self.ds['test']))):
            question = self.ds['test']['question'][i]
            choices = self.ds['test']['choices'][i]
            choices_out = ''
            each_choice = []
            for choice,option in zip(choices, ['A', 'B', 'C', 'D']):
                each_choice.append(f'\n({option}) {choice}')
            choices_out = ''.join(each_choice)
            correct_answer = mapping[self.ds['test']['answer'][i]]
            full_prompt = prompting_template1(question, choices_out)
            
            losses = {}
            for j in each_choice:
                model_prediction = full_prompt + j[1:]
                # print(model_prediction)
                model_prediction_option = j[1:][1] # This is the option A, B,C or D
                losses[model_prediction_option] = (model.calculate_loss(model_prediction))
            
            # print(losses)
            
            predicted_choice = min(losses, key=losses.get)
            if predicted_choice == correct_answer:
                # print('Correct')
                score += 1
        
        print(f'-'*20)
        print('BENCHMARKING RESULTS:')
        print(f'Total questions: {i+1}')
        print(f'Correct Answers {score}' )
        print(f'MMLU Benchmarking Score: {(score*100/i+1):3f}')

        

