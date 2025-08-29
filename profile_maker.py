import anthropic

def profileAI(client: anthropic.Anthropic, history: list):
    prompt = input()
    history.append({'role': 'user', 'content': prompt})
    response = client.messages.create(model="claude-sonnet-4-20250514",
                                      max_tokens=1000,
                                      messages=history)
    history.append({"role": "assistant", "content": response.content[0].text})
    print(response.content[0].text)

def main():
    key = 'your key here'
    client = anthropic.Anthropic(api_key=key)
    history = [{'role': 'user',
                'content': 'You are a friendly pal trying to help me as a user to register an account for Perth house finder app. '
                'You will need information such as my name, date of birth, phone number, email, occupation, and about myself. '
                'You will need to gather all necessary information before giving a plain JSON-like response with the format: \n'
                '{{"name": (my name), "dob": (my birthdate), "phone": (my number), "email": (my email), "job": (my occupation), "about": (about myself)}}\n'
                'change all brackets with a string of answers you get from my answers to your questions. '
                'for the about myself part, summarize it to be less than 50 words if it exceeds 50 words. '
                'Now you can start by introducing yourself and ask the first question about my name'}]
    
    response = client.messages.create(model="claude-sonnet-4-20250514",
                                      max_tokens=1000,
                                      messages=history)
    history.append({"role": "assistant", "content": response.content[0].text})
    print(response.content[0].text)
    while(True):
        profileAI()

if __name__ == '__main__':
    main()
    
