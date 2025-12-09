from equation_utils import ELEMENTS, generate_equation_for_element, build_equations, my_solve
from string_utils import split_before_uppercases, split_at_digit, count_atoms_in_molecule, parse_chemical_reaction, count_atoms_in_reaction
from sympy import Eq, symbols, solve


def balance_reaction(reaction):  # "Fe2O3 + H2 -> Fe + H2O"

    # 1. parse reaction
    reactants, products = parse_chemical_reaction(reaction)  # ["Fe2O3", "H2"], ["Fe", "H2O"]
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    # 2. build equations and solve
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    solution_dict = my_solve(equations, coefficients)

    # 3. return a list in the correct order
    ordered_solution = [solution_dict[c] for c in coefficients]

    return ordered_solution


