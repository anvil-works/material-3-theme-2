import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
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
    if s is None:
        return s
    if s.endswith("px"):
        return float(s[:-2])


def _get_unset(styles, key, current=None):
    raw = _as_style_array(styles, key)
    current_styles = _style_getter[key](current)
    current = _as_style_array(current_styles, key)
    raw = [None if v_curr else v_comp for v_curr, v_comp in zip(current, raw)]
    return {"value": [_get_value(x) for x in raw], "css": raw}


def get_unset_margin(element, current_value):
    _get_unset(window.getComputedStyle(element), "margin", current_value)


def get_unset_padding(element, current_value):
    return _get_unset(window.getComputedStyle(element), "padding", current_value)


def _get_current_spacing_key(current_value, key):
    try:
        return current_value[key]
    except Exception:
        return None


def get_unset_spacing(element_margin, element_padding, current_value):
    m_styles = window.getComputedStyle(element_margin)
    p_styles = window.getComputedStyle(element_padding)
    m = _get_unset(
        m_styles, "margin", _get_current_spacing_key(current_value, "margin")
    )
    p = _get_unset(
        p_styles, "padding", _get_current_spacing_key(current_value, "padding")
    )
    return {
        "value": {"margin": m["value"], "padding": p["value"]},
        "css": {"margin": m["css"], "padding": p["css"]},
    }


def get_unset_value(element, key, current_value):
    if current_value is not None and current_value != "":
        return {"value": None, "css": None}

    styles = window.getComputedStyle(element)
    css = styles[key]
    return {"value": _get_value(css), "css": css}


try:
    from anvil.property_utils import (
        get_unset_margin,
        get_unset_padding,
        get_unset_spacing,
        get_unset_value,
    )
except (ImportError, AttributeError):
    pass

class ComponentTag():
  def __repr__(self):
    return f"ComponentTag({self.__dict__})"