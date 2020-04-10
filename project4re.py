import Matrix
import Faller
 
def user_interface():
    row = int(input())
    col = int(input())
    m = Matrix.Matrix(row,col)

    m.print_plain()
    m.print()

    while(True):
    	command = input()
    	command = command.upper()

    	if not command:
    		m.drop(fal)
    		m.print()

    	elif command == "Q":
    		quit()

    	elif command[0] == "F":
    		fal = Faller.Faller(command)
    		fal.print()


if __name__ == '__main__':
    user_interface()
