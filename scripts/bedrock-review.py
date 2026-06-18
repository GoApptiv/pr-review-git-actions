import boto3
import json


bedrock = boto3.client(
    "bedrock-runtime",
    region_name="ap-south-1"
)


with open("review-instructions.md") as f:
    instructions = f.read()


with open("pr-details.json") as f:
    pr_details = f.read()


with open("pr.diff") as f:
    diff = f.read()


prompt = f"""
{instructions}

PR Details:
{pr_details}

Code Changes:
{diff}
"""


response = bedrock.invoke_model(
    modelId="apac.anthropic.claude-3-5-sonnet-20240620-v1:0",

    body=json.dumps({

        "anthropic_version":
        "bedrock-2023-05-31",

        "max_tokens": 8000,

        "system": instructions,

        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]

    })
)


result = json.loads(
    response["body"].read()
)


review = result["content"][0]["text"]


with open(
    "pr-review.md",
    "w"
) as f:
    f.write(review)