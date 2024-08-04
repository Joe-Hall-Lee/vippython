scores = (('评书新势力作品集', '34'), ('水浒全传(SK)', '43'), ('端木范读SK《道德经》标准朗诵',
                                                               '21'), ('静心养性&端木精品雅读(SK)', '16'),
          ('欧美幼儿经典读物(SK英文版)', '16'))
for index, item in enumerate(scores):
    print(index + 1, '.', end=' ')
    for score in item:
        print(score, end=' ')
    print()
