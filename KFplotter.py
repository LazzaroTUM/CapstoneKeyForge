import KFtoDataFrame as KFdf
import numpy  as np
import matplotlib.pyplot as plt

df = KFdf.loadDataFrame()


def simplePlot():
    plt.plot(np.arange(df.shape[0]), list(df['wins']))
    plt.title("official game won by decks in local data")
    plt.show()



