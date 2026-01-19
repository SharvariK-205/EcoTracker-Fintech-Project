# Data Dictionary: Eco-Tracker Feature

## 1. Transaction Input Data (From Bank Core)
This table defines the raw data we receive from the banking transaction engine.

| Field Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `transaction_id` | String (UUID) | Unique identifier for the transaction | `TXN-98765` |
| `user_id` | String | Unique identifier for the customer | `USER-123` |
| `mcc_code` | Integer | Merchant Category Code (determines spending type) | `5411` (Grocery) |
| `amount_usd` | Decimal | Total spent in USD | `45.50` |
| `merchant_name` | String | Name of the vendor | `Starbucks` |

## 2. Carbon Calculation Data (Calculated Fields)
This table defines the data we generate using the Carbon API.

| Field Name | Data Type | Description | Formula / Source |
| :--- | :--- | :--- | :--- |
| `emission_factor` | Float | CO2e kg per dollar spent for that MCC | Climatiq API |
| `total_co2e_kg` | Float | Calculated carbon footprint of the spend | `amount_usd` * `emission_factor` |
| `impact_level` | String | Qualitative ranking (Low, Medium, High) | Logic: <1kg=Low, >5kg=High |

## 3. User Sustainability Profile
Data stored to track user progress over time.

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `monthly_goal_kg` | Float | User-defined carbon limit for the month |
| `total_offset_kg` | Float | Sum of all carbon offsets purchased by the user |
| `eco_rank` | String | Tier based on performance (e.g., Seed, Sapling, Oak) |
