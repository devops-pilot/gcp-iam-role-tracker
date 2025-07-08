# 🔐 GCP IAM Role Usage Tracker

A simple and powerful CLI tool to audit **who has what roles** in a GCP project — and flag risky or overly permissive bindings like `roles/owner`, `roles/editor`, or `dns.admin`.

---

## 🎯 Features

- ✅ Lists all IAM role bindings in a GCP project
- 🔍 Flags risky roles (e.g., `roles/owner`, `dns.admin`, `editor`)
- 🎨 Color-coded output with tabular display
- ⚙️ Works with service accounts, users, groups, etc.
- ☁️ Uses the Google Cloud Python SDK (no GCP billing required)

---

## 📁 Project Structure
```
gcp-iam-role-tracker/
├── tracker.py # Main script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Quickstart

### 🔧 Prerequisites

- Python 3.8+
- Access to the GCP project (with `roles/viewer` or better)
- `gcloud auth application-default login` setup

---

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/gcp-iam-role-tracker.git
cd gcp-iam-role-tracker
```
 ### 2. Set up virtual environment (recommended)
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 3. Set GCP project ID
```
export GCP_PROJECT_ID="your-project-id"
```
### 4. Run the tool
```
python tracker.py
```
## 🧪 Sample Output
```
🔍 IAM Bindings for project: "your-project-id"

| Member                                      | Role                         | Risk Level |
|--------------------------------------------|------------------------------|------------|
| user:admin@example.com                     | roles/owner                  | ❗ Risky   |
| sa:external-dns@...gserviceaccount.com     | roles/dns.admin              | ❗ Risky   |
| sa:ci-bot@...gserviceaccount.com           | roles/viewer                 | ✔️ Normal  |

```
## 🔒 IAM Permissions Required
```
{
  "Effect": "Allow",
  "Action": [
    "resourcemanager.projects.getIamPolicy"
  ],
  "Resource": "*"
}
```
## 💡 Ideas for Future Enhancements
 - Export report to CSV or JSON
 - Scan multiple projects or folders
 - Alert for unused service accounts
 - GitHub Action or scheduler
## 📄 License
  - MIT

## 🙌 Contribute
- Feel free to fork, enhance, and submit PRs.
- If you find this tool helpful, consider giving it a ⭐ on GitHub!

