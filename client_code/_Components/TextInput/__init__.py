from ._anvil_designer import TextInputTemplate
from anvil import *
import anvil.server
from ...Functions import italic_property, bold_property, underline_property, font_size_property, font_family_property, color_property, margin_property, tooltip_property, theme_color_to_css
from anvil import HtmlTemplate
from ...utils import gen_id
from ...utils.properties import get_unset_value, get_unset_margin, anvil_prop

class TextInput(TextInputTemplate):
  def __init__(self, **properties):
    self.tag = ComponentTag()
    self._props = properties
    self._tooltip_node = None
    self.init_components(**properties)
    
    self._on_input = self._on_input

  def _get_common_unset_property_values_(self):
    el = self.dom_nodes['anvil-m3-textinput']
    m = get_unset_margin(el, self.margin)
    lfs = get_unset_value(self.dom_nodes['anvil-m3-label-text'], "fontSize", self.label_font_size)
    spfs = get_unset_value(self.dom_nodes['anvil-m3-supporting-text'], "fontSize", self.supporting_text_font_size)
    clfs = get_unset_value(self.dom_nodes['anvil-m3-character-counter'], "fontSize", self.character_limit_font_size)
    return {"label_font_size": lfs, "supporting_text_font_size": spfs, "character_limit_font_size": clfs, "margin": m}
    
  def _set_id(self, value):
    self.dom_nodes["anvil-m3-label-text"].setAttribute("for", value)
    self.dom_nodes["anvil-m3-supporting-text"].setAttribute("for", value)
    self.dom_nodes["anvil-m3-character-amount"].setAttribute("for", value)

  def _on_input(self, e):
    self.dom_nodes['anvil-m3-character-amount'].innerText = len(e.target.value)
    # input event is anvil's change event
    self.raise_event("change")

  def _on_change(self, e):
    # On text input/textarea the change event fires when we lose focus
    self.raise_event("x-anvil-write-back-input_text")

  def _on_focus(self, e):
    self.raise_event("focus")

  def _on_lost_focus(self, e):
    self.raise_event("lost_focus")

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "label_text", self.dom_nodes['anvil-m3-label-text'])
      }
    }]
 
  visible = HtmlTemplate.visible
  label_italic = italic_property('anvil-m3-label-text', 'label_italic')
  label_bold = bold_property('anvil-m3-label-text', 'label_bold')
  label_underline = underline_property('anvil-m3-label-text', 'label_underline')
  label_font_size = font_size_property('anvil-m3-label-text', 'label_font_size')
  label_font_family = font_family_property('anvil-m3-label-text', 'label_font_family')
  label_color = color_property('anvil-m3-label-text', 'color', 'label_color')
  margin = margin_property('anvil-m3-textinput')
  tooltip = tooltip_property('anvil-m3-textinput')
  supporting_text_color = color_property('anvil-m3-supporting-text', 'color', 'supporting_text_color')
  supporting_text_font_family = font_family_property('anvil-m3-supporting-text', 'supporting_text_font_family')
  supporting_text_font_size = font_size_property('anvil-m3-supporting-text', 'supporting_text_font_size')
  character_limit_color = color_property('anvil-m3-character-counter', 'color', 'charcter_limit_color')
  character_limit_font_family = font_family_property('anvil-m3-character-counter', 'character_limit_font_family')
  character_limit_font_size = font_size_property('anvil-m3-character-counter', 'character_limit_font_size')

  @anvil_prop
  def appearance(self, value):
    if value == 'outlined':
      self.dom_nodes['anvil-m3-textinput'].classList.toggle('outlined', True) 
    else:
      self.dom_nodes['anvil-m3-textinput'].classList.toggle('outlined', False)

  @anvil_prop
  def supporting_text(self, value):
    self.dom_nodes['anvil-m3-supporting-text'].innerHTML = value

  @anvil_prop
  def error(self, value):
    classes = self.dom_nodes['anvil-m3-textinput'].classList
    if value:
      classes.add("anvil-m3-textinput-error")
    else:
      classes.remove("anvil-m3-textinput-error")

  @anvil_prop
  def border_color(self, value):
    if self.border_color:
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-outlined-border', theme_color_to_css(self.border_color))
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-outlined-border-hover', theme_color_to_css(self.border_color))
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-outlined-border-focus', theme_color_to_css(self.border_color))
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-filled-border', theme_color_to_css(self.border_color))
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-filled-border-hover', theme_color_to_css(self.border_color))
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-filled-border-focus', theme_color_to_css(self.border_color))
    else:
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-outlined-border', 'var(--anvil-m3-outline)')
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-outlined-border-hover', 'var(--anvil-m3-on-surface)')
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-outlined-border-focus', 'var(--anvil-m3-primary)')
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-filled-border', 'var(--anvil-m3-on-surface-variant)')
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-filled-border-hover', 'var(--anvil-m3-on-surface)')
      self.dom_nodes["anvil-m3-textinput"].style.setProperty('--anvil-m3-filled-border-focus', 'var(--anvil-m3-primary)')

  def form_show(self, **event_args):
    id = gen_id();
    self._set_id(id)
    if anvil.designer.in_designer:
      if not self.label:
        self.dom_nodes['anvil-m3-label-text'].innerText = anvil.designer.get_design_name(self)