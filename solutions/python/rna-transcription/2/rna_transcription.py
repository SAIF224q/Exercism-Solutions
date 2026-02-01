def to_rna(dna_strand):
    dna_to_rna_dic = {"G":"C", "C":"G", "T":"A", "A":"U"}
    rna_strand = []
    for nucleo in list(dna_strand):
        rna_strand.append(dna_to_rna_dic[nucleo])
    return "".join(rna_strand)
