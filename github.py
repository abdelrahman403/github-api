import requests


def create_query(languages, min_stars=50000):
    ''' Create API Query '''

    query = f"stars:>{min_stars}"
    for language in languages:
        query += f" language:{language}"

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    ''' Get Repos With Most Stars in a Specific Languages in GitHub '''

    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(gh_api_repo_search_url, params=parameters)
    # print(response.json().keys())

    # status_code = response.status_code
    status_code = 500
    if status_code != 200:
        raise RuntimeError(f"An erorr occured, Status code: {status_code}")
    else:
        response_json = response.json()["items"]
        return response_json 


if __name__ == "__main__":
    ''' Main Method '''
    
    languages = ["Python", "JavaScript", "Ruby"]
    items = repos_with_most_stars(languages)
    # print(items)
    for item in items:
        name = item['name']
        language = item['language']
        stars_count = item['stargazers_count']
        repo_url = item['clone_url']
        print(f"-> {name} is a {language} repo with {stars_count} stars and repo link {repo_url}")
