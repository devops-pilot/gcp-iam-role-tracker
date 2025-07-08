import os
from googleapiclient import discovery
from google.auth import default
from tabulate import tabulate
from colorama import Fore, Style

# Get credentials and initialize API client
creds, _ = default()
service = discovery.build('cloudresourcemanager', 'v1', credentials=creds)

project_id = os.getenv("GCP_PROJECT_ID")
if not project_id:
    print("❌ Please set the environment variable GCP_PROJECT_ID")
    exit(1)

request = service.projects().getIamPolicy(resource=project_id, body={})
response = request.execute()

bindings = response.get("bindings", [])
table = []

print(f"\n🔍 IAM Bindings for project: {project_id}\n")

for binding in bindings:
    role = binding["role"]
    members = binding.get("members", [])
    
    for member in members:
        # Format roles
        risky = "owner" in role.lower() or "admin" in role.lower()
        color = Fore.RED if risky else Fore.GREEN
        table.append([
            member,
            role,
            f"{color}❗ Risky{Style.RESET_ALL}" if risky else f"{color}✔️ Normal{Style.RESET_ALL}"
        ])

print(tabulate(table, headers=["Member", "Role", "Risk Level"]))
