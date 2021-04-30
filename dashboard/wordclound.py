#for importing data and wrangling
import pandas as pd
import numpy as np

#for plotting images & adjusting colors
import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image


comment_words = ["ai", "Khô.n?g", "cugRƯƠNGn Cùng", "flavor", "flavors","one", "onetwo", "three"]
# comment_words = 'mot hai ba boob nam sau bay tam'
# comment_words = 'Chi Là Không\nCùng Nhau - \nTĂNG \nPHÚC ft TRƯƠNG THẢO NHI'
# comment_words = [("mot  hai",40),("dam ba",29), ("bA",21),("a  bon nam sa",13),("u  bay tam chin muoi ",12)]
# wordcloud = WordCloud(width = 800, height = 800,
#                 background_color ='white',
#                 stopwords = stopwords,
#                 min_font_size = 10,contour_width=4).generate_from_frequencies(comment_words)
  
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10,contour_width=4,regexp=r"\w[\w-]+").generate(' '.join(comment_words))
# wordcloud = wordcloud.fit_words(comment_words)
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud,interpolation='bilinear',aspect="auto")
plt.axis("off")
  
plt.show()