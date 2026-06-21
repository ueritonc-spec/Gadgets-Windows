import psutil
import time


last_sent = 0
last_recv = 0
last_time = time.time()


def get_network_usage():

    global last_sent
    global last_recv
    global last_time

    current = psutil.net_io_counters()

    now = time.time()

    sent = current.bytes_sent
    recv = current.bytes_recv

    # =========================
    # DIFERENÇA
    # =========================

    upload = sent - last_sent
    download = recv - last_recv

    elapsed = now - last_time

    if elapsed <= 0:
        elapsed = 1

    # =========================
    # MB/s
    # =========================

    upload_speed = (
        upload / elapsed
    ) / 1024 / 1024

    download_speed = (
        download / elapsed
    ) / 1024 / 1024

    # =========================
    # SALVA ESTADO
    # =========================

    last_sent = sent
    last_recv = recv
    last_time = now

    # =========================
    # USO VISUAL
    # =========================

    total_speed = (
        upload_speed +
        download_speed
    )

    # amplificação visual
    visual_usage = total_speed * 120

    # mantém vivo
    if visual_usage < 2:
        visual_usage = 2

    # limite
    if visual_usage > 100:
        visual_usage = 100

    return {

        "upload": round(
            upload_speed,
            2
        ),

        "download": round(
            download_speed,
            2
        ),

        "usage": round(
            visual_usage,
            1
        )
    }