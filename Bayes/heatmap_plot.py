import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True)

plt.rc('font', family='Times New Roman')
plt.style.use('ggplot')

fig, ax = plt.subplots()

matrix = np.array([[8431, 1161], [674, 4353]], dtype=np.int)
ax.imshow(matrix)
sns.heatmap(matrix, annot=True, fmt='.20g', ax=ax)

ax.set_ylabel("True Label")
ax.set_xlabel("Predicted Label")
plt.xticks([0.5, 1.5], ['spam', 'ham'])
plt.yticks([0.5, 1.5], ['spam', 'ham'])
fig.savefig("heatmap.png", dpi=300)
# plt.show()
