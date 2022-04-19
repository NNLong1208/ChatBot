import asyncio
import time

from rasa.core.agent import Agent


class Model:

    def __init__(self, model_path=r"./models/20220418-210445-burning-borzoi.tar.gz") -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")

    def predict(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        return result

    def run(self, message: str) -> str:
        message = message.strip()
        results = asyncio.run(self.agent.handle_text(message))
        output = self.predict(message)
        print(output)
        for result in results:
            result['text'] = self.format_output(result['text'], output)
        return results

    @staticmethod
    def format_output(text, output):
        if output['intent']['name'] == 'ask_product':
            for entity in output['entities']:
                text = text.replace(entity['entity'], entity['value'])
        return text


if __name__ == "__main__":
    bot = Model()
    while True:
        text = input()
        start = time.time()
        res = bot.run(text)
        print(res)
        print(time.time() - start)
