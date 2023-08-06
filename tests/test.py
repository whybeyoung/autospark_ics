from pyartifactory import Artifactory
from pyartifactory.exception import RepositoryNotFoundException

art = Artifactory(url="https://artifacts.iflytek.com",
                  auth=('ybyang7', 'AKCp8k7airuUmUwCo7c3p7VC794F2qHME1KZuuY38zsFHuBQPsTUxtQpv7o5A7sNy7SdxG82T'),
                  api_version=2)

try:
    repo = art.repositories.get_repo("docker-private/atp")
except RepositoryNotFoundException as e:
    print('not find')

artifacts = art.artifacts._query_knowledge("\"docker-private/atp/awake\"")
for a in artifacts.files:
    if a.uri.endswith("manifest.json"):
        items = a.uri.split("/")
        repo_path =  '/'.join(items[0:-2]) + ":" + items[-2]
        print(repo_path.lstrip("/"))
