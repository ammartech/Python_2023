def is_64_fit(num):
    return (num>=-(2**63)-1 and num<=(2**63)-1)

if __name__== "__main__":
    num=48757493
    print(is_64_fit(num))
