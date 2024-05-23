def languages():
    yield "Python"
    yield "PHP"
    yield "Ruby"
    yield "Java"
    yield "C"
    yield "C#"
    yield "Javascript"

lan = languages()
print(next(lan))
print(next(lan))
print(next(lan))
lan.close()
print(next(lan))
lan.throw(StopIteration)

