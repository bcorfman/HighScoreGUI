from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server
from ..EntryEdit import EntryEdit

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
]    # Any code you write here will run when the form opens.
    self.refresh_entries()

  def add_entry_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_entry = {}
    # Open an alert displaying the 'EntryEdit' Form
    #save_clicked = alert(
    #  content=EntryEdit(item=new_entry),
    #  title="Add Entry",
    #  large=True,
    #  buttons=[("Save", True), ("Cancel", False)]
    #)
    # If the alert returned 'True', the save button was clicked.
    #if save_clicked:
    #  anvil.server.call('add_entry', new_entry)
    #  self.refresh_entries()
    
  def refresh_entries(self):
     # Load existing entries from the Data Table, 
     # and display them in the RepeatingPanel
     json = anvil.server.call('get_high_scores')
     self.entries_panel.items = json
     for elem in self.entries_panel.items:
       elem.


