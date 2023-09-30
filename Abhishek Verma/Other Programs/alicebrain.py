import os
import openai,time
empty_que=''
empty_ans=''

def autosave():
  f = open("alicedata.txt", "a")
  for null_void in range(2):
    f.write('\n')

  f.write('Question:-   ')
  f.write(empty_que)

  for null_void1 in range(2):
    f.write('\n')
    time.sleep(0.01)
  f.write('Answers:-')

  for null_void2 in range(2):
    f.write('\n')
    time.sleep(0.01)
  f.write(empty_ans)
  f.write('\n')
  f.write('----------------------------------------------------------------------------------------------')


  f.close()
  time.sleep(0.5)
  
while True:
  print('\n')
  abhii_input=str(input('Listening...'))

  if abhii_input=='close':
      break

  else:
     
     
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Q:"+abhii_input+"\nA:",
      temperature=1,
      max_tokens=2000,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["A:"]
    )

    variable_x=response['choices'][0]['text']
    empty_ans=variable_x
    empty_que=abhii_input
    #print('\n\n',variable_x)


    text_lines=variable_x.splitlines()
  
    for variable1 in range(0,len(text_lines)):
      print(text_lines[variable1])
      time.sleep(0.1)

    autosave()



#print(response["choices"]["text"])

#print(response['choices'])