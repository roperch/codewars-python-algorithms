# test cases:
# alias_gen('Mike', 'Millington'), 'Malware Mike'
# alias_gen('Fahima', 'Tash'), 'Function T-Rex'
# alias_gen('Daisy', 'Petrovic'), 'Data Payload'
# alias_gen('Barny', 'White'), 'Beta Worm'
# alias_gen('Hank', 'Kutz'), 'Half-life Killer'
# alias_gen('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'
# alias_gen('walter', 'white'), 'WiFi Worm'

def alias_gen(f_name, l_name):
    try:
      f_name = f_name.upper()
      l_name = l_name.upper()
      f = f_name[0]
      l = l_name[0]
      return "{} {}".format(FIRST_NAME[f], SURNAME[l])
    except KeyError:
        return "Your name must start with a letter from A - Z."
