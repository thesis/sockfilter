

def apply_attr_and_dict(target, key, value):
    if target is None:
        return
    setattr(target, key, value)
    target.__dict__[key] = value
