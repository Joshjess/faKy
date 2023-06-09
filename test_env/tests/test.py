import pandas as pd
import faKy

'''
Create dummy data
'''
data = {
    'id': [0, 1],
    'object': [
        'sample sentence to test the library',
        'lorem ipsum the more you write the better yheaa'
    ]
}

df = pd.DataFrame(data)

'''
Import and apply functions respectively
'''
from faKy import process_text_readability
df['readability'] = df['object'].apply(process_text_readability)

from faKy import process_text_complexity
df['complexity'] = df['object'].apply(process_text_complexity)

'''
For multiple functions, the user can import the function and apply it to the dataframe in one line.
'''
from faKy import process_text_vader
df[['vader_neg', 'vader_neu', 'vader_pos', 'vader_compound']] = df['object'].apply(
                                                                        lambda x: pd.Series(process_text_vader(x)))

'''
It is important to import the input vector functions from the library, as they are used in the next step.
'''
from faKy import count_named_entities, count_ner_labels, create_input_vector_NER, ner_labels
df['tot_ner_count'] = df['object'].apply(count_named_entities)
df['ner_counts'] = df['object'].apply(count_ner_labels)
df['input_vector_ner'] = df['ner_counts'].apply(create_input_vector_NER)

'''
The individual NER labels can be added as follows.
'''
for tag in ner_labels:
    col_name = f'NER_{tag}'
    df[col_name] = df['input_vector_ner'].apply(
                                    lambda x: x[ner_labels.index(tag)] if tag in ner_labels else 0)

'''
The same applies to the POS tags.
'''
from faKy import count_pos, create_input_vector_pos, pos_tags
df['pos counts'] = df['object'].apply(count_pos)
df['input_vector_pos'] = df['pos counts'].apply(create_input_vector_pos)
for tag in pos_tags:
    col_name = f'pos_{tag}'
    df[col_name] = df['input_vector_pos'].apply(lambda x: x[pos_tags.index(tag)] if tag in pos_tags else 0)


print(df)