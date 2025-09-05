import json
from openai import OpenAI


with open("t2t_secret.json", "r") as secretFile:
  secret = json.load(secretFile)
  key = secret["openai_api_key"]

apiRef = OpenAI(
  api_key = key
)

with open("lore.txt", "r", encoding="utf-8") as f: lore = f.read()

conversation = [{"role": "system", "content": lore}]

userRequest = ""

regularModel = "gpt-4o-mini"
fineTunedModel = "ft:gpt-4o-mini-2024-07-18:fyrnsfaeryland:vervada-test:BRZ0XGrT"

def getCompletion():
  return apiRef.chat.completions.create(
    model=regularModel,
    store=True,
    messages=[
      {
        "role": "developer",
        "content": [
          {
            "type": "text",
            "text": lore
          }
        ]
      },
      {
        "role": "user",
        "content": userRequest
      }
    ]
  ).choices[0].message.content