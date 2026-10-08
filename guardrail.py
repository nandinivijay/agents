# Configure AWS clients
import boto3

bedrock_client = boto3.client("bedrock")
bedrock_runtime = boto3.client("bedrock-runtime")

def get_guardrail_id():
    """
    Get the guardrail ID for the Bitcoin advice guardrail.
    
    Returns:
        str or None: The guardrail ID if found, None otherwise
    """
    guardrail_name = "CleaningAgentGuardrail"
    
    try:
        existing_guardrails = bedrock_client.list_guardrails()
        for guardrail in existing_guardrails.get("guardrails", []):
            if guardrail.get("name") == guardrail_name:
                guardrail_id = guardrail.get("id")
                print(f"Found guardrail '{guardrail_name}' with ID: {guardrail_id}")
                return guardrail_id
        
        print(f"Guardrail '{guardrail_name}' not found")
        return None
        
    except Exception as e:
        print(f"Error finding guardrail: {e}")
        return None
