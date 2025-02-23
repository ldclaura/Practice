###


#nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#nesting a list in a dictionary
#key is string, value is list
travel_log = {
    "France" : {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Essen"], "total_visits" : 12},
}

print(travel_log) #is this correct?

#nesting dictionary in list
travel_log = [
    {
        "country" : "France",
          "cities_visited": ["Paris", "Lille", "Dijon"],
            "total_visits" : 12
            }
    {
        "country" : "Germany",
          "cities_visited": ["Berlin", "Hamburg", "Essen"],
            "total_visits" : 12
            }
]

print(travel_log) #is this correct?