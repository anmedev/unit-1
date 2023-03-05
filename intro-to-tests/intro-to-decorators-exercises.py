# Intro to Decorators - id: 2f98105e-287d-464d-9429-9f015ba2b249
# Select the line that applies a decorator.

# 1   def prechorus(func):
# 2       def lyrics():
# 3           print("So when the night falls, my lonely heart calls...")
# 4           func()
# 5       return lyrics
# 6
# 7
# 8   @prechorus
# 9   def chorus():
# 10      print("Oh, I wanna dance with somebody, I wanna feel the HEAT with somebody..")
# 11      print("Yeah, I wanna dance with somebody... with somebody who loves me!")
# 12
# 13
# 14  chorus()

# Answer: 8

# Intro to Decorators - id: ad99bf78-de0d-43a8-a054-5843c210cbdd
# Select the line that applies a decorator.

# 1    def concatenate_words(format_str_func):
# 2        def inner(values):
# 3            return ''.join(format_str_func(values))
# 4        return inner
# 5
# 6
# 7    @concatenate_words
# 8    def make_camel_case(string):
# 9        return [word.capitalize() for word in string.split(' ')]
# 10
# 11
# 12   print(make_camel_case("hello world"))

# Answer: 7