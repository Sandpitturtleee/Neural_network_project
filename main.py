from functions import optimize_wages, letter_recognition
from variables import byte_A, byte_C, byte_Test, learning_rate

if __name__ == '__main__':
    optimize_wages(learning_rate)
    print("Y: " + str(letter_recognition(byte_C)))



