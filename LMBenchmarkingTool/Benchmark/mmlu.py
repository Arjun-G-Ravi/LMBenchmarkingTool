# Massive Multitask Language Understanding (MMLU) 
from datasets import load_dataset

class MMLU:
    def __init__(self, subset=None):
        if subset: self.ds = load_dataset("cais/mmlu", subset)
        else: self.ds = load_dataset("cais/mmlu", 'all')
    
    def run(self, model, num_samples=None):
        print('MMLU Benchmarking Started...')
        from LMBenchmarkingTool import prompting_template1, _progress_bar
        score = 0
        mapping = {0:'A', 1:'B', 2:'C', 3:'D'}
        assert model.return_loss == True, 'Set model.return_loss to be True'

        
        if num_samples is None:
            num_samples = len(self.ds['test'])

        tot = min(num_samples, len(self.ds['test']))
        print('Total benchmarks:',tot)
        
        for i in range(tot):
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
            _progress_bar(i+1, tot)
        
        print('\n')
        print('BENCHMARKING RESULTS:')
        print(f'Total questions: {tot}')
        print(f'Correct Answers {score}' )
        print(f'MMLU Benchmarking Score: {(score*100/(i+1)):.3f}')

        

