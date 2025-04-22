# 염기 코돈 개수
# 염기 서열 3개가 묶인 것을 코돈이라 한다.
# ex)ctacaatgtcagtacccattgcattagccgg ex)cta, caa, tgt
dna = input("염기 서열을 입력해해주세요: ")
dict_dna = {}

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if len(codon) == 3:
        if codon not in dict_dna:
            dict_dna[codon] = 0
        dict_dna[codon] += 1

print(dict_dna)
