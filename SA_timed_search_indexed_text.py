from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import time

ix = open_dir("indexdir")

debut = time.time()

try:
    searcher = ix.searcher()

    i = 1
    while i <= 100:

        qp = QueryParser("content", schema=ix.schema)
        q = qp.parse("dog")

        with ix.searcher() as s:
            results = s.search(q, limit = None)

        q = qp.parse("cat")

        with ix.searcher() as s:
            results1 = s.search(q, limit = None)

        q = qp.parse("cow")

        with ix.searcher() as s:
            results2 = s.search(q, limit = None)

        q = qp.parse("beef")

        with ix.searcher() as s:
            results3 = s.search(q, limit = None)

        q = qp.parse("country")

        with ix.searcher() as s:
            results4 = s.search(q, limit = None)

        q = qp.parse("sunrise")

        with ix.searcher() as s:
            results5 = s.search(q, limit = None)

        q = qp.parse("snowstorm")

        with ix.searcher() as s:
            results6 = s.search(q, limit = None)

        q = qp.parse("festivities")

        with ix.searcher() as s:
            results7 = s.search(q, limit = None)

        q = qp.parse("running")

        with ix.searcher() as s:
            results8 = s.search(q, limit = None)

        q = qp.parse("gluttony")

        with ix.searcher() as s:
            results9 = s.search(q, limit = None)

        q = qp.parse("Arthur")

        with ix.searcher() as s:
            results10 = s.search(q, limit = None)

        i = i + 1

finally:
    searcher.close()

fin = time.time()

print((fin - debut)/1000)
