import requests
from app import db
from app.models import Url

def count_words_at_url(url, to_store_in_db=1):   
    errors = []
    resp = requests.get(url)
    count = len(resp.text.split())
    try:
        result = Url(
            url = url,
            count = count
        )
        if(to_store_in_db):
            db.session.add(result)
            db.session.commit()

            print(result.id)
            return result.id

        return result

    except:
        errors.append("Unable to add url to database.")
        return {"error": errors}