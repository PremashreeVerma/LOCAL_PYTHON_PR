import json

import traceback

 

def main(input_data):

    result = {}

    try:

        input_json = input_data["input_data"]

        json_data = json.loads(input_json)

        # Process the input data

        processed_data = process_items(json_data["items"])

        processed_data_str = json.dumps(processed_data["success"])
        print(processed_data_str)

        failed = processed_data["failed"]

        if len(failed) == 0:

            result |= {"log": "Success", "processed_data_str": processed_data_str, "unprocessed_data_str": ""}

        else:

            result |= {"log": "Partial Success", "processed_data_str": processed_data_str, "unprocessed_data_str": json.dumps(failed)}

    except:

        log = traceback.format_exc()

        result |= {"processed_data_str": "[]", "log": log}

   

    return result

 

def process_items(items):

    output_lines = []

    failed_lines = []

   

    for item in items:

        try:

            rdm = {}

 

            rdm |= {"tenantId": item["tenantId"]}

            rdm |= {"type": item["type"]}

            rdm |= {"code": item["code"]}

            rdm |= {"enabled": item["enabled"]}

            rdm |= {"startDate": item["startDate"]}

            rdm |= {"endDate": item["endDate"]}

            rdm |= {"updatedBy": item["updatedBy"]}

            rdm |= {"updateDate": item["updateDate"]}

            rdm |= {"version": item["version"]}

 

            source_mappings = []

            for mapping in item["sourceMappings"]:

                for value in mapping["values"]:

                    source_mapping = {

                        "source": mapping["source"],

                        "code": value["code"],

                        "value": value["value"],

                        "enabled": value["enabled"],

                        "canonicalValue": value["canonicalValue"],

                        "downStreamDefaultValue": value["downStreamDefaultValue"]

                    }

                    source_mappings.append(source_mapping)

           

            rdm["sourceMappings"] = source_mappings

           

            output_lines.append(rdm)

        except:

            log = traceback.format_exc()

            failed_row = {"log": log, "data": item}

            failed_lines.append(failed_row)

 
    return {"success": output_lines, "failed": failed_lines}

data=input("data:")
main(data)
