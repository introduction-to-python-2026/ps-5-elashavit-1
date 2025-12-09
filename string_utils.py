def split_before_uppercases(formula):
    t = []
    splited_formula = []

    for char in formula:
        if char.isupper():
            if t:  # only append if t is not empty
                splited_formula.append(''.join(t))
            t = [char]
        else:
            t.append(char)

    if t:  # append the last chunk after the loop
        splited_formula.append(''.join(t))

    return splited_formula

def split_at_digit(formula):
    digits = []
    letters = []
    for char in formula:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
    if digits == []:
        digits.append("1")
    return ''.join(letters), int(''.join(digits))

def count_atoms_in_molecule(molecular_formula):
  count = {}
  splited_formula = split_before_uppercases(molecular_formula)
  for atom in splited_formula:
    element,amount = split_at_digit(atom)
    if element in count:
      count[element] += amount
    else:
      count[element] = amount

  return count


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
