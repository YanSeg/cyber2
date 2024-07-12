## à adapeter pour https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:a:laravel:framework:8.83.27:*:*:*:*:*:*:*
#{"resultsPerPage":1,"startIndex":0,"totalResults":1,"format":"NVD_CVE","version":"2.0","timestamp":"2024-07-12T14:25:09.140","vulnerabilities":[{"cve":{"id":"CVE-2022-40482","sourceIdentifier":"cve@mitre.org","published":"2023-04-25T19:15:10.180","lastModified":"2023-05-04T19:40:31.363","vulnStatus":"Analyzed","cveTags":[],"descriptions":[{"lang":"en","value":"The authentication method in Laravel 8.x through 9.x before 9.32.0 was discovered to be vulnerable to user enumeration via timeless timing attacks with HTTP\/2 multiplexing. This is caused by the early return inside the hasValidCredentials method in the Illuminate\\Auth\\SessionGuard class when a user is found to not exist."}],"metrics":{"cvssMetricV31":[{"source":"nvd@nist.gov","type":"Primary","cvssData":{"version":"3.1","vectorString":"CVSS:3.1\/AV:N\/AC:L\/PR:N\/UI:N\/S:U\/C:L\/I:N\/A:N","attackVector":"NETWORK","attackComplexity":"LOW","privilegesRequired":"NONE","userInteraction":"NONE","scope":"UNCHANGED","confidentialityImpact":"LOW","integrityImpact":"NONE","availabilityImpact":"NONE","baseScore":5.3,"baseSeverity":"MEDIUM"},"exploitabilityScore":3.9,"impactScore":1.4}]},"weaknesses":[{"source":"nvd@nist.gov","type":"Primary","description":[{"lang":"en","value":"CWE-203"}]}],"configurations":[{"nodes":[{"operator":"OR","negate":false,"cpeMatch":[{"vulnerable":true,"criteria":"cpe:2.3:a:laravel:framework:*:*:*:*:*:*:*:*","versionStartIncluding":"8.0.0","versionEndExcluding":"9.32.0","matchCriteriaId":"E4552441-3DC8-4890-B731-4F34868C15C8"}]}]}],"references":[{"url":"https:\/\/ephort.dk\/blog\/laravel-timing-attack-vulnerability\/","source":"cve@mitre.org","tags":["Exploit","Technical Description","Third Party Advisory"]},{"url":"https:\/\/github.com\/ephort\/laravel-user-enumeration-demo","source":"cve@mitre.org","tags":["Exploit","Third Party Advisory"]},{"url":"https:\/\/github.com\/laravel\/framework\/pull\/44069","source":"cve@mitre.org","tags":["Patch","Vendor Advisory"]},{"url":"https:\/\/github.com\/laravel\/framework\/releases\/tag\/v9.32.0","source":"cve@mitre.org","tags":["Release Notes"]}]}}]}

# https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:a:laravel:framework:v8.83.27:*:*:*:*:*:*:*
# {"resultsPerPage":0,"startIndex":0,"totalResults":0,"format":"NVD_CVE","version":"2.0","timestamp":"2024-07-12T13:56:50.583","vulnerabilities":[]}

#https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:a:filp:whoops:2.15.4:*:*:*:*:*:*:*
#{"resultsPerPage":0,"startIndex":0,"totalResults":0,"format":"NVD_CVE","version":"2.0","timestamp":"2024-07-12T14:30:54.653","vulnerabilities":[]}

import requests
import sys

API_key ="44c0ee91-aa4f-4308-bed4-6c369cead6ac"   

def get_vulnerabilities(part, vendor, product, version):
    headers = {
        'Authorization': 'Bearer {}'.format(API_key)
    }
    print (f"Vendor: {vendor} product: {product} version: {version}:")
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:{part}:{vendor}:{product}:{version}:*:*:*:*:*:*:*"
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        
        data = response.json()

        vulnerabilities_info = {}

        for vulnerability in data['vulnerabilities']:
            cve_info = vulnerability['cve']
            cve_id = cve_info['id']
            vulnerabilities_info[cve_id] = {
                "Published": cve_info['published'],
                "Last Modified": cve_info['lastModified'],
                "Description (English)": cve_info['descriptions'][0]['value'],
                "Severity": cve_info['metrics']['cvssMetricV2'][0]['baseSeverity']
            }

        for cve_id, info in vulnerabilities_info.items():
            print("CVE ID:", cve_id)
            for key, value in info.items():
                print(key + ":", value)
            print()
    else:
        print("Failed to retrieve data. Status code:", response.status_code)



if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <part> <vendor> <product> <version>")
        sys.exit(1)

    part = sys.argv[1]
    vendor = sys.argv[2]
    product = sys.argv[3]
    version = sys.argv[4]

    get_vulnerabilities(part, vendor, product, version)