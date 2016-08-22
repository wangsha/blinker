import blinker


def quash_exceptions(fn, sender, kwargs):
    """Always call all receivers, collecting values or exceptions."""
    try:
        return fn(sender, **kwargs), None
    except Exception as exc:
        return None, exc


def _adapt_xyz(fn, sender, kwargs):
    return fn(sender, kwargs['x'], kwargs['y'], kwargs['z'])

class PositionalSignal(blinker.Signal):
    """Positional send and receive (x, y, z)"""
    receiver_adapter = staticmethod(_adapt_xyz)

    def send(self, sender, x, y, z):
        return blinker.Signal.send(self, sender, x=x, y=y, z=z)
