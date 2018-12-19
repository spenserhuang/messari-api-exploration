# IMPORT LIBRARIES
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# PARSE JSON FILE
with open('assets_info.json') as f:
    asset_details = json.load(f)


# COMPARISONS
currency = {"symbol": [], "age": [], "ath": [], "roi": [], "dev": [], "vlad": []}
infrastructure = {"symbol": [], "age": [], "ath": [], "roi": [], "dev": [], "vlad": []}
financial = {"symbol": [], "age": [], "ath": [], "roi": [], "dev": [], "vlad": []}
services = {"symbol": [], "age": [], "ath": [], "roi": [], "dev": [], "vlad": []}
media_and_entertainment = {"symbol": [], "age": [], "ath": [], "roi": [], "dev": [], "vlad": []}

categories = {"currency": currency, "infrastructure": infrastructure, "financial": financial, "services": services, "media_and_entertainment": media_and_entertainment}

for asset in asset_details:
    if asset["metrics"]["misc_data"]["categories"][0] == "Currency":
        categories["currency"]["symbol"].append(asset["symbol"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Infrastructure":
        categories["infrastructure"]["symbol"].append(asset["symbol"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Financial":
        categories["financial"]["symbol"].append(asset["symbol"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Services":
        categories["services"]["symbol"].append(asset["symbol"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Media and Entertainment":
        categories["media_and_entertainment"]["symbol"].append(asset["symbol"])


# AGE
for asset in asset_details:
    if asset["metrics"]["misc_data"]["categories"][0] == "Currency":
        categories["currency"]["age"].append(asset["metrics"]["misc_data"]["asset_age_days"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Infrastructure":
        categories["infrastructure"]["age"].append(asset["metrics"]["misc_data"]["asset_age_days"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Financial":
        categories["financial"]["age"].append(asset["metrics"]["misc_data"]["asset_age_days"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Services":
        categories["services"]["age"].append(asset["metrics"]["misc_data"]["asset_age_days"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Media and Entertainment":
        categories["media_and_entertainment"]["age"].append(asset["metrics"]["misc_data"]["asset_age_days"])


# ATH
for asset in asset_details:
    if asset["metrics"]["misc_data"]["categories"][0] == "Currency":
        categories["currency"]["ath"].append(asset["metrics"]["all_time_high"]["percent_down"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Infrastructure":
        categories["infrastructure"]["ath"].append(asset["metrics"]["all_time_high"]["percent_down"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Financial":
        categories["financial"]["ath"].append(asset["metrics"]["all_time_high"]["percent_down"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Services":
        categories["services"]["ath"].append(asset["metrics"]["all_time_high"]["percent_down"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Media and Entertainment":
        categories["media_and_entertainment"]["ath"].append(asset["metrics"]["all_time_high"]["percent_down"])


# ROI
for asset in asset_details:
    if asset["metrics"]["misc_data"]["categories"][0] == "Currency":
        categories["currency"]["roi"].append(asset["metrics"]["roi_data"]["percent_change_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Infrastructure":
        categories["infrastructure"]["roi"].append(asset["metrics"]["roi_data"]["percent_change_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Financial":
        categories["financial"]["roi"].append(asset["metrics"]["roi_data"]["percent_change_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Services":
        categories["services"]["roi"].append(asset["metrics"]["roi_data"]["percent_change_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Media and Entertainment":
        categories["media_and_entertainment"]["roi"].append(asset["metrics"]["roi_data"]["percent_change_last_1_year"])


# DEV
for asset in asset_details:
    if asset["metrics"]["misc_data"]["categories"][0] == "Currency":
        if asset["metrics"]["developer_activity"]["commits_last_1_year"] is not None:
            categories["currency"]["dev"].append(asset["metrics"]["developer_activity"]["commits_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Infrastructure":
        if asset["metrics"]["developer_activity"]["commits_last_1_year"] is not None:
            categories["infrastructure"]["dev"].append(asset["metrics"]["developer_activity"]["commits_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Financial":
        if asset["metrics"]["developer_activity"]["commits_last_1_year"] is not None:
            categories["financial"]["dev"].append(asset["metrics"]["developer_activity"]["commits_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Services":
        if asset["metrics"]["developer_activity"]["commits_last_1_year"] is not None:
            categories["services"]["dev"].append(asset["metrics"]["developer_activity"]["commits_last_1_year"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Media and Entertainment":
        if asset["metrics"]["developer_activity"]["commits_last_1_year"] is not None:
            categories["media_and_entertainment"]["dev"].append(asset["metrics"]["developer_activity"]["commits_last_1_year"])

# VLAD
for asset in asset_details:
    if asset["metrics"]["misc_data"]["categories"][0] == "Currency":
        categories["currency"]["vlad"].append(asset["metrics"]["misc_data"]["vladmir_cost_club"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Infrastructure":
        categories["infrastructure"]["vlad"].append(asset["metrics"]["misc_data"]["vladmir_cost_club"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Financial":
        categories["financial"]["vlad"].append(asset["metrics"]["misc_data"]["vladmir_cost_club"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Services":
        categories["services"]["vlad"].append(asset["metrics"]["misc_data"]["vladmir_cost_club"])
    elif asset["metrics"]["misc_data"]["categories"][0] == "Media and Entertainment":
        categories["media_and_entertainment"]["vlad"].append(asset["metrics"]["misc_data"]["vladmir_cost_club"])


for key in categories:
    avg_age = sum(categories[key]["age"]) / len(categories[key]["age"])
    categories[key]["avg_age"] = avg_age

    avg_ath = sum(categories[key]["ath"]) / len(categories[key]["ath"])
    categories[key]["avg_ath"] = avg_ath

    avg_roi = sum(categories[key]["roi"]) / len(categories[key]["roi"])
    categories[key]["avg_roi"] = avg_roi * -1

    avg_dev = sum(categories[key]["dev"]) / len(categories[key]["dev"])
    categories[key]["avg_dev"] = avg_dev

    avg_vlad = sum(categories[key]["vlad"]) / len(categories[key]["vlad"])
    categories[key]["avg_vlad"] = avg_vlad
    print(categories[key]["avg_vlad"])


# # AGE GRAPH
# age_objects = ['Currency', 'Infrastructure', 'Financial', 'Services', 'Media & Entertainment']
# age_y_pos = np.arange(len(age_objects))
# age_performance = [categories["currency"]["avg_age"], categories["infrastructure"]["avg_age"], categories["financial"]["avg_age"], categories["services"]["avg_age"], categories["media_and_entertainment"]["avg_age"]]
#
# plt.bar(age_y_pos, age_performance, align='center')
# plt.xticks(age_y_pos, age_objects)
# plt.ylabel('Average Age (days)')
# plt.xlabel('Category')
# plt.title('Comparison of Average Asset Age Across Categories')
#
# plt.show()


# # ATH GRAPH
# ath_objects = ['Currency', 'Infrastructure', 'Financial', 'Services', 'Media & Entertainment']
# ath_y_pos = np.arange(len(ath_objects))
# ath_performance = [categories["currency"]["avg_ath"], categories["infrastructure"]["avg_ath"], categories["financial"]["avg_ath"], categories["services"]["avg_ath"], categories["media_and_entertainment"]["avg_ath"]]
#
# plt.bar(ath_y_pos, ath_performance, align='center')
# plt.xticks(ath_y_pos, ath_objects)
# plt.ylabel('Average ATH Percent Down (%)')
# plt.xlabel('Category')
# plt.title('Comparison of Average All Time High Percent Down Across Categories')
#
# plt.show()


# # ROI GRAPH
# roi_objects = ['Currency', 'Infrastructure', 'Financial', 'Services', 'Media & Entertainment']
# roi_y_pos = np.arange(len(roi_objects))
# roi_performance = [categories["currency"]["avg_roi"], categories["infrastructure"]["avg_roi"], categories["financial"]["avg_roi"], categories["services"]["avg_roi"], categories["media_and_entertainment"]["avg_roi"]]
#
# plt.bar(roi_y_pos, roi_performance, align='center')
# plt.xticks(roi_y_pos, roi_objects)
# plt.ylabel('Average ROI Percent Down (%)')
# plt.xlabel('Category')
# plt.title('Comparison of Average 1 Year ROI Percent Down Across Categories')
#
# plt.show()


# # DEV GRAPH
# dev_objects = ['Currency', 'Infrastructure', 'Financial', 'Services', 'Media & Entertainment']
# dev_y_pos = np.arange(len(dev_objects))
# dev_performance = [categories["currency"]["avg_dev"], categories["infrastructure"]["avg_dev"], categories["financial"]["avg_dev"], categories["services"]["avg_dev"], categories["media_and_entertainment"]["avg_dev"]]
#
# plt.bar(dev_y_pos, dev_performance, align='center')
# plt.xticks(dev_y_pos, dev_objects)
# plt.ylabel('Average Commits Last 1 Year')
# plt.xlabel('Category')
# plt.title('Comparison of Commits Last 1 Year Across Categories')
#
# plt.show()


# # VLAD GRAPH
# vlad_objects = ['Currency', 'Infrastructure', 'Financial', 'Services', 'Media & Entertainment']
# vlad_y_pos = np.arange(len(vlad_objects))
# vlad_performance = [categories["currency"]["avg_vlad"], categories["infrastructure"]["avg_vlad"], categories["financial"]["avg_vlad"], categories["services"]["avg_vlad"], categories["media_and_entertainment"]["avg_vlad"]]
#
# plt.bar(vlad_y_pos, vlad_performance, align='center')
# plt.xticks(vlad_y_pos, vlad_objects)
# plt.ylabel('Average Vlad Club Cost ($)')
# plt.xlabel('Category')
# plt.title('Comparison of Vlad Club Cost Across Categories')
#
# plt.show()
