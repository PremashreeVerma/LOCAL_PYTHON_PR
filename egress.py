import json
import traceback
import copy
 
 
def __flatten(
    parent_uuid,
    parent_id,
    parent_created,
    parent_updated,
    attribute_type,
    attribute_type_map,
    flattened_cursor,
):
    attribute_type |= {"crosswalk_type": "ODS-MDM"} if "crosswalk_type" not in attribute_type else {}
    attribute_type |= {"parent_uuid": parent_uuid}
    attribute_type |= {"parent_id": parent_id}
    attribute_type |= {"parent_created": parent_created}
    attribute_type |= {"parent_updated": parent_updated}
    flattened_cursor.append(attribute_type)
 
 
def flatten_cursor(transformed_cursor):
    flattened_reltio_cursor = {
        "identifiers": [],
        "phone": [],
        "email": [],
        "education": [],
        "specialties": [],
        "licenses": [],
        "areasofExperience": [],
        "sanction": [],
        "statusInformation": [],
        "certificates": [],
        "speaker": [],
        "privacyPreferences": [],
        "otherNames": [],
        "policyConsent": [],
        "multiChannelCommunicationConsent": [],
        "taxonomy": [],
        "dEA": [],
        "cDSDetails": [],
        "salesRep": [],
        "languagesKnown": [],
        "studyRoles": [],
        "address": [],
        "records": transformed_cursor,
    }
 
    identifiers_map = {}
    phone_map = {}
    email_map = {}
    education_map = {}
    specialties_map = {}
    licenses_map = {}
    areasofExperience_map = {}
    sanction_map = {}
    statusInformation_map = {}
    certificates_map = {}
    speaker_map = {}
    privacyPreferences_map = {}
    otherNames_map = {}
    policyConsent_map = {}
    multiChannelCommunicationConsent_map = {}
    taxonomy_map = {}
    dEA_map = {}
    cDSDetails_map = {}
    salesRep_map = {}
    languagesKnown_map = {}
    studyRoles_map = {}
    address_map = {}
 
    for reltio_object in transformed_cursor:
        parent_uuid = reltio_object["entityUUID"]
        parent_id = reltio_object["uri"]
        parent_created = reltio_object["createdTime"]
        parent_updated = reltio_object["updatedTime"]
 
        # This if condition and the code inside it, flattens out
        # identifiers array. Repeat this code for each array and put
        # them in the above flattened_reltio_cursor object
 
        if "Identifiers" in reltio_object["attributes"]:
            # The following loop, goes through each identifier,
            # adds the parent_* attributes to it, and then adds it
            # to the flattened_reltio_cursor.identifiers array
            # The flattend array will thus have all the identifiers
            # for all the objects in the reltio cursor
            # In Workato, we can batch process the flattened_reltio_cursor.identifiers
            # and load 2000 identifiers at a time.
            for identifiers in reltio_object["attributes"]["Identifiers"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    identifiers,
                    identifiers_map,
                    flattened_reltio_cursor["identifiers"],
                )
 
        # Flatten Phones
        if "Phone" in reltio_object["attributes"]:
            for phone in reltio_object["attributes"]["Phone"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    phone,
                    phone_map,
                    flattened_reltio_cursor["phone"],
                )
 
        # Flatten Emails
        if "Email" in reltio_object["attributes"]:
            for email in reltio_object["attributes"]["Email"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    email,
                    email_map,
                    flattened_reltio_cursor["email"],
                )
 
        # Flatten Education
        if "Education" in reltio_object["attributes"]:
            for education in reltio_object["attributes"]["Education"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    education,
                    education_map,
                    flattened_reltio_cursor["education"],
                )
 
        # Flatten Specialties
        if "Specialties" in reltio_object["attributes"]:
            for specialties in reltio_object["attributes"]["Specialties"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    specialties,
                    specialties_map,
                    flattened_reltio_cursor["specialties"],
                )
 
        # Flatten Licenses
        if "License" in reltio_object["attributes"]:
            for licenses in reltio_object["attributes"]["License"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    licenses,
                    licenses_map,
                    flattened_reltio_cursor["licenses"],
                )
 
        # Flatten AreasofExperience
        if "AreasofExperience" in reltio_object["attributes"]:
            for areasofExperience in reltio_object["attributes"]["AreasofExperience"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    areasofExperience,
                    areasofExperience_map,
                    flattened_reltio_cursor["areasofExperience"],
                )
 
        # Flatten Sanction
        if "Sanction" in reltio_object["attributes"]:
            for sanction in reltio_object["attributes"]["Sanction"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    sanction,
                    sanction_map,
                    flattened_reltio_cursor["sanction"],
                )
 
        # Flatten StatusInformation
        if "StatusInformation" in reltio_object["attributes"]:
            for statusInformation in reltio_object["attributes"]["StatusInformation"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    statusInformation,
                    statusInformation_map,
                    flattened_reltio_cursor["statusInformation"],
                )
 
        # Flatten Certificates
        if "Certificates" in reltio_object["attributes"]:
            for certificates in reltio_object["attributes"]["Certificates"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    certificates,
                    certificates_map,
                    flattened_reltio_cursor["certificates"],
                )
 
        # Flatten Speaker
        if "Speaker" in reltio_object["attributes"]:
            for speaker in reltio_object["attributes"]["Speaker"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    speaker,
                    speaker_map,
                    flattened_reltio_cursor["speaker"],
                )
 
        # Flatten PrivacyPreferences
        if "PrivacyPreferences" in reltio_object["attributes"]:
            for privacyPreferences in reltio_object["attributes"]["PrivacyPreferences"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    privacyPreferences,
                    privacyPreferences_map,
                    flattened_reltio_cursor["privacyPreferences"],
                )
 
        # Flatten OtherNames
        if "OtherNames" in reltio_object["attributes"]:
            for otherNames in reltio_object["attributes"]["OtherNames"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    otherNames,
                    otherNames_map,
                    flattened_reltio_cursor["otherNames"],
                )
 
        # Flatten PolicyConsent
        if "PolicyConsent" in reltio_object["attributes"]:
            for policyConsent in reltio_object["attributes"]["PolicyConsent"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    policyConsent,
                    policyConsent_map,
                    flattened_reltio_cursor["policyConsent"],
                )
 
        # Flatten MultiChannelCommunicationConsent
        if "MultiChannelCommunicationConsent" in reltio_object["attributes"]:
            for multiChannelCommunicationConsent in reltio_object["attributes"][
                "MultiChannelCommunicationConsent"
            ]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    multiChannelCommunicationConsent,
                    multiChannelCommunicationConsent_map,
                    flattened_reltio_cursor["multiChannelCommunicationConsent"],
                )
 
        # Flatten Taxonomy
        if "Taxonomy" in reltio_object["attributes"]:
            for taxonomy in reltio_object["attributes"]["Taxonomy"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    taxonomy,
                    taxonomy_map,
                    flattened_reltio_cursor["taxonomy"],
                )
 
        # Flatten DEA
        if "DEA" in reltio_object["attributes"]:
            for dEA in reltio_object["attributes"]["DEA"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    dEA,
                    dEA_map,
                    flattened_reltio_cursor["dEA"],
                )
 
        # Flatten CDSDetails
        if "CDSDetails" in reltio_object["attributes"]:
            for cDSDetails in reltio_object["attributes"]["CDSDetails"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    cDSDetails,
                    cDSDetails_map,
                    flattened_reltio_cursor["cDSDetails"],
                )
 
        # Flatten SalesRep
        if "SalesRep" in reltio_object["attributes"]:
            for salesRep in reltio_object["attributes"]["SalesRep"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    salesRep,
                    salesRep_map,
                    flattened_reltio_cursor["salesRep"],
                )
 
        # Flatten LanguagesKnown
        if "LanguagesKnown" in reltio_object["attributes"]:
            for languagesKnown in reltio_object["attributes"]["LanguagesKnown"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    languagesKnown,
                    languagesKnown_map,
                    flattened_reltio_cursor["languagesKnown"],
                )
 
        # Flatten StudyRoles
        if "StudyRoles" in reltio_object["attributes"]:
            for studyRoles in reltio_object["attributes"]["StudyRoles"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    studyRoles,
                    studyRoles_map,
                    flattened_reltio_cursor["studyRoles"],
                )
 
        # Flatten Address
        if "Address" in reltio_object["attributes"]:
            for address in reltio_object["attributes"]["Address"]:
                __flatten(
                    parent_uuid,
                    parent_id,
                    parent_created,
                    parent_updated,
                    address,
                    address_map,
                    flattened_reltio_cursor["address"],
                )
 
    return flattened_reltio_cursor
 
 
def transform_cursor(reltio_cursor_json):
    all_sources = []
    excluded_source_names = [
        "configuration/sources/ReltioCleanser",
        "configuration/sources/Reltio",
        "configuration/sources/ReltioStringFunctionCleanser",
        "configuration/sources/ReltioFullNameBuilder",
    ]
 
    for reltio_object in reltio_cursor_json: #remove
        required_crosswalks = []                    
        for crosswalk in reltio_object["crosswalks"]:    #input_data["crosswalks"]
            if crosswalk["type"] not in excluded_source_names:
                required_crosswalks.append(crosswalk)
 
        for crosswalk in required_crosswalks:
            cw_attributes = crosswalk["attributes"]
            current_object_copy = __process_reltio_object_for_pr(
                cw_attributes=cw_attributes,
                crosswalk=crosswalk,
                reltio_object=reltio_object,
            )
            all_sources.append(current_object_copy)
 
        gr = __process_reltio_object_for_gr(reltio_object=copy.deepcopy(reltio_object))
        all_sources.append(gr)
 
    return all_sources
 
 
def __process_reltio_object_for_pr(cw_attributes, crosswalk, reltio_object):
    current_object_copy = copy.deepcopy(reltio_object)
    current_object_copy |= {"crosswalk_type": crosswalk["type"]}
    current_object_copy |= {"crosswalk_value": crosswalk["value"]}
    current_object_copy |= {"isOV": False}
 
    for attr, attributes in current_object_copy["attributes"].items():
        remove_values = []
        for value in attributes:
            if value["uri"] not in cw_attributes:
                remove_values.append(value)
            if isinstance(value["value"], dict):
                # This is a nested entity.
                # For each value["value"] in each property, check if URI exists in current crosswalk
                # If not, remove the value
                # Finally set the NestedEntityId as an external property so it can be bound directly
                # This will make NestedEntityId the PK of this nested entity.
                for key, vals in value["value"].items():
                    remove_nested_value = []
                    for nested_val in vals:
                        if nested_val["uri"] not in cw_attributes:
                            remove_nested_value.append(nested_val)
                        if key == "NestedEntityId" and len(vals) == 1:
                            value |= {"nestedEntityId": nested_val["value"]}
                            value |= {"crosswalk_type": crosswalk["type"]}
                        # For merge cases when there are >1 NestedIds, create data for each key
                        elif key == "NestedEntityId" and len(vals) > 1:
                            for val_item in vals:
                                value |= {"nestedEntityId": val_item["value"]} if val_item["uri"] in cw_attributes else value
                                value |= {"crosswalk_type": crosswalk["type"]}
 
                    for i in remove_nested_value:
                        vals.remove(i)
 
        for i in remove_values:
            attributes.remove(i)
        if attr == "EntityUUID":
            current_object_copy |= {"entityUUID": attributes[0]["value"]}
    return current_object_copy
 
 
def __process_reltio_object_for_gr(reltio_object):
 
    reltio_object |= {"isOV": True}
    reltio_object |= {"crosswalk_type": "ODS-MDM"}
    reltio_object |= {
        "crosswalk_value": reltio_object["attributes"]["EntityUUID"][0]["value"]
    }
    for attr, attributes in reltio_object["attributes"].items():
        remove_values = []
        for value in attributes:
            if value["ov"] == False:
                remove_values.append(value)
            if isinstance(value["value"], dict):
                for key, vals in value["value"].items():
                    remove_nested_value = []
                    for nested_val in vals:
                        if nested_val["ov"] == False:
                            remove_nested_value.append(nested_val)
                    for i in remove_nested_value:
                        vals.remove(i)
                    if key == "NestedEntityId":
                        value |= {"nestedEntityId": nested_val["value"]}
 
        for i in remove_values:
            attributes.remove(i)
        if attr == "EntityUUID":
            reltio_object |= {"entityUUID": attributes[0]["value"]}
 
    return reltio_object
 
 
def main(input_data):
    
    result = {}
    search_result_count = 0
    flattened_reltio_cursor = {
        "identifiers": [],
        "phone": [],
        "email": [],
        "education": [],
        "specialties": [],
        "licenses": [],
        "areasofExperience": [],
        "sanction": [],
        "statusInformation": [],
        "certificates": [],
        "speaker": [],
        "privacyPreferences": [],
        "otherNames": [],
        "policyConsent": [],
        "multiChannelCommunicationConsent": [],
        "taxonomy": [],
        "dEA": [],
        "cDSDetails": [],
        "salesRep": [],
        "languagesKnown": [],
        "studyRoles": [],
        "address": [],
        "records": [],
    }
    try:
       
        transformed_cursor = transform_cursor(input_data)
        with open("transform.json","w") as file:
            json.dump(transformed_cursor, file, indent = 4)
        flattened_reltio_cursor = flatten_cursor(transformed_cursor)
        flattened_reltio_cursor_str = json.dumps(flattened_reltio_cursor)
        result |= {
            "flattened_reltio_cursor": flattened_reltio_cursor_str,
            "log": "Success",
            "search_result_count": search_result_count
        }
    except:
        
        log = traceback.format_exc()
        result |= {
            "flattened_reltio_cursor": "{}",
            "log": log,
            "search_result_count": search_result_count
        }
    return result
data=[ {
  "analyticsAttributes": {},
  "attributes": {
    "Address": [
      {
        "endObjectCrosswalks": [
          {
            "type": "configuration/sources/CITELINE",
            "value": "HCP-973664-WORKPLACE"
          }
        ],
        "label": "1100 Walnut St, Philadelphia, PENNSYLVANIA, 19107-5563, United States",
        "ov": True,
        "refEntity": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/iyC8ApN/NestedEntityId/iyC8F5d",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/iyC8ApN",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T10:52:15.547Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:52:15.547Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.iyC8JLt",
              "value": "HCP-2077-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/140NAjYR",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/140NAjYR/NestedEntityId/140NAnoh",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T10:55:21.212Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:55:21.212Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.ihLkxvS",
              "value": "HCP-29414-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZki81K",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZki81K/NestedEntityId/1DZkiCHa"
              ],
              "createDate": "2025-02-24T10:52:45.754Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:52:45.754Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.nTfbnFr",
              "value": "HCP-4974-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkkwlu",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkkwlu/NestedEntityId/1DZkl12A",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:03:26.587Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:03:26.587Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.vtakOdH",
              "value": "HCP-133864-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZknlWU/NestedEntityId/1DZknpmk",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZknlWU",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:07:18.025Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:07:18.025Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.ibCLZvZ",
              "value": "HCP-269403-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkqaH4/NestedEntityId/1DZkqeXK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkqaH4"
              ],
              "createDate": "2025-02-24T11:07:17.475Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:07:17.475Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.wG4KKm3",
              "value": "HCP-272280-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZktP1e",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZktP1e/NestedEntityId/1DZktTHu"
              ],
              "createDate": "2025-02-24T10:52:59.111Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:52:59.111Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.gKdjzlM",
              "value": "HCP-6151-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkwDmE",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkwDmE/NestedEntityId/1DZkwI2U",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T10:53:02.314Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:53:02.314Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.unUUP7j",
              "value": "HCP-7026-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkz2Wo",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkz2Wo/NestedEntityId/1DZkz6n4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T10:53:54.614Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:53:54.614Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.iU96eL0",
              "value": "HCO-45626-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl1rHO",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl1rHO/NestedEntityId/1DZl1vXe",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:03:48.671Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:03:48.671Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.oeTr73b",
              "value": "HCP-152934-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl4g1y",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl4g1y/NestedEntityId/1DZl4kIE",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:00:36.109Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:00:36.109Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.oKUPudv",
              "value": "HCP-89452-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl7UmY/NestedEntityId/1DZl7Z2o",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl7UmY"
              ],
              "createDate": "2025-02-24T11:03:27.114Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:03:27.114Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.hWTVPEK",
              "value": "HCO-183398-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlAJX8/NestedEntityId/1DZlANnO",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlAJX8",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:08:46.219Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:08:46.219Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.kh92DiT",
              "value": "HCP-327673-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlD8Hi/NestedEntityId/1DZlDCXy",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlD8Hi"
              ],
              "createDate": "2025-02-24T10:54:07.941Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:54:07.941Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.Ko3sdUI",
              "value": "HCP-14105-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlFx2I",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlFx2I/NestedEntityId/1DZlG1IY",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T10:53:56.447Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:53:56.447Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.Kmko1is",
              "value": "HCP-13389-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlIlms",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlIlms/NestedEntityId/1DZlIq38",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T10:54:08.506Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:54:08.506Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.gTM7dqu",
              "value": "HCP-15131-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlLaXS/NestedEntityId/1DZlLeni",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlLaXS"
              ],
              "createDate": "2025-02-24T10:59:53.012Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:59:53.012Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.LSoHbso",
              "value": "HCP-83578-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlOPI2",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlOPI2/NestedEntityId/1DZlOTYI",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T10:53:30.548Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:53:30.548Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.j7SeZ8z",
              "value": "HCP-10695-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlRE2c",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlRE2c/NestedEntityId/1DZlRIIs",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:05:31.701Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:05:31.701Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.jfKte0E",
              "value": "HCP-213876-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlU2nC",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlU2nC/NestedEntityId/1DZlU73S",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:04:29.808Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:04:29.808Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.ojAPxrf",
              "value": "HCP-177181-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlWrXm",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlWrXm/NestedEntityId/1DZlWvo2",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:08:32.579Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:08:32.579Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.p5zIzDf",
              "value": "HCP-324008-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlZgIM/NestedEntityId/1DZlZkYc",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlZgIM",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:08:15.155Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:08:15.155Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.ifo91wj",
              "value": "HCP-311524-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlcV2w/NestedEntityId/1DZlcZJC",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlcV2w",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:08:15.155Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:08:15.155Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.ifm8sMf",
              "value": "HCP-311107-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlfJnW",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlfJnW/NestedEntityId/1DZlfO3m"
              ],
              "createDate": "2025-02-24T10:55:04.244Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:55:04.244Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.njHzRh5",
              "value": "HCP-22464-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZli8Y6/NestedEntityId/1DZliCoM",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZli8Y6",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:03:48.671Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:03:48.671Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.oeUC52J",
              "value": "HCP-153018-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlkxIg/NestedEntityId/1DZll1Yw",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlkxIg",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:07:59.192Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:07:59.192Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.1SVuZ6Zu",
              "value": "HCP-302200-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/SourceCreatedDate/1DZlo7MY",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco/NestedEntityId/1DZloFt4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco/SourceCreatedDate/1DZloK9K",
                "entities/0OfT51J/attributes/Address/6t2u7C9/IsDeleted/1DZlnyq2",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco/SourceLastUpdateDate/1DZloOPa",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco"
              ],
              "createDate": "2025-02-24T11:06:15.665Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-02-24T11:06:15.665Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.osvQvgJ",
              "value": "1-1T6P6TM--1-1T6P6TN"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlr8tu",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlr8tu/NestedEntityId/1DZlrDAA",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:08:15.353Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:08:15.353Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.ifsLZmn",
              "value": "HCP-305808-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZltxeU",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZltxeU/NestedEntityId/1DZlu1uk",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-24T11:08:48.740Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:08:48.740Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.ilYxdav",
              "value": "HCP-329823-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/1DZlxOlO",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/1DZlxKV8",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/1DZlxByc",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlxbYA",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1DZlu6B0",
                "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/1DZlxOlO/Latitude/1DZlxT1e",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlxbYA/NestedEntityId/1DZlxfoQ",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/1DZlxOlO/Longitude/1DZlxXHu",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine2/1DZlx3S6",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/1DZlxGEs"
              ],
              "createDate": "2025-02-24T12:23:57.621Z",
              "type": "configuration/sources/ONEKEY",
              "updateDate": "2025-02-24T12:23:57.621Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.kxSZ1oD",
              "value": "WUS00000125254"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/PHFiMEf",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/PHFiMEf/NestedEntityId/PHFiQUv"
              ],
              "createDate": "2025-02-24T10:59:32.510Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T10:59:32.510Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.jjQM8ev",
              "value": "HCP-78391-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/sNtNmqL/NestedEntityId/sNtNr6b",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/sNtNmqL"
              ],
              "createDate": "2025-02-25T08:08:00.511Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-25T08:08:00.511Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.sLB9uZZ",
              "value": "HCP-579064-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/18mOm1EM",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/18mOm1EM/NestedEntityId/18mOm5Uc"
              ],
              "createDate": "2025-02-25T08:10:01.371Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-25T08:10:01.371Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.18hoQHPy",
              "value": "HCP-685789-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1rrIwTRm",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1rrIwTRm/NestedEntityId/1rrIwXi2",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-25T08:16:34.825Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-25T08:16:34.825Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.1rp83doU",
              "value": "HCP-905602-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1910Gtzy",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1910Gtzy/NestedEntityId/1910GyGE",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-02-25T08:22:06.428Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-25T08:22:06.428Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.190GaJCg",
              "value": "HCP-1120944-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/nNSeQaC",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/nNSeQaC/NestedEntityId/nNSeUqS"
              ],
              "createDate": "2025-03-07T11:37:27.182Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:37:27.182Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.15MFX0Xd",
              "value": "HCP-973664-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/WwqkdYD/NestedEntityId/WwqkhoT",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/WwqkdYD",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:43:05.379Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:43:05.379Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.1h1PE7JS",
              "value": "HCP-1373290-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/YNYhpQi/NestedEntityId/YNYhtgy",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/YNYhpQi"
              ],
              "createDate": "2025-03-07T11:37:27.234Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:37:27.234Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.yVwMAFy",
              "value": "HCP-974758-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfExZA/NestedEntityId/1VwfF1pQ",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfExZA"
              ],
              "createDate": "2025-03-07T11:25:31.408Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:25:31.408Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.xNFDFtW",
              "value": "HCP-354633-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfGP4a/NestedEntityId/1VwfGTKq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfGP4a",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:41:02.892Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:41:02.892Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.nB0TAPx",
              "value": "HCP-1197505-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfHqa0/NestedEntityId/1VwfHuqG",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfHqa0"
              ],
              "createDate": "2025-03-07T11:40:13.740Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:40:13.740Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.15ez886f",
              "value": "HCP-1131924-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfJI5Q/NestedEntityId/1VwfJMLg",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfJI5Q"
              ],
              "createDate": "2025-03-07T11:40:13.727Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:40:13.727Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.yjsH9mQ",
              "value": "HCP-1136087-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfKjaq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfKjaq/NestedEntityId/1VwfKnr6",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:37:58.958Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:37:58.958Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.yYfdD7O",
              "value": "HCP-997087-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfMB6G/NestedEntityId/1VwfMFMW",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfMB6G",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:37:55.691Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:37:55.691Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.mqoqnRR",
              "value": "HCP-992032-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfNcbg/NestedEntityId/1VwfNgrw",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfNcbg",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:38:38.373Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:38:38.373Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.TEl6GaV",
              "value": "HCP-1042599-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfP476",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfP476/NestedEntityId/1VwfP8NM"
              ],
              "createDate": "2025-03-07T11:33:40.283Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:33:40.283Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.hBR7Uuj",
              "value": "HCP-780288-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDrdn7",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDrdn7/NestedEntityId/17cDri3N",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:25:29.824Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:25:29.824Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.xMQrRuY",
              "value": "HCP-353686-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDswm1/NestedEntityId/17cDt12H",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDswm1",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:34:23.185Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:34:23.185Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.Sngvjzb",
              "value": "HCP-815771-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDuFkv",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDuFkv/NestedEntityId/17cDuK1B",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:32:54.466Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:32:54.466Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.h6ODu4T",
              "value": "HCP-744437-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDvYjp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDvYjp/NestedEntityId/17cDvd05"
              ],
              "createDate": "2025-03-07T11:36:36.239Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:36:36.239Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.15GOBhAD",
              "value": "HCP-930077-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDwrij/NestedEntityId/17cDwvyz",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDwrij",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:40:47.920Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:40:47.920Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.n9cd5bN",
              "value": "HCP-1177742-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDyAhd/NestedEntityId/17cDyExt",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDyAhd"
              ],
              "createDate": "2025-03-07T11:39:59.864Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:39:59.864Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.n4wAUen",
              "value": "HCP-1120938-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMNzQFD",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMNzQFD/NestedEntityId/MMNzUVT"
              ],
              "createDate": "2025-03-07T11:36:34.681Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:36:34.681Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.1gQ3HKcc",
              "value": "HCP-921968-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMO0SB5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMO0SB5/NestedEntityId/MMO0WRL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:39:59.864Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:39:59.864Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.n4wIoO1",
              "value": "HCP-1120946-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchp3sg",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchp3sg/NestedEntityId/lchp88w",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:25:29.824Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:25:29.824Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.xMPjGB4",
              "value": "HCP-353582-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchrKXC",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchrKXC/NestedEntityId/lchrOnS",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:25:46.313Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:25:46.313Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.RyjU7TL",
              "value": "HCP-365370-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchtbBi",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchtbBi/NestedEntityId/lchtfRy",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:29:28.873Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:29:28.873Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.1fbCs6iY",
              "value": "HCP-562724-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchvrqE",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchvrqE/NestedEntityId/lchvw6U",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:36:25.473Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:36:25.473Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.hRwD3cr",
              "value": "HCP-918166-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchy8Uk",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchy8Uk/NestedEntityId/lchyCl0"
              ],
              "createDate": "2025-03-07T11:33:16.924Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:33:16.924Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.14xMlLmH",
              "value": "HCP-760705-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci0P9G/NestedEntityId/lci0TPW",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci0P9G"
              ],
              "createDate": "2025-03-07T11:33:32.858Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:33:32.858Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.1g0okTOU",
              "value": "HCP-777667-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci2fnm",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci2fnm/NestedEntityId/lci2k42",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:39:47.366Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:39:47.366Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.15csu65V",
              "value": "HCP-1110020-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci4wSI",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci4wSI/NestedEntityId/lci50iY",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:33:56.716Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:33:56.716Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.hDNYRCv",
              "value": "HCP-794377-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci7D6o",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci7D6o/NestedEntityId/lci7HN4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:39:47.366Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:39:47.366Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.15cwGoCz",
              "value": "HCP-1110606-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci9TlK/NestedEntityId/lci9Y1a",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci9TlK"
              ],
              "createDate": "2025-03-07T11:39:59.864Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:39:59.864Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.n4w6Zi5",
              "value": "HCP-1120937-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciBkPq",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciBkPq/NestedEntityId/lciBog6",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:34:55.777Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:34:55.777Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.yHT3aOU",
              "value": "HCP-837977-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciE14M/NestedEntityId/lciE5Kc",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciE14M"
              ],
              "createDate": "2025-03-07T11:34:47.208Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:34:47.208Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.156TMGNR",
              "value": "HCP-833045-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciGHis",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciGHis/NestedEntityId/lciGLz8",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:36:25.450Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:36:25.450Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.hRmfE7B",
              "value": "HCP-919003-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciIYNO/NestedEntityId/lciIcde",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciIYNO",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:37:55.691Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:37:55.691Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.mqonUr3",
              "value": "HCP-992016-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciKp1u",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciKp1u/NestedEntityId/lciKtIA"
              ],
              "createDate": "2025-03-07T11:35:03.997Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:35:03.997Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.yJjiAek",
              "value": "HCP-849201-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciN5gQ/NestedEntityId/lciN9wg",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciN5gQ"
              ],
              "createDate": "2025-03-07T11:39:52.080Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:39:52.080Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.TN1d5nj",
              "value": "HCP-1111707-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciPMKw",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciPMKw/NestedEntityId/lciPQbC",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:36:36.138Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:36:36.138Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.15GFhveX",
              "value": "HCP-926336-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciRczS",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciRczS/NestedEntityId/lciRhFi",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:39:52.080Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:39:52.080Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.TMzdy9X",
              "value": "HCP-1111614-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciTtdy/NestedEntityId/lciTxuE",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciTtdy",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:29:08.402Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:29:08.402Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.14VM1c69",
              "value": "HCP-550808-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciWAIU/NestedEntityId/lciWEYk",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciWAIU",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7"
              ],
              "createDate": "2025-03-07T11:35:34.222Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:35:34.222Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.hMN3Alh",
              "value": "HCP-877190-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
                "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/1DZlxByc",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE/Zip5/lciepL0",
                "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw/Latitude/lcigXtS",
                "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw",
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw/Longitude/lcigc9i",
                "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw/GeoAccuracy/lcigTdC",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE/Zip4/lciel4k",
                "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE",
                "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE/PostalCode/lciegoU",
                "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
                "entities/0OfT51J/attributes/Address/6t2u7C9/VerificationStatus/lcieU1i"
              ],
              "createDate": "2025-03-11T00:56:26.061Z",
              "type": "configuration/sources/ReltioCleanser",
              "updateDate": "2025-03-11T00:56:26.061Z",
              "uri": "entities/0OfT51J/crosswalks/0Av5FoP.lciWIp0",
              "value": "0Av5FoP"
            }
          ],
          "objectURI": "entities/0Av5FoP",
          "type": "configuration/entityTypes/Location"
        },
        "refRelation": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/6t2u7C9",
                "entities/0OfT51J/attributes/Address/6t2u7C9/AddressType/15MFWFen"
              ],
              "createDate": "2025-03-07T11:37:27.182Z",
              "type": "configuration/sources/Reltio",
              "updateDate": "2025-03-07T11:37:27.182Z",
              "uri": "entities/0OfT51J/crosswalks/6t2u7C9.15MHuk4D",
              "value": "6t2u7C9"
            }
          ],
          "endRefIgnored": False,
          "endRefPinned": False,
          "objectURI": "relations/6t2u7C9",
          "startRefIgnored": False,
          "startRefPinned": False,
          "type": "configuration/relationTypes/HCPHasAddress"
        },
        "relationshipLabel": "CITELINE",
        "startObjectCrosswalks": [
          {
            "type": "configuration/sources/CITELINE",
            "value": "HCP-973664"
          }
        ],
        "uri": "entities/0OfT51J/attributes/Address/6t2u7C9",
        "value": {
          "AddressLine1": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine1/iyC7lFp",
              "value": "1100 Walnut St"
            }
          ],
          "AddressLine2": [
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine2",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/AddressLine2/1DZlx3S6",
              "value": "1100 Walnut St"
            }
          ],
          "AddressType": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/relationTypes/HCPHasAddress/attributes/AddressType",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/AddressType/15MFWFen",
              "value": "CITELINE"
            }
          ],
          "City": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/City",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/City/iyC7pW5",
              "value": "Philadelphia"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/City",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/City/1DZlxKV8",
              "value": "PHILADELPHIA"
            }
          ],
          "Country": [
            {
              "lookupCode": "US",
              "lookupRawValue": "United States",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Country/iyC86Z7",
              "value": "United States"
            },
            {
              "lookupCode": "US",
              "lookupRawValue": "UNITED STATES",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Country/1DZlxGEs",
              "value": "United States"
            }
          ],
          "GeoLocation": [
            {
              "label": "39.948460, -75.159260",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw",
              "value": {
                "GeoAccuracy": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/GeoAccuracy",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw/GeoAccuracy/lcigTdC",
                    "value": "P4"
                  }
                ],
                "Latitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Latitude",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw/Latitude/lcigXtS",
                    "value": "39.948460"
                  }
                ],
                "Longitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Longitude",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/lcigPMw/Longitude/lcigc9i",
                    "value": "-75.159260"
                  }
                ]
              }
            },
            {
              "label": ",",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/1DZlxOlO",
              "value": {
                "Latitude": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Latitude",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/1DZlxOlO/Latitude/1DZlxT1e",
                    "value": "39.948452"
                  }
                ],
                "Longitude": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Longitude",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/GeoLocation/1DZlxOlO/Longitude/1DZlxXHu",
                    "value": "-75.15925"
                  }
                ]
              }
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/IsDeleted/1DZlnyq2",
              "value": "False"
            }
          ],
          "PostalCode": [
            {
              "label": "19107-5563",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE",
              "value": {
                "PostalCode": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE/PostalCode/lciegoU",
                    "value": "19107-5563"
                  }
                ],
                "Zip4": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip4",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE/Zip4/lciel4k",
                    "value": "5563"
                  }
                ],
                "Zip5": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/lciecYE/Zip5/lciepL0",
                    "value": "19107"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4",
              "value": {
                "PostalCode": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1914EsFK",
                    "value": "19107-5563"
                  },
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/PostalCode/1DZlu6B0",
                    "value": "19107 5563"
                  }
                ],
                "Zip4": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip4",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip4/1914EwVa",
                    "value": "5563"
                  }
                ],
                "Zip5": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/PostalCode/1914Enz4/Zip5/1914F0lq",
                    "value": "19107"
                  }
                ]
              }
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/SourceCreatedDate/1DZlo7MY",
              "value": "2015-04-14T19:51:09.000+0000"
            }
          ],
          "StateProvince": [
            {
              "lookupCode": "PA",
              "lookupRawValue": "PA",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/1DZlxByc",
              "value": "PENNSYLVANIA"
            },
            {
              "lookupCode": "PA",
              "lookupRawValue": "Pennsylvania",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/StateProvince/iyC7tmL",
              "value": "PENNSYLVANIA"
            }
          ],
          "Unit": [
            {
              "label": "",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/WwqkdYD",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/WwqkdYD/NestedEntityId/WwqkhoT",
                    "value": "HCP-1373290-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfGP4a",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfGP4a/NestedEntityId/1VwfGTKq",
                    "value": "HCP-1197505-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDwrij",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDwrij/NestedEntityId/17cDwvyz",
                    "value": "HCP-1177742-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfHqa0",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfHqa0/NestedEntityId/1VwfHuqG",
                    "value": "HCP-1131924-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfJI5Q",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfJI5Q/NestedEntityId/1VwfJMLg",
                    "value": "HCP-1136087-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci9TlK",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci9TlK/NestedEntityId/lci9Y1a",
                    "value": "HCP-1120937-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMO0SB5",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMO0SB5/NestedEntityId/MMO0WRL",
                    "value": "HCP-1120946-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDyAhd",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDyAhd/NestedEntityId/17cDyExt",
                    "value": "HCP-1120938-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciRczS",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciRczS/NestedEntityId/lciRhFi",
                    "value": "HCP-1111614-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciN5gQ",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciN5gQ/NestedEntityId/lciN9wg",
                    "value": "HCP-1111707-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci7D6o",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci7D6o/NestedEntityId/lci7HN4",
                    "value": "HCP-1110606-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci2fnm",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci2fnm/NestedEntityId/lci2k42",
                    "value": "HCP-1110020-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfNcbg",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfNcbg/NestedEntityId/1VwfNgrw",
                    "value": "HCP-1042599-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfKjaq",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfKjaq/NestedEntityId/1VwfKnr6",
                    "value": "HCP-997087-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciIYNO",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciIYNO/NestedEntityId/lciIcde",
                    "value": "HCP-992016-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfMB6G",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfMB6G/NestedEntityId/1VwfMFMW",
                    "value": "HCP-992032-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/YNYhpQi",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/YNYhpQi/NestedEntityId/YNYhtgy",
                    "value": "HCP-974758-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/nNSeQaC",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/nNSeQaC/NestedEntityId/nNSeUqS",
                    "value": "HCP-973664-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDvYjp",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDvYjp/NestedEntityId/17cDvd05",
                    "value": "HCP-930077-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciPMKw",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciPMKw/NestedEntityId/lciPQbC",
                    "value": "HCP-926336-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMNzQFD",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/MMNzQFD/NestedEntityId/MMNzUVT",
                    "value": "HCP-921968-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchvrqE",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchvrqE/NestedEntityId/lchvw6U",
                    "value": "HCP-918166-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciGHis",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciGHis/NestedEntityId/lciGLz8",
                    "value": "HCP-919003-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciWAIU",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciWAIU/NestedEntityId/lciWEYk",
                    "value": "HCP-877190-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciKp1u",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciKp1u/NestedEntityId/lciKtIA",
                    "value": "HCP-849201-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciBkPq",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciBkPq/NestedEntityId/lciBog6",
                    "value": "HCP-837977-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciE14M",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciE14M/NestedEntityId/lciE5Kc",
                    "value": "HCP-833045-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDswm1",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDswm1/NestedEntityId/17cDt12H",
                    "value": "HCP-815771-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci4wSI",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci4wSI/NestedEntityId/lci50iY",
                    "value": "HCP-794377-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfP476",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfP476/NestedEntityId/1VwfP8NM",
                    "value": "HCP-780288-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci0P9G",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lci0P9G/NestedEntityId/lci0TPW",
                    "value": "HCP-777667-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchy8Uk",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchy8Uk/NestedEntityId/lchyCl0",
                    "value": "HCP-760705-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDuFkv",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDuFkv/NestedEntityId/17cDuK1B",
                    "value": "HCP-744437-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchtbBi",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchtbBi/NestedEntityId/lchtfRy",
                    "value": "HCP-562724-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciTtdy",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lciTtdy/NestedEntityId/lciTxuE",
                    "value": "HCP-550808-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchrKXC",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchrKXC/NestedEntityId/lchrOnS",
                    "value": "HCP-365370-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfExZA",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1VwfExZA/NestedEntityId/1VwfF1pQ",
                    "value": "HCP-354633-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchp3sg",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/lchp3sg/NestedEntityId/lchp88w",
                    "value": "HCP-353582-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDrdn7",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/17cDrdn7/NestedEntityId/17cDri3N",
                    "value": "HCP-353686-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1910Gtzy",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1910Gtzy/NestedEntityId/1910GyGE",
                    "value": "HCP-1120944-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1rrIwTRm",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1rrIwTRm/NestedEntityId/1rrIwXi2",
                    "value": "HCP-905602-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/18mOm1EM",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/18mOm1EM/NestedEntityId/18mOm5Uc",
                    "value": "HCP-685789-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/sNtNmqL",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/sNtNmqL/NestedEntityId/sNtNr6b",
                    "value": "HCP-579064-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlxbYA",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlxbYA/NestedEntityId/1DZlxfoQ",
                    "value": "WUS00000023991"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZltxeU",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZltxeU/NestedEntityId/1DZlu1uk",
                    "value": "HCP-329823-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlAJX8",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlAJX8/NestedEntityId/1DZlANnO",
                    "value": "HCP-327673-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlWrXm",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlWrXm/NestedEntityId/1DZlWvo2",
                    "value": "HCP-324008-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlr8tu",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlr8tu/NestedEntityId/1DZlrDAA",
                    "value": "HCP-305808-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlcV2w",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlcV2w/NestedEntityId/1DZlcZJC",
                    "value": "HCP-311107-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlZgIM",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlZgIM/NestedEntityId/1DZlZkYc",
                    "value": "HCP-311524-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlkxIg",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlkxIg/NestedEntityId/1DZll1Yw",
                    "value": "HCP-302200-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZknlWU",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZknlWU/NestedEntityId/1DZknpmk",
                    "value": "HCP-269403-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkqaH4",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkqaH4/NestedEntityId/1DZkqeXK",
                    "value": "HCP-272280-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco/NestedEntityId/1DZloFt4",
                    "value": "1-1T6P6TM--1-1T6P6TN|-2960454550397313839"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco/SourceCreatedDate/1DZloK9K",
                    "value": "2015-04-14T19:51:09.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZloBco/SourceLastUpdateDate/1DZloOPa",
                    "value": "2024-03-01T22:22:45.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlRE2c",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlRE2c/NestedEntityId/1DZlRIIs",
                    "value": "HCP-213876-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlU2nC",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlU2nC/NestedEntityId/1DZlU73S",
                    "value": "HCP-177181-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZli8Y6",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZli8Y6/NestedEntityId/1DZliCoM",
                    "value": "HCP-153018-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl1rHO",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl1rHO/NestedEntityId/1DZl1vXe",
                    "value": "HCP-152934-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl7UmY",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl7UmY/NestedEntityId/1DZl7Z2o",
                    "value": "HCO-183398-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkkwlu",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkkwlu/NestedEntityId/1DZkl12A",
                    "value": "HCP-133864-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl4g1y",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZl4g1y/NestedEntityId/1DZl4kIE",
                    "value": "HCP-89452-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlLaXS",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlLaXS/NestedEntityId/1DZlLeni",
                    "value": "HCP-83578-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/PHFiMEf",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/PHFiMEf/NestedEntityId/PHFiQUv",
                    "value": "HCP-78391-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/140NAjYR",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/140NAjYR/NestedEntityId/140NAnoh",
                    "value": "HCP-29414-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlfJnW",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlfJnW/NestedEntityId/1DZlfO3m",
                    "value": "HCP-22464-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlIlms",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlIlms/NestedEntityId/1DZlIq38",
                    "value": "HCP-15131-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlD8Hi",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlD8Hi/NestedEntityId/1DZlDCXy",
                    "value": "HCP-14105-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlFx2I",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlFx2I/NestedEntityId/1DZlG1IY",
                    "value": "HCP-13389-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkz2Wo",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkz2Wo/NestedEntityId/1DZkz6n4",
                    "value": "HCO-45626-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlOPI2",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZlOPI2/NestedEntityId/1DZlOTYI",
                    "value": "HCP-10695-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkwDmE",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZkwDmE/NestedEntityId/1DZkwI2U",
                    "value": "HCP-7026-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZktP1e",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZktP1e/NestedEntityId/1DZktTHu",
                    "value": "HCP-6151-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZki81K",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/1DZki81K/NestedEntityId/1DZkiCHa",
                    "value": "HCP-4974-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/iyC8ApN",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/Unit/iyC8ApN/NestedEntityId/iyC8F5d",
                    "value": "HCP-2077-WORKPLACE"
                  }
                ]
              }
            }
          ],
          "VerificationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/VerificationStatus",
              "uri": "entities/0OfT51J/attributes/Address/6t2u7C9/VerificationStatus/lcieU1i",
              "value": "Verified"
            }
          ]
        }
      },
      {
        "endObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-653WBFW--1-653WBFX"
          },
          {
            "type": "configuration/sources/CTMS",
            "value": "1-4PJGPO--1-653WBFV"
          }
        ],
        "label": "1100 Walnut St Ste 500, Philadelphia, PENNSYLVANIA, 19107-5563, United States",
        "ov": True,
        "refEntity": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceLastUpdateDate/O93ddKP",
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B/SourceCreatedDate/O93dydh",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/O93dUnt",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B/NestedEntityId/O93duNR",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/Zip5/O93dMHN",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B/SourceLastUpdateDate/O93e2tx",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/O93dhaf",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr"
              ],
              "createDate": "2025-02-28T11:25:45.191Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-02-28T11:25:45.191Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.O93e7AD",
              "value": "1-1YQ-4703|1-20O-214"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceLastUpdateDate/O93ddKP",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C/SourceLastUpdateDate/6WzpT0my",
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/O93dUnt",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/6WzpSbDQ",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C/SourceCreatedDate/6WzpSwWi",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C/NestedEntityId/6WzpSsGS"
              ],
              "createDate": "2025-03-07T11:29:41.034Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T11:29:41.034Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.xmnzGrO",
              "value": "1-2UUUULR|1-4PJGPO"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/6WzpSbDQ",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF/SourceLastUpdateDate/1K5JlzZ1",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF/NestedEntityId/1K5Jlr2V",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF/SourceCreatedDate/1K5JlvIl"
              ],
              "createDate": "2025-03-07T12:30:01.035Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:30:01.035Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.jxfnWVZ",
              "value": "1-4PJGPO--1-34ORVHD"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o/NestedEntityId/1QGECCM4",
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o/SourceCreatedDate/1QGECGcK",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/6WzpSbDQ",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o/SourceLastUpdateDate/1QGECKsa",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.1jpzDWmg",
              "value": "1-4PJGPO--1-653WBFV"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5/SourceLastUpdateDate/wc4McZr",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5",
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/6WzpSbDQ",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5/SourceCreatedDate/wc4MYJb",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5/NestedEntityId/wc4MU3L"
              ],
              "createDate": "2025-03-07T12:28:49.767Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:28:49.767Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.17k4N5OX",
              "value": "1-4PJGPO--1-351E26D"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/6WzpSbDQ",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9/NestedEntityId/Vs18URP",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9/SourceCreatedDate/Vs18Yhf",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9/SourceLastUpdateDate/Vs18cxv"
              ],
              "createDate": "2025-03-07T12:39:23.827Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:39:23.827Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.18MrSKVB",
              "value": "1-4PJGPO--1-4LP3UJI"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH/NestedEntityId/M2BanBX",
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH/SourceCreatedDate/M2BarRn",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/6WzpSbDQ",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH/SourceLastUpdateDate/M2Bavi3"
              ],
              "createDate": "2025-03-07T12:31:44.323Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:31:44.323Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.1jEP42hm",
              "value": "1-4PJGPO--1-391XTIT"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD/SourceCreatedDate/M2BcRTj",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD/SourceLastUpdateDate/M2BcVjz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/M2Bc6AR",
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/M2BcEgx",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD/NestedEntityId/M2BcNDT",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.1jpzA5fm",
              "value": "1-653WBFW--1-653WBFX"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/M2Bzg6x",
                "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF/Latitude/M2C09wl",
                "entities/0OfT51J/attributes/Address/0VFRhXm",
                "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/M2BzKnf",
                "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF/GeoAccuracy/M2C05gV",
                "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol/Zip4/M2ByALH",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol/Zip5/M2ByEbX",
                "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol",
                "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF/Longitude/M2C0ED1",
                "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol/PostalCode/M2By651",
                "entities/0OfT51J/attributes/Address/0VFRhXm/VerificationStatus/M2BxtIF",
                "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr"
              ],
              "createDate": "2025-03-10T23:14:32.945Z",
              "type": "configuration/sources/ReltioCleanser",
              "updateDate": "2025-03-10T23:14:32.945Z",
              "uri": "entities/0OfT51J/crosswalks/04rVs73.M2BpVIl",
              "value": "04rVs73"
            }
          ],
          "objectURI": "entities/04rVs73",
          "type": "configuration/entityTypes/Location"
        },
        "refRelation": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressType/1jpzCZ74",
                "entities/0OfT51J/attributes/Address/0VFRhXm"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/Reltio",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0VFRhXm.1jq2XDMo",
              "value": "0VFRhXm"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRhXm/AddressType/1jpzCZ74",
                "entities/0OfT51J/attributes/Address/0VFRhXm"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/Reltio",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0VFRhXm.1jq2WnnG",
              "value": "0VFRUl0"
            }
          ],
          "endRefIgnored": False,
          "endRefPinned": False,
          "objectURI": "relations/0VFRhXm",
          "startRefIgnored": False,
          "startRefPinned": False,
          "type": "configuration/relationTypes/HCPHasAddress"
        },
        "relationshipLabel": "Mailing",
        "startObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-4TMZR8M"
          }
        ],
        "uri": "entities/0OfT51J/attributes/Address/0VFRhXm",
        "value": {
          "AddressLine1": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/M2Bzg6x",
              "value": "1100 Walnut St Ste 500"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/M2Bc6AR",
              "value": "1100 Walnut Street."
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine1/O93d5EL",
              "value": "1100 Walnut Street"
            }
          ],
          "AddressLine2": [
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine2",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/AddressLine2/O93d9Ub",
              "value": "Suite 500"
            }
          ],
          "AddressType": [
            {
              "lookupCode": "Mailing",
              "lookupRawValue": "Mailing",
              "ov": True,
              "type": "configuration/relationTypes/HCPHasAddress/attributes/AddressType",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/AddressType/1jpzCZ74",
              "value": "Mailing"
            }
          ],
          "City": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/City",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/City/O93dDkr",
              "value": "Philadelphia"
            }
          ],
          "Country": [
            {
              "lookupCode": "US",
              "lookupRawValue": "United States",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Country/1K5JliVz",
              "value": "United States"
            },
            {
              "lookupCode": "US",
              "lookupRawValue": "UNITED STATES",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Country/O93dUnt",
              "value": "United States"
            }
          ],
          "GeoLocation": [
            {
              "label": "39.948460, -75.159260",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF",
              "value": {
                "GeoAccuracy": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/GeoAccuracy",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF/GeoAccuracy/M2C05gV",
                    "value": "P4"
                  }
                ],
                "Latitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Latitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF/Latitude/M2C09wl",
                    "value": "39.948460"
                  }
                ],
                "Longitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Longitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/GeoLocation/M2C01QF/Longitude/M2C0ED1",
                    "value": "-75.159260"
                  }
                ]
              }
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/IsDeleted/O93dlqv",
              "value": "False"
            }
          ],
          "PostalCode": [
            {
              "label": "19107-5563",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol",
              "value": {
                "PostalCode": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol/PostalCode/M2By651",
                    "value": "19107-5563"
                  }
                ],
                "Zip4": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip4",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol/Zip4/M2ByALH",
                    "value": "5563"
                  }
                ],
                "Zip5": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/M2By1ol/Zip5/M2ByEbX",
                    "value": "19107"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17",
              "value": {
                "PostalCode": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/PostalCode/O93dQXd",
                    "value": "19107"
                  }
                ],
                "Zip5": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/PostalCode/O93dI17/Zip5/O93dMHN",
                    "value": "19107"
                  }
                ]
              }
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/6WzpSbDQ",
              "value": "2011-09-12T23:36:31.000+0000"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/M2BcEgx",
              "value": "2022-07-15T12:36:04.000+0000"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/SourceCreatedDate/O93dhaf",
              "value": "2010-04-23T22:41:33.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/SourceLastUpdateDate/O93ddKP",
              "value": "2014-02-23T02:59:20.000+0000"
            }
          ],
          "StateProvince": [
            {
              "lookupCode": "PA",
              "lookupRawValue": "PA",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/M2BzKnf",
              "value": "PENNSYLVANIA"
            },
            {
              "lookupCode": "PA",
              "lookupRawValue": "Pennsylvania",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/StateProvince/O93dZ49",
              "value": "PENNSYLVANIA"
            }
          ],
          "Unit": [
            {
              "label": "",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o/NestedEntityId/1QGECCM4",
                    "value": "1-4PJGPO--1-653WBFV|-7137422633780351310"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o/SourceCreatedDate/1QGECGcK",
                    "value": "2011-09-12T23:36:31.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1QGEC85o/SourceLastUpdateDate/1QGECKsa",
                    "value": "2014-02-23T02:59:20.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD/NestedEntityId/M2BcNDT",
                    "value": "1-653WBFW--1-653WBFX|-6733756849079056443"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD/SourceCreatedDate/M2BcRTj",
                    "value": "2022-07-15T12:36:04.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BcIxD/SourceLastUpdateDate/M2BcVjz",
                    "value": "2022-07-15T12:36:49.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9/NestedEntityId/Vs18URP",
                    "value": "1-4PJGPO--1-4LP3UJI|-4692881764345118438"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9/SourceCreatedDate/Vs18Yhf",
                    "value": "2011-09-12T23:36:31.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/Vs18QB9/SourceLastUpdateDate/Vs18cxv",
                    "value": "2014-02-23T02:59:20.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH/NestedEntityId/M2BanBX",
                    "value": "1-4PJGPO--1-391XTIT|5922361177721247316"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH/SourceCreatedDate/M2BarRn",
                    "value": "2011-09-12T23:36:31.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/M2BaivH/SourceLastUpdateDate/M2Bavi3",
                    "value": "2014-02-23T02:59:20.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF/NestedEntityId/1K5Jlr2V",
                    "value": "1-4PJGPO--1-34ORVHD|242092336478109576"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF/SourceCreatedDate/1K5JlvIl",
                    "value": "2011-09-12T23:36:31.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/1K5JlmmF/SourceLastUpdateDate/1K5JlzZ1",
                    "value": "2014-02-23T02:59:20.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5/NestedEntityId/wc4MU3L",
                    "value": "1-4PJGPO--1-351E26D|5841565852468682715"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5/SourceCreatedDate/wc4MYJb",
                    "value": "2011-09-12T23:36:31.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/wc4MPn5/SourceLastUpdateDate/wc4McZr",
                    "value": "2014-02-23T02:59:20.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C/NestedEntityId/6WzpSsGS",
                    "value": "1-2UUUULR|1-4PJGPO|8312855377635339038"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C/SourceCreatedDate/6WzpSwWi",
                    "value": "2011-09-12T23:36:31.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/6WzpSo0C/SourceLastUpdateDate/6WzpT0my",
                    "value": "2014-02-23T02:59:20.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B/NestedEntityId/O93duNR",
                    "value": "1-1YQ-4703|1-20O-214|8299027466259521565"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B/SourceCreatedDate/O93dydh",
                    "value": "2010-04-23T22:41:33.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/Unit/O93dq7B/SourceLastUpdateDate/O93e2tx",
                    "value": "2014-02-23T02:59:20.000+0000"
                  }
                ]
              }
            }
          ],
          "VerificationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/VerificationStatus",
              "uri": "entities/0OfT51J/attributes/Address/0VFRhXm/VerificationStatus/M2BxtIF",
              "value": "Verified"
            }
          ]
        }
      },
      {
        "endObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-4QKNL4--1-4TMZR8P"
          }
        ],
        "label": "1015 Walnut St Fl 10, Philadelphia, PENNSYLVANIA, 19107-5005, United States",
        "ov": True,
        "refEntity": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine2/14YP2oQv",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR/PostalCode/14YP31Dh",
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/14YP2kAf",
                "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/14YP39kD",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF/SourceLastUpdateDate/14YP3da1",
                "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
                "entities/0OfT51J/attributes/Address/0VFRdHW/IsDeleted/14YP3MWz",
                "entities/0OfT51J/attributes/Address/0VFRdHW",
                "entities/0OfT51J/attributes/Address/0VFRdHW/SourceLastUpdateDate/14YP3E0T",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF",
                "entities/0OfT51J/attributes/Address/0VFRdHW/SourceCreatedDate/14YP3IGj",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Country/14YP35Tx",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF/NestedEntityId/14YP3V3V",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF/SourceCreatedDate/14YP3ZJl"
              ],
              "createDate": "2025-03-07T11:29:41.151Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T11:29:41.151Z",
              "uri": "entities/0OfT51J/crosswalks/0OHfw9l.14YP3hqH",
              "value": "1-2UV250U|1-4QKNL4"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine2/14YP2oQv",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR/PostalCode/14YP31Dh",
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/14YP2kAf",
                "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/14YP39kD",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR",
                "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu/SourceLastUpdateDate/kR5Ay5g",
                "entities/0OfT51J/attributes/Address/0VFRdHW/IsDeleted/14YP3MWz",
                "entities/0OfT51J/attributes/Address/0VFRdHW",
                "entities/0OfT51J/attributes/Address/0VFRdHW/SourceCreatedDate/14YP3IGj",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu/SourceCreatedDate/kR5AtpQ",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu/NestedEntityId/kR5ApZA",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Country/kR5Ah2e"
              ],
              "createDate": "2025-03-07T12:15:10.705Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:15:10.705Z",
              "uri": "entities/0OfT51J/crosswalks/0OHfw9l.16yQynnh",
              "value": "1-4QKNL4--1-1V11QGT"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine2/14YP2oQv",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR/PostalCode/14YP31Dh",
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/14YP2kAf",
                "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/14YP39kD",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg/SourceLastUpdateDate/kH0MpdS",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg/SourceCreatedDate/kH0MlNC",
                "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
                "entities/0OfT51J/attributes/Address/0VFRdHW/IsDeleted/14YP3MWz",
                "entities/0OfT51J/attributes/Address/0VFRdHW",
                "entities/0OfT51J/attributes/Address/0VFRdHW/SourceCreatedDate/14YP3IGj",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg/NestedEntityId/kH0Mh6w",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Country/kR5Ah2e",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0OHfw9l.1jpzCMKI",
              "value": "1-4QKNL4--1-4TMZR8P"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine2/14YP2oQv",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR/PostalCode/14YP31Dh",
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/14YP2kAf",
                "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/14YP39kD",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR",
                "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
                "entities/0OfT51J/attributes/Address/0VFRdHW/IsDeleted/14YP3MWz",
                "entities/0OfT51J/attributes/Address/0VFRdHW",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7/NestedEntityId/14z0wFrN",
                "entities/0OfT51J/attributes/Address/0VFRdHW/SourceCreatedDate/14YP3IGj",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7/SourceCreatedDate/14z0wK7d",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Country/kR5Ah2e",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7/SourceLastUpdateDate/14z0wONt"
              ],
              "createDate": "2025-03-07T12:25:07.796Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:25:07.796Z",
              "uri": "entities/0OfT51J/crosswalks/0OHfw9l.jf4ljh7",
              "value": "1-4QKNL4--1-2I3XRU1"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine2/14YP2oQv",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR/PostalCode/14YP31Dh",
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/14YP2kAf",
                "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/14YP39kD",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR",
                "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
                "entities/0OfT51J/attributes/Address/0VFRdHW/IsDeleted/14YP3MWz",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J/SourceCreatedDate/1Ub3w8fp",
                "entities/0OfT51J/attributes/Address/0VFRdHW",
                "entities/0OfT51J/attributes/Address/0VFRdHW/SourceCreatedDate/14YP3IGj",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J/SourceLastUpdateDate/1Ub3wCw5",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J/NestedEntityId/1Ub3w4PZ",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Country/kR5Ah2e"
              ],
              "createDate": "2025-03-07T12:25:07.796Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:25:07.796Z",
              "uri": "entities/0OfT51J/crosswalks/0OHfw9l.jf4tMnl",
              "value": "1-4QKNL4--1-2I3XRWM"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine2/14YP2oQv",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR/PostalCode/14YP31Dh",
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/14YP2kAf",
                "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/14YP39kD",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR",
                "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej/SourceLastUpdateDate/1Ub3xeRV",
                "entities/0OfT51J/attributes/Address/0VFRdHW/IsDeleted/14YP3MWz",
                "entities/0OfT51J/attributes/Address/0VFRdHW",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej/SourceCreatedDate/1Ub3xaBF",
                "entities/0OfT51J/attributes/Address/0VFRdHW/SourceCreatedDate/14YP3IGj",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej/NestedEntityId/1Ub3xVuz",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Country/kR5Ah2e"
              ],
              "createDate": "2025-03-07T12:37:56.901Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:37:56.901Z",
              "uri": "entities/0OfT51J/crosswalks/0OHfw9l.18GYieoH",
              "value": "1-4QKNL4--1-SD86C2"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/1Ub4ICqf",
                "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x",
                "entities/0OfT51J/attributes/Address/0VFRdHW/VerificationStatus/1Ub4GQ1x",
                "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x/Latitude/1Ub4IggT",
                "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x/GeoAccuracy/1Ub4IcQD",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT",
                "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT/PostalCode/1Ub4Gcoj",
                "entities/0OfT51J/attributes/Address/0VFRdHW",
                "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x/Longitude/1Ub4Ikwj",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT/Zip5/1Ub4GlLF",
                "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/1Ub4HrXN",
                "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT/Zip4/1Ub4Gh4z",
                "entities/0OfT51J/attributes/Address/0VFRdHW/Country/kR5Ah2e"
              ],
              "createDate": "2025-03-11T00:59:50.938Z",
              "type": "configuration/sources/ReltioCleanser",
              "updateDate": "2025-03-11T00:59:50.938Z",
              "uri": "entities/0OfT51J/crosswalks/0OHfw9l.1Ub47kzR",
              "value": "0OHfw9l"
            }
          ],
          "objectURI": "entities/0OHfw9l",
          "type": "configuration/entityTypes/Location"
        },
        "refRelation": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRdHW/AddressType/1jpzBOeg",
                "entities/0OfT51J/attributes/Address/0VFRdHW"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/Reltio",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0VFRdHW.1jq2X4qI",
              "value": "0VFRdHW"
            }
          ],
          "endRefIgnored": False,
          "endRefPinned": False,
          "objectURI": "relations/0VFRdHW",
          "startRefIgnored": False,
          "startRefPinned": False,
          "type": "configuration/relationTypes/HCPHasAddress"
        },
        "relationshipLabel": "Mailing",
        "startObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-4TMZR8M"
          }
        ],
        "uri": "entities/0OfT51J/attributes/Address/0VFRdHW",
        "value": {
          "AddressLine1": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/1Ub4ICqf",
              "value": "1015 Walnut St Fl 10"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine1/14YP2kAf",
              "value": "1015 Walnut Street"
            }
          ],
          "AddressLine2": [
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine2",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/AddressLine2/14YP2oQv",
              "value": "Curtis Building, 10th Floor"
            }
          ],
          "AddressType": [
            {
              "lookupCode": "Mailing",
              "lookupRawValue": "Mailing",
              "ov": True,
              "type": "configuration/relationTypes/HCPHasAddress/attributes/AddressType",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/AddressType/1jpzBOeg",
              "value": "Mailing"
            }
          ],
          "City": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/City",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/City/14YP2shB",
              "value": "Philadelphia"
            }
          ],
          "Country": [
            {
              "lookupCode": "US",
              "lookupRawValue": "United States",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Country/kR5Ah2e",
              "value": "United States"
            },
            {
              "lookupCode": "US",
              "lookupRawValue": "UNITED STATES",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Country/14YP35Tx",
              "value": "United States"
            }
          ],
          "GeoLocation": [
            {
              "label": "39.948780, -75.157930",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x",
              "value": {
                "GeoAccuracy": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/GeoAccuracy",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x/GeoAccuracy/1Ub4IcQD",
                    "value": "P4"
                  }
                ],
                "Latitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Latitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x/Latitude/1Ub4IggT",
                    "value": "39.948780"
                  }
                ],
                "Longitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Longitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/GeoLocation/1Ub4IY9x/Longitude/1Ub4Ikwj",
                    "value": "-75.157930"
                  }
                ]
              }
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/IsDeleted/14YP3MWz",
              "value": "False"
            }
          ],
          "PostalCode": [
            {
              "label": "19107-5005",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT",
              "value": {
                "PostalCode": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT/PostalCode/1Ub4Gcoj",
                    "value": "19107-5005"
                  }
                ],
                "Zip4": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip4",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT/Zip4/1Ub4Gh4z",
                    "value": "5005"
                  }
                ],
                "Zip5": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/1Ub4GYYT/Zip5/1Ub4GlLF",
                    "value": "19107"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR",
              "value": {
                "PostalCode": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/PostalCode/14YP2wxR/PostalCode/14YP31Dh",
                    "value": "19107"
                  }
                ]
              }
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/SourceCreatedDate/14YP3IGj",
              "value": "2011-09-13T22:16:40.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/SourceLastUpdateDate/14YP3E0T",
              "value": "2016-09-26T14:35:27.000+0000"
            }
          ],
          "StateProvince": [
            {
              "lookupCode": "PA",
              "lookupRawValue": "PA",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/1Ub4HrXN",
              "value": "PENNSYLVANIA"
            },
            {
              "lookupCode": "PA",
              "lookupRawValue": "Pennsylvania",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/StateProvince/14YP39kD",
              "value": "PENNSYLVANIA"
            }
          ],
          "Unit": [
            {
              "label": "",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg/NestedEntityId/kH0Mh6w",
                    "value": "1-4QKNL4--1-4TMZR8P|3797989946631188977"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg/SourceCreatedDate/kH0MlNC",
                    "value": "2011-09-13T22:16:40.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kH0Mcqg/SourceLastUpdateDate/kH0MpdS",
                    "value": "2016-09-26T14:35:27.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej/NestedEntityId/1Ub3xVuz",
                    "value": "1-4QKNL4--1-SD86C2|1440609217670625806"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej/SourceCreatedDate/1Ub3xaBF",
                    "value": "2011-09-13T22:16:40.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3xRej/SourceLastUpdateDate/1Ub3xeRV",
                    "value": "2016-09-26T14:35:27.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J/NestedEntityId/1Ub3w4PZ",
                    "value": "1-4QKNL4--1-2I3XRWM|2933571492161600809"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J/SourceCreatedDate/1Ub3w8fp",
                    "value": "2011-09-13T22:16:40.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/1Ub3w09J/SourceLastUpdateDate/1Ub3wCw5",
                    "value": "2016-09-26T14:35:27.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7/NestedEntityId/14z0wFrN",
                    "value": "1-4QKNL4--1-2I3XRU1|535278089507149200"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7/SourceCreatedDate/14z0wK7d",
                    "value": "2011-09-13T22:16:40.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14z0wBb7/SourceLastUpdateDate/14z0wONt",
                    "value": "2016-09-26T14:35:27.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu/NestedEntityId/kR5ApZA",
                    "value": "1-4QKNL4--1-1V11QGT|-2308074932721542928"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu/SourceCreatedDate/kR5AtpQ",
                    "value": "2011-09-13T22:16:40.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/kR5AlIu/SourceLastUpdateDate/kR5Ay5g",
                    "value": "2016-09-26T14:35:27.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF/NestedEntityId/14YP3V3V",
                    "value": "1-2UV250U|1-4QKNL4|6726242020657891243"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF/SourceCreatedDate/14YP3ZJl",
                    "value": "2011-09-13T22:16:40.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/Unit/14YP3QnF/SourceLastUpdateDate/14YP3da1",
                    "value": "2016-09-26T14:35:27.000+0000"
                  }
                ]
              }
            }
          ],
          "VerificationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/VerificationStatus",
              "uri": "entities/0OfT51J/attributes/Address/0VFRdHW/VerificationStatus/1Ub4GQ1x",
              "value": "Verified"
            }
          ]
        }
      },
      {
        "endObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-653WBFT--1-653WBFU"
          }
        ],
        "label": "723 W Mount Airy Ave, Philadelphia, PENNSYLVANIA, 19119-3327, United States",
        "ov": True,
        "refEntity": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRlo2/AddressLine1/1jpzDnpi",
                "entities/0OfT51J/attributes/Address/0VFRlo2/IsDeleted/1jpzEYiY",
                "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jpzE0cU",
                "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW/NestedEntityId/1jpzELvm",
                "entities/0OfT51J/attributes/Address/0VFRlo2/StateProvince/1jpzDwME",
                "entities/0OfT51J/attributes/Address/0VFRlo2/Country/1jpzE990",
                "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW/SourceLastUpdateDate/1jpzEUSI",
                "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jpzE0cU/PostalCode/1jpzE4sk",
                "entities/0OfT51J/attributes/Address/0VFRlo2",
                "entities/0OfT51J/attributes/Address/0VFRlo2/City/1jpzDs5y",
                "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW",
                "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW/SourceCreatedDate/1jpzEQC2",
                "entities/0OfT51J/attributes/Address/0VFRlo2/SourceCreatedDate/1jpzEDPG"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0iOoNLm.1jpzEcyo",
              "value": "1-653WBFT--1-653WBFU"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI/Latitude/1jq7aUKo",
                "entities/0OfT51J/attributes/Address/0VFRlo2/AddressLine1/1jpzDnpi",
                "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI/GeoAccuracy/1jq7aQ4Y",
                "entities/0OfT51J/attributes/Address/0VFRlo2/StateProvince/1jq7ZjRy",
                "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK/Zip4/1jq7YdFq",
                "entities/0OfT51J/attributes/Address/0VFRlo2/Country/1jpzE990",
                "entities/0OfT51J/attributes/Address/0VFRlo2/VerificationStatus/1jq7YMCo",
                "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK",
                "entities/0OfT51J/attributes/Address/0VFRlo2",
                "entities/0OfT51J/attributes/Address/0VFRlo2/City/1jpzDs5y",
                "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI",
                "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK/PostalCode/1jq7YYza",
                "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK/Zip5/1jq7YhW6",
                "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI/Longitude/1jq7aYb4"
              ],
              "createDate": "2025-03-07T12:41:54.367Z",
              "type": "configuration/sources/ReltioCleanser",
              "updateDate": "2025-03-07T12:41:54.367Z",
              "uri": "entities/0OfT51J/crosswalks/0iOoNLm.1jq7QB06",
              "value": "0iOoNLm"
            }
          ],
          "objectURI": "entities/0iOoNLm",
          "type": "configuration/entityTypes/Location"
        },
        "refRelation": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRlo2",
                "entities/0OfT51J/attributes/Address/0VFRlo2/AddressType/1jpzDjZS"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/Reltio",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0VFRlo2.1jq2XLtK",
              "value": "0VFRlo2"
            }
          ],
          "endRefIgnored": False,
          "endRefPinned": False,
          "objectURI": "relations/0VFRlo2",
          "startRefIgnored": False,
          "startRefPinned": False,
          "type": "configuration/relationTypes/HCPHasAddress"
        },
        "relationshipLabel": "Mailing",
        "startObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-4TMZR8M"
          }
        ],
        "uri": "entities/0OfT51J/attributes/Address/0VFRlo2",
        "value": {
          "AddressLine1": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/AddressLine1/1jpzDnpi",
              "value": "723 W Mount Airy Ave"
            }
          ],
          "AddressType": [
            {
              "lookupCode": "Mailing",
              "lookupRawValue": "Mailing",
              "ov": True,
              "type": "configuration/relationTypes/HCPHasAddress/attributes/AddressType",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/AddressType/1jpzDjZS",
              "value": "Mailing"
            }
          ],
          "City": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/City",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/City/1jpzDs5y",
              "value": "Philadelphia"
            }
          ],
          "Country": [
            {
              "lookupCode": "US",
              "lookupRawValue": "United States",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/Country/1jpzE990",
              "value": "United States"
            }
          ],
          "GeoLocation": [
            {
              "label": "40.047670, -75.204200",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI",
              "value": {
                "GeoAccuracy": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/GeoAccuracy",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI/GeoAccuracy/1jq7aQ4Y",
                    "value": "I4"
                  }
                ],
                "Latitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Latitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI/Latitude/1jq7aUKo",
                    "value": "40.047670"
                  }
                ],
                "Longitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Longitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/GeoLocation/1jq7aLoI/Longitude/1jq7aYb4",
                    "value": "-75.204200"
                  }
                ]
              }
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/IsDeleted/1jpzEYiY",
              "value": "False"
            }
          ],
          "PostalCode": [
            {
              "label": "19119-3327",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK",
              "value": {
                "PostalCode": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK/PostalCode/1jq7YYza",
                    "value": "19119-3327"
                  }
                ],
                "Zip4": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip4",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK/Zip4/1jq7YdFq",
                    "value": "3327"
                  }
                ],
                "Zip5": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jq7YUjK/Zip5/1jq7YhW6",
                    "value": "19119"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jpzE0cU",
              "value": {
                "PostalCode": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/PostalCode/1jpzE0cU/PostalCode/1jpzE4sk",
                    "value": "19119"
                  }
                ]
              }
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/SourceCreatedDate/1jpzEDPG",
              "value": "2022-07-15T12:34:23.000+0000"
            }
          ],
          "StateProvince": [
            {
              "lookupCode": "PA",
              "lookupRawValue": "PA",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/StateProvince/1jq7ZjRy",
              "value": "PENNSYLVANIA"
            },
            {
              "lookupCode": "PA",
              "lookupRawValue": "Pennsylvania",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/StateProvince/1jpzDwME",
              "value": "PENNSYLVANIA"
            }
          ],
          "Unit": [
            {
              "label": "",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW/NestedEntityId/1jpzELvm",
                    "value": "1-653WBFT--1-653WBFU|-7903753867387295172"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW/SourceCreatedDate/1jpzEQC2",
                    "value": "2022-07-15T12:34:23.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/Unit/1jpzEHfW/SourceLastUpdateDate/1jpzEUSI",
                    "value": "2022-07-15T12:35:57.000+0000"
                  }
                ]
              }
            }
          ],
          "VerificationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/VerificationStatus",
              "uri": "entities/0OfT51J/attributes/Address/0VFRlo2/VerificationStatus/1jq7YMCo",
              "value": "Verified"
            }
          ]
        }
      },
      {
        "endObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-1YKOAEQ--1-653WBFS"
          }
        ],
        "label": "132 S 10th St Ste 285, Philadelphia, PENNSYLVANIA, 19107-5207, United States",
        "ov": True,
        "refEntity": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/ojB0ftT",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ojB0oPz/NestedEntityId/ojB0sgF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/ojB0KaB",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ojB0oPz"
              ],
              "createDate": "2025-02-24T11:04:29.808Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-02-24T11:04:29.808Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.ojB0wwV",
              "value": "HCP-177262-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn/SourceLastUpdateDate/XJ7lp4Z",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn/SourceCreatedDate/XJ7lkoJ",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/Zip5/XJ7lY1X",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn/NestedEntityId/XJ7lgY3"
              ],
              "createDate": "2025-02-24T11:15:57.663Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-02-24T11:15:57.663Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.jGOO2KL",
              "value": "1-1YKOAEQ--1-39NYQF0"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA/NestedEntityId/OkuDrcQ",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA/SourceCreatedDate/OkuDvsg",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA/SourceLastUpdateDate/OkuE08w",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/Zip5/XJ7lY1X",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-02-24T11:11:58.194Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-02-24T11:11:58.194Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.kw4Aj2v",
              "value": "1-1YKOAEQ--1-1YKOAER"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/ojB0ftT",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/Zip4/1lcfN9A1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfNHgX",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/ojB0KaB",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/Zip5/XJ7lY1X",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfNHgX/NestedEntityId/1lcfNLwn"
              ],
              "createDate": "2025-03-07T11:15:15.585Z",
              "type": "configuration/sources/CITELINE",
              "updateDate": "2025-03-07T11:15:15.585Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.1e0uQtjW",
              "value": "HCO-258695-WORKPLACE"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB/SourceLastUpdateDate/1lcfOjBx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB/SourceCreatedDate/1lcfOevh",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB/NestedEntityId/1lcfOafR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.1jpzBBru",
              "value": "1-1YKOAEQ--1-653WBFS"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL/SourceLastUpdateDate/1KLEfDM7",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/1KLEewJ5",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL/NestedEntityId/1KLEf4pb",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceLastUpdateDate/1KLEfHcN",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL/SourceCreatedDate/1KLEf95r",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T11:37:10.066Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T11:37:10.066Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.1gTS0hso",
              "value": "1-5ROZKOV|1-1YKOAEQ"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3/SourceLastUpdateDate/wcpWEYp",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3/SourceCreatedDate/wcpWAIZ",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3/NestedEntityId/wcpW62J",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:43:12.033Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:43:12.033Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.18ZDX0LF",
              "value": "1-1YKOAEQ--1-4YPF9J2"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp/SourceCreatedDate/Vr9R8nL",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp/NestedEntityId/Vr9R4X5",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp/SourceLastUpdateDate/Vr9RD3b",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:25:07.796Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:25:07.796Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.jf4uSzt",
              "value": "1-1YKOAEQ--1-2NW6F3Z"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn/SourceLastUpdateDate/1Kg3hQEZ",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn/SourceCreatedDate/1Kg3hLyJ",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn/NestedEntityId/1Kg3hHi3"
              ],
              "createDate": "2025-03-07T12:32:08.104Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:32:08.104Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.17uBbv1Z",
              "value": "1-1YKOAEQ--1-39NWVRN"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx/SourceCreatedDate/1Kg3ijDT",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx/SourceLastUpdateDate/1Kg3inTj",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx/NestedEntityId/1Kg3iexD"
              ],
              "createDate": "2025-03-07T12:42:34.297Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:42:34.297Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.18WEWs3R",
              "value": "1-1YKOAEQ--1-4WK321A"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx/NestedEntityId/ebxuLlD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx/SourceCreatedDate/ebxuQ1T",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx/SourceLastUpdateDate/ebxuUHj",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:37:37.184Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:37:37.184Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.kPJKcZB",
              "value": "1-1YKOAEQ--1-4EV1FMG"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc/SourceCreatedDate/jFix9r8",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc/SourceLastUpdateDate/jFixE7O",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc/NestedEntityId/jFix5as",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:28:37.868Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:28:37.868Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.1j26K5Ni",
              "value": "1-1YKOAEQ--1-302WR9L"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco/SourceLastUpdateDate/jFiysPa",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco/NestedEntityId/jFiyjt4",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco/SourceCreatedDate/jFiyo9K"
              ],
              "createDate": "2025-03-07T12:42:34.297Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:42:34.297Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.18WEPJD3",
              "value": "1-1YKOAEQ--1-4WJXITH"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0/SourceCreatedDate/jFj0SRW",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0/NestedEntityId/jFj0OBG",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0/SourceLastUpdateDate/jFj0Whm",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:42:34.297Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:42:34.297Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.18WFFPyf",
              "value": "1-1YKOAEQ--1-4WK3275"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC/SourceCreatedDate/jFj26ji",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC/SourceLastUpdateDate/jFj2Azy",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC/NestedEntityId/jFj22TS",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:48:09.431Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:48:09.431Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.18oYtTrR",
              "value": "1-1YKOAEQ--1-5O7SV3U"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO/NestedEntityId/jFj3gle",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO/SourceLastUpdateDate/jFj3pIA",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO/SourceCreatedDate/jFj3l1u"
              ],
              "createDate": "2025-03-07T12:32:08.104Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:32:08.104Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.17uBWh5x",
              "value": "1-1YKOAEQ--1-39NWVMP"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna/SourceCreatedDate/jFj5PK6",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna/SourceLastUpdateDate/jFj5TaM",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna/NestedEntityId/jFj5L3q",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:32:08.104Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:32:08.104Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.17uBn7ld",
              "value": "1-1YKOAEQ--1-39O03RP"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/1KLEewJ5",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa/SourceCreatedDate/1pCKxtL6",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa/SourceLastUpdateDate/1pCKxxbM",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceLastUpdateDate/1KLEfHcN",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa/NestedEntityId/1pCKxp4q"
              ],
              "createDate": "2025-03-07T11:37:10.066Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T11:37:10.066Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.1gTS6TuU",
              "value": "1-5ROZKQG|1-1YKOAEQ"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m/NestedEntityId/1pCKzTN2",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m/SourceCreatedDate/1pCKzXdI",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m/SourceLastUpdateDate/1pCKzbtY",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:32:08.104Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:32:08.104Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.17uBIsO5",
              "value": "1-1YKOAEQ--1-39NPUTB"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy/NestedEntityId/1pCL17fE",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy/SourceLastUpdateDate/1pCL1GBk",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy/SourceCreatedDate/1pCL1BvU",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:42:34.297Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:42:34.297Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.18WF8gHN",
              "value": "1-1YKOAEQ--1-4WK323C"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ/SourceCreatedDate/1pCL2uTw",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ/NestedEntityId/1pCL2qDg",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ/SourceLastUpdateDate/1pCL2ykC",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/1KLEewJ5",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceLastUpdateDate/1KLEfHcN",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T11:37:10.066Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T11:37:10.066Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.1gTS3ate",
              "value": "1-5ROZKPS|1-1YKOAEQ"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc/SourceLastUpdateDate/1pCL4d2O",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc/SourceCreatedDate/1pCL4Ym8",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc/NestedEntityId/1pCL4UVs",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF"
              ],
              "createDate": "2025-03-07T12:32:08.104Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:32:08.104Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.17uBQ5vB",
              "value": "1-1YKOAEQ--1-39NWVFR"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo/SourceLastUpdateDate/1pCL6HKa",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo/SourceCreatedDate/1pCL6D4K",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo/NestedEntityId/1pCL68o4"
              ],
              "createDate": "2025-03-07T12:26:43.725Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:26:43.725Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.1iw9vZIY",
              "value": "1-1YKOAEQ--1-4XM1YSJ"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD/SourceCreatedDate/duVpKLj",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD/SourceLastUpdateDate/duVpObz",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD/NestedEntityId/duVpG5T"
              ],
              "createDate": "2025-03-07T12:42:34.297Z",
              "type": "configuration/sources/CTMS",
              "updateDate": "2025-03-07T12:42:34.297Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.18WFLoMf",
              "value": "1-1YKOAEQ--1-4WK328O"
            },
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/VerificationStatus/duWVbcR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/duWXOR9",
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x/Zip5/duWVwvj",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/duWX37r",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR/Longitude/duWXwXD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x/Zip4/duWVsfT",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x/PostalCode/duWVoPD",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR/Latitude/duWXsGx",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR/GeoAccuracy/duWXo0h",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j"
              ],
              "createDate": "2025-03-10T23:42:29.079Z",
              "type": "configuration/sources/ReltioCleanser",
              "updateDate": "2025-03-10T23:42:29.079Z",
              "uri": "entities/0OfT51J/crosswalks/0JPUuEV.duWMwZv",
              "value": "0JPUuEV"
            }
          ],
          "objectURI": "entities/0JPUuEV",
          "type": "configuration/entityTypes/Location"
        },
        "refRelation": {
          "crosswalks": [
            {
              "attributeURIs": [
                "entities/0OfT51J/attributes/Address/0VFRZ1G",
                "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressType/1jpzAISY"
              ],
              "createDate": "2025-03-07T12:41:53.787Z",
              "type": "configuration/sources/Reltio",
              "updateDate": "2025-03-07T12:41:53.787Z",
              "uri": "entities/0OfT51J/crosswalks/0VFRZ1G.1jq2WwJm",
              "value": "0VFRZ1G"
            }
          ],
          "endRefIgnored": False,
          "endRefPinned": False,
          "objectURI": "relations/0VFRZ1G",
          "startRefIgnored": False,
          "startRefPinned": False,
          "type": "configuration/relationTypes/HCPHasAddress"
        },
        "relationshipLabel": "Mailing",
        "startObjectCrosswalks": [
          {
            "type": "configuration/sources/CTMS",
            "value": "1-4TMZR8M"
          }
        ],
        "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G",
        "value": {
          "AddressLine1": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/duWXOR9",
              "value": "132 S 10th St Ste 285"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/XJ7lGyV",
              "value": "132 South 10th Street, Suite 285"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/AddressLine1",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressLine1/ojB0KaB",
              "value": "132 S 10th St, Suite 285 the Main Building"
            }
          ],
          "AddressType": [
            {
              "lookupCode": "Mailing",
              "lookupRawValue": "Mailing",
              "ov": True,
              "type": "configuration/relationTypes/HCPHasAddress/attributes/AddressType",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/AddressType/1jpzAISY",
              "value": "Mailing"
            }
          ],
          "City": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/City",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/City/ojB0OqR",
              "value": "Philadelphia"
            }
          ],
          "Country": [
            {
              "lookupCode": "US",
              "lookupRawValue": "United States",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/ojB0k9j",
              "value": "United States"
            },
            {
              "lookupCode": "US",
              "lookupRawValue": "UNITED STATES",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/Country",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Country/1KLEewJ5",
              "value": "United States"
            }
          ],
          "GeoLocation": [
            {
              "label": "39.948940, -75.157420",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR",
              "value": {
                "GeoAccuracy": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/GeoAccuracy",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR/GeoAccuracy/duWXo0h",
                    "value": "P4"
                  }
                ],
                "Latitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Latitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR/Latitude/duWXsGx",
                    "value": "39.948940"
                  }
                ],
                "Longitude": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/GeoLocation/attributes/Longitude",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/GeoLocation/duWXjkR/Longitude/duWXwXD",
                    "value": "-75.157420"
                  }
                ]
              }
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/IsDeleted/XJ7lCiF",
              "value": "False"
            }
          ],
          "PostalCode": [
            {
              "label": "19107-5207",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x",
              "value": {
                "PostalCode": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x/PostalCode/duWVoPD",
                    "value": "19107-5207"
                  }
                ],
                "Zip4": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip4",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x/Zip4/duWVsfT",
                    "value": "5207"
                  }
                ],
                "Zip5": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/duWVk8x/Zip5/duWVwvj",
                    "value": "19107"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD",
              "value": {
                "PostalCode": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/1lcfNQD3",
                    "value": "19107"
                  },
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/PostalCode",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/PostalCode/ojB0ftT",
                    "value": "19107-5244"
                  }
                ],
                "Zip4": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip4",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/Zip4/1lcfN9A1",
                    "value": "5244"
                  }
                ],
                "Zip5": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/PostalCode/attributes/Zip5",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/PostalCode/ojB0bdD/Zip5/XJ7lY1X",
                    "value": "19107"
                  }
                ]
              }
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceCreatedDate/XJ7lPV1",
              "value": "2015-06-23T10:29:46.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/SourceLastUpdateDate/1KLEfHcN",
              "value": "2016-09-21T18:20:36.000+0000"
            }
          ],
          "StateProvince": [
            {
              "lookupCode": "PA",
              "lookupRawValue": "PA",
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/duWX37r",
              "value": "PENNSYLVANIA"
            },
            {
              "lookupCode": "PA",
              "lookupRawValue": "Pennsylvania",
              "ov": False,
              "type": "configuration/entityTypes/Location/attributes/StateProvince",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/StateProvince/ojB0XMx",
              "value": "PENNSYLVANIA"
            }
          ],
          "Unit": [
            {
              "label": "",
              "ov": True,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC/NestedEntityId/jFj22TS",
                    "value": "1-1YKOAEQ--1-5O7SV3U|-3044546754297683824"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC/SourceCreatedDate/jFj26ji",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": True,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj1yDC/SourceLastUpdateDate/jFj2Azy",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3/NestedEntityId/wcpW62J",
                    "value": "1-1YKOAEQ--1-4YPF9J2|-8568873381714198168"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3/SourceCreatedDate/wcpWAIZ",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/wcpW1m3/SourceLastUpdateDate/wcpWEYp",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD/NestedEntityId/duVpG5T",
                    "value": "1-1YKOAEQ--1-4WK328O|-7345432720794077939"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD/SourceCreatedDate/duVpKLj",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/duVpBpD/SourceLastUpdateDate/duVpObz",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy/NestedEntityId/1pCL17fE",
                    "value": "1-1YKOAEQ--1-4WK323C|8185160919743682469"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy/SourceCreatedDate/1pCL1BvU",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL13Oy/SourceLastUpdateDate/1pCL1GBk",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0/NestedEntityId/jFj0OBG",
                    "value": "1-1YKOAEQ--1-4WK3275|-7484156985409653632"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0/SourceCreatedDate/jFj0SRW",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj0Jv0/SourceLastUpdateDate/jFj0Whm",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco/NestedEntityId/jFiyjt4",
                    "value": "1-1YKOAEQ--1-4WJXITH|-1641208672083922643"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco/SourceCreatedDate/jFiyo9K",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFiyfco/SourceLastUpdateDate/jFiysPa",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx/NestedEntityId/1Kg3iexD",
                    "value": "1-1YKOAEQ--1-4WK321A|8736625124639548096"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx/SourceCreatedDate/1Kg3ijDT",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3iagx/SourceLastUpdateDate/1Kg3inTj",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB/NestedEntityId/1lcfOafR",
                    "value": "1-1YKOAEQ--1-653WBFS|-1040811748851075627"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB/SourceCreatedDate/1lcfOevh",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfOWPB/SourceLastUpdateDate/1lcfOjBx",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx/NestedEntityId/ebxuLlD",
                    "value": "1-1YKOAEQ--1-4EV1FMG|-7415854091697507847"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx/SourceCreatedDate/ebxuQ1T",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ebxuHUx/SourceLastUpdateDate/ebxuUHj",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc/NestedEntityId/1pCL4UVs",
                    "value": "1-1YKOAEQ--1-39NWVFR|-8404786439889434350"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc/SourceCreatedDate/1pCL4Ym8",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL4QFc/SourceLastUpdateDate/1pCL4d2O",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m/NestedEntityId/1pCKzTN2",
                    "value": "1-1YKOAEQ--1-39NPUTB|6064965850259549121"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m/SourceCreatedDate/1pCKzXdI",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKzP6m/SourceLastUpdateDate/1pCKzbtY",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna/NestedEntityId/jFj5L3q",
                    "value": "1-1YKOAEQ--1-39O03RP|-2656242172135655396"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna/SourceCreatedDate/jFj5PK6",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj5Gna/SourceLastUpdateDate/jFj5TaM",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO/NestedEntityId/jFj3gle",
                    "value": "1-1YKOAEQ--1-39NWVMP|-3862818511467590633"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO/SourceCreatedDate/jFj3l1u",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFj3cVO/SourceLastUpdateDate/jFj3pIA",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn/NestedEntityId/1Kg3hHi3",
                    "value": "1-1YKOAEQ--1-39NWVRN|-3419428117099268240"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn/SourceCreatedDate/1Kg3hLyJ",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1Kg3hDRn/SourceLastUpdateDate/1Kg3hQEZ",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc/NestedEntityId/jFix5as",
                    "value": "1-1YKOAEQ--1-302WR9L|-7977032807255439569"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc/SourceCreatedDate/jFix9r8",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/jFix1Kc/SourceLastUpdateDate/jFixE7O",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo/NestedEntityId/1pCL68o4",
                    "value": "1-1YKOAEQ--1-4XM1YSJ|8596186001537580588"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo/SourceCreatedDate/1pCL6D4K",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL64Xo/SourceLastUpdateDate/1pCL6HKa",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp/NestedEntityId/Vr9R4X5",
                    "value": "1-1YKOAEQ--1-2NW6F3Z|-6648724966834598614"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp/SourceCreatedDate/Vr9R8nL",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/Vr9R0Gp/SourceLastUpdateDate/Vr9RD3b",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ/NestedEntityId/1pCL2qDg",
                    "value": "1-5ROZKPS|1-1YKOAEQ|5181169065032262443"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ/SourceCreatedDate/1pCL2uTw",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCL2lxQ/SourceLastUpdateDate/1pCL2ykC",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa/NestedEntityId/1pCKxp4q",
                    "value": "1-5ROZKQG|1-1YKOAEQ|8895098399933414139"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa/SourceCreatedDate/1pCKxtL6",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1pCKxkoa/SourceLastUpdateDate/1pCKxxbM",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL/NestedEntityId/1KLEf4pb",
                    "value": "1-5ROZKOV|1-1YKOAEQ|861454395011105069"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL/SourceCreatedDate/1KLEf95r",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1KLEf0ZL/SourceLastUpdateDate/1KLEfDM7",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfNHgX",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/1lcfNHgX/NestedEntityId/1lcfNLwn",
                    "value": "HCO-258695-WORKPLACE"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn/NestedEntityId/XJ7lgY3",
                    "value": "1-1YKOAEQ--1-39NYQF0|-6602836012880963378"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn/SourceCreatedDate/XJ7lkoJ",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/XJ7lcHn/SourceLastUpdateDate/XJ7lp4Z",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA/NestedEntityId/OkuDrcQ",
                    "value": "1-1YKOAEQ--1-1YKOAER|1716557123374076694"
                  }
                ],
                "SourceCreatedDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceCreatedDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA/SourceCreatedDate/OkuDvsg",
                    "value": "2015-06-23T10:29:46.000+0000"
                  }
                ],
                "SourceLastUpdateDate": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/SourceLastUpdateDate",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/OkuDnMA/SourceLastUpdateDate/OkuE08w",
                    "value": "2016-09-21T18:20:36.000+0000"
                  }
                ]
              }
            },
            {
              "label": "",
              "ov": False,
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ojB0oPz",
              "value": {
                "NestedEntityId": [
                  {
                    "ov": False,
                    "type": "configuration/entityTypes/Location/attributes/Unit/attributes/NestedEntityId",
                    "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/Unit/ojB0oPz/NestedEntityId/ojB0sgF",
                    "value": "HCP-177262-WORKPLACE"
                  }
                ]
              }
            }
          ],
          "VerificationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/Location/attributes/VerificationStatus",
              "uri": "entities/0OfT51J/attributes/Address/0VFRZ1G/VerificationStatus/duWVbcR",
              "value": "Verified"
            }
          ]
        }
      }
    ],
    "Education": [
      {
        "label": "Doctor of Medicine,",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Education/evnc6Lb",
        "value": {
          "Degree": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Education/attributes/Degree",
              "uri": "entities/0OfT51J/attributes/Education/evnc6Lb/Degree/evncJ8N",
              "value": "Doctor of Medicine"
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Education/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Education/evnc6Lb/IsDeleted/evncAbr",
              "value": "False"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Education/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Education/evnc6Lb/NestedEntityId/evncEs7",
              "value": "1-4TMZR8M|7944030965589951862"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Education/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Education/evnc6Lb/SourceCreatedDate/evncNOd",
              "value": "2022-07-15T12:31:30.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Education/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Education/evnc6Lb/SourceLastUpdateDate/evncRet",
              "value": "2022-07-15T12:31:33.000+0000"
            }
          ]
        }
      },
      {
        "label": "FACS,",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Education/15MFa6LF",
        "value": {
          "Degree": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Education/attributes/Degree",
              "uri": "entities/0OfT51J/attributes/Education/15MFa6LF/Degree/15MFaAbV",
              "value": "FACS"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Education/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Education/15MFa6LF/NestedEntityId/15MFaErl",
              "value": "HCP-973664|FACS"
            }
          ]
        }
      }
    ],
    "Email": [
      {
        "label": "alliric.willis@jefferson.edu - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Email/15MFZ097",
        "value": {
          "Domain": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Email/attributes/Domain",
              "uri": "entities/0OfT51J/attributes/Email/15MFZ097/Domain/nq1Wq1I",
              "value": "jefferson.edu"
            }
          ],
          "DomainType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Email/attributes/DomainType",
              "uri": "entities/0OfT51J/attributes/Email/15MFZ097/DomainType/nq1WuHY",
              "value": "PRIVATE"
            }
          ],
          "Email": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Email/attributes/Email",
              "uri": "entities/0OfT51J/attributes/Email/15MFZ097/Email/evnruex",
              "value": "alliric.willis@jefferson.edu"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Email/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Email/15MFZ097/NestedEntityId/npysOm0",
              "value": "HCP-973664|CITELINE|alliric.willis@jefferson.edu"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Email/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Email/15MFZ097/Type/npysKVk",
              "value": "CITELINE"
            }
          ],
          "Username": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Email/attributes/Username",
              "uri": "entities/0OfT51J/attributes/Email/15MFZ097/Username/nq1X2o4",
              "value": "alliric.willis"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Email/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Email/15MFZ097/ValidationStatus/nq1WyXo",
              "value": "VALID"
            }
          ]
        }
      }
    ],
    "EntityUUID": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/EntityUUID",
        "uri": "entities/0OfT51J/attributes/EntityUUID/15N4ACrt",
        "value": "f8217197-6d49-41ea-a171-976d49f1eacb"
      },
      {
        "ov": False,
        "type": "configuration/entityTypes/HCP/attributes/EntityUUID",
        "uri": "entities/0OfT51J/attributes/EntityUUID/evnjSPD",
        "value": "373e2e9b-45c3-439e-be2e-9b45c3d39e09"
      },
      {
        "ov": False,
        "type": "configuration/entityTypes/HCP/attributes/EntityUUID",
        "uri": "entities/0OfT51J/attributes/EntityUUID/evnc25L",
        "value": "29b07876-8857-4db5-b078-7688575db513"
      }
    ],
    "FirstName": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/FirstName",
        "uri": "entities/0OfT51J/attributes/FirstName/15MFVuLV",
        "value": "Alliric"
      }
    ],
    "Gender": [
      {
        "lookupCode": "Male",
        "lookupRawValue": "Male",
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/Gender",
        "uri": "entities/0OfT51J/attributes/Gender/evnjJsh",
        "value": "Male"
      }
    ],
    "Identifiers": [
      {
        "label": "CITELINE - 973664",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Identifiers/15MFZHC9",
        "value": {
          "ID": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/ID",
              "uri": "entities/0OfT51J/attributes/Identifiers/15MFZHC9/ID/15MFZPif",
              "value": "973664"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Identifiers/15MFZHC9/NestedEntityId/15MFZTyv",
              "value": "HCP-973664|CITELINE|973664"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Identifiers/15MFZHC9/Type/15MFZLSP",
              "value": "CITELINE"
            }
          ]
        }
      },
      {
        "label": "CTMS - 1-4TMZR8M",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Identifiers/evndc7H",
        "value": {
          "ID": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/ID",
              "uri": "entities/0OfT51J/attributes/Identifiers/evndc7H/ID/evndtAJ",
              "value": "1-4TMZR8M"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Identifiers/evndc7H/NestedEntityId/evndkdn",
              "value": "1-4TMZR8M|CTMS|1-4TMZR8M"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Identifiers/evndc7H/SourceCreatedDate/evndou3",
              "value": "2019-11-06T00:26:15.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Identifiers/evndc7H/SourceLastUpdateDate/evndxQZ",
              "value": "2023-06-22T18:19:36.000+0000"
            }
          ],
          "Type": [
            {
              "lookupCode": "CTMS",
              "lookupRawValue": "CTMS",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Identifiers/evndc7H/Type/evndgNX",
              "value": "CTMS"
            }
          ]
        }
      },
      {
        "label": "NPI - 1366475287",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Identifiers/15MFZYFB",
        "value": {
          "ID": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/ID",
              "uri": "entities/0OfT51J/attributes/Identifiers/15MFZYFB/ID/15MFZglh",
              "value": "1366475287"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Identifiers/15MFZYFB/NestedEntityId/evnjjSF",
              "value": "WUSM00617052|NPI|1366475287"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Identifiers/15MFZYFB/NestedEntityId/15MFZl1x",
              "value": "HCP-973664|NPI|1366475287"
            }
          ],
          "Type": [
            {
              "lookupCode": "NPI",
              "lookupRawValue": "NPI",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Identifiers/15MFZYFB/Type/15MFZcVR",
              "value": "NPI"
            }
          ]
        }
      },
      {
        "label": "ONEKEY - WUSM00617052",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Identifiers/1jpzF6oc",
        "value": {
          "ID": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/ID",
              "uri": "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/ID/evneETb",
              "value": "WUSM00617052"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/NestedEntityId/evnhSnj",
              "value": "WUSM00617052|ONEKEY|WUSM00617052"
            },
            {
              "ov": False,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/NestedEntityId/evne5x5",
              "value": "1-4TMZR8M|ONEKEY|WUSM00617052"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/SourceCreatedDate/evneADL",
              "value": "2019-11-06T00:26:15.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/SourceLastUpdateDate/evneIjr",
              "value": "2023-06-22T18:19:36.000+0000"
            }
          ],
          "Type": [
            {
              "lookupCode": "ONEKEY",
              "lookupRawValue": "ONEKEY",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Identifiers/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/Type/evne1gp",
              "value": "ONEKEY"
            }
          ]
        }
      }
    ],
    "IsDeleted": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/IsDeleted",
        "uri": "entities/0OfT51J/attributes/IsDeleted/evnYs1T",
        "value": "False"
      }
    ],
    "LastName": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/LastName",
        "uri": "entities/0OfT51J/attributes/LastName/15MFW2s1",
        "value": "Willis"
      }
    ],
    "License": [
      {
        "label": "310-110808, State MISSOURI",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/License/evnilmd",
        "value": {
          "ExpirationDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/ExpirationDate",
              "uri": "entities/0OfT51J/attributes/License/evnilmd/ExpirationDate/evnj75v",
              "value": "2004-06-30"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/License/evnilmd/NestedEntityId/evniuJ9",
              "value": "WUSM00617052|310-110808"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/Number",
              "uri": "entities/0OfT51J/attributes/License/evnilmd/Number/evnj2pf",
              "value": "310-110808"
            }
          ],
          "State": [
            {
              "lookupCode": "MO",
              "lookupRawValue": "MO",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/State",
              "uri": "entities/0OfT51J/attributes/License/evnilmd/State/evnjBMB",
              "value": "MISSOURI"
            }
          ],
          "Status": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/Status",
              "uri": "entities/0OfT51J/attributes/License/evnilmd/Status/evniq2t",
              "value": "Inactive"
            }
          ],
          "Type": [
            {
              "lookupError": "1003: RDM canonical value mapping not found for value [Medical Doctor] and source [ONEKEY] in tenant [vasuRDDHVgTtB0e]",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/Type",
              "uri": "entities/0OfT51J/attributes/License/evnilmd/Type/evniyZP",
              "value": "Medical Doctor"
            }
          ]
        }
      },
      {
        "label": "424463, State PENNSYLVANIA",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/License/evnarcx",
        "value": {
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/License/evnarcx/IsDeleted/evnavtD",
              "value": "False"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/License/evnarcx/NestedEntityId/evnb09T",
              "value": "1-4TMZR8M|7741449714341258764"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/Number",
              "uri": "entities/0OfT51J/attributes/License/evnarcx/Number/evnb4Pj",
              "value": "424463"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/License/evnarcx/SourceCreatedDate/evnb8fz",
              "value": "2022-07-15T12:32:42.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/License/evnarcx/SourceLastUpdateDate/evnbHCV",
              "value": "2022-07-15T12:33:00.000+0000"
            }
          ],
          "State": [
            {
              "lookupCode": "PA",
              "lookupRawValue": "Pennsylvania",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/State",
              "uri": "entities/0OfT51J/attributes/License/evnarcx/State/evnbCwF",
              "value": "PENNSYLVANIA"
            }
          ]
        }
      },
      {
        "label": "25MA10031000, State NEW JERSEY",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/License/evnbLSl",
        "value": {
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/License/evnbLSl/IsDeleted/evnbPj1",
              "value": "False"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/License/evnbLSl/NestedEntityId/evnbTzH",
              "value": "1-4TMZR8M|3658216328968552810"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/Number",
              "uri": "entities/0OfT51J/attributes/License/evnbLSl/Number/evnbYFX",
              "value": "25MA10031000"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/License/evnbLSl/SourceCreatedDate/evnbcVn",
              "value": "2022-07-15T12:33:00.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/License/evnbLSl/SourceLastUpdateDate/evnbl2J",
              "value": "2022-07-15T12:33:22.000+0000"
            }
          ],
          "State": [
            {
              "lookupCode": "NJ",
              "lookupRawValue": "New Jersey",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/License/attributes/State",
              "uri": "entities/0OfT51J/attributes/License/evnbLSl/State/evnbgm3",
              "value": "NEW JERSEY"
            }
          ]
        }
      }
    ],
    "MiddleInitial": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/MiddleInitial",
        "uri": "entities/0OfT51J/attributes/MiddleInitial/15MFVybl",
        "value": "I"
      }
    ],
    "MiddleName": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/MiddleName",
        "uri": "entities/0OfT51J/attributes/MiddleName/evnbxp5",
        "value": "Isaac"
      }
    ],
    "Name": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/Name",
        "uri": "entities/0OfT51J/attributes/Name/nq0CpBQ",
        "value": "Alliric Isaac Willis"
      }
    ],
    "Phone": [
      {
        "label": "(215) 955-6000 - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/AreaCode/evnlFDv",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/CountryCode/evnl2R9",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/DigitCount/evnlWGx",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/FormatMask/evnl6hP",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/FormattedNumber/evnlenT",
              "value": "(215) 955-6000"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/GeoArea/evnlS0h",
              "value": "Philadelphia, PA"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/GeoCountry/evnlNkR",
              "value": "United States"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/LineType/evnlAxf",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/LocalNumber/evnlaXD",
              "value": "9556000"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/NestedEntityId/15MFXHaf",
              "value": "HCP-973664|CITELINE|215-955-6000"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/Number/15MFXDKP",
              "value": "215-955-6000"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/Type/15MFX949",
              "value": "CITELINE"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/15MFX4nt/ValidationStatus/evnlJUB",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 955-6750 - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/AreaCode/evnlvqV",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/CountryCode/evnlj3j",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/DigitCount/evnmCtX",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/FormatMask/evnlnJz",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/FormattedNumber/evnmLQ3",
              "value": "(215) 955-6750"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/GeoArea/evnm8dH",
              "value": "Philadelphia, PA"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/GeoCountry/evnm4N1",
              "value": "United States"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/LineType/evnlraF",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/LocalNumber/evnmH9n",
              "value": "9556750"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/NestedEntityId/15MFXYdh",
              "value": "HCP-973664|CITELINE|215-955-6750"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/Number/15MFXUNR",
              "value": "215-955-6750"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/Type/15MFXQ7B",
              "value": "CITELINE"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXLqv/ValidationStatus/evnm06l",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 955-6999 - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/15MFXctx",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/AreaCode/evnmcT5",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/CountryCode/evnmPgJ",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/DigitCount/evnmtW7",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/FormatMask/evnmTwZ",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/FormattedNumber/evnn22d",
              "value": "(215) 955-6999"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/GeoArea/evnmpFr",
              "value": "Philadelphia, PA"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/GeoCountry/evnmkzb",
              "value": "United States"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/LineType/evnmYCp",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/LocalNumber/evnmxmN",
              "value": "9556999"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/NestedEntityId/15MFXpgj",
              "value": "HCP-973664|CITELINE|215-955-6999"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/Number/15MFXlQT",
              "value": "215-955-6999"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/Type/15MFXhAD",
              "value": "CITELINE"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXctx/ValidationStatus/evnmgjL",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 955-7106 - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/AreaCode/evnnJ5f",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/CountryCode/evnn6It",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/DigitCount/evnna8h",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/FormatMask/evnnAZ9",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/FormattedNumber/evnnifD",
              "value": "(215) 955-7106"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/GeoArea/evnnVsR",
              "value": "Philadelphia, PA"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/GeoCountry/evnnRcB",
              "value": "United States"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/LineType/evnnEpP",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/LocalNumber/evnneOx",
              "value": "9557106"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/NestedEntityId/15MFY6jl",
              "value": "HCP-973664|CITELINE|215-955-7106"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/Number/15MFY2TV",
              "value": "215-955-7106"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/Type/15MFXyDF",
              "value": "CITELINE"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/15MFXtwz/ValidationStatus/evnnNLv",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 627-3925 - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/15MFYB01",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/AreaCode/evnnziF",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/CountryCode/evnnmvT",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/DigitCount/evnoGlH",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/FormatMask/evnnrBj",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/FormattedNumber/evnoPHn",
              "value": "(215) 627-3925"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/GeoArea/evnoCV1",
              "value": "Philadelphia, PA"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/GeoCountry/evno8El",
              "value": "United States"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/LineType/evnnvRz",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/LocalNumber/evnoL1X",
              "value": "6273925"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/NestedEntityId/15MFYNmn",
              "value": "HCP-973664|CITELINE|215-627-3925"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/Number/15MFYJWX",
              "value": "215-627-3925"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/Type/15MFYFGH",
              "value": "CITELINE"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYB01/ValidationStatus/evno3yV",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 823-8222 - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/15MFYS33",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/AreaCode/evnogKp",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/CountryCode/evnoTY3",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/DigitCount/evnoxNr",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/FormatMask/evnoXoJ",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/FormattedNumber/evnp5uN",
              "value": "(215) 823-8222"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/GeoArea/evnot7b",
              "value": "Philadelphia, PA"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/GeoCountry/evnoorL",
              "value": "United States"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/LineType/evnoc4Z",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/LocalNumber/evnp1e7",
              "value": "8238222"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/NestedEntityId/15MFYepp",
              "value": "HCP-973664|CITELINE|215-823-8222"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/Number/15MFYaZZ",
              "value": "215-823-8222"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/Type/15MFYWJJ",
              "value": "CITELINE"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYS33/ValidationStatus/evnokb5",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 955-8732 - CITELINE - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/15MFYj65",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/AreaCode/evnpMxP",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/CountryCode/evnpAAd",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/DigitCount/evnpe0R",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/FormatMask/evnpEQt",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/FormattedNumber/evnpmWx",
              "value": "(215) 955-8732"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/GeoArea/evnpZkB",
              "value": "Philadelphia, PA"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/GeoCountry/evnpVTv",
              "value": "United States"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/LineType/evnpIh9",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/LocalNumber/evnpiGh",
              "value": "9558732"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/NestedEntityId/15MFYvsr",
              "value": "HCP-973664|CITELINE|215-955-8732"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/Number/15MFYrcb",
              "value": "215-955-8732"
            }
          ],
          "Type": [
            {
              "lookupCode": "CITELINE",
              "lookupRawValue": "CITELINE",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/Type/15MFYnML",
              "value": "CITELINE"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/15MFYj65/ValidationStatus/evnpRDf",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 600-9020 - Work_Phone - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/evncaBP",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/AreaCode/evnq3Zz",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/CountryCode/evnpqnD",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/DigitCount/evnqKd1",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/FormatMask/evnpv3T",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/FormattedNumber/evnqT9X",
              "value": "(215) 600-9020"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/GeoArea/evnqGMl",
              "value": "Pennsylvania"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/GeoCountry/evnqC6V",
              "value": "United States"
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/IsDeleted/evnceRf",
              "value": "False"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/LineType/evnpzJj",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/LocalNumber/evnqOtH",
              "value": "6009020"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/NestedEntityId/evncihv",
              "value": "1-4TMZR8M|1-4TMZR8M|Work_Phone|2156009020"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/Number/evncrER",
              "value": "2156009020"
            }
          ],
          "Type": [
            {
              "lookupCode": "Work_Phone",
              "lookupRawValue": "Work_Phone",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/Type/evncmyB",
              "value": "Work_Phone"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/evncaBP/ValidationStatus/evnq7qF",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 498-1015 - Alt_Phone - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/evncvUh",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/AreaCode/evnqkCZ",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/CountryCode/evnqXPn",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/DigitCount/evnr1Fb",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/FormatMask/evnqbg3",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/FormattedNumber/evnr9m7",
              "value": "(215) 498-1015"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/GeoArea/evnqwzL",
              "value": "Pennsylvania"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/GeoCountry/evnqsj5",
              "value": "United States"
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/IsDeleted/evnczkx",
              "value": "False"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/LineType/evnqfwJ",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/LocalNumber/evnr5Vr",
              "value": "4981015"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/NestedEntityId/evnd41D",
              "value": "1-4TMZR8M|1-4TMZR8M|Alt_Phone|2154981015"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/Number/evndCXj",
              "value": "2154981015"
            }
          ],
          "Type": [
            {
              "lookupCode": "Alt_Phone",
              "lookupRawValue": "Alt_Phone",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/Type/evnd8HT",
              "value": "Alt_Phone"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/evncvUh/ValidationStatus/evnqoSp",
              "value": "VALID"
            }
          ]
        }
      },
      {
        "label": "(215) 600-9020 - Other_Phone - VALID",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Phone/evndGnz",
        "value": {
          "AreaCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/AreaCode",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/AreaCode/evnrQp9",
              "value": "215"
            }
          ],
          "CountryCode": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/CountryCode",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/CountryCode/evnrE2N",
              "value": "US"
            }
          ],
          "DigitCount": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/DigitCount",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/DigitCount/evnrhsB",
              "value": "10"
            }
          ],
          "FormatMask": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormatMask",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/FormatMask/evnrIId",
              "value": "(nnn) nnn-nnnn"
            }
          ],
          "FormattedNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/FormattedNumber",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/FormattedNumber/evnrqOh",
              "value": "(215) 600-9020"
            }
          ],
          "GeoArea": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoArea",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/GeoArea/evnrdbv",
              "value": "Pennsylvania"
            }
          ],
          "GeoCountry": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/GeoCountry",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/GeoCountry/evnrZLf",
              "value": "United States"
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/IsDeleted/evndL4F",
              "value": "False"
            }
          ],
          "LineType": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LineType",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/LineType/evnrMYt",
              "value": "FIXED_LINE_OR_MOBILE"
            }
          ],
          "LocalNumber": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/LocalNumber",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/LocalNumber/evnrm8R",
              "value": "6009020"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/NestedEntityId/evndPKV",
              "value": "1-4TMZR8M|1-4TMZR8M|Other_Phone|(215) 600-9020"
            }
          ],
          "Number": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Number",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/Number/evndXr1",
              "value": "(215) 600-9020"
            }
          ],
          "Type": [
            {
              "lookupCode": "Other_Phone",
              "lookupRawValue": "Other_Phone",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/Type",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/Type/evndTal",
              "value": "Other_Phone"
            }
          ],
          "ValidationStatus": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Phone/attributes/ValidationStatus",
              "uri": "entities/0OfT51J/attributes/Phone/evndGnz/ValidationStatus/evnrV5P",
              "value": "VALID"
            }
          ]
        }
      }
    ],
    "Prefix": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/Prefix",
        "uri": "entities/0OfT51J/attributes/Prefix/evnbtYp",
        "value": "Dr"
      }
    ],
    "SourceCreatedDate": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/SourceCreatedDate",
        "uri": "entities/0OfT51J/attributes/SourceCreatedDate/evnjWfT",
        "value": "2010-10-05T12:00:00.000+0000"
      },
      {
        "ov": False,
        "type": "configuration/entityTypes/HCP/attributes/SourceCreatedDate",
        "uri": "entities/0OfT51J/attributes/SourceCreatedDate/evncVv9",
        "value": "2019-11-06T00:26:15.000+0000"
      }
    ],
    "SourceLastUpdateDate": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/SourceLastUpdateDate",
        "uri": "entities/0OfT51J/attributes/SourceLastUpdateDate/evnjryl",
        "value": "2019-05-07T16:52:39.000+0000"
      },
      {
        "ov": False,
        "type": "configuration/entityTypes/HCP/attributes/SourceLastUpdateDate",
        "uri": "entities/0OfT51J/attributes/SourceLastUpdateDate/evneN07",
        "value": "2023-06-22T18:19:36.000+0000"
      }
    ],
    "Speaker": [
      {
        "label": "(speaker - False)",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Speaker/evneRGN",
        "value": {
          "IsSpeaker": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Speaker/attributes/IsSpeaker",
              "uri": "entities/0OfT51J/attributes/Speaker/evneRGN/IsSpeaker/evnee39",
              "value": "False"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Speaker/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Speaker/evneRGN/NestedEntityId/evneVWd",
              "value": "1-4TMZR8M|N"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Speaker/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Speaker/evneRGN/SourceCreatedDate/evneZmt",
              "value": "2019-11-06T00:26:15.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Speaker/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Speaker/evneRGN/SourceLastUpdateDate/evneiJP",
              "value": "2023-06-22T18:19:36.000+0000"
            }
          ]
        }
      }
    ],
    "Specialties": [
      {
        "label": "Onekey Specialty - General Surgery",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Specialties/evni0tn",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Specialties/evni0tn/NestedEntityId/evni9QJ",
              "value": "WUSM00617052|General Surgery"
            }
          ],
          "Specialty": [
            {
              "lookupCode": "General Surgery",
              "lookupRawValue": "General Surgery",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/Specialty",
              "uri": "entities/0OfT51J/attributes/Specialties/evni0tn/Specialty/evni5A3",
              "value": "General Surgery"
            }
          ],
          "SpecialtyType": [
            {
              "lookupCode": "Onekey Specialty",
              "lookupRawValue": "Onekey Specialty",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/SpecialtyType",
              "uri": "entities/0OfT51J/attributes/Specialties/evni0tn/SpecialtyType/evniDgZ",
              "value": "Onekey Specialty"
            }
          ]
        }
      },
      {
        "label": "Onekey Specialty - Surgical Oncology",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Specialties/evniHwp",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Specialties/evniHwp/NestedEntityId/evniQTL",
              "value": "WUSM00617052|Surgical Oncology"
            }
          ],
          "Specialty": [
            {
              "lookupCode": "Surgical Oncology",
              "lookupRawValue": "Surgical Oncology",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/Specialty",
              "uri": "entities/0OfT51J/attributes/Specialties/evniHwp/Specialty/evniMD5",
              "value": "Surgical Oncology"
            }
          ],
          "SpecialtyType": [
            {
              "lookupCode": "Onekey Specialty",
              "lookupRawValue": "Onekey Specialty",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/SpecialtyType",
              "uri": "entities/0OfT51J/attributes/Specialties/evniHwp/SpecialtyType/evniUjb",
              "value": "Onekey Specialty"
            }
          ]
        }
      },
      {
        "label": "Surgery - Surgery",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj",
        "value": {
          "BoardCertified": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/BoardCertified",
              "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj/BoardCertified/evnZHb1",
              "value": "False"
            }
          ],
          "IsDeleted": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/IsDeleted",
              "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj/IsDeleted/evnZ4oF",
              "value": "False"
            }
          ],
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj/NestedEntityId/evnZ94V",
              "value": "1-4TMZR8M|1182759142198002807"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj/SourceCreatedDate/evnZLrH",
              "value": "2022-07-15T17:30:45.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj/SourceLastUpdateDate/evnZQ7X",
              "value": "2022-07-15T17:31:14.000+0000"
            }
          ],
          "Specialty": [
            {
              "lookupCode": "Surgery",
              "lookupRawValue": "Surgery",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/Specialty",
              "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj/Specialty/evnZ0Xz",
              "value": "Surgery"
            }
          ],
          "SpecialtyType": [
            {
              "lookupCode": "Surgery",
              "lookupRawValue": "Surgery",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/SpecialtyType",
              "uri": "entities/0OfT51J/attributes/Specialties/evnYwHj/SpecialtyType/evnZDKl",
              "value": "Surgery"
            }
          ]
        }
      },
      {
        "label": "Citeline Speciality - Surgery - Oncology",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/Specialties/15MFZpID",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/Specialties/15MFZpID/NestedEntityId/15MFa24z",
              "value": "HCP-973664|Surgery - Oncology"
            }
          ],
          "Specialty": [
            {
              "lookupCode": "Surgery - Oncology",
              "lookupRawValue": "Surgery - Oncology",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/Specialty",
              "uri": "entities/0OfT51J/attributes/Specialties/15MFZpID/Specialty/15MFZxoj",
              "value": "Surgery - Oncology"
            }
          ],
          "SpecialtyType": [
            {
              "lookupCode": "Citeline Speciality",
              "lookupRawValue": "Citeline Speciality",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/Specialties/attributes/SpecialtyType",
              "uri": "entities/0OfT51J/attributes/Specialties/15MFZpID/SpecialtyType/15MFZtYT",
              "value": "Citeline Speciality"
            }
          ]
        }
      }
    ],
    "StatusInformation": [
      {
        "label": "Valid",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/StatusInformation/evniYzr",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StatusInformation/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/StatusInformation/evniYzr/NestedEntityId/evnihWN",
              "value": "WUSM00617052|Valid"
            }
          ],
          "Status": [
            {
              "lookupCode": "Valid",
              "lookupRawValue": "Valid",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StatusInformation/attributes/Status",
              "uri": "entities/0OfT51J/attributes/StatusInformation/evniYzr/Status/evnidG7",
              "value": "Valid"
            }
          ]
        }
      },
      {
        "label": "Active",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/StatusInformation/evnZUNn",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StatusInformation/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/StatusInformation/evnZUNn/NestedEntityId/evnZcuJ",
              "value": "1-4TMZR8M|Active"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StatusInformation/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/StatusInformation/evnZUNn/SourceCreatedDate/evnZhAZ",
              "value": "2019-11-06T00:26:15.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StatusInformation/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/StatusInformation/evnZUNn/SourceLastUpdateDate/evnZlQp",
              "value": "2023-06-22T18:19:36.000+0000"
            }
          ],
          "Status": [
            {
              "lookupCode": "Active",
              "lookupRawValue": "Active",
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StatusInformation/attributes/Status",
              "uri": "entities/0OfT51J/attributes/StatusInformation/evnZUNn/Status/evnZYe3",
              "value": "Active"
            }
          ]
        }
      }
    ],
    "StudyRoles": [
      {
        "label": "Sub-Investigator",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/StudyRoles/evnZph5",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnZph5/NestedEntityId/evnZtxL",
              "value": "1-4TMZR8M|4786479320843971299|Sub-Investigator|2019-07-23 00:00:00.000"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnZph5/SourceCreatedDate/evnZyDb",
              "value": "2019-11-06T00:34:40.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnZph5/SourceLastUpdateDate/evna6k7",
              "value": "2019-11-06T00:34:40.000+0000"
            }
          ],
          "StudyRole": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/StudyRole",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnZph5/StudyRole/evna2Tr",
              "value": "Sub-Investigator"
            }
          ]
        }
      },
      {
        "label": "Sub-Investigator",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/StudyRoles/evnaB0N",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaB0N/NestedEntityId/evnaFGd",
              "value": "1-4TMZR8M|8686518979564612673|Sub-Investigator|2019-07-24 00:00:00.000"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaB0N/SourceCreatedDate/evnaJWt",
              "value": "2020-01-31T23:17:34.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaB0N/SourceLastUpdateDate/evnaS3P",
              "value": "2020-01-31T23:17:34.000+0000"
            }
          ],
          "StudyRole": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/StudyRole",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaB0N/StudyRole/evnaNn9",
              "value": "Sub-Investigator"
            }
          ]
        }
      },
      {
        "label": "Sub-Investigator",
        "ov": True,
        "uri": "entities/0OfT51J/attributes/StudyRoles/evnaWJf",
        "value": {
          "NestedEntityId": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/NestedEntityId",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaWJf/NestedEntityId/evnaaZv",
              "value": "1-4TMZR8M|3798311571670601180|Sub-Investigator|2022-07-12 00:00:00.000"
            }
          ],
          "SourceCreatedDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/SourceCreatedDate",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaWJf/SourceCreatedDate/evnaeqB",
              "value": "2022-07-12T19:25:40.000+0000"
            }
          ],
          "SourceLastUpdateDate": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/SourceLastUpdateDate",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaWJf/SourceLastUpdateDate/evnanMh",
              "value": "2022-07-12T19:25:40.000+0000"
            }
          ],
          "StudyRole": [
            {
              "ov": True,
              "type": "configuration/entityTypes/HCP/attributes/StudyRoles/attributes/StudyRole",
              "uri": "entities/0OfT51J/attributes/StudyRoles/evnaWJf/StudyRole/evnaj6R",
              "value": "Sub-Investigator"
            }
          ]
        }
      }
    ],
    "Title": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/Title",
        "uri": "entities/0OfT51J/attributes/Title/evnjFcR",
        "value": "DR"
      },
      {
        "ov": False,
        "type": "configuration/entityTypes/HCP/attributes/Title",
        "uri": "entities/0OfT51J/attributes/Title/evnbpIZ",
        "value": "Dr"
      }
    ],
    "YoB": [
      {
        "ov": True,
        "type": "configuration/entityTypes/HCP/attributes/YoB",
        "uri": "entities/0OfT51J/attributes/YoB/evnjO8x",
        "value": "1971"
      }
    ]
  },
  "createdBy": "NA03-SVT-20250129",
  "createdTime": 1741347447182,
  "crosswalks": [
    {
      "attributes": [
        "entities/0OfT51J/attributes/StudyRoles/evnaB0N/SourceLastUpdateDate/evnaS3P",
        "entities/0OfT51J/attributes/License/evnarcx/State/evnbCwF",
        "entities/0OfT51J/attributes/Identifiers/evndc7H/Type/evndgNX",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/ID/evneETb",
        "entities/0OfT51J/attributes/Education/evnc6Lb/IsDeleted/evncAbr",
        "entities/0OfT51J/attributes/StatusInformation/evnZUNn/SourceLastUpdateDate/evnZlQp",
        "entities/0OfT51J/attributes/Prefix/evnbtYp",
        "entities/0OfT51J/attributes/Education/evnc6Lb",
        "entities/0OfT51J/attributes/StatusInformation/evnZUNn/SourceCreatedDate/evnZhAZ",
        "entities/0OfT51J/attributes/Phone/evncvUh/NestedEntityId/evnd41D",
        "entities/0OfT51J/attributes/Speaker/evneRGN/IsSpeaker/evnee39",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/SourceCreatedDate/evneADL",
        "entities/0OfT51J/attributes/License/evnbLSl/SourceLastUpdateDate/evnbl2J",
        "entities/0OfT51J/attributes/MiddleName/evnbxp5",
        "entities/0OfT51J/attributes/Phone/evndGnz/Type/evndTal",
        "entities/0OfT51J/attributes/Education/evnc6Lb/Degree/evncJ8N",
        "entities/0OfT51J/attributes/License/evnarcx/SourceLastUpdateDate/evnbHCV",
        "entities/0OfT51J/attributes/SourceCreatedDate/evncVv9",
        "entities/0OfT51J/attributes/StudyRoles/evnaWJf/SourceCreatedDate/evnaeqB",
        "entities/0OfT51J/attributes/Phone/evndGnz",
        "entities/0OfT51J/attributes/StatusInformation/evnZUNn/Status/evnZYe3",
        "entities/0OfT51J/attributes/StudyRoles/evnaWJf",
        "entities/0OfT51J/attributes/License/evnbLSl/State/evnbgm3",
        "entities/0OfT51J/attributes/Speaker/evneRGN/SourceLastUpdateDate/evneiJP",
        "entities/0OfT51J/attributes/License/evnarcx/SourceCreatedDate/evnb8fz",
        "entities/0OfT51J/attributes/Phone/evncvUh",
        "entities/0OfT51J/attributes/Education/evnc6Lb/NestedEntityId/evncEs7",
        "entities/0OfT51J/attributes/License/evnarcx",
        "entities/0OfT51J/attributes/Education/evnc6Lb/SourceCreatedDate/evncNOd",
        "entities/0OfT51J/attributes/Title/evnbpIZ",
        "entities/0OfT51J/attributes/StatusInformation/evnZUNn/NestedEntityId/evnZcuJ",
        "entities/0OfT51J/attributes/IsDeleted/evnYs1T",
        "entities/0OfT51J/attributes/StudyRoles/evnaWJf/NestedEntityId/evnaaZv",
        "entities/0OfT51J/attributes/Specialties/evnYwHj/NestedEntityId/evnZ94V",
        "entities/0OfT51J/attributes/Speaker/evneRGN/SourceCreatedDate/evneZmt",
        "entities/0OfT51J/attributes/Phone/evndGnz/IsDeleted/evndL4F",
        "entities/0OfT51J/attributes/Phone/evncaBP/NestedEntityId/evncihv",
        "entities/0OfT51J/attributes/Specialties/evnYwHj/SourceLastUpdateDate/evnZQ7X",
        "entities/0OfT51J/attributes/Phone/evndGnz/Number/evndXr1",
        "entities/0OfT51J/attributes/Identifiers/evndc7H/NestedEntityId/evndkdn",
        "entities/0OfT51J/attributes/StudyRoles/evnZph5/StudyRole/evna2Tr",
        "entities/0OfT51J/attributes/SourceLastUpdateDate/evneN07",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/SourceLastUpdateDate/evneIjr",
        "entities/0OfT51J/attributes/Specialties/evnYwHj/IsDeleted/evnZ4oF",
        "entities/0OfT51J/attributes/FirstName/15MFVuLV",
        "entities/0OfT51J/attributes/License/evnarcx/NestedEntityId/evnb09T",
        "entities/0OfT51J/attributes/License/evnbLSl/Number/evnbYFX",
        "entities/0OfT51J/attributes/Specialties/evnYwHj/SourceCreatedDate/evnZLrH",
        "entities/0OfT51J/attributes/License/evnarcx/IsDeleted/evnavtD",
        "entities/0OfT51J/attributes/StudyRoles/evnaB0N/SourceCreatedDate/evnaJWt",
        "entities/0OfT51J/attributes/StudyRoles/evnaWJf/StudyRole/evnaj6R",
        "entities/0OfT51J/attributes/Phone/evncvUh/Type/evnd8HT",
        "entities/0OfT51J/attributes/StudyRoles/evnaB0N",
        "entities/0OfT51J/attributes/StatusInformation/evnZUNn",
        "entities/0OfT51J/attributes/StudyRoles/evnZph5/SourceLastUpdateDate/evna6k7",
        "entities/0OfT51J/attributes/Specialties/evnYwHj",
        "entities/0OfT51J/attributes/Phone/evncaBP/Number/evncrER",
        "entities/0OfT51J/attributes/Phone/evndGnz/NestedEntityId/evndPKV",
        "entities/0OfT51J/attributes/StudyRoles/evnaB0N/StudyRole/evnaNn9",
        "entities/0OfT51J/attributes/License/evnbLSl/SourceCreatedDate/evnbcVn",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/Type/evne1gp",
        "entities/0OfT51J/attributes/Phone/evncaBP/Type/evncmyB",
        "entities/0OfT51J/attributes/Specialties/evnYwHj/SpecialtyType/evnZDKl",
        "entities/0OfT51J/attributes/StudyRoles/evnZph5/NestedEntityId/evnZtxL",
        "entities/0OfT51J/attributes/Phone/evncvUh/Number/evndCXj",
        "entities/0OfT51J/attributes/Identifiers/evndc7H",
        "entities/0OfT51J/attributes/Phone/evncaBP",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/NestedEntityId/evne5x5",
        "entities/0OfT51J/attributes/License/evnarcx/Number/evnb4Pj",
        "entities/0OfT51J/attributes/Identifiers/evndc7H/SourceCreatedDate/evndou3",
        "entities/0OfT51J/attributes/StudyRoles/evnaWJf/SourceLastUpdateDate/evnanMh",
        "entities/0OfT51J/attributes/StudyRoles/evnZph5",
        "entities/0OfT51J/attributes/License/evnbLSl",
        "entities/0OfT51J/attributes/EntityUUID/evnc25L",
        "entities/0OfT51J/attributes/Phone/evncvUh/IsDeleted/evnczkx",
        "entities/0OfT51J/attributes/License/evnbLSl/NestedEntityId/evnbTzH",
        "entities/0OfT51J/attributes/StudyRoles/evnZph5/SourceCreatedDate/evnZyDb",
        "entities/0OfT51J/attributes/Specialties/evnYwHj/BoardCertified/evnZHb1",
        "entities/0OfT51J/attributes/StudyRoles/evnaB0N/NestedEntityId/evnaFGd",
        "entities/0OfT51J/attributes/Identifiers/evndc7H/SourceLastUpdateDate/evndxQZ",
        "entities/0OfT51J/attributes/Speaker/evneRGN/NestedEntityId/evneVWd",
        "entities/0OfT51J/attributes/Education/evnc6Lb/SourceLastUpdateDate/evncRet",
        "entities/0OfT51J/attributes/Identifiers/evndc7H/ID/evndtAJ",
        "entities/0OfT51J/attributes/LastName/15MFW2s1",
        "entities/0OfT51J/attributes/Specialties/evnYwHj/Specialty/evnZ0Xz",
        "entities/0OfT51J/attributes/Phone/evncaBP/IsDeleted/evnceRf",
        "entities/0OfT51J/attributes/License/evnbLSl/IsDeleted/evnbPj1",
        "entities/0OfT51J/attributes/Speaker/evneRGN"
      ],
      "createDate": "2025-03-07T12:41:53.787Z",
      "reltioLoadDate": "2025-03-07T12:41:53.787Z",
      "singleAttributeUpdateDates": {},
      "type": "configuration/sources/CTMS",
      "updateDate": "2025-03-07T12:41:53.787Z",
      "uri": "entities/0OfT51J/crosswalks/1jpzJEY6",
      "value": "1-4TMZR8M"
    },
    {
      "attributes": [
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB/NestedEntityId/evnjjSF",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/ID/evneETb",
        "entities/0OfT51J/attributes/Specialties/evniHwp",
        "entities/0OfT51J/attributes/SourceCreatedDate/evnjWfT",
        "entities/0OfT51J/attributes/License/evnilmd/NestedEntityId/evniuJ9",
        "entities/0OfT51J/attributes/SourceLastUpdateDate/evnjryl",
        "entities/0OfT51J/attributes/Specialties/evni0tn/NestedEntityId/evni9QJ",
        "entities/0OfT51J/attributes/EntityUUID/evnjSPD",
        "entities/0OfT51J/attributes/FirstName/15MFVuLV",
        "entities/0OfT51J/attributes/Specialties/evni0tn",
        "entities/0OfT51J/attributes/Specialties/evniHwp/SpecialtyType/evniUjb",
        "entities/0OfT51J/attributes/StatusInformation/evniYzr",
        "entities/0OfT51J/attributes/MiddleName/evnbxp5",
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB",
        "entities/0OfT51J/attributes/Specialties/evni0tn/SpecialtyType/evniDgZ",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/Type/evne1gp",
        "entities/0OfT51J/attributes/Gender/evnjJsh",
        "entities/0OfT51J/attributes/Specialties/evniHwp/Specialty/evniMD5",
        "entities/0OfT51J/attributes/StatusInformation/evniYzr/NestedEntityId/evnihWN",
        "entities/0OfT51J/attributes/License/evnilmd",
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB/ID/15MFZglh",
        "entities/0OfT51J/attributes/Identifiers/1jpzF6oc/NestedEntityId/evnhSnj",
        "entities/0OfT51J/attributes/License/evnilmd/Number/evnj2pf",
        "entities/0OfT51J/attributes/Specialties/evniHwp/NestedEntityId/evniQTL",
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB/Type/15MFZcVR",
        "entities/0OfT51J/attributes/YoB/evnjO8x",
        "entities/0OfT51J/attributes/License/evnilmd/Type/evniyZP",
        "entities/0OfT51J/attributes/Specialties/evni0tn/Specialty/evni5A3",
        "entities/0OfT51J/attributes/License/evnilmd/Status/evniq2t",
        "entities/0OfT51J/attributes/StatusInformation/evniYzr/Status/evnidG7",
        "entities/0OfT51J/attributes/Title/evnjFcR",
        "entities/0OfT51J/attributes/License/evnilmd/State/evnjBMB",
        "entities/0OfT51J/attributes/License/evnilmd/ExpirationDate/evnj75v",
        "entities/0OfT51J/attributes/LastName/15MFW2s1"
      ],
      "createDate": "2025-03-07T16:00:16.965Z",
      "reltioLoadDate": "2025-03-07T16:00:16.965Z",
      "singleAttributeUpdateDates": {},
      "type": "configuration/sources/ONEKEY",
      "updateDate": "2025-03-07T16:00:16.965Z",
      "uri": "entities/0OfT51J/crosswalks/1owhwIsM",
      "value": "WUSM00617052"
    },
    {
      "attributes": [
        "entities/0OfT51J/attributes/MiddleName/evnbxp5",
        "entities/0OfT51J/attributes/FirstName/15MFVuLV",
        "entities/0OfT51J/attributes/LastName/15MFW2s1"
      ],
      "createDate": "2025-03-11T00:00:48.090Z",
      "reltioLoadDate": "2025-03-10T23:59:10.316Z",
      "singleAttributeUpdateDates": {},
      "type": "configuration/sources/ReltioStringFunctionCleanser",
      "updateDate": "2025-03-11T00:00:48.090Z",
      "uri": "entities/0OfT51J/crosswalks/evnjwF1",
      "value": "0OfT51J"
    },
    {
      "attributes": [
        "entities/0OfT51J/attributes/Name/nq0CpBQ"
      ],
      "createDate": "2025-03-11T00:00:48.091Z",
      "reltioLoadDate": "2025-03-10T23:59:10.316Z",
      "singleAttributeUpdateDates": {},
      "type": "configuration/sources/ReltioFullNameBuilder",
      "updateDate": "2025-03-11T00:00:48.091Z",
      "uri": "entities/0OfT51J/crosswalks/evnkcrb",
      "value": "0OfT51J"
    },
    {
      "attributes": [
        "entities/0OfT51J/attributes/Phone/15MFYB01/DigitCount/evnoGlH",
        "entities/0OfT51J/attributes/Phone/15MFXctx/LineType/evnmYCp",
        "entities/0OfT51J/attributes/Phone/evncvUh/DigitCount/evnr1Fb",
        "entities/0OfT51J/attributes/Phone/evncvUh/ValidationStatus/evnqoSp",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/LocalNumber/evnlaXD",
        "entities/0OfT51J/attributes/Phone/evncvUh/LocalNumber/evnr5Vr",
        "entities/0OfT51J/attributes/Phone/15MFXtwz",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/LineType/evnlAxf",
        "entities/0OfT51J/attributes/Phone/15MFYj65/ValidationStatus/evnpRDf",
        "entities/0OfT51J/attributes/Phone/15MFYj65/GeoCountry/evnpVTv",
        "entities/0OfT51J/attributes/Phone/evncaBP/FormatMask/evnpv3T",
        "entities/0OfT51J/attributes/Phone/evndGnz/GeoArea/evnrdbv",
        "entities/0OfT51J/attributes/Phone/15MFYS33",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/LineType/evnlraF",
        "entities/0OfT51J/attributes/Phone/evncvUh/AreaCode/evnqkCZ",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/LocalNumber/evnmH9n",
        "entities/0OfT51J/attributes/Email/15MFZ097/Domain/nq1Wq1I",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/GeoArea/evnm8dH",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/AreaCode/evnlvqV",
        "entities/0OfT51J/attributes/Phone/15MFXctx",
        "entities/0OfT51J/attributes/Phone/15MFXctx/FormattedNumber/evnn22d",
        "entities/0OfT51J/attributes/Phone/15MFYS33/LocalNumber/evnp1e7",
        "entities/0OfT51J/attributes/Phone/15MFYS33/GeoCountry/evnoorL",
        "entities/0OfT51J/attributes/Phone/15MFYS33/FormattedNumber/evnp5uN",
        "entities/0OfT51J/attributes/Phone/15MFYB01",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/LocalNumber/evnneOx",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/GeoCountry/evnnRcB",
        "entities/0OfT51J/attributes/Phone/evncaBP/LineType/evnpzJj",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/GeoArea/evnnVsR",
        "entities/0OfT51J/attributes/Phone/15MFYS33/Type/15MFYWJJ",
        "entities/0OfT51J/attributes/Phone/evndGnz/DigitCount/evnrhsB",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/CountryCode/evnl2R9",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/FormatMask/evnnAZ9",
        "entities/0OfT51J/attributes/Phone/15MFYS33/ValidationStatus/evnokb5",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/CountryCode/evnn6It",
        "entities/0OfT51J/attributes/Phone/15MFYj65/CountryCode/evnpAAd",
        "entities/0OfT51J/attributes/Phone/15MFYj65/FormatMask/evnpEQt",
        "entities/0OfT51J/attributes/Phone/15MFYj65/DigitCount/evnpe0R",
        "entities/0OfT51J/attributes/Phone/evndGnz/ValidationStatus/evnrV5P",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/FormattedNumber/evnlenT",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/GeoArea/evnlS0h",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/Type/15MFX949",
        "entities/0OfT51J/attributes/Email/15MFZ097/Username/nq1X2o4",
        "entities/0OfT51J/attributes/Phone/15MFYB01/LocalNumber/evnoL1X",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/Number/15MFY2TV",
        "entities/0OfT51J/attributes/Phone/15MFYB01/AreaCode/evnnziF",
        "entities/0OfT51J/attributes/Phone/evncaBP/DigitCount/evnqKd1",
        "entities/0OfT51J/attributes/Phone/15MFXctx/Number/15MFXlQT",
        "entities/0OfT51J/attributes/Phone/15MFXctx/Type/15MFXhAD",
        "entities/0OfT51J/attributes/Phone/evncaBP/LocalNumber/evnqOtH",
        "entities/0OfT51J/attributes/Phone/evncaBP/Type/evncmyB",
        "entities/0OfT51J/attributes/Phone/15MFXctx/GeoArea/evnmpFr",
        "entities/0OfT51J/attributes/Phone/evncvUh/GeoArea/evnqwzL",
        "entities/0OfT51J/attributes/Phone/evncvUh/Number/evndCXj",
        "entities/0OfT51J/attributes/Phone/15MFYj65/LocalNumber/evnpiGh",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/LineType/evnnEpP",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/DigitCount/evnlWGx",
        "entities/0OfT51J/attributes/Phone/15MFYj65/FormattedNumber/evnpmWx",
        "entities/0OfT51J/attributes/Phone/evndGnz/GeoCountry/evnrZLf",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/FormattedNumber/evnmLQ3",
        "entities/0OfT51J/attributes/Phone/evncaBP/AreaCode/evnq3Zz",
        "entities/0OfT51J/attributes/Phone/15MFXctx/DigitCount/evnmtW7",
        "entities/0OfT51J/attributes/Phone/15MFYB01/FormattedNumber/evnoPHn",
        "entities/0OfT51J/attributes/Phone/evndGnz/CountryCode/evnrE2N",
        "entities/0OfT51J/attributes/Phone/15MFXLqv",
        "entities/0OfT51J/attributes/Phone/evncvUh/FormattedNumber/evnr9m7",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/FormatMask/evnl6hP",
        "entities/0OfT51J/attributes/Phone/15MFYS33/GeoArea/evnot7b",
        "entities/0OfT51J/attributes/Phone/evncvUh/GeoCountry/evnqsj5",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/CountryCode/evnlj3j",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/FormattedNumber/evnnifD",
        "entities/0OfT51J/attributes/Phone/evndGnz/LocalNumber/evnrm8R",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/ValidationStatus/evnm06l",
        "entities/0OfT51J/attributes/Phone/evndGnz/LineType/evnrMYt",
        "entities/0OfT51J/attributes/Phone/15MFYB01/CountryCode/evnnmvT",
        "entities/0OfT51J/attributes/Phone/15MFYS33/Number/15MFYaZZ",
        "entities/0OfT51J/attributes/Phone/15MFYB01/ValidationStatus/evno3yV",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/Type/15MFXyDF",
        "entities/0OfT51J/attributes/Phone/15MFYj65/GeoArea/evnpZkB",
        "entities/0OfT51J/attributes/Phone/15MFXctx/CountryCode/evnmPgJ",
        "entities/0OfT51J/attributes/Phone/evncvUh/LineType/evnqfwJ",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/Number/15MFXUNR",
        "entities/0OfT51J/attributes/Phone/15MFXctx/FormatMask/evnmTwZ",
        "entities/0OfT51J/attributes/Phone/evndGnz/Type/evndTal",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/AreaCode/evnlFDv",
        "entities/0OfT51J/attributes/Phone/15MFYS33/DigitCount/evnoxNr",
        "entities/0OfT51J/attributes/Phone/evndGnz/FormatMask/evnrIId",
        "entities/0OfT51J/attributes/Phone/evndGnz",
        "entities/0OfT51J/attributes/Phone/15MFYj65/AreaCode/evnpMxP",
        "entities/0OfT51J/attributes/Phone/evndGnz/FormattedNumber/evnrqOh",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/Number/15MFXDKP",
        "entities/0OfT51J/attributes/Phone/15MFYS33/LineType/evnoc4Z",
        "entities/0OfT51J/attributes/Phone/15MFXctx/AreaCode/evnmcT5",
        "entities/0OfT51J/attributes/Phone/evncaBP/FormattedNumber/evnqT9X",
        "entities/0OfT51J/attributes/Phone/evncvUh",
        "entities/0OfT51J/attributes/Phone/evncvUh/FormatMask/evnqbg3",
        "entities/0OfT51J/attributes/Phone/15MFYS33/CountryCode/evnoTY3",
        "entities/0OfT51J/attributes/Phone/15MFYj65/LineType/evnpIh9",
        "entities/0OfT51J/attributes/Phone/evncvUh/CountryCode/evnqXPn",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/AreaCode/evnnJ5f",
        "entities/0OfT51J/attributes/Phone/15MFYj65/Number/15MFYrcb",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/ValidationStatus/evnlJUB",
        "entities/0OfT51J/attributes/Phone/15MFXctx/LocalNumber/evnmxmN",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/FormatMask/evnlnJz",
        "entities/0OfT51J/attributes/Phone/evndGnz/Number/evndXr1",
        "entities/0OfT51J/attributes/Phone/15MFYj65",
        "entities/0OfT51J/attributes/Email/15MFZ097/DomainType/nq1WuHY",
        "entities/0OfT51J/attributes/Phone/15MFYB01/Number/15MFYJWX",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/DigitCount/evnmCtX",
        "entities/0OfT51J/attributes/Phone/15MFYB01/Type/15MFYFGH",
        "entities/0OfT51J/attributes/Phone/evncaBP/CountryCode/evnpqnD",
        "entities/0OfT51J/attributes/Phone/15MFYS33/AreaCode/evnogKp",
        "entities/0OfT51J/attributes/Phone/evncaBP/ValidationStatus/evnq7qF",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/Type/15MFXQ7B",
        "entities/0OfT51J/attributes/Phone/evncvUh/Type/evnd8HT",
        "entities/0OfT51J/attributes/Phone/15MFXctx/GeoCountry/evnmkzb",
        "entities/0OfT51J/attributes/Phone/15MFYS33/FormatMask/evnoXoJ",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/ValidationStatus/evnnNLv",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/GeoCountry/evnm4N1",
        "entities/0OfT51J/attributes/Phone/evncaBP/Number/evncrER",
        "entities/0OfT51J/attributes/Phone/evncaBP/GeoCountry/evnqC6V",
        "entities/0OfT51J/attributes/Email/15MFZ097",
        "entities/0OfT51J/attributes/Phone/15MFYB01/GeoArea/evnoCV1",
        "entities/0OfT51J/attributes/Phone/evncaBP/GeoArea/evnqGMl",
        "entities/0OfT51J/attributes/Phone/evncaBP",
        "entities/0OfT51J/attributes/Email/15MFZ097/Email/evnruex",
        "entities/0OfT51J/attributes/Phone/15MFXctx/ValidationStatus/evnmgjL",
        "entities/0OfT51J/attributes/Phone/evndGnz/AreaCode/evnrQp9",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/DigitCount/evnna8h",
        "entities/0OfT51J/attributes/Phone/15MFX4nt",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/GeoCountry/evnlNkR",
        "entities/0OfT51J/attributes/Phone/15MFYB01/FormatMask/evnnrBj",
        "entities/0OfT51J/attributes/Email/15MFZ097/ValidationStatus/nq1WyXo",
        "entities/0OfT51J/attributes/Phone/15MFYj65/Type/15MFYnML",
        "entities/0OfT51J/attributes/Phone/15MFYB01/LineType/evnnvRz",
        "entities/0OfT51J/attributes/Phone/15MFYB01/GeoCountry/evno8El"
      ],
      "createDate": "2025-03-11T00:00:48.093Z",
      "reltioLoadDate": "2025-03-10T23:59:10.316Z",
      "singleAttributeUpdateDates": {},
      "type": "configuration/sources/ReltioCleanser",
      "updateDate": "2025-03-11T00:00:48.093Z",
      "uri": "entities/0OfT51J/crosswalks/evnkyAt",
      "value": "0OfT51J"
    },
    {
      "attributes": [
        "entities/0OfT51J/attributes/Specialties/15MFZpID",
        "entities/0OfT51J/attributes/Specialties/15MFZpID/NestedEntityId/15MFa24z",
        "entities/0OfT51J/attributes/MiddleInitial/15MFVybl",
        "entities/0OfT51J/attributes/Phone/15MFYS33/Number/15MFYaZZ",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/Type/15MFXyDF",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/NestedEntityId/15MFY6jl",
        "entities/0OfT51J/attributes/Phone/15MFXtwz",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/Number/15MFXUNR",
        "entities/0OfT51J/attributes/Phone/15MFXctx/NestedEntityId/15MFXpgj",
        "entities/0OfT51J/attributes/Phone/15MFYS33",
        "entities/0OfT51J/attributes/Specialties/15MFZpID/SpecialtyType/15MFZtYT",
        "entities/0OfT51J/attributes/Phone/15MFYB01/NestedEntityId/15MFYNmn",
        "entities/0OfT51J/attributes/Phone/15MFXctx",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/Number/15MFXDKP",
        "entities/0OfT51J/attributes/Phone/15MFYB01",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/NestedEntityId/15MFXYdh",
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB/Type/15MFZcVR",
        "entities/0OfT51J/attributes/Phone/15MFYj65/NestedEntityId/15MFYvsr",
        "entities/0OfT51J/attributes/Phone/15MFYS33/Type/15MFYWJJ",
        "entities/0OfT51J/attributes/Phone/15MFYj65/Number/15MFYrcb",
        "entities/0OfT51J/attributes/Identifiers/15MFZHC9/NestedEntityId/15MFZTyv",
        "entities/0OfT51J/attributes/Identifiers/15MFZHC9/ID/15MFZPif",
        "entities/0OfT51J/attributes/Phone/15MFYj65",
        "entities/0OfT51J/attributes/Education/15MFa6LF/Degree/15MFaAbV",
        "entities/0OfT51J/attributes/Phone/15MFYB01/Number/15MFYJWX",
        "entities/0OfT51J/attributes/Phone/15MFYS33/NestedEntityId/15MFYepp",
        "entities/0OfT51J/attributes/Phone/15MFYB01/Type/15MFYFGH",
        "entities/0OfT51J/attributes/FirstName/15MFVuLV",
        "entities/0OfT51J/attributes/Education/15MFa6LF/NestedEntityId/15MFaErl",
        "entities/0OfT51J/attributes/Phone/15MFXLqv/Type/15MFXQ7B",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/Type/15MFX949",
        "entities/0OfT51J/attributes/Phone/15MFXtwz/Number/15MFY2TV",
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB",
        "entities/0OfT51J/attributes/Specialties/15MFZpID/Specialty/15MFZxoj",
        "entities/0OfT51J/attributes/Phone/15MFXctx/Number/15MFXlQT",
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB/NestedEntityId/15MFZl1x",
        "entities/0OfT51J/attributes/Phone/15MFXctx/Type/15MFXhAD",
        "entities/0OfT51J/attributes/Email/15MFZ097",
        "entities/0OfT51J/attributes/Education/15MFa6LF",
        "entities/0OfT51J/attributes/Identifiers/15MFZHC9/Type/15MFZLSP",
        "entities/0OfT51J/attributes/Email/15MFZ097/Email/evnruex",
        "entities/0OfT51J/attributes/Identifiers/15MFZYFB/ID/15MFZglh",
        "entities/0OfT51J/attributes/Identifiers/15MFZHC9",
        "entities/0OfT51J/attributes/Email/15MFZ097/Type/npysKVk",
        "entities/0OfT51J/attributes/Phone/15MFX4nt",
        "entities/0OfT51J/attributes/EntityUUID/15N4ACrt",
        "entities/0OfT51J/attributes/Phone/15MFXLqv",
        "entities/0OfT51J/attributes/Phone/15MFYj65/Type/15MFYnML",
        "entities/0OfT51J/attributes/Email/15MFZ097/NestedEntityId/npysOm0",
        "entities/0OfT51J/attributes/LastName/15MFW2s1",
        "entities/0OfT51J/attributes/Phone/15MFX4nt/NestedEntityId/15MFXHaf"
      ],
      "createDate": "2025-03-07T11:37:27.182Z",
      "reltioLoadDate": "2025-04-14T07:00:30.062Z",
      "singleAttributeUpdateDates": {},
      "type": "configuration/sources/CITELINE",
      "updateDate": "2025-03-07T11:37:27.182Z",
      "uri": "entities/0OfT51J/crosswalks/15MFaJ81",
      "value": "HCP-973664"
    }
  ],
  "label": "Alliric Isaac Willis",
  "secondaryLabel": "1100 Walnut St, Philadelphia, PENNSYLVANIA, 19107-5563, United States",
  "type": "configuration/entityTypes/HCP",
  "updatedBy": "NA03-SVT-20250129",
  "updatedTime": 1744614030062,
  "uri": "entities/0OfT51J"
}]
outputData=main(data)
with open("egressHCP.json","w") as file:
    json.dump(outputData, file, indent = 4)
