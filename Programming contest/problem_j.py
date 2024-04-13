# 2HBr + H2O+SO2=H2+H2SO3+He
from collections import Counter


def find_multiplier(substance):
    multiplier = []
    element = []
    valid = True
    for letter in substance:
        if valid:
            if letter.isdigit():
                multiplier.append(letter)
            else:
                if letter != ' ':
                    if multiplier:
                        multiplier = int(''.join(multiplier))
                    else:
                        multiplier = 1
                    valid = False
        if not letter.islower() and letter.isalpha():
            element.append(letter)
            if substance.index(letter) <= len(substance) - 2:
                if substance[substance.index(letter) + 1].isdigit():
                    for times in range(int(substance[substance.index(letter) + 1]) - 1):
                        element.append(letter)
        elif letter.islower():
            element[-1] = ''.join([element[-1], letter])
    return [element, multiplier]


count = 0
while True:
    # Splitting both sides into reactants and products
    equation = input()
    if equation == "#":
        break
    else:
        equation = equation.split('=')
    count += 1
    # Splitting each substance
    reactants = equation[0].split('+')
    products = equation[1].split('+')
    # finding multipliers

    reactant_multipliers = []
    for reactant in reactants:
        reactant_multipliers.append(find_multiplier(reactant))
    product_multipliers = []
    for product in products:
        product_multipliers.append(find_multiplier(product))

    reactants_list = []
    for reactant_compound in reactant_multipliers:
        for times in range(reactant_compound[1]):
            reactants_list.append(reactant_compound[0])

    products_list = []
    for product_compound in product_multipliers:
        for times in range(product_compound[1]):
            products_list.append(product_compound[0])


    def get_atoms(compound_list):
        atoms = []
        for compound in compound_list:
            for atom in compound:
                atoms.append(atom)
        return atoms


    all_reactants = get_atoms(reactants_list)
    all_products = get_atoms(products_list)
    balance = True
    destroyed = []
    for reactant in all_reactants:
        if reactant in all_products:
            all_products.remove(reactant)
        else:
            balance = False
            destroyed.append(reactant)
    if all_products:
        balance = False
    if balance:
        print(f"Equation {count} is balanced.")
    else:
        print(f"Equation {count} is unbalanced.")
        already_destroyed = dict(Counter(sorted(destroyed)))
        for key in already_destroyed.keys():
            if already_destroyed[key] == 1:
                extra = ''
            elif already_destroyed[key] > 1:
                extra = 's'
            print(f'You have destroyed {already_destroyed[key]} atom{extra} of {key}.')
        created = dict(Counter(sorted(all_products)))
        for key in created.keys():
            if created[key] == 1:
                extra = ''
            elif created[key] > 1:
                extra = 's'
            print(f'You have created {created[key]} atom{extra} of {key}.')
        print('')




