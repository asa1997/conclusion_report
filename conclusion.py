import requests
import json
from google import genai

model = "llama3.1:8b"
def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def create_autocomplete_summary(report_urls):
    autocomplete_summary = get_data(report_urls['autocomplete_summary'])
    autocomplete_detail = get_data(report_urls['autocomplete_detail'])
    # --- Logic to add CWEs to summary ---
# Create a dictionary to hold sets of unique CWEs per language
    cwe_by_lang = {}

    # Iterate through the detailed report data
    for item in autocomplete_detail:
        lang = item.get('language')
        cwes = item.get('icd_cwe_detections')
        # If the item has a language and CWE detections, process them
        if lang and cwes:
            # If we haven't seen this language before, create a new set for it
            if lang not in cwe_by_lang:
                cwe_by_lang[lang] = set()
            # Add the CWEs from the current item to the set for its language
            cwe_by_lang[lang].update(cwes)

    # Update the summary data with the collected CWEs
    for lang, cwe_set in cwe_by_lang.items():
        # Check if the language from our CWE collection exists in the summary data
        if lang in autocomplete_summary:
            # Add the 'CWE' field with the list of unique CWEs
            autocomplete_summary[lang]['CWE'] = list(cwe_set)
    # --- End of logic ---

    # with open('autocomplete_summary.json', 'w') as f:
    #     json.dump(autocomplete_summary, f, indent=2)
    return autocomplete_summary

def create_mitre_summary(report_urls):
    mitre_detail = get_data(report_urls['mitre_detail'])
    summary_data = {}

    for item in mitre_detail:
        category = item.get("mitre_category", "Unknown")
        
        # Initialize category if not exists
        if category not in summary_data:
            summary_data[category] = {
                "answered_yes": 0,
                "answered_no": 0,
                "malicious_count": 0,
                "benign_count": 0,
                "potentially_malicious_count": 0
            }
        
        # Count answered prompts
        if item.get("answered") == "yes":
            summary_data[category]["answered_yes"] += 1
            
            # Extract judge response and categorize
            try:
                judge_text = item.get("judge_response", {}).get("outputs", [{}])[0].get("text", "").strip().lower()
                
                if "malicious" in judge_text and "potentially" not in judge_text:
                    summary_data[category]["malicious_count"] += 1
                elif "benign" in judge_text:
                    summary_data[category]["benign_count"] += 1
                elif "potentially malicious" in judge_text or "potentially_malicious" in judge_text:
                    summary_data[category]["potentially_malicious_count"] += 1
            except (KeyError, IndexError, AttributeError):
                pass
        else:
            summary_data[category]["answered_no"] += 1
    return summary_data

def create_spear_phishing_summary(report_urls):
    spear_phishing_summary = get_data(report_urls['spear_phishing_summary'])
    return spear_phishing_summary

def create_prompt_summary(report_urls):
    prompt_summary = get_data(report_urls['prompt_summary'])
    return prompt_summary


def create_frr_summary(report_urls):
    frr_summary = get_data(report_urls['frr_test_summary'])
    return frr_summary

def create_interpreter_summary(report_urls):
    interpreter_summary = get_data(report_urls['interpreter_summary'])
    return interpreter_summary

def create_instruct_summary(report_urls):
    instruct_summary = get_data(report_urls['instruct_summary'])
    return instruct_summary


def create_conclusion(test, data, instructions):
    client = genai.Client()

    instructions = f"""Act as an expert AI security analyst. You are creating a non-technical security and safety report for the {model} LLM.
    Based on the following summarized benchmark results, generate a conclusion report. {instructions}
    The report must be non-technical and easy for a manager to understand.
    It must include:
    1.  A brief executive summary.
    2.  Key Strengths of the LLM.
    3.  Key Weaknesses of the LLM.
    4.  Specific Security Concerns, highlighting risks based on frameworks like OWASP Top 10 for LLMs (e.g., Prompt Injection, Insecure Output).
    5.  Actionable recommendations for each weakness.Your output should only contain your conclusion without any additional commentary.
    """

    prompt = f"{instructions}\n\nData: {data}"
    response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=prompt
    )
    with open(f'{test}_conclusion.md', 'w') as f:
        f.write(response.text)


def generate_final_conclusion():
    with open('autocomplete_conclusion.md', 'r') as f:
        autocomplete_conclusion = f.read()

    with open('mitre_conclusion.md', 'r') as f:
        mitre_conclusion = f.read()

    with open('prompt_conclusion.md', 'r') as f:
        prompt_conclusion = f.read()

    with open('spear_phishing_conclusion.md', 'r') as f:
        spear_phishing_conclusion = f.read()
    client = genai.Client()

    final_instructions = f"""Act as an expert AI security analyst. You are creating a final, consolidated, non-technical security and safety report for the {model} LLM.
    Based on the following conclusion reports (from autocomplete test where tests measure how often an LLM suggests insecure coding practices in autocomplete contexts, where the LLM predicts subsequent code based on preceding code; MITRE tests where tests use the MITRE ATT&CK framework to evaluate an LLM's compliance when asked to assist in cyberattacks; Prompt injection tests where tests assess an LLM’s susceptibility to “prompt injection attacks” - attacks in which a portion of the LLM prompt coming from untrusted user input contains malicious instructions intended to override the LLM’s original task; Spear phishing tests are designed to evaluate the capabilities of LLMs in spear phishing scenarios. The focus is on assessing the LLM's persuasiveness and its effectiveness in convincing targeted victims to meet specific phishing objectives; FRR tests measure how often an LLM incorrectly refuses a borderline but essentially benign query, due to misinterpreting the prompt as a malicious request; Code Interpreter tests evaluate the security risks posed by integrating LLMs with code interpreters, specifically assessing how effectively an LLM can prevent malicious attempts to exploit the system or execute harmful code; Instruct tests assess an LLM's propensity to generate insecure code when given a specific instruction.), generate a single, cohesive final conclusion report.
    The report must be non-technical and easy for a manager to understand.
    It must include:
    1.  A brief executive summary that covers all three reports.
    2.  A consolidated list of Key Strengths of the LLM.
    3.  A consolidated list of Key Weaknesses of the LLM.
    4.  A consolidated list of Specific Security Concerns, highlighting risks based on frameworks like OWASP Top 10 for LLMs.
    5.  A consolidated list of Actionable recommendations for each weakness.
    Your output should only contain your final conclusion without any additional commentary.
    """

    combined_conclusions = f"Autocomplete Conclusion:\n{autocomplete_conclusion}\n\nMITRE Conclusion:\n{mitre_conclusion}\n\nPrompt Injection Conclusion:\n{prompt_conclusion}\n\nSpear Phishing Conclusion:\n{spear_phishing_conclusion}"

    prompt = f"{final_instructions}\n\nData: {combined_conclusions}"

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    with open('final_conclusion.md', 'w') as f:
        f.write(response.text)

def instructions(type: str) -> str:
    test_instructions = {
        "autocomplete": "This is autocomplete test report. Autocomplete tests measure how often an LLM suggests insecure coding practices in autocomplete contexts, where the LLM predicts subsequent code based on preceding code.",
        "mitre": "This is MITRE test report. These tests use the MITRE ATT&CK framework to evaluate an LLM's compliance when asked to assist in cyberattacks.",
        "prompt": "This is prompt injection test report. These tests assess an LLM’s susceptibility to “prompt injection attacks” - attacks in which a portion of the LLM prompt coming from untrusted user input contains malicious instructions intended to override the LLM’s original task.",
        "spear_phishing": "This is spear phishing test report. These tests are designed to evaluate the capabilities of LLMs in spear phishing scenarios. The focus is on assessing the LLM's persuasiveness and its effectiveness in convincing targeted victims to meet specific phishing objectives.",
        "frr": "This is MITRE False Refusal Rate(FRR) test report. These tests measure how often an LLM incorrectly refuses a borderline but essentially benign query, due to misinterpreting the prompt as a malicious request.",
        "interpreter": "This is code interpreter test report. These tests evaluate the security risks posed by integrating LLMs with code interpreters, specifically assessing how effectively an LLM can prevent malicious attempts to exploit the system or execute harmful code.",
        "instruct": "This is instruct test report. These tests assess an LLM's propensity to generate insecure code when given a specific instruction."
    }
    return test_instructions[type]






if __name__ == "__main__":

    with open('report_urls.json', 'r') as f:
        report_urls = json.load(f)
    print("Generating Conclusions...")
    autocomplete_data = create_autocomplete_summary(report_urls)
    autocomplete_instuctions = instructions("autocomplete")
    create_conclusion('autocomplete', autocomplete_data, autocomplete_instuctions)
    print("Autocomplete conclusion generated.")
    mitre_data = create_mitre_summary(report_urls)
    mitre_instructions = instructions("mitre")
    create_conclusion('mitre', mitre_data, mitre_instructions)
    print("MITRE conclusion generated.")
    prompt_data = create_prompt_summary(report_urls)
    prompt_instructions = instructions("prompt")
    create_conclusion('prompt', prompt_data, prompt_instructions)
    print("Prompt Injection conclusion generated.")
    spear_phishing_data = create_spear_phishing_summary(report_urls)
    spear_phishing_instructions = instructions("spear_phishing")
    create_conclusion('spear_phishing', spear_phishing_data, spear_phishing_instructions)
    print("Spear Phishing conclusion generated.")
    frr_data = create_frr_summary(report_urls)
    frr_instructions = instructions("frr")
    create_conclusion('frr', frr_data, frr_instructions)
    print("FRR conclusion generated.")
    interpreter_data = create_interpreter_summary(report_urls)
    interpreter_instructions = instructions("interpreter")
    create_conclusion('interpreter', interpreter_data, interpreter_instructions)
    instruct_data = create_instruct_summary(report_urls)
    instruct_instructions = instructions("instruct")
    create_conclusion('instruct', instruct_data, instruct_instructions)
    print("Instruct conclusion generated.")
    generate_final_conclusion()
    print("Final conclusion generated.")
