# Max bending moment for a simply supported beam with a central point load
# Inputs: P (kN), L (m)  -> Output: M (kN·m)

P = float(input("Enter point load P (kN): "))
L = float(input("Enter span length L (m): "))

Mmax = P * L / 4

print(f"Maximum bending moment = {Mmax:.3f} kN·m")
