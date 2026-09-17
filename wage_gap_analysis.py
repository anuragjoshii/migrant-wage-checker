import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "minimum_wage_data.csv"


ESTIMATED_MIGRANT_WORKERS = 100_000_000
ESTIMATED_SHARE_UNDERPAID = 0.30
ASSUMED_AVG_DAILY_SHORTFALL_RS = 150
WORKING_DAYS_PER_MONTH = 26


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def compute_state_wage_gap(df: pd.DataFrame) -> pd.Series:
    return (
        df.groupby("state")["daily_wage_rs"]
        .mean()
        .sort_values(ascending=False)
        .round(0)
    )


def compute_disparity_ratio(state_avg: pd.Series) -> float:
    return round(state_avg.max() / state_avg.min(), 2)


def estimate_national_wage_theft_impact() -> dict:
    affected_workers = ESTIMATED_MIGRANT_WORKERS * ESTIMATED_SHARE_UNDERPAID
    monthly_loss_per_worker = ASSUMED_AVG_DAILY_SHORTFALL_RS * WORKING_DAYS_PER_MONTH
    total_monthly_loss = affected_workers * monthly_loss_per_worker
    total_annual_loss = total_monthly_loss * 12

    return {
        "estimated_affected_workers": int(affected_workers),
        "monthly_loss_per_worker_rs": monthly_loss_per_worker,
        "total_annual_loss_crore_rs": round(total_annual_loss / 1e7, 1),
    }


def plot_state_wage_gap(state_avg: pd.Series, output_path: str = "state_wage_gap_chart.png"):
    plt.figure(figsize=(10, 6))
    colors = ["#c0392b" if v == state_avg.min() else
              "#27ae60" if v == state_avg.max() else
              "#2980b9" for v in state_avg.values]
    bars = plt.bar(state_avg.index, state_avg.values, color=colors)
    plt.title("Average Minimum Daily Wage by State (Sample Dataset)", fontsize=13, fontweight="bold")
    plt.ylabel("Average Daily Wage (₹)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 5,
                  f"₹{int(height)}", ha="center", fontsize=8)

    plt.savefig(output_path, dpi=150)
    print(f"Chart saved to {output_path}")


def main():
    df = load_data(DATA_FILE)
    state_avg = compute_state_wage_gap(df)
    disparity_ratio = compute_disparity_ratio(state_avg)
    impact = estimate_national_wage_theft_impact()

    print("WAGE GAP ANALYSIS — Migrant Wage Checker\n")
    for state, wage in state_avg.items():
        print(f"  {state:<20} ₹{wage:.0f}/day")

    print(f"\nHighest-paying state: {state_avg.idxmax()} (₹{state_avg.max():.0f}/day)")
    print(f"Lowest-paying state:  {state_avg.idxmin()} (₹{state_avg.min():.0f}/day)")
    print(f"Disparity ratio:      {disparity_ratio}x")

    print("\nIllustrative national impact estimate (assumptions stated above):")
    print(f"Estimated workers affected: {impact['estimated_affected_workers']:,}")
    print(f"Estimated annual wage theft: ₹{impact['total_annual_loss_crore_rs']:,} crore")

    plot_state_wage_gap(state_avg)


if __name__ == "__main__":
    main()
