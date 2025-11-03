description = "strings are..."
# Make it all upper case
description_upper = description.upper()
# Replace the word "ARE" (since it's now uppercase) with "IS"
description_replaced = description_upper.replace("ARE", "IS")
# Print just the word "STRINGS"
print(description_replaced.split()[0])
