

def split_before_uppercases(formula):
    """Splits a formula string at each uppercase letter."""
    if not formula:
        return []

    splitted_formula = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            splitted_formula.append(formula[start:i])
            start = i

    splitted_formula.append(formula[start:])
    return splitted_formula


def split_at_digit(formula):
    """Splits a string into the element and its count. Example: 'H2' -> ('H', 2)"""
    if not formula:
        return "", 1

    for i, ch in enumerate(formula):
        if ch.isdigit():
            j = i
            while j < len(formula) and formula[j].isdigit():
                j += 1
            prefix = formula[:i]
            number_part = int(formula[i:j])
            return prefix, number_part

    return formula, 1  # No digits means count is 1


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    my_dict = {}
    splitted_formula = split_before_uppercases(molecular_formula)

    for formula in splitted_formula:
        prefix, number_part = split_at_digit(formula)

        if prefix in my_dict:
            my_dict[prefix] += number_part
        else:
            my_dict[prefix] = number_part

    return my_dict


   def parse_chemical_reaction(reaction_equation): # Step 1: Initialize an empty dictionary to store atom counts

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary



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
