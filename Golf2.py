import os
file_path = os.path.join('C:\\', 'Users', 'ronnv', 'Desktop', 'golf.txt')
def main():

    data = open(file_path, 'r')
    name = data.readline()

    while name != '':

        score = data.readline()
        name = name.rstrip('\n')
        score = score.rstrip('\n')
        print(name + ' score is ' + score)
        name = data.readline()
  
    data.close()

main()
