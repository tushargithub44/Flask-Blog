from flask import current_app

def add_to_index(index,model):
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, id=model.id)


def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        print('search.py if not')
        return [], 0
    print('query_index in one search.py ')
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match':{'query': query, 'fields': ['*']}},
                        'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    print('ids are :')
    print(ids)
    return ids, search['hits']['total']['value']