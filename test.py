def test(*args, **kwargs):
    for i in args:
        print(i)

    for j in kwargs:
        print(j, kwargs[j])


dc = {
    "sorted": True,
    "list": [1,4,5]
}

test(**dc)
