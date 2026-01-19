# User Stories & Acceptance Criteria (AC)

This document translates business goals into technical requirements for the engineering team.

## US.1: Real-time Carbon Calculation
**As a** customer,  
**I want** to see an estimated carbon footprint for my individual transactions,  
**So that** I can understand my immediate environmental impact.

### Acceptance Criteria:
* **AC 1.1:** The system must trigger a calculation immediately after a transaction is authorized.
* **AC 1.2:** The calculation must use the `mcc_code` to fetch the correct `emission_factor`.
* **AC 1.3:** The result must be displayed in the "Transaction Details" screen within 2 seconds.

---

## US.2: Monthly Sustainability Dashboard
**As a** user,  
**I want** a monthly summary of my carbon footprint categorized by spend type,  
**So that** I can identify which habits (e.g., travel vs. dining) are my biggest carbon drivers.

### Acceptance Criteria:
* **AC 2.1:** The dashboard must display a bar chart showing CO2e by category.
* **AC 2.2:** The dashboard must compare the current month's total to the previous month.
* **AC 2.3:** Data must be aggregated from the `transactions_synthetic.csv` logic.

---

## US.3: High-Carbon Alert
**As a** conscious spender,  
**I want** to receive a notification if a single transaction exceeds 50kg of CO2e,  
**So that** I can consider offsetting that specific purchase.

### Acceptance Criteria:
* **AC 3.1:** The system must check the `total_co2e_kg` field against a threshold of 50.0.
* **AC 3.2:** A push notification must be triggered if the threshold is met.
