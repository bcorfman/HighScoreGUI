import anvil.http
import anvil.server

HIGHSCORE_SERVICE = "https://highscore-ibq0itxr.b4a.run"

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
