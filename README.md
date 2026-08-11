# 🌱 Soil Health Recommender

### Rule-Based Crop Condition Analysis with Streamlit

A lightweight Streamlit application for comparing soil and environmental readings against predefined crop-specific reference ranges.

The application evaluates individual parameters, highlights readings that fall above or below the configured ranges, and generates simple recommendations to help users understand which conditions may require attention.

> **Note:** This is a rule-based educational prototype, not a machine-learning model or validated agronomic decision-support system.

---

## ✨ Features

* 🌾 Crop-specific analysis for rice and wheat
* 💧 Water-level evaluation
* 🌱 Nitrogen, phosphorus, and potassium analysis
* 🌡️ Temperature comparison
* 🧪 Soil pH evaluation
* 📊 Parameter-by-parameter status table
* 📈 Reference-range match score
* 💡 Automatic recommendations for values outside configured ranges
* 🖥️ Interactive Streamlit interface

---

## 🧠 How It Works

The application uses predefined reference ranges for each supported crop.

For example:

```text
User selects crop
       ↓
Enter soil/environment readings
       ↓
Compare each parameter with configured range
       ↓
┌────────┬────────┬────────┐
│  Low   │ Normal │  High  │
└────────┴────────┴────────┘
       ↓
Generate parameter-level recommendations
       ↓
Calculate reference-range match percentage
```

No trained machine-learning model is used.

The system is deterministic: the same readings and crop selection always produce the same result.

---

## 🌾 Supported Crops

The current prototype supports:

* Rice
* Wheat

Each crop has configured reference ranges for:

| Parameter   | Unit  |
| ----------- | ----- |
| Water level | %     |
| Nitrogen    | kg/ha |
| Phosphorus  | kg/ha |
| Temperature | °C    |
| Potassium   | kg/ha |
| pH          | —     |

---

## 🔍 Recommendation Logic

Each reading is compared with the selected crop's configured range.

### Below Range

```text
value < minimum
```

The application identifies the parameter as **Low** and recommends increasing it toward the configured range.

### Within Range

```text
minimum <= value <= maximum
```

The parameter is marked **Normal**.

### Above Range

```text
value > maximum
```

The parameter is marked **High** and the application recommends reducing it toward the configured range.

---

## 📊 Reference-Range Match Score

The application calculates the percentage of entered parameters that fall within their configured ranges:

```text
parameters within range
────────────────────────── × 100
total parameters
```

For example, if 4 of the 6 parameters are within their configured ranges:

```text
4 / 6 × 100 ≈ 66%
```

This value should be interpreted only as a **reference-range match score** for this prototype.

It is not a scientifically validated soil-health index.

---

## 🛠️ Tech Stack

**Language**

`Python`

**Application**

`Streamlit`

**Data Handling**

`Pandas`

---

## 📁 Project Structure

```text
soil-health-recommender/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Gravity-2010/soil-health-recommender.git
cd soil-health-recommender
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will open the application in your browser.

---

## 💻 Example Workflow

1. Select **Rice** or **Wheat**.
2. Enter readings for:

   * water level
   * nitrogen
   * phosphorus
   * temperature
   * potassium
   * pH
3. Click **Analyze Soil Health**.
4. Review the parameter table.
5. Review values classified as Low, Normal, or High.
6. Review the generated recommendations.

---

## ⚠️ Limitations

This project is intentionally lightweight.

Current limitations include:

* Only rice and wheat are supported.
* Reference ranges are statically configured.
* Recommendations use deterministic rules rather than a trained ML model.
* Geographic location is not considered.
* Soil type is not considered.
* Crop variety and growth stage are not considered.
* Weather and historical sensor data are not incorporated.
* The reference-range match score is not a validated soil-health metric.

---

## 🔮 Possible Improvements

Potential extensions include:

* Supporting additional crops
* Moving crop ranges into a configuration/database layer
* Adding authoritative references for agronomic ranges
* Incorporating soil type and crop growth stage
* Integrating live IoT sensor readings
* Storing historical measurements
* Adding trend visualization
* Adding location-aware recommendations
* Building a validated data-driven recommendation model when suitable training data are available

---

## ⚠️ Disclaimer

This application is an **educational software prototype**.

The configured crop ranges and generated recommendations should not be treated as professional agricultural advice. Real crop and soil-management decisions depend on factors such as location, crop variety, soil type, climate, growth stage, and locally validated agronomic guidance.

---

## 👩‍💻 Author

**Garvita Jain**

M.S. Computer Science — University of Maryland, Baltimore County

[GitHub](https://github.com/Gravity-2010) · [LinkedIn](https://www.linkedin.com/in/garvitajain-605a89160/)

---

## 📌 Repository Status

**Archived experimental project**

This repository is preserved as a small demonstration of rule-based decision-support logic and Streamlit application development.
