def keyval(lst: list):
    key = None
    for i, val in enumerate(lst):
        if i % 2:
            yield key, val
        else:
            key = val
