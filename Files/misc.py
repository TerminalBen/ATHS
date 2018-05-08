#! python3
#!QuizGenerator
'''with open(filename, mode) as fileobject:
    for line in fileobject:
        # process line'''

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
<<<<<<< HEAD
    
=======
    quizfile = open('capitalquiz%s.txt' % quiznum+1 , 'w')
    Answerfile = open ('capitalquiz_Answer%s.txt'%quizNum+1,'w')
    #header

    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizfile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range (50):
        correctAnswer = capitals[states[questionNum]]
        wronganswers = list(capitals.values())
        del wronganswers(correctAnswer)
        wronganswers = random.sample(wronganswers,3)
        answeroptions = wronganswers + [correctAnswer]
        random.shuffle(answeroptions)

    quizfile
>>>>>>> a19cdc0525893dd8c8c1e036276a0aece5e504f9
