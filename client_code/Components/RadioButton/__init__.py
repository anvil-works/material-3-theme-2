from ._anvil_designer import RadioButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from anvil.js.window import document
import anvil.designer
from ...Functions import checked_property, name_property, innerText_property, enabled_property, style_property, underline_property, italic_property, bold_property, font_size_property, color_property, theme_color_to_css, value_property

class RadioButton(RadioButtonTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-radiobutton-hover'].addEventListener("click", self.handle_click)

  # Properties 
  visible = HtmlTemplate.visible
  group_name = name_property('anvil-m3-radiobutton-input')
  value = value_property('anvil-m3-radiobutton-input')
  enabled = enabled_property('anvil-m3-radiobutton-input')
  italic = italic_property('anvil-m3-radiobutton-label')
  bold = bold_property('anvil-m3-radiobutton-label')
  underline = underline_property('anvil-m3-radiobutton-label')
  font_size = font_size_property('anvil-m3-radiobutton-label')
  border = style_property('anvil-m3-radiobutton-container', 'border')
  font = style_property('anvil-m3-radiobutton-label', 'fontFamily')
  text_color = color_property('anvil-m3-radiobutton-label', 'color')
  background = color_property('anvil-m3-radiobutton-container', 'backgroundColor')
  text = innerText_property('anvil-m3-radiobutton-label')
  align = style_property('anvil-m3-radiobutton-component', 'justifyContent')
  selected = checked_property('anvil-m3-radiobutton-input')

  # Class Functions
  def _anvil_get_design_info_(self, as_layout=False):
    di = super()._anvil_get_design_info_(as_layout)
    di['interactions'] = [
      {
      "type": "whole_component_multi",
      "title": "Align",
      "options": [{
        "name": "Left Align",
        "id": "left",
        "icon" : "align-left",
      },{
        "name": "Left Center",
        "id": "center",
        "icon" : "align-center",
      },{
        "name": "Left Right",
        "id": "right",
        "icon" : "align-right",
      }],
      "callbacks": {
        "execute": self.setAlignment
      }
    },
      {
      "type": "whole_component",
      "title": "Visible",
      "icon": "add", #TODO: eye icon
      "callbacks": {
        "execute": self.toggle_visible
      }
    }, {
      "type": "whole_component",
      "title": "Enable",
      "icon": "add", #TODO: power icon
      "callbacks": {
        "execute": self.toggle_enabled
      }
    },{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-radiobutton-label'])
      },   
    },{
      "type": "region",
      "bounds": self.dom_nodes['anvil-m3-radiobutton-hover'],
      "callbacks": {
        "doubleClick": self.toggle_selected
      }
    } ]
    return di 

  # todo: interaction bold, italic, underline
  def toggle_selected(self):
    self.selected = not self.selected
    anvil.designer.update_component_properties(self, {'selected': self.selected})

  def toggle_enabled(self):
    self.enabled = not self.enabled
    anvil.designer.update_component_properties(self, {'enabled': self.enabled})

  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})

  def setAlignment(self, value):
    self.align = value
    anvil.designer.update_component_properties(self, {'align': self.align})

  
  # def _anvil_get_design_info_(self, as_layout=False):
  #   di = super()._anvil_get_design_info_(as_layout)
  #   di['interactions'] = [{
  #     "type": "whole_component",
  #     "title": "Toggle",
  #     "icon": "edit",
  #     "default": True,
  #     "callbacks": {
  #       "execute": self.toggle_checked 
  #     }
  #   },
  #   {
  #     "type": "region",
  #     "bounds": self.dom_nodes['anvil-m3-checkbox-label'],
  #     "callbacks": {
  #       "doubleClick": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-checkbox-label'])
  #     }
  #   }       
  #   ]
  #   return di

    
  def handle_click(self, event):
    if self.enabled:
      self.dom_nodes['anvil-m3-radiobutton-input'].focus()
      self.selected = True
      self.raise_event("clicked")
    
  def form_show(self, **event_args):
    if anvil.designer.in_designer and not self.text:
      self.text = anvil.designer.get_design_name(self)

  def get_group_value(self):
    selectedItem = document.querySelector(f".anvil-m3-radiobutton-input[name={self.group_name}]:checked")
    return selectedItem.value
