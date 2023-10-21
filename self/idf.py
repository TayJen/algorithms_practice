import math
from typing import Dict, List

def idf(a: List[List[str]]) -> Dict[str, float]:
    """
        Inverse Document Frequency
        IDF(t) = log(N / (1 + n(t)))
        N - количество текстовых документов
        t - токен
        n(t) - количество документов в которых встречается токен t

        :param a: список документов, каждый документ это список токенов
    """
    N = len(a)
    dict_tokens = {}
    for doc in a:
        # So as not to repeat
        for token in set(doc):
            dict_tokens[token] = dict_tokens.get(token, 0) + 1

    for token in dict_tokens:
        idf_t = math.log10(N / (1 + dict_tokens[token]))
        dict_tokens[token] = idf_t

    return dict_tokens

if __name__ == "__main__":
    docs = [
        ["interview", "question"],
        ["repeat", "interview"]
    ]

    print(idf(docs))
