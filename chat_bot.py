import asyncio
import time
import json
import random
from rasa.core.agent import Agent


class Model:

    def __init__(self, model_path=r"./models/20220418-210445-burning-borzoi.tar.gz") -> None:
        self.agent = Agent.load(model_path)
        f = open('./config.json', encoding='utf-8')
        self.config = json.load(f)
        print("NLU model loaded")

    def predict(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        return result

    def run(self, message: str) -> str:
        message = message.strip()
        results = asyncio.run(self.agent.handle_text(message))
        output = self.predict(message)
        for result in results:
            result['text'] = self.format_output(result['text'], output)
        return results

    def format_output(self, text, output):
        keys = list(self.config)
        keys.remove('domain')
        if output['intent']['name'] == 'ask_product':
            for entity in output['entities']:
                text = text.replace(entity['entity'], entity['value'])
            # for key in keys:
            #     text = text.replace(key, self.config['domain'] + self.config[key])
            # if "<brand/product>" in text:
            #     text = "Xin lỗi bạn, mình không tìm thấy sản phẩm. Mình giới thiệu bạn sản phẩm này nè{}".format( self.config['domain'] + self.config[random.choice(keys)])
            try:
                start = text.index("<")
                end = text.index(">")
                key = text[start:end+1]
                text = text.replace(key, self.config['domain'] + self.config[key])
            except Exception:
                text = "Xin lỗi bạn, mình không tìm thấy sản phẩm. Mình giới thiệu bạn sản phẩm này nè {}".format(self.config['domain'] + self.config[random.choice(keys)])
            text = text.replace("<", "")
            text = text.replace(">", "")
        return text


if __name__ == "__main__":
    bot = Model()
    while True:
        text = input()
        start = time.time()
        res = bot.run(text)
        print(res)
        print(time.time() - start)
