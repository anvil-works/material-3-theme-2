from ._anvil_designer import StandardPageLayoutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Functions import innerText_property
from anvil.js import window



class StandardPageLayout(StandardPageLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.app_bar = self.dom_nodes['anvil-m3-top-app-bar']
    self.nav_drawer_open_btn = self.dom_nodes['anvil-m3-drawer-open-btn']
    self.nav_drawer_close_btn = self.dom_nodes['anvil-m3-drawer-close-btn']
    self.nav_rail = self.dom_nodes['anvil-m3-navigation-rail']
    self.nav_drawer_scrim = self.dom_nodes['anvil-m3-navigation-drawer-scrim']

    window.document.addEventListener('scroll', self.add_scroll_class)
    self.nav_drawer_open_btn.addEventListener('click', self.open_nav_drawer)
    self.nav_drawer_close_btn.addEventListener('click', self.hide_nav_drawer)
    self.nav_drawer_scrim.addEventListener('click', self.hide_nav_drawer)

  def open_nav_drawer(self, e):
    self.nav_rail.style.width = '360px'
    self.nav_rail.style.left = "0px"
    self.nav_rail.classList.add('anvil-m3-shown')
    self.nav_drawer_scrim.animate([{'opacity': '0'},{'opacity': '1'}], {'duration': 250, 'iterations': 1})

  def hide_nav_drawer(self, e):
    self.nav_rail.style.left = "-101%"
    self.nav_drawer_scrim.animate([{'opacity': '1'},{'opacity': '0'}], {'duration': 250, 'iterations': 1})
    window.setTimeout(lambda: self.nav_rail.style.setProperty('width', '0px'), 250)
    window.setTimeout(lambda: self.nav_rail.classList.remove('anvil-m3-shown'), 245)

        
  def add_scroll_class(self, e):
    if self.app_bar.classList.contains('anvil-m3-scrolled'):
      if window.scrollY == 0:
        self.app_bar.classList.remove('anvil-m3-scrolled')
    else:
      self.app_bar.classList.add('anvil-m3-scrolled')    
  
  @property
  def navigation_rail_collapse_to(self):
    return self._navigation_rail_collapse_to

  @navigation_rail_collapse_to.setter
  def navigation_rail_collapse_to(self, value):
    self._navigation_rail_collapse_to = value
    value = value.lower().replace(' ', '-')
    self.dom_nodes['anvil-m3-navigation-rail'].className = "anvil-m3-navigation-rail"
    self.dom_nodes['anvil-m3-navigation-rail'].classList.add(f"anvil-m3-{value}")
    #todo: remove the below?
    self.dom_nodes['anvil-m3-content'].className = "anvil-m3-content"
    self.dom_nodes['anvil-m3-content'].classList.add(f"anvil-m3-{value}")


