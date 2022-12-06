import string
import json
from redshift_conn import session, redshift_engine, namespace_table
from asimetrix_client import asimetrix_client
from schema.barn import create_barn_table, Barn

def load_dados_pessoais(reload=False, run=None):
    if reload:
        logger.info("Re-creating dados pessoais table")
        create_dados_pessoais_table()

    #Get dados pessoais data from FormAssembly
    logger.info("Getting  data from FormAssembly")
    barns = asimetrix_client.get_cerberus(endpoint='/master/barn/')

    logger.info("Inserting barn data into barn table")
    rows_to_insert = []
    for row in barns:
        barn_doc = {
                "barnId": row['id'],
                "barnName": row['name'],
                "farmId": row['farm'],
                "guideId": row['guide'],
                "barnAliases": json.dumps(row['aliases']),
                "createdDate": row['createdDate'],
                "updatedDate": row['updatedDate'],
                "effectiveTemperature": row['effective_temperature'],
                "outsideTemperature": row['outside_temperature']
            }
        rows_to_insert.append(barn_doc)

    Barn.upsert(rows_to_insert)
    logger.debug("Committed {} barn docs".format(len(rows_to_insert)))