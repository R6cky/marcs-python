def paginate(query, page: int = 1, limit: int = 10):
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "data": items,
        "total": total,
        "page": page,
        "limit": limit
    }