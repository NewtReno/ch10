#Reads each player's name and golf score as input

#Save to golf.txt

result = open('golf.txt', 'w')

while True:

    name = str(input('Player Name(or q to quit):'))

    if name == 'q':

        break

    if name == '' or not name.isalpha():
        raise ValueError('Invalid name')
    score = input('Player Score:')
    if score == '' or not score.isdigit():
        raise ValueError('Score must be an integer')



#write to file golf.txt

    result.write(name + '\n')



    result.write(str(score) + '\n')



result.close()
