EQ = input("\n\nEnter the chemical equation. Surround \"+\" and \"+\" with spaces. ex: AgNO3 + 2CaO = Ag2O + Ca(NO3)2\n ")
K = input("\nEnter the equilibrium constant\n ")
EQ = [[[1, j] if j[0].isalpha() else [j[0], j[1:]] for j in i.split(" + ")] for i in EQ.split(" = ")]
[[j.append(input("\nWhat is the concentration of " + j[1] + "? ")) for j in i] for i in EQ]