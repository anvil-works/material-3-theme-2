import anvil
import anvil.designer

from ..._utils.properties import (
  anvil_prop,
  bold_property,
  color_property,
  font_family_property,
  font_size_property,
  italic_property,
  role_property,
  spacing_property,
  style_property,
  tooltip_property,
  underline_property,
)
from ._anvil_designer import LinkTemplate


class Link(LinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.temp_url = None
    self.tag = anvil.ComponentTag()
    self._props = properties
    self._tooltip_node = None
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-link'].addEventListener("click", self._handle_click)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_cleanup(self, **event_args):
    self._revoke_tmp_url()

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if (
      anvil.designer.in_designer
      and not self.text
      and not self.icon
      and not self.get_components()
    ):
      self.dom_nodes['anvil-m3-link-text'].innerText = anvil.designer.get_design_name(
        self
      )
      self.dom_nodes['anvil-m3-link-text'].style.display = 'block'

  def _handle_click(self, event):
    keys = {
      'shift': event.shiftKey,
      'alt': event.altKey,
      'ctrl': event.ctrlKey,
      'meta': event.metaKey,
    }
    self.raise_event("click", keys=keys, event=event)

  def _anvil_get_interactions_(self):
    return [
      {
        "type": "whole_component",
        "title": "Edit text",
        "icon": "edit",
        "default": True,
        "callbacks": {
          "execute": lambda: anvil.designer.start_inline_editing(
            self, "text", self.dom_nodes['anvil-m3-link-text']
          )
        },
      }
    ]

  def _revoke_tmp_url(self):
    if self.temp_url:
      self.temp_url.revoke()

  #!componentEvent(m3.Link)!1: {name: "click", description: "When the Link is clicked."}
  #!componentEvent(m3.Link)!1: {name: "show", description: "When the Link is shown on the screen."}
  #!componentEvent(m3.Link)!1: {name: "hide", description: "When the Link is removed from the screen."}

  #!componentProp(m3.Link)!1: {name:"text",type:"string",description:"The text displayed on this component."}
  #!componentProp(m3.Link)!1: {name:"align",type:"enum", options:["left", "center", "right"],description:"The position of this component in the available space."}
  #!componentProp(m3.Link)!1: {name:"italic",type:"boolean",description:"If True, this component’s text will be italic."}
  #!componentProp(m3.Link)!1: {name:"bold",type:"boolean",description:"If True, this component’s text will be bold."}
  #!componentProp(m3.Link)!1: {name:"underline",type:"boolean",description:"If True, this component’s text will be underlined."}
  #!componentProp(m3.Link)!1: {name:"font_family",type:"string",description:"The font family to use for this component."}
  #!componentProp(m3.Link)!1: {name:"font_size",type:"number",description:"The font size of text displayed on this component."}
  #!componentProp(m3.Link)!1: {name:"icon",type:"enum",description:"The icon to display on this component."}
  #!componentProp(m3.Link)!1: {name:"visible",type:"boolean",description:"If True, the component will be displayed."}
  #!componentProp(m3.Link)!1: {name:"text_color",type:"color",description:"The color of the text on the component."}
  #!componentProp(m3.Link)!1: {name:"icon_color",type:"color",description:"The color of the icon displayed on this component."}
  #!componentProp(m3.Link)!1: {name:"border",type:"string",description:"The border of this component. Can take any valid CSS border value."}
  #!componentProp(m3.Link)!1: {name:"spacing",type:"spacing",description:"The margin and padding (pixels) of the component."}
  #!componentProp(m3.Link)!1: {name:"tooltip",type:"string",description:"The text to display when the mouse is hovered over this component."}
  #!componentProp(m3.Link)!1: {name:"role",type:"themeRole",description:"A style for this component defined in CSS and added to Roles."}
  #!componentProp(m3.Link)!1: {name:"url",type:"string",description:"TThe target URL of the link. Can be set to a URL string or to a Media object."}
  #!componentProp(m3.Link)!1: {name:"icon_size",type:"number",description:"The size (pixels) of the icon displayed on this component."}
  #!componentProp(m3.Link)!1: {name:"tag",type:"object",description:"Use this property to store any extra data for the component."}
  #!componentProp(m3.Link)!1: {name:"background_color",type:"color",description:"The color of the background of this component."}

  italic = italic_property('anvil-m3-link-text')
  bold = bold_property('anvil-m3-link')
  font_family = font_family_property('anvil-m3-link', 'font_family')
  font_size = font_size_property('anvil-m3-link')
  underline = underline_property('anvil-m3-link-text')
  visible = anvil.HtmlTemplate.visible
  text_color = color_property('anvil-m3-link', 'color', 'text_color')
  icon_color = color_property('anvil-m3-link-icon', 'color', 'icon_color')
  border = style_property('anvil-m3-link', 'border', 'border')
  spacing = spacing_property('anvil-m3-link')
  tooltip = tooltip_property('anvil-m3-link')
  role = role_property('anvil-m3-link')
  background_color = color_property(
    'anvil-m3-link', 'backgroundColor', 'background_color'
  )

  @anvil_prop(default_value='left')
  def align(self, value):
    self.dom_nodes['anvil-m3-link'].style.textAlign = value
    self.dom_nodes['anvil-m3-link-icon-container'].style.justifyContent = value

  @anvil_prop
  def url(self, value):
    self.dom_nodes['anvil-m3-link'].removeAttribute("download")
    self.dom_nodes['anvil-m3-link'].removeAttribute("target")
    self._revoke_tmp_url()
    if value:
      if isinstance(value, anvil.Media):
        if value.name:
          self.dom_nodes['anvil-m3-link'].setAttribute("download", value.name)
        self.temp_url = anvil.media.TempUrl(value)
        self.dom_nodes['anvil-m3-link'].href = self.temp_url.url
      else:
        self.dom_nodes['anvil-m3-link'].href = value
        self.dom_nodes['anvil-m3-link'].setAttribute("target", "_blank")
    else:
      self.dom_nodes['anvil-m3-link'].href = 'javascript:void(0)'

  @anvil_prop
  def icon_size(self, value):
    if value:
      value = f'{value}px'
    self.dom_nodes['anvil-m3-link-icon'].style.fontSize = value

  @anvil_prop
  def icon(self, value):
    if value and self.text:
      self.dom_nodes['anvil-m3-link-icon'].style.marginRight = "8px"
    else:
      self.dom_nodes['anvil-m3-link-icon'].style.marginRight = ""
    self.dom_nodes['anvil-m3-link-icon'].innerText = value[3:]

  @anvil_prop
  def text(self, value):
    self.dom_nodes['anvil-m3-link-text'].innerText = value
    if value:
      self.dom_nodes['anvil-m3-link-text'].style.display = 'block'
    else:
      self.dom_nodes['anvil-m3-link-text'].style.display = 'none'


#!defClass(m3, Link, anvil.Component)!:
