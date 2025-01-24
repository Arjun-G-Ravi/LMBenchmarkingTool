def prompting_template1(question, choices):
    '''
    Question: <Question>
    Choices:
    (A) Option A
    (B) Option B
    (C) Option C
    (D) Option D
    Answer:
    '''
    return  f"Question: {question}\nChoices: {choices}\nAnswer: "

def _progress_bar(current, total, width=50):
    import sys
    # Calculate the percentage of completion
    percent = float(current) / total
    
    # Calculate the number of filled and empty bar segments
    filled = int(width * percent)
    bar = '#' * filled + '-' * (width - filled)
    
    # Print the progress bar with percentage
    sys.stdout.write(f'\rProgress: [{bar}] {int(percent * 100)}%')
    sys.stdout.flush()