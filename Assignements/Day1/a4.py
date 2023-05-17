'''
You have list of Dictionaries like following

    Task is to print body from attributes key on the order of oldest to latest by filtering updated date_time
'''
varList = [
    {
        "meta": {
            "totalPages": 13
        },
        "data": [
            {
                "type": "articles",
                "id": "3",
                "attributes": {
                        "title": "JSON:API paints my bikeshed!",
                        "body": "The shortest article. Ever.",
                        "created": "2015-05-22T14:56:29.000Z",
                        "updated": "2015-05-25T14:56:28.000Z"
                }
            }
        ],
        "links": {
            "self": "http://example.com/articles?page[number]=3&page[size]=1",
            "first": "http://example.com/articles?page[number]=1&page[size]=1",
            "prev": "http://example.com/articles?page[number]=2&page[size]=1",
            "next": "http://example.com/articles?page[number]=4&page[size]=1",
            "last": "http://example.com/articles?page[number]=13&page[size]=1"
        }
    }, {
        "meta": {
            "totalPages": 13
        },
        "data": [
            {
                "type": "articles",
                "id": "3",
                "attributes": {
                        "title": "JSON:API paints my carshed!",
                        "body": "The mini article. Ever.",
                        "created": "2015-05-20T14:56:29.000Z",
                        "updated": "2015-05-22T14:56:28.000Z"
                }
            }
        ],
        "links": {
            "self": "http://example.com/articles?page[number]=3&page[size]=1",
            "first": "http://example.com/articles?page[number]=1&page[size]=1",
            "prev": "http://example.com/articles?page[number]=2&page[size]=1",
            "next": "http://example.com/articles?page[number]=4&page[size]=1",
            "last": "http://example.com/articles?page[number]=13&page[size]=1"
        }
    }, {
        "meta": {
            "totalPages": 13
        },
        "data": [
            {
                "type": "articles",
                "id": "3",
                "attributes": {
                        "title": "JSON:API paints my carshed!",
                        "body": "The mini article. Ever.",
                        "created": "2015-05-20T14:56:29.000Z",
                        "updated": "2015-05-22T12:56:28.000Z"
                }
            }
        ],
        "links": {
            "self": "http://example.com/articles?page[number]=3&page[size]=1",
            "first": "http://example.com/articles?page[number]=1&page[size]=1",
            "prev": "http://example.com/articles?page[number]=2&page[size]=1",
            "next": "http://example.com/articles?page[number]=4&page[size]=1",
            "last": "http://example.com/articles?page[number]=13&page[size]=1"
        }
    }
    , {
        "meta": {
            "totalPages": 13
        },
        "data": [
            {
                "type": "articles",
                "id": "3",
                "attributes": {
                        "title": "JSON:API paints my carshed!",
                        "body": "The mini article. Ever.",
                        "created": "2015-05-20T14:56:29.000Z",
                        "updated": "2015-05-22T14:56:28.000Z"
                }
            }
        ],
        "links": {
            "self": "http://example.com/articles?page[number]=3&page[size]=1",
            "first": "http://example.com/articles?page[number]=1&page[size]=1",
            "prev": "http://example.com/articles?page[number]=2&page[size]=1",
            "next": "http://example.com/articles?page[number]=4&page[size]=1",
            "last": "http://example.com/articles?page[number]=13&page[size]=1"
        }
    }
]
varTempList = list()
for i in varList:
    varDate = i["data"][0]['attributes']["updated"][:10]
    varTime = i["data"][0]['attributes']["updated"][11:-5]
    varBody = i["data"][0]['attributes']["body"]
    varTempList.append((varDate,varTime,varBody))
print("****")   
print(varTempList) 
sorted_list = sorted(varTempList,key=lambda x: (x[0],x[1]))
print(sorted_list)
print("****")   

'''
python3 a4.py
'''

