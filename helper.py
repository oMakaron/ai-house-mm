import json
import anthropic

def dictify(jsonStr: str) -> dict:
    return json.loads(jsonStr)

def get_anthropic() -> anthropic.Anthropic:
    key = 'your api key'
    client = anthropic.Anthropic(api_key=key)
    return client