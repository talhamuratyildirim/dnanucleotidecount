"""
**DNA Nucleotide Count Web App**
"""

# Import Libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


# Create image variable that will be shown on top of the page
image = Image.open("dnastructure.jpg")

st.image(image, use_column_width=True)

st.write("""
# **DNA Nucleotide Count Web Application**

This application counts the nucleotide composition of query DNA!
***
""")

st.header("Enter DNA Sequence")

dna_sequence_input = ">DNA Sequence\ngcaacgcaaagcgtccgttgtagatcggttcaggtgtatatcacccggttcacgacccaatatatgcctcagtaacaggtattgaacccctcaggtatag"

dna_sequence = st.text_area("Please enter DNA sequence starting from the second line!", dna_sequence_input, height=300)
dna_sequence = dna_sequence.splitlines()
dna_sequence = dna_sequence[1:] # Skips the first line, sequence name, of dna_seqeunce_input (>DNA Sequence)
dna_sequence = "".join(dna_sequence) # Concatenates all DNA sequence to one string 

st.write('''
***
''')

# Shows the DNA Sequence string
st.header("INPUT (DNA Query)")
dna_sequence

st.header("OUTPUT (DNA Nucleotide Count)")

st.subheader("1. Print Dictionary")

# Creating a dictionary function 
def dna_dic(dna_sequence):
    dic = {
        "A": dna_sequence.count("a"),
        "G": dna_sequence.count("g"),
        "C": dna_sequence.count("c"),
        "T": dna_sequence.count("t")
    }
    return dic

X = dna_dic(dna_sequence)

X

st.subheader("2. Print Numbers of Nitrogenous Bases")
st.write("There are " + str(X['A']) + " adenine (A) in this DNA sequence.")
st.write("There are " + str(X['G']) + " guanine (G) in this DNA sequence.")
st.write("There are " + str(X['C']) + " cytosine (C) in this DNA sequence.")
st.write("There are " + str(X['T']) + " thymine (T) in this DNA sequence.")

st.subheader("3. Display a DataFrame")
df = pd.DataFrame.from_dict(X, orient='index') # orient='index', makes keys rows
# df
df = df.rename({0: "count"}, axis='columns')
# df
df.reset_index(inplace=True) # inplace=True, modifies the df, not create a new one
# df
df.rename({"index": "nucleotide"}, axis='columns', inplace=True)
st.write(df)

# Display Bar Chart using Altair
st.subheader("Display a Bar Chart")
bar_chart = alt.Chart(df).mark_bar().encode(x='nucleotide', y='count') # mark_bar makes it bar plot
# st.write(bar_chart)
bar_chart = bar_chart.properties(width=alt.Step(80)) # increases the width of the bar
st.write(bar_chart)
