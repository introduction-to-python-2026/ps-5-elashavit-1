from sympy import symbols, Eq, solve, Rational
from math import lcm

def balance_reaction(reaction):
    reactants_atoms, products_atoms = parse_chemical_reaction(reaction)
    equations, coefficients = build_equations(reactants_atoms, products_atoms)
    coeff_values = my_solve(equations, coefficients)
    coeff_values.append(Rational(1))
    denominators = [v.q if isinstance(v, Rational) else 1 for v in coeff_values]
    lcm_den = 1
    for d in denominators:
        lcm_den = lcm(lcm_den, d)
    normalized = [v * lcm_den for v in coeff_values]
    normalized = [Rational(v).limit_denominator() for v in normalized]
    return normalized






