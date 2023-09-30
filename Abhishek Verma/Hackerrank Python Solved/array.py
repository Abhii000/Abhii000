
import openai
import os
import sys
import time
while True:
    print('-'*30)
    abhii_input=str(input('Type = '))

    print('Let me think...\n\n')
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Q:"+abhii_input+"\nA:",
        temperature=0.9,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,

    )
    print(response.choices[0]['text'])



