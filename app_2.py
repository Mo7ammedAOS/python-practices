from Questions_SetUp import FruitsQuestions

Fruits_Colors_Questions = [
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yello\n\n',
    'What color are StrawBerries?\n(a) Yello\n(b) Red\n(c) Blue\n\n'
]

Pure_Questions_Solutions = [
    FruitsQuestions(Fruits_Colors_Questions[0], 'a'),
    FruitsQuestions(Fruits_Colors_Questions[1], 'c'),
    FruitsQuestions(Fruits_Colors_Questions[2], 'b')
]

def run_Test (Pure_Questions_Solutions):
    score = 0
    for Ques in Pure_Questions_Solutions:
        answer = input(Ques.prompt)
        if answer == Ques.answer:
            score += 1
        print()
    print('You got '+ str(score) + '/' + str(len(Pure_Questions_Solutions)) + ' Correct')
    print()
    print('Thank you for taking the test\nHave a happy night ..')

run_Test(Pure_Questions_Solutions)