import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#ttt
@anvil.server.callable
def get_jobs():
  rows = app_tables.jobs.search()
  return {
    'items': [(row['Titles'], row) for row in rows],
    'selected': rows[1]
  }