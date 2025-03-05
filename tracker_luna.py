import ephem
from datetime import datetime

def calcola_fase_luna(data=None):
    """
    Calcola la fase della luna per una data specifica.
    
    :param data: Data per la quale calcolare la fase della luna.
                 Se None, utilizza la data odierna.
    :return: Fase della luna.
    """
    if data is None:
        data = datetime.now()
    
    # Crea un oggetto Moon
    luna = ephem.Moon()
    
    # Imposta la data
    luna.compute(data)
    
    # Calcola la fase della luna
    fase = luna.phase
    
    return fase

def calcola_posizione_luna(data=None):
    """
    Calcola la posizione della luna per una data specifica.
    
    :param data: Data per la quale calcolare la posizione della luna.
                 Se None, utilizza la data odierna.
    :return: Posizione della luna.
    """
    if data is None:
        data = datetime.now()
    
    # Crea un oggetto Moon
    luna = ephem.Moon()
    
    # Imposta la data
    luna.compute(data)
    
    # Calcola la posizione della luna
    ascensione_retta = luna.ra
    declinazione = luna.dec
    
    return ascensione_retta, declinazione

def main():
    print("Tracker della Luna")
    print("------------------")
    
    # Calcola e visualizza la fase della luna
    fase_luna = calcola_fase_luna()
    print(f"Fase della luna: {fase_luna:.2f}%")
    
    # Calcola e visualizza la posizione della luna
    ascensione_retta, declinazione = calcola_posizione_luna()
    print(f"Ascensione retta: {ascensione_retta}")
    print(f"Declinazione: {declinazione}")

if __name__ == "__main__":
    main()
