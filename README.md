# Chatbot Engine

This is a demo of a multi-lingual chatbot powered by [Rasa](https://rasa.com/). 
The entire app runs on a single web server, which makes it easy to deploy and maintain it at low cost.

The demo runs on Heroku, feel free to [try it out](https://chatbot-engine-web.herokuapp.com/)!

## Features
- Supports multiple models and languages
- Easy to spin up (Docker) and deploy (automated CI)  
- Makes it easy to build your own model (training, interactive learning, custom actions)
- Continuously updated to run on the latest Rasa stack 

## How to ..

### Start it on your local machine
`docker-compose up`

Please note it might take longer the first time for the server to start. There are many dependencies that need to be downloaded. Subsequent starts are gonna be quick though.

### Train your model
`./server.sh train [en|de]`

The script process training data stored in `config/models` and stores the output in the `models` directory.

Currently, only two languages are supported, but it's easy to completely change them or add more.
In fact, given the simplicity of the model in the demo, it can be trained for any language you like.
It makes use of [supervised embeddings](https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/#supervised-embeddings).
Anyway, feel free to completely change the pipeline as you please. [Rasa docs](https://rasa.com/docs/rasa/nlu/choosing-a-pipeline) are your best friend.

### Add a custom action
Either amend the [actions.py](actions/actions.py) script or drop a new script to the [actions](actions) module.

### Write your model from scratch
Drop a new model config in the [models](config/models) directory. Have a look at the existing examples.

## Architecture

Rasa provides a lot of convenience. It's easy to start the core as well as the action server. Running multiple web servers can however be a problem when it comes to hosting.
Multiple web processes or communication via HTTP in a Heroku cluster is only allowed with pricier plans.

Another issue is the lack of support for multiple models in the current version of Rasa (1.3.0). Suppose you train your bot in two languages. As it stands now, you need to spin up an additional core server to serve your other model.
With a little bit of an extra effort, it is perfectly possible to enable multiple models with Rasa's SDK. Check my [BotFactory](utils/bot_factory.py) if you are interested in details.

## Attribution
- [Rasa](https://rasa.com) for providing such an awesome framework.
- 