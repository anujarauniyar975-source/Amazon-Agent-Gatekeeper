"""
Amazon Agent Gatekeeper Application
====================================
Academic Project Simulation for MBA Assignment
Topic: Autonomous Agent Governance & Transaction Gatekeeping
Note: The rules implemented here are proposed project rules for academic study
      and do not represent actual Amazon policies.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Amazon Agent Gatekeeper",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# File-backed Storage Helpers (Optional Persistence)
# ---------------------------------------------------------
LOG_FILE = "audit_log.csv"

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
# 1. Registered Agents database (default active & revoked agents for testing)
if "agents" not in st.session_state:
    st.session_state.agents = {
        "Agent_Alpha": {"status": "Active", "role": "Customer Support Agent"},
        "Agent_Beta": {"status": "Active", "role": "Fulfillment Assistant"},
        "Agent_Gamma": {"status": "Revoked", "role": "Contractor Agent (Deactivated)"},
    }

# 2. Audit Log database
if "audit_log" not in st.session_state:
    if os.path.exists(LOG_FILE):
        try:
            df_existing = pd.read_csv(LOG_FILE)
            st.session_state.audit_log = df_existing.to_dict(orient="records")
        except Exception:
            st.session_state.audit_log = []
    else:
        st.session_state.audit_log = []

# 3. Student Enrolment Number default
if "enrolment_no" not in st.session_state:
    st.session_state.enrolment_no = "MBA/2026/0142"


# ---------------------------------------------------------
# Gatekeeper Logic Function (Proposed Project Rules)
# ---------------------------------------------------------
def evaluate_transaction(customer_name, agent_name, action, amount, customer_confirmed):
    """
    Evaluates a transaction against the proposed project gatekeeping rules.
    Returns: (decision, reason, badge_type)
    Badge types: 'success', 'error', 'warning'
    """
    # Clean inputs
    agent_name = agent_name.strip()
    customer_name = customer_name.strip()

    # Rule Check 1: Agent Registration
    if agent_name not in st.session_state.agents:
        return (
            "BLOCKED",
            f"Agent '{agent_name}' is UNREGISTERED in the Gatekeeper system. Request denied.",
            "error"
        )

    # Rule Check 2: Agent Revocation
    agent_info = st.session_state.agents[agent_name]
    if agent_info["status"] == "Revoked":
        return (
            "BLOCKED",
            f"Agent '{agent_name}' authorization has been REVOKED by the administrator. Request denied.",
            "error"
        )

    # At this point, the agent is registered and ACTIVE.

    # Rule Check 3: View Order Details
    if action == "View Order Details":
        return (
            "ALLOWED",
            f"Active registered agent '{agent_name}' is authorized to view order details.",
            "success"
        )

    # Rule Check 4: Place Order
    if action == "Place Order":
        if amount <= 5000:
            return (
                "ALLOWED",
                f"Order of ₹{amount:,.2f} is within the autonomous approval threshold (≤ ₹5,000).",
                "success"
            )
        else:
            # Order amount exceeds ₹5,000: Needs customer confirmation
            if customer_confirmed:
                return (
                    "ALLOWED (CONFIRMED)",
                    f"High-value order of ₹{amount:,.2f} (> ₹5,000) verified and confirmed by customer '{customer_name}'.",
                    "success"
                )
            else:
                return (
                    "NEEDS CONFIRMATION",
                    f"Orders above ₹5,000 (Requested: ₹{amount:,.2f}) require explicit customer confirmation before processing.",
                    "warning"
                )

    # Rule Check 5: Return Request & Refund Request
    if action in ["Return Request", "Refund Request"]:
        if customer_confirmed:
            return (
                "ALLOWED (CONFIRMED)",
                f"{action} for ₹{amount:,.2f} verified and authorized by customer '{customer_name}'.",
                "success"
            )
        else:
            return (
                "NEEDS CONFIRMATION",
                f"All {action.lower()}s strictly require customer confirmation under proposed safety rules.",
                "warning"
            )

    return ("BLOCKED", "Unrecognized action requested.", "error")


def record_audit_log(customer_name, agent_name, action, amount, decision, reason):
    """Appends an entry to the audit log."""
    now = datetime.now()
    log_entry = {
        "Date": now.strftime("%Y-%m-%d"),
        "Time": now.strftime("%H:%M:%S"),
        "Enrolment_No": st.session_state.enrolment_no,
        "Customer": customer_name if customer_name else "N/A",
        "Agent": agent_name if agent_name else "N/A",
        "Action": action,
        "Amount (₹)": f"{amount:,.2f}" if action != "View Order Details" else "0.00",
        "Decision": decision,
        "Reason": reason
    }
    st.session_state.audit_log.insert(0, log_entry)  # Newest first

    # Save to CSV for persistence
    try:
        df = pd.DataFrame(st.session_state.audit_log)
        df.to_csv(LOG_FILE, index=False)
    except Exception:
        pass


# ---------------------------------------------------------
# Sidebar: Project Identity & Enrolment Number Field
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎓 MBA Project Details")
    enrol_input = st.text_input(
        "Student Enrolment Number:",
        value=st.session_state.enrolment_no,
        help="Display your academic enrolment number as required by the assignment."
    )
    st.session_state.enrolment_no = enrol_input

    st.markdown(f"**Enrolment No:** `{st.session_state.enrolment_no}`")
    st.markdown("**Subject:** AI Governance & Management")
    st.markdown("**Application:** Autonomous Agent Gatekeeper")

    st.divider()

    st.markdown("### 📜 Proposed Project Rules")
    st.info(
        """
        **Governance Rules Summary:**
        1. **Agent Authorization:** Unregistered or Revoked agents are blocked.
        2. **Order Viewing:** Active agents can view order details freely.
        3. **Autonomous Orders:** Orders ≤ ₹5,000 can be processed directly.
        4. **High-Value Orders:** Orders > ₹5,000 require customer confirmation.
        5. **Returns & Refunds:** Always require customer confirmation.
        6. **Auditability:** Every decision is logged with date, time, and reasoning.
        """
    )
    st.caption("ℹ️ *Note: These are proposed project rules for an MBA study and not actual Amazon corporate policies.*")


# ---------------------------------------------------------
# Main Page Header & Title
# ---------------------------------------------------------
st.title("🛡️ Amazon Agent Gatekeeper")
st.markdown(
    f"##### *A Governance & Policy Enforcement Interface for Autonomous E-Commerce Agents*  \n"
    f"**Academic Submission | Student Enrolment No:** `{st.session_state.enrolment_no}`"
)

# Disclaimer Banner
st.warning(
    "⚠️ **Academic Disclaimer:** The rules, thresholds (e.g., ₹5,000), and workflows shown below are "
    "**proposed project rules** designed for an MBA assignment on AI governance. They do not represent official Amazon policies.",
    icon="⚠️"
)

# ---------------------------------------------------------
# Tabs for Clean Organisation
# ---------------------------------------------------------
tab_gatekeeper, tab_admin, tab_logs, tab_guide = st.tabs([
    "🚪 Gatekeeper Simulation",
    "⚙️ Administrator Console",
    "📋 Audit Log & Analytics",
    "📘 Project Rules & MBA Guide"
])


# =========================================================
# TAB 1: GATEKEEPER SIMULATION
# =========================================================
with tab_gatekeeper:
    st.subheader("Process Agent Transaction Request")
    st.write("Submit a request on behalf of a customer or agent to see the Gatekeeper evaluate and enforce governance rules in real time.")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("#### 1. Transaction Details")

        customer_name = st.text_input("Customer Name", value="Rahul Sharma", placeholder="e.g. Rahul Sharma")

        # Select registered agent or type custom agent to test unregistered agents
        agent_options = list(st.session_state.agents.keys()) + ["Type Custom / Unregistered Agent..."]
        selected_agent_option = st.selectbox(
            "Select Agent:",
            options=agent_options,
            index=0,
            help="Choose an existing agent or select 'Type Custom' to test an unregistered agent."
        )

        if selected_agent_option == "Type Custom / Unregistered Agent...":
            agent_name = st.text_input("Enter Custom Agent Name:", placeholder="e.g. Rogue_Agent_X")
        else:
            agent_name = selected_agent_option

        # Display agent status pill
        if agent_name in st.session_state.agents:
            status = st.session_state.agents[agent_name]["status"]
            if status == "Active":
                st.caption(f"🟢 Status: **Active Registered Agent** ({st.session_state.agents[agent_name]['role']})")
            else:
                st.caption(f"🔴 Status: **REVOKED Agent** ({st.session_state.agents[agent_name]['role']})")
        else:
            if agent_name.strip():
                st.caption("⚪ Status: **Unregistered Agent**")

        action = st.selectbox(
            "Requested Action:",
            options=[
                "View Order Details",
                "Place Order",
                "Return Request",
                "Refund Request"
            ]
        )

        # Amount field (applicable for Place Order, Return Request, Refund Request)
        if action == "View Order Details":
            amount = 0.0
            st.text_input("Transaction Amount (₹):", value="N/A (Read-Only Action)", disabled=True)
        else:
            amount = st.number_input(
                "Transaction Amount (₹):",
                min_value=1.0,
                max_value=500000.0,
                value=3500.0 if action == "Place Order" else 1200.0,
                step=500.0,
                help="Autonomous agent threshold is ₹5,000 for placing orders."
            )

        st.markdown("#### 2. Human-In-The-Loop Verification")
        # Customer confirmation toggle
        customer_confirmed = st.checkbox(
            "✅ Customer Confirmation Received (OTP / Explicit Approval)",
            value=False,
            help="Check this box if the customer has provided explicit confirmation or OTP."
        )

        # Evaluate button
        process_btn = st.button("🚀 Submit to Gatekeeper", type="primary", use_container_width=True)

    with col2:
        st.markdown("#### 3. Gatekeeper Decision & Evaluation")

        if process_btn:
            if not customer_name.strip() or not agent_name.strip():
                st.error("Please enter both a valid Customer Name and Agent Name.")
            else:
                decision, reason, badge = evaluate_transaction(
                    customer_name=customer_name,
                    agent_name=agent_name,
                    action=action,
                    amount=amount,
                    customer_confirmed=customer_confirmed
                )

                # Record into Audit Log
                record_audit_log(
                    customer_name=customer_name,
                    agent_name=agent_name,
                    action=action,
                    amount=amount,
                    decision=decision,
                    reason=reason
                )

                # Show Result Card
                st.markdown("---")
                if badge == "success":
                    st.success(f"### ✅ DECISION: {decision}")
                    st.write(f"**Reason:** {reason}")
                elif badge == "error":
                    st.error(f"### 🛑 DECISION: {decision}")
                    st.write(f"**Reason:** {reason}")
                else:
                    st.warning(f"### ⚠️ DECISION: {decision}")
                    st.write(f"**Reason:** {reason}")
                    st.info("💡 **Next Step:** To proceed with this transaction, obtain explicit customer confirmation (check the confirmation box) and resubmit.")

                st.markdown("---")
                st.markdown("##### 📌 Evaluation Summary")
                st.json({
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Enrolment_No": st.session_state.enrolment_no,
                    "Customer": customer_name,
                    "Agent": agent_name,
                    "Agent Registered?": agent_name in st.session_state.agents,
                    "Agent Status": st.session_state.agents.get(agent_name, {}).get("status", "Not Registered"),
                    "Action": action,
                    "Amount (₹)": amount,
                    "Customer Confirmed?": customer_confirmed,
                    "Final Gatekeeper Decision": decision
                })
        else:
            st.info("Enter transaction details on the left and click **'Submit to Gatekeeper'** to evaluate.")
            st.markdown(
                """
                **Quick Scenarios to Test:**
                - 🟢 **Allowed:** Agent `Agent_Alpha` places order of ₹3,500 (≤ ₹5,000).
                - 🟢 **Allowed:** Agent `Agent_Alpha` views order details.
                - ⚠️ **Confirmation Required:** Agent `Agent_Alpha` places order of ₹7,500 (> ₹5,000) without confirmation.
                - 🟢 **Allowed with Confirmation:** Agent `Agent_Alpha` places order of ₹7,500 with confirmation checked.
                - ⚠️ **Confirmation Required:** Return or Refund request without customer confirmation.
                - 🛑 **Blocked:** Revoked agent `Agent_Gamma` attempts any action.
                - 🛑 **Blocked:** Custom unregistered agent (e.g. `Hacker_Agent`) attempts any action.
                """
            )


# =========================================================
# TAB 2: ADMINISTRATOR CONSOLE (Agent Registration & Revocation)
# =========================================================
with tab_admin:
    st.subheader("Administrator Console: Agent Lifecycle Management")
    st.write("Register new authorized agents or revoke access privileges of existing agents.")

    admin_col1, admin_col2 = st.columns(2, gap="large")

    with admin_col1:
        st.markdown("#### ➕ Register New Agent")
        with st.form("register_agent_form"):
            new_agent_name = st.text_input("New Agent Identifier / Name:", placeholder="e.g. Agent_Delta")
            new_agent_role = st.selectbox(
                "Agent Role / Permission Scope:",
                ["Customer Support Agent", "Order Fulfillment Agent", "Returns Specialist", "General AI Assistant"]
            )
            submit_register = st.form_submit_button("Register Agent", type="primary")

            if submit_register:
                clean_name = new_agent_name.strip()
                if not clean_name:
                    st.error("Agent name cannot be empty.")
                elif clean_name in st.session_state.agents:
                    st.warning(f"Agent '{clean_name}' is already registered.")
                else:
                    st.session_state.agents[clean_name] = {"status": "Active", "role": new_agent_role}
                    st.success(f"Agent '{clean_name}' successfully registered and marked ACTIVE.")
                    st.rerun()

    with admin_col2:
        st.markdown("#### 🚫 Revoke / Reinstate Agent")
        with st.form("revoke_agent_form"):
            agent_to_modify = st.selectbox(
                "Select Agent to Modify:",
                options=list(st.session_state.agents.keys()),
                help="Choose an agent to revoke or reinstate."
            )
            target_status = st.radio(
                "Set Authorization Status:",
                ["Active", "Revoked"],
                index=0 if st.session_state.agents.get(agent_to_modify, {}).get("status") == "Active" else 1
            )
            submit_modify = st.form_submit_button("Update Agent Status")

            if submit_modify:
                st.session_state.agents[agent_to_modify]["status"] = target_status
                if target_status == "Revoked":
                    st.error(f"Agent '{agent_to_modify}' has been REVOKED. All future requests will be blocked.")
                else:
                    st.success(f"Agent '{agent_to_modify}' is now ACTIVE.")
                st.rerun()

    st.markdown("---")
    st.markdown("#### 📋 Current Agent Directory")

    # Render agents table
    agent_rows = []
    for ag_name, ag_details in st.session_state.agents.items():
        agent_rows.append({
            "Agent Name": ag_name,
            "Role": ag_details["role"],
            "Status": "🟢 Active" if ag_details["status"] == "Active" else "🔴 Revoked"
        })
    df_agents = pd.DataFrame(agent_rows)
    st.dataframe(df_agents, use_container_width=True)


# =========================================================
# TAB 3: AUDIT LOG & ANALYTICS
# =========================================================
with tab_logs:
    st.subheader("Audit Log & Compliance Records")
    st.write("Complete traceability log tracking every gatekeeper evaluation, decision, and policy rationale.")

    # KPI summary cards
    if st.session_state.audit_log:
        df_log = pd.DataFrame(st.session_state.audit_log)

        total_tx = len(df_log)
        allowed_tx = len(df_log[df_log["Decision"].str.contains("ALLOWED", na=False)])
        blocked_tx = len(df_log[df_log["Decision"] == "BLOCKED"])
        needs_conf_tx = len(df_log[df_log["Decision"] == "NEEDS CONFIRMATION"])

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Total Requests Evaluated", total_tx)
        kpi2.metric("Allowed Transactions", allowed_tx)
        kpi3.metric("Blocked Requests", blocked_tx)
        kpi4.metric("Pending Confirmations", needs_conf_tx)

        st.markdown("---")

        # Filters
        filter_col1, filter_col2 = st.columns([1, 1])
        with filter_col1:
            decision_filter = st.multiselect(
                "Filter by Decision:",
                options=list(df_log["Decision"].unique()),
                default=list(df_log["Decision"].unique())
            )
        with filter_col2:
            agent_filter = st.multiselect(
                "Filter by Agent:",
                options=list(df_log["Agent"].unique()),
                default=list(df_log["Agent"].unique())
            )

        filtered_df = df_log[
            df_log["Decision"].isin(decision_filter) &
            df_log["Agent"].isin(agent_filter)
        ]

        st.dataframe(filtered_df, use_container_width=True)

        col_export, col_clear = st.columns([1, 1])
        with col_export:
            csv_data = filtered_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Audit Log as CSV",
                data=csv_data,
                file_name=f"amazon_gatekeeper_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        with col_clear:
            if st.button("🗑️ Clear Audit Log History"):
                st.session_state.audit_log = []
                if os.path.exists(LOG_FILE):
                    os.remove(LOG_FILE)
                st.success("Audit log cleared.")
                st.rerun()

    else:
        st.info("No transaction logs recorded yet. Run a transaction in the 'Gatekeeper Simulation' tab to generate logs.")


# =========================================================
# TAB 4: MBA PROJECT GUIDE & RULES EXPLANATION
# =========================================================
with tab_guide:
    st.subheader("MBA Assignment Concept: Autonomous Agent Governance")
    st.markdown(
        f"""
        ### 1. Executive Summary & Purpose
        As artificial intelligence agents gain autonomy in enterprise e-commerce systems, organizations face significant risk:
        - **Financial exposure:** Agents placing accidental, unauthorized, or fraudulent orders.
        - **Operational liability:** Unverified refund payouts and inventory depletion.
        - **Access control risks:** Rogue, compromised, or deactivated third-party agents executing actions.

        This **Amazon Agent Gatekeeper** application implements a **Policy Enforcement Point (PEP)** architecture,
        ensuring that autonomous agents operate within strictly defined risk boundaries.

        ---

        ### 2. Proposed Project Rules vs MBA Governance Principles

        | Requirement # | Proposed Project Rule | MBA Governance Principle |
        | :--- | :--- | :--- |
        | **Req 1 & 10** | Title & Enrolment Number Display | Academic integrity, audit ownership, and traceability. |
        | **Req 2** | Capture Customer, Agent, Action & Amount | Complete context ingestion before decision execution. |
        | **Req 3 & 4** | Administrator Agent Registration & Revocation | **Principle of Least Privilege & Zero Trust:** Unregistered or Revoked entities are instantly blocked. |
        | **Req 5** | Active agents can view order details | **Read-Only Authorization:** Non-monetary, low-risk actions have zero financial impact. |
        | **Req 6** | Autonomous order placement up to ₹5,000 | **Risk Tiering / Velocity Threshold:** Small transactions are automated for business efficiency. |
        | **Req 7** | Orders above ₹5,000 require customer confirmation | **Human-In-The-Loop (HITL):** High-value decisions require human oversight to prevent financial loss. |
        | **Req 8** | All Returns & Refunds require customer confirmation | **Loss Prevention:** Reversing transactions or disbursing money requires verified customer intent. |
        | **Req 9** | Comprehensive Audit Log | **Non-Repudiation & Forensic Compliance:** Full logging of date, time, actor, decision, and rationale. |

        ---

        ### 3. Student Submission Details
        - **Candidate Enrolment No:** `{st.session_state.enrolment_no}`
        - **Technology Stack:** Python 3, Streamlit, Pandas
        - **Architecture:** Rule-Based Gatekeeper with Session State & CSV Audit Logging
        """
    )
