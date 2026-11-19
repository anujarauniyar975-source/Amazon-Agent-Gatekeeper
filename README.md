# 🛡️ Amazon Agent Gatekeeper

> **Academic Disclaimer:** This application is developed as an **MBA Assignment Simulation** on Autonomous AI Agent Governance and Risk Management. The policies and thresholds (e.g., ₹5,000 threshold, return verification) are **proposed project rules** designed for academic evaluation and do not represent actual Amazon corporate policies.

---

## 📌 Project Overview
As enterprise systems integrate autonomous AI agents to interact with customers and process transactions, organizations need a **Gatekeeper (Policy Enforcement Point)**. Without proper controls, autonomous agents could place unauthorized high-value orders, disburse unverified refunds, or execute actions after their security access has been revoked.

This application provides a simple, interactive **Streamlit** interface to demonstrate how gatekeeper policies evaluate and govern agent actions in real time.

---

## 🚀 How to Run the Application

### Option 1: Quick Launch (Windows)
Double-click the `run.bat` file in this folder. It will automatically detect your Python environment and start the application.

### Option 2: Running via Terminal / PowerShell
Open your terminal in this folder (`Amazon agent gatekeeper`) and run:

```bash
# If using Anaconda (default on your system):
"C:\Users\Anuja\anaconda3\Scripts\streamlit.exe" run app.py

# Or if streamlit is in your system PATH:
streamlit run app.py
```

Once started, open your web browser at:
👉 **`http://localhost:8501`**

---

## 📋 Requirements & Implementation Mapping

| # | Requirement | Implementation in App |
|---|---|---|
| **1** | Title: "Amazon Agent Gatekeeper" | Displayed prominently at the top header, browser tab, and navigation bar. |
| **2** | Customer name, Agent name, Requested action, Transaction amount | Input fields provided in the **Gatekeeper Simulation** tab. |
| **3** | Administrator can register and revoke agents | **Administrator Console** tab allows adding new agents with specific roles and toggling status between `Active` and `Revoked`. |
| **4** | Block requests from unregistered or revoked agents | Gatekeeper rule immediately flags unregistered or revoked agents with a 🛑 **BLOCKED** status. |
| **5** | Active agents can view order details | Action `View Order Details` is evaluated with ✅ **ALLOWED** (zero financial liability). |
| **6** | Active agents can place orders up to ₹5,000 | Action `Place Order` with amount ≤ ₹5,000 is automatically ✅ **ALLOWED**. |
| **7** | Orders above ₹5,000 require customer confirmation | Action `Place Order` > ₹5,000 triggers ⚠️ **NEEDS CONFIRMATION**. Approved once customer confirmation is checked. |
| **8** | Return and refund requests require customer confirmation | `Return Request` and `Refund Request` always require explicit customer confirmation. |
| **9** | Maintain an audit log with required fields | **Audit Log & Analytics** tab records: `Date`, `Time`, `Customer`, `Agent`, `Action`, `Amount (₹)`, `Decision`, and `Reason`. Can be exported to CSV. |
| **10** | Display Enrolment Number field | Clearly displayed in the sidebar and top page header (customizable for student submission). |

---

## 🧪 Demo Test Scenarios (For Viva & Presentation)

1. **Scenario 1: Read-Only Query (Allowed)**
   - Customer: `Rahul Sharma`
   - Agent: `Agent_Alpha` (Active)
   - Action: `View Order Details`
   - *Result:* ✅ **ALLOWED** — Non-monetary query allowed.

2. **Scenario 2: Low-Value Autonomous Order (Allowed)**
   - Customer: `Priya Patel`
   - Agent: `Agent_Beta` (Active)
   - Action: `Place Order`, Amount: `₹3,200`
   - *Result:* ✅ **ALLOWED** — Within autonomous threshold (≤ ₹5,000).

3. **Scenario 3: High-Value Order without Confirmation (Blocked/Pending)**
   - Customer: `Ananya Gupta`
   - Agent: `Agent_Alpha` (Active)
   - Action: `Place Order`, Amount: `₹12,500`, Confirmation: `Unchecked`
   - *Result:* ⚠️ **NEEDS CONFIRMATION** — High-value transactions require human-in-the-loop oversight.

4. **Scenario 4: High-Value Order with Confirmation (Allowed)**
   - Same as Scenario 3, but check the **"Customer Confirmation Received"** box.
   - *Result:* ✅ **ALLOWED (CONFIRMED)** — Human approval recorded in the audit trail.

5. **Scenario 5: Return / Refund Request**
   - Customer: `Vikram Singh`
   - Agent: `Agent_Alpha` (Active)
   - Action: `Refund Request`, Amount: `₹1,800`, Confirmation: `Unchecked`
   - *Result:* ⚠️ **NEEDS CONFIRMATION** — All financial disbursement/return requests require explicit confirmation.

6. **Scenario 6: Revoked Agent Attempt (Blocked)**
   - Agent: `Agent_Gamma` (Revoked in Admin tab)
   - Action: Any
   - *Result:* 🛑 **BLOCKED** — Authorization revoked.

7. **Scenario 7: Unregistered Agent Attempt (Blocked)**
   - Agent: Select `Type Custom...` and enter `Rogue_Agent_99`
   - Action: Any
   - *Result:* 🛑 **BLOCKED** — Unregistered entity detected.

---

## 📁 File Structure

```text
Amazon agent gatekeeper/
│
├── app.py              # Main Streamlit web application
├── requirements.txt    # Python package dependencies
├── run.bat             # 1-Click launcher script for Windows
├── audit_log.csv       # Automatically generated audit history
└── README.md           # Project documentation and assignment notes
## Project Status

The Amazon Agent Gatekeeper prototype has been developed and tested using sample transactions.

The application checks agent permissions, customer confirmation requirements, and revoked agent status. It also maintains an audit log of decisions.

This project is an academic simulation and does not represent Amazon's actual internal policies.
## Limitations

This prototype is designed for academic demonstration. The ₹5,000 order threshold and permission rules are sample project rules, not verified Amazon policies. The application uses simulated agent activities and does not connect to Amazon's real customer accounts or systems.
```

---

## 💡 Key MBA Takeaways for Academic Submission
- **Principle of Least Privilege:** Agents are only granted capabilities strictly necessary for their function.
- **Human-In-The-Loop (HITL):** Financial risk escalation triggers mandatory human authorization.
- **Non-Repudiation & Traceability:** Immutable audit logs ensure regulatory compliance and forensic accountability.
