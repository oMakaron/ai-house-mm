import anthropic
import helper

def profileAI(client: anthropic.Anthropic, history: list):
    prompt = input()
    history.append({'role': 'user', 'content': prompt})
    response = client.messages.create(model="claude-sonnet-4-20250514",
                                      max_tokens=1000,
                                      messages=history)
    history.append({"role": "assistant", "content": response.content[0].text})
    print(response.content[0].text)
    if ('{' in response.content[0].text):
        return False
    return True

def profileMain():
    client = helper.get_anthropic()
    history = [{'role': 'user',
                'content': 'You are a friendly pal trying to help me as a user to register an account for Perth house finder app. '
                'You will need information such as my name, date of birth, phone number, email, occupation, current suburb, about myself, and my preferences for a place to stay. '
                'You will need to gather all necessary information before giving a plain JSON-like response with the format: \n'
                '{{"name": (my name), "dob": (my birthdate), "phone": (my number), "email": (my email), "job": (my occupation), "suburb": (my suburb) "about": (about myself), "prefer": (my house preferences)}}\n'
                'change all brackets with a string of answers you get from my answers to your questions. '
                'for the about myself part, summarize it to be less than 50 words if it exceeds 50 words. '
                'for the birthdate make it in the format of DD/MM/YYYY. '
                'the phone number is in the string with format of numbers with no spaces in between them. '
                'make sure when all of the information is completed and you are going to give the JSON response, dont give any comments! just give a raw JSON format. '
                'also translate all non english response like in occupation and about myself into english if the user decided to use another language than english' 
                'Now you can start by introducing yourself and ask the prefered language and ask my identity with the prefered language'}]
    
    response = client.messages.create(model="claude-sonnet-4-20250514",
                                      max_tokens=1000,
                                      messages=history)
    history.append({"role": "assistant", "content": response.content[0].text})
    print(response.content[0].text)
    flag = True
    while(flag):
        flag = profileAI(client, history)
    
    curlStart = history[-1]['content'].find('{')
    curlEnd = history[-1]['content'].find('}')
    return history[-1]['content'][curlStart:curlEnd + 1]

if __name__ == '__main__':
    json = profileMain()
    
