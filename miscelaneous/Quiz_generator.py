import random

# The quiz data. Keys are states and values are their capitals.
vcapitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

   #generate 35 quiz files
for quizNum in range(35):
      quizFile = open ('/Users/bentolima/Documents/Projects/ATHS/Quiz/capitalQuiz%s.txt' % (quizNum +1) , 'w')
      answerfile = open ('/Users/bentolima/Documents/Projects/ATHS/Quiz/capital_answer%s' % (quizNum+1) , 'w')

      quizFile.write('Name: \n\n Date: \n\n')   
      quizFile.write((' '*20)+'quizFile number %d' %(quizNum+1))
      quizFile.write('\n\n')

      states = list(vcapitals.keys())
      random.shuffle(states)

      for questionNum in range(50):
         correctAnswer = vcapitals[states[questionNum]]
         wrongAnswer = list(vcapitals.values())
         del wrongAnswer[wrongAnswer.index(correctAnswer)]
         wrongAnswer = random.sample(wrongAnswer,3)
         
         answerOptions = wrongAnswer + [correctAnswer]
         random.shuffle(answerOptions) # randomize the order of the answers

        # Write the question and answer options to the quiz file.
         quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
         for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
         quizFile.write('\n')

        # Write out the answer key to a file.
         answerfile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerfile.close()

