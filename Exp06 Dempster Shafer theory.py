def predict(df, combine):
    best = 0.0
    bestClass = frozenset({})
    for c in combine.all():
        if (combine[c] > best):
            best = combine[c]
            bestClass = c
    return (bestClass, best)

countFail = 0
countPredict = 0
ms = {}
for index, row in df.iterrows():
    sample = row
    for f in fields:
        hypothesisCount = dict.fromkeys(powerset(df.Class.unique()), 0)
        h = hypothesis(df, classRange, f, sample[f])
        hypothesisCounts(hypothesisCount, h, singletons, frame)   
        ms[f] = MassFunction(hypothesisCount).normalize()
        
    combine_mf = functools.reduce(lambda a,b: a & b, ms.values())

    (bestClass, best) = predict(df, combine_mf)
    if (bestClass in singletons) and (best > 0.8):
        countPredict += 1
        if bestClass != frozenset({sample.Class}):
            countFail +=1
    else:
        fsvClass = min_dist_attr(sdf, fsv_attr, list(bestClass), sample)
        if (best > 0.8):
            countPredict += 1
            if fsvClass != sample.Class:
                countFail +=1
    
print('total rows', df.Class.count())
print('total predicted', countPredict)
print('total fail predicted', countFail)
print('accuracy rate', (countPredict - countFail)/(countPredict*1.0))