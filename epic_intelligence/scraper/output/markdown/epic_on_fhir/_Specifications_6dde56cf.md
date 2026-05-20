# Specifications - Epic on FHIR

> Source: https://fhir.epic.com/Specifications?api=1048

---

0 || FilterManager.FilteredCount() > 0)" style="min-height: 280px;">
 

 

 **Loading...**

 

 
 0 || FilterManager.FilteredCount() > 0)">
 

 
 
 

 
 

 

 
 0">
 
 
 
 
 
 
 
 

 - 
 
 All
 
 

 
 - 
 
 
 
 
 
 
 

 
 

 

 

 

 
 0)">
 
 

 
 
 
 
 
 

 
 

 
 0 && AvailableApis().length > 0)">
 
 0)">
 
### We couldn't find any APIs that match your search criteria.

 

 

 

 

 
= 2) }">

 

 
 
### Select an API to get started.

 With Epic's publicly available HL7® FHIR® standard APIs, you can design your software to interoperate with the Epic comprehensive health record at clinics, hospitals, and health systems worldwide. No purchase is necessary to access the specifications or work with an Epic customer that licenses API technology and services.

 

 

 
 

 

 **Loading...**

 
 
 

 

 
### 

 
 

 

 

 

 

 
 

 

 
 

 
 

 
 

 
 
 

 
 
 General Information
 
 
 

 
HTTP Method:

 

 

 
 
 

 
URL Template:

 

 

 
 
 

 
 

 Supported OAuth 2.0 User Types:
 [
 
 ](https://fhir.epic.com/Documentation?docId=usercontext)
 

 
 
 

 Supported User Types:
 [
 
 ](https://fhir.epic.com/Documentation?docId=usercontext)
 

 
 

 

 
 
 

 
Performs Scope Validation:

 

 

 
 
 

 
Subset of USCDI API Type:

 

 

 
 
 

 
API Group:

 

 

 
 
 

 

 MyChart Activity:
 [
 
 ](https://fhir.epic.com/Documentation?docId=patientfacingapps)
 

 

 
 [
 
 ](https://fhir.epic.com/Documentation?docId=patientfacingapps)
 

 

 
 
 
### Description

 

 
 
 

 
 This API may behave differently when used in a patient-facing context. See the Patient-Facing Apps Using FHIR document for more information.
 

 

 
 
 

 
 
 

 
 
 

 
 
 Request:
 

 
```

```

 
 
 

 

 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 (
 
 
 )
 
 | 
 | 
 | 
 | 
 |

 
 
 
 

 

 

 
 
 

 
 
 
### Native Request Elements

 

 
 
 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 

 | 
 
 
 | 
 
 
 conditional | 
 
 
 | 
 |

 
 
 
 

 
 
 

 
 | 
 Name | 
 
 Description | 
 
 
 Requirement | 
 
 
 Cardinality | 
 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 
 

 | 
 
 
 
 

 | 
 
 
 
 

 | 
 
 |

 
 
 
 

 

 
### Post-filter Request Elements

 

 Starting in the May 2024 version of Epic, the following search parameters that use a post-filtering mechanism are available. When responding to a request, the Epic FHIR server first retrieves all results that match your search (using any native search parameters you’ve provided), then filters down those results based on the additional post-filtered parameters you’ve specified.
 
For more information about post-filter parameters and related considerations, refer to the General Considerations section of the [FHIR Search Parameters](https://fhir.epic.com/Documentation?docId=searchparameters) document.

 
 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 

 | 
 
 
 | 
 
 
 conditional 
 | 
 
 
 | 
 |

 
 
 
 

 
 
 

 
 | 
 Name | 
 
 Description | 
 
 
 Requirement | 
 
 
 Cardinality | 
 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 
 

 | 
 
 
 
 

 | 
 
 
 
 

 | 
 
 |

 
 
 
 

 

 
 
 
### Post-filter Request Elements

 

 Starting in the May 2024 version of Epic, the following search parameters that use a post-filtering mechanism are available. When responding to a request, the Epic FHIR server first retrieves all results that match your search (using any native search parameters you’ve provided), then filters down those results based on the additional post-filtered parameters you’ve specified.
 
For more information about post-filter parameters and related considerations, refer to the General Considerations section of the [FHIR Search Parameters](https://fhir.epic.com/Documentation?docId=searchparameters) document.

 
 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 

 | 
 
 
 | 
 
 
 conditional 
 | 
 
 
 | 
 |

 
 
 
 

 
 
 

 
 | 
 Name | 
 
 Description | 
 
 
 Requirement | 
 
 
 Cardinality | 
 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 
 

 | 
 
 
 
 

 | 
 
 
 
 

 | 
 
 |

 
 
 
 

 

 
 
 
 
### Native Request Elements

 

 
 
 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 

 | 
 
 
 | 
 
 
 conditional | 
 
 
 | 
 |

 
 
 
 

 
 
 

 
 | 
 Name | 
 
 Description | 
 
 
 Requirement | 
 
 
 Cardinality | 
 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 
 

 | 
 
 
 
 

 | 
 
 
 
 

 | 
 
 |

 
 
 
 

 

 
 

 
 
 

 
 
 
 
 
 

 
 
 Response:
 

 
```

```

 
 
 

 

 
 0">
 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 (
 
 
 )
 
 | 
 | 
 | 
 | 
 |

 
 
 
 

 

 

 
 
 

 

 
 
 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 

 | 
 
 
 | 
 
 
 conditional | 
 
 
 | 
 |

 
 
 
 

 
 
 

 
 | 
 Name | 
 
 Description | 
 
 
 Requirement | 
 
 
 Cardinality | 
 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 
 

 | 
 
 
 
 

 | 
 
 
 
 

 | 
 
 |

 
 
 
 

 

 

 
 
 

 
### Types: 

 
 

 
#### 

 
 
 

 
 
 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 

 | 
 
 
 | 
 
 
 conditional | 
 
 
 | 
 |

 
 
 
 

 
 
 

 
 | 
 Name | 
 
 Description | 
 
 
 Requirement | 
 
 
 Cardinality | 
 
 |

 
 
 
 
 | 
 
 
 
 
 
 
 ()
 
 
 ()
 
 
 ()
 
 | 
 
 
 

 | 
 
 
 
 

 | 
 
 
 
 

 | 
 
 |

 
 
 
 

 

 

 
 

 
 
 

 
### Types: 

 
 
 

 
 

 

 

 

 
 | 
 Name | 
 Description | 
 Is Optional | 
 Is Array | 
 |

 
 
 
 
 | 
 
 
 (
 
 
 )
 
 | 
 | 
 | 
 | 
 |

 
 
 
 

 

 
 

 

 

 
 0">
 
### Remarks:

 

 

 

 
### Errors
When things go wrong, the API will respond with an error code and a human-readable description to describe the incorrect submission. Currently, the error code is not included in the REST version of the specification, but it is provided here for your reference. These codes are meant for developer use only - they should not be presented to end users. Instead, your application should interpret the codes and provide user-friendly resolution steps when data cannot be filed.

FHIR Errors come in two flavors:

- **Fatal Errors** cause the response to contain no results and are usually due to requests from the client processed as invalid - missing or invalid data in the request, unauthorized access, or expired content in the system.
- **Warning Errors** accompany a successful response and are used to indicate that part of a request could not be fulfilled - for example, if a status is unknown, but the request can be fulfilled, the API will return the data and indicate that part of the request couldn't be understood.

#### FHIR Error Codes

| Error Code | Severity | Description | Example | |
| 4100 | Fatal | The resource request contained an invalid parameter | Invalid parameter such as a nonexistent patient ID: `AllergyIntolerance?patient=foo` | |
| 4101 | Warning | Resource request returns no results | A request for data that was otherwise valid but no information was documented or found (i.e. a patient with no pertinent implanted devices, or a demographic search where no patients met the search criteria). | |
| 4102 | Fatal | The read resource request contained an invalid ID | Invalid Resource ID: `AllergyIntolerance/foo` | |
| 4103 | Fatal | The resource requested has been deleted | A read request for a resource that was deleted in the system | |
| 4104 | Fatal | A required FHIR element was not available to send in the response | Failed to determine a SNOMED code for the smoking status. | |
| 4107 | Fatal | The read resource request has been merged | Requesting a Patient which has been merged - in this event, in addition to the error response, we will respond with an HTTP Redirect status. To browsers and many HTTP clients, the redirect will be transparent. | |
| 4110 | Fatal | No parameters are provided in the search request | An invalid search request such as : `AllergyIntolerance?` | |
| 4111 | Fatal | Required search parameter missing from request | A request missing a required parameter (such as the patient): `Condition?category=diagnosis` | |
| 4112 | Fatal | The resource request contained an invalid combination of parameters | A search containing multiple different patient ID: `AllergyIntolerance?patient=[ID 1]&patient=[ID 2]` | |
| 4113 | Fatal | Session ID for cached search results has expired. | Making a request for previously accessed paginated search results after the search has expired. | |
| 4115 | Fatal | Required search parameter has an invalid value | An invalid parameter required for searching: `Condition?Patient=[ID]&category=foo` | |
| 4116 | Fatal | Invalid query for session. This error only applies to DSTU2 version paging functionality. | Called in paging context if the user has gone to the next page of the same session but changed the original query: 
 AllergyIntolerance?patient=[ID 1] <-- original query 
 AllergyIntolerance?patient=[ID 1]&page=2&session=123 <-- valid 
 AllergyIntolerance?patient=[ID 2]&page=2&session=123 <-- error is logged. | |
| 4117 | Warning | No CVX code for Immunization resource | Request for an Immunization resource without a documented CVX code. | |
| 4118 | Fatal | User not authorized for request | Request data that the authenticated user is not allowed access to view (i.e. a patient asking for data about a stranger's allergies). | |
| 4119 | Warning | Additional data may be present for patient | Request data while authenticated as an authorized patient or patient proxy. Inidicates that data available to the patient may not be the complete medical record within the system. | |
| 4122 | Warning | An unknown query parameter was supplied by the client | A request with dateWritten on a resource for which the parameter is ignored. 
 A request with parameter zzzzzz on any resource. | |
| 4127 | Fatal | Additional data may exist | This error is logged whenever Patient.Search exceeds 100 results. | |
| 4130 | Fatal | Break-the-Glass security does not authorize you to access the selected patient/resource | The patient has a sensitive psychiatric visit and you are not part of the psychiatric or care team. This is returned when you would attempt Encounter.Read on this encounter. 
Note: these checks are configured by each health system and may vary based on their security policies. | |
| 4131 | Fatal | The patient you are attempting to access is restricted. You must break the glass to access patient data. | The patient is a hospital employee so extra protection is in place such that only those who have provided a reason to access the chart can access all data. This is returned when you attempt a Patient.Read on that patient. 
Note: these checks are configured by each health system and may vary based on their security policies. | |
| 4134 | Information | The patient you are attempting to access is resctricted. You must Break-the-Glass to view patient data. | The patient is a hospital employee so extra protection is in place such that only those who have provided a reason to access the chart can access all data. 
Note: these checks are configured by each health system and may vary based on their security policies. | |
| 4135 | Fatal | Please try again tomorrow | Maximum document queries has been reached for the day. | |
| 40000 | Fatal | Incoming table mapping error | When calling the FamilyMemberHistory API, a relationship type is not mapped. | |
| 59100 | Information | Content invalid against the specification or a profile. | `/api/FHIR/MedicationStatement?patient=el5.bHVk3kkdaA-5ezLMCHQ3&stat=1` where "stat" is an unknown parameter. | |
| 59101 | Warning | Content invalid against the specification or a profile. | `/api/FHIR/R4/MedicationRequest?patient=eHtj-Tb68iBKA8ZsY8Ioq7w3&category=homemeds` where "homemeds" is an unknown category value. | |
| 59102 | Fatal | Content invalid against the specification or a profile. | `/api/FHIR/R4/MedicationRequest?patient=fakepatientid` where the patient ID is invalid. | |
| 59105 | Fatal | A structural issue in the content. | Invalid json syntax. | |
| 59108 | Fatal | Required {element name} missing | `/api/FHIR/STU3/Observation?patient=eTtVpZg2-.J.yFIP1qJbK4A3` where either the category or code parameter must be specified | |
| 59109 | Information | Optional {element name} invalid: {element value} | `/api/FHIR/STU3/Encounter?patient=e63wRTbPfr1p8UW81d8Seiw3&class=math` where the optional `class` parameter is not a valid category option | |
| 59111 | Fatal | Required {element name} invalid: {element value} | `/api/FHIR/R4/Observation?patient=e63wRTbPfr1p8UW81d8Seiw3&category=labresults` where the required `category` parameter is not a valid category option | |
| 59133 | Information | Processing issues. | This error is logged when fewer data elements than required are included in the request or when the search exceeds 100 results. | |
| 59141 | Fatal | An attempt was made to create a duplicate record. | AllergyIntolerance.Create was used to add an allergy to bees, but an allergy to bees already exists in the patient's chart. | |
| 59144 | Fatal | The reference provided was not found. | `/api/FHIR/STU3/Binary/eKqBNFDq6lyQ5SoH5lVu3oNUw1qX1ux2nVAxvjy9qQ9GqOvhmga08hSScb7nvH9ismBvLErBhIFIjKWeEpwa6kiO6w1ZAm5wt.LozW5CSo3s3` when this ID is not found. | |
| 59159 | Fatal | The content/operation failed to pass a business rule, and so could not proceed. | A request missing a required parameter (such as the patient): `Condition?category=diagnosis` | |
| 59177 | Fatal | An unexpected internal error has occurred. | Failed to file the LDA. | |
| 59187 | Fatal | Failed to find any patient-entered flowsheets. | When using FHIR Observation.Create in a patient-facing app, the patient does not have any Patient-Entered Flowsheets assigned. | |
| 59188 | Fatal | Failed to find one vital-signs flowsheet row by given codes. | When using FHIR Observation.Create, no single flowsheet row can be found by the codes provided in the request body. It can also be logged if the flowsheet row found is not mapped to the vital sign LOINC code (8716-3). | |
| 59189 | Fatal | Failed to file the reading. | When using FHIR Observation.Create, the API fails to file any readings to the patient's chart. | |

 

 
 0">
 
### Faults:

 

 
 | 
 
 Code | 
 
 
 Severity | 
 
 
 Alias | 
 
 
 Description | 
 
 |

 
 
 
 | 
 
 | 
 
 
 | 
 
 
 | 
 
 
 | 
 
 |

 
 
 

 

 
 0">
 
### Change Log:

 

 

 
 0 || $parent.CertificationVersions().length > 0">
 
### Product Information

 
 

 
Products:

 

 

 
 - 

 
 

 

 

 
 
 

 
First Available Version:

 

 

 
 

 

 

 

 
 

 
## That API was not found. It may have moved or you may not have access to it.

 

 

 

 

 

 

 

 

 

 

 

 

 [
 
 ](http://www.epic.com)
 

 

 
[Frequently Asked Questions (FAQs)](/FAQ)

 
[Contact](https://open.epic.com/Home/Contact)

 

 [Terms of Use](/Resources/Terms)
 

 
[Privacy Policy](https://open.epic.com/Home/PrivacyPolicy)

 

 

 
1979 Milky Way, Verona, WI 53593 

 

 © 1979-2026 Epic Systems Corporation. All rights reserved.
 Protected by U.S. patents. For details visit [www.epic.com/patents](http://www.epic.com/patents).
 

 HL7®, FHIR® and the FLAME mark are the registered trademarks of HL7 and are used with the permission of HL7. The use of these trademarks does not constitute a product endorsement by HL7.
 

 

 Epic, open.epic, and Epic on FHIR are trademarks or registered trademarks of Epic Systems Corporation.
 

 

 

 

 

 

 

 
 

 
#### 

 

 

 

 

 OK
 

 
 

 

 

 

 

 
 

 
#### 
 
 

 
 

 
 

 

 

 

 

 Confirm
 Cancel
 

 
 

 

 

 

 

 

 Due to inactivity you will be logged out in 60 seconds.

 

 

 

 

 

 

 

 

 
 
 
 

 

 
 

Saving

 

Loading

 
 

 
False