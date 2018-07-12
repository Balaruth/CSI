analysis = {"Black Hair": 0,
            "Brown Hair": 0,
            "Blonde Hair": 0,
            "Square Face": 0,
            "Round Face": 0,
            "Oval Face": 0,
            "Blue Eyes": 0,
            "Green Eyes": 0,
            "Brown Eyes": 0,
            "Female Gender": 0,
            "Male Gender": 0,
            "White Race": 0,
            "Black Race": 0,
            "Asian Race": 0,}

print "WHO ATE THE ICE CREAM?!"
print
print "Fetching DNA to be analysed..."
print
dna_file = open("dna.txt", "r")
dna = dna_file.read()
print dna
dna_file.close()
print
print "Done."
print
print "Now analysing DNA to determine culprit..."

analysis["Black Hair"] = dna.count("CCAGCAATCGC")
analysis["Brown Hair"] = dna.count("GCCAGTGCCG")
analysis["Blonde Hair"] = dna.count("TTAGCTATCGC")

analysis["Square Face"] = dna.count("GCCACGG")
analysis["Round Face"] = dna.count("ACCACAA")
analysis["Oval Face"] = dna.count("AGGCCTCA")

analysis["Blue Eyes"] = dna.count("TTGTGGTGGC")
analysis["Green Eyes"] = dna.count("GGGAGGTGGC")
analysis["Brown Eyes"] = dna.count("AAGTAGTGAC")

analysis["Female Gender"] = dna.count("TGAAGGACCTTC")
analysis["Male Gender"] = dna.count("TGCAGGAACTTC")

analysis["White Race"] = dna.count("AAAACCTCA")
analysis["Black Race"] = dna.count("CGACTACAG")
analysis["Asian Race"] = dna.count("CGCGGGCCG")

print
print "The culprit has the following genetic traits:"
print
for check in analysis:
  if analysis[check] == 1:
    print check