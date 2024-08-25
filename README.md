# NLP Parsers

This repository contains a two parsers I used for assignments in CS4661: Natural Language Processing. They are:

1. CFG Parser
2. Earley Parser

## CFG Parser

The CFG parser is a simple parser that uses a context-free grammar to parse a sentence. The parser uses a top-down approach to parse the sentence. I used the [NLTK ChartParser](https://www.nltk.org/api/nltk.parse.chart.html) module to implement this parser.

## Earley Parser

The Earley parser is a bottom-up parser that uses the Earley algorithm to parse a sentence. The Earley algorithm is a dynamic programming algorithm that uses a chart to parse a sentence.

### Acknowledgements

The code for the Earley parser is based on this [script](https://gist.github.com/bufas/65022d522b5bb31cc0d9). I have made some modifications to it to make it work with the grammar rules I have defined.
