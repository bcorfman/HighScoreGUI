from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_entries()

  def add_entry_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_entry = {}
    # Open an alert displaying the 'EntryEdit' Form
    save_clicked = alert(
      content=EntryEdit(item=new_entry),
      title="Add High Score",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      anvil.server.call(f'add_score?initials={initials}&score={score}', new_entry)
      self.refresh_entries()
    
  def refresh_entries(self):
     # Load existing entries from the Data Table, 
     # and display them in the RepeatingPanel
     json = anvil.server.call('get_high_scores')
     self.panel.items = json
    

