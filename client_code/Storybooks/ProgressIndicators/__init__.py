from ._anvil_designer import ProgressIndicatorsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time

class ProgressIndicators(ProgressIndicatorsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    self.circular_progress_indicator_determinate.progress = 0
    self.linear_progress_indicator_determinate.progress = 0
    self.change_progress()
    
  def change_progress(self):
    start_time = time.time()
    end_time = start_time + 20  # 20 seconds timer

    while time.time() < end_time and self.circular_progress_indicator_determinate.progress <= 100:
        self.circular_progress_indicator_determinate.progress += 10
        self.linear_progress_indicator_determinate.progress += 10
        time.sleep(0.1)  # Adjust the sleep time to change the speed of counting

    
    