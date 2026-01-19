# 🌍 Eco-Tracker: Fintech ESG Solution
**A Data-Driven Framework for Sustainable Banking**

### ⚡ Executive Summary
Developed an end-to-end Business Analysis and Product Management framework to integrate carbon footprint tracking into a digital banking ecosystem. This project demonstrates the ability to translate high-level ESG goals into technical requirements and validated data models.

---

### 🚀 Key Artifacts
* **[Product Strategy (PRD)](./PRD.md):** Vision, user stories, and success metrics for the Eco-Tracker feature.
* **[Technical Requirements](./Data_Dictionary.md):** Detailed data dictionary mapping MCC codes to carbon emission factors.
* **[Execution & Risk](./Risk_Register.md):** Mitigation strategies for data accuracy, API downtime, and compliance.
* **[User Stories & AC](./User_Stories.md):** Developer-ready acceptance criteria using the Gherkin-style framework.

---

### 📊 Technical Implementation (The "BA" Engine)
I utilized **Python** to engineer a privacy-safe, synthetic dataset to simulate real-world fintech transactions and validate the carbon-scoring logic.

* **[Synthetic Dataset](./data/transactions_synthetic.csv):** 100+ rows of categorized transaction data.
* **[Generation Script](./scripts/generate_data.py):** Python script utilizing the `Faker` library for scalable data modeling.

---

### 🛠️ Process Flow
```mermaid
graph LR
    A[Transaction] --> B(Categorization)
    B --> C{Carbon Engine}
    C --> D[User Dashboard]
    D --> E[Offset Actions]
