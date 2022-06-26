from neuralintents import GenericAssistant
from assistant import mappings


assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()
assistant.save_model()
