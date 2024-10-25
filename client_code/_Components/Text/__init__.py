from ._anvil_designer import TextTemplate
from anvil import *
import anvil.server
from anvil import HtmlTemplate
import anvil.designer
from anvil.js.window import document
from ...Functions import tooltip_property, role_property, underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property, font_family_property, border_property, spacing_property
from ...utils import fui, noop
from ...utils.properties import get_unset_value, get_unset_spacing
import time
#TODO: figure out what to do with line height
#TODO: figure out default icon sizes 

class Text(TextTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.tag = ComponentTag()
    self._props = properties
    self._tooltip_node = None
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
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-text'])
      }
    }]

  def _anvil_get_unset_property_values_(self):
    el = self.dom_nodes["anvil-m3-text-container"]
    sp = get_unset_spacing(el, el, self.spacing)
    tfs = get_unset_value(self.dom_nodes['anvil-m3-text'], "fontSize", self.font_size)
    ifs = get_unset_value(self.dom_nodes['anvil-m3-text-icon'], "fontSize", self.icon_size)
    return {"font_size": tfs, "icon_size": ifs, "spacing": sp}

  #!componentEvent(material_3.Text)!1: {name: "show", description: "When the Text is shown on the screen."}
  #!componentEvent(material_3.Text)!1: {name: "hide", description: "When the Text is removed from the screen."}

  #!componentProp(material_3.Text)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."}
  #!componentProp(material_3.Text)!1: {name:"underline",type:"boolean",description:"If True, this component’s text will be underlined."}
  #!componentProp(material_3.Text)!1: {name:"italic",type:"boolean",description:"If True, this component’s text will be italic."}
  #!componentProp(material_3.Text)!1: {name:"bold",type:"boolean",description:"If True, this component’s text will be bold."}
  #!componentProp(material_3.Text)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.Text)!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  #!componentProp(material_3.Text)!1: {name:"text_color",type:"color",description:"The color of the text on the component."} 
  #!componentProp(material_3.Text)!1: {name:"icon_color",type:"color",description:"The color of the icon displayed on this component."}
  #!componentProp(material_3.Text)!1: {name:"background_color",type:"color",description:"The color of the background of this component."}
  #!componentProp(material_3.Text)!1: {name:"text",type:"string",description:"The text displayed on this component"}
  #!componentProp(material_3.Text)!1: {name:"icon_size",type:"number",description:"The size (pixels) of the icon displayed on this component."}
  #!componentProp(material_3.Text)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(material_3.Text)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.Text)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"}
  #!componentProp(material_3.Text)!1: {name:"align",type:"enum",options:['left', 'right', 'center', 'justify'], description:"The position of this component in the available space."} 
  #!componentProp(material_3.Text)!1: {name:"font_size",type:"number",description:"The font size of text displayed on this component."}
  #!componentProp(material_3.Text)!1: {name:"icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.Text)!1: {name:"line_height",type:"string",description:"The line height of this component."}
  #!componentProp(material_3.Text)!1: {name:"material_icon",type:"enum",description:"The icon to display on this component."} 
  #!componentProp(material_3.Text)!1: {name:"style",type:"enum",options:['display', 'headline', 'title'],description:"Role of the text component: display, headline or title."}  
  #!componentProp(material_3.Text)!1: {name:"scale",type:"enum",options:['small', 'medium', 'large'],description:"The size of the text component."}
  #!componentProp(material_3.Text)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}

  visible = HtmlTemplate.visible
  underline = underline_property('anvil-m3-text')
  italic = italic_property('anvil-m3-text')
  bold = bold_property('anvil-m3-text')
  border = border_property('anvil-m3-text-container')
  font_family = font_family_property('anvil-m3-text', 'font_family')
  text_color = color_property('anvil-m3-text-container', 'color', 'text_color')
  icon_color = color_property('anvil-m3-text-icon', 'color', 'icon_color')
  background_color = color_property('anvil-m3-text-container', 'backgroundColor', 'background_color')
  text = innerText_property('anvil-m3-text')
  icon_size = font_size_property('anvil-m3-text-icon', 'icon_size')
  spacing = spacing_property('anvil-m3-text-container')
  tooltip = tooltip_property('anvil-m3-text-container')
  role = role_property('anvil-m3-text-container')

  @property
  def align(self):
    return self._props.get('align')

  @align.setter
  def align(self, value):
    self._props['align'] = value
    if value == 'justify':
      self.dom_nodes['anvil-m3-text-container'].style.justifyContent = 'left'
    else:
      self.dom_nodes['anvil-m3-text-container'].style.justifyContent = value
    self.dom_nodes['anvil-m3-text'].style.textAlign = value

  @property
  def font_size(self):
    return self._props.get('font_size')

  @font_size.setter
  def font_size(self, value):
    self._props['font_size'] = value
    if value: value = f'{value}px'
    self.dom_nodes['anvil-m3-text'].style.fontSize = value
    self.dom_nodes['anvil-m3-text-container'].style.fontSize = value

  @property
  def icon(self):
    return self._icon

  @property
  def line_height(self):
    return self._props.get('line_height')

  @line_height.setter
  def line_height(self, value):
    self._props['line_height'] = value
    self.dom_nodes['anvil-m3-text-container'].style.lineHeight = value
    self.dom_nodes['anvil-m3-text'].style.lineHeight = value

  @icon.setter
  def icon(self, value):
    self._icon = value
    if value:
      self.dom_nodes['anvil-m3-text-icon'].style.marginRight = "8px"
    else:
      self.dom_nodes['anvil-m3-text-icon'].style.marginRight = ""
    self.dom_nodes['anvil-m3-text-icon'].innerText = value[3:]

  @property
  def style(self):
    return self._style

  @style.setter
  def style(self, value):
    self._style = value
    self.dom_nodes['anvil-m3-text'].classList.remove('anvil-m3-text-label', 'anvil-m3-text-body')
    self.dom_nodes['anvil-m3-text'].classList.add(f'anvil-m3-text-{value}')
    self.dom_nodes['anvil-m3-text-container'].classList.remove('anvil-m3-text-label', 'anvil-m3-text-body')
    self.dom_nodes['anvil-m3-text-container'].classList.add(f'anvil-m3-text-{value}')

  @property
  def scale(self):
    return self._scale

  @scale.setter
  def scale(self, value):
    self._scale = value
    self.dom_nodes['anvil-m3-text'].classList.remove('anvil-m3-text-large', 'anvil-m3-text-medium', 'anvil-m3-text-small')
    self.dom_nodes['anvil-m3-text-container'].classList.remove('anvil-m3-text-large', 'anvil-m3-text-medium', 'anvil-m3-text-small')
    self.dom_nodes['anvil-m3-text'].classList.add(f'anvil-m3-text-{value}')
    self.dom_nodes['anvil-m3-text-container'].classList.add(f'anvil-m3-text-{value}')

#!defClass(material_3, Text, anvil.Component)!:      
