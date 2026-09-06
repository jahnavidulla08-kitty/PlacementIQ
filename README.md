# PlacementIQ
### Smart Placement Analytics & Prediction Dashboard
> **Tagline:** *From Placement Data to Career Intelligence*

---

## 📌 Project Overview
**PlacementIQ** is an end-to-end college hackathon prototype engineered to transform raw campus placement data into actionable intelligence for both **Students** and **Placement Officers**.

Unlike static dashboards, PlacementIQ is built on live database records and an actual trained **Random Forest Machine Learning model** that dynamically calculates placement probabilities, assesses skill gaps against recruiter criteria, matches students to top hiring partners, and triages at-risk candidates for targeted academic intervention.

---

## 🚀 Key Features

### 🏢 1. Placement Officer Intelligence Hub
- **Dynamic KPI Cards:** Total Students (360), Eligible Candidates (CGPA ≥ 6.0, 0 backlogs), Placed Students, Overall Placement Conversion %, Recruiting Partners (20), Average CTC (12.75 LPA), and Highest Dream CTC (38.31 LPA).
- **Multi-Filter Toolbar:** Slice and dice real-time metrics by Academic Batch Year (2023, 2024, 2025, 2026), Department (CSE, IT, ECE, EEE, MECH, CIVIL), and Recruiter.
- **6 Dynamic Analytics Visualizations (Recharts):**
  1. *Placement Trend:* Multi-year placement percentage and average salary progression.
  2. *Department Comparison:* Placement conversion rates across all 6 engineering branches.
  3. *Salary Distribution:* Offer volume across package tiers (3–6 LPA, 6–10 LPA, 10–15 LPA, 15–22 LPA, 22+ LPA).
  4. *Company Hiring:* Campus recruitment volume per corporate partner.
  5. *Placement Status:* Placed vs Unplaced student ratio donut chart.
  6. *Skill Demand:* Most in-demand technical competencies across all companies.
- **Students Directory:** Searchable and filterable student roster with detailed profile drawer.
- **Department Analytics:** Branch-wise metrics, average/highest CTC, and top recruiters.
- **Partner Companies:** Corporate directory with CTC packages, minimum CGPA cutoffs, required skills, and alumni hire histories.
- **Campus Skill Intelligence:** Campus-wide competency supply vs industry demand matrix.
- **At-Risk Student Triage:** Prioritized candidate triage (HIGH, MEDIUM, LOW risk) with transparent root concerns and constructive remediation plans.

### 🎓 2. Student Career Intelligence Portal
- **Academic & Skills Profile:** Verified CGPA, 10th/12th board marks, coding assessment, quantitative aptitude, communication score, projects, internships, and certifications.
- **Placement Readiness Score Gauge:** Animated SVG radial gauge displaying readiness percentage (e.g., `86%`), placement probability, confidence level, and contextual disclaimer.
- **Explainable AI Factors:** Positive and negative factors influencing the candidate's prediction.
- **Interactive "What-If" Trajectory Simulator:** Real-time parameter sliders allowing students to simulate profile upgrades (raising coding score, clearing backlogs, adding internships) to observe instant impact on readiness score.
- **Skill Gap Engine:** Compare verified student skills against specific target companies or overall market benchmarks to reveal missing competencies and tailored learning roadmaps.
- **Top 5 Company Recommendations:** Multi-criteria matched companies with transparent percentage match scores (e.g., `94% Match — Google`) and explicit explanations for why the company fits the candidate.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React.js (v19), Vite (v8), Tailwind CSS (v4), Recharts, Axios, Lucide React |
| **Backend** | Python 3.12, FastAPI, SQLAlchemy, Uvicorn, Pydantic |
| **Database** | SQLite (`placement_data.db`) |
| **Machine Learning** | Scikit-learn (Random Forest Classifier), Pandas, NumPy, Joblib |

---

## 📁 Project Structure

```
PlacementIQ/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                     # FastAPI entrypoint, CORS, startup auto-seed
│   │   ├── database.py                 # SQLite connection & session management
│   │   ├── models.py                   # SQLAlchemy ORM models (Students, Skills, Companies, Placements)
│   │   ├── schemas.py                  # Pydantic response & request validation models
│   │   ├── seed.py                     # Synthetic dataset generator (360 students, 20 companies, 18 skills)
│   │   ├── routers/
│   │   │   ├── auth.py                 # Demo login & user profile router
│   │   │   ├── dashboard.py            # Officer KPI stats, trends & department analytics
│   │   │   ├── students.py             # Filterable student roster & profile drawer
│   │   │   ├── companies.py            # Corporate partner directory & alumni hires
│   │   │   ├── skills.py               # Market skill demand & student skill gaps
│   │   │   ├── predictions.py          # ML readiness score, simulator & company recommendations
│   │   │   └── at_risk.py              # At-risk candidate classification & remediation
│   │   └── services/
│   │       ├── ml_service.py           # Feature extraction & Random Forest inference engine
│   │       ├── recommendation_service.py # Multi-criteria company match scoring
│   │       └── risk_service.py         # At-risk student heuristics & triage
│   └── requirements.txt
├── ml/
│   ├── train.py                        # Standalone ML training script
│   ├── placement_model.pkl             # Trained Random Forest Classifier
│   ├── scaler.pkl                      # Feature standard scaler
│   └── model_metrics.json              # Accuracy (88.5%), Precision, Recall, F1 & Feature Importances
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx              # Top bar, demo role switcher, student picker, notifications, theme
│   │   │   ├── Sidebar.jsx             # Role-aware navigation menu
│   │   │   ├── KPICard.jsx             # Metric card with gradient accents
│   │   │   ├── FilterBar.jsx           # Batch year, branch & company filter toolbar
│   │   │   ├── ReadinessGauge.jsx      # Radial progress gauge with disclaimer
│   │   │   └── WhatIfSimulator.jsx     # Interactive live parameter simulator
│   │   ├── pages/
│   │   │   ├── LandingPage.jsx         # Hackathon intro & one-click portal launchers
│   │   │   ├── LoginPage.jsx           # Demo credentials login
│   │   │   ├── OfficerDashboard.jsx    # Executive overview with 6 dynamic charts
│   │   │   ├── OfficerStudents.jsx     # Student directory with search & profile modal
│   │   │   ├── OfficerDepartments.jsx  # 6-department comparative intelligence
│   │   │   ├── OfficerCompanies.jsx    # Recruiter directory with packages & alumni hires
│   │   │   ├── OfficerSkills.jsx       # Campus-wide skill demand vs supply matrix
│   │   │   ├── OfficerAtRisk.jsx       # Triage station with priority classifications
│   │   │   ├── StudentDashboard.jsx    # Student central hub & readiness score
│   │   │   ├── StudentProfile.jsx      # Full academic, coding & skill record
│   │   │   ├── StudentPrediction.jsx   # Deep ML explanation & What-If simulator
│   │   │   ├── StudentSkillGap.jsx     # Target company skill comparison & roadmap
│   │   │   └── StudentRecommendations.jsx # Top 5 matched companies with match rationale
│   │   ├── context/
│   │   │   └── AuthContext.jsx         # Global authentication and active filter state
│   │   ├── services/
│   │   │   └── api.js                  # Axios client calling FastAPI backend
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── data/
│   └── placement_data.db               # SQLite database with 360 students & 4 years of history
└── README.md
```

---

## 🏃 Quick Start Guide

### Prerequisites
- Python 3.10+ (or Python 3.12)
- Node.js 18+ (or Node 20/22)

---

### Step 1: Start Backend Server
```powershell
# Navigate to project root
cd PlacementIQ

# Install backend dependencies
pip install -r backend/requirements.txt

# Seed the database and train the ML model
python ml/train.py

# Start the FastAPI server on port 8000
uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload
```
*The FastAPI backend will start at: `http://127.0.0.1:8000` (Interactive Swagger Docs: `http://127.0.0.1:8000/docs`).*

---

### Step 2: Start Frontend Web App
```powershell
# Open a new terminal in frontend directory
cd frontend

# Install dependencies
npm install

# Start Vite dev server
npm run dev
```
*Open your browser and visit: `http://localhost:5173`.*

---

## 👥 Demo User Credentials

The application includes built-in one-click role switching in the top navigation bar:

| Role | Email | Description |
|---|---|---|
| **Placement Officer** | `officer@demo.com` | Full access to executive analytics, department trends, company drives, skill demand, and at-risk triage. |
| **Student (Alex Mercer)** | `student@demo.com` | Access to student portal with AI placement readiness score, What-If simulator, skill gaps, and top 5 matching companies. |

*(You can also use the **Student Selector Dropdown** in the top navigation to instantly explore other student profiles across CSE, IT, ECE, EEE, MECH, and CIVIL branches!)*

---

## 🤖 Machine Learning Model Details

- **Model Type:** Scikit-learn `RandomForestClassifier` (120 Estimators, Class-balanced)
- **Features Used (12):**
  1. `cgpa` (Academic cumulative GPA)
  2. `tenth_percentage` (Secondary school marks)
  3. `twelfth_percentage` (Higher secondary marks)
  4. `backlogs` (Active standing backlogs)
  5. `attendance` (Classroom attendance %)
  6. `coding_score` (Technical coding assessment index)
  7. `aptitude_score` (Quantitative & logical reasoning score)
  8. `communication_score` (Soft skill & interview score)
  9. `projects` (Verified portfolio projects)
  10. `internships` (Industry internship count)
  11. `certifications` (Technical certifications)
  12. `num_skills` (Total verified skills count)
- **Evaluation Metrics:**
  - **Accuracy:** `88.5%`
  - **Precision:** `87.2%`
  - **Recall:** `89.4%`
  - **F1 Score:** `88.3%`
- **Top Predictive Features:** Coding Score (24.5%), CGPA (22.8%), Active Backlogs (14.2%), Aptitude Score (11.5%).

---

## 🏆 Hackathon Demonstration Flow

1. **Landing Page (`/`):**
   - Review hero branding, project tagline, and feature cards.
   - Click **"Placement Officer Portal"** to log in as Officer.
2. **Officer Demonstration:**
   - **Executive Dashboard:** Inspect the 7 top KPI cards, Placement Trend line chart, Department placement comparison, Salary distribution, Company hiring volume, Placed/Unplaced donut chart, and Skill Demand bar chart.
   - **Interactive Filtering:** Toggle Academic Year to `2025` or Department to `CSE` to watch all 6 charts dynamically recalculate from the database.
   - **Student Directory:** Search for students, filter by status, and click **"Profile"** to open the student drawer.
   - **Department Analytics:** Explore the 6 branch cards with placement conversion rates and top recruiters.
   - **Partner Companies:** Review the 20 corporate partners (Google, Microsoft, Amazon, Cisco, Qualcomm, etc.), packages, and alumni hires.
   - **Campus Skill Intelligence:** Review campus skill demand vs supply deficit matrix.
   - **At-Risk Triage:** Inspect High, Medium, and Low risk students with root concerns and constructive remediation actions.
3. **Student Demonstration:**
   - Click the **"Student"** toggle in the top navbar.
   - **Placement Central:** View the large circular **Placement Readiness Score** (e.g. `86% Ready`), probability, and AI factors.
   - **AI What-If Simulator:** Open the simulator, adjust coding score slider from 65 to 90, and observe the simulated score jump from `72%` to `89%`.
   - **Skill Gap Analysis:** Select `Google` or `Cisco` from the dropdown to view matched vs missing skills and the 4-week remediation roadmap.
   - **Top 5 Company Matches:** Inspect top 5 recommended companies with match scores (e.g. `94% Match`) and itemized match reasons.

---

## 📄 License
Developed for Hackathon Prototype Demonstration.
