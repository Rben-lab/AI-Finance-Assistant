def calculate_budget(income, profile):

    if profile == "Student Investor":

        return {
            "Kebutuhan Pokok": income * 0.45,
            "Saham Indonesia": income * 0.25,
            "ETF US": income * 0.25,
            "Self Growth": income * 0.05
        }

    elif profile == "Balanced":

        return {
            "Kebutuhan Pokok": income * 0.5,
            "Investasi": income * 0.2,
            "Dana Darurat": income * 0.2,
            "Self Growth": income * 0.1
        }

    else:

        return {
            "Kebutuhan Pokok": income * 0.6,
            "Dana Darurat": income * 0.3,
            "Self Growth": income * 0.1
        }