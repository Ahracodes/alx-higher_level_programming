#!/usr/bin/python3

class LockedClass:
    def __setattr__(mod, atr, val):
        if not hasattr(mod, atr) and atr != "first_name":
            raise AttributeError(f"No '{atr}' attribute in 'LockedClass'")
        super().__setattr__(atr, val)
