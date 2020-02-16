result = dict()

cat = "test"
obj = [1, 2]
result[cat] = result[cat] + [obj] if cat in result.keys() else [obj]
result[cat] = result[cat] + [obj] if cat in result.keys() else [obj]
print(result)