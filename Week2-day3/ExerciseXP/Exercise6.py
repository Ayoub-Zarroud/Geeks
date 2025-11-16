import datetime

def minutes_lived(birthdate_str):
    # Example format: "2002-06-15"
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.datetime.now()

    diff = now - birthdate
    minutes = diff.total_seconds() / 60

    print(f"You have lived approximately {int(minutes)} minutes.")

minutes_lived("2002-06-15")
