import asyncio
import time

from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string


class Model:

    def __init__(self, model_path=r"./models/20220418-210445-burning-borzoi.tar.gz") -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")

    def message(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        return json_to_string(result)

    def run(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.handle_text(message))
        return result


if __name__ == "__main__":
    bot = Model()
    start = time.time()
    res = bot.run("Hello")
    print(time.time() - start)
