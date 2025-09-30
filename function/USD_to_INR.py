def covnersion(usd):
    con= 87.09*usd
    print(con)
    return con
covnersion(2)
# usd input
usd_input=float(input("enter the USD value for conversion: "))
# output
inr_output=covnersion(usd_input)
print(usd_input,"USD equal to", inr_output,"INR")