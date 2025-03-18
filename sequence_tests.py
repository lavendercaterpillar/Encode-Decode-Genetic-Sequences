from part_one import categorize_strand, decode_strand, encode_strand
from part_two import categorize_strand as categorize_encoded_strand

DNA = "GGGGGAAAGGCCCCTTTAAAACCCCTTTTTAAAACCCCCGGGAAAATTTTAAA"
DNA_ENCODED = "G5A3G2C4T3A4C4T5A4C5G3A4T4A3"
RNA = "CCCAAAAAUUUUCCCCGGGUUAAAAUUUUUGGGGGAAACCCGGGGAAAACCCCC"
RNA_ENCODED= "C3A5U4C4G3U2A4U5G5A3C3G4A4C5"
STRAND_BOTH_BASES = "GGGGGAAAUUTTTCCCCAAAACCCCUUUUUAAAATTTTCCCCCAAAAGGGAAA"
ENCODED_BOTH_BASES = "G5A3U2T3C4A4C4U5A4T4C5A4G3A3"
STRAND_NEITHER_BASE = "CCCAAAAAGGGGCCCCCGGGGAAAACCCCGGGGGAAACCCGGGGAAAACCCCC"
ENCODED_NEITHER_BASE = "C3A5G4C5G4A4C4G5A3C3G4A4C5"

def tests():
    part_one_tests()
    part_two_tests()
    print("All tests passed!\n")

def part_one_tests():
    dna_tests()
    rna_tests()
    uncategorized_tests()

def dna_tests():
    result = encode_strand(DNA)
    assert result == DNA_ENCODED     # f"{result}\n{DNA_ENCODED}"  # f string instead of line 25

    result = decode_strand(DNA_ENCODED)
    assert result == DNA

    result = categorize_strand(DNA)
    assert result == 0


def rna_tests():
    result = encode_strand(RNA)
    assert result == RNA_ENCODED

    result = decode_strand(RNA_ENCODED)
    assert result == RNA

    result = categorize_strand(RNA)
    assert result == 1

def uncategorized_tests():
    result = categorize_strand(STRAND_BOTH_BASES)
    assert result == -1

    result = categorize_strand(STRAND_NEITHER_BASE)
    assert result == -1

def part_two_tests():
    result = categorize_encoded_strand(DNA_ENCODED)
    assert result == 0

    result = categorize_encoded_strand(RNA_ENCODED)
    assert result == 1

    result = categorize_encoded_strand(ENCODED_BOTH_BASES)
    assert result == -1, f"{result}"

    result = categorize_encoded_strand(ENCODED_NEITHER_BASE)
    assert result == -1