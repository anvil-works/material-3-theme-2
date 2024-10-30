from anvil.designer import in_designer, register_interaction
from anvil.js import window

from ..._utils.properties import (
  anvil_prop,
  color_property,
  padding_property,
  theme_color_to_css,
)
from ._anvil_designer import NavigationDrawerLayoutTemplate


class NavigationDrawerLayout(NavigationDrawerLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties

    self.nav_drawer = self.dom_nodes["anvil-m3-navigation-drawer"]
    self.nav_drawer_open_btn = self.dom_nodes["anvil-m3-drawer-open-btn"]
    self.nav_drawer_scrim = self.dom_nodes["anvil-m3-navigation-drawer-scrim"]
    self.app_bar = self.dom_nodes["anvil-m3-top-app-bar"]
    self.sidesheet_scrim = self.dom_nodes["anvil-m3-sidesheet-scrim"]
    self.sidesheet = self.dom_nodes["anvil-m3-sidesheet"]
    self.content = self.dom_nodes["anvil-m3-content"]
    self.sidesheet_previous_state = False
    self.init_components(**properties)

    window.document.addEventListener("scroll", self._on_scroll)
    self.nav_drawer_open_btn.addEventListener("click", self._open_nav_drawer)
    self.nav_drawer_scrim.addEventListener("click", self._hide_nav_drawer)

    if in_designer:
      register_interaction(self, self.nav_drawer, "dblclick", self._toggle_nav_drawer)

  def _toggle_nav_drawer(self):
    if self._is_nav_drawer_open():
      self._hide_nav_drawer()
    else:
      self._open_nav_drawer()

  def _anvil_get_interactions_(self):
    return [
      {
        "type": "region",
        "bounds": self.nav_drawer,
        "sensitivity": 2,
        "callback": self._toggle_nav_drawer,
      }
    ]

  def _open_nav_drawer(self, e):
    self.nav_drawer.style.width = "360px"
    self.nav_drawer.style.left = "0px"
    self.nav_drawer.classList.add("anvil-m3-shown")
    self.nav_drawer_scrim.animate(
      [{"opacity": "0"}, {"opacity": "1"}], {"duration": 250, "iterations": 1}
    )

  def _hide_nav_drawer(self, e):
    self.nav_drawer.style.left = "-101%"
    self.nav_drawer_scrim.animate(
      [{"opacity": "1"}, {"opacity": "0"}], {"duration": 250, "iterations": 1}
    )
    window.setTimeout(lambda: self.nav_drawer.style.setProperty("width", "0px"), 250)
    window.setTimeout(lambda: self.nav_drawer.classList.remove("anvil-m3-shown"), 245)

  def _on_scroll(self, e):
    if window.scrollY == 0:
      self.app_bar.classList.remove("anvil-m3-scrolled")
    else:
      self.app_bar.classList.add("anvil-m3-scrolled")

  def _open_sidesheet(self):
    if self.sidesheet_previous_state:
      self.sidesheet.classList.add("anvil-m3-display-block")
      window.setTimeout(lambda: self.sidesheet.classList.add("anvil-m3-open"), 1)
      self.sidesheet_scrim.classList.add("anvil-m3-sidesheet-open")
      self.content.classList.add("anvil-m3-transition-width")
      window.setTimeout(
        lambda: self.content.classList.add("anvil-m3-sidesheet-open"), 5
      )
      self.sidesheet_scrim.animate(
        [{"opacity": "0"}, {"opacity": "1"}], {"duration": 250, "iterations": 1}
      )
    else:
      self.sidesheet_scrim.classList.add("anvil-m3-sidesheet-open")
      self.sidesheet_scrim.style.opacity = 1
      self.sidesheet.classList.add("anvil-m3-display-block")
      self.sidesheet.classList.add("anvil-m3-open")
      self.content.classList.add("anvil-m3-sidesheet-open")
      self.sidesheet_previous_state = True

  def _close_sidesheet(self):
    self.content.classList.add("anvil-m3-transition-width")
    self.sidesheet_scrim.animate(
      [{"opacity": "1"}, {"opacity": "0"}], {"duration": 250, "iterations": 1}
    )
    window.setTimeout(
      lambda: self.sidesheet_scrim.classList.remove("anvil-m3-sidesheet-open"), 245
    )
    self.sidesheet.classList.remove("anvil-m3-open")
    self.content.classList.remove("anvil-m3-sidesheet-open")
    window.setTimeout(
      lambda: self.content.classList.remove("anvil-m3-sidesheet-open"), 245
    )
    window.setTimeout(
      lambda: self.sidesheet.classList.remove("anvil-m3-display-block"), 245
    )

  def _is_nav_drawer_open(self):
    return self.nav_drawer.classList.contains("anvil-m3-shown")

  #!componentEvent(m3.NavigationDrawerLayout)!1: {name: "show", description: "When the Form is shown on the screen."}
  #!componentEvent(m3.NavigationDrawerLayout)!1: {name: "hide", description: "When the Form is removed from the screen."}
  #!componentEvent(m3.NavigationDrawerLayout)!1: {name: "refreshing_data_bindings", description: "When refresh_data_bindings is called."}

  #!componentProp(m3.NavigationDrawerLayout)!1: {name:"navigation_drawer_color",type:"color",description:"The color of the navigation drawer on Forms using this Layout."}
  #!componentProp(m3.NavigationDrawerLayout)!1: {name:"background_color",type:"color",description:"The background color of Forms using this Layout."}
  #!componentProp(m3.NavigationDrawerLayout)!1: {name:"text_color",type:"color",description:"The default color of the text on Forms using this Layout."}
  #!componentProp(m3.NavigationDrawerLayout)!1: {name:"show_sidesheet",type:"boolean",description:"If True, the sidesheet will be shown on Forms using this Layout."}
  #!componentProp(m3.NavigationDrawerLayout)!1: {name:"content_padding",type:"padding",description:"The padding (pixels) around the content of the page."}

  navigation_drawer_color = color_property(
    "anvil-m3-navigation-drawer", "backgroundColor", "navigation_drawer_color"
  )

  @anvil_prop
  def background_color(self, value):
    if value:
      value = theme_color_to_css(value)
    window.document.body.style.backgroundColor = value

  @anvil_prop
  def text_color(self, value):
    if value:
      value = theme_color_to_css(value)
    window.document.body.style.color = value

  @property
  def show_sidesheet(self):
    return self._show_sidesheet

  @show_sidesheet.setter
  def show_sidesheet(self, value):
    self._show_sidesheet = value
    if value:
      self._open_sidesheet()
    else:
      self._close_sidesheet()

  content_padding = padding_property("anvil-m3-content")


#!defClass(m3, NavigationDrawerLayout, anvil.Component)!:
