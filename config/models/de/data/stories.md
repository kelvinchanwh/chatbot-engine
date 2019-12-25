## chatbot intro
* bot_welcome
  - action_welcome

## neutral
* greet
- utter_greet

## happy path
* mood_great
  - utter_happy

## sad path 1
* mood_unhappy
  - action_joke
* affirm
  - utter_happy

## sad path 2
* mood_unhappy
  - action_cheer_up
> check_asked_question

## user affirms question
> check_asked_question
* affirm
  - utter_happy

## user denies question
> check_asked_question
* deny
  - utter_advice
  - action_joke

## say goodbye
* goodbye
  - utter_goodbye

## request for coffee
* coffee
  - action_coffee

## offer coffee
* coffee_type
  - action_confirm_coffee

## approval
* opinion+positive
  - utter_positive_feedback_reaction  

## rejection
* opinion+negative
  - utter_negative_feedback_reaction  

## acknowledge
* acknowledge
  - utter_positive_feedback_reaction

## affirm
* affirm
  - utter_positive_feedback_reaction

## fallback story
* out_of_scope
  - action_default_fallback

## Generated Story 7713572701080784553
* coffee
    - action_coffee
* coffee_type{"coffee_type": "americano"}
    - slot{"coffee_type": "americano"}
    - action_confirm_coffee
* opinion+positive
    - utter_positive_feedback_reaction
