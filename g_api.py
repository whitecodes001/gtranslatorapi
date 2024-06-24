import requests



def translate(text, target_language, source_language):
    url = "https://translate.googleapis.com/translate_a/single"

    params = {
        "client": "gtx",
        "sl": source_language,
        "tl": target_language,
        "dt": "t",
        "q": text
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_json = response.json()

        translated_text = response_json[0][0][0] if response_json and response_json[0] and response_json[0][0] else None
        return translated_text

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None