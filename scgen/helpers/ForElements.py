def hasAllElements(this, of):
    thisElements = set(this)
    ofElements = set(of)
    return thisElements.issuperset(ofElements)