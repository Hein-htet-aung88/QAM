month_conversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",

}
print(month_conversion["Jul"])
print(month_conversion.get("Jan"))
print(month_conversion.get("lol","Not a valid key"))
