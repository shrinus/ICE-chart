#EQ = input("Enter the chemical equation\n ")
EQ = "AgNO3 + 2CaO = Ag2O + Ca(NO3)2"


#EQ = [EQ.split(" = ")[i].split(" + ") for i in range(2)]

#EQ = [[[1, j] if j[0].isalpha() else [j[0], j[1:]] for j in i] for i in EQ]

EQ = [[[1, j] if j[0].isalpha() else [j[0], j[1:]] for j in EQ.split(" = ")[i].split(" + ")] for i in range(2)]

print(EQ)