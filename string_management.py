import re
import pandas as pd
import numpy as np


def linebreak(txt = str):
    """
    This function detect systematica errors and rectify them
    """
    pattern = [['—\s', ' '], ['‘‘\s','"'], ['\s‘‘','"'], ['-\s', ' '], ['k', 'me']]
    for i in pattern:
        txt = re.sub(i[0], i[1], txt)
    return txt
def merge_linebreak(col):
    pass

# For example:
df = pd.DataFrame({'text': ['kill-','at', '-kill-', '3'], 'dan':['66', '87', '64', '4']})
df_serie = df['text']
df_serie = df_serie.str.findall('-$')
index_to_replace = np.array(df_serie.index[df_serie.str.len() != 0].tolist())
index_to_drop = index_to_replace + 1
substitute = []
for i in index_to_drop:
    substitute.append(df['text'][i])
df.drop(index = index_to_drop, inplace = True)
for i, j in enumerate(index_to_replace):
    df['text'][j] = df['text'][j][:-1] + substitute[i]

print(df)
"""
loop over the df series
find the index of words end with a dash
store the text at index + 1 to a new list
drop index + 1
and combine back to the original df
"""




# txt = " ‘‘Is this made ground?” he asked, a little anxiously. . Marcella laughed back: ‘‘ Yes! the Lord made it —with a very little help from my grandpa. This hillside was in what we country folks call benches—he flattened the benches a little, filled in a few places, and turfed over the slopes, so they should not wash. At least, he began to do it— Uncle-Major has followed the pattern set him. We are mighty proud of our orchards—also of the fact that the Hawk’s Nest is a brand that always fetches the top of the market. Yousee nobody can quite touch us in quality, because nobody has got just such another hillside. See! It spreads in a big half moon. There are seventy-five acres planted. We need not go higher. The early peaches, there at the top, went to market three months back. Look down and along these rows, though, and tell me if New York can show anything more beautiful?”"
# print(linebreak(txt))