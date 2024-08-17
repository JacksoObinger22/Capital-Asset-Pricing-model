
# Capital Asset Pricing Model (CAPM)


https://github.com/user-attachments/assets/810a2344-dc34-4453-b0c0-e3a72916c0d3



![CAPM](https://user-images.githubusercontent.com/your_image_link.png)

## Overview

The **Capital Asset Pricing Model (CAPM)** project is designed to help users understand and apply the CAPM in real-world scenarios. The CAPM is a foundational concept in finance that describes the relationship between systematic risk and expected return for assets, particularly stocks. This project leverages Python, Streamlit, and various financial libraries to allow users to calculate and visualize key metrics like beta and alpha for a portfolio of stocks against a benchmark index (e.g., S&P 500).

## Features

- **Dynamic Data Download**: Download historical stock prices and market index data using Yahoo Finance.
- **Risk and Return Analysis**: Calculate daily returns, beta, and alpha for individual stocks relative to the market.
- **Interactive Visualizations**: Visualize stock returns, regression lines, and bar plots for beta values.
- **User-Friendly Interface**: Use Streamlit to create an interactive web app where users can input stock tickers, start dates, and end dates.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Concepts](#key-concepts)
- [Example Outputs](#example-outputs)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [yfinance](https://pypi.org/project/yfinance/)
- [Plotly](https://plotly.com/python/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shubh123a3/Capital-Asset-Pricing-model.git
   cd Capital-Asset-Pricing-model
   ```

2. **Install Dependencies**

   Use pip to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   Start the Streamlit app by running:

   ```bash
   streamlit run app.py
   ```

## Usage

1. **Input Stock Tickers**: Enter the stock tickers (e.g., AAPL, MSFT) separated by commas.
2. **Select Date Range**: Choose the start and end dates for your analysis.
3. **Download Data**: Click the button to download historical data.
4. **Analyze and Visualize**: View calculated beta, alpha, and regression plots. Additionally, see bar plots of beta values across different stocks.

## Project Structure

```plaintext
Capital-Asset-Pricing-model/
│
├── app.py                 # Main Streamlit application
├── helpers.py             # Helper functions for calculations and plotting
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation (this file)
└── data/                  # Directory to store downloaded data (optional)
```

## Key Concepts

### Capital Asset Pricing Model (CAPM)
CAPM is a model used to determine the expected return on an asset, given the risk-free rate, the asset's beta, and the expected market return.

\[ \text{Expected Return} = \text{Risk-Free Rate} + \beta \times (\text{Market Return} - \text{Risk-Free Rate}) \]

### Beta
Beta is a measure of an asset's volatility in relation to the overall market. A beta greater than 1 indicates the asset is more volatile than the market, while a beta less than 1 indicates less volatility.

### Alpha
Alpha represents the excess return of an asset over the expected return predicted by the CAPM. Positive alpha indicates outperformance, while negative alpha indicates underperformance.

## Example Outputs

### Beta and Alpha Calculation

```plaintext
Beta values:
AAPL: 1.2
MSFT: 1.1
TSLA: 2.3

Alpha values:
AAPL: 0.03
MSFT: 0.02
TSLA: 0.05
```

### Interactive Regression Plot

![Regression Plot](https://user-images.githubusercontent.com/your_image_link.png)

### Beta Value Bar Plot

![Beta Bar Plot](https://user-images.githubusercontent.com/your_image_link.png)

## Future Enhancements

- **Portfolio Optimization**: Extend the project to include Markowitz portfolio optimization.
- **Real-Time Data**: Integrate real-time stock data for live analysis.
- **Historical Risk-Free Rate**: Automate the fetching of historical risk-free rates.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

