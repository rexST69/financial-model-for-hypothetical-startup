# Financial Model for Indian Tech YouTube Startup

A comprehensive 3-year financial projection model for a hypothetical Indian tech YouTube channel, built with Python. This model generates detailed revenue projections, cash flow analysis, and scenario analyses for a YouTube startup focused on AI/tech content.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Framework](#model-framework)
- [Key Assumptions](#key-assumptions)
- [Output & Reports](#output--reports)
- [Scenario Analysis](#scenario-analysis)
- [Example Output](#example-output)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## 📊 Overview

This project provides a sophisticated financial modeling toolkit for analyzing the viability of a YouTube-based tech startup in India. It accounts for:

- **Revenue Streams**: AdSense earnings + Channel Membership subscriptions
- **Operational Cost Structure**: Editor, scriptwriter, and AI software expenses
- **Timing Constraints**: YouTube Partner Program (YPP) activation delays and AdSense payment thresholds
- **Cash Flow Dynamics**: Month-by-month cash position tracking, runway analysis, and valley-of-death identification

The model generates professional financial statements (Income Statement, Balance Sheet, Cash Flow Statement) and provides scenario analysis to evaluate business viability and valuation.

---

## ✨ Features

### 1. **Comprehensive Financial Projections**
   - 36-month detailed revenue projections with compound month-on-month growth
   - Separate tracking of AdSense and subscription revenue streams
   - YouTube's 30% cut on memberships factored into calculations
   - AdSense payment threshold logic (₹8,600 minimum buffering)

### 2. **Cash Flow Analysis**
   - Month-by-month closing balance calculations
   - Runway analysis (months of cash remaining at current burn rate)
   - Capital expenditure tracking (equipment investment)
   - Identification of "Valley of Death" (minimum cash point)
   - Financing gap analysis

### 3. **Professional Financial Statements**
   - **Income Statement**: 3-year revenue, EBITDA, EBIT, and net income
   - **Balance Sheet**: Assets, liabilities, and equity position
   - **Cash Flow Statement**: Operating, investing, and financing cash flows
   - Tax calculations (25% on positive profits)
   - Depreciation schedules for equipment

### 4. **Scenario & Sensitivity Analysis**
   - Base case valuation using revenue multiples (4x standard for SaaS/AI)
   - Downside scenario: 50% reduction in membership conversion rate
   - Impact quantification on revenue and enterprise valuation

### 5. **Professional Visualizations**
   - **Cash Runway Chart**: 24-month visualization highlighting the valley of death
   - **Revenue Mix Chart**: Stacked annual breakdown of AdSense vs. subscription revenue
   - Exported as high-resolution PNG (300 DPI)

### 6. **Excel Export**
   - Multi-worksheet workbook (`Model_Rextea.xlsx`)
   - Separate sheets for assumptions, revenue build, cash budget, and annual pro forma statements

---

## 📁 Project Structure

```
financial-model-for-hypothetical-startup/
├── README.md                              # Project documentation
├── LICENSE                                # Project license
├── startup_model.py                       # Main financial modeling code
├── Model_Rextea.xlsx                      # Generated Excel workbook (output)
└── Financial_Analysis_Charts.png          # Generated visualization (output)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/rexST69/financial-model-for-hypothetical-startup.git
   cd financial-model-for-hypothetical-startup
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install pandas matplotlib tabulate openpyxl
   ```

   **Required packages**:
   - `pandas` - Data manipulation and analysis
   - `matplotlib` - Data visualization
   - `tabulate` - Pretty-print tabular data
   - `openpyxl` - Excel workbook manipulation

---

## 💻 Usage

### Basic Execution

Run the model from the command line:

```bash
python startup_model.py
```

### Output

The script will display:

1. **Assumptions Table** - All input parameters in formatted tables
2. **Revenue Projections** - First 12 months of detailed revenue breakdown
3. **Cash Budget & Runway Analysis** - 12-month cash flow and runway metrics
4. **3-Year Income Statement** - Aggregate financial performance
5. **Valuation Analysis** - Enterprise valuation using revenue multiples
6. **Scenario Testing** - Downside case analysis with sensitivity metrics
7. **Files Generated**:
   - `Model_Rextea.xlsx` - Multi-sheet Excel workbook
   - `Financial_Analysis_Charts.png` - Professional charts

---

## 🏗️ Model Framework

### Architecture Overview

```python
class StartupModel:
    ├── __init__()                           # Initialize with assumptions
    ├── print_assumptions()                  # Display all parameters
    ├── get_assumption()                     # Query specific assumptions
    ├── generate_revenue_projections()       # Create 36-month revenue forecast
    ├── calculate_monthly_cash_flow()        # Track cash position & runway
    ├── generate_annual_statements()         # Financial statements & Excel export
    └── run_scenario_analysis()              # Valuation & sensitivity analysis
```

### Core Modules

#### 1. **Revenue Projection Engine**
- Calculates monthly views with compound 15% month-on-month growth
- Applies YPP activation delay (6 months before earning AdSense)
- Converts views to AdSense revenue at ₹250 per 1,000 views
- Estimates subscriptions at 0.2% conversion rate × ₹299 price
- Applies YouTube's 30% revenue cut on memberships

#### 2. **Cash Flow Tracker**
- Tracks opening balance, inflows, outflows, and closing balance
- Implements AdSense buffering logic (accumulates until ₹8,600 threshold)
- Calculates runway = closing balance / monthly OpEx
- Identifies financing gaps and valley of death

#### 3. **Financial Statement Generator**
- Aggregates monthly data into annual periods
- Calculates EBITDA, depreciation, EBIT, taxes, and net income
- Generates balance sheet with depreciation schedules
- Produces cash flow statement with operating/investing/financing breakdown

#### 4. **Scenario Analysis Engine**
- Base case: Current assumptions
- Downside case: 50% reduction in membership conversion (0.1% vs. 0.2%)
- Calculates valuation impact and percentage changes
- Generates comparison tables and visualizations

---

## 📈 Key Assumptions

All assumptions are centralized in the `ASSUMPTIONS` dictionary:

### Revenue Drivers
| Parameter | Value | Description |
|-----------|-------|-------------|
| Initial Monthly Views | 5,000 | Starting audience size |
| MoM Growth Rate | 15% | Monthly compound growth rate |
| AI Niche RPM | ₹250 | Revenue per 1,000 views |
| Membership Price | ₹299 | Monthly subscription cost |
| Conversion Rate | 0.2% | % of viewers becoming members |

### Operational Costs (Monthly)
| Cost Category | Amount | Purpose |
|---------------|--------|---------|
| Freelance Editor | ₹15,000 | Video editing |
| Scriptwriter | ₹10,000 | Content creation |
| AI Software Suite | ₹4,500 | Tools (Runway, Synthesia, etc.) |
| **Total Monthly OpEx** | **₹29,500** | |

### Capital Expenditure (One-Time)
| Item | Cost |
|------|------|
| Gear Investment | ₹150,000 | Microphone, lighting, backdrop, etc. |

### Timing Logic
| Parameter | Value |
|-----------|-------|
| YPP Activation Delay | 6 months |
| AdSense Payment Threshold | ₹8,600 |
| Starting Cash | ₹200,000 |

### Financial Assumptions
| Parameter | Value |
|-----------|-------|
| Depreciation Rate | 20% straight-line |
| Tax Rate | 25% (on positive profits) |
| Valuation Multiple | 4x Revenue |

---

## 📊 Output & Reports

### Console Output

When you run the script, it displays formatted tables for:

1. **Assumptions Summary**
   - Organized by category (revenue, costs, timing)
   - Color-coded with emojis for quick scanning

2. **Revenue Projections (First 12 Months)**
   - Monthly views with growth trajectory
   - AdSense revenue (after YPP activation)
   - Subscription metrics and revenue
   - Total monthly revenue

3. **Cash Budget & Runway (12 Months)**
   - Opening/closing balances
   - AdSense buffer tracking
   - Monthly runway calculation
   - Valley of Death identification

4. **3-Year Income Statement**
   - Revenue by source (AdSense, subscriptions)
   - EBITDA, depreciation, EBIT
   - Tax and net income
   - Key metrics totaled

### Excel Export: `Model_Rextea.xlsx`

Multi-sheet workbook with:

**Sheet 1 - Assumptions**
- All input parameters in tabular format
- Easy to modify for sensitivity testing

**Sheet 2 - Revenue_Build**
- First 12 months of revenue details
- Useful for monthly planning

**Sheet 3 - Cash_Budget**
- Month-by-month cash flow
- Runway analysis per month

**Sheet 4 - Annual_Pro_Forma**
- Income Statement (rows 1-3)
- Balance Sheet (rows 6-8)
- Cash Flow Statement (rows 11-13)

### Visualization: `Financial_Analysis_Charts.png`

**Chart 1: Cash Runway Analysis (24 Months)**
- Line chart of closing cash balance
- Highlights valley of death with annotation
- Shows break-even point and financing needs
- Useful for identifying at what point external funding is needed

**Chart 2: Revenue Mix (Annual Breakdown)**
- Stacked bar chart showing AdSense vs. subscriptions
- Annual aggregation for years 1-3
- Value labels showing component and total revenue

---

## 🔍 Scenario Analysis

The model includes a built-in sensitivity analysis comparing:

### Base Case
- All assumptions at stated values
- Membership conversion: 0.2%
- 3-year revenue trajectory

### Downside Case ("Founder Pain Scenario")
- Membership conversion reduced by 50% to 0.1%
- All other assumptions unchanged
- Impact on Year 3 revenue and enterprise valuation

### Metrics Reported
- Revenue change percentage
- Valuation change (₹ amount and %)
- Visual comparison tables

---

## 📋 Example Output

### Sample Console Output

```
================================================================================
FINANCIAL MODEL ASSUMPTIONS - INDIAN TECH YOUTUBE STARTUP
================================================================================

📊 REVENUE DRIVERS
───────────────────────────────────────────────────────────────────────────────
Parameter                     Value
────────────────────────────┬───────────────────────────────────────────────────
Initial Monthly Views       │ 5,000
Month-on-Month Growth       │ 15.0%
AI Niche RPM                │ ₹250
Membership Price            │ ₹299
Membership Conversion Rate  │ 0.20%

💰 OPERATIONAL COSTS (Monthly)
───────────────────────────────────────────────────────────────────────────────
Cost Category           Amount
─────────────────────┬─────────────────
Freelance Editor      │ ₹15,000
Scriptwriter          │ ₹10,000
AI Software Suite     │ ₹4,500
TOTAL MONTHLY OPEX    │ ₹29,500
```

### Sample Generated Files

**Excel Workbook**: `Model_Rextea.xlsx`
- Professional, cell-formatted financial statements
- Multiple scenarios on separate sheets
- Ready for presentation or investor discussions

**Visualization**: `Financial_Analysis_Charts.png`
- High-quality (300 DPI) charts
- Professional fonts and coloring
- Suitable for presentations or reports

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3** | Core language |
| **Pandas** | Data manipulation, financial calculations |
| **Matplotlib** | Chart generation and visualization |
| **Tabulate** | Formatted table output |
| **OpenPyXL** | Excel workbook creation |

---

## 🎯 Key Insights from the Model

1. **Valley of Death**: Most YouTube channels face a critical cash shortage period before reaching profitability. This model identifies when external funding is needed.

2. **Revenue Diversification**: The model shows how important membership revenue becomes relative to AdSense, especially as the channel grows.

3. **Timing Sensitivity**: The 6-month delay before YPP activation has a significant impact on Year 1 cash flow and the financing requirement.

4. **Scenario Planning**: By testing sensitivity to key assumptions (like membership conversion), founders can understand which metrics drive business viability.

5. **Valuation**: Using a 4x revenue multiple (standard for SaaS/AI startups), Year 3 revenue translates to a potential enterprise valuation.

---

## 📝 Customization

To run your own scenario, modify the `ASSUMPTIONS` dictionary in `startup_model.py`:

```python
ASSUMPTIONS = {
    "revenue_drivers": {
        "initial_monthly_views": 10_000,  # Change starting audience
        "mom_growth_rate": 0.20,          # Change growth rate
        "ai_niche_rpm": 300,              # Change CPM
        # ... other parameters
    },
    # ... rest of assumptions
}
```

Then run:
```bash
python startup_model.py
```

The model will recalculate all projections, statements, and visualizations with your custom assumptions.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Suggestions for enhancement:
- Multi-channel modeling
- TaxL custom tax brackets for different regions
- Advertising cost scenarios
- Team expansion modeling
- Additional revenue streams (courses, sponsorships)

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

Created as a financial modeling tool for analyzing YouTube startup viability in the Indian tech space.

---

## 📞 Support & Questions

For questions or issues:
1. Check the documentation above
2. Review the inline code comments in `startup_model.py`
3. Modify assumptions and rerun to test scenarios

---

## 🚀 Getting Started Checklist

- [ ] Clone/download the repository
- [ ] Install Python 3.8+
- [ ] Install dependencies: `pip install pandas matplotlib tabulate openpyxl`
- [ ] Run the model: `python startup_model.py`
- [ ] Review generated `Model_Rextea.xlsx` and `Financial_Analysis_Charts.png`
- [ ] Customize assumptions as needed
- [ ] Rerun for your scenario

---

**Version**: 1.0  
**Last Updated**: February 2026  
**Python Version**: 3.8+
