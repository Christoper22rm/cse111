import re

def make_periodic_table():
    """Returns a list with the periodic table. Each element is a tuple:
    (symbol, name, atomic mass, atomic number)."""
    return [
        ("H", "Hydrogen", 1.00794, 1),
        ("He", "Helium", 4.002602, 2),
        ("Li", "Lithium", 6.941, 3),
        ("Be", "Beryllium", 9.012182, 4),
        ("B", "Boron", 10.811, 5),
        ("C", "Carbon", 12.0107, 6),
        ("N", "Nitrogen", 14.0067, 7),
        ("O", "Oxygen", 15.9994, 8),
        ("F", "Fluorine", 18.9984032, 9),
        ("Ne", "Neon", 20.1797, 10),
        ("Na", "Sodium", 22.98976928, 11),
        ("Mg", "Magnesium", 24.305, 12),
        ("Al", "Aluminum", 26.9815386, 13),
        ("Si", "Silicon", 28.0855, 14),
        ("P", "Phosphorus", 30.973762, 15),
        ("S", "Sulfur", 32.065, 16),
        ("Cl", "Chlorine", 35.453, 17),
        ("Ar", "Argon", 39.948, 18),
        ("K", "Potassium", 39.0983, 19),
        ("Ca", "Calcium", 40.078, 20),
        ("Sc", "Scandium", 44.955912, 21),
        ("Ti", "Titanium", 47.867, 22),
        ("V", "Vanadium", 50.9415, 23),
        ("Cr", "Chromium", 51.9961, 24),
        ("Mn", "Manganese", 54.938045, 25),
        ("Fe", "Iron", 55.845, 26),
        ("Co", "Cobalt", 58.933195, 27),
        ("Ni", "Nickel", 58.6934, 28),
        ("Cu", "Copper", 63.546, 29),
        ("Zn", "Zinc", 65.38, 30),
        ("Ga", "Gallium", 69.723, 31),
        ("Ge", "Germanium", 72.64, 32),
        ("As", "Arsenic", 74.9216, 33),
        ("Se", "Selenium", 78.96, 34),
        ("Br", "Bromine", 79.904, 35),
        ("Kr", "Krypton", 83.798, 36),
        ("Rb", "Rubidium", 85.4678, 37),
        ("Sr", "Strontium", 87.62, 38),
        ("Y", "Yttrium", 88.90585, 39),
        ("Zr", "Zirconium", 91.224, 40),
        ("Nb", "Niobium", 92.90638, 41),
        ("Mo", "Molybdenum", 95.96, 42),
        ("Tc", "Technetium", 98, 43),
        ("Ru", "Ruthenium", 101.07, 44),
        ("Rh", "Rhodium", 102.9055, 45),
        ("Pd", "Palladium", 106.42, 46),
        ("Ag", "Silver", 107.8682, 47),
        ("Cd", "Cadmium", 112.411, 48),
        ("In", "Indium", 114.818, 49),
        ("Sn", "Tin", 118.71, 50),
        ("Sb", "Antimony", 121.76, 51),
        ("Te", "Tellurium", 127.6, 52),
        ("I", "Iodine", 126.90447, 53),
        ("Xe", "Xenon", 131.293, 54),
        ("Cs", "Cesium", 132.9054519, 55),
        ("Ba", "Barium", 137.327, 56),
        ("La", "Lanthanum", 138.90547, 57),
        ("Ce", "Cerium", 140.116, 58),
        ("Pr", "Praseodymium", 140.90765, 59),
        ("Nd", "Neodymium", 144.242, 60),
        ("Pm", "Promethium", 145, 61),
        ("Sm", "Samarium", 150.36, 62),
        ("Eu", "Europium", 151.964, 63),
        ("Gd", "Gadolinium", 157.25, 64),
        ("Tb", "Terbium", 158.92535, 65),
        ("Dy", "Dysprosium", 162.5, 66),
        ("Ho", "Holmium", 164.93032, 67),
        ("Er", "Erbium", 167.259, 68),
        ("Tm", "Thulium", 168.93421, 69),
        ("Yb", "Ytterbium", 173.054, 70),
        ("Lu", "Lutetium", 174.9668, 71),
        ("Hf", "Hafnium", 178.49, 72),
        ("Ta", "Tantalum", 180.94788, 73),
        ("W", "Tungsten", 183.84, 74),
        ("Re", "Rhenium", 186.207, 75),
        ("Os", "Osmium", 190.23, 76),
        ("Ir", "Iridium", 192.217, 77),
        ("Pt", "Platinum", 195.084, 78),
        ("Au", "Gold", 196.966569, 79),
        ("Hg", "Mercury", 200.59, 80),
        ("Tl", "Thallium", 204.3833, 81),
        ("Pb", "Lead", 207.2, 82),
        ("Bi", "Bismuth", 208.9804, 83),
        ("Po", "Polonium", 209, 84),
        ("At", "Astatine", 210, 85),
        ("Rn", "Radon", 222, 86),
        ("Fr", "Francium", 223, 87),
        ("Ra", "Radium", 226, 88),
        ("Ac", "Actinium", 227, 89),
        ("Th", "Thorium", 232.03806, 90),
        ("Pa", "Protactinium", 231.03588, 91),
        ("U", "Uranium", 238.02891, 92),
    ]

def parse_formula(formula):
    """Parses the chemical formula and returns a dictionary with elements and their quantities."""
    pattern = r"([A-Z][a-z]*)(\d*)"
    matches = re.findall(pattern, formula)
    composition = {}
    for element, count in matches:
        count = int(count) if count else 1
        composition[element] = composition.get(element, 0) + count
    return composition

def compute_molar_mass(formula, periodic_table):
    """Calculate the molar mass of a chemical formula."""
    composition = parse_formula(formula)
    molar_mass = 0
    for element, count in composition.items():
        for entry in periodic_table:
            if entry[0] == element:
                molar_mass += entry[2] * count
                break
        else:
            raise ValueError(f"Unknown element: {element}")
    return molar_mass

def sum_protons(formula, periodic_table):
    """Calculate the total number of protons in the chemical formula."""
    composition = parse_formula(formula)
    total_protons = 0
    for element, count in composition.items():
        for entry in periodic_table:
            if entry[0] == element:
                total_protons += entry[3] * count
                break
        else:
            raise ValueError(f"Unknown element: {element}")
    return total_protons

def main():
    periodic_table = make_periodic_table()

    formula = input("Enter the chemical formula of the substance: ")
    mass = float(input("Enter the mass of the sample in grams: "))

    molar_mass = compute_molar_mass(formula, periodic_table)

    moles = mass / molar_mass

    print(f"Molar mass of {formula}: {molar_mass:.5f} g/mol")
    print(f"Number of moles in the sample: {moles:.5f} mol")

if __name__ == "__main__":
    main()
