import logging
import os
import json
from azure.cosmos import CosmosClient, PartitionKey
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Salvando registros no CosmosDB.")

    try:
        endpoint = os.getenv("-------")
        key = os.getenv("-------")
        client = CosmosClient(endpoint, key)

        database_name = req.params.get("testdb")
        container_name = req.params.get("testcont")
        item = req.get_json()  

        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        container.upsert_item(item)

        return func.HttpResponse(f"Registro salvo no container {container_name}.", status_code=200)

    except Exception as e:
        logging.error(f"Erro ao salvar registro: {e}")
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
