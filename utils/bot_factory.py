import logging
import uuid
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from collections.abc import Mapping

logger = logging.getLogger(__name__)

DEFAULT_LANG = 'en'

SUPPORTED_LANGS = {
    DEFAULT_LANG: 'english',
    'de': 'german'
}


class LazyDict(Mapping):
    def __init__(self, *args, **kw):
        self._raw_dict = dict(*args, **kw)

    def __getitem__(self, key):
        value = self._raw_dict.__getitem__(key)
        if isinstance(value, tuple):
            func, arg = value
            result = func(arg)
            self._raw_dict.__setitem__(key, result)
            return result
        else:
            return value

    def __iter__(self):
        return iter(self._raw_dict)

    def __len__(self):
        return len(self._raw_dict)


class BotFactory:

    __instance = None

    def __init__(self):
        if BotFactory.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BotFactory.__instance = self
            bots_dict = dict((k, (self.__createInstance, k)) for k in SUPPORTED_LANGS.keys())
            self.dict = LazyDict(bots_dict)

    @staticmethod
    def getInstance(lang):
        if BotFactory.__instance == None:
            BotFactory()
        return BotFactory.__instance.dict[lang]

    def __createInstance(self, lang):
        if not lang in SUPPORTED_LANGS:
            logger.warn(f'Unsupported language: ${lang}. The default will be used: ${DEFAULT_LANG}')

        chatbot = ChatBot(uuid.uuid4().hex)

        # Create a new trainer for the chatbot
        trainer = ChatterBotCorpusTrainer(chatbot)

        # Train the chatbot based on the english corpus
        selected_lang = SUPPORTED_LANGS.get(lang, DEFAULT_LANG)
        trainer.train(f'chatterbot.corpus.{selected_lang}')

        return chatbot
