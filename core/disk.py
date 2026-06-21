import psutil


def get_main_disk():

    partitions = psutil.disk_partitions()

    for partition in partitions:

        if "fixed" in partition.opts.lower():

            return partition.mountpoint

    return "C:\\"


def get_disk_usage():

    try:

        path = get_main_disk()

        disk = psutil.disk_usage(path)

        return round(
            disk.percent,
            1
        )

    except Exception as e:

        print("Erro DISK:", e)

        return 0


def get_disk_total():

    try:

        path = get_main_disk()

        disk = psutil.disk_usage(path)

        return round(
            disk.total / (1024 ** 3),
            1
        )

    except Exception as e:

        print("Erro DISK:", e)

        return 0


def get_disk_free():

    try:

        path = get_main_disk()

        disk = psutil.disk_usage(path)

        return round(
            disk.free / (1024 ** 3),
            1
        )

    except Exception as e:

        print("Erro DISK:", e)

        return 0