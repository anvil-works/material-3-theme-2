from ._anvil_designer import HeadingTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
import anvil.designer
from ...Functions import underline_property, role_property, tooltip_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, font_family_property, border_property
from anvil.property_utils import set_element_spacing
from ...utils.properties import get_unset_value, get_unset_spacing


class Heading(HeadingTemplate):
  def __init__(self, **properties):
    self.tag = ComponentTag()
    self._props = properties
    self._tooltip_node = None
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
        "execute": self._start_inline_editing
      }
    }]

  def _anvil_get_unset_property_values_(self):
    full_el = self.dom_nodes["anvil-m3-heading-container"]
    sp = get_unset_spacing(full_el, full_el, self.spacing)
    if self.style == "display":
      h = self.dom_nodes['anvil-m3-heading-display']
    elif self.style == "headline":
      h = self.dom_nodes['anvil-m3-heading-headline']
    elif self.style == "title":
      h = self.dom_nodes['anvil-m3-heading-title']
    fs = get_unset_value(h, "fontSize", self.font_size)
    ifs = get_unset_value(self.dom_nodes['anvil-m3-heading-icon'], "fontSize", self.icon_size)
    return {"spacing": sp, "font_size": fs, "icon_size": ifs}

  def _start_inline_editing(self):
    el_name = f'anvil-m3-heading-{self.style}'
    anvil.designer.start_inline_editing(self, "text", self.dom_nodes[el_name])

  #!componentEvent(material_3.Heading)!1: {name: "show", description: "When the Heading is shown on the screen."}
  #!componentEvent(material_3.Heading)!1: {name: "hide", description: "When the Heading is removed from the screen."}

  #!componentProp(material_3.Heading)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.Heading)!1: {name:"italic",type:"boolean",description:"If True, this component’s text will be italic."}
  #!componentProp(material_3.Heading)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.Heading)!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  #!componentProp(material_3.Heading)!1: {name:"text_color",type:"color",description:"The color of the text on the component."} 
  #!componentProp(material_3.Heading)!1: {name:"icon_color",type:"color",description:"The color of the icon displayed on this component."}
  #!componentProp(material_3.Heading)!1: {name:"background_color",type:"color",description:"The color of the background of this component."}
  #!componentProp(material_3.Heading)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.Heading)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"}
  #!componentProp(material_3.Heading)!1: {name:"align",type:"enum",options:['left', 'right', 'center', 'justify'], description:"The position of this component in the available space."} 
  #!componentProp(material_3.Heading)!1: {name:"font_size",type:"number",description:"The font size of text displayed on this component."}
  #!componentProp(material_3.Heading)!1: {name:"icon_size",type:"number",description:"The size (pixels) of the icon displayed on this component."}
  #!componentProp(material_3.Heading)!1: {name:"underline",type:"boolean",description:"If True, this component’s text will be underlined."}
  #!componentProp(material_3.Heading)!1: {name:"bold",type:"boolean",description:"If True, this component’s text will be bold."}
  #!componentProp(material_3.Heading)!1: {name:"text",type:"string",description:"The text displayed on this component"}
  #!componentProp(material_3.Heading)!1: {name:"icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.Heading)!1: {name:"style",type:"enum",options:['display', 'headline', 'title'],description:"Role of the heading component: display, headline or title."}  
  #!componentProp(material_3.Heading)!1: {name:"scale",type:"enum",options:['small', 'medium', 'large'],description:"The size of the heading component."}
  #!componentProp(material_3.Heading)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(material_3.Heading)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(material_3.Heading)!1: {name:"line_height",type:"string",description:"The line height of this component."}

  visible = HtmlTemplate.visible
  italic = italic_property('anvil-m3-heading-container')
  border = border_property('anvil-m3-heading-container')
  font_family = font_family_property('anvil-m3-heading-container')
  text_color = color_property('anvil-m3-heading-container', 'color', 'text_color')
  icon_color = color_property('anvil-m3-heading-icon', 'color', 'icon_color')
  background_color = color_property('anvil-m3-heading-container', 'backgroundColor', 'background_color')
  tooltip = tooltip_property('anvil-m3-heading-container')
  role = role_property('anvil-m3-heading-container')

  @property
  def align(self):
    return self._props.get('align')

  @align.setter
  def align(self, value):
    self._props['align'] = value
    if value == 'justify':
      self.dom_nodes['anvil-m3-heading-container'].style.justifyContent = 'left'
    else:
      self.dom_nodes['anvil-m3-heading-container'].style.justifyContent = value
    self.dom_nodes['anvil-m3-heading-container'].style.textAlign = value

  @property
  def font_size(self):
    return self._font_size

  @font_size.setter
  def font_size(self, value):
    self._font_size = value
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
  def icon(self):
    return self._icon

  @icon.setter
  def icon(self, value):
    self._icon = value
    if value:
      self.dom_nodes['anvil-m3-heading-icon'].style.marginRight = "8px"
    else:
      self.dom_nodes['anvil-m3-heading-icon'].style.marginRight = ""
    self.dom_nodes['anvil-m3-heading-icon'].innerText = value[3:]

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
    return self._scale

  @scale.setter
  def scale(self, value):
    self._scale = value
    self.dom_nodes['anvil-m3-heading-display'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-headline'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-title'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-container'].classList.remove('anvil-m3-heading-large', 'anvil-m3-heading-medium', 'anvil-m3-heading-small')
    self.dom_nodes['anvil-m3-heading-display'].classList.add(f'anvil-m3-heading-{value}')
    self.dom_nodes['anvil-m3-heading-headline'].classList.add(f'anvil-m3-heading-{value}')
    self.dom_nodes['anvil-m3-heading-title'].classList.add(f'anvil-m3-heading-{value}')
    self.dom_nodes['anvil-m3-heading-container'].classList.add(f'anvil-m3-heading-{value}')

  @property
  def spacing(self):
    return self._props.get('spacing')

  @spacing.setter
  def spacing(self, value):
    set_element_spacing(self.dom_nodes['anvil-m3-heading-container'], value)
    # set_element_spacing(self.dom_nodes['anvil-m3-heading-headline'], value)
    # set_element_spacing(self.dom_nodes['anvil-m3-heading-title'], value)
    self._props['spacing'] = value

  @property
  def line_height(self):
    return self._props.get('line_height')

  @line_height.setter
  def line_height(self, value):
    self._props['line_height'] = value
    self.dom_nodes['anvil-m3-heading-display'].style.lineHeight = value
    self.dom_nodes['anvil-m3-heading-headline'].style.lineHeight = value
    self.dom_nodes['anvil-m3-heading-title'].style.lineHeight = value
    self.dom_nodes['anvil-m3-heading-container'].style.lineHeight = {value}

#!defClass(material_3, Heading, anvil.Component)!:
