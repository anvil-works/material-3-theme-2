from anvil.js import window
from anvil.property_utils import (
  get_margin_styles,
  get_padding_styles,
  get_spacing_styles,
)

_directions = ("Top", "Right", "Bottom", "Left")

_style_getter = {"margin": get_margin_styles, "padding": get_padding_styles}

def _as_style_array(styles, key):
  return [styles[f"{key}{dir}"] for dir in _directions]


def _get_value(s):
  if s.endswith("px"):
    return float(s[:-2])


def _get_unset(styles, key, current=None):
  raw = _as_style_array(styles, key)
  current_styles = _style_getter[key](current)
  current = _as_style_array(current_styles, key)
  raw = [v_comp if not v_curr else v_curr for v_curr, v_comp in zip(current, raw)]
  return {"value": [_get_value(x) for x in raw], "css": raw}


def get_unset_margin(element, current_value):
  _get_unset(window.getComputedStyle(element), "margin", current_value)


def get_unset_padding(element, current_value):
  return _get_unset(window.getComputedStyle(element), "padding", current_value)


def get_unset_spacing(element, current_value):
  styles = window.getComputedStyle(element)
  m = _get_unset(styles, "margin")
  p = _get_unset(styles, "padding")
  return {
    "value": {"margin": m["value"], "padding": p["value"]},
    "css": {"margin": m["css"], "padding": p["css"]},
  }
