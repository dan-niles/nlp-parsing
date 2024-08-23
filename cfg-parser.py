INDEX_NO = ""

import nltk
from nltk import CFG, Tree

# Define the grammar
grammar = CFG.fromstring("""
    S ->  NP VP | NP | PP | VP
    NP -> DT N | DT JJ N |  N
    VP -> V | NP V | V NP | V PP
    PP -> P NP | P VP
    DT -> 'a' | 'this'
    N -> 'flight' | 'Nimal' | 'Colombo' | 'call' | 'plane' | 'Kamal' | 'Amal'
    V -> 'made' | 'wanted' | 'leaving' | 'called' | 'call'
    P -> 'from' | 'on' | 'to'
    JJ -> 'morning' | 'jet'
""")

# Sentences to be parsed
sentences = [
    "from Colombo",
    "Amal called Nimal",
    "from a flight",
    "Amal made a call",
    "Nimal wanted a morning flight",
    "leaving on a jet plane",
    "Kamal wanted to call Nimal"
]

# Create a parser
parser = nltk.ChartParser(grammar)

# Traverse tree in preorder
def get_preorder_string(tree):
    preorder_string = " "
    if tree.height() > 1: preorder_string = " ("
    preorder_string += tree.label()
    for subtree in tree:
        if isinstance(subtree, str):
            preorder_string += " " + subtree
        else:
            preorder_string += "" + get_preorder_string(subtree)
    if tree.height() > 1: preorder_string += ")"
    return preorder_string

# Progressively build tree
def get_progressive_trees(tree):
    subtrees = list(tree.subtrees())
    tree_strings = []

    for i in range(len(subtrees)):
        # Create a new tree up to the i-th subtree
        new_tree = tree.copy(deep=True)
        for j, subtree in enumerate(new_tree.subtrees()):
            if j > i:
                subtree.clear()  # Remove all subtrees after the i-th one

        tree_strings.append(get_preorder_string(new_tree).strip())

    return tree_strings


# Function to parse and write output to file
def parse_sentences_to_file(sentences, filename):
    with open(filename, 'w') as file:
        file.write("-" * 40 + "")
        for i, sentence in enumerate(sentences):
            file.write(f"\nSentence #{i+1}: {sentence}")
            for tree in parser.parse(sentence.split()):
                tree_strings = get_progressive_trees(tree)
                for tree_str in tree_strings:
                    file.write("\n" + tree_str )
            if i+1 != len(sentences): file.write("\n" + "-" * 40)

# Parse the sentences and write to a file
output_file = f'/content/{INDEX_NO}_CFG_Parse.txt'
parse_sentences_to_file(sentences, output_file)

