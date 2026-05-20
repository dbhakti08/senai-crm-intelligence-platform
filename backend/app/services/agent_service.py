def generate_agent_trace(thread_type: str):

    if thread_type == "bob_outage":

        return [

            {
                "thought": "Customer reports production outage and SLA breach.",
                "action": "Classify incident severity.",
                "observation": "Detected P0 critical outage."
            },

            {
                "thought": "Need enterprise SLA guidance.",
                "action": "Retrieve SLA policy from knowledge base.",
                "observation": "99.9% uptime SLA with legal escalation requirements."
            },

            {
                "thought": "Customer threatens legal escalation.",
                "action": "Escalate to legal and incident response teams.",
                "observation": "Escalation policy triggered."
            },

            {
                "thought": "Need customer communication.",
                "action": "Generate operational response.",
                "observation": "Prepared executive escalation response."
            }
        ]

    if thread_type == "karen_refund":

        return [

            {
                "thought": "Customer is frustrated and threatening churn.",
                "action": "Analyze sentiment.",
                "observation": "Negative sentiment detected."
            },

            {
                "thought": "Need refund eligibility guidance.",
                "action": "Retrieve refund policy.",
                "observation": "Refund exceptions allowed for outages."
            },

            {
                "thought": "High-value customer risk detected.",
                "action": "Escalate to retention team.",
                "observation": "Retention workflow initiated."
            }
        ]

    return [
        {
            "thought": "General operational workflow.",
            "action": "Monitor conversation.",
            "observation": "No escalation required."
        }
    ]