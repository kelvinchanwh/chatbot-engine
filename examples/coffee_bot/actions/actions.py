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
    dispatcher.utter_template("utter_welcome", tracker)
    return []

class ActionDefaultFallback(Action):
  def name(self):
    return "action_default_fallback"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_default_fallback", tracker)
    return []


class ActionCheerUp(Action):
  def name(self):
    return "action_cheer_up"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_cheer_up", tracker)
    dispatcher.utter_template("utter_did_that_help", tracker)
    return []


class ActionCoffee(Action):
  def name(self):
    return "action_coffee"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template("utter_coffee", tracker)
    dispatcher.utter_template("utter_which_coffee", tracker)
    return []


class ActionConfirmCoffee(Action):
  def name(self):
    return "action_confirm_coffee"

  def run(self, dispatcher, tracker, domain):
    coffee_type = tracker.get_slot('coffee_type')
    if not coffee_type:
      dispatcher.utter_template("utter_uknown_coffee_type", tracker)
      dispatcher.utter_template("utter_try_again", tracker)
    else:
      dispatcher.utter_template("utter_enjoy_your_drink", tracker)
    return []
