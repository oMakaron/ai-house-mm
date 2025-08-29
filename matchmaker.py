import pandas as pd
import helper
import anthropic

def MMmain(user_info: dict):
    client = helper.get_anthropic()
    housedf = pd.read_csv('housemock.csv')
    housedfstr = housedf.to_string(index=False)
    prompt = f"""
    Here is a dataset of house listings:
    
    {housedfstr}
    
    User Data: {user_info}
    
    Please analyze the listings and recommend the top 5 houses that best match the user's preferences. 
    For each recommendation, explain why it's a good match and provide the key details.
    Format your response into a list of JSON type format such as that it looks like:
    [{{"ID": (listing ID 1), "reason": (your reccomendation reason}}, {{"ID": (listing ID 2), "reason": (your reccomendation reason}}, {{"ID": (listing ID 3), "reason": (your reccomendation reason}}, {{"ID": (listing ID 4), "reason": (your reccomendation reason}}, {{"ID": (listing ID 5), "reason": (your reccomendation reason}}].
    """
    response = client.messages.create(model="claude-sonnet-4-20250514",
                                      max_tokens=1000,
                                      messages=[{"role": "user", "content": prompt}])

    return response.content[0].text

if __name__ == '__main__':
    res = MMmain({"name": "Nick Polish", "dob": "24/11/2000", "phone": "0416305461", "email": "nick@gmail.com", "job": "student", "suburb": "Crawley", "about": "I am a sociable student looking for a house", 'prefer': 'I would like a place to live near my campus at UWA, ideally I would not need to waste more than 1 hour on travel time'})
    print(res)