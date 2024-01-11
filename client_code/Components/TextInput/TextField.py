import anvil.server
from . import TextInput
import anvil.designer
from ...Functions import property_with_callback, italic_property, bold_property, underline_property, font_family_property, font_size_property, color_property
from anvil.property_utils import anvil_property
from ...utils import _m3_icons

"""
Remaining tasks on hold for DEV: 
- property "NONE" enum selection for icons
- properties being set in init -> Once this is done we will have to do all the style props for the textarea
"""

leading_icon_property = {"name": "leading_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Attributes", 
                         "important": True, 
                         "default_value": "",
                         # "include_none_option": True, 
                         # "none_option_label": "None", 
                         "description": "right side icon"}
trailing_icon_property = {"name": "trailing_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Attributes", 
                         "important": True, 
                         "default_value": "",
                         # "include_none_option": True, 
                         "description": "left side icon"}

# italic_display_property = {"name": "italic_display", "type": "boolean", "default_value": False, "important": False," description": "Display this component’s text in italics", "group": "Style"}
# bold_display_property = {"name": "bold_display", "type": "boolean", "default_value": False, "important": False, "description": "Display this component’s text in bold", "group": "Style"}
# underline_display_property = {"name": "underline_display", "type": "boolean", "default_value": False, "important": False, "description": "Display this component’s text in underline", "group": "Style"}
# display_font_property = {"name": "display_font", "type": "string", "default_value": '', "important": False, "description": "The font family to use for this component’s text", "group": "Style"}
# display_font_size_property = {"name": "display_font_size", "type": "number", "important": False, "description": "The height of text displayed on this component’s text in pixels", "group": "Style"}
# display_text_color_property = {"name": "display_text_color", "type": "color", "default_value": '', "important": False, "description": "Component’s Input Text Color",  "group": "Style"}

click_event = {"name": "click", "defaultEvent": True, "description": "When the trailing icon is clicked"}

class TextField(TextInput):
  _anvil_properties_ = [leading_icon_property, trailing_icon_property, *TextInput._anvil_properties_]
  _anvil_events_ = [click_event, *TextInput._anvil_events_]
  
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['textarea']
    self.dom_nodes['input-container'].removeChild(hiddenInput)
    
    self.on_key_down = self.on_key_down
    self.on_change = self.on_change
    self.handle_click = self.handle_click

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['textfield'].addEventListener("input", self.on_input)
    self.dom_nodes['textfield'].addEventListener("keydown", self.on_key_down)
    self.dom_nodes['textfield'].addEventListener("change", self.on_change)
    self.dom_nodes['trailing-icon'].addEventListener("click", self.handle_click)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['textfield'].removeEventListener("input", self.on_input)
    self.dom_nodes['textfield'].removeEventListener("keydown", self.on_key_down)
    self.dom_nodes['textfield'].removeEventListener("change", self.on_change)
    self.dom_nodes['trailing-icon'].removeEventListener("click", self.handle_click)
  

  def set_placeholder(self, value):
    input = self.dom_nodes['textfield']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', set_placeholder)
      
  def set_label(self, value):
    self.dom_nodes['label-text'].innerText = value or ""
    if value:
      self.dom_nodes['textfield'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['textfield'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", set_label)

  def set_enabled(self, value):
    supporting_text = self.dom_nodes['subcontent']
    if value:
      self.dom_nodes['textfield'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['textfield'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
  enabled = property_with_callback("enabled", set_enabled)
  
  def set_id(self, value):
    super().set_id(value)
    self.dom_nodes["textfield"].id = value

  def set_error(self, value):
    super().set_error(value)
    icon = "error" if value else self.trailing_icon
    self.set_trailing_icon(icon)
  error = property_with_callback("error", set_error)

  @anvil_property('enum')
  def leading_icon(self):
    return self._props.get('leading_icon')

  @leading_icon.setter
  def leading_icon(self, value):
    self._props['leading_icon'] = value
    self.set_leading_icon(value)

  @anvil_property('enum')
  def trailing_icon(self):
    return self._props.get('trailing_icon')

  @trailing_icon.setter
  def trailing_icon(self, value):
    self._props['trailing_icon'] = value
    self.set_trailing_icon(value)
    
  def set_leading_icon(self, value):
    icon_container = self.dom_nodes['icon-container']
    leading_icon = self.dom_nodes['leading-icon']
    text_field_input = self.dom_nodes['textfield']
    border_container = self.dom_nodes['border-container']

    if value:
      leading_icon.style.display = "block"
      leading_icon.innerText = value
      icon_container.style.paddingLeft = "12px"
      text_field_input.style.paddingLeft = "48px"
      border_container.classList.add("with-icon")
    else:
      leading_icon.style.display = "none"
      leading_icon.innerText = ""
      icon_container.style.paddingLeft = "16px"
      text_field_input.style.paddingLeft = "16px"
      border_container.classList.remove("with-icon")
  # leading_icon = property_with_callback("leading_icon", set_leading_icon)  
  
  def set_trailing_icon(self, value):
    icon_container = self.dom_nodes['icon-container']
    trailing_icon = self.dom_nodes['trailing-icon']
    text_field_input = self.dom_nodes['textfield']

    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "none"
      trailing_icon.innerText = ""
      text_field_input.style.paddingRight = "16px"
  # trailing_icon = property_with_callback("trailing_icon", set_trailing_icon)

  italic_display = italic_property('textfield', 'italic_label')
  bold_display = bold_property('textfield', 'bold_display')
  underline_display = underline_property('textfield', 'underline_display')
  display_font_size = font_size_property('textfield', 'display_font_size')
  display_font = font_family_property('textfield', 'display_font')
  display_text_color = color_property('textfield', 'color', 'display_text_color')

  def set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['textfield'].removeAttribute("maxlength")
      self.dom_nodes['character-counter'].style = "display: none";
    else:
      text_field_input = self.dom_nodes['textfield'].setAttribute("maxlength", value)
      self.dom_nodes['character-counter'].style = "display: inline";
      self.dom_nodes['character-limit'].innerText = int(value);
  character_limit = property_with_callback("character_limit", set_character_limit)

  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

