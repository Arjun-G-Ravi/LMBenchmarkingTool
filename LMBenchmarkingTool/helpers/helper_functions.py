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