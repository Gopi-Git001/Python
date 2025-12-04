D = {'Monday': 16, 'Tuesday': 17,'Wednesday': 18,'Thurday': 19,'Friday': 20,'Saturday': 21,'Sunday': 22 }

print(D.items())

for i,j in D.items():
    print(i)
    print(j)
    
print(D.keys())
    
#three functions for Dictionaries keys ,values and Items  , Dictionaries are also having Mutations 



nested = {
    "user": {
        "id": 123,
        "name": "Alice",
        "contact": {
            "email": "alice@example.com",
            "phone": "+1-555-0100"
        }
    },
    "settings": {
        "theme": "dark",
        "notifications": {
            "email": True,
            "sms": False
        }
    },
    "projects": [
        {
            "id": 1,
            "title": "Alpha",
            "tags": ["ml", "api"],
            "owner": {"id": 123, "role": "admin"}
        },
        {
            "id": 2,
            "title": "Beta",
            "tags": [],
            "owner": {"id": 456, "role": "viewer"}
        }
    ]
}


print(nested["projects"][0]['id'])
