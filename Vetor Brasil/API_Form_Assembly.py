import requests
import boto3

from logger import logger

_VERSION_API = "v2"
_URL_BASE = "https://app.formassembly.com/forms"

class FormAssembly:
    """this class performs requests to FormAssembly"""

    def __init__(self, url: str = _URL_BASE, version: str = _VERSION_API):
        self.url = url
        self.version = version
        self.token = None
        self.get_asimetrix_token()

    def get_asimetrix_token(self):

        # You need to have your AWS credentials set up in your environment
        self.token = boto3.client("ssm", region_name="us-east-1").get_parameter(Name="microservices_token",WithDecryption=True)["Parameter"]["Value"]
        if self.token:
            logger.debug("Asimetrix Token acquired")
        else:
            logger.error("Asimetrix Token not acquired")


    def get_cerberus(self,endpoint: str, params=None) -> list:
        """Helper function to make GET requests to the cerberus endpoint
        Returns a list of dictionaries containing the response data.
        The `endpoint` parameter must be the endpoint route after the version number.
        Examples
        --------
        get_cerberus("/master/company/", {"company_name": "example"})
        Logic
        """
        #TODO: Add retry logic

        session = requests.Session()
        urlreq = f"{self.url}{self.version}{endpoint}"
        if params is None:
            params = {}
        headers = {
            "Authorization": "Bearer " + self.token,
            "Accept": "application/json",
        }

        resp = session.get(urlreq, params=params, headers=headers)

        logger.debug("Unprocessed results of get_cerberus()")
        logger.debug(f"{resp}")

        if resp.status_code != 200:
            logger.warning(resp.status_code)
            logger.warning(resp.text)
            return None

        resp = resp.json()

        if "results" not in resp.keys():
            return resp

        results = resp["results"]

        while resp["next"] is not None:
            urlreq = resp["next"]
            resp = session.get(urlreq, headers=headers).json()
            results.extend(resp["results"])

        return results

asimetrix_client = AsimetrixClient()