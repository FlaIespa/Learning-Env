#run_id = run[0] if run is not None else run
#all_histo = flat_map([load_s3_object_as_dict(path)
#for path in build_histo_paths(prefix=run_id)])

import requests as res
from bs4 import BeautifulSoup

def load_dados_pessoais(reload=False, run=None):
    if reload:
        logger.info("Recriando mesa de dados pessoais")
        create_dados_pessoais_table()

    #create and API with FormAssembly
    page = requests.get('https://app.formassembly.com/reports/view/4835013')

    txt = res.text
    status = res.status_code

    print(txt, res.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    page_title = soup.title.text  # gets you the text of the <title>(...)</title>
    page_body = soup.body
    page_head = soup.head

    rows_to_insert = []

    for dados in all_histo:
        sampleId = histo["sample_id"]
        researchNumber = histo.get('ResearchNumber', None)
        additiveScore = histo.get('AdditiveScore', None) or histo.get(
            'Additive score', None)
        overallArchitecture = histo.get('OverallArchitecture', None)
        mucosalIntegrity = histo.get('MucosalIntegrity', None)
        lymphoidImmune = histo.get('LymphoidImmune', None)
        inflammationSeverity = histo.get('InflammationSeverity', None)
        microbialOrganisms = histo.get('MicrobialOrganisms', None)

        doc = {
            "sampleId": sampleId,
            "researchNumber": researchNumber,
            "additiveScore": additiveScore,
            "overallArchitecture": overallArchitecture,
            "mucosalIntegrity": mucosalIntegrity,
            "lymphoidImmune": lymphoidImmune,
            "inflammationSeverity": inflammationSeverity,
            "microbialOrganisms": microbialOrganisms,
        }
        rows_to_insert.append(doc)

    Histopathology.upsert(rows_to_insert)
    logger.debug("Committed {} histopathologies".format(len(rows_to_insert)))