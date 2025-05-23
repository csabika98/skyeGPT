# import common.ChromaClient as ChromaClient
# from typing import List
#
# from . import Confluence2Text
# from . import ImportFromS3
# from . import Markdown2VectorDB
#
#
# rag_settings_store = {}
#
#
# def setup_rag_pipeline(
#         collection_name: str,
#         should_import: bool,
#         folder_path: str,
#         k_nearest_neighbors: int,
#         markdown_split_headers: List[str],
#         gpt_model: str,
#         gpt_temperature: float,
#         gpt_developer_prompt: str,
#         documentation_selector: dict[str, bool],
#         s3_bucket: str,
#         s3_folder_prefix: str,
#         s3_local_folder: str,
#         confl_api_endpoint: str,
#         confl_space_key: str,
#         confl_save_path: str
# ):
#     save_settings_to_settings_store(
#         k_nearest_neighbors,
#         gpt_model,
#         gpt_temperature,
#         gpt_developer_prompt
#         )
#
#     ChromaClient.create_collection_if_needed(collection_name)
#
#     if documentation_selector.get("s3") is True:
#         ImportFromS3.download_files_from_s3_bucket(
#             s3_bucket,
#             s3_folder_prefix,
#             s3_local_folder
#         )
#     if documentation_selector.get("innoveo_partner_hub") is True:
#         Confluence2Text.download_public_confluence_as_text(
#             confl_api_endpoint,
#             confl_space_key,
#             confl_save_path
#         )
#
#     if should_import:
#         print("Import is enabled. Starting to import...")
#         Markdown2VectorDB.scan_and_import_markdowns_from_folder(
#             collection_name,
#             folder_path,
#             markdown_split_headers
#         )
#     else:
#         print("Import is disabled. Proceeding...")
#     number_of_documents = ChromaClient.number_of_documents_in_collection(collection_name)
#     print(f"Collection {collection_name} is ready to use. There are {number_of_documents} loaded to the collection.")
#     return number_of_documents
#
#
# def save_settings_to_settings_store(
#         k_nearest_neighbors: int,
#         gpt_model: str,
#         gpt_temperature: float,
#         gpt_developer_prompt: str
# ):
#     rag_settings_store["k_nearest_neighbors"] = k_nearest_neighbors
#     rag_settings_store["gpt_model"] = gpt_model
#     rag_settings_store["gpt_temperature"] = gpt_temperature
#     rag_settings_store["gpt_developer_prompt"] = gpt_developer_prompt
