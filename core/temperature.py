import requests


URL = "http://localhost:8085/data.json"


# Nomes de sensores de temperatura conhecidos
# (AMD Ryzen, Intel, outros)
CPU_TEMP_NAMES = [
    "Core (Tctl/Tdie)",   # AMD Ryzen
    "CPU Package",         # Intel
    "Core Average",        # Intel (alguns modelos)
    "CPU",                 # Genérico
    "Tdie",               # AMD alternativo
    "Tctl",               # AMD alternativo
]


def find_temperature(children, depth=0):

    # Protecção contra recursão infinita
    if depth > 10:
        return None

    for item in children:

        item_type = item.get("Type", "")
        item_text = item.get("Text", "")

        # Verifica se é um sensor de temperatura da CPU
        if item_type == "Temperature":

            # Tenta primeiro os nomes conhecidos
            for name in CPU_TEMP_NAMES:
                if name.lower() in item_text.lower():
                    value = item.get("Value", "0")
                    try:
                        return float(
                            value.replace("°C", "")
                            .replace(",", ".")
                            .strip()
                        )
                    except ValueError:
                        pass

        # Recursão nos filhos
        if "Children" in item:
            result = find_temperature(
                item["Children"],
                depth + 1
            )
            if result is not None:
                return result

    return None


def find_any_cpu_temperature(children, depth=0):
    """
    Fallback: procura qualquer sensor de temperatura
    dentro de um nó chamado 'CPU'.
    """
    if depth > 10:
        return None

    for item in children:

        item_text = item.get("Text", "").lower()
        item_type = item.get("Type", "")

        # Entra no ramo da CPU
        if "cpu" in item_text and "Children" in item:
            # Procura o primeiro sensor de temperatura dentro deste ramo
            for child in item["Children"]:
                if child.get("Type") == "Temperature":
                    value = child.get("Value", "0")
                    try:
                        return float(
                            value.replace("°C", "")
                            .replace(",", ".")
                            .strip()
                        )
                    except ValueError:
                        pass
                if "Children" in child:
                    result = find_any_cpu_temperature(
                        child["Children"],
                        depth + 1
                    )
                    if result is not None:
                        return result

        if "Children" in item:
            result = find_any_cpu_temperature(
                item["Children"],
                depth + 1
            )
            if result is not None:
                return result

    return None


def get_cpu_temperature():

    try:

        response = requests.get(
            URL,
            timeout=2
        )

        data = response.json()

        children = data.get("Children", [])

        # Tentativa 1: nomes conhecidos
        temp = find_temperature(children)

        # Tentativa 2: fallback - qualquer temp. dentro do ramo CPU
        if temp is None:
            temp = find_any_cpu_temperature(children)

        if temp is not None:
            return temp

    except Exception:
        pass

    return 0