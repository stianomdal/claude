# main.py
def hilsen(navn="verden"):
    """Returnerer en hilsen til angitt navn eller 'verden' som standard."""
    return f"Hallo, {navn}!"

def adder(a, b):
    """Legger sammen to tall og returnerer resultatet."""
    return a + b

# Test funksjonene
if __name__ == "__main__":
    print(hilsen())
    print(hilsen("GitHub"))
    
    tall1 = 5
    tall2 = 7
    sum_resultat = adder(tall1, tall2)
    print(f"{tall1} + {tall2} = {sum_resultat}")