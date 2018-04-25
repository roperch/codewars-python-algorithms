# test cases:
cannonsReady({'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}) --> "Fire!"
cannonsReady({'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}) --> "Shiver me timbers!"


def cannons_ready(gunners):
    for item in gunners:
        if gunners[item] == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'
