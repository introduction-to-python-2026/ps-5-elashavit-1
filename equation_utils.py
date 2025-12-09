from equation_utils import ELEMENTS, generate_equation_for_element, build_equations
from string_utils import parse_chemical_reaction, count_atoms_in_reaction
from sympy import Eq, symbols, solve, Rational

def my_solve(equations, coefficients):
    solution_list = solve(equations, coefficients)
    solution = solution_list[0]  # dict ראשון
    # החזרה כרשימה של שברים מדויקים
    return [Rational(solution[c].p, solution[c].q) for c in coefficients]

def balance_reaction(reaction):
    # 1. פירוק התגובה
    reactants, products = parse_chemical_reaction(reaction)
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    # 2. בניית משוואות ופתרונן
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    ordered_solution = my_solve(equations, coefficients)

    # 3. החזרת הרשימה הסופית של השברים
    return ordered_solution
