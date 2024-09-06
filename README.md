# NLP Parsers

This repository contains a two parsers I used for assignments in CS4661: Natural Language Processing. They are:

1. CFG Parser
2. Earley Parser

## CFG Parser

The CFG parser is a simple parser that uses a context-free grammar to parse a sentence. The parser uses a top-down approach to parse the sentence. I used the [NLTK ChartParser](https://www.nltk.org/api/nltk.parse.chart.html) module to implement this parser.

The output looks like this:
```
----------------------------------------
Sentence #1: from Colombo
(S PP)
(S (PP P NP))
(S (PP (P from) NP))
(S (PP (P from) (NP N)))
(S (PP (P from) (NP (N Colombo))))
----------------------------------------
Sentence #2: Amal called Nimal
(S NP VP)
(S (NP N) VP)
(S (NP (N Amal)) VP)
(S (NP (N Amal)) (VP V NP))
(S (NP (N Amal)) (VP (V called) NP))
(S (NP (N Amal)) (VP (V called) (NP N)))
(S (NP (N Amal)) (VP (V called) (NP (N Nimal))))
----------------------------------------
...
```

Look at [CFG_Parse.txt](https://github.com/dan-niles/nlp-parsing/blob/main/output/CFG_Parse.txt) for the full output.

## Earley Parser

The Earley parser is a bottom-up parser that uses the Earley algorithm to parse a sentence. The Earley algorithm is a dynamic programming algorithm that uses a chart to parse a sentence.

The output (tsv file) looks like this:

<img width="431" alt="image" src="https://github.com/user-attachments/assets/35804db2-19d8-4f5a-8a40-b2df43e31b49">

Look at [Early_Parse.tsv](https://github.com/dan-niles/nlp-parsing/blob/main/output/Early_Parse.tsv) for the full output.

### Acknowledgements

The code for the Earley parser is based on this [script](https://gist.github.com/bufas/65022d522b5bb31cc0d9). I have made some modifications to it to make it work with the grammar rules I have defined.
