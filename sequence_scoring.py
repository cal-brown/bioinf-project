import sys

def input_aligned_sequences(filename, print_on=False):
    sequence = ""
    sequences = []
    sequence_name_mode = -1
    with open(filename) as fileobj:
        if print_on:
            print("SEQUENCES FOUND")
        for line in fileobj:
            if line[:1] == ">":
                if print_on:
                    print(line[1:-1])
                if sequence != "":
                    sequences.append(sequence)
                sequence = ""
            else:
                sequence += line[:-1]
    sequences.append(sequence)
    if print_on:
        print("")
    return sequences

def check_aligned_sequences(sequences):
    print("SEQUENCE ARRAY")
    for element in sequences:
        print(element)
    print("")

def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        raise ValueError("Incorrect command line argument usage. Correct: python sequence_scoring.py [filename]")
    print("\n" + "---------------[" + sys.argv[1] + "]---------------" + "\n")
    sequences = input_aligned_sequences(sys.argv[1], print_on=True)
    if len(sys.argv) == 3:
        if sys.argv[2] == "-A":
            check_aligned_sequences(sequences)

if __name__ == "__main__":
    main()
