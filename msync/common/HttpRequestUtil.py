import logging

import requests

logger = logging.getLogger('log')


class HttpRequestUtil:

    @staticmethod
    def get(url, headers, cookies):
        logger.info("[GET]:%s\n[Headers]:%s\n", url, headers)

        response = requests.request("GET", url, headers=headers, cookies=cookies)
        if response.status_code != 200:
            logger.error("[status_code]:%s\n[headers]:%s\n[content]:%s\n", response.status_code, response.headers,
                         response.text)

        logger.info("[response]:%s\n", response.text)
        return response

    @staticmethod
    def post(url, headers, data, cookies):
        logger.info("[POST]:%s\n[Headers]:%s\n[Data]:%s\n", url, headers, data)

        response = requests.request("POST", url, headers=headers, data=data, cookies=cookies)
        if response.status_code != 200:
            logger.error("[status_code]:%s\n[headers]:%s\n[content]:%s\n", response.status_code, response.headers,
                         response.text)

        logger.info("[response]:%s\n", response.text)
        return response

    @staticmethod
    def put(url, headers, data, cookies):
        logger.info("[PUT]:%s\n[Headers]:%s\n[Data]:%s\n", url, headers, data)

        response = requests.request("PUT", url, headers=headers, data=data, cookies=cookies)
        if response.status_code != 200:
            logger.error("[status_code]:%s\n[headers]:%s\n[content]:%s\n", response.status_code, response.headers,
                         response.text)

        logger.info("[response]:%s\n", response.text)
        return response
