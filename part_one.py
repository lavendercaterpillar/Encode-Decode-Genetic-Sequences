def driver():
    print("-------------------------")
    print("Categorizing sequences...")
    print("-------------------------")

    all_sequences = [
        "GGGGGAAAGGCCCCTTTAAAACCCCTTTTTAAAACCCCCGGGAAAATTTTAAA",
        "GGGGGAAAUUCCCCTTTAAAACCCCUUUUUAAAACCCCCGGGAAAATTTTAAA",
        "CCCAAAAATTTTCCCCGGGTTAAAATTTTTGGGGGAAACCCGGGGAAAACCCCC",
        "CCCAAAAAGGGGCCCCCGGGGAAAACCCCGGGGGAAACCCGGGGAAAACCCCC"
    ]

    categorized_sequences = {}
    # categorized_sequences["undetermined"] = [] # Error! strands that can't be determined
    # categorized_sequences["dna"] = [] # dna strands
    # categorized_sequences["rna"] = [] # rna strands
    categorized_sequences[-1] = [] # Error! strands that can't be determined
    categorized_sequences[0] = [] # dna strands
    categorized_sequences[1] = [] # rna strands

    for sequence in all_sequences:
        category = categorize_strand(sequence)
        # categorized_sequences[category].append(sequence) # Error! categorized_sequences is a dictionary!
        categorized_sequences[category] = sequence

    print("-------------------------")
    print("Encoding sequences for storage...")
    print("-------------------------")

    encoded_sequences = []

    for sequence in all_sequences:
        encoded_strand = encode_strand(sequence)
        encoded_sequences.append(encoded_strand)

    print("-------------------------")
    print("Listing undetermined sequences for review...")
    print("-------------------------")

    for sequence in categorized_sequences[-1]:
        print(sequence)

# Returns 0 for DNA (Contains "T" bases)
# Returns 1 for RNA (Contains "U" bases)
# Returns -1 if the strand cannot be categorized: 
#   - Contains both "T" and "U" in the same strand 
#   - There are no "T" or "U" bases in the strand
def categorize_strand(strand):
    is_t_present = False
    is_u_present = False

    for base in strand:  # checks if T or U present in the sequence
        if base == "T":
            is_t_present = True

        if base == "U":
            is_u_present = True

    has_both_bases = (is_t_present and is_u_present)
    has_neither_base = (not is_t_present and not is_u_present)
    if (has_both_bases or has_neither_base):
        return -1

    return 0 if is_t_present else 1

def encode_strand(strand):
    if not strand:
        return ""

    encoding = []
    count = 1

    for index in range(1, len(strand)):
        if strand[index - 1] == strand[index]:
            count += 1
        else:
            new_entry = strand[index - 1] + str(count) # TypeError
            encoding.append(new_entry)
            count = 1
        
    # Append the last character and its count
    new_entry = strand[ - 1] + str(count) 
    encoding.append(new_entry)
    # encoding.append(strand[-1] + str(count))

    return "".join(encoding)

def decode_strand(encoding):
    if not encoding:
        return ""

    strand = []

    for index in range(0, len(encoding) - 1, 2):
        letter = encoding[index]
        count = int(encoding[index + 1])  # ValueError: invalid literal for int() with base 10: 'G'
        next_base = [letter] * count
        strand.extend(next_base)

    return "".join(strand)
