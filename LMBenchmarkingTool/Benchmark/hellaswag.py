from datasets import load_dataset

class Hellaswag:
    def __init__(self):
        self.ds = load_dataset("Rowan/hellaswag")
    
    def run(self, model, num_samples=None):
        print('Hellaswag Benchmarking Started...')
        from LMBenchmarkingTool import prompting_template1, _progress_bar
        score = 0
        mapping = {0:'A', 1:'B', 2:'C', 3:'D'}
        assert model.return_loss == True, 'Set model.return_loss to be True'
        
        if num_samples is None:
            num_samples = len(self.ds['validation'])
            print(num_samples)
        
        tot = min(num_samples, len(self.ds['validation']))
        print('Total benchmarks:', tot)

        for i in range(tot):
            context = self.ds['validation']['ctx_a'][i]
            endings = self.ds['validation']['endings'][i]
            correct_answer = int(self.ds['validation']['label'][i])

            if len(endings) != 4:
                print('No 4 endings')
                continue

            each_choice = {}
            for ending,num in zip(endings,[0,1,2,3]):
                each_choice[num] = f'{context} {ending}'
            
            losses = {}
            for j in range(4):
                losses[j] = (model.calculate_loss(each_choice[j]))
            predicted_choice = min(losses, key=losses.get)

            if predicted_choice == correct_answer:
                score += 1            
            _progress_bar(i+1, tot)
        
        print('\n')
        print('BENCHMARKING RESULTS:')
        print(f'Total questions: {tot}')
        print(f'Correct Answers {score}')
        print(f'Hellaswag Benchmarking Score: {(score*100/(i+1)):.3f}')