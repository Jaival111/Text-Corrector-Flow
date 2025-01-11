from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('MIRA_API_KEY')

client = MiraClient(config={"API_KEY":api_key})

version = "1.0.0"
input_dict = {'context':'professional', 'text':"Yo, I'm tryna snag a day off this Monday—think you could approve my leave?"}

if version:
    flow_name = f"jaival175/text-corrector/{version}"
else:
    flow_name = "jaival175/text-corrector"

result = client.flow.execute(flow_name, input_dict)
print(result)