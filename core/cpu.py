import psutil
import wmi


# =====================================
# WMI
# =====================================

computer = wmi.WMI()


# =====================================
# CPU USAGE
# =====================================

def get_cpu_usage():

    return int(
        psutil.cpu_percent()
    )


# =====================================
# CPU NAME
# =====================================

def get_cpu_name():

    try:

        return (
            computer
            .Win32_Processor()[0]
            .Name
        )

    except:

        return "CPU"


# =====================================
# CPU FREQUENCY
# =====================================

def get_cpu_frequency():

    try:

        freq = psutil.cpu_freq()

        return round(
            freq.current / 1000,
            2
        )

    except:

        return 0


# =====================================
# CPU CORES
# =====================================

def get_cpu_cores():

    return psutil.cpu_count(
        logical=False
    )


# =====================================
# CPU THREADS
# =====================================

def get_cpu_threads():

    return psutil.cpu_count(
        logical=True
    )