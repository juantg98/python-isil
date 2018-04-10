def principal():
   # mydict = {}
    mydict = {
        "red": "ff0000",
        "blue": "azul",
        "blanco": "000000",
    }
    mydict["negro"] = "ffffff"
    print(mydict)

    print(list(mydict.keys()))
    print(list(mydict.values()))
    import ipdb
    ipdb.set_trace()
    for key, value in mydict.items():
        print(key, "-"*3 + ">", value)

         

if __name__ == '__main__':
    principal()