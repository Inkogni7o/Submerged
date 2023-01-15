from screeninfo import get_monitors


def get_monitor_size() -> tuple:
    global SIZE, WIDTH, HEIGHT
    monitor = get_monitors()[0]
    print('вызвали функцию')
    SIZE = WIDTH, HEIGHT = monitor.width, monitor.height
    return SIZE


SIZE = WIDTH, HEIGHT = get_monitor_size()