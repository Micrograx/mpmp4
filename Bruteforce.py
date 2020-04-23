from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer
# We need to import numpy and numba to get the improved perfromance and run the
# Code in 30 minutes compared to 2-3 days :)
# Update: By separating the code that checks if a sequence
# Has 2 consecutive equal instructions, we can achieve
# A runtime of 8 minutes YAY!!

# Initialize all the possible card combinations
def initialize(count):
    c_ind = (2**count) - 1
    initialCards = np.zeros((c_ind, count), dtype=np.int8)
    for i in range(1,2**count):
        initialCards[i-1] = (change_base(i, count, 2))
        print('indice {}, cartas: {}'.format(i-1, initialCards[i-1]))
    return initialCards

# Transforms an integer to an array of fixed bites in a fixed base
# Used to encode the card combinations in binary (1: face up, 0: face down)
# And to encode each tried instruction set from integer to instructions mod cards
@jit(nopython=True)
def change_base(numero, bites, base):
    res = np.zeros((bites), dtype=np.int8)
    for i in range(bites-1, -1, -1):
        res[i] = numero % base
        numero = numero // base
    return res

# Main function to check all possible instructions
@jit(nopython=True)
def trabajar(initialCards):
    count = len(initialCards[0])
    c_ind = (2**count) - 1
    intento  = count**(c_ind - 2)
    contador = 0

    res = []
    while(intento < (count**c_ind)):
        newCards = initialCards.copy()
        sequence = change_base(intento, c_ind, count)
        valid = True
        for i in range(len(sequence) - 2):
            # If two consecutives instructions are equal, abort and check next instructions
            if (sequence[i] == sequence[i+1]):
                valid = False
                break

        if (valid):
            # For every card combination
            for j in range(len(newCards)):
                # Try the proposed instructions
                for i in range(len(sequence)):
                    newCards[j][sequence[i]] = 1 if newCards[j][sequence[i]] == 0 else 0
                    # If after any instruction we have all cards face down, dont continue turning cards
                    if(np.count_nonzero(newCards[j]) == 0):
                        break
                # If after executing all instructions we dont have all cards face down
                # Dont even bother trying to analyze the other combinations
                if(np.count_nonzero(newCards[j]) != 0):
                    break

            # When we find a set of instructions that work on all card combinations, save it
            if (int(np.count_nonzero(newCards)) == 0):
                print("-------------------------------", contador)
                print(sequence)
                contador = contador + 1
                res.append(sequence)
        intento = intento + 1
    return res


if __name__ == "__main__":
    # First we run the functons wiht only 2 cards to pre-compile them
    # Using jit(nopython)
    initialCards = initialize(2)
    start = timer()
    trabajar(initialCards)
    print("Time Elapsed: ", timer()-start)

    #Then we run the function with the desired card ammount
    secondCards = initialize(4)
    start = timer()
    finales = trabajar(secondCards)
    print("Time Elapsed2: {}".format(timer()-start))
    with open("Solutions/4cards.txt", "a+") as file_object:
        for item in finales:
            file_object.write("%s \n" % item)
