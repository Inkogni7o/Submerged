from screeninfo import get_monitors

SIZE = WIDTH, HEIGHT = 1920, 1200


def get_monitor_size():
    global SIZE, WIDTH, HEIGHT
    monitor = get_monitors()[0]
    SIZE = WIDTH, HEIGHT = monitor.width, monitor.height
