[README_performance_trends.md](https://github.com/user-attachments/files/27129168/README_performance_trends.md)
# 📈 Performance Trend Analysis — Line & Bar Graph

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-green) ![Domain](https://img.shields.io/badge/Domain-Football%20Analytics-black)

## 📌 Overview
This project tracks and compares football player and team performance metrics across multiple matches using line graphs and bar charts. It helps identify form trends, performance peaks, and areas that need improvement over a season.

## 🎯 Objectives
- Track player statistics (goals, assists, distance) across match-weeks
- Compare team and player performance side by side
- Identify performance trends, slumps and peak form periods

## 🛠️ Tools & Libraries
| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| VS Code | Development environment |
| Matplotlib | Line graphs and bar charts |
| Pandas | Data handling and processing |

---

## 📊 Part 1 — Line Graph Analysis

### What it Shows
- Performance metrics plotted over time (match-week by match-week)
- Trend lines showing improvement or decline in form
- Multi-player comparison on the same graph

### Metrics Tracked
- Goals per match-week
- Assists per match-week
- Distance covered per match
- Pass accuracy over time

## 🖼️ Line Graph Output
> Multi-line graph showing player performance trends across an entire season.

---

## 📊 Part 2 — Bar Graph Analysis

### What it Shows
- Side-by-side comparison of player or team statistics
- Total goals, assists and key passes per player
- Team vs team statistical comparison

### Metrics Compared
- Total goals scored per player
- Shots on target vs total shots
- Pass completion rates by position
- Team statistics comparison across a match

## 🖼️ Bar Graph Output
> Grouped bar chart comparing key statistics across multiple players or teams.

---

## 📁 Project Structure
```
performance-trend-analysis/
│
├── data/
│   └── performance_data.csv    # Player/team stats across matches
├── line_graph.py               # Line graph analysis script
├── bar_graph.py                # Bar graph analysis script
├── output/
│   ├── line_graph_plot.png     # Line graph output
│   └── bar_graph_plot.png      # Bar graph output
└── README.md
```

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/shabab-analyst/performance-trend-analysis

# Install dependencies
pip install matplotlib pandas

# Run line graph analysis
python line_graph.py

# Run bar graph analysis
python bar_graph.py
```

## 💡 Key Insights
- Player form dropped significantly between match-weeks 8–12 before recovering
- Team A scored 40% more goals from open play compared to set pieces
- Midfielders covered on average 2km more per match than forwards

## 👤 Author
**Shabab** — Aspiring Sports Analyst | Kerala, India
- LinkedIn: linkedin.com/in/shabab-sports-analyst
- Email: shabab326@gmail.com
