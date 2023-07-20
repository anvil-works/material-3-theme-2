from anvil import *

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
    if value:
      self.dom_nodes[dom_node_name].style[style_prop] = theme_color_to_css(value)

  return property(getter, setter)

def style_property(dom_node_name, style_prop):
  def getter(self):
    return self.dom_nodes[dom_node_name].style[style_prop]

  def setter(self, value):
    if value:
      self.dom_nodes[dom_node_name].style[style_prop] = value

  return property(getter, setter)

