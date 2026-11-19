# 📝 Prompts & AI Assistance Documentation

**Course / Degree:** MBA  
**Subject:** AI Governance & Information Systems  
**Project:** Amazon Agent Gatekeeper (Streamlit Application)  
**Student Enrolment No:** MBA/2025/66518  

---

## 1. Academic Integrity & AI Disclosure Statement

This project was developed with the assistance of an AI coding assistant (Google Antigravity / Gemini) to assist with code structure, Streamlit user interface design, and policy rule implementation.

### Student Review Statement:
- The underlying business rules, thresholds (e.g., ₹5,000 order limit, customer confirmation for returns/refunds), and gatekeeping logic represent **proposed project rules** for an MBA academic assignment.
- The application code was reviewed and inspected by the student to understand the governance principles, transaction evaluation logic, and audit trail functionality.

---

## 2. Actual Prompts Used in This Project

### Prompt 1: Initial Application Generation & Requirements
*Used to generate the initial Streamlit application (`app.py`), requirements, batch runner, and documentation.*

```text
I am a beginner working on an MBA assignment. Help me build a simple Amazon Agent Gatekeeper application using Python and Streamlit.

The application should:
1. Display the title "Amazon Agent Gatekeeper".
2. Ask for customer name, agent name, requested action and transaction amount.
3. Allow the administrator to register agents and revoke agents.
4. Block requests from unregistered or revoked agents.
5. Allow registered active agents to view order details.
6. Allow registered active agents to place orders up to ₹5,000.
7. Ask for customer confirmation for orders above ₹5,000.
8. Ask for customer confirmation for all return and refund requests.
9. Maintain an audit log with date, time, customer, agent, action, amount, decision and reason.
10. Display the enrolment number field.

Use simple Python code and a beginner-friendly interface. Create all required files in the currently open project folder. Explain each step and tell me how to run the application. Do not invent real Amazon policies; label these as proposed project rules.
```

---

### Prompt 2: Documentation & Prompt Logging Request
*Used to request the creation of `PROMPTS.md` to document the actual prompts used.*

```text
Create a file named PROMPTS.md in my current Amazon Agent Gatekeeper project folder.

Document the actual prompts used during this project, including the initial prompt used to generate the Streamlit application and any subsequent prompts used for corrections or improvements.

Do not invent prompts that were not used. Clearly explain that the application was developed with AI assistance and that the student reviewed and tested the output.

Keep the file simple and suitable for an MBA assignment.
```

---

### Prompt 3: Correction & Verification Accuracy
*Used to update the enrolment number and ensure strict accuracy regarding testing claims.*

```text
Please correct PROMPTS.md:
1. Change the enrolment number to MBA/2025/66518.
2. Remove any claim that all scenarios were tested or verified unless we have actually completed those tests.
3. Keep the actual prompts used in this project.
4. Save the corrected file in the current project folder.

Do not modify app.py or any other project file.
## Testing and Validation

The prototype was tested with different scenarios:

1. Order placement within the ₹5,000 limit.
2. Order placement above the ₹5,000 limit without customer confirmation.
3. Order placement above the ₹5,000 limit with customer confirmation.
4. Attempted action by a revoked agent.
5. Product return request without customer confirmation.

The results were checked in the application and audit log.
```

---

## 3. Project Status & Corrections Note
- The enrolment number has been updated to `MBA/2025/66518`.
- Broad claims of comprehensive testing have been removed; the student reviews the code and validates features directly through the Streamlit interface.
- No changes were made to `app.py` or any other project files as requested.
