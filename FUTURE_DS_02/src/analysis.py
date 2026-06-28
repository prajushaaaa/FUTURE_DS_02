import pandas as pd
import matplotlib.pyplot as plt

print("Social Media Campaign Performance Tracker")
print("-" * 50)

# Load Dataset
df = pd.read_csv("data/Advertising_Data.csv")

# Total Sales
total_sales = df["Product_Sold"].sum()

# Marketing Channels
channels = [
    "TV",
    "Billboards",
    "Google_Ads",
    "Social_Media",
    "Influencer_Marketing",
    "Affiliate_Marketing"
]

# Total Spend
total_spend = df[channels].sum().sum()

# Profit
profit = total_sales - total_spend

# ROI
roi = ((profit / total_spend) * 100)

# Best Channel
best_channel = df[channels].sum().idxmax()

print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Spend: {total_spend:,.2f}")
print(f"Profit: {profit:,.2f}")
print(f"ROI: {roi:.2f}%")
print(f"Best Channel: {best_channel}")

# Channel-wise Spend
channel_spend = df[channels].sum()

print("\nChannel-wise Spend:")
print(channel_spend)

# Channel-wise ROI
channel_roi = {}

for channel in channels:
    spend = df[channel].sum()
    channel_roi[channel] = ((total_sales - spend) / spend) * 100

roi_df = pd.DataFrame(
    list(channel_roi.items()),
    columns=["Channel", "ROI"]
)

print("\nROI by Channel:")
print(roi_df)

# -------------------------
# Visualization 1
# ROI by Channel
# -------------------------
plt.figure(figsize=(8,5))
plt.plot(roi_df["Channel"], roi_df["ROI"], marker="o")
plt.title("ROI by Channel")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/roi_by_channel.png")
plt.close()

# -------------------------
# Visualization 2
# Total Spend by Channel
# -------------------------
plt.figure(figsize=(8,5))
channel_spend.sort_values().plot(kind="bar")
plt.title("Total Spend by Channel")
plt.ylabel("Spend")
plt.tight_layout()
plt.savefig("images/spend_by_channel.png")
plt.close()

# -------------------------
# Visualization 3
# Spend Distribution
# -------------------------
plt.figure(figsize=(8,8))
channel_spend.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Marketing Spend Distribution")
plt.tight_layout()
plt.savefig("images/spend_distribution.png")
plt.close()

print("\nAnalysis Completed Successfully!")