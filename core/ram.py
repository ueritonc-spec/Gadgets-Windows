import psutil


def get_ram_usage():

    memory = psutil.virtual_memory()

    return memory.percent


def get_ram_total():

    memory = psutil.virtual_memory()

    return round(
        memory.total / (1024 ** 3),
        1
    )