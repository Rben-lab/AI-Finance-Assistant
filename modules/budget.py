# Generate budget allocation based on financial profile
def calculate_budget(income, profile):

    # Student investor allocation strategy
    if profile == "Student Investor":

        return {

            # Daily and essential expenses
            "Kebutuhan Pokok": income * 0.45,

            # Indonesian stock investment allocation
            "Saham Indonesia": income * 0.25,

            # US ETF investment allocation
            "ETF US": income * 0.25,

            # Self development and learning budget
            "Self Growth": income * 0.05
        }

    # Balanced financial strategy
    elif profile == "Balanced":

        return {

            # Main living expenses
            "Kebutuhan Pokok": income * 0.5,

            # General investment allocation
            "Investasi": income * 0.2,

            # Emergency fund allocation
            "Dana Darurat": income * 0.2,

            # Personal development allocation
            "Self Growth": income * 0.1
        }

    # Conservative financial strategy
    else:

        return {

            # Higher allocation for essential needs
            "Kebutuhan Pokok": income * 0.6,

            # Focus on financial safety
            "Dana Darurat": income * 0.3,

            # Smaller self development allocation
            "Self Growth": income * 0.1
        }
