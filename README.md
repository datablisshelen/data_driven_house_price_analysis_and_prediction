# data_driven_house_price_analysis_and_prediction
A data analytics and AI project exploring residential house prices using Python, machine learning, and an interactive dashboard.

## Client Brief

The client is a **property analytics stakeholder** operating within the residential housing market who requires a **data-driven decision-support tool** to better understand the factors influencing house prices and to improve price estimation accuracy.

Currently, property valuation decisions rely heavily on manual appraisal, market intuition, or limited historical comparisons. These approaches can be inconsistent, slow to adapt to market changes, and prone to bias. The client requires a **transparent, explainable, and interactive analytics solution** that transforms historical housing data into actionable insights.

### Client Needs

- Understand which property features most strongly influence sale prices  
- Explore patterns, trends, and anomalies within historical housing data  
- Access predictive price estimates based on comparable property characteristics  
- Communicate insights clearly to both technical analysts and non-technical decision-makers  

The solution must adhere to **ethical data practices**, use **publicly available and anonymised data**, and be delivered through an **accessible web-based dashboard** that supports exploration, interpretation, and future extension.

---

## Project Aim

The aim of this project is to design and deliver a **Data Analytics Web Application** that applies **statistical analysis, machine learning, and data visualisation techniques** to analyse and predict residential property sale prices.

Using Python-based data analytics tools and a Streamlit user interface, the project will:

- Perform exploratory data analysis (EDA) to identify key drivers of house prices  
- Apply statistical methods to summarise, compare, and interpret housing features  
- Develop and evaluate predictive models to estimate property sale values  
- Present insights through interactive visualisations and narratives tailored to different audiences  
- Demonstrate responsible data handling, including data cleaning, transformation, and documentation  
- Integrate generative AI tools to support ideation, analysis, and data storytelling  

The final outcome is a **publishable, professional-grade dashboard** that supports informed decision-making in the housing domain while clearly evidencing all required learning outcomes (LO1–LO11) of the **Data Analytics with Artificial Intelligence Bootcamp**.

---

## Hackathon Delivery Model

This project follows a **3-person, 3-day hackathon**, with one designated lead. Roles and responsibilities are explicitly mapped to the **Data Analytics with AI Bootcamp Learning Outcomes (LO1–LO11)** to maximise assessment coverage, avoid duplication, and mitigate assessment risk.

---

## Team Structure (Fixed for All 3 Days)

### 1. Project Lead / Product Owner (Person A – Lead)

**Primary accountability:** Coherence, assessment coverage, business rationale, and final submission quality.  
This role orchestrates delivery and provides final sign-off.

**Primary Learning Outcomes Owned:**  
- LO3, LO7, LO8, LO9, LO10, LO11 (final sign-off on all LOs)

---

### 2. Data & Modelling Engineer (Person B)

**Primary accountability:** Data integrity, analysis correctness, modelling, and statistics.

**Primary Learning Outcomes Owned:**  
- LO1, LO2, LO3, LO5

---

### 3. Dashboard & UX Engineer (Person C)

**Primary accountability:** Streamlit application, visualisations, UX, accessibility, and storytelling.

**Primary Learning Outcomes Owned:**  
- LO2, LO4, LO8

---

## Day-by-Day Breakdown (With Explicit Deliverables)

### DAY 1 — Foundations & Direction (Critical)

**Goal:** Lock scope, dataset, structure, and eliminate ambiguity early.

#### Project Lead (Person A)

**Responsibilities**
- Finalise project idea aligned to a real-world user need  
- Define target audience and business problem  
- Select and approve a public, anonymised, assessable dataset  
- Create GitHub repository structure:

- Draft README skeleton:
- Purpose  
- Business Case  
- Target Audience  
- Hypotheses (mandatory)  
- Project Plan (LO10)

**Learning Outcomes Covered**
- LO3 – Problem framing  
- LO7 – Project organisation  
- LO9 – Domain relevance  
- LO10 – Planning  

---

#### Data & Modelling Engineer (Person B)

**Responsibilities**
- Load dataset into Jupyter Notebook  
- Perform:
- Initial EDA  
- Missing value analysis  
- Feature overview  
- Implement core statistics:
- Mean, median, variance, standard deviation  
- Probability and distributions  
- Save cleaned dataset to `/data/processed/`

**Deliverables**
- `01_eda_and_statistics.ipynb`  
- Cleaned CSV with documented pipeline  

**Learning Outcomes Covered**
- LO1 – Statistics & probability  
- LO2 – Python data manipulation  
- LO5 – Data management  

---

#### Dashboard & UX Engineer (Person C)

**Responsibilities**
- Scaffold Streamlit app:
- Navigation  
- Page layout  
- Placeholder visuals  
- Identify at least four plot types (e.g. bar, line, box, scatter, map)  
- Implement basic accessibility:
- Labels  
- Tooltips  
- Clear information hierarchy  

**Deliverables**
- Running Streamlit app with dummy data  
- Documented UI/wireframe decisions  

**Learning Outcomes Covered**
- LO8 – Communication  
- UX & accessibility requirements  

---

### DAY 2 — Analysis, AI Integration & Insight Generation

**Goal:** Produce assessable analytics and intelligence.

#### Project Lead (Person A)

**Responsibilities**
- Write methodology narrative:
- Why these methods?  
- Why these visuals?  
- Draft Ethics & Governance section:
- Bias  
- Privacy  
- GDPR considerations  
- Ensure AI usage is explicitly documented  

**Learning Outcomes Covered**
- LO6 – Ethics  
- LO7 – Methodology  
- LO11 – Reflection on tools  

---

#### Data & Modelling Engineer (Person B)

**Responsibilities**
- Implement at least one model:
- Regression / classification / clustering  
- Evaluate model:
- Metrics  
- Limitations  
- Alternatives  
- Explicitly document AI assistant usage (e.g. Copilot, ChatGPT)  
- Save results for dashboard integration  

**Deliverables**
- `02_modelling.ipynb`  
- Metrics table  
- Commentary markdown cells  

**Learning Outcomes Covered**
- LO2 – Advanced analysis  
- LO3 – Problem solving  
- LO4 – AI-enhanced analysis  

---

#### Dashboard & UX Engineer (Person C)

**Responsibilities**
- Replace placeholders with real data  
- Integrate:
- Interactive filters  
- Hover tooltips  
- Clear narrative flow  
- Add clearly labelled AI-generated insight summary  

**Deliverables**
- Polished Streamlit dashboard  
- At least four meaningful plot types  

**Learning Outcomes Covered**
- LO4 – AI storytelling  
- LO8 – Visual communication  

---

### DAY 3 — Polish, Evidence & Submission Readiness

**Goal:** Remove assessor doubts.

#### Project Lead (Person A)

**Responsibilities**
- Finalise README:
- Hypotheses validation  
- Limitations  
- Future roadmap  
- Maintenance & updates (LO10)  
- Verify all learning outcomes are explicitly evidenced  
- Review git history:
- Small, logical commits  
- Clear messages  

**Learning Outcomes Covered**
- LO8 – Documentation  
- LO10 – Lifecycle planning  
- LO11 – Continuous learning  

---

#### Data & Modelling Engineer (Person B)

**Responsibilities**
- Final code clean-up:
- Docstrings  
- Comments  
- Reproducibility  
- Validate statistical outputs  
- Ensure notebooks run end-to-end  

**Learning Outcomes Covered**
- LO1–LO5 robustness  

---

#### Dashboard & UX Engineer (Person C)

**Responsibilities**
- Final UX pass:
- Accessibility  
- Consistency  
- Error handling  
- Ensure the dashboard communicates insights independently  

**Learning Outcomes Covered**
- LO8 – Non-technical communication  
- UX compliance  

---

## Accountability Matrix (Condensed)

| Learning Outcome | Owner |
|---|---|
| LO1 – Statistics | Person B |
| LO2 – Python & Tools | Person B / Person C |
| LO3 – Problem Analysis | Person A / Person B |
| LO4 – AI Usage | Person B / Person C |
| LO5 – Data Management | Person B |
| LO6 – Ethics | Person A |
| LO7 – Research Design | Person A |
| LO8 – Communication | Person C |
| LO9 – Domain Context | Person A |
| LO10 – Planning | Person A |
| LO11 – Reflection & Adaptation | All (compiled by Person A) |

---

## Key Hackathon Rule

**No one “helps” casually.**  
Each task has **one clear owner**. Others may review but not rewrite. This protects against:

- Plagiarism concerns  
- Git history ambiguity  
- Assessment gaps  