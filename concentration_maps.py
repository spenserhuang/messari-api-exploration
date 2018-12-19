# IMPORT LIBRARIES
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# PARSE JSON FILE
with open('assets_info.json') as f:
    asset_details = json.load(f)


# # MAX SUPPLY
# max_supply_list = []
# max_supply_1 = []
# max_supply_2 = []
# max_supply_3 = []
# max_supply_4 = []
# max_supply_5 = []
# max_supply_6 = []
#
# # only 53 assets are not null or 0
# for asset in asset_details:
#     if asset["profile"]["token_distribution"]["max_supply"] is not None and asset["profile"]["token_distribution"]["max_supply"] is not 0:
#             max_supply_list.append(asset["profile"]["token_distribution"]["max_supply"])
#
# for supply in max_supply_list:
#     if supply >= 0 and supply < 10_000_000:
#         max_supply_1.append(supply)
#     elif supply >= 10_000_000 and supply < 50_000_000:
#         max_supply_2.append(supply)
#     elif supply >= 50_000_000 and supply < 100_000_000:
#         max_supply_3.append(supply)
#     elif supply >= 100_000_000 and supply < 500_000_000:
#         max_supply_4.append(supply)
#     elif supply >= 500_000_000 and supply < 1_000_000_000:
#         max_supply_5.append(supply)
#     else:
#         max_supply_6.append(supply)
#
# ms_objects = ['0 - 10mil', '10mil - 50mil', '50mil - 100mil', '100mil - 500mil', '500mil - 1bil', '1bil +']
# ms_y_pos = np.arange(len(ms_objects))
# ms_performance = [len(max_supply_1), len(max_supply_2), len(max_supply_3), len(max_supply_4), len(max_supply_5), len(max_supply_6)]
#
# plt.bar(ms_y_pos, ms_performance, align='center')
# plt.xticks(ms_y_pos, ms_objects)
# plt.ylabel('Number of Assets')
# plt.xlabel('Max Supply')
# plt.title('Distribution of Max Supply for Assets')
#
# plt.show()



# Y2050 SUPPLY
# y_2050_list = []
# y_2050_1 = []
# y_2050_2 = []
# y_2050_3 = []
# y_2050_4 = []
# y_2050_5 = []
# y_2050_6 = []
#
# # only 53 assets are not null or 0
# for asset in asset_details:
#     if asset["metrics"]["supply"]["y_2050"] is not None and asset["metrics"]["supply"]["y_2050"] is not 0:
#         if asset["profile"]["token_distribution"]["max_supply"] is not None and asset["profile"]["token_distribution"]["max_supply"] is not 0:
#             y_2050_list.append(asset["metrics"]["supply"]["y_2050"])
#
# for supply in y_2050_list:
#     if supply >= 0 and supply < 10_000_000:
#         y_2050_1.append(supply)
#     elif supply >= 10_000_000 and supply < 50_000_000:
#         y_2050_2.append(supply)
#     elif supply >= 50_000_000 and supply < 100_000_000:
#         y_2050_3.append(supply)
#     elif supply >= 100_000_000 and supply < 500_000_000:
#         y_2050_4.append(supply)
#     elif supply >= 500_000_000 and supply < 1_000_000_000:
#         y_2050_5.append(supply)
#     else:
#         y_2050_6.append(supply)
#
# y2050_objects = ['0 - 10mil', '10mil - 50mil', '50mil - 100mil', '100mil - 500mil', '500mil - 1bil', '1bil +']
# y2050_y_pos = np.arange(len(y2050_objects))
# y2050_performance = [len(y_2050_1), len(y_2050_2), len(y_2050_3), len(y_2050_4), len(y_2050_5), len(y_2050_6)]
#
# plt.bar(y2050_y_pos, y2050_performance, align='center')
# plt.xticks(y2050_y_pos, y2050_objects)
# plt.ylabel('Number of Assets')
# plt.xlabel('Y2050 Supply')
# plt.title('Distribution of Y2050 for Assets')
#
# plt.show()


#
# # PERCENT SUPPLY CIRCULATING
# percent_supply_circulating_list = []
# percent_group_1 = []
# percent_group_2 = []
# percent_group_3 = []
# percent_group_4 = []
# percent_group_5 = []
# percent_group_6 = []
#
# # only 53 assets are not null or 0
# for asset in asset_details:
#     if asset["profile"]["token_distribution"]["max_supply"] is not None and asset["profile"]["token_distribution"]["max_supply"] is not 0:
#         max_supply = asset["profile"]["token_distribution"]["max_supply"]
#         circulating = asset["metrics"]["supply"]["circulating"]
#         percentage = circulating / max_supply * 100
#         percent_supply_circulating_list.append(percentage)
#
# for percentage in percent_supply_circulating_list:
#     if percentage >= 0 and percentage < 20:
#         percent_group_1.append(percentage)
#     elif percentage >= 20 and percentage < 40:
#         percent_group_2.append(percentage)
#     elif percentage >= 40 and percentage < 60:
#         percent_group_3.append(percentage)
#     elif percentage >= 60 and percentage < 80:
#         percent_group_4.append(percentage)
#     elif percentage >= 80 and percentage < 100:
#         percent_group_5.append(percentage)
#     else:
#         percent_group_6.append(percentage)
#
# per_group_objects = ['0% - 20%', '20% - 40%', '40% - 60%', '60% - 80%', '80% - 99%', '100%']
# per_group_y_pos = np.arange(len(per_group_objects))
# per_group_performance = [len(percent_group_1), len(percent_group_2), len(percent_group_3), len(percent_group_4), len(percent_group_5), len(percent_group_6)]
#
# plt.bar(per_group_y_pos, per_group_performance, align='center')
# plt.xticks(per_group_y_pos, per_group_objects)
# plt.ylabel('Number of Assets')
# plt.xlabel('Percentage of Total Supply Circulating')
# plt.title('Distribution of Percentage of Total Supply Circulating for Assets')
#
# plt.show()
#


# # Y2050 DISTRIBUTION PERCENTAGE
# y_2050_distribution_percentage_list = []
# y_2050_percent_group_1 = []
# y_2050_percent_group_2 = []
# y_2050_percent_group_3 = []
# y_2050_percent_group_4 = []
# y_2050_percent_group_5 = []
# y_2050_percent_group_6 = []
#
# # only 45 assets are not null or 0
# for asset in asset_details:
#     if asset["profile"]["token_distribution"]["max_supply"] is not None and asset["profile"]["token_distribution"]["max_supply"] is not 0:
#         max_supply = asset["profile"]["token_distribution"]["max_supply"]
#         y_2050 = asset["metrics"]["supply"]["y_2050"]
#         percentage = y_2050 / max_supply * 100
#         y_2050_distribution_percentage_list.append(percentage)
#
# for percentage in y_2050_distribution_percentage_list:
#     if percentage >= 0 and percentage < 20:
#         y_2050_percent_group_1.append(percentage)
#     elif percentage > 20 and percentage < 40:
#         y_2050_percent_group_2.append(percentage)
#     elif percentage >= 40 and percentage < 60:
#         y_2050_percent_group_3.append(percentage)
#     elif percentage >= 60 and percentage < 80:
#         y_2050_percent_group_4.append(percentage)
#     elif percentage >= 80 and percentage < 100:
#         y_2050_percent_group_5.append(percentage)
#     elif percentage == 100:
#         y_2050_percent_group_6.append(percentage)
#
# per_group_y2050_objects = ['0% - 20%', '20% - 40%', '40% - 60%', '60% - 80%', '80% - 99%', '100%']
# per_group_y2050_y_pos = np.arange(len(per_group_y2050_objects))
# per_group_y2050_performance = [len(y_2050_percent_group_1), len(y_2050_percent_group_2), len(y_2050_percent_group_3), len(y_2050_percent_group_4), len(y_2050_percent_group_5), len(y_2050_percent_group_6)]
#
# plt.bar(per_group_y2050_y_pos, per_group_y2050_performance, align='center')
# plt.xticks(per_group_y2050_y_pos, per_group_y2050_objects)
# plt.ylabel('Number of Assets')
# plt.xlabel('Percentage of Total Supply Distributed by Y2050')
# plt.title('Distribution of Percentage of Total Supply Distributed by Y2050 for Assets')
#
# plt.show()



# # INITIAL DISTRIBUTION PERCENTAGE
# initial_distribution_percentage_list = []
# initial_percent_group_1 = []
# initial_percent_group_2 = []
# initial_percent_group_3 = []
# initial_percent_group_4 = []
# initial_percent_group_5 = []
# initial_percent_group_6 = []
#
# # only 45 assets are not null or 0
# for asset in asset_details:
#     if asset["profile"]["token_distribution"]["max_supply"] is not None and asset["profile"]["token_distribution"]["max_supply"] is not 0 and asset["profile"]["token_distribution"]["initial_distribution"] is not None:
#         max_supply = asset["profile"]["token_distribution"]["max_supply"]
#         initial_distribution = asset["profile"]["token_distribution"]["initial_distribution"]
#         percentage = initial_distribution / max_supply * 100
#         initial_distribution_percentage_list.append(percentage)
#
# for percentage in initial_distribution_percentage_list:
#     if percentage >= 0 and percentage < 20:
#         initial_percent_group_1.append(percentage)
#     elif percentage >= 20 and percentage < 40:
#         initial_percent_group_2.append(percentage)
#     elif percentage >= 40 and percentage < 60:
#         initial_percent_group_3.append(percentage)
#     elif percentage >= 60 and percentage < 80:
#         initial_percent_group_4.append(percentage)
#     elif percentage >= 80 and percentage < 100:
#         initial_percent_group_5.append(percentage)
#     elif percentage == 100:
#         initial_percent_group_6.append(percentage)
#
# per_group_initial_objects = ['0% - 20%', '20% - 40%', '40% - 60%', '60% - 80%', '80% - 99%', '100%']
# per_group_initial_y_pos = np.arange(len(per_group_initial_objects))
# per_group_initial_performance = [len(initial_percent_group_1), len(initial_percent_group_2), len(initial_percent_group_3), len(initial_percent_group_4), len(initial_percent_group_5), len(initial_percent_group_6)]
#
# plt.bar(per_group_initial_y_pos, per_group_initial_performance, align='center')
# plt.xticks(per_group_initial_y_pos, per_group_initial_objects)
# plt.ylabel('Number of Assets')
# plt.xlabel('Percentage of Total Supply Distributed Initially')
# plt.title('Distribution of Percentage of Total Supply Distributed Initially for Assets')
#
# plt.show()



# # VLAD CLUB COST
# vlad_cost_list = []
# vlad_cost_1 = []
# vlad_cost_2 = []
# vlad_cost_3 = []
# vlad_cost_4 = []
# vlad_cost_5 = []
# vlad_cost_6 = []
#
# # only 53 assets are not null or 0
# for asset in asset_details:
#     if asset["metrics"]["misc_data"]["vladmir_cost_club"] is not None and asset["metrics"]["misc_data"]["vladmir_cost_club"] is not 0:
#             vlad_cost_list.append(asset["metrics"]["misc_data"]["vladmir_cost_club"])
#
# for cost in vlad_cost_list:
#     if cost >= 0 and cost < 1_000:
#         vlad_cost_1.append(cost)
#     elif cost >= 1_000 and cost < 5_000:
#         vlad_cost_2.append(cost)
#     elif cost >= 5_000 and cost < 10_000:
#         vlad_cost_3.append(cost)
#     elif cost >= 10_000 and cost < 50_000:
#         vlad_cost_4.append(cost)
#     elif cost >= 50_000 and cost < 100_000:
#         vlad_cost_5.append(cost)
#     else:
#         vlad_cost_6.append(cost)
#
# vc_objects = ['0 - 1,000', '1,000 - 5,000', '5,000 - 10,000', '10,000 - 50,000', '50,000 - 100,000', '100,000+']
# vc_y_pos = np.arange(len(vc_objects))
# vc_performance = [len(vlad_cost_1), len(vlad_cost_2), len(vlad_cost_3), len(vlad_cost_4), len(vlad_cost_5), len(vlad_cost_6)]
#
# plt.bar(vc_y_pos, vc_performance, align='center')
# plt.xticks(vc_y_pos, vc_objects)
# plt.ylabel('Number of Assets')
# plt.xlabel('Cost ($)')
# plt.title('Distribution of Vlad Club Cost for Assets')
#
# plt.show()
