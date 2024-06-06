from ._anvil_designer import NavigationLinkTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from ...Functions import color_property, role_property, tooltip_property, href_property, innerHTML_property, font_family_property, font_size_property, margin_property
import anvil.designer

#Currently, material_icon works and not icon (because they can't both work at the same time)
class NavigationLink(NavigationLinkTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._tooltip_node = None
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)
    
  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-navigation-link'].addEventListener("click", self._handle_click)
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-navigation-link'].removeEventListener("click", self._handle_click)
    
    if anvil.designer.in_designer:
      anvil.designer.register_interaction(self, self.dom_nodes['anvil-m3-navigation-link'], 'dblclick', lambda x: anvil.designer.start_editing_form(self.navigate_to))

  def _handle_click(self, event):
    self.raise_event("click")
    if self.navigate_to:
      open_form(self.navigate_to)
      self.selected = True

  def _anvil_get_interactions_(self):
    return [{
        "type": "whole_component",
        "title": "Edit text",
        "icon": "edit",
        "default": True,
        "callbacks": {
          "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-navigation-link-text'])
        }
      }]

  visible = HtmlTemplate.visible
  text = innerHTML_property('anvil-m3-navigation-link-text')
  role = role_property('anvil-m3-navigation-link')

  @property
  def url(self):
    return self._props.get('url')

  @url.setter
  def url(self, value):
    if value:
      self._props['url'] = value
      self.dom_nodes['anvil-m3-navigation-link'].href = value
    else:
      self.dom_nodes['anvil-m3-navigation-link'].href = 'javascript:void(0)'

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    link_icon = self.dom_nodes['anvil-m3-navigation-link-icon']
    self._material_icon = value
    if value:
      link_icon.className = ""
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value

  @property
  def selected(self):
    return self._selected

  @selected.setter
  def selected(self, value):
    if value:
      self.dom_nodes['anvil-m3-navigation-link'].classList.add('anvil-m3-navigation-link-selected')
    else:
      self.dom_nodes['anvil-m3-navigation-link'].classList.remove('anvil-m3-navigation-link-selected')
    self._selected = value

  @property
  def badge(self):
    return self._badge

  @badge.setter
  def badge(self, value):
    if value:
      self.dom_nodes['anvil-m3-icon-badge'].style.display = "block"
    else:
      self.dom_nodes['anvil-m3-icon-badge'].style.display = "none"
    self._badge = value

  @property
  def badge_count(self):
    return self._badge_count

  @badge_count.setter
  def badge_count(self, value):
    if value and self.badge:
      self.dom_nodes['anvil-m3-icon-badge'].innerHTML = value
      self.dom_nodes['anvil-m3-icon-badge'].classList.add("anvil-m3-large-badge")
    else:
      self.dom_nodes['anvil-m3-icon-badge'].innerHTML = ""
      self.dom_nodes['anvil-m3-icon-badge'].classList.remove("anvil-m3-large-badge")
    self._badge_count = value

  @property
  def navigate_to(self):
    return self._navigate_to

  @navigate_to.setter
  def navigate_to(self, value):
    self._navigate_to = value

  text_color = color_property('anvil-m3-navigation-link-text', 'color', 'text_color')
  icon_color = color_property('anvil-m3-navigation-link-icon', 'color', 'icon_color')
  font_family = font_family_property('anvil-m3-navigation-link-text')
  font_size = font_size_property('anvil-m3-navigation-link-text', 'font_size')
  icon_size = font_size_property('anvil-m3-navigation-link-icon', 'icon_size')
  tooltip = tooltip_property('anvil-m3-navigation-link-container')
  margin = margin_property('anvil-m3-navigation-link-container')

  
