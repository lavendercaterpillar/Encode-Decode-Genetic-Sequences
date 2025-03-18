from part_one import decode_strand, encode_strand

def driver():
    print("-------------------------")
    print("Encoding all sequences...")
    print("-------------------------")

    all_sequences = [
        "GGGGGAAAGGCCCCTTTAAAACCCCTTTTTAAAACCCCCGGGAAAATTTTAAA",
        "GGGGGAAAUUCCCCTTTAAAACCCCUUUUUAAAACCCCCGGGAAAATTTTAAA",
        "CCCAAAAATTTTCCCCGGGTTAAAATTTTTGGGGGAAACCCGGGGAAAACCCCC",
        "CCCAAAAAGGGGCCCCCGGGGAAAACCCCGGGGGAAACCCGGGGAAAACCCCC"
    ]
    encoded_sequences = []

    for sequence in all_sequences:
        encoded_strand = encode_strand(sequence)
        encoded_sequences.append(encoded_strand)

    print("-------------------------")
    print("Categorizing encoded sequences...")
    print("-------------------------")

    categorized_sequences = {}
    categorized_sequences[-1] = []  # strands that can't be determined
    categorized_sequences[0] = []  # dna strands
    categorized_sequences[1] = []  # rna strands

    for sequence in encoded_sequences:
        category = categorize_strand(sequence)
        categorized_sequences[category].append(sequence)

    print("-------------------------")
    print("Decoding and listing undetermined sequences for review...")
    print("-------------------------")

    for sequence in categorized_sequences[-1]:
        decoded = decode_strand(sequence)
        print(decoded)


# Returns 0 for DNA (Contains "T" bases)
# Returns 1 for RNA (Contains "U" bases)
# Returns -1 if the strand cannot be categorized:
#   - Contains both "T" and "U" in the same strand
#   - There are no "T" or "U" bases in the strand
def categorize_strand(strand):
    is_t_present = False
    is_u_present = False

    for index in range(0, len(strand) - 1):
        base = strand[index]
        if base == "T":
            is_t_present = True

        if base == "U":
            is_u_present = True

    has_both_bases = is_t_present and is_u_present
    has_neither_base = (not is_t_present) and (not is_u_present)
    if (has_both_bases or has_neither_base):
        return -1

    return 0 if is_t_present else 1