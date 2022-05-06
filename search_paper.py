import sematic_API
import sys
import json

#They are all parameters
#you can choose whcih parameters you want
fields_cate='paperId,externalIds,url,title,abstract,venue,year,referenceCount,citationCount,influentialCitationCount,isOpenAccess,fieldsOfStudy,s2FieldsOfStudy,authors'
data = sematic_API.paper_search(offset=0,
                                limit=None,
                                fields=fields_cate,
                                query='alcohol'
                                )
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)
print('finish')
