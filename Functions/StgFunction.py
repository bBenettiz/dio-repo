import logging
import os
from azure.storage.blob import BlobServiceClient
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Salvando arquivos no Storage Account.")

    try:
        
        connection_string = os.getenv("-----------")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        
        container_name = req.params.get("container")
        file_name = req.params.get("file_name")
        file_content = req.get_body()  

        
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        blob_client.upload_blob(file_content, overwrite=True)

        return func.HttpResponse(f"Arquivo {file_name} salvo no container {container_name}.", status_code=200)

    except Exception as e:
        logging.error(f"Erro ao salvar arquivo: {e}")
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
