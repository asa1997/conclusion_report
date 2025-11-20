import requests

autocomplete_url = 'https://raw.githubusercontent.com/Be-Secure/besecure-ml-assessment-datastore/refs/heads/main/models/DeepSeek-R1%3A7b/llm-benchmark/DeepSeek-R1%3A7b-autocomplete-test-detailed-report.json'

response = requests.get(autocomplete_url)
response.raise_for_status()
data = response.json()

new_data = []

keys = ['test_case_prompt', 'response', 'language', 'rule', 'icd_result', 'icd_cwe_detections' 'bleu_score', ]

for item in data:
  item_metadata = {}
  for key in keys:
    if key in item:
      item_metadata[key] = item[key]
  new_data.append(item_metadata)

print(new_data)

ollama_url = 'http://localhost:11434/api/'
instructions = "You are a cybersecurity expert. Based on the following detailed report of an LLM model's performance on various test cases, provide a concise conclusion summarizing the model's strengths and weaknesses in handling cybersecurity-related prompts."

payload = {
    "model": "deepseek-r1:7b",
    "messages": [
        {"role": "system", "content": instructions},
        {"role": "user", "content": str(new_data)}
    ],
    "temperature": 0.2,
    "max_tokens": 500,
}

for item in new_data:
    print("Processing item:", item)
    payload["messages"][1]["content"] = str(item)
    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()
    conclusion = response.json().get('choices', [])[0].get('message', {}).get('content', '')
    print("Conclusion:", conclusion)