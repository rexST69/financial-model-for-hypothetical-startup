"""
Financial Model for Indian Tech YouTube Startup (3-Year Projection)
"""

import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from datetime import datetime

# Central Assumptions Dictionary
ASSUMPTIONS = {
    "revenue_drivers": {
        "initial_monthly_views": 5_000,
        "mom_growth_rate": 0.15,  # 15%
        "ai_niche_rpm": 250,  # ₹ per 1000 views
        "membership_price": 299,  # ₹
        "membership_conversion_rate": 0.002,  # 0.2%
    },
    "operational_costs_monthly": {
        "freelance_editor": 15_000,  # ₹
        "scriptwriter": 10_000,  # ₹
        "ai_software_suite": 4_500,  # ₹
    },
    "capex": {
        "gear_investment": 150_000,  # ₹ (one-time)
    },
    "timing_logic": {
        "ypp_activation_delay_months": 6,  # Months before YPP eligibility
        "adsense_payment_threshold": 8_600,  # ₹ minimum for payment
    },
    "projection_duration_years": 3,
}


class StartupModel:
    """
    Financial modeling class for Indian Tech YouTube startup.
    Loads and manages assumptions for revenue, costs, and timing.
    """

    def __init__(self, assumptions=None):
        """
        Initialize the StartupModel with provided assumptions.
        
        Args:
            assumptions (dict, optional): Custom assumptions dictionary.
                                         Defaults to global ASSUMPTIONS.
        """
        self.assumptions = assumptions or ASSUMPTIONS
        self.created_at = datetime.now()

    def print_assumptions(self):
        """
        Print assumptions in a clean, organized table format.
        """
        print("\n" + "=" * 70)
        print("FINANCIAL MODEL ASSUMPTIONS - INDIAN TECH YOUTUBE STARTUP")
        print("=" * 70 + "\n")

        # Revenue Drivers Section
        print("📊 REVENUE DRIVERS")
        print("-" * 70)
        revenue_data = [
            ["Initial Monthly Views", f"{self.assumptions['revenue_drivers']['initial_monthly_views']:,}"],
            ["Month-on-Month Growth", f"{self.assumptions['revenue_drivers']['mom_growth_rate'] * 100:.1f}%"],
            ["AI Niche RPM", f"₹{self.assumptions['revenue_drivers']['ai_niche_rpm']:,}"],
            ["Membership Price", f"₹{self.assumptions['revenue_drivers']['membership_price']:,}"],
            ["Membership Conversion Rate", f"{self.assumptions['revenue_drivers']['membership_conversion_rate'] * 100:.2f}%"],
        ]
        print(tabulate(revenue_data, headers=["Parameter", "Value"], tablefmt="grid"))

        # Operational Costs Section
        print("\n💰 OPERATIONAL COSTS (Monthly)")
        print("-" * 70)
        opex_data = [
            ["Freelance Editor", f"₹{self.assumptions['operational_costs_monthly']['freelance_editor']:,}"],
            ["Scriptwriter", f"₹{self.assumptions['operational_costs_monthly']['scriptwriter']:,}"],
            ["AI Software Suite", f"₹{self.assumptions['operational_costs_monthly']['ai_software_suite']:,}"],
        ]
        total_monthly_opex = sum(self.assumptions['operational_costs_monthly'].values())
        opex_data.append(["TOTAL MONTHLY OPEX", f"₹{total_monthly_opex:,}"])
        print(tabulate(opex_data, headers=["Cost Category", "Amount"], tablefmt="grid"))

        # CapEx Section
        print("\n🛠️  CAPITAL EXPENDITURE (One-Time)")
        print("-" * 70)
        capex_data = [
            ["Gear Investment", f"₹{self.assumptions['capex']['gear_investment']:,}"],
        ]
        print(tabulate(capex_data, headers=["Asset", "Cost"], tablefmt="grid"))

        # Timing Logic Section
        print("\n⏱️  TIMING LOGIC")
        print("-" * 70)
        timing_data = [
            ["YPP Activation Delay", f"{self.assumptions['timing_logic']['ypp_activation_delay_months']} months"],
            ["AdSense Payment Threshold", f"₹{self.assumptions['timing_logic']['adsense_payment_threshold']:,}"],
        ]
        print(tabulate(timing_data, headers=["Parameter", "Value"], tablefmt="grid"))

        # Projection Duration
        print("\n📅 PROJECTION DURATION")
        print("-" * 70)
        duration_data = [
            ["Model Timeframe", f"{self.assumptions['projection_duration_years']} years"],
        ]
        print(tabulate(duration_data, headers=["Period", "Duration"], tablefmt="grid"))

        print("\n" + "=" * 70 + "\n")

    def get_assumption(self, *keys):
        """
        Retrieve specific assumption values using nested keys.
        
        Args:
            *keys: Variable length argument list for nested dictionary access.
        
        Returns:
            The value at the specified path in the assumptions dictionary.
        
        Example:
            model.get_assumption('revenue_drivers', 'initial_monthly_views')
        """
        value = self.assumptions
        for key in keys:
            value = value[key]
        return value

    def generate_revenue_projections(self, months=36):
        """
        Generate monthly revenue projections for the specified number of months.
        
        Calculates:
        - Monthly Views with compound MoM growth
        - Gross AdSense (after YPP activation delay)
        - Subscription Revenue (after 30% YouTube cut)
        - Total Monthly Revenue
        
        Args:
            months (int): Number of months to project. Defaults to 36 (3 years).
        
        Returns:
            pd.DataFrame: DataFrame with monthly revenue projections.
        """
        # Get assumptions
        initial_views = self.get_assumption('revenue_drivers', 'initial_monthly_views')
        mom_growth = self.get_assumption('revenue_drivers', 'mom_growth_rate')
        ai_rpm = self.get_assumption('revenue_drivers', 'ai_niche_rpm')
        membership_price = self.get_assumption('revenue_drivers', 'membership_price')
        conversion_rate = self.get_assumption('revenue_drivers', 'membership_conversion_rate')
        ypp_delay = self.get_assumption('timing_logic', 'ypp_activation_delay_months')
        
        # Initialize data structure
        data = []
        
        for month in range(1, months + 1):
            # Calculate monthly views with compound growth
            monthly_views = initial_views * ((1 + mom_growth) ** (month - 1))
            
            # Calculate AdSense revenue
            if month <= ypp_delay:
                gross_adsense = 0
            else:
                gross_adsense = (monthly_views / 1000) * ai_rpm
            
            # Calculate subscription revenue
            monthly_subscribers = monthly_views * conversion_rate
            gross_subscription_revenue = monthly_subscribers * membership_price
            net_subscription_revenue = gross_subscription_revenue * (1 - 0.30)
            
            # Total monthly revenue
            total_revenue = gross_adsense + net_subscription_revenue
            
            data.append({
                'Month': month,
                'Monthly Views': monthly_views,
                'Gross AdSense (₹)': gross_adsense,
                'Monthly Subscribers': monthly_subscribers,
                'Gross Subscription Revenue (₹)': gross_subscription_revenue,
                'Net Subscription Revenue (₹)': net_subscription_revenue,
                'Total Monthly Revenue (₹)': total_revenue,
            })
        
        df = pd.DataFrame(data)
        
        # Print first 12 months
        print("\n" + "=" * 160)
        print("REVENUE PROJECTIONS - FIRST 12 MONTHS")
        print("=" * 160 + "\n")
        
        # Format the dataframe for display
        display_df = df.head(12).copy()
        display_df['Monthly Views'] = display_df['Monthly Views'].apply(lambda x: f"{x:,.0f}")
        display_df['Gross AdSense (₹)'] = display_df['Gross AdSense (₹)'].apply(lambda x: f"₹{x:,.2f}")
        display_df['Monthly Subscribers'] = display_df['Monthly Subscribers'].apply(lambda x: f"{x:,.0f}")
        display_df['Gross Subscription Revenue (₹)'] = display_df['Gross Subscription Revenue (₹)'].apply(lambda x: f"₹{x:,.2f}")
        display_df['Net Subscription Revenue (₹)'] = display_df['Net Subscription Revenue (₹)'].apply(lambda x: f"₹{x:,.2f}")
        display_df['Total Monthly Revenue (₹)'] = display_df['Total Monthly Revenue (₹)'].apply(lambda x: f"₹{x:,.2f}")
        
        print(tabulate(display_df, headers="keys", tablefmt="grid", showindex=False))
        print("\n" + "=" * 160 + "\n")
        
        return df

    def calculate_monthly_cash_flow(self, revenue_df):
        """
        Calculate monthly cash flow with AdSense threshold logic and runway analysis.
        
        Implements:
        - One-time CapEx in Month 1
        - Monthly OpEx deductions
        - Net Subscription Revenue (immediate inflow)
        - AdSense buffering until threshold is met
        - Burn rate and runway calculations
        
        Args:
            revenue_df (pd.DataFrame): Revenue projections from generate_revenue_projections()
        
        Returns:
            pd.DataFrame: Monthly cash flow statement with runway analysis
        """
        # Get assumptions
        monthly_opex = sum(self.assumptions['operational_costs_monthly'].values())
        capex = self.assumptions['capex']['gear_investment']
        adsense_threshold = self.assumptions['timing_logic']['adsense_payment_threshold']
        starting_cash = 200_000  # ₹2,00,000
        
        # Initialize tracking variables
        data = []
        opening_balance = starting_cash
        adsense_buffer = 0
        year_1_outflows = []
        
        for idx, row in revenue_df.iterrows():
            month = int(row['Month'])
            
            # Opening Balance
            current_opening = opening_balance
            
            # Revenue Inflow
            net_subscription_revenue = row['Net Subscription Revenue (₹)']
            gross_adsense = row['Gross AdSense (₹)']
            
            # AdSense threshold logic
            released_adsense = 0
            if gross_adsense > 0:  # Only after YPP activation
                adsense_buffer += gross_adsense
                if adsense_buffer >= adsense_threshold:
                    released_adsense = adsense_buffer
                    adsense_buffer = 0
            
            total_revenue_inflow = net_subscription_revenue + released_adsense
            
            # OpEx Outflow
            opex_outflow = monthly_opex
            
            # CapEx Outflow
            capex_outflow = capex if month == 1 else 0
            
            # Total Outflow
            total_outflow = opex_outflow + capex_outflow
            
            # Net Cash Flow
            net_cash_flow = total_revenue_inflow - total_outflow
            
            # Closing Balance
            closing_balance = current_opening + net_cash_flow
            opening_balance = closing_balance
            
            # Calculate runway (months of cash remaining at current burn rate)
            runway = closing_balance / monthly_opex if monthly_opex > 0 else float('inf')
            
            # Track Year 1 outflows for burn rate calculation
            if month <= 12:
                year_1_outflows.append(total_outflow)
            
            data.append({
                'Month': month,
                'Opening Balance (₹)': current_opening,
                'Revenue Inflow (₹)': total_revenue_inflow,
                'OpEx Outflow (₹)': opex_outflow,
                'CapEx Outflow (₹)': capex_outflow,
                'Total Outflow (₹)': total_outflow,
                'Net Cash Flow (₹)': net_cash_flow,
                'Closing Balance (₹)': closing_balance,
                'Runway (Months)': runway,
                'AdSense Buffer (₹)': adsense_buffer,
                'Released AdSense (₹)': released_adsense,
            })
        
        df = pd.DataFrame(data)
        
        # Calculate burn rate for Year 1
        burn_rate_year1 = sum(year_1_outflows) / 12 if year_1_outflows else 0
        
        # Find financing gap (minimum closing balance)
        min_balance_idx = df['Closing Balance (₹)'].idxmin()
        financing_gap_month = df.loc[min_balance_idx, 'Month']
        min_closing_balance = df.loc[min_balance_idx, 'Closing Balance (₹)']
        financing_gap_amount = abs(min_closing_balance) if min_closing_balance < 0 else 0
        
        # Print 12-Month Cash Budget
        print("\n" + "=" * 240)
        print("12-MONTH CASH BUDGET & RUNWAY ANALYSIS")
        print("=" * 240 + "\n")
        
        display_df = df.head(12).copy()
        
        # Format for display
        for col in display_df.columns:
            if col == 'Month':
                continue
            elif col == 'Runway (Months)':
                display_df[col] = display_df[col].apply(lambda x: f"{x:.2f}" if x != float('inf') else "∞")
            elif col == 'AdSense Buffer (₹)' or col == 'Released AdSense (₹)':
                display_df[col] = display_df[col].apply(lambda x: f"₹{x:,.2f}")
            else:
                display_df[col] = display_df[col].apply(lambda x: f"₹{x:,.2f}")
        
        print(tabulate(display_df, headers="keys", tablefmt="grid", showindex=False))
        
        # Print summary metrics
        print("\n" + "=" * 240)
        print("CASH FLOW METRICS & ANALYSIS")
        print("=" * 240)
        print(f"Starting Cash Balance:        ₹{starting_cash:,.2f}")
        print(f"Year 1 Average Burn Rate:     ₹{burn_rate_year1:,.2f}/month")
        print(f"Month 1 CapEx Investment:     ₹{capex:,.2f}")
        print(f"Monthly OpEx (Steady State):  ₹{monthly_opex:,.2f}")
        print(f"\nMonth 12 Closing Balance:     ₹{df.loc[11, 'Closing Balance (₹)']:,.2f}")
        print(f"Month 12 Runway:              {df.loc[11, 'Runway (Months)']:.2f} months")
        if financing_gap_amount > 0:
            print(f"\n⚠️  Financing Gap Required:   ₹{financing_gap_amount:,.2f} (at Month {financing_gap_month})")
        else:
            print(f"\n✅ No Financing Gap: Business remains cash-positive throughout projection")
        print("=" * 240 + "\n")
        
        return df

    def generate_annual_statements(self, revenue_df, cashflow_df):
        """
        Generate 3-year Income Statements, Balance Sheets, and Cash Flow Statements.
        Exports to Excel with multiple worksheets.
        
        Args:
            revenue_df (pd.DataFrame): Revenue projections from generate_revenue_projections()
            cashflow_df (pd.DataFrame): Cash flow data from calculate_monthly_cash_flow()
        
        Returns:
            tuple: (income_statement_df, balance_sheet_df, cfs_df)
        """
        # Constants
        capex = self.assumptions['capex']['gear_investment']
        depn_rate = 0.20  # 20% straight-line depreciation
        annual_depn = capex * depn_rate
        tax_rate = 0.25  # 25% tax on positive profits
        starting_cash = 200_000
        
        # Initialize lists for annual data
        years = []
        revenues = []
        adsense_revenues = []
        subscription_revenues = []
        opex_outflows = []
        year_end_cash = []
        
        # Aggregate by year
        for year in range(1, 4):
            start_month = (year - 1) * 12 + 1
            end_month = year * 12
            
            year_data = revenue_df[(revenue_df['Month'] >= start_month) & (revenue_df['Month'] <= end_month)]
            year_cashflow = cashflow_df[(cashflow_df['Month'] >= start_month) & (cashflow_df['Month'] <= end_month)]
            
            # Year info
            years.append(f"Year {year}")
            
            # Revenue aggregation
            year_adsense = year_data['Gross AdSense (₹)'].sum()
            year_subscription = year_data['Net Subscription Revenue (₹)'].sum()
            year_revenue = year_adsense + year_subscription
            
            adsense_revenues.append(year_adsense)
            subscription_revenues.append(year_subscription)
            revenues.append(year_revenue)
            
            # OpEx aggregation
            year_opex = year_cashflow['OpEx Outflow (₹)'].sum()
            opex_outflows.append(year_opex)
            
            # Year-end cash
            year_end_balance = year_cashflow.iloc[-1]['Closing Balance (₹)'] if len(year_cashflow) > 0 else 0
            year_end_cash.append(year_end_balance)
        
        # ===== INCOME STATEMENT =====
        is_data = []
        cumulative_ni = 0
        cumulative_depn = 0
        
        for i, year in enumerate(years):
            revenue = revenues[i]
            opex = opex_outflows[i]
            ebitda = revenue - opex
            depreciation = annual_depn
            cumulative_depn += depreciation
            ebit = ebitda - depreciation
            
            # Tax logic: 25% on positive profits only
            tax = max(0, ebit * tax_rate) if ebit > 0 else 0
            net_income = ebit - tax
            cumulative_ni += net_income
            
            is_data.append({
                'Year': year,
                'AdSense Revenue (₹)': adsense_revenues[i],
                'Subscription Revenue (₹)': subscription_revenues[i],
                'Total Revenue (₹)': revenue,
                'Operating Expenses (₹)': opex,
                'EBITDA (₹)': ebitda,
                'Depreciation (₹)': depreciation,
                'EBIT (₹)': ebit,
                'Tax @ 25% (₹)': tax,
                'Net Income (₹)': net_income,
            })
        
        is_df = pd.DataFrame(is_data)
        
        # ===== BALANCE SHEET =====
        bs_data = []
        cumulative_assets_ni = 0
        
        for i, year in enumerate(years):
            # Assets
            cash = max(0, year_end_cash[i])  # Only positive cash on balance sheet
            
            # Fixed Assets
            gross_ppe = capex
            accumulated_depn = min(annual_depn * (i + 1), capex)  # Can't exceed CapEx
            net_ppe = gross_ppe - accumulated_depn
            
            total_assets = cash + net_ppe
            
            # Equity (from start of model)
            cumulative_ni_so_far = sum([is_df.iloc[j]['Net Income (₹)'] for j in range(i + 1)])
            total_equity = starting_cash + cumulative_ni_so_far
            
            # Liabilities = Assets - Equity (if negative cash, it's effectively a liability/debt)
            total_liabilities = total_assets - total_equity
            
            bs_data.append({
                'Year': year,
                'Cash (₹)': cash,
                'Net PPE (₹)': net_ppe,
                'Total Assets (₹)': total_assets,
                'Total Equity (₹)': total_equity,
                'Total Liabilities (₹)': total_liabilities,
                'Liabilities + Equity (₹)': total_liabilities + total_equity,
            })
        
        bs_df = pd.DataFrame(bs_data)
        
        # ===== CASH FLOW STATEMENT =====
        cfs_data = []
        
        for i, year in enumerate(years):
            net_income = is_df.iloc[i]['Net Income (₹)']
            depreciation = annual_depn
            
            # Operating CF = NI + Depreciation
            operating_cf = net_income + depreciation
            
            # Investing CF = -CapEx in Year 1
            investing_cf = -capex if i == 0 else 0
            
            # Financing CF = Initial cash in Year 1
            financing_cf = starting_cash if i == 0 else 0
            
            # Net Change in Cash
            net_cf_change = operating_cf + investing_cf + financing_cf
            
            cfs_data.append({
                'Year': year,
                'Net Income (₹)': net_income,
                'Add: Depreciation (₹)': depreciation,
                'Operating Cash Flow (₹)': operating_cf,
                'Investing CF: -CapEx (₹)': investing_cf,
                'Financing CF: +Equity (₹)': financing_cf,
                'Net Cash Flow (₹)': net_cf_change,
            })
        
        cfs_df = pd.DataFrame(cfs_data)
        
        # ===== PRINT INCOME STATEMENT SUMMARY =====
        print("\n" + "=" * 140)
        print("3-YEAR INCOME STATEMENT SUMMARY")
        print("=" * 140 + "\n")
        
        display_is = is_df.copy()
        for col in display_is.columns:
            if col != 'Year':
                display_is[col] = display_is[col].apply(lambda x: f"₹{x:,.2f}")
        
        print(tabulate(display_is, headers="keys", tablefmt="grid", showindex=False))
        
        # Print key metrics
        print("\n" + "=" * 140)
        print("KEY METRICS")
        print("=" * 140)
        total_revenue_3yr = is_df['Total Revenue (₹)'].sum()
        total_ni_3yr = is_df['Net Income (₹)'].sum()
        print(f"3-Year Cumulative Revenue:  ₹{total_revenue_3yr:,.2f}")
        print(f"3-Year Cumulative Net Income:  ₹{total_ni_3yr:,.2f}")
        year3_cash = max(0, year_end_cash[2])
        print(f"Year 3 Ending Cash:  ₹{year3_cash:,.2f}")
        print("=" * 140 + "\n")
        
        # ===== EXCEL EXPORT =====
        excel_filename = "Model_Rextea.xlsx"
        
        try:
            with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
                # Sheet 1: Assumptions
                assumptions_data = []
                for category, items in ASSUMPTIONS.items():
                    if isinstance(items, dict):
                        for key, value in items.items():
                            assumptions_data.append({
                                'Category': category,
                                'Parameter': key,
                                'Value': value,
                            })
                    else:
                        assumptions_data.append({
                            'Category': category,
                            'Parameter': 'Value',
                            'Value': items,
                        })
                
                assumptions_df = pd.DataFrame(assumptions_data)
                assumptions_df.to_excel(writer, sheet_name='Assumptions', index=False)
                
                # Sheet 2: Revenue Build (first 12 months for clarity)
                revenue_display = revenue_df.head(12).copy()
                revenue_display.to_excel(writer, sheet_name='Revenue_Build', index=False)
                
                # Sheet 3: Cash Budget
                cashflow_display = cashflow_df.head(12).copy()
                cashflow_display.to_excel(writer, sheet_name='Cash_Budget', index=False)
                
                # Sheet 4: Annual Pro Forma (combining IS, BS, CFS)
                is_df.to_excel(writer, sheet_name='Annual_Pro_Forma', startrow=0, index=False)
                bs_df.to_excel(writer, sheet_name='Annual_Pro_Forma', startrow=len(is_df) + 3, index=False)
                cfs_df.to_excel(writer, sheet_name='Annual_Pro_Forma', startrow=len(is_df) + len(bs_df) + 6, index=False)
            
            print(f"✅ Excel file '{excel_filename}' exported successfully!\n")
        
        except Exception as e:
            print(f"⚠️  Error exporting Excel: {e}\n")
        
        return is_df, bs_df, cfs_df

    def run_scenario_analysis(self, base_revenue_df, base_cashflow_df):
        """
        Run scenario analysis including valuation, sensitivity analysis, and visualizations.
        
        Includes:
        - Base case valuation (4x Revenue Multiple)
        - Sensitivity analysis (50% reduction in conversion rate)
        - Cash runway visualization (highlight Valley of Death)
        - Revenue mix stacked bar chart
        
        Args:
            base_revenue_df (pd.DataFrame): Base case revenue projections
            base_cashflow_df (pd.DataFrame): Base case cash flow data
        """
        # ===== VALUATION (BASE CASE) =====
        print("\n" + "=" * 140)
        print("VALUATION & SCENARIO ANALYSIS")
        print("=" * 140 + "\n")
        
        # Year 3 Annual Revenue (Base Case)
        y3_revenue_base = base_revenue_df[
            (base_revenue_df['Month'] >= 25) & (base_revenue_df['Month'] <= 36)
        ]['Total Monthly Revenue (₹)'].sum()
        
        # Valuation (4x Revenue Multiple)
        revenue_multiple = 4
        valuation_base = y3_revenue_base * revenue_multiple
        
        print("📊 BASE CASE VALUATION")
        print("-" * 140)
        print(f"Year 3 Annual Revenue (Months 25-36):  ₹{y3_revenue_base:,.2f}")
        print(f"Valuation Multiple (SaaS/AI Standard):  {revenue_multiple}x")
        print(f"Enterprise Valuation:                  ₹{valuation_base:,.2f}")
        print()
        
        # ===== SENSITIVITY ANALYSIS (FOUNDER PAIN SCENARIO) =====
        print("📉 SENSITIVITY ANALYSIS: FOUNDER PAIN SCENARIO")
        print("-" * 140)
        print("Assumption Change: Membership Conversion Rate 0.2% → 0.1% (50% Drop)\n")
        
        # Create modified assumptions (downside case)
        downside_assumptions = self.assumptions.copy()
        downside_assumptions['revenue_drivers'] = downside_assumptions['revenue_drivers'].copy()
        downside_assumptions['revenue_drivers']['membership_conversion_rate'] = 0.001  # 0.1%
        
        # Create new model instance with downside assumptions
        downside_model = StartupModel(downside_assumptions)
        downside_revenue_df = downside_model.generate_revenue_projections(months=36)
        
        # Suppress output by not calling print methods
        y3_revenue_downside = downside_revenue_df[
            (downside_revenue_df['Month'] >= 25) & (downside_revenue_df['Month'] <= 36)
        ]['Total Monthly Revenue (₹)'].sum()
        
        valuation_downside = y3_revenue_downside * revenue_multiple
        
        # Calculate impact
        revenue_change_pct = ((y3_revenue_downside - y3_revenue_base) / y3_revenue_base) * 100
        valuation_change_pct = revenue_change_pct  # Same percentage change
        valuation_change = valuation_downside - valuation_base
        
        print(f"Year 3 Revenue (Downside Case):        ₹{y3_revenue_downside:,.2f}")
        print(f"Valuation (Downside Case):             ₹{valuation_downside:,.2f}")
        print(f"\nRevenue Impact:                         {revenue_change_pct:.2f}%")
        print(f"Valuation Impact:                       {valuation_change_pct:.2f}% (₹{valuation_change:,.2f})")
        print()
        
        # Summary table
        scenario_data = [
            ['Metric', 'Base Case', 'Downside Case', 'Impact'],
            ['Year 3 Revenue', f"₹{y3_revenue_base:,.2f}", f"₹{y3_revenue_downside:,.2f}", f"{revenue_change_pct:.2f}%"],
            ['Valuation (4x)', f"₹{valuation_base:,.2f}", f"₹{valuation_downside:,.2f}", f"{valuation_change_pct:.2f}%"],
        ]
        print(tabulate(scenario_data, headers="firstrow", tablefmt="grid"))
        print()
        
        # ===== VISUALIZATIONS =====
        print("📈 GENERATING VISUALIZATIONS...\n")
        
        # Chart 1: Cash Runway (24 months) - Highlight Valley of Death
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Extract months 1-24
        months_24 = base_cashflow_df.head(24)
        
        # Plot cash balance
        ax1.plot(months_24['Month'], months_24['Closing Balance (₹)'], 
                linewidth=2.5, color='#1f77b4', marker='o', markersize=4)
        ax1.axhline(y=0, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Break-even')
        
        # Highlight the Valley of Death (minimum point)
        min_idx = months_24['Closing Balance (₹)'].idxmin()
        min_cash = months_24.loc[min_idx, 'Closing Balance (₹)']
        min_month = months_24.loc[min_idx, 'Month']
        
        ax1.scatter([min_month], [min_cash], color='red', s=150, zorder=5, 
                   label=f'Valley of Death (Month {int(min_month)}: ₹{min_cash:,.0f})')
        ax1.annotate(f'Month {int(min_month)}\n₹{min_cash:,.0f}', 
                    xy=(min_month, min_cash), xytext=(min_month + 2, min_cash - 30000),
                    fontsize=9, ha='left',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', color='red'))
        
        ax1.fill_between(months_24['Month'], months_24['Closing Balance (₹)'], 0, 
                        where=(months_24['Closing Balance (₹)'] < 0), 
                        alpha=0.2, color='red', label='Negative Cash Period')
        
        ax1.set_xlabel('Month', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Closing Cash Balance (₹)', fontsize=11, fontweight='bold')
        ax1.set_title('Cash Runway Analysis (24 Months) - Identifying the Valley of Death', 
                     fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc='best', fontsize=9)
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.0f}L' if abs(x) >= 100000 else f'₹{x/1000:.0f}K'))
        
        # Chart 2: Revenue Mix (Stacked Bar Chart for Years)
        years_labels = ['Year 1', 'Year 2', 'Year 3']
        
        # Aggregate by year
        year_adsense = []
        year_subscription = []
        
        for year in range(1, 4):
            start_month = (year - 1) * 12 + 1
            end_month = year * 12
            
            year_data = base_revenue_df[
                (base_revenue_df['Month'] >= start_month) & (base_revenue_df['Month'] <= end_month)
            ]
            
            adsense_total = year_data['Gross AdSense (₹)'].sum()
            subscription_total = year_data['Net Subscription Revenue (₹)'].sum()
            
            year_adsense.append(adsense_total)
            year_subscription.append(subscription_total)
        
        x_pos = range(len(years_labels))
        width = 0.6
        
        ax2.bar(x_pos, year_adsense, width, label='AdSense Revenue', color='#2ca02c', alpha=0.8)
        ax2.bar(x_pos, year_subscription, width, bottom=year_adsense, 
               label='Net Subscription Revenue', color='#ff7f0e', alpha=0.8)
        
        # Add value labels on stacked bars
        for i, (adsense, subscription) in enumerate(zip(year_adsense, year_subscription)):
            total = adsense + subscription
            # AdSense label
            if adsense > 0:
                ax2.text(i, adsense / 2, f'₹{adsense/100000:.1f}L', 
                        ha='center', va='center', fontweight='bold', fontsize=9, color='white')
            # Subscription label
            ax2.text(i, adsense + subscription / 2, f'₹{subscription/100000:.1f}L', 
                    ha='center', va='center', fontweight='bold', fontsize=9, color='white')
            # Total on top
            ax2.text(i, total, f'₹{total/100000:.1f}L', 
                    ha='center', va='bottom', fontweight='bold', fontsize=10)
        
        ax2.set_ylabel('Annual Revenue (₹)', fontsize=11, fontweight='bold')
        ax2.set_title('Revenue Mix: AdSense vs. Subscription (3-Year Projection)', 
                     fontsize=13, fontweight='bold')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(years_labels)
        ax2.legend(loc='upper left', fontsize=10)
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.0f}L'))
        
        plt.tight_layout()
        
        # Save figures
        fig.savefig('Financial_Analysis_Charts.png', dpi=300, bbox_inches='tight')
        print("✅ Chart saved: Financial_Analysis_Charts.png\n")
        
        # Print summary
        print("=" * 140)
        print("VISUALIZATION SUMMARY")
        print("=" * 140)
        print(f"Chart 1 - Cash Runway (Months 1-24):")
        print(f"  • Valley of Death at Month {int(min_month)}: ₹{min_cash:,.2f}")
        print(f"  • Financing need through this period: ₹{abs(min_cash):,.2f}")
        print(f"\nChart 2 - Revenue Mix (Annual Breakdown):")
        print(f"  • Year 1: AdSense ₹{year_adsense[0]:,.2f} + Subscriptions ₹{year_subscription[0]:,.2f}")
        print(f"  • Year 2: AdSense ₹{year_adsense[1]:,.2f} + Subscriptions ₹{year_subscription[1]:,.2f}")
        print(f"  • Year 3: AdSense ₹{year_adsense[2]:,.2f} + Subscriptions ₹{year_subscription[2]:,.2f}")
        print("=" * 140 + "\n")


if __name__ == "__main__":
    # Initialize the model
    model = StartupModel()

    # Print assumptions in table format
    model.print_assumptions()

    # Example: Access specific assumptions
    print("Example Queries:")
    print("-" * 70)
    print(f"Initial Monthly Views: {model.get_assumption('revenue_drivers', 'initial_monthly_views'):,}")
    print(f"Monthly Opex: ₹{sum(model.assumptions['operational_costs_monthly'].values()):,}")
    print(f"YPP Delay: {model.get_assumption('timing_logic', 'ypp_activation_delay_months')} months")
    print()

    # Generate and display revenue projections
    revenue_df = model.generate_revenue_projections(months=36)
    
    # Calculate and display cash flow analysis
    cashflow_df = model.calculate_monthly_cash_flow(revenue_df)
    
    # Generate and export annual financial statements
    is_df, bs_df, cfs_df = model.generate_annual_statements(revenue_df, cashflow_df)
    
    # Run scenario analysis with visualizations
    model.run_scenario_analysis(revenue_df, cashflow_df)
