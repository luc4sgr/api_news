def paginate(data: list, page: int = 1, per_page: int = 10) -> dict:
    total = len(data)
    start = (page - 1) * per_page
    end = start + per_page
    items = data[start:end]
    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "items": items
    }
