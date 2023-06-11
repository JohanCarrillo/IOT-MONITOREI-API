def monitoreoEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "lugar": str(item["lugar"]),
        "autor": str(item["autor"]),
        "temperatura": item["temperatura"],
        "humedad": item["humedad"],
        "createdAt": str(item["createdAt"]),
        "updateddAt": str(item["updatedAt"]),
    }

def muchosMonitoreosEntity(items) -> list:
    return [monitoreoEntity(item) for item in items]