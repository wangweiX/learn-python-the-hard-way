def bob():
    #global me
    me = "locally defined"    # Defined only in local context
    print me
bob()
print me 