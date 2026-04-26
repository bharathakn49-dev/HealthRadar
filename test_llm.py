from backend.llm_engine import get_ai_recommendation
from backend.data_loader import prepare_outbreak_summary

location = "KR Puram"
disease = "Dengue"

outbreak_data = prepare_outbreak_summary(location, disease)

result = get_ai_recommendation(outbreak_data)

print(result)