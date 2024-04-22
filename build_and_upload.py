import os
import subprocess
import requests
from requests.auth import HTTPBasicAuth

repo_url = os.environ["REPO_URL"]
username = os.environ["USER"]
password = os.environ["PASS"]

def get_chart_version(file_to_read):
    with open(file_to_read, "r") as chart_file:
        for line in chart_file.readlines():
            if "version:" in line:
                return line.split(" ")[1].strip()

def repo_has_version(chart, local_version):
    r = requests.get(f"{repo_url}/api/charts/{chart}/{local_version}")
    try:
        if r.json()["version"] == local_version:
            return True
        else:
            return False
    except KeyError:
        return False

chart_dirs = os.listdir("charts")
for chart_dir in chart_dirs:
    print("#####")
    print(f"Chart: {chart_dir}")
    version = get_chart_version(f"charts/{chart_dir}/Chart.yaml")

    if repo_has_version(chart_dir, version) == False:
        print(f"Building and uploading chart {chart_dir} version {version} to {repo_url}.")
        subprocess.run(["helm", "dependency", "update", f"charts/{chart_dir}/"])
        subprocess.run(["helm", "package", f"helm/{chart_dir}/"])

        with open(f"{chart_dir}-{version}.tgz", "rb") as f:
            data = f.read()
            requests.post(url=f"{repo_url}/api/charts", data=data, auth=HTTPBasicAuth(username, password))
    else:
        print(f"Chart {chart_dir} version {version} already exists in {repo_url}, skipping.")
    print("#####")