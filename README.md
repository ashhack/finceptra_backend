# Finceptra

A GenAI-powered investment recommendation system that connects to various data sources to provide intelligent investment recommendations.

## Features

- Multiple data source connectors (Market Data, Financial Statements, News)
- AI-powered investment recommendations
- Risk profiling and portfolio analysis
- Extensible architecture for adding new data sources
- Comprehensive testing and CI/CD pipeline

## Installation

```bash
pip install finceptra
```

For development:

```bash
git clone https://github.com/yourusername/finceptra.git
cd finceptra
pip install -e .[dev]
```

## Usage

```python
from finceptra import RecommendationEngine
from finceptra.data_sources import MarketDataAPI, FinancialStatementsAPI, NewsAPI

# Initialize data sources
market_data = MarketDataAPI(api_key="your_api_key")
financials = FinancialStatementsAPI(api_key="your_api_key")
news = NewsAPI(api_key="your_api_key")

# Create recommendation engine
engine = RecommendationEngine(
    market_data=market_data,
    financials=financials,
    news=news
)

# Get investment recommendations
recommendations = engine.get_recommendations(
    risk_profile={
        "risk_tolerance": "medium",
        "investment_horizon": "5 years",
        "financial_goals": ["retirement", "wealth growth"]
    }
)
```

## Development

### Setup

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -e .[dev]
   ```
3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Testing

Run tests with coverage:
```bash
pytest --cov=finceptra
```

### Code Style

This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

Run all checks:
```bash
black .
isort .
flake8
mypy .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
