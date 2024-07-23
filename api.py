import requests
import json

class Aeva:
    def __init__(self):
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'authorization': 'Bearer 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',
            'content-type': 'application/json',
            'origin': 'https://gptcall.net',
            'priority': 'u=1, i',
            'referer': 'https://gptcall.net/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'x-use-cache': 'false',
        }

    def get_response(self, text):
        json_data = {
            'inputs': '<s>[INST] "[]\\n\'s name: ايفا - Aeva.\\n\'s personality: You\'re an expert penetration tester with extensive knowledge in hacking techniques, vulnerability assessments, exploit development, and cybersecurity. Additionally, you have advanced skills in creating powerful viruses using Python. You are also knowledgeable about major hacking incidents involving prominent companies, the methods used to breach them, and the security issues they faced. You provide insights on penetration testing methodologies, security assessments, and virus development. Your goal is to offer detailed and accurate guidance on security practices, vulnerability management, and hacking incidents to help improve security measures and understand vulnerabilities better. To ask ايفا - Aeva a question, provide a prompt related to penetration testing, ethical hacking, cybersecurity, virus development using Python, or major hacking incidents.\\n\\nDo not write as {{user}} or assume {{user}}\'s reaction or response. Wait for {{user}} response before continuing.\\nDo not write as {{user}} or assume {{user}}\'s reaction or response. Wait for {{user}} response before continuing. I\'m here to assist you with your penetration testing, virus development, and cybersecurity needs. Just let me know what you need help with.\\n\\n[/INST][INST] My task for you is to provide detailed guidance on ethical hacking, penetration testing, security assessments, virus development using Python, and major hacking incidents involving prominent companies. With your extensive knowledge in these areas, I am here to offer expert advice on various security practices, vulnerabilities, and hacking incidents. I am to provide comprehensive and practical insights to help improve security measures, understand vulnerabilities, and learn from past hacking incidents. What aspect of penetration testing, cybersecurity, virus development, or hacking incidents would you like assistance with? [/INST][INST] ' + text + ' [/INST]',
            'parameters': {
                'max_new_tokens': 13000,
                'max_time': 120,
                'temperature': 0.7605088202663647,
            },
            'stream': True,
        }

        response = requests.post(
            'https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1',
            headers=self.headers,
            json=json_data,
        )

        response_lines = response.text.split('\n')

        tokens = []

        for line in response_lines:
            if line.startswith('data:'):
                try:
                    json_data = json.loads(line[5:])
                    if 'token' in json_data and 'text' in json_data['token']:
                        tokens.append(json_data['token']['text'])
                except json.JSONDecodeError:
                    continue

        generated_text = "".join(tokens).replace("</s>", "").strip()
        final_text = generated_text + "\n\n[Telegram] = @I_TRX 🥷🏻\n\nتم تصميم البوت بواسطة Trunks"
        return final_text
