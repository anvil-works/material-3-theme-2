from ._anvil_designer import TextFieldTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import property_with_callback, name_property, innerText_property, enabled_property, style_property, underline_property, italic_property, bold_property, font_size_property, color_property, theme_color_to_css, value_property
import anvil.designer

# Todo: region interactions

class TextField(TextFieldTemplate):
  def __init__(self, **properties):
    
    self._props = properties
    self._label_text = properties.get('label_text', '')
    self._trailing_icon = properties.get('trailing_icon', '')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.dom_nodes['text-field-input'].addEventListener("keydown", self.on_key_down)
    self.dom_nodes['text-field-input'].addEventListener("change", self.on_change)
    # self.dom_nodes['text-field-input'].addEventListener("keydown", self.char_counter)

    # Any code you write here will run before the form opens.

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

  # def char_counter(self, e):
  #   input = self.dom_nodes['text-field-input']
  #   count = input.value
  #   print(count)
  
  visible = HtmlTemplate.visible
  
  background = color_property('text-field-input', 'backgroundColor')
  
  italic_label = italic_property('label-text')
  bold_label = bold_property('label-text')
  underline_label = underline_property('label-text')
  label_font_size = font_size_property('label-text')
  label_font = style_property('label-text', 'fontFamily')
  label_text_color = color_property('label-text', 'color')
  
  # label_text = innerText_property('label-text')
  def set_label(self, value):
    self.dom_nodes['label-text'].innerText = value or ""
  label_text = property_with_callback("label_text", set_label)
    
  italic_display = italic_property('text-field-input')
  bold_display = bold_property('text-field-input')
  underline_display = underline_property('text-field-input')
  display_font_size = font_size_property('text-field-input')
  display_font = style_property('text-field-input', 'fontFamily')
  display_text_color = color_property('text-field-input', 'color')
  # display_text = innerText_property('text-field-input')
  
  # @property
  # def label_text(self):
  #   return self._label_text

  # @label_text.setter
  # def label_text(self, value):
  #   self._label_text = value
  #   self.dom_nodes['label-text'].innerHTML = value or ""

  @property
  def supporting_text(self):
    return self.dom_nodes['text-field-supporting'].innerHTML

  @supporting_text.setter
  def supporting_text(self, value):
    self._supporting_text = value
    if value:
      self.dom_nodes['text-field-supporting'].innerHTML = value

  # @property
  # def max_characters(self):
  #   return self._max_characters

  # @max_characters.setter
  # def max_characters(self, value):
  #   character_count = self.dom_nodes['text-field-character-count']
  #   if value:
  #     character_count.style.display = "block"
  #     character_count.innerHTML = value

  @property
  def leading_icon(self):
    return self._leading_icon

  @leading_icon.setter
  def leading_icon(self, value):
    self._leading_icon = value
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

  @property
  def trailing_icon(self):
    return self._trailing_icon

  @trailing_icon.setter
  def trailing_icon(self, value):
    self._trailing_icon = value
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

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    input = self.dom_nodes['text-field-input']
    supporting_text = self.dom_nodes['text-field-supporting']
    if value:
      input.removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-text-field-supporting-disabled")
    else:
      input.setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-text-field-supporting-disabled")

  @property
  def appearance(self):
    return self._appearance

  @appearance.setter
  def appearance(self, value):
    self._appearance = value
    classes = self.dom_nodes['text-field'].classList
    classes.remove("anvil-m3-outlined")
    if value:
      classes.add(f"anvil-m3-{value}")

  @property
  def error(self):
    return self._error

  @error.setter
  def error(self, value):
    self._error = value
    classes = self.dom_nodes['text-field'].classList
    if value:
      classes.add("anvil-m3-tfield-error")
      if self.trailing_icon:
        self.trailing_icon = "error"
    else:
      classes.remove("anvil-m3-tfield-error")

  @property
  def placeholder(self):
    return self._placeholder

  @placeholder.setter
  def placeholder(self, value):
    self._placeholder = value
    input = self.dom_nodes['text-field-input']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.designer.in_designer:
      if not self.label_text:
        self.label_text = anvil.designer.get_design_name(self)
