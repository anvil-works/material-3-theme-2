from ._anvil_designer import HeadingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
import anvil.designer
from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property

#TODO: figure out what to do with line height
#TODO: add margin and padding

class Heading(HeadingTemplate):
  def __init__(self, **properties):
    self._props = properties
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer and not self.text:
      self.text = anvil.designer.get_design_name(self)

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-heading'])
      }
    }]

  visible = HtmlTemplate.visible
  italic = italic_property('anvil-m3-heading-container')
  border = style_property('anvil-m3-heading-container', 'border')
  font = style_property('anvil-m3-heading-container', 'fontFamily')
  text_color = color_property('anvil-m3-heading-container', 'color')
  icon_color = color_property('anvil-m3-heading-icon', 'color')
  background_color = color_property('anvil-m3-heading-container', 'backgroundColor')
  align = style_property('anvil-m3-heading-container', 'justifyContent')

  @property
  def font_size(self):
    return self._font_size

  @font_size.setter
  def font_size(self, value):
    self._font_size = value
    if value: value = f'{value}px'
    self.dom_nodes['anvil-m3-heading-display'].style.fontSize = f'{value}px'
    self.dom_nodes['anvil-m3-heading-headline'].style.fontSize = f'{value}px'
    self.dom_nodes['anvil-m3-heading-title'].style.fontSize = f'{value}px'
    self.dom_nodes['anvil-m3-heading-container'].style.fontSize = f'{value}px'

  @property
  def icon_size(self):
    return self._icon_size

  @icon_size.setter
  def icon_size(self, value):
    self._icon_size = value
    if value: value = f'{value}px'
    self.dom_nodes['anvil-m3-heading-icon'].style.fontSize = value

  @property
  def underline(self):
    return self._underline

  @underline.setter
  def underline(self, value):
    self._underline = value
    if value:
      self.dom_nodes['anvil-m3-heading-display'].style.textDecoration = 'underline'
      self.dom_nodes['anvil-m3-heading-headline'].style.textDecoration = 'underline'
      self.dom_nodes['anvil-m3-heading-title'].style.textDecoration = 'underline'
    else:
      self.dom_nodes['anvil-m3-heading-display'].style.textDecoration = 'none'
      self.dom_nodes['anvil-m3-heading-headline'].style.textDecoration = 'none'
      self.dom_nodes['anvil-m3-heading-title'].style.textDecoration = 'none'

  @property
  def bold(self):
    return self._bold

  @bold.setter
  def bold(self, value):
    self._bold = value
    if value:
      self.dom_nodes['anvil-m3-heading-display'].style.fontWeight = 'bold'
      self.dom_nodes['anvil-m3-heading-headline'].style.fontWeight = 'bold'
      self.dom_nodes['anvil-m3-heading-title'].style.fontWeight = 'bold'
    else:
      self.dom_nodes['anvil-m3-heading-display'].style.fontWeight = 'normal'
      self.dom_nodes['anvil-m3-heading-headline'].style.fontWeight = 'normal'
      self.dom_nodes['anvil-m3-heading-title'].style.fontWeight = 'normal'

  @property
  def text(self):
    return self._text

  @text.setter
  def text(self, value):
    self._text = value
    if value:
      self.dom_nodes['anvil-m3-heading-display'].innerText = value
      self.dom_nodes['anvil-m3-heading-headline'].innerText = value
      self.dom_nodes['anvil-m3-heading-title'].innerText = value

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    self._material_icon = value
    if value:
      self.dom_nodes['anvil-m3-heading-icon'].innerText = value

  @property
  def style(self):
    return self._style

  @style.setter
  def style(self, value):
    self._style = value
    display = self.dom_nodes['anvil-m3-heading-display']
    headline = self.dom_nodes['anvil-m3-heading-headline']
    title = self.dom_nodes['anvil-m3-heading-title']
    self.dom_nodes['anvil-m3-heading-container'].classList.remove('anvil-m3-heading-display', 'anvil-m3-heading-headline', 'anvil-m3-heading-title')
    self.dom_nodes['anvil-m3-heading-container'].classList.add(f'anvil-m3-heading-{value}')
    if value == 'display':
      display.style.display = 'block'
      headline.style.display = 'none'
      title.style.display = 'none'
    elif value == 'headline':
      display.style.display = 'none'
      headline.style.display = 'block'
      title.style.display = 'none'
    elif value == 'title':
      display.style.display = 'none'
      headline.style.display = 'none'
      title.style.display = 'block'

  @property
  def scale(self):
    return self._style

  @scale.setter
  def scale(self, value):
    self._style = value
    self.dom_nodes['anvil-m3-heading-display'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-headline'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-title'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-container'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-display'].classList.add(f'anvil-m3-heading-{value}')
    self.dom_nodes['anvil-m3-heading-headline'].classList.add(f'anvil-m3-heading-{value}')
    self.dom_nodes['anvil-m3-heading-title'].classList.add(f'anvil-m3-heading-{value}')
    self.dom_nodes['anvil-m3-heading-container'].classList.add(f'anvil-m3-heading-{value}')

