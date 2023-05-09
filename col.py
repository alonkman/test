def myZip(it1, it2):
    iter1 = iter(it1)
    iter2 = iter(it2)
    
    while True:
        try:
            elem1 = next(iter1)
            elem2 = next(iter2)
            
            yield (elem1, elem2)
        except StopIteration:

            return

list1 = ['nachman','yosef', 'maimon']
list2 = ['alon', 'ben', 'lidor']

zipped = myZip(list1, list2)

for tuple in zipped:
    print(tuple)
