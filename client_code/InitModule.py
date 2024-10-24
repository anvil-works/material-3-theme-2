import anvil.pluggable_ui
from .._Components.Button import Button

anvil.pluggable_ui.provide("m3", {
  "anvil.TextB"
  "anvil.Button": Button,
})



print('hello world')

