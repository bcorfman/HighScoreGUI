import anvil.http
import anvil.server

HIGHSCORE_SERVICE = "https://https://highscore1-1y492j9s.b4a.run"

@anvil.server.callable
def add_score(initials, score):
  result = anvil.http.request(HIGHSCORE_SERVICE + f'/add_score?initials={initials}&score={score}', 'POST')
  return result

@anvil.server.callable
def get_high_scores():
  result = anvil.http.request(HIGHSCORE_SERVICE + '/high_scores', json=True)
  return result
  
@anvil.server.callable
def clear_high_scores():
  result = anvil.http.request(HIGHSCORE_SERVICE + '/clear_scores', 'POST')
  return result
