import glob
import json
import os
from pathlib import Path
import pandas as pd

results = list(Path(".").rglob("scoutsuite_results_aws*.js"))

for result in results:
    file_variable = open(result, "r")
    all_lines_variable = file_variable.readlines()
    json_string = all_lines_variable[2 - 1]
    json_object = json.loads(json_string)
    foldername = str(result).split("/")[0]
    accountid = json_object["account_id"]
    findings = []
    for service in json_object["services"].values():
        for finding in service["findings"].values():
            if finding["flagged_items"] > 0:
                print(finding)
                findings.append(
                    {
                        "folder name": foldername,
                        "account id": accountid,
                        "service": finding["service"],
                        "title": finding["description"],
                        "rationale": finding["rationale"],
                        "level": finding["level"],
                        "remediation": finding.get("remediation"),
                        "checked": finding["checked_items"],
                        "flagged": finding["flagged_items"],
                        "items": finding["items"],
                    }
                )
df = pd.DataFrame(findings)
print(df)
df.to_csv("tool_output.csv", index=False, encoding="utf-8-sig")
