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
    percent = float(current) / total
    filled = int(width * percent)
    bar = '#' * filled + '-' * (width - filled)
    # Print the progress bar with percentage
    sys.stdout.write(f'\rProgress: [{bar}] ({current}/{total}) {int(percent * 100)}%')
    sys.stdout.flush()