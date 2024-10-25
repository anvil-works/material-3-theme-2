from ._anvil_designer import RadioButtonTemplate
from anvil import *
import anvil.server
from anvil import HtmlTemplate
from anvil.js.window import document
import anvil.designer
from ..._Components.RadioGroupPanel import RadioGroup
from ...Functions import role_property, tooltip_property, enabled_property, style_property, underline_property, italic_property, border_property, bold_property, font_size_property, color_property, theme_color_to_css, font_family_property, spacing_property
from ...utils import gen_id
from ...utils.properties import anvil_prop

class RadioButton(RadioButtonTemplate):
  def __init__(self, **properties):
    self.tag = ComponentTag()
    self._props = properties
    self._tooltip_node = None
    self._design_name = ""
    self._group = None
    self._group_set_from_code = False
    self.init_components(**properties)

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

    self.dom_nodes['anvil-m3-radiobutton-hover'].addEventListener("click", self._handle_click)
    self.dom_nodes['anvil-m3-radiobutton-input'].addEventListener("change", self._handle_change)

    if not anvil.designer.in_designer:
        id = gen_id()
        self.dom_nodes["anvil-m3-radiobutton-input"].id = id
        self.dom_nodes["anvil-m3-radiobutton-label"].setAttribute("for", id)

  def _on_mount(self, **event_args):
    if not self._group_set_from_code:
      self._set_group(RadioGroup.enclosing(self))

  def _on_cleanup(self, **event_args):
    if not self._group_set_from_code:
      self._set_group(None)

  #!componentEvent(material_3.RadioButton)!1: {name: "change", description: "When the Radio Button is selected or unselected."}
  #!componentEvent(material_3.RadioButton)!1: {name: "show", description: "When the Radio Button is shown on the screen."}
  #!componentEvent(material_3.RadioButton)!1: {name: "hide", description: "When the Raio Button is removed from the screen."}

  #!componentProp(material_3.RadioButton)!1: {name:"enabled",type:"boolean",description:"If True, this component allows user interaction."}
  #!componentProp(material_3.RadioButton)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."} 
  #!componentProp(material_3.RadioButton)!1: {name:"underline",type:"boolean",description:"If True, this component’s text will be underlined."}
  #!componentProp(material_3.RadioButton)!1: {name:"italic",type:"boolean",description:"If True, this component’s text will be italic."}
  #!componentProp(material_3.RadioButton)!1: {name:"bold",type:"boolean",description:"If True, this component’s text will be bold."}
  #!componentProp(material_3.RadioButton)!1: {name:"font_size",type:"number",description:"The font size of text displayed on this component."}
  #!componentProp(material_3.RadioButton)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(material_3.RadioButton)!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  #!componentProp(material_3.RadioButton)!1: {name:"text_color",type:"color",description:"The color of the text on the component."} 
  #!componentProp(material_3.RadioButton)!1: {name:"background_color",type:"color",description:"The color of the background of this component."}
  #!componentProp(material_3.RadioButton)!1: {name:"align",type:"enum",description:"The position of this component in the available space."} 
  #!componentProp(material_3.RadioButton)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(material_3.RadioButton)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(material_3.RadioButton)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles"} 
  #!componentProp(material_3.RadioButton)!1: {name:"text",type:"string",description:"The text displayed on this component"}
  #!componentProp(material_3.RadioButton)!1: {name:"radio_color",type:"color",description:"The color of the radio button."}
  #!componentProp(material_3.RadioButton)!1: {name:"selected",type:"boolean",description:"If True, the radio button is selected."}
  #!componentProp(material_3.RadioButton)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}

  # Properties 
  enabled = enabled_property('anvil-m3-radiobutton-input')
  visible = HtmlTemplate.visible
  value = anvil_prop('value')
  underline = underline_property('anvil-m3-radiobutton-label')
  italic = italic_property('anvil-m3-radiobutton-label')
  bold = bold_property('anvil-m3-radiobutton-label')
  font_size = font_size_property('anvil-m3-radiobutton-label')
  border = border_property('anvil-m3-radiobutton-container')
  font_family = font_family_property('anvil-m3-radiobutton-label', 'font_family')
  text_color = color_property('anvil-m3-radiobutton-label', 'color', 'text_color')
  background_color = color_property('anvil-m3-radiobutton-component', 'backgroundColor', 'background')
  align = style_property('anvil-m3-radiobutton-component', 'justifyContent', 'align')
  spacing = spacing_property('anvil-m3-radiobutton-component')
  tooltip = tooltip_property('anvil-m3-radiobutton-component')
  role = role_property('anvil-m3-radiobutton-container')
  
  @property
  def radio_color(self):
    return self._props.get('radio_color')

  @radio_color.setter
  def radio_color(self, value):
    if value: value = theme_color_to_css(value)
    self.dom_nodes['anvil-m3-radiobutton-checked'].style['color'] = value
    self.dom_nodes['anvil-m3-radiobutton-unchecked'].style['color'] = value
    self._props['radio_color'] = value

  @property
  def group(self):
    return self._group

  @group.setter
  def group(self, new_group):
    if not (new_group is None or isinstance(new_group, RadioGroup)):
      raise ValueError("group must be a RadioGroup object")

    self._group_set_from_code = True
    self._set_group(new_group)

  def _set_group(self, new_group):
    if self._group is not None:
      self._group._remove_button(self)

    self._group = new_group
    if new_group is None:
      self.dom_nodes["anvil-m3-radiobutton-input"].name = ""
    else:
      new_group._add_button(self)
      self.dom_nodes["anvil-m3-radiobutton-input"].name = id(new_group)

  @property
  def selected(self):
    return self.dom_nodes['anvil-m3-radiobutton-input'].checked

  @selected.setter
  def selected(self, new_state):
    self.dom_nodes['anvil-m3-radiobutton-input'].checked = new_state

    # The previously selected RadioButton needs deselecting in the designer yml
    if anvil.designer.in_designer and new_state and self._group is not None:
      for button in self._group.buttons:
        if button is not self:
          try:
            anvil.designer.update_component_properties(button, {'selected': False})
          except anvil.js.ExternalError:
            pass  # Ignore error if the component isn't on the currently editing form

  @anvil_prop
  def text(self, value):
    v = value
    self.dom_nodes['anvil-m3-radiobutton-label'].classList.toggle('anvil-m3-textlessComponentText', False)
    if anvil.designer.in_designer and not value:
      v = self._design_name
      self.dom_nodes['anvil-m3-radiobutton-label'].classList.toggle('anvil-m3-textlessComponentText', True)
    self.dom_nodes['anvil-m3-radiobutton-label'].innerText = v
  
  # Class Functions
  def _anvil_get_interactions_(self):
    return [
      {
        "type": "whole_component",
        "title": "Edit text",
        "icon": "edit",
        "default": True,
        "callbacks": {
          "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-radiobutton-label'])
        },   
      },
      {
        "type": "region",
        "bounds": self.dom_nodes['anvil-m3-radiobutton-hover'],
        "sensitivity": 0,
        "callbacks": {
          "execute": self._toggle_selected
        }
      }
    ]

  def _toggle_selected(self):
    self.selected = not self.selected
    anvil.designer.update_component_properties(self, {'selected': self.selected})
   
  def _handle_click(self, event):
    if not anvil.designer.in_designer:
      self.dom_nodes['anvil-m3-radiobutton-input'].click()

  def _handle_change(self, event):
    if self._group is not None:
      self._group._handle_change()
    self.raise_event("select")

  def form_show(self, **event_args):
    if anvil.designer.in_designer:
      self._design_name = anvil.designer.get_design_name(self)
      if not self.text:
        self.dom_nodes['anvil-m3-radiobutton-label'].innerText = self._design_name

#!defClass(material_3, RadioButton, anvil.Component)!:
