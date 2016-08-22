import asyncio

from blinker.base import Signal


try:
    schedule = asyncio.ensure_future
except AttributeError:
    schedule = asyncio.async


@asyncio.coroutine
def _wrap_plain_value(value):
    """Pass through a coroutine *value* or wrap a plain value."""
    if asyncio.iscoroutine(value):
        value = yield from value
    return value


def send_async(scheduler=schedule):
    def adapter(receiver, sender, kwargs):
        result = receiver(sender, **kwargs)
        return scheduler(_wrap_plain_value(result))
    return adapter
