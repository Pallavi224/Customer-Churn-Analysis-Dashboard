# Customer Churn Analysis Dashboard

A comprehensive Streamlit-based dashboard for analyzing customer churn patterns and identifying key drivers of customer attrition. This tool helps businesses understand churn behavior, segment customers, and make data-driven retention decisions.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Data Format](#data-format)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Troubleshooting](#troubleshooting)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

This dashboard provides interactive visualizations and analytics for understanding customer churn patterns. It enables you to:

- Identify at-risk customer segments
- Analyze churn drivers and correlations
- Track customer behavior metrics
- Make informed business decisions based on data insights

**Perfect for:** Data analysts, business intelligence teams, and customer success managers.

## Features

- **Churn Distribution Analysis** - Visualize overall churn rates and trends
- **Demographic Breakdown** - Analyze churn patterns by gender, subscription type, and other segments
- **Support Impact Analysis** - Understand correlation between support calls and churn rates
- **Financial Analysis** - Explore relationship between customer spend and churn behavior
- **Interactive Filters** - Dynamic filtering by customer segments, time periods, and metrics
- **Custom Visualizations** - Multiple chart types (histograms, scatter plots, bar charts) for comprehensive insights
- **Exportable Reports** - Generate and download analysis summaries

## Project Structure

```
Customer-Churn-Analysis-Dashboard/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── app.py                   # Main Streamlit application
├── data/                    # Data directory (if applicable)
│   └── sample_data.csv      # Sample dataset for testing
├── src/                     # Source code modules
│   ├── analysis.py          # Analysis functions
│   ├── visualizations.py    # Chart and visualization code
│   └── utils.py             # Utility functions
└── assets/                  # Images and static files
    └── dashboard_preview.png # Dashboard screenshot
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Pallavi224/Customer-Churn-Analysis-Dashboard.git
cd Customer-Churn-Analysis-Dashboard
```

2. **Create a virtual environment (recommended):**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n churn-dashboard python=3.9
conda activate churn-dashboard
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Data Format

### Expected CSV Structure

Your data should be in CSV format with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | string | Unique customer identifier |
| `gender` | string | Customer gender (M/F) |
| `subscription_type` | string | Type of subscription (Basic/Standard/Premium) |
| `support_calls` | integer | Number of support calls made |
| `total_spend` | float | Total customer spending |
| `churn` | binary | Churn status (0=retained, 1=churned) |
| `tenure_months` | integer | Customer tenure in months |

### Loading Data

Place your CSV file in the `data/` directory or modify the data path in `app.py`:

```python
df = pd.read_csv('data/your_data.csv')
```

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root:

```bash
# Streamlit configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost

# Data path
DATA_PATH=data/sample_data.csv

# Display settings
THEME=light  # or 'dark'
```

### Streamlit Config

Customize Streamlit settings in `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## Usage Guide

### Running the Dashboard

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Basic Workflow

1. **Load Data** - Upload or select your CSV file
2. **Explore Overview** - View summary statistics and churn rates
3. **Filter Results** - Use sidebar filters to segment your data
4. **Analyze Patterns** - Examine visualizations by different dimensions
5. **Export Insights** - Download charts or summary reports

### Example Queries

- "What's the churn rate for customers with more than 3 support calls?"
- "How does churn differ between subscription types?"
- "What's the correlation between total spend and churn?"

## Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'streamlit'"**
- **Solution:** Ensure you've activated your virtual environment and installed requirements:
  ```bash
  pip install -r requirements.txt
  ```

**Issue: "FileNotFoundError: data/sample_data.csv"**
- **Solution:** Verify the data file path in `app.py` matches your actual file location
- Check that the file exists: `ls data/` or `dir data\` (Windows)

**Issue: "Port 8501 already in use"**
- **Solution:** Run on a different port:
  ```bash
  streamlit run app.py --server.port 8502
  ```

**Issue: Dashboard is slow or unresponsive**
- **Solution:** Try restarting Streamlit with caching enabled
- Check that your CSV file isn't too large (>500MB)
- Reduce the date range if filtering large datasets

### Debug Mode

Enable verbose logging:
```bash
streamlit run app.py --logger.level=debug
```

## Deployment

### Local Deployment

Already covered in the [Usage Guide](#usage-guide).

### Cloud Deployment

#### Streamlit Cloud (Recommended - Free)

1. Push your repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" and select your repository
4. Configure the main file as `app.py`
5. Deploy!

[Streamlit Cloud Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)

#### Heroku

1. Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

#### Docker

1. Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

2. Build and run:
```bash
docker build -t churn-dashboard .
docker run -p 8501:8501 churn-dashboard
```

## Contributing

Contributions are welcome! Here's how you can help:

### Steps to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Contribution Areas

- Bug fixes and performance improvements
- New visualization types
- Additional analysis features
- Documentation improvements
- Data processing optimizations

Please ensure your code follows PEP 8 style guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support & Feedback

- **Issues:** [Report a bug](https://github.com/Pallavi224/Customer-Churn-Analysis-Dashboard/issues)
- **Discussions:** [Start a discussion](https://github.com/Pallavi224/Customer-Churn-Analysis-Dashboard/discussions)
- **Email:** [Your contact info]

## Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Data visualization with [Plotly](https://plotly.com) and [Seaborn](https://seaborn.pydata.org)
- Data processing with [Pandas](https://pandas.pydata.org)

---

**Last Updated:** 2026-04-19 08:21:51
