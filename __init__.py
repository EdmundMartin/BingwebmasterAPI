import requests


class BingWebmasterException(Exception):
    pass


class BingWebmasterAPI:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://ssl.bing.com/webmaster/api.svc/json/'

    def __site_key_concat(self, site):
        return '?siteUrl={}&apiKey={}'.format(site, self.api_key)

    def __api_key_concat(self):
        return '?apiKey={}'.format(self.api_key)

    def __get_api_request(self, url, message):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.HTTPError:
            raise BingWebmasterException(message)
        else:
            return response.json()

    def get_crawl_stats(self, site):
        method = 'GetCrawlStats'
        target_url = '{}{}{}'.format(self.base_url, method, self.__site_key_concat(site))
        return self.__get_api_request(target_url, 'Error retrieving crawl stats, URL: {}, API_KEY: {}'.format(site, self.api_key))

    def get_keyword_stats(self, keyword, country="", language=""):
        method = 'GetKeywordStats'
        query_string = '&q={}&country={}&language={}'.format(keyword, country, language)
        target_url = '{}{}{}{}'.format(self.base_url, method, self.__api_key_concat(), query_string)
        return self.__get_api_request(target_url, 'Error retrieving keyword stats, API_KEY: {}'.format(self.api_key))

    def get_link_counts(self, page):
        method = 'GetLinkCounts'
        target_url = '{}{}{}'.format(self.base_url, method, self.__site_key_concat(page))
        return self.__get_api_request(target_url, 'Error retrieving link stats, URL: {}, API_KEY: {}'.format(page, self.api_key))

    def get_traffic_info(self, site, url):
        method = 'GetUrlTrafficInfo'
        url = '&url={}'.format(url)
        target_url = '{}{}{}{}'.format(self.base_url, method, self.__site_key_concat(site), url)
        return self.__get_api_request(target_url, 'Error retrieving link stats, Site: {}, Page: {}, API_KEY: {}'.format(site, url, self.api_key))

    def get_url_info(self, site, url):
        method = 'GetUrlInfo'
        url = '&url={}'.format(url)
        target_url = '{}{}{}{}'.format(self.base_url, method, self.__site_key_concat(site), url)
        return self.__get_api_request(target_url, 'Error retrieving URL info, Site: {}, Page: {}, API_KEY: {}'.format(site, url, self.api_key))

    def get_crawl_issues(self, site):
        method = 'GetCrawlIssues'
        target_url = '{}{}{}'.format(self.base_url, method, self.__site_key_concat(site))
        return self.__get_api_request(target_url, 'Error retrieving crawl info, Site: {}, API_KEY: {}'.format(site, self.api_key))
