def to_rna(dna_strand):
    dna_to_rna_dic = {"G":"C", "C":"G", "T":"A", "A":"U"}
    rna_strand = []
    dna_strand_nucleo = list(dna_strand)
    for nucleo in dna_strand_nucleo:
        rna_strand.append(dna_to_rna_dic[nucleo])
    return "".join(rna_strand)
