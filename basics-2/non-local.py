def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('Inner', x)

    inner()
    print('outer', x)
outer()