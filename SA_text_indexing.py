import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StemmingAnalyzer


def createSearchableData(root):

    stem_ana = StemmingAnalyzer()
    schema = Schema(title=TEXT(analyzer=stem_ana, stored=True), path=ID(analyzer=stem_ana),
                    content=TEXT(analyzer=stem_ana), textdata=TEXT(analyzer=stem_ana))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    # Creating a index writer to add document as per schema
    ix = create_in("indexdir", schema)
    writer = ix.writer()

    filepaths = [os.path.join(root, i) for i in os.listdir(root)]
    for path in filepaths:
        fp = open(path, 'r')
        print(path)
        text = fp.read()
        writer.add_document(title=path.split("\\")[1], path=path,
                            content=text, textdata=text)
        fp.close()
    writer.commit()


import time

root = "E:\etext00"
debut = time.time()
createSearchableData(root)
fin = time.time()
print(fin - debut)
