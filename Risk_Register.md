# Risk Register: Eco-Tracker Launch

This document tracks potential threats to the project and outlines our strategy to prevent or handle them.

## Risk Assessment Matrix
We use a Score (1-25) = Probability (1-5) x Impact (1-5).

| ID | Risk Description | Category | Probability | Impact | Score | Mitigation Strategy (The Plan) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R1| **Inaccurate Data:** Carbon estimates are wrong, leading to "Greenwashing" claims. | Reputation | 3 | 5 | **15** | Use third-party verified APIs (Climatiq) and add a "Disclaimer" in the app. |
| R2 | **API Downtime:** The carbon calculation service goes offline. | Technical | 2 | 4 | **8** | Implement a "Cache" system that uses the last known average if the API fails. |
| R3 | **Data Privacy:** Leaking sensitive user transaction data. | Compliance | 1 | 5 | **5** | Anonymize all data before sending it to the carbon API; ensure GDPR & PSD2 compliance. |
| R4 | **Low Adoption:** Users don't care about their carbon footprint and ignore the feature. | Product | 4 | 3 | **12** | Run a marketing "Pilot" with 500 users first; use gamification (badges) to boost interest. |

## Risk Status Definitions
* Open: Active threat being monitored.
* Mitigated: Action has been taken to reduce the score.
* Closed:The risk is no longer a threat.
