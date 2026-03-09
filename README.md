# TelemetryX
web-based analytics dashboard that automatically collects Formula 1 race data and presents it through interactive visualizations.



DataFlow of TelemetryX
FastF1 API
     ↓
fetch_data.py
     ↓
preprocess.py
     ↓
analysis.py
     ↓
visualization.py
     ↓
Dash dashboard