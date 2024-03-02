def hello(**kwargs):
    #print("hello " + kwargs['first'] + " " + kwartgs['last'])
    print("hello ", end="")
    for key, value in kwargs.items():
        print(value, end="")

hello(title="Mr.", first="oskar ", middle="zxc ", last="qwerty")