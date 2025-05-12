# Parameters
def say_hello(name = 'John', emoji = ':)'):
    print(f"Hey {name} {emoji}")


# Arguments
# Order matters !
say_hello('Bob', '😊')
say_hello('😊', 'James')

# Keyword Arguments
# say_hello(emoji='😊', name = 'Bebe')
say_hello(emoji = '😊')

