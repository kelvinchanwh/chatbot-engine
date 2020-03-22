import requests
from rasa_sdk import Action


class ActionJoke(Action):
  def name(self):
    return "action_joke"

  def run(self, dispatcher, tracker, domain):
    request = requests.get('http://api.icndb.com/jokes/random').json()  # make an api call
    joke = request['value']['joke']  # extract a joke from returned json response
    dispatcher.utter_message(joke)  # send the message back to the user
    return []


class ActionWelcome(Action):
  def name(self):
    return "action_welcome"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message(template="utter_welcome")
    return []

class ActionDefaultFallback(Action):
  def name(self):
    return "action_default_fallback"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message(template="utter_default_fallback")
    return []


class ActionCheerUp(Action):
  def name(self):
    return "action_cheer_up"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message(template="utter_cheer_up")
    dispatcher.utter_message(template="utter_did_that_help")
    return []


class ActionCoffee(Action):
  def name(self):
    return "action_coffee"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message(template="utter_coffee")
    dispatcher.utter_message(template="utter_which_coffee")
    return []


class ActionConfirmCoffee(Action):
  def name(self):
    return "action_confirm_coffee"

  def run(self, dispatcher, tracker, domain):
    coffee_type = tracker.get_slot('coffee_type')
    if not coffee_type:
      dispatcher.utter_message(template="utter_uknown_coffee_type")
      dispatcher.utter_message(template="utter_try_again")
    else:
      dispatcher.utter_message(template="utter_enjoy_your_drink")
    return []
