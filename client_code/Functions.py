from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

def m3_alert(title=None, content=None, buttons="OK", icon=None, dividers=False, centered=False):
  pass

def theme_color_to_css(color:str):
  if color.startswith('theme:'):
    color = color.strip('theme:')
    return app.theme_colors[color]
  else:
    return color

#REUSABLE PROPERTIES
def color_property(dom_node_name, style_prop):
  def getter(self):
    return self.dom_nodes[dom_node_name].style[style_prop]

  def setter(self, value):
    if value: value = theme_color_to_css(value)
    self.dom_nodes[dom_node_name].style[style_prop] = value

  return property(getter, setter)

def style_property(dom_node_name, style_prop):
  def getter(self):
    return self.dom_nodes[dom_node_name].style[style_prop]

  def setter(self, value):
    self.dom_nodes[dom_node_name].style[style_prop] = value

  return property(getter, setter)

def innerHTML_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].innerHTML

  def setter(self, value):
    self.dom_nodes[dom_node_name].innerHTML = value

  return property(getter, setter)

def innerText_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].innerText

  def setter(self, value):
    self.dom_nodes[dom_node_name].innerText = value

  return property(getter, setter)

def href_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].href

  def setter(self, value):
    self.dom_nodes[dom_node_name].href = value

  return property(getter, setter)

def checked_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].checked

  def setter(self, value):
    self.dom_nodes[dom_node_name].checked = value

  return property(getter, setter)

def enabled_property(dom_node_name):
  def getter(self):
    return self._enabled

  def setter(self, value):
    self._enabled = value
    if value:
      self.dom_nodes[dom_node_name].removeAttribute("disabled")
    else:
      self.dom_nodes[dom_node_name].setAttribute("disabled", " ")
      
  return property(getter, setter)

def name_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].name

  def setter(self, value):
    self.dom_nodes[dom_node_name].name = value

  return property(getter, setter)

def value_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].value

  def setter(self, value):
    self.dom_nodes[dom_node_name].value = value

  return property(getter, setter)

def underline_property(dom_node_name):
  def getter(self):
    return self._underline

  def setter(self, value):
    self._underline = value
    if value:
      self.dom_nodes[dom_node_name].style.textDecoration = 'underline'
    else:
      self.dom_nodes[dom_node_name].style.textDecoration = 'none'

  return property(getter, setter)

def italic_property(dom_node_name):
  def getter(self):
    return self._italic

  def setter(self, value):
    self._italic = value
    if value:
      self.dom_nodes[dom_node_name].style.fontStyle = 'italic'
    else:
      self.dom_nodes[dom_node_name].style.fontStyle = 'normal'

  return property(getter, setter)

def bold_property(dom_node_name):
  def getter(self):
    return self._props['bold']

  def setter(self, value):
    self._props['bold'] = value
    if value:
      self.dom_nodes[dom_node_name].style.fontWeight = 'bold'
    else:
      self.dom_nodes[dom_node_name].style.fontWeight = 'normal'

  return property(getter, setter)

def font_size_property(dom_node_name):
  def getter(self):
    return self._font_size

  def setter(self, value):
    self._font_size = value
    if value: value = f'{value}px'
    self.dom_nodes[dom_node_name].style.fontSize = value

  return property(getter, setter)
  
  


