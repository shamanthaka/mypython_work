#Remove missing data

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "",
             "Ecuador", "", "", "Venezueala"]

data = list(filter(None, countries))

print("Removing empty " + str(data))