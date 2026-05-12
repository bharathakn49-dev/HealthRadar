# HealthRadar

"AI-Powered Disease Prevention & Outbreak Intelligence Platform"  
Predict Early → Prevent Faster → Act Smarter

## Team
- **Team Name**: 404 THINKERS
- **Members**:
  - Bharatha K N
  - Bhargav S Acharya
  - Vibha D Naik
  - B S Keerthikumari

## Problem Statement
Current Public Health Systems Are Reactive:
- People get sick → Hospitals overflow → Government reacts → Too late
- Issues: Delayed outbreak response, preventable deaths, poor resource allocation, blind vaccine deployment, high-risk communities suffer more

## Solution
HealthRadar provides a comprehensive AI-powered platform for proactive disease prevention and outbreak intelligence.

## Core Features

### 1. Outbreak Detection Engine
Predict outbreaks early using clinical, weather, and air quality data.

### 2. Vulnerability Heatmap
Identify high-risk neighborhoods with interactive maps.

### 3. Clinical Monitoring Dashboard
Hospital reporting and validation system.

### 4. AI Recommendation Engine
Government action suggestions powered by local LLM.

## System Architecture
```
hospital_master.csv + clinical_reports.csv + weather_data.csv + aqi_data.csv
    ↓
Python Data Engine
    ↓
Local LLM (Ollama phi3)
    ↓
AI Recommendations
    ↓
Streamlit Dashboard
    ↓
Government Decision Support
```

## Technology Stack

### Frontend
- Streamlit
- Folium (maps)

### Backend
- Python
- Pandas (data processing)

### AI Layer
- Ollama (local LLM)
- Phi-3 model

### Data Sources
- CSV files (hospital, clinical reports, weather, AQI data)

## Prerequisites

### System Requirements
- Python 3.8+
- Ollama installed and running

### Local Models Needed
- **Phi-3**: A 3.8B parameter language model by Microsoft, optimized for local inference.
  - Download and install via Ollama: `ollama pull phi3`

## Installation

1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and setup Ollama**:
   - Download Ollama from [ollama.ai](https://ollama.ai)
   - Install it on your system
   - Pull the Phi-3 model:
     ```bash
     ollama pull phi3
     ```
   - Ensure Ollama is running in the background

4. **Data Setup**:
   - Ensure the following CSV files are present in `data/raw/`:
     - `hospital_master.csv`
     - `clinical_reports.csv`
     - `weather_data.csv`
     - `aqi_data.csv`

## How to Run

1. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the dashboard**:
   - Open your browser and go to `http://localhost:8501`
   - The EpiSense Dashboard will load with outbreak monitoring and AI recommendations

## Usage

- **Outbreak Dashboard**: View current outbreak data and predictions
- **Vulnerability Heatmap**: Interactive map showing high-risk areas
- **Clinical Monitoring**: Hospital status and patient data
- **AI Recommendations**: Get AI-powered suggestions for government actions

## Real-World Impact

HealthRadar helps governments:
- Prevent outbreaks early
- Reduce preventable deaths
- Optimize vaccines and resources
- Improve hospital readiness
- Protect vulnerable communities
- Transition from reactive to preventive healthcare

## Future Scope

- Real-time Google Trends integration
- Live AQI and weather APIs
- District-level government deployment
- Multilingual citizen alerts
- SMS outbreak warnings
- State-wide outbreak monitoring
- National disease intelligence platform
