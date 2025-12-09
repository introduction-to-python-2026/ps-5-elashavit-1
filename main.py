from equation_utils import ELEMENTS, generate_equation_for_element, build_equations, my_solve
from string_utils import split_before_uppercases, split_at_digit, count_atoms_in_molecule, parse_chemical_reaction, count_atoms_in_reaction

def balance_reaction(reaction):  # "Fe2O3 + H2 -> Fe + H2O"
    # 1. פירוק התגובה
    reactants, products = parse_chemical_reaction(reaction)
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    # 2. בניית משוואות ופתרונן
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    ordered_solution = my_solve(equations, coefficients)  # ← בלי + [1] ובלי float

    return ordered_solution
