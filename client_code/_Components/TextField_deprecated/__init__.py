from ._anvil_designer import TextField_deprecatedTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import property_with_callback, innerText_property, enabled_property, underline_property, italic_property, bold_property, font_size_property, color_property, theme_color_to_css, margin_property, font_family_property
import anvil.designer

# Todo: region interactions

class TextField_deprecated(TextField_deprecatedTemplate):
  def __init__(self, **properties):
    
    self._props = properties
    self.init_components(**properties)

    self.on_key_down = self.on_key_down
    self.on_change = self.on_change
    self.on_input = self.on_input
    
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['text-field-input'].addEventListener("keydown", self.on_key_down)
    self.dom_nodes['text-field-input'].addEventListener("change", self.on_change)
    self.dom_nodes['text-field-input'].addEventListener("input", self.on_input)
  def on_cleanup(self, **event_args):
    self.dom_nodes['text-field-input'].removeEventListener("keydown", self.on_key_down)
    self.dom_nodes['text-field-input'].removeEventListener("change", self.on_change)
    self.dom_nodes['text-field-input'].removeEventListener("input", self.on_input)

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "label_text", self.dom_nodes['label-text'])
      }
    }]

  def on_key_down(self, e):
    if e.key == "Enter":
      self.raise_event("pressed_enter")

  def on_change(self, e):
    self.raise_event("change")
    
  def on_input(self, e):
    self.dom_nodes['text-field-character-amount'].innerText = len(e.target.value);

  visible = HtmlTemplate.visible
  background = color_property('text-field-input', 'backgroundColor', 'background')
  italic_label = italic_property('label-text', 'italic_label')
  bold_label = bold_property('label-text', 'bold_label')
  underline_label = underline_property('label-text', 'underline_label')
  label_font_size = font_size_property('label-text', 'label_font_size')
  label_font = font_family_property('label-text', 'label_font')
  label_text_color = color_property('label-text', 'color', 'label_text_color')
  
  def set_label(self, value):
    self.dom_nodes['label-text'].innerText = value or ""
    if value:
      self.dom_nodes['text-field-input'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['text-field-input'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", set_label)
  
  italic_display = italic_property('text-field-input', 'italic_label')
  bold_display = bold_property('text-field-input', 'bold_display')
  underline_display = underline_property('text-field-input', 'underline_display')
  display_font_size = font_size_property('text-field-input', 'display_font_size')
  display_font = font_family_property('text-field-input', 'display_font')
  display_text_color = color_property('text-field-input', 'color', 'display_text_color')
  margin = margin_property('text-field')

  def set_supporting_text(self, value):
    self.dom_nodes['text-field-supporting'].innerHTML = value
  supporting_text = property_with_callback("supporting_text", set_supporting_text)
      
  def set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['text-field-input'].removeAttribute("maxlength")
      self.dom_nodes['text-field-character-counter'].style = "display: none";
    else:
      text_field_input = self.dom_nodes['text-field-input'].setAttribute("maxlength", value)
      self.dom_nodes['text-field-character-counter'].style = "display: inline";
      self.dom_nodes['text-field-character-limit'].innerText = value;
  character_limit = property_with_callback("character_limit", set_character_limit)

  def set_leading_icon(self, value):
    icon_container = self.dom_nodes['anvil-m3-icon-container']
    leading_icon = self.dom_nodes['leading-icon']
    text_field_input = self.dom_nodes['text-field-input']
    border_container = self.dom_nodes['anvil-m3-border-container']
    self._material_icon = value
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
  leading_icon = property_with_callback("leading_icon", set_leading_icon)    

  def set_trailing_icon(self, value):
    icon_container = self.dom_nodes['anvil-m3-icon-container']
    trailing_icon = self.dom_nodes['trailing-icon']
    text_field_input = self.dom_nodes['text-field-input']
    self._material_icon = value
    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "none"
      trailing_icon.innerText = ""
      text_field_input.style.paddingRight = "16px"
  trailing_icon = property_with_callback("trailing_icon", set_trailing_icon)

  def set_enabled(self, value):
    input = self.dom_nodes['text-field-input']
    supporting_text = self.dom_nodes['text-field-supporting']
    if value:
      input.removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-text-field-supporting-disabled")
    else:
      input.setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-text-field-supporting-disabled")
  enabled = property_with_callback("enabled", set_enabled)

  def set_appearance(self, value):
    classes = self.dom_nodes['text-field'].classList
    classes.remove("anvil-m3-outlined")
    if value:
      classes.add(f"anvil-m3-{value}")
  appearance = property_with_callback("appearance", set_appearance)
  
  def set_error(self, value):
    classes = self.dom_nodes['text-field'].classList
    if value:
      classes.add("anvil-m3-tfield-error")
      if self.trailing_icon:
        self.trailing_icon = "error"
    else:
      classes.remove("anvil-m3-tfield-error")
  error = property_with_callback("error", set_error)

  def set_placeholder(self, value):
    input = self.dom_nodes['text-field-input']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', set_placeholder)

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer:
      if not self.label_text:
        self.dom_nodes['label-text'].innerText = anvil.designer.get_design_name(self)
