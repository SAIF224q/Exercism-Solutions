def proteins(strand):
    codon_table = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
    }
    chunk = 3
    codons = [strand[i:i+chunk] for i in range(0, len(strand), chunk)]
    amino_seq = []
    for codon in codons:
        if codon_table[codon] == "STOP":
            break
        else:
            amino_seq.append(codon_table[codon])
    return amino_seq

