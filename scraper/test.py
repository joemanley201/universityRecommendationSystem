__author__ = 'joemanley'
import requests
import json

def get_json_response_for_request_uri(uri):
    '''
    Forms JSON from the response of request based on the given URI
    :param uri: URI to which request needs to be made
    :return: JSON of the reponse
    '''

    auth_token = {'Authorization':'Bearer DEMO_TOKEN'}
    response = requests.get(uri, headers = auth_token)
    response.raise_for_status()
    return json.loads(response.text)

def get_districts_uris():
    '''
    Get the available district URIs for the demo token
    :return:
    '''

    json_response = get_json_response_for_request_uri('https://api.clever.com/v1.1/districts?limit=100')
    return [district['uri'] for district in json_response['data']]


def get_average_number_of_students_per_section(district_uris):
    '''
    Get the average number of students per section for the given list of district URIs
    :param district_uris: list of district URIs
    :return: average of students per sections
    '''

    students_count = 0
    sections_count = 0
    for uri in district_uris:
        json_response = get_json_response_for_request_uri('https://api.clever.com' + uri + '/sections')
        sections = json_response['data']
        students_count_each_section = [len(section['data']['students']) for section in sections]
        students_count += sum(students_count_each_section)
        sections_count += len(sections)
    return ((1.0 * students_count) / sections_count)

average_number_of_students_per_section = get_average_number_of_students_per_section(get_districts_uris())
print "Average number of students per section is", average_number_of_students_per_section
