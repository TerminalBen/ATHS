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
    quizfile = open('capitalquiz'+str(quizNum+1)+'.txt', 'w')
    Answerfile = open('capitalquiz_Answer'+str(quizNum+1)+'.txt','w')
    #header

    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz Form'+str(quizNum + 1))
    quizfile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)


for questionNum in range (50):
    correctAnswer = capitals[states[questionNum]]
    wronganswers = list(capitals.values())
    del wronganswers[wronganswers.index(correctAnswer)]
    wronganswers = random.sample(wronganswers,3)
    answeroptions =wronganswers + list(correctAnswer)
    random.shuffle(answeroptions)
    
quizfile.write(str(questionNum+1)+'. What is the capital of '+ states[questionNum])

for i in range (4):
    quizfile.write('      %s. %s \n' % ('abcd'[i],answeroptions[i]))
quizfile.write('\n')

Answerfile.write('      %s. %s \n' % (questionNum +1, 'abcd'[answeroptions.index(correctAnswer)]))
quizfile.close()
Answerfile.close()

