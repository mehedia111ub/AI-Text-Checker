# Utility functions for the AI Text Checker application

# Import necessary libraries
import matplotlib.pyplot as plt

# Function to plot a pie chart of AI vs Human scores
def plot_pie(ai_score, human_score):
    labels = ['AI Generated', 'Human Written']
    sizes = [ai_score, human_score]

    fig, ax = plt.subplots()
    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90
    )
    ax.axis('equal')
    return fig

# Function to count words in a given text
def word_count(text):
    return len(text.split())