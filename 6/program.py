import json


def load_data():
    """
    Reads from a JSON file of sports match statistics used later in the program
    """
    with open('sports.json') as file:
        data = json.loads(file.read())
        return data["data"]


def filter_results(data, **kwargs):
    """
    Iterates over every search keyword and keyword value, narrowing down result list
    until only matches of all conditions are left
    """

    for key, val in kwargs.items():
        data = list(filter(lambda x: val.lower() in x[key].lower(), data))

    return data


def __main__():
    """
    Main program wrapper for all application logic
    """
    data = load_data()
    keywords = { "team": "Minnesota Wild", "sport": "hockey" }
    matches = filter_results(data, **keywords)

    # default data assumes they won't match
    statusCode = 404
    statusMessage = ""

    if matches:
        statusCode = 200
        data = data

        for match in matches:
            statusMessage += f"\n\n Matching result - The {match['team']} {match['sport'].lower()} team had a {match['result'].lower()} against {match['vs']}, {match['score']}, on {match['date']}"
    else:
        statusMessage = "No results found - if searching sports, be sure your sport is a valid option among football, hockey, or soccer"

    return {
        "statusCode": statusCode,
        "statusMessage": statusMessage,
        "data": matches
    }



# Activates core program
if __name__ == "__main__":
    __main__()