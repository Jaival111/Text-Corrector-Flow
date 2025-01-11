from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('MIRA_API_KEY')

client = MiraClient(config={"API_KEY":api_key})

flow = Flow(source='flow.yaml')

input_dict = {'context':'professional', 'text':"Yo, I'm tryna snag a day off this Monday—think you could approve my leave?"}

response = client.flow.test(flow, input_dict)

print(response)