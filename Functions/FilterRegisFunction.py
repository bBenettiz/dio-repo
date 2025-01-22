import logging
import os
from azure.cosmos import CosmosClient
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Filtrando registros no CosmosDB.")

    try:
        endpoint = os.getenv("------")
        key = os.getenv("------")
        client = CosmosClient(endpoint, key)

        database_name = req.params.get("testdb")
        container_name = req.params.get("testcont")
        query = req.params.get("testquery")  

        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        results = container.query_items(query=query, enable_cross_partition_query=True)
        records = [item for item in results]

        return func.HttpResponse(json.dumps(records), status_code=200, mimetype="application/json")

    except Exception as e:
        logging.error(f"Erro ao filtrar registros: {e}")
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
