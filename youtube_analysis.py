# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns


# # Load dataset
# data = pd.read_csv("USvideos.csv")

# #
# plt.figure(figsize=(14,10))
# plt.suptitle("YouTube Trending Video Analysis", fontsize=16)

# # Show first rows
# print("First 5 rows of dataset:")
# print(data.head())

# # Dataset info
# print("\nDataset Shape:")
# print(data.shape)

# print("\nColumns:")
# print(data.columns)

# # Missing values
# print("\nMissing Values:")
# print(data.isnull().sum())

# # Top 10 most viewed videos
# top_videos = data.sort_values(by="views", ascending=False).head(10)

# print("\nTop 10 Most Viewed Videos:")
# print(top_videos[["title","channel_title","views"]])

# # Average values using NumPy
# print("\nAverage Views:", np.mean(data["views"]))
# print("Average Likes:", np.mean(data["likes"]))


# # ------------------------------
# # Subplots (4 graphs together)
# # ------------------------------

# plt.figure(figsize=(14,10))

# # Graph 1 - Category distribution
# plt.subplot(2,2,1)
# sns.countplot(x="category_id", data=data)
# plt.title("Video Category Distribution")

# # Graph 2 - Views vs Likes
# plt.subplot(2,2,2)
# sns.scatterplot(x="views", y="likes", data=data)
# plt.title("Views vs Likes")

# # Graph 3 - Top 10 most viewed videos
# plt.subplot(2,2,3)

# category_counts = data["category_id"].value_counts().head(6)

# plt.pie(
#     category_counts,
#     labels=category_counts.index,
#     autopct="%1.1f%%",
#     startangle=140
# )

# plt.title("Top Video Categories Share")
# # Graph 4 - Correlation Heatmap
# plt.subplot(2,2,4)
# sns.heatmap(data[["views","likes","dislikes","comment_count"]].corr(),
#             annot=True,
#             cmap="coolwarm")

# plt.title("Correlation Heatmap")

# plt.tight_layout()
# plt.show()



# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# data = pd.read_csv("USvideos.csv")

# # Dashboard title
# plt.figure(figsize=(14,10))
# plt.suptitle("YouTube Trending Video Analysis", fontsize=16)

# # Graph 1
# plt.subplot(2,2,1)
# sns.countplot(x="category_id", data=data)
# plt.title("Video Category Distribution")

# # Graph 2
# plt.subplot(2,2,2)
# sns.scatterplot(x="views", y="likes", data=data)
# plt.title("Views vs Likes")

# # Graph 3
# plt.subplot(2,2,3)
# category_counts = data["category_id"].value_counts().head(6)

# plt.pie(
#     category_counts,
#     labels=category_counts.index,
#     autopct="%1.1f%%"
# )
# plt.title("Top Video Categories Share")

# # Graph 4
# plt.subplot(2,2,4)
# sns.heatmap(data[["views","likes","dislikes","comment_count"]].corr(),
#             annot=True)

# plt.title("Correlation Heatmap")

# plt.tight_layout()
# plt.show()


# plt.tight_layout(rect=[0,0,1,0.95])
# plt.show()

# # Top 10 Channels Graph
# top_channels = data["channel_title"].value_counts().head(10)

# plt.figure(figsize=(8,5))
# sns.barplot(x=top_channels.values, y=top_channels.index)

# plt.title("Top 10 Channels with Most Trending Videos")
# plt.xlabel("Number of Videos")
# plt.ylabel("Channel Name")

# plt.show()




# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # load dataset
# data = pd.read_csv("USvideos.csv")

# # style
# sns.set_style("whitegrid")

# # dashboard size
# plt.figure(figsize=(18,10))
# plt.suptitle("YouTube Trending Video Analysis Dashboard", fontsize=20)

# # 1️⃣ Video Category Distribution
# plt.subplot(2,3,1)
# sns.countplot(x="category_id", data=data)
# plt.title("Video Category Distribution")
# plt.xticks(rotation=45)

# # 2️⃣ Views vs Likes
# plt.subplot(2,3,2)
# sns.scatterplot(x="views", y="likes", data=data)
# plt.title("Views vs Likes")

# # 3️⃣ Likes vs Dislikes
# plt.subplot(2,3,3)
# sns.scatterplot(x="likes", y="dislikes", data=data)
# plt.title("Likes vs Dislikes")

# # 4️⃣ Top Categories Pie Chart
# plt.subplot(2,3,4)
# top_categories = data["category_id"].value_counts().head(6)
# plt.pie(top_categories, labels=top_categories.index, autopct='%1.1f%%')
# plt.title("Top Video Categories Share")

# # 5️⃣ Correlation Heatmap
# plt.subplot(2,3,5)
# sns.heatmap(
#     data[["views","likes","dislikes","comment_count"]].corr(),
#     annot=True,
#     cmap="coolwarm"
# )
# plt.title("Correlation Heatmap")

# # 6️⃣ Top Channels
# plt.subplot(2,3,6)
# top_channels = data["channel_title"].value_counts().head(10)
# sns.barplot(x=top_channels.values, y=top_channels.index, palette="viridis")
# plt.title("Top 10 Channels with Most Trending Videos")

# plt.tight_layout(rect=[0,0,1,0.95])
# plt.show()









import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
data = pd.read_csv("USvideos.csv")

# style
plt.style.use("dark_background")
sns.set_style("darkgrid")

# figure
fig = plt.figure(figsize=(18,10))

# MAIN HEADING
fig.suptitle(
    "YouTube Trending Video Analysis Dashboard",
    fontsize=24,
    color="white",
    fontweight="bold"
)

# SUB HEADING
plt.figtext(
    0.5, 0.92,
    "Insights from US Trending Dataset (Views • Likes • Categories • Channels)",
    ha="center",
    fontsize=14,
    color="Black"
)

# 1️⃣ Category Distribution
plt.subplot(2,3,1)
sns.countplot(x="category_id", data=data, palette="viridis")
plt.title("Video Category Distribution")
plt.xticks(rotation=45)

# 2️⃣ Views vs Likes
plt.subplot(2,3,2)
sns.scatterplot(x="views", y="likes", data=data, alpha=0.6, color="cyan")
plt.title("Views vs Likes")

# 3️⃣ Likes vs Dislikes
plt.subplot(2,3,3)
sns.scatterplot(x="likes", y="dislikes", data=data, alpha=0.6, color="orange")
plt.title("Likes vs Dislikes")

# 4️⃣ Pie Chart
plt.subplot(2,3,4)
top_categories = data["category_id"].value_counts().head(6)
plt.pie(
    top_categories,
    labels=top_categories.index,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Top Video Categories Share")

# 5️⃣ Correlation Heatmap
plt.subplot(2,3,5)
sns.heatmap(
    data[["views","likes","dislikes","comment_count"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")

# 6️⃣ Top Channels
plt.subplot(2,3,6)
top_channels = data["channel_title"].value_counts().head(10)
sns.barplot(x=top_channels.values, y=top_channels.index, palette="magma")
plt.title("Top 10 Channels with Most Trending Videos")

plt.tight_layout(rect=[0,0,1,0.9])
plt.show()