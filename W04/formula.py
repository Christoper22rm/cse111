from chemistry import make_periodic_table, compute_molar_mass, sum_protons

def main():
    """Program entry point."""
    try:
        periodic_table = make_periodic_table()

        formula = input("Enter the chemical formula of the substance: ").strip()
        if not formula:
            raise ValueError("The formula cannot be empty.")

        mass = float(input("Enter the mass of the sample in grams: "))
        if mass <= 0:
            raise ValueError("The mass must be a positive number.")

        molar_mass = compute_molar_mass(formula, periodic_table)
        moles = mass / molar_mass

        total_protons = sum_protons(formula, periodic_table)

        print(f"Molar mass of {formula}: {molar_mass:.5f} g/mol")
        print(f"Number of moles in the sample: {moles:.5f} mol")
        print(f"Total number of protons in the formula: {total_protons}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

