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

def innerHTML_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].innerHTML

  def setter(self, value):
    if value:
      self.dom_nodes[dom_node_name].innerHTML = value

  return property(getter, setter)

def innerText_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].innerText

  def setter(self, value):
    if value:
      self.dom_nodes[dom_node_name].innerText = value

  return property(getter, setter)

def href_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].href

  def setter(self, value):
    if value:
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
    return self.dom_nodes[dom_node_name].enabled

  def setter(self, value):
    self.dom_nodes[dom_node_name].enabled = value

  return property(getter, setter)

def disabled_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].disabled

  def setter(self, value):
    self.dom_nodes[dom_node_name].disabled = value

  return property(getter, setter)

def name_property(dom_node_name):
  def getter(self):
    return self.dom_nodes[dom_node_name].name

  def setter(self, value):
    self.dom_nodes[dom_node_name].name = value

  return property(getter, setter)
