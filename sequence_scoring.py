import sys

def input_aligned_sequences(filename):
    sequence = ""
    sequences = []
    sequence_name_mode = -1
    with open(filename) as fileobj:
        print("SEQUENCES FOUND")
        for line in fileobj:
            if line[:1] == ">":
                print(line[1:-1])
                if sequence != "":
                    sequences.append(sequence)
                sequence = ""
            else:
                sequence += line[:-1]
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
    sequences = input_aligned_sequences(sys.argv[1])
    if len(sys.argv) == 3:
        if sys.argv[2] == "-A":
            check_aligned_sequences(sequences)

if __name__ == "__main__":
    main()
