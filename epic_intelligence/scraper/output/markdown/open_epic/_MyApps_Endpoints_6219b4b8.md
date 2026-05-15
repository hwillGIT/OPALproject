# open.epic :: Endpoints

> Source: https://open.epic.com/MyApps/Endpoints

---

## 
 
 Sandbox Endpoints
 

 

 

 

 

 Testing is important. We've got servers waiting for you with
 [test patient data](https://fhir.epic.com/Documentation?docId=testpatients) to use.
 

 

 

 

 

 
 | 
 Sandbox Type | 
 FHIR Base URL | 
 |

 
 
 | 
 Fhir.epic.com Sandbox - R4 | 
 https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4/ | 
 |

 | 
 Fhir.epic.com Sandbox - STU3 | 
 https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/STU3/ | 
 |

 | 
 Fhir.epic.com Sandbox - DSTU2 | 
 https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/DSTU2/ | 
 |

 
 

 

 

 

 

 

 
## 
 
 Production Endpoints
 

 

 

 

 

 Your apps can use the endpoint information below to connect to health systems that use Epic software.
 

 

 

 

 
#### Production Endpoint Information

 

 Production endpoint information is available in several formats. We recommend using the [User-access Brands Bundle](#brands)
 which includes details that can help patients find the right endpoint.
 The other formats are deprecated, but retained for backwards compatibility to support apps that consume those formats.
 

 
#### Important Note for Developers

 

 Applications SHOULD NOT perform runtime queries for endpoint data hosted on open.epic.com.
 Applications should reguarly (for example, weekly) download endpoint information and re-host endpoint data on your own infrastructure.
 Epic provides no service level agreement or uptime guarantees for the endpoint files hosted on open.epic.com.
 

 

 

 

 
### 
 User-access Brands Bundle
 

 Recommended
 Machine-readable Format
 

 

 R4
 

 

 

 

 

 Details about FHIR endpoints are provided in the
 [User-access Brands Bundle](https://hl7.org/fhir/smart-app-launch/brands.html)
 formats defined by the [SMART App Launch](https://hl7.org/fhir/smart-app-launch/) specification.
 This format uses FHIR Endpoint and Organization resources to provide details about FHIR endpoints,
 including branding information and facility identifiers and addresses for the organizations hosting these endpoints.
 This is the recommended machine-readable format.
 

 

 - Identifiers and physical location details are included to help patients search for their health system.

 - 
 Conforms to [SMART App Launch User-access Brands](https://hl7.org/fhir/smart-app-launch/brands.html)
 endpoint publishing standard.
 

 

 Epic's implementation of the [User-access Brands Bundle](https://hl7.org/fhir/smart-app-launch/brands.html) specification
 includes two types of Organization resources and one type of Endpoint resource:

 

 
## Organization (Primary Brand)

 

 This represents the brand of the healthcare organization that patients will recognize.
 Epic recommends that Organization Brands be the primary selectable item in the patient's user experience.
 

 

 
 | 
 
 Name
 | 
 
 Flags
 | 
 
 Card.
 | 
 
 Type
 | 
 
 Description & Constraints
 | 
 |

 | 
 Organization | 
 | 
 0..* | 
 [UserAccessBrand](http://hl7.org/fhir/smart-app-launch/STU2.2/StructureDefinition-user-access-brand.html) | 
 The Organizational Brand of the healthcare organization that patients will recognize. Epic recommends that Organization Brands be the primary selectable item most user interfaces. | 
 |

 | 
 Slices for identifier | 
 | 
 0..* | 
 [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
 Identifies this organization across multiple systems | 
 |

 | 
 identifier:NPI | 
 | 
 0..* | 
 [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
 National Provider Identifier (NPI)

Required Pattern: At least the following | 
 |

 | 
 system | 
 | 
 1..1 | 
 [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
 The namespace for the identifier value
Fixed Value: http://hl7.org/fhir/sid/us-npi | 
 |

 | 
 value | 
 | 
 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 The value that is unique | 
 |

 | 
 Slices for type | 
 | 
 0..* | 
 [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
 Kind of organizationSlice: Unordered, Open by value:$this | 
 |

 | 
 type:pab | 
 | 
 0..* | 
 [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
 Categories of user access offered
Binding: [User Access Category Value Set](http://hl7.org/fhir/smart-app-launch/STU2.2/ValueSet-user-access-category.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)) | 
 |

 | 
 coding | 
 | 
 | 
 | 
 | 
 |

 | 
 code | 
 | 
 0..1 | 
 [code](http://hl7.org/fhir/R4/datatypes.html#code) | 
 Symbol in syntax defined by the system | 
 |

 | 
 name | 
 [C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 The patient-friendly name for the organization | 
 |

 | 
 address | 
 [C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
 0..* | 
 [Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
 An address for the organization | 
 |

 | 
 state | 
 | 
 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 A state where this organization provides patient care | 
 |

 | 
 endpoint | 
 S | 
 0..* | 
 [Reference](http://hl7.org/fhir/R4/references.html)([Endpoint](http://hl7.org/fhir/R4/endpoint.html)) | 
 Endpoint associated with this brand | 
 |

 | 
 reference | 
 S | 
 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Relative URL to an Endpoint within the User Access Brands Bundle | 
 |

 

 

 

 
## Organization (Care Facility)

 

 This represents the physical locations where patients receive care.
 Often many facilities are associated with a single brand.
 This information may be used to supplement the user experience of selecting the Organization Brand.
 For example, you may use this information to sort the associated Organization Brands
 based on geospatial proximity to the patient.

 The FHIR endpoint associated with a facility will be on the Organization Brand
 that is referenced by the facility's Organization.partOf property.
 

 

 
 | 
 
 Name
 | 
 
 Flags
 | 
 
 Card.
 | 
 
 Type
 | 
 
 Description & Constraints
 | 
 |

 | 
 Organization | 
 
 | 0..* | 
 [UserAccessBrand](http://hl7.org/fhir/smart-app-launch/STU2.2/StructureDefinition-user-access-brand.html) | 
 A specific facility where patients can receive care. Facilities represented in in this Organization profile are always part of a larger healthcare organization brand, referenced in Organization.partOf. | 
 |

 | 
 name | 
 [C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Name of the healthcare facility | 
 |

 | 
 address | 
 [C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
 0..* | 
 [Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
 An address for the organization | 
 |

 | 
 type | 
 
 | 0..1 | 
 [code](http://hl7.org/fhir/R4/datatypes.html#code) | 
 postal | physical | both | 
 |

 | 
 text | 
 
 | 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Text representation of the address | 
 |

 | 
 line | 
 
 | 0..* | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Street name, number, direction & P.O. Box etc. | 
 |

 | 
 city | 
 
 | 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Name of city, town etc. | 
 |

 | 
 state | 
 
 | 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Sub-unit of country (abbreviations ok) | 
 |

 | 
 postalCode | 
 
 | 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Postal code for area | 
 |

 | 
 country | 
 
 | 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Country (e.g. can be ISO 3166 2 or 3 letter code) | 
 |

 | 
 partOf | 
 
 | 0..1 | 
 [Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
 The primary, patient-recognizable brand this facility is assocaited with | 
 |

 | 
 reference | 
 [C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 Literal reference, Relative, internal or absolute URL | 
 |

 

 

 

 
## Endpoint (FHIR Service Base URL)

 

 This includes the connection details for a brand, including the FHIR service base URL.
 

 

 .managingOrganization: Organization ID for the organization in the Manage keys activity for the
 client in Build Apps on fhir.epic.com
 

 

 
 | 
 
 Name
 | 
 
 Flags
 | 
 
 Card.
 | 
 
 Type
 | 
 
 Description & Constraints
 | 
 |

 | 
 Endpoint | 
 | 
 0..* | 
 [UserAccessEndpoint](http://hl7.org/fhir/smart-app-launch/STU2.2/StructureDefinition-user-access-endpoint.html) | 
 The technical details of an endpoint that can be used for electronic services | 
 |

 | 
 Slices for extension | 
 | 
 | 
 | 
 Content/Rules for all slices | 
 |

 | 
 endpoint-fhir-version | 
 | 
 0..* | 
 [code](http://hl7.org/fhir/R4/datatypes.html#code) | 
 Endpoint FHIR Version
URL: [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)
Binding: [FHIRVersion](http://hl7.org/fhir/R4/valueset-FHIR-version.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)) | 
 |

 | 
 connectionType | 
 Σ | 
 1..1 | 
 [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
 Protocol/Profile/Standard to be used with this endpoint connection
Binding: [EndpointConnectionType](http://hl7.org/fhir/R4/valueset-endpoint-connection-type.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible))
Required Pattern: At least the following | 
 |

 | 
 system | 
 | 
 1..1 | 
 [uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
 Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-connection-type | 
 |

 | 
 code | 
 | 
 1..1 | 
 [code](http://hl7.org/fhir/R4/datatypes.html#code) | 
 Symbol in syntax defined by the system
Fixed Value: hl7-fhir-rest | 
 |

 | 
 managingOrganization | 
 | 
 0..1 | 
 [Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
 The organization with which client secrets/keys are registered in the 'Review & Manage Downloads' screen in fhir.epic.com | 
 |

 | 
 identifier | 
 | 
 0..1 | 
 [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
 The identifier of the organization with which client secrets/keys are registered | 
 |

 | 
 display | 
 | 
 0..1 | 
 [string](http://hl7.org/fhir/R4/datatypes.html#string) | 
 The name of the organization with which client secrets/keys are registered | 
 |

 | 
 address | 
 | 
 1..1 | 
 [url](http://hl7.org/fhir/R4/datatypes.html#url) | 
 The technical base address for connecting to this endpoint | 
 |

 

 

 

 

 
 [Download R4 Endpoints as a Brands File](/Endpoints/Brands)
 

 

 

 

 

 

 

 
### 
 Endpoint Bundle
 

 Deprecated
 Machine-readable Format
 

 

 DSTU2
 R4
 

 

 

 

 

 

 The FHIR Endpoint Bundle provides a URL for a FHIR endpoint and a patient-friendly name for that endpoint in a
 generic FHIR Endpoint resource format that predates the creation of the User-access Brands specification.
 This format includes both FHIR DSTU2 and FHIR R4 endpoints.
 

 

 This format is deprecated but retained for backwards compatibility to support apps that already use this format.
 The [User-access Brands Bundle](#brands) format is recommended for new and existing apps, as that format
 includes additional information, such the addresses associated with facilities using each endpoint.
 

 

 The FHIR Endpoint Bundle file includes a few key properties for each endpoint:
 

 - *Endpoint.name*: The patient-friendly name for the FHIR endpoint.

 - *Endpoint.address*: The FHIR URL which patient-facing applications can use access data for the patient.

 - *Endpoint.period.start*: The date this endpoint was first available.

 

 

 

 

 

 
 [Download DSTU2 Endpoints as a FHIR Bundle](/Endpoints/DSTU2)
 

 
 [Download R4 Endpoints as a FHIR Bundle](/Endpoints/R4)
 

 

 

 

 

 

 

 
### 
 JSON File
 

 Deprecated
 Machine-readable Format
 

 

 DSTU2
 

 

 

 

 

 

 The JSON file provides a URL for a FHIR endpoint and a patient-friendly name for that endpoint.
 This format only includes FHIR DSTU2 endpoints. FHIR R4 endpoint are not included.
 This format is deprecated but retained for backwards compatibility to support apps that already use this format.
 

 

 The [User-access Brands Bundle](#brands) format is recommended for new and existing apps, as that format
 includes additional information, such the addresses associated with facilities using each endpoint.
 

 

 The JSON file includes two properties for each endpoint:
 

 - *OrganizationName*: The patient-friendly name for the FHIR endpoint.

 - *FHIRPatientFacingURI*: The FHIR URL which patient-facing applications can use access data for the patient.

 

 

 

 

 

 
 [Download DSTU2 Endpoints as a JSON File](/MyApps/EndpointsJson)
 

 

 

 

 

 

 

 
### 
 Table View
 

 Human-readable Format
 

 

 R4
 

 

 

 

 Your apps can use the information below to connect to the 1197 FHIR R4 endpoints for the listed organizations.
 

 

 

 
 | 
 Organization ID | 
 Organization Name | 
 Production FHIR Base URLs | 
 |

 
 
 | 
 476 | 
 AACI | 
 https://webprd.ochin.org/prd-fhir/MyChartAACI/api/FHIR/R4 | 
 |

 | 
 827 | 
 Access Community Health Centers | 
 https://epicproxy.hosp.wisc.edu/FhirProxy/api/FHIR/R4 | 
 |

 | 
 1696 | 
 Access Community Health Network | 
 https://eprescribing.accesscommunityhealth.net/FHIR/ACCESS/api/FHIR/R4 | 
 |

 | 
 525 | 
 Acumen Physician Solutions | 
 https://epicproxy.et1041.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 912 | 
 Adams Memorial Hospital | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 337 | 
 Adams School of Dentistry for UNC | 
 https://epicfe.unch.unc.edu/FHIR/UNCADAMSDENTISTRY/api/FHIR/R4 | 
 |

 | 
 476 | 
 Adapt Integrated Health Care | 
 https://webprd.ochin.org/prd-fhir/MYCHARTADAPTIHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Advance Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTADVANCECH/api/FHIR/R4 | 
 |

 | 
 568 | 
 Advanced Radiology | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Advanced Spine and Pain Specialists | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 560 | 
 Advanced Vascular Surgery | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1108 | 
 AdvantageCare Physicians | 
 https://epwebapps.acpny.com/FHIRproxy/ACPNY/api/FHIR/R4 | 
 |

 | 
 9392 | 
 AdventHealth | 
 https://mobile.adventhealth.com/oauth2-PRD/api/FHIR/R4 | 
 |

 | 
 838 | 
 Adventist Health Columbia Gorge | 
 https://epicmobile.ohsu.edu/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 754 | 
 Advocate Aurora Health | 
 https://epicproxy.et0301.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Agape Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTAGAPE/api/FHIR/R4 | 
 |

 | 
 912 | 
 AIHS Guide | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 1193 | 
 Akron Children's | 
 https://haiku-canto-prod.chmca.org/ARR-FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 4126 | 
 Alameda Health System | 
 https://epicproxy.et1075.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Alaska Neurology Center | 
 https://haikuak.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1882 | 
 Alaska Regional Hospital | 
 https://mountainstarhealthfhirprd.app.medcity.net/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Albany County Department of Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTACH/api/FHIR/R4 | 
 |

 | 
 16296 | 
 Albany Med Health System | 
 https://epicproxy.et1299.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1005 | 
 Aligned Geriatrics | 
 https://epicproxy.et0502.epichosted.com/FhirProxy/RAW/api/FHIR/R4 | 
 |

 | 
 337 | 
 Alignment Corporation | 
 https://epicfe.unch.unc.edu/FHIR/Alignment/api/FHIR/R4 | 
 |

 | 
 476 | 
 All Care Health Center | 
 https://webprd.ochin.org/prd-fhir/ALLCAREHEALTHCENTER/api/FHIR/R4 | 
 |

 | 
 2246 | 
 Alleghany Health | 
 https://epicproxy.et0905.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 969 | 
 Allegheny Health Network | 
 https://epicprisfd.ahn.org/PRD-FHIR/api/FHIR/R4 | 
 |

 | 
 912 | 
 Alliance Health Centers | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Alliance Medical Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTAMC/api/FHIR/R4 | 
 |

 | 
 355 | 
 Allina | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 9098 | 
 Altais Health Solutions | 
 https://epicproxy.et1138.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 4050 | 
 AltaMed | 
 https://epicproxy.et1123.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 1832 | 
 Altru | 
 https://epicsoap.altru.org/fhir/STANDARD/api/FHIR/R4 | 
 |

 | 
 405 | 
 Anchorage Neighborhood Health Center | 
 https://haikuak.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Anchorage Neurosurgical Associates | 
 https://haikuak.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1626 | 
 AnMed Health | 
 https://epicproxy.et0971.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 901 | 
 Ann & Robert H. Lurie Children's Hospital of Chicago | 
 https://epicmobile.luriechildrens.org/Interconnect-FHIRPRD/HOME/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Appleton Health | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 10008 | 
 Arizona Community Physicians | 
 https://epicproxy.et1186.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 323 | 
 Arkansas Children's | 
 https://epicproxy.et1036.epichosted.com/APIProxyPRD/AC/api/FHIR/R4 | 
 |

 | 
 1882 | 
 Arlington Maternal Fetal Specialists | 
 https://stdavidsfhirprd.app.medcity.net/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 14997 | 
 Array | 
 https://epicproxy.et1284.epichosted.com/FHIRProxy/KEYCARE/api/FHIR/R4 | 
 |

 | 
 7885 | 
 Arrowhead Regional Medical Center | 
 https://epicproxy.et1152.epichosted.com/fhirproxy/ARMC/api/FHIR/R4 | 
 |

 | 
 19520 | 
 Articularis | 
 https://epicproxy.et4006.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 358 | 
 Asante Health System | 
 https://epicmobile.asante.org/FHIR-PRD/HOME/api/FHIR/R4 | 
 |

 | 
 6111 | 
 Ascension - Providence HealthCare Network | 
 https://stofo.providence-waco.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 475 | 
 Ascension Illinois | 
 https://epicmobile.presencehealth.org/fhirPRD/api/FHIR/R4 | 
 |

 | 
 564 | 
 Ascension Wisconsin | 
 https://eprescribe.wfhc.org/FHIRproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Asian Counseling and Referral Service | 
 https://webprd.ochin.org/prd-fhir/MYCHARTACRS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Asian Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTAHS/api/FHIR/R4 | 
 |

 | 
 14539 | 
 Aspen Valley Health | 
 https://epicproxy.et1254.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2285 | 
 Aspire | 
 https://epichaiku.chs-mi.com/FHIRPROXY/api/FHIR/R4 | 
 |

 | 
 1929 | 
 Aspirus | 
 https://erx.aspirus.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Astera Health | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 1854 | 
 Atlantic Health | 
 https://epicproxy.et0907.epichosted.com/FHIRProxyPRD/MYCHARTATLANTICHEALTH/api/FHIR/R4 | 
 |

 | 
 2246 | 
 Atrium Health | 
 https://epicproxy.et0905.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 684 | 
 Atrius Health | 
 https://iatrius.atriushealth.org/FHIR/MYCHART/api/FHIR/R4 | 
 |

 | 
 585 | 
 Audubon County Memorial Hospital & Clinics | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1741 | 
 Austin Regional Clinic | 
 https://mobileprod.arcmd.com/FHIR/api/FHIR/R4 | 
 |

 | 
 9833 | 
 AvanceCare | 
 https://epicproxy.et1190.epichosted.com/FHIRProxyPRD/AvanceCare/api/FHIR/R4 | 
 |

 | 
 476 | 
 Avenue 360 | 
 https://webprd.ochin.org/prd-fhir/MYCHARTA360/api/FHIR/R4 | 
 |

 | 
 26238 | 
 Avera Health | 
 https://epicproxy.et1439.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 528 | 
 Avita Health System | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 476 | 
 Axis Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTAXIS/api/FHIR/R4 | 
 |

 | 
 623 | 
 Bailey Medical Center | 
 https://epicproxy.ardenthealth.com/fhir/BMC/api/FHIR/R4 | 
 |

 | 
 1002 | 
 Ballad Health | 
 https://soap.wellmont.org/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 2159 | 
 Baptist Health | 
 https://api.baptist-health.org/Interconnect-FHIR/MYCHARTBH/api/FHIR/R4 | 
 |

 | 
 10933 | 
 Baptist Health - Northeast Florida | 
 https://epicproxy.et1206.epichosted.com/FHIRProxy/BHJ/api/FHIR/R4 | 
 |

 | 
 1515 | 
 Baptist Healthcare | 
 https://epicproxy.bhsi.com/PRD-FHIR/BHSI/api/FHIR/R4 | 
 |

 | 
 572 | 
 Baptist Memorial Health Care | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 405 | 
 Barrett Hospital and Healthcare | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2088 | 
 Barton Health | 
 https://fhir.renown.org/FHIRProxy/BMH/api/FHIR/R4 | 
 |

 | 
 476 | 
 Bartz-Altadonna Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTBACHC/api/FHIR/R4 | 
 |

 | 
 2378 | 
 Bassett Healthcare | 
 https://soap.bassett.org/FHIR/api/FHIR/R4 | 
 |

 | 
 17550 | 
 Baton Rouge General | 
 https://interconnect.brgeneral.org/oauth/BRG/api/FHIR/R4 | 
 |

 | 
 982 | 
 Baton Rouge Orthopaedic Clinic | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Bay Area Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTBACH/api/FHIR/R4 | 
 |

 | 
 904 | 
 Bay Area Hospital | 
 https://epicproxy.et1030.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 904 | 
 Bay Clinic | 
 https://epicproxy.et1030.epichosted.com/FHIRProxy/SCHS/api/FHIR/R4 | 
 |

 | 
 754 | 
 BayCare Clinic | 
 https://epicproxy.et0301.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 397 | 
 Bayhealth Medical Center | 
 https://epproxy.bayhealth.org/FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 643 | 
 Baylor | 
 https://fhir.clinical.bcm.edu/Stage1Fhir/BCMMYC/api/FHIR/R4 | 
 |

 | 
 974 | 
 Baylor Scott & White Health | 
 https://epicproxy.bswhealth.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Baywell Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTBAYWELL/api/FHIR/R4 | 
 |

 | 
 476 | 
 Bear Lake Memorial Clinic | 
 https://webprd.ochin.org/prd-fhir/BLMHOSPITAL/api/FHIR/R4 | 
 |

 | 
 476 | 
 Bee Busy Wellness Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTBBWC/api/FHIR/R4 | 
 |

 | 
 26474 | 
 Beebe Healthcare | 
 https://icfg-p.beebehealthcare.org/oauth2prdproxy/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Bellaire Allergy & Asthma | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 902 | 
 Bellin | 
 https://arr.thedacare.org/FHIR/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Beloved Community Family Wellness Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Ben Archer Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 18855 | 
 Benefis Health System | 
 https://epicproxy.et1334.epichosted.com/FHIRProxy/BENEFIS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Bertie County Rural Health | 
 https://webprd.ochin.org/prd-fhir/BCRHA/api/FHIR/R4 | 
 |

 | 
 476 | 
 BestCare Treatment | 
 https://webprd.ochin.org/prd-fhir/BESTCARETREATMENT/api/FHIR/R4 | 
 |

 | 
 835 | 
 Beth Israel Lahey Health | 
 https://fhir.laheyhealth.org/proxy-prd-fhir/api/FHIR/R4 | 
 |

 | 
 434 | 
 Bethlehem Health Bureau | 
 https://proxy.lvh.com/FHIR/api/FHIR/R4 | 
 |

 | 
 516 | 
 Billings OBGYN | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 11509 | 
 BioSpine Institute | 
 https://epicproxy.et1233.epichosted.com/FHIRProxy/AFFILIATE/api/FHIR/R4 | 
 |

 | 
 348 | 
 BJC Healthcare & Washington University | 
 https://epicproxy.et0965.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1752 | 
 Bon Secours Health System | 
 https://carepath.health-partners.org/Proxy-FHIR/BBSHSI/api/FHIR/R4 | 
 |

 | 
 715 | 
 Boston Children's Hospital | 
 https://epicproxy.et1351.epichosted.com/APIProxyPRD/HOME/api/FHIR/R4 | 
 |

 | 
 1718 | 
 Boston Medical Center | 
 https://emerge-soap1.bmc.org/FHIR-PRD/HOME/api/FHIR/R4 | 
 |

 | 
 3726 | 
 Boulder Community Health | 
 https://prevprox.bch.org/FHIRproxyPRD/api/FHIR/R4 | 
 |

 | 
 3726 | 
 Boulder Medical Center | 
 https://prevprox.bch.org/FHIRproxyPRD/api/FHIR/R4 | 
 |

 | 
 14009 | 
 Bozeman Health | 
 https://revproxy.bh.bozemanhealth.org/Interconnect-OAuth2-PRD/api/FHIR/R4 | 
 |

 | 
 1563 | 
 Broadway | 
 https://minerva.northmemorial.com/fhir/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Brockton Neighborhood Health Center | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 560 | 
 Bronson | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2815 | 
 Brooklyn Health | 
 https://epicproxy.et1043.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 3442 | 
 Brookwood Baptist Health | 
 https://epicproxy.bhsala.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Broward Community and Family Health Centers | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 20050 | 
 Broward Health | 
 https://epicproxy.et1369.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Bruce W Moskowitz | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/BWM/api/FHIR/R4 | 
 |

 | 
 2255 | 
 Bryan Health | 
 https://epicproxy.et1031.epichosted.com/FHIRProxy/BHS/api/FHIR/R4 | 
 |

 | 
 623 | 
 BSA | 
 https://epicproxy.ardenthealth.com/fhir/BSA/api/FHIR/R4 | 
 |

 | 
 1924 | 
 Buffalo Medical Group | 
 https://fhir.buffalomedicalgroup.com/fhir-arr/api/FHIR/R4 | 
 |

 | 
 476 | 
 Burnett Medical Center | 
 https://webprd.ochin.org/prd-fhir/BURNETTMEDICALCENTER/api/FHIR/R4 | 
 |

 | 
 798 | 
 Burnsville Family Physicians | 
 https://sfd.fairview.org/FHIR/BFP/api/FHIR/R4 | 
 |

 | 
 405 | 
 Butte Native Wellness | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Caldera Family Medicine | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/CFM/api/FHIR/R4 | 
 |

 | 
 1981 | 
 Cambridge Health Alliance | 
 https://epicmobile.challiance.org/Interconnect-OAuth2/CHA/api/FHIR/R4 | 
 |

 | 
 476 | 
 CamCare | 
 https://webprd.ochin.org/prd-fhir/CAMCARE/api/FHIR/R4 | 
 |

 | 
 912 | 
 Cameron Health | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Camillus Health Concern | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2246 | 
 Camino Health Center | 
 https://epicproxy.et0905.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Cancer Care NorthWest | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 746 | 
 CancerCare Specialists | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 8278 | 
 Cape Cod Healthcare | 
 https://epicproxy.et1149.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 476 | 
 Care Alliance Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCA/api/FHIR/R4 | 
 |

 | 
 576 | 
 Care New England | 
 https://cnesp001.carene.org/FHIR/api/FHIR/R4 | 
 |

 | 
 13877 | 
 CareArc | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 18458 | 
 Carelon | 
 https://interconnect.carelonhealth.com/Interconnect-PRD-OAuth2/api/FHIR/R4/ | 
 |

 | 
 457 | 
 Carilion Clinic | 
 https://epicproxy.et0600.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 1911 | 
 Carle | 
 https://epicproxy.et0316.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1311 | 
 Carol Milgard Breast Center | 
 https://soapprod.multicare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Carolina Family Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCFHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Carolina Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCHC/api/FHIR/R4 | 
 |

 | 
 20730 | 
 CarolinaEast Health System | 
 https://epicproxy.et1385.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 959 | 
 CaroMont Health | 
 https://spp.caromonthealth.org/FhirProxy/CAROMONT/api/FHIR/R4 | 
 |

 | 
 338 | 
 Carson Tahoe | 
 https://webproxyprd.med.utah.edu/FHIRMyChart/api/FHIR/R4 | 
 |

 | 
 2088 | 
 Carson Valley Health | 
 https://fhir.renown.org/FHIRProxy/CVH/api/FHIR/R4 | 
 |

 | 
 405 | 
 Cascade Community Health | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Cascade Internal Medicine | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/CIM/api/FHIR/R4 | 
 |

 | 
 476 | 
 Cascade Medical Center | 
 https://webprd.ochin.org/prd-fhir/CASCADEMEDICALCENTER/api/FHIR/R4 | 
 |

 | 
 476 | 
 Cascadia Health | 
 https://webprd.ochin.org/prd-fhir/CASCADIAHEALTH/api/FHIR/R4 | 
 |

 | 
 585 | 
 Cass County Health System | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 6552 | 
 Catholic Health | 
 https://epicproxy.et1144.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1054 | 
 Catholic Health Services of Long Island | 
 https://epx1.chsli.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1375 | 
 CCM Health | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 709 | 
 Cedars-Sinai | 
 https://cslinkmobile.csmc.edu/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2585 | 
 CEENTA | 
 https://epicproxy.et1001.epichosted.com/FHIRProxyPRD/CEENTA/api/FHIR/R4 | 
 |

 | 
 476 | 
 Cempa Community Care | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCEMPA/api/FHIR/R4 | 
 |

 | 
 1375 | 
 CentraCare | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Central City Concern | 
 https://webprd.ochin.org/prd-fhir/CENTRALCITYCONCERN/api/FHIR/R4 | 
 |

 | 
 9682 | 
 Central Health | 
 https://epicproxy.et1164.epichosted.com/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2285 | 
 Central Michigan University | 
 https://epichaiku.chs-mi.com/FHIRPROXY/api/FHIR/R4 | 
 |

 | 
 16451 | 
 Central Ohio Primary Care Physicians | 
 https://rp-prd.copcp.com/fhirProxy/HOME/api/FHIR/R4 | 
 |

 | 
 476 | 
 Central Outreach Wellness Center | 
 https://webprd.ochin.org/prd-fhir/CENTRALOUTREACH/api/FHIR/R4 | 
 |

 | 
 405 | 
 Central Peninsula Hospital | 
 https://haikuak.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 572 | 
 Central Surgical Associates | 
 https://rxedi.bmhcc.org/prd-fhir/CSA/api/FHIR/R4 | 
 |

 | 
 20340 | 
 Centralus Health | 
 https://epicrpprd.xtensys.com/oauth2-prd/api/FHIR/R4 | 
 |

 | 
 560 | 
 Cereal City Pediatrics | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 26330 | 
 CGH Medical Center | 
 https://epicproxy.et1437.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 ChapCare | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCHAP/api/FHIR/R4 | 
 |

 | 
 476 | 
 Charles B. Wang Community Health Center | 
 https://webprd.ochin.org/prd-fhir/CBWCHC/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Charles River Community Health | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Chehalis Tribal Wellness Center | 
 https://webprd.ochin.org/prd-fhir/CHEHALISTRIBEMYCHART/api/FHIR/R4 | 
 |

 | 
 686 | 
 Cherry Hill Free Clinic | 
 https://epicproxy.et1017.epichosted.com/FHIRProxy/CHFC/api/FHIR/R4 | 
 |

 | 
 1752 | 
 Chesapeake Regional Healthcare | 
 https://carepath.health-partners.org/Proxy-FHIR/CRH/api/FHIR/R4 | 
 |

 | 
 1948 | 
 Cheyenne Regional Medical Center | 
 https://soap.crmcwy.org/fhirproxy/HOME/api/FHIR/R4 | 
 |

 | 
 700 | 
 CHI Franciscan Health | 
 https://rp.catholichealth.net/fhir/api/FHIR/R4 | 
 |

 | 
 700 | 
 CHI Health | 
 https://rp.chihealth.com/fhir/api/FHIR/R4 | 
 |

 | 
 700 | 
 CHI Memorial | 
 https://rpsouth.catholichealth.net/fhir/api/FHIR/R4 | 
 |

 | 
 700 | 
 CHI St. Alexius Health | 
 https://rp.chihealth.com/fhir/api/FHIR/R4 | 
 |

 | 
 700 | 
 CHI St. Joseph's Health | 
 https://rpsouth.catholichealth.net/fhir/api/FHIR/R4 | 
 |

 | 
 403 | 
 CHI St. Vincent | 
 https://epic-fhir.mercy.net/PRDFHIRSGF/CHI/api/FHIR/R4/ | 
 |

 | 
 13877 | 
 Chicago Family Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 19344 | 
 Chickasaw Nation Health | 
 https://epicintconn.chickasawnationhealth.net/Interconnect-OAuth2-PRD/api/FHIR/R4 | 
 |

 | 
 1193 | 
 Child Guidance and Family Solutions | 
 https://haiku-canto-prod.chmca.org/ARR-FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 411 | 
 Children's Health | 
 https://fhir.childrens.com/Interconnect-OAuth2PRD/api/FHIR/R4 | 
 |

 | 
 1036 | 
 Children's Healthcare of Atlanta | 
 https://wpprod.choa.org/FHIR_PRD/api/FHIR/R4 | 
 |

 | 
 1367 | 
 Children's Heart Clinic of LA | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 1334 | 
 Children's Hospital Colorado | 
 https://fhir.childrenscolorado.org/fhirprd/api/FHIR/R4 | 
 |

 | 
 26341 | 
 Children's Mercy Kansas City | 
 https://epicproxy.et1422.epichosted.com/fhirproxyPRD/api/FHIR/R4 | 
 |

 | 
 1245 | 
 Children's Nebraska | 
 https://EPROXY1.chsomaha.org/FHIRPROXY/api/FHIR/R4/ | 
 |

 | 
 13417 | 
 Children's of Alabama | 
 https://epicproxy.et1246.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 634 | 
 Children's Wisconsin | 
 https://epicproxy.et0815.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 20763 | 
 Choctaw Nation | 
 https://epicproxy.et1380.epichosted.com/APIPROXYPRD/api/FHIR/R4 | 
 |

 | 
 332 | 
 CHOP | 
 https://epicnsproxy.chop.edu/fhir/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Christian Community Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1911 | 
 Christie Clinic | 
 https://epicproxy.et0316.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 866 | 
 Christus Health | 
 https://proxy.christushealth.org/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 340 | 
 Cincinnati Children's | 
 https://boomer.cchmc.org/fhir/CCHMC/api/FHIR/R4 | 
 |

 | 
 26721 | 
 Citizen Potawatomi Nation | 
 https://epicproxy.et1447.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Citizens Health | 
 https://webprd.ochin.org/prd-fhir/CMCIKS/api/FHIR/R4 | 
 |

 | 
 434 | 
 City of Allentown Pennsylvania | 
 https://proxy.lvh.com/FHIR/api/FHIR/R4 | 
 |

 | 
 1344 | 
 City of Hope | 
 https://epic-rproxyprod.coh.org/Interconnect-FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 City of Milwaukee Health Department | 
 https://webprd.ochin.org/prd-fhir/MHDMYCHART/api/FHIR/R4 | 
 |

 | 
 476 | 
 Clackamas County Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCLACKAMAS/api/FHIR/R4 | 
 |

 | 
 405 | 
 Clark Fork Valley Hospital | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 619 | 
 Cleveland Clinic | 
 https://api.ccf.org/mu/api/FHIR/R4 | 
 |

 | 
 619 | 
 Cleveland Clinic | 
 https://api.ccf.org/mu/api/FHIR/R4 | 
 |

 | 
 476 | 
 Clinica Romero | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCR/api/FHIR/R4 | 
 |

 | 
 23440 | 
 Clinica Sierra Vista | 
 https://epicproxy.et1430.epichosted.com/APIPROXYPRD/CSV/api/FHIR/R4 | 
 |

 | 
 476 | 
 Clinicas Del Camino Real | 
 https://webprd.ochin.org/prd-fhir/CLINICAS/api/FHIR/R4 | 
 |

 | 
 397 | 
 CNMRI | 
 https://epproxy.bayhealth.org/FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 476 | 
 Coast Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCCHC/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Coastal Carolina Health Care | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/CCHC/api/FHIR/R4 | 
 |

 | 
 1718 | 
 Codman Square Health Center | 
 https://emerge-soap1.bmc.org/FHIR-PRD/HOME/api/FHIR/R4 | 
 |

 | 
 516 | 
 Cody Regional Health | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 405 | 
 Columbia Basin Hospital | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Columbia Community Mental Health | 
 https://webprd.ochin.org/prd-fhir/CCMH1/api/FHIR/R4 | 
 |

 | 
 405 | 
 Columbia Gorge Family Medicine | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Columbia River Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCRH/api/FHIR/R4 | 
 |

 | 
 2475 | 
 Columbia University Irving Medical Center | 
 https://epicproxy-pub.et1089.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 2373 | 
 Columbus Regional Health | 
 https://epicprdproxy.crh.org/FHIRPRD/HOME/api/FHIR/R4 | 
 |

 | 
 700 | 
 CommonSpirit - AR/GA/KY/TN/TX | 
 https://rpsouth.catholichealth.net/fhir/api/FHIR/R4 | 
 |

 | 
 700 | 
 CommonSpirit Health | 
 https://epicproxy.et1482.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 741 | 
 CommonSpirit Mountain Region | 
 https://epic-p-foreground.centura.org/prd-fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 CommuniCare+OLE | 
 https://webprd.ochin.org/prd-fhir/CCOLEMYCHART/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Health Care, Inc | 
 https://webprd.ochin.org/prd-fhir/CHCQCA/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Health Center of Fort Dodge | 
 https://webprd.ochin.org/prd-fhir/CHCFD/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Community Health Center of Franklin County | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Community Health Center of Lubbock | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Health Center of Southeastern Iowa | 
 https://webprd.ochin.org/prd-fhir/CHCSEIA/api/FHIR/R4 | 
 |

 | 
 922 | 
 Community Health Connections | 
 https://epicproxy.et0978.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 699 | 
 Community Health Network | 
 https://esp.ecommunity.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Health of Central Washington | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCHCW/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Community Health of South Florida | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 14009 | 
 Community Health Partners | 
 https://revproxy.bh.bozemanhealth.org/Interconnect-OAuth2-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Health Services, Inc | 
 https://webprd.ochin.org/prd-fhir/CHSIMYCHART/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Health Systems | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCHSOFWI/api/FHIR/R4 | 
 |

 | 
 405 | 
 Community Hospital for Anaconda | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2255 | 
 Community Medical Center | 
 https://epicproxy.et1031.epichosted.com/FHIRProxy/CMC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Medical Centers | 
 https://webprd.ochin.org/prd-fhir/CMCENTERS/api/FHIR/R4 | 
 |

 | 
 617 | 
 Community Medical Centers | 
 https://epicsoapprd.communitymedical.org/arr_fhir/api/FHIR/R4 | 
 |

 | 
 405 | 
 Community Memorial Healthcare | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 Community Memorial Hospital | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Community Mental Health Affiliates | 
 https://webprd.ochin.org/prd-fhir/CMHACC/api/FHIR/R4 | 
 |

 | 
 960 | 
 CommunityCare | 
 https://geisapi.geisinger.edu/FHIR_PROD/api/FHIR/R4 | 
 |

 | 
 9682 | 
 CommUnityCare | 
 https://epicproxy.et1164.epichosted.com/fhirproxy/CUC/api/FHIR/R4 | 
 |

 | 
 938 | 
 Communitycare PLAN | 
 https://mhssp.mhs.net/fhir/api/FHIR/R4 | 
 |

 | 
 13877 | 
 CommWell Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1005 | 
 Compassionate Care Medical Center | 
 https://epicproxy.et0502.epichosted.com/FhirProxy/CCMC/api/FHIR/R4 | 
 |

 | 
 982 | 
 Complete Cardiovascular Care | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 817 | 
 Concentra | 
 https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Concierge Health Partners | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 1011 | 
 Cone Health | 
 https://epsoap.conehealth.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 968 | 
 Conemaugh Health System | 
 https://epicproxy.et0962.epichosted.com/APIPROXYPRD/api/FHIR/R4 | 
 |

 | 
 1073 | 
 Confluence Health | 
 https://epicproxy.et0764.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 938 | 
 Connect PBC | 
 https://mhssp.mhs.net/fhir/api/FHIR/R4 | 
 |

 | 
 670 | 
 Connecticut Children's Medical Center | 
 https://epicproxy.connecticutchildrens.org/FHIR/api/FHIR/R4 | 
 |

 | 
 568 | 
 Connecticut Ear, Nose & Throat Associates | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 568 | 
 Connecticut GI | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 568 | 
 Connecticut Orthopaedics | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 877 | 
 Contra Costa Health Services | 
 https://icproxy.mycclink.org/proxy-FHIR/api/FHIR/R4 | 
 |

 | 
 427 | 
 Cook Children's | 
 https://cookicfg.cookchildrens.org/CookFHIR/api/FHIR/R4 | 
 |

 | 
 1128 | 
 Cooper | 
 https://epicproxy.et0578.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 409 | 
 Corewell Health West | 
 https://epicarr02.spectrumhealth.org/EpicFHIR/HOME/api/FHIR/R4 | 
 |

 | 
 862 | 
 Coteau des Prairie Medical Center | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1859 | 
 Cottage Health System | 
 https://eparp.sbch.org/FHIR/SBCH/api/FHIR/R4 | 
 |

 | 
 20774 | 
 County of San Mateo | 
 https://epicproxy.et1356.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 1752 | 
 Covenant Health | 
 https://carepath.health-partners.org/Proxy-FHIR/COV/api/FHIR/R4 | 
 |

 | 
 405 | 
 Covenant Health and Grace Clinic | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2285 | 
 Covenant HealthCare | 
 https://epichaiku.chs-mi.com/FHIRPROXY/api/FHIR/R4 | 
 |

 | 
 26387 | 
 Covington County Hospital | 
 https://epicproxy.et1453.epichosted.com/FHIRProxyPRD/COVINGTON/api/FHIR/R4 | 
 |

 | 
 22751 | 
 CoxHealth | 
 https://epicproxy.et1402.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 405 | 
 Credena Health | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Credena Health - Alaska | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Credena Health - Washington/Montana | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Crescent Community Health Center | 
 https://webprd.ochin.org/prd-fhir/CRESCENTCHC/api/FHIR/R4 | 
 |

 | 
 2154 | 
 Crossing Rivers Health | 
 https://scproxy.gundersenhealth.org/FHIRARR/GHS/api/FHIR/R4 | 
 |

 | 
 1367 | 
 Culicchia Neurological | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 405 | 
 Curry Health Network | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 355 | 
 Cuyuna Regional Medical Center | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 476 | 
 DAP | 
 https://webprd.ochin.org/prd-fhir/MYCHARTDAP/api/FHIR/R4 | 
 |

 | 
 339 | 
 Dartmouth | 
 https://edhwebportal.hitchcock.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 4099 | 
 DaVita Physician Solutions | 
 https://epicproxy.et1087.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 575 | 
 Dayton Children's Hospital | 
 https://appprd.childrensdayton.org/interconnect-prd-fhir/api/FHIR/R4 | 
 |

 | 
 337 | 
 DCO Public Health | 
 https://epicfe.unch.unc.edu/FHIR/DCOPUBLICHEALTH/api/FHIR/R4 | 
 |

 | 
 540 | 
 Deaconess | 
 https://eprp.deaconess.com/FHIR/api/FHIR/R4 | 
 |

 | 
 397 | 
 Dedicated to Women | 
 https://epproxy.bayhealth.org/FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 1278 | 
 Denver Health | 
 https://webservices.dhha.org/PRD-FHIR/DH/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Dickson Medical Associates | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/DMA/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Digestive Specialists PA | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 13877 | 
 District Health Care Services | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 355 | 
 District One Hospital | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 7852 | 
 Doctors on Duty | 
 https://epicproxy.et1146.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1718 | 
 DotHouse Health | 
 https://emerge-soap1.bmc.org/FHIR-PRD/HOME/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Douglas County Hospital | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 862 | 
 Douglas County Memorial Hospital | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Drexel | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 3825 | 
 Driscoll Children's Hospital | 
 https://hubble.dchstx.org/fhir/HOME/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Duffy Health Center | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 733 | 
 Duke University Health System | 
 https://health-apis.duke.edu/FHIR/api/FHIR/R4 | 
 |

 | 
 15361 | 
 Duly Health and Care | 
 https://epicproxy.et1296.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Eagle View Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTEAGLEVIEWHEALTH/api/FHIR/R4 | 
 |

 | 
 982 | 
 Ear, Nose, & Throat Surgical | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1311 | 
 East Adams Rural Hospital | 
 https://soapprod.multicare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 16090 | 
 East Cascade Women's Group | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/ECWG/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Eau Claire GI Associates – OakLeaf Medical Network | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 986 | 
 ECU Health | 
 https://prd-proxy.vidanthealth.com/FHIR/api/FHIR/R4 | 
 |

 | 
 1669 | 
 Eisenhower Health | 
 https://epicarr.emc.org/EMC_FHIR_PRD/HOME/api/FHIR/R4 | 
 |

 | 
 1834 | 
 El Camino | 
 https://rwebproxy.elcaminohospital.org/FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 1834 | 
 El Camino Hospital | 
 https://rwebproxy.elcaminohospital.org/FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 476 | 
 El Centro de Corazón | 
 https://webprd.ochin.org/prd-fhir/ECDC/api/FHIR/R4 | 
 |

 | 
 11545 | 
 El Rio Health | 
 https://epicproxy.et1240.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 16090 | 
 eleHealth | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Elevated Community Health | 
 https://webprd.ochin.org/prd-fhir/ELEVATEDCH/api/FHIR/R4 | 
 |

 | 
 476 | 
 Elica Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTEHC/api/FHIR/R4 | 
 |

 | 
 11179 | 
 Emory Healthcare | 
 https://epicrp-prd.eushc.org/OAUTH2-PRD/api/FHIR/R4 | 
 |

 | 
 2154 | 
 Emplify Health | 
 https://scproxy.gundersenhealth.org/FHIRARR/GHS/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Empower U | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2819 | 
 Endeavor Health | 
 https://epicprdproxy.nch.org/prd-fhir/api/FHIR/R4 | 
 |

 | 
 1456 | 
 Endeavor Health | 
 https://fhirprd.edward.org/fhirprd/api/FHIR/R4 | 
 |

 | 
 857 | 
 Endeavor Health – NorthShore University HealthSystem | 
 https://epicproxy.et0431.epichosted.com/FHIRProxyPRD/HOME/api/FHIR/R4 | 
 |

 | 
 568 | 
 Endoscopy Center of Connecticut | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 2727 | 
 Englewood | 
 https://epicproxy.et1073.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 897 | 
 Enloe Medical Center | 
 https://epicproxy.et1034.epichosted.com/FHIRProxy/STANDARD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Equitas Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTEQUITAS/api/FHIR/R4 | 
 |

 | 
 397 | 
 Eranga Cardiology | 
 https://epproxy.bayhealth.org/FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 1234 | 
 Erlanger Health System | 
 https://epicproxy.et0967.epichosted.com/FHIRProxy/EHS/api/FHIR/R4 | 
 |

 | 
 488 | 
 Eskenazi | 
 https://proxy.eskenazihealth.edu/FHIR-Proxy/HOME/api/FHIR/R4 | 
 |

 | 
 2054 | 
 Essentia Health | 
 https://m.essentiahealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1002 | 
 ETSU Health | 
 https://soap.wellmont.org/FHIRPRD/MYCHART/api/FHIR/R4 | 
 |

 | 
 960 | 
 Evangelical Community Hospital | 
 https://geisapi.geisinger.edu/FHIR_PROD/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Evara Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Everett Bone and Joint | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Evergreen Surgical – OakLeaf Medical Network | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 14326 | 
 EvergreenHealth | 
 https://epicproxy.et1270.epichosted.com/apiproxyprd/api/FHIR/R4 | 
 |

 | 
 6432 | 
 Evernorth Care Group | 
 https://epicarr.healthcare.cigna.com/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 6432 | 
 Evernorth Home-Based Care | 
 https://epicarr.healthcare.cigna.com/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 6432 | 
 Evernorth Workplace Care | 
 https://epicarr.healthcare.cigna.com/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 4248 | 
 Exact Sciences | 
 https://epicproxy.et1126.epichosted.com/FHIRProxy/EXACT/api/FHIR/R4 | 
 |

 | 
 405 | 
 Excelsior Family Medicine | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Fairchild Medical Center | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Fall Creek Internal Medicine | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/FCIM/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Family and Aging Center | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Family Care Health Centers of St. Louis | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 16543 | 
 Family Care Network | 
 https://epicproxy.fcn.net/fhir/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Family Christian Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 560 | 
 Family Health Center | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Family Health Center of Marshfield | 
 https://webprd.ochin.org/prd-fhir/FAMILYHEALTHCENTER/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Family Health Center of Worcester | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Family Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYERIE/api/FHIR/R4 | 
 |

 | 
 516 | 
 Family Health West | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 862 | 
 Family Healthcare | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 405 | 
 Family Medical Group | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 9833 | 
 FastMed | 
 https://epicproxy.et1190.epichosted.com/FHIRProxyPRD/FastMed/api/FHIR/R4 | 
 |

 | 
 476 | 
 Father Joe's Villages | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSVDP/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Fenway Health | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 397 | 
 First State Infectious Diseases | 
 https://epproxy.bayhealth.org/FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 1460 | 
 FirstHealth of the Carolinas | 
 https://epicrp.firsthealth.org/FHIR-PRD/FHMYCHART/api/FHIR/R4 | 
 |

 | 
 9392 | 
 Florida Advanced Gastroenterology Center | 
 https://mobile.adventhealth.com/oauth2-PRD/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Florida Community Health Centers | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 20718 | 
 Florida Health Care Plans | 
 https://epicproxy.et1359.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 982 | 
 FMOL Health | Our Lady of Lourdes | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 982 | 
 FMOL Health | Our Lady of the Angels | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 982 | 
 FMOL Health | Our Lady of the Lake | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 982 | 
 FMOL Health | Our Lady of the Lake Children's | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 982 | 
 FMOL Health | St. Dominic | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 982 | 
 FMOL Health | St. Francis | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Foot and Ankle Clinic – OakLeaf Medical Network | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/FAC/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Foothill Family Clinic | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/FFC/api/FHIR/R4 | 
 |

 | 
 13877 | 
 FoundCare | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 567 | 
 Franciscan Alliance | 
 https://ema.franciscanalliance.org/FHIR_PROXY/api/FHIR/R4/ | 
 |

 | 
 715 | 
 Franciscan Children's Hospital | 
 https://epicproxy.et1351.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 567 | 
 Franciscan HealthConnect | 
 https://ema.franciscanalliance.org/FHIR_PROXY/api/FHIR/R4/ | 
 |

 | 
 476 | 
 Franklin Primary Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTFPHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Friends of Family Health Center | 
 https://webprd.ochin.org/prd-fhir/FOFHEALTHCENTER/api/FHIR/R4 | 
 |

 | 
 492 | 
 Froedtert | 
 https://epicservicegw.froedtert.com/FHIRproxyPRD/api/FHIR/R4 | 
 |

 | 
 492 | 
 Froedtert South | 
 https://epicservicegw.froedtert.com/FHIRproxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Full Circle Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTFCH/api/FHIR/R4 | 
 |

 | 
 531 | 
 GA Carmichael | 
 https://soapproxy.umc.edu/FHIRProxy/GAC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Gardner Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTGHS/api/FHIR/R4 | 
 |

 | 
 591 | 
 Garnet Health | 
 https://epic.garnethealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 960 | 
 Geisinger | 
 https://geisapi.geisinger.edu/FHIR_PROD/api/FHIR/R4 | 
 |

 | 
 1544 | 
 Genesis | 
 https://fhir.genesishcs.org/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Genesis Community Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Gentle Pediatrics | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Gerald L. Ignace Indian Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTGLIIHC/api/FHIR/R4 | 
 |

 | 
 880 | 
 GHC | 
 https://linkpoint.ghcscw.com/Interconnect-PRD-FHIR/api/FHIR/R4 | 
 |

 | 
 355 | 
 Glencoe Regional Health Services | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 16570 | 
 Go East Medical Services | 
 https://epicproxy.et1332.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 27123 | 
 GoHealth Urgent Care | 
 https://epicproxy.et1462.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 8372 | 
 Golden Valley Health Centers | 
 https://ep-rps.gvhc.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 GoldenShore Medical | 
 https://webprd.ochin.org/prd-fhir/MYCHARTGSM/api/FHIR/R4 | 
 |

 | 
 540 | 
 Good Samaritan | 
 https://eprp.deaconess.com/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Grace Health | 
 https://webprd.ochin.org/prd-fhir/GRACEHEALTHKY/api/FHIR/R4 | 
 |

 | 
 9392 | 
 Grace Medical Home | 
 https://mobile.adventhealth.com/oauth2-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Gracelight Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTGCH/api/FHIR/R4 | 
 |

 | 
 574 | 
 Grady Health System | 
 https://surescripts.gmh.edu/OAuth2PRD/GHSMYC/api/FHIR/R4 | 
 |

 | 
 405 | 
 Grande Ronde | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1576 | 
 Greater Baltimore Medical Center | 
 https://eportal.gbmc.org/fhir/api/FHIR/R4 | 
 |

 | 
 405 | 
 Greater Orange County Ear, Nose, Throat, Head & Neck Surgeons | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Gritman Medical Center | 
 https://webprd.ochin.org/prd-fhir/GRITMAN/api/FHIR/R4 | 
 |

 | 
 1038 | 
 Guthrie | 
 https://fhir.guthrie.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 11215 | 
 GW University Medical Faculty Associates | 
 https://epicproxy.et1222.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 476 | 
 Habitat Health | 
 https://webprd.ochin.org/prd-fhir/HABITATHEALTH/api/FHIR/R4 | 
 |

 | 
 335 | 
 Hackensack Meridian Health | 
 https://mepic.hmhn.org/fhir/api/FHIR/R4 | 
 |

 | 
 26340 | 
 Halifax Hospital Medical Center | 
 https://epicproxy.et1393.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 746 | 
 Hannibal Regional Healthcare System | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Harbor Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTHH/api/FHIR/R4 | 
 |

 | 
 572 | 
 Harmony | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 26500 | 
 Harmony | 
 https://epicproxy.et1434.epichosted.com/APIPROXYPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Harmony Health Medical Clinic | 
 https://webprd.ochin.org/prd-fhir/MYHARMONYHEALTH/api/FHIR/R4 | 
 |

 | 
 904 | 
 Harney District Hospital | 
 https://epicproxy.et1030.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 2287 | 
 Harris County Public Health | 
 https://fhir.harrishealth.org/fhir/api/FHIR/R4 | 
 |

 | 
 2287 | 
 Harris Health | 
 https://fhir.harrishealth.org/fhir/api/FHIR/R4 | 
 |

 | 
 568 | 
 Hartford Healthcare | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 740 | 
 Hattiesburg | 
 https://soapprod.hattiesburgclinic.com/OAuth2/api/FHIR/R4 | 
 |

 | 
 26599 | 
 Hawaii Health Systems Corp | 
 https://epicproxy.et1454.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Hawaii Island Community Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 721 | 
 Hawaii Pacific Health | 
 https://webservices.hawaiipacifichealth.org/fhir/api/FHIR/R4 | 
 |

 | 
 1882 | 
 HCA | 
 https://mountainstarhealthfhirprd.app.medcity.net/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Head and Neck Associates of Orange County | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Health Care District of Palm Beach County | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 375 | 
 Health Center, powered by Mount Sinai | 
 https://epicsoapproxyprd.mountsinai.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 22582 | 
 Health First | 
 https://epicproxy.et1426.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Health First Family Care Center | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1222 | 
 Health Ventures | 
 https://emrproxy.mcfarlandclinic.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2287 | 
 Healthcare for the Homeless Houston | 
 https://fhir.harrishealth.org/fhir/api/FHIR/R4 | 
 |

 | 
 577 | 
 HealthPartners | 
 https://proxy.healthpartners.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 20328 | 
 HealthPoint | 
 https://epicproxy.et1395.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 HealthRIGHT 360 | 
 https://webprd.ochin.org/prd-fhir/MYCHARTHEALTHRIGHT360/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Healthy Living Heart and Vein | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 528 | 
 Heart of Ohio Family Health | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 2166 | 
 Heart of Texas | 
 https://epicrpx.shannonhealth.org/FHIR_ARR/api/FHIR/R4 | 
 |

 | 
 746 | 
 Heartland Health Services | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 1589 | 
 Helen Newberry Joy | 
 https://arrprod.midmichigan.net/ProdFHIR/api/FHIR/R4 | 
 |

 | 
 1525 | 
 Hemophilia Outreach Center | 
 https://scripts.prevea.com/FHIR-ARR-PRD/api/FHIR/R4 | 
 |

 | 
 1444 | 
 Hendricks Regional Health | 
 https://sehproxy.stelizabeth.com/arr-fhir/api/FHIR/R4 | 
 |

 | 
 1227 | 
 Hennepin | 
 https://hie.hcmed.org/FHIR/api/FHIR/R4 | 
 |

 | 
 812 | 
 Henry Ford Health | 
 https://fhir.hfhs.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 333 | 
 Heritage Medical Associates | 
 https://arr01.service.vumc.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 425 | 
 Highland District Hospital | 
 https://epicscripts.trihealth.com/fhirproxy/api/FHIR/R4 | 
 |

 | 
 425 | 
 Highland Health Providers | 
 https://epicscripts.trihealth.com/fhirproxy/api/FHIR/R4 | 
 |

 | 
 3757 | 
 Hill Physicians Medical Group | 
 https://epicproxy.et1013.epichosted.com/FHIRProxy/MYCHART/api/FHIR/R4 | 
 |

 | 
 623 | 
 Hillcrest | 
 https://epicproxy.ardenthealth.com/fhir/HMC/api/FHIR/R4 | 
 |

 | 
 912 | 
 Hillsdale Hospital | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Hilltown Community Health Center | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 9377 | 
 Hoag Memorial Hospital Presbyterian | 
 https://epicproxy.et1197.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 528 | 
 Hocking Valley | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Holyoke Health | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Homestead Community Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 572 | 
 Hometown Health Clinic | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 1670 | 
 Honor Health | 
 https://interconnect.honorhealth.com/Interconnect-FHIR-PRD/api/FHIR/R4/ | 
 |

 | 
 16991 | 
 Hope Digestive and Liver Disease Clinic | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 330 | 
 Hospital for Special Surgery | 
 https://epicproxy.et0927.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1525 | 
 Hospital Sisters Health System | 
 https://scripts.prevea.com/FHIR-ARR-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Hot Springs Health Program | 
 https://webprd.ochin.org/prd-fhir/MYCHARTHSH/api/FHIR/R4 | 
 |

 | 
 323 | 
 Hot Springs Pediatric Clinic | 
 https://epicproxy.et1036.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Houston Foot and Ankle Professional Group | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 1224 | 
 Houston Methodist | 
 https://epicproxy.et0922.epichosted.com/FHIRProxy/HM/api/FHIR/R4 | 
 |

 | 
 476 | 
 Howard Brown Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTHBH/api/FHIR/R4 | 
 |

 | 
 1111 | 
 HPI | 
 https://FHIR.Integrisok.com/Interconnect-FHIR/api/FHIR/R4/ | 
 |

 | 
 1525 | 
 HSHS Medical Group | 
 https://scripts.prevea.com/FHIR-ARR-PRD/api/FHIR/R4 | 
 |

 | 
 709 | 
 Huntington Hospital | 
 https://cslinkmobile.csmc.edu/fhirproxy/api/FHIR/R4 | 
 |

 | 
 808 | 
 Hurley Medical Center | 
 https://fhir.hurleymc.com/fhir/api/FHIR/R4 | 
 |

 | 
 355 | 
 Hutchinson Health | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 11049 | 
 Illinois Bone & Joint Institute | 
 https://epicproxy.et1195.epichosted.com/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Immanuel PACE | 
 https://webprd.ochin.org/prd-fhir/IMMANUEL/api/FHIR/R4 | 
 |

 | 
 476 | 
 Indian Health Board of Minneapolis | 
 https://webprd.ochin.org/prd-fhir/IHB/api/FHIR/R4 | 
 |

 | 
 476 | 
 Indian Health Center of Santa Clara Valley | 
 https://webprd.ochin.org/prd-fhir/MYCHARTIHCSCV/api/FHIR/R4 | 
 |

 | 
 476 | 
 Indian Health Council | 
 https://webprd.ochin.org/prd-fhir/INDIANHEALTH/api/FHIR/R4 | 
 |

 | 
 11509 | 
 Infectious Disease Associates of Naples | 
 https://epicproxy.et1233.epichosted.com/FHIRProxy/AFFILIATE/api/FHIR/R4 | 
 |

 | 
 476 | 
 Infinity Health Care | 
 https://webprd.ochin.org/prd-fhir/WEAREINFINITYHEALTH/api/FHIR/R4 | 
 |

 | 
 1047 | 
 Infirmary | 
 https://ssproxyprod.infirmaryhealth.org/epicFHIR/MYCPRD/api/FHIR/R4 | 
 |

 | 
 14417 | 
 InnovAge | 
 https://rp.innovage.com/OAUTH2-PRD/INNV/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Innovista Medical Center | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/INV/api/FHIR/R4 | 
 |

 | 
 561 | 
 Inova Health System | 
 https://epicproxy.et0816.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 1111 | 
 INTEGRIS Health | 
 https://FHIR.Integrisok.com/Interconnect-FHIR/api/FHIR/R4/ | 
 |

 | 
 11509 | 
 Integris Physician Group | 
 https://epicproxy.et1233.epichosted.com/FHIRProxy/AFFILIATE/api/FHIR/R4 | 
 |

 | 
 476 | 
 InterCommunity Health Care | 
 https://webprd.ochin.org/prd-fhir/MYCHARTINTERCOMMUNITY/api/FHIR/R4 | 
 |

 | 
 516 | 
 Intermountain Health | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 405 | 
 International Health Community Services | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 585 | 
 Iowa Specialty Hospitals and Clinics | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 912 | 
 Iridescent Health | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Island Health Care | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 Jacobson Memorial Hospital | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 405 | 
 Jamestown Family Health Clinic | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 Jamestown Regional Medical Center | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 JAMHI | 
 https://webprd.ochin.org/prd-fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Jane Pauley Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTJPCHC/api/FHIR/R4 | 
 |

 | 
 585 | 
 Jefferson County Health Center | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Jefferson Healthcare | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Jessie Trice Community Health System | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Jewish Community Free Clinic | 
 https://webprd.ochin.org/prd-fhir/JEWISHFREECLINIC/api/FHIR/R4 | 
 |

 | 
 16991 | 
 JOHN IKE, MD, MPH, PA | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 460 | 
 John Muir Health | 
 https://fhir.johnmuirhealth.com/fhir-prd/JMH/api/FHIR/R4 | 
 |

 | 
 7852 | 
 Johnny Blanchard, MD | 
 https://epicproxy.et1146.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 429 | 
 Johns Hopkins Medicine | 
 https://epicproxy.et0842.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Johnson Memorial Health Services | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Jordan Valley Community Health Center | 
 https://webprd.ochin.org/prd-fhir/JORDANVALLEYMYCHART/api/FHIR/R4 | 
 |

 | 
 2539 | 
 JPS Health Network | 
 https://oauth2.revprxprd.jpshealth.org/epoauth2/api/FHIR/R4 | 
 |

 | 
 20215 | 
 Jupiter Medical Center | 
 https://epicrp.jupitermed.com/oauth2-prd/api/FHIR/R4 | 
 |

 | 
 16991 | 
 JW Family Medicine | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 405 | 
 Kadlec Health System | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Kahuku Medical Center | 
 https://webprd.ochin.org/prd-fhir/KAHUKUMEDICALCENTER/api/FHIR/R4 | 
 |

 | 
 6267 | 
 Kaiser Permanente - Colorado | 
 https://fhir.kp.org/service/ptnt_care/EpicEdiFhirRoutingSvc/v2014/esb-envlbl/140/api/FHIR/R4/ | 
 |

 | 
 6265 | 
 Kaiser Permanente - Georgia | 
 https://fhir.kp.org/service/ptnt_care/EpicEdiFhirRoutingSvc/v2014/esb-envlbl/200/api/FHIR/R4/ | 
 |

 | 
 6268 | 
 Kaiser Permanente - Hawaii | 
 https://fhir.kp.org/service/ptnt_care/EpicEdiFhirRoutingSvc/v2014/esb-envlbl/130/api/FHIR/R4/ | 
 |

 | 
 6269 | 
 Kaiser Permanente - Mid-Atlantic | 
 https://FHIR.KP.ORG/service/ptnt_care/EpicEdiFhirRoutingSvc/v2014/esb-envlbl/170/api/FHIR/R4 | 
 |

 | 
 6270 | 
 Kaiser Permanente - Northern California | 
 https://FHIR.KP.ORG/service/ptnt_care/EpicEdiFhirRoutingSvc/v2014/esb-envlbl/326/api/FHIR/R4/ | 
 |

 | 
 6264 | 
 Kaiser Permanente - Northwest | 
 https://FHIR.KP.ORG/service/ptnt_care/EpicEdiFhirRoutingSvc/v2014/esb-envlbl/190/api/FHIR/R4/ | 
 |

 | 
 6271 | 
 Kaiser Permanente - Southern California | 
 https://fhir.kp.org/service/ptnt_care/EpicEdiFhirRoutingSvc/v2014/esb-envlbl/226/api/FHIR/R4/ | 
 |

 | 
 1723 | 
 Kaiser Permanente - Washington | 
 https://fhir.kp.org/Interconnect-FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 560 | 
 Kalamazoo College | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 560 | 
 Kalamazoo Foot Surgery | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1091 | 
 Kelsey-Seybold | 
 https://ssrx.ksnet.com/FHIRproxy/MKO/api/FHIR/R4 | 
 |

 | 
 6133 | 
 Kennedy Krieger Institute | 
 https://epicproxy.et1095.epichosted.com/FHIRProxy/KKI/api/FHIR/R4 | 
 |

 | 
 476 | 
 Kenosha Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTKCHC/api/FHIR/R4 | 
 |

 | 
 1759 | 
 Kettering | 
 https://KHNARR.KETTHEALTH.COM/FHIR-PROD/api/FHIR/R4 | 
 |

 | 
 14997 | 
 KeyCare | 
 https://epicproxy.et1284.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 472 | 
 Keystone Health | 
 https://interconnect.wellspan.org/interconnect-prd-oauth2/api/FHIR/R4 | 
 |

 | 
 572 | 
 Khumalo Foot and Ankle Clinic | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 16991 | 
 Kids First Pediatrics | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 476 | 
 King County Public Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTKINGCOUNTY/api/FHIR/R4 | 
 |

 | 
 476 | 
 Kintegra Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTKINTEGRA/api/FHIR/R4 | 
 |

 | 
 405 | 
 Kinwell | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 Kittson Healthcare | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Ko-Kwel Wellness Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTKOKWELWELLNESS/api/FHIR/R4 | 
 |

 | 
 1311 | 
 Kootenai Health | 
 https://soapprod.multicare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 La Casa Family Health Centers | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 La Clinica | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLACLINICAHEALTH/api/FHIR/R4 | 
 |

 | 
 476 | 
 La Clinica | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLCLR/api/FHIR/R4 | 
 |

 | 
 2166 | 
 La Esperanza Clinic | 
 https://epicrpx.shannonhealth.org/FHIR_ARR/api/FHIR/R4 | 
 |

 | 
 476 | 
 La Pine Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLPCHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Laguna Beach | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLBCC/api/FHIR/R4 | 
 |

 | 
 982 | 
 Lake Charles Memorial Health System | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 Lake Region Healthcare | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lake Superior Community Health Center | 
 https://webprd.ochin.org/prd-fhir/LSCHC/api/FHIR/R4 | 
 |

 | 
 13715 | 
 Lakeland Regional Health | 
 https://epicapp.mylrh.org/OAuth2/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lakeshore Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLCHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lakewood Health System | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLHS/api/FHIR/R4 | 
 |

 | 
 1367 | 
 Lallie Kemp Regional Medical Center | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 521 | 
 Lancaster | 
 https://epicproxy.lghealth.org/fhirproxy/HOMEPAGE/api/FHIR/R4 | 
 |

 | 
 982 | 
 Lane Regional Medical Center | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lawndale Christian Health Center | 
 https://webprd.ochin.org/prd-fhir/MYLAWNDALE/api/FHIR/R4 | 
 |

 | 
 1367 | 
 LCMC Health | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 2560 | 
 Lee Health Systems, Inc | 
 https://epicedi.leememorial.org/FHIR-prd/api/FHIR/R4/ | 
 |

 | 
 13877 | 
 Legacy Community Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1154 | 
 Legacy Health System | 
 https://LHSPDXFHIRPRD.LHS.ORG/FHIR/api/FHIR/R4 | 
 |

 | 
 434 | 
 Lehigh Valley Health Network | 
 https://proxy.lvh.com/FHIR/api/FHIR/R4 | 
 |

 | 
 2244 | 
 Leon Medical Centers | 
 https://prodinterconnect.leonmedicalcenters.com/FHIR-PRD/MYLEON/api/FHIR/R4 | 
 |

 | 
 1283 | 
 Lexington County Health Services | 
 https://lmcrcs.lexmed.com/FHIR/api/FHIR/R4 | 
 |

 | 
 9332 | 
 Licking Memorial Health System | 
 https://epicproxy.et1168.epichosted.com/FHIRProxy/LMHPRD/api/FHIR/R4 | 
 |

 | 
 528 | 
 LifeCare Alliance | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 476 | 
 LifeLong Medical | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLLMC/api/FHIR/R4 | 
 |

 | 
 862 | 
 Lifescape | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 392 | 
 Lifespan | 
 https://lsepprdsoap.lifespan.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Lincoln Hospital & Clinics | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2255 | 
 Lincoln Medical Education Partnership | 
 https://epicproxy.et1031.epichosted.com/FHIRProxy/LMEP/api/FHIR/R4 | 
 |

 | 
 1116 | 
 Lindner Center of Hope | 
 https://epic-soap.uchealth.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 912 | 
 Linke Urology and Robotics | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Little Traverse Bay Bands | 
 https://webprd.ochin.org/prd-fhir/LTBBHEALTH/api/FHIR/R4 | 
 |

 | 
 687 | 
 Loma Linda | 
 https://prd.lluh.org/fhir/api/FHIR/R4 | 
 |

 | 
 1088 | 
 Longstreet Clinic | 
 https://wpprod.nghs.com/fhir/NGHS/api/FHIR/R4 | 
 |

 | 
 982 | 
 Louisiana Orthopaedic Specialists | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 623 | 
 Lovelace Health | 
 https://epicproxy.ardenthealth.com/fhir/LHS/api/FHIR/R4 | 
 |

 | 
 15680 | 
 Lowell Community Health Center | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lower Lights Christian Health Center | 
 https://webprd.ochin.org/prd-fhir/LOWERLIGHTSHEALTH/api/FHIR/R4 | 
 |

 | 
 1367 | 
 LSU Health Network | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 777 | 
 Lumina | 
 https://fhir.metrohealth.org/fhir_prd/api/FHIR/R4 | 
 |

 | 
 934 | 
 Luminis Health | 
 https://epicarr.aahs.org/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lummi Tribal Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLTHS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lynn Community Health Center | 
 https://webprd.ochin.org/prd-fhir/LYNNCHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Lyon Martin | 
 https://webprd.ochin.org/prd-fhir/MYCHARTLMHS/api/FHIR/R4 | 
 |

 | 
 798 | 
 M Health Fairview | 
 https://sfd.fairview.org/FHIR/api/FHIR/R4/ | 
 |

 | 
 16991 | 
 Macie Medical | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 1589 | 
 Mackinac Straits Health System | 
 https://arrprod.midmichigan.net/ProdFHIR/api/FHIR/R4 | 
 |

 | 
 528 | 
 Madison Health | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 476 | 
 Madison Regional Health System | 
 https://webprd.ochin.org/prd-fhir/MRHSMYCHART/api/FHIR/R4 | 
 |

 | 
 982 | 
 Madison Ridgeland Medical Clinic | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Maeville Pediatrics | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 26387 | 
 Magee General Hospital | 
 https://epicproxy.et1453.epichosted.com/FHIRProxyPRD/MAGEE/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Magnolia Lane Pediatrics | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 862 | 
 Mahnomen Health Center | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 2459 | 
 Main Line Health | 
 https://epicproxy.et1007.epichosted.com/FHIRProxy/LAUNCH/api/FHIR/R4 | 
 |

 | 
 972 | 
 MaineHealth | 
 https://fhir.mainehealth.org/FHIRPRD/api/FHIR/R4/ | 
 |

 | 
 13877 | 
 Malama I Ke Ola Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Maple City Health Care Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMCHCC/api/FHIR/R4 | 
 |

 | 
 687 | 
 Maren Medical Group | 
 https://prd.lluh.org/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Marimn Health | 
 https://webprd.ochin.org/prd-fhir/MARIMNHEALTH/api/FHIR/R4 | 
 |

 | 
 476 | 
 Marin Community Clinic | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMCC/api/FHIR/R4 | 
 |

 | 
 940 | 
 Marshall Medical Center | 
 https://emrrp.ucdmc.ucdavis.edu/FHIR/api/FHIR/R4 | 
 |

 | 
 2285 | 
 Mary Free Bed | 
 https://epichaiku.chs-mi.com/FHIRPROXY/api/FHIR/R4 | 
 |

 | 
 2701 | 
 Mary Washington | 
 https://epicproxy.et1055.epichosted.com/FHIRProxy/MWHC/api/FHIR/R4 | 
 |

 | 
 547 | 
 Maryland Primary Care Physicians | 
 https://fhir.umm.edu/fhir/api/FHIR/R4/ | 
 |

 | 
 404 | 
 Mass General Brigham | 
 https://ws-interconnect-fhir.partners.org/Interconnect-FHIR-MU-PRD/api/FHIR/R4 | 
 |

 | 
 529 | 
 Mayo Clinic | 
 https://tls.mcc.apix.mayo.edu/epic-fhir/api/FHIR/R4 | 
 |

 | 
 572 | 
 MCAM | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 476 | 
 MCHC Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMC/api/FHIR/R4 | 
 |

 | 
 862 | 
 McKenzie County Healthcare | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 14369 | 
 McLeod Health | 
 https://epicproxy.et1267.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 982 | 
 MEA Medical Clinic | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Med Centro | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1014 | 
 MediSys Health Network | 
 https://eprescribe-p.medisys.org/fhir-prd/MED/api/FHIR/R4 | 
 |

 | 
 528 | 
 Memorial Health | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 1882 | 
 Memorial Health | 
 https://memorialhealthfhirprd.app.medcity.net/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 938 | 
 Memorial Healthcare System | 
 https://mhssp.mhs.net/fhir/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Memorial Hermann Health System | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MYMH/api/FHIR/R4 | 
 |

 | 
 10147 | 
 Memorial Hospital and Healthcare Center | 
 https://arrprd.mhhcc.org/OAuth2/api/FHIR/R4 | 
 |

 | 
 516 | 
 Memorial Regional Health | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 18574 | 
 Memorial Sloan Kettering Cancer Center | 
 https://epicproxy.et1353.epichosted.com/APIPROXYPRD/api/FHIR/R4 | 
 |

 | 
 342 | 
 MemorialCare | 
 https://epicproxy.et0498.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 10933 | 
 Men's Mental Health | 
 https://epicproxy.et1206.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 528 | 
 Mercer Health | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 403 | 
 Mercy | 
 https://epic-fhir.mercy.net/prdfhirstl/api/FHIR/R4/ | 
 |

 | 
 476 | 
 Mercy Care | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSJMC/api/FHIR/R4 | 
 |

 | 
 1752 | 
 Mercy Health | 
 https://carepath.health-partners.org/Proxy-FHIR/MYCHART/api/FHIR/R4 | 
 |

 | 
 1916 | 
 Mercy Health Services | 
 https://epicproxy.et0876.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 831 | 
 Mercy Medical Center | 
 https://eproxy.mercycare.org/oauth2/api/FHIR/R4/ | 
 |

 | 
 2542 | 
 Meritus | 
 https://epicproxy.et1062.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 2407 | 
 Methodist Health System | 
 https://epcapp.mhd.com/arr-prd-fhir/api/FHIR/R4 | 
 |

 | 
 1158 | 
 Methodist Hospitals | 
 https://arr.methodisthospitals.org/FHIR/api/FHIR/R4 | 
 |

 | 
 19299 | 
 Methodist Le Bonheur Healthcare | 
 https://epicproxy.et1342.epichosted.com/APIProxyPRD/MLH/api/FHIR/R4 | 
 |

 | 
 403 | 
 Metro Imaging | 
 https://epic-fhir.mercy.net/prdfhirstl/api/FHIR/R4/ | 
 |

 | 
 777 | 
 MetroHealth OH | 
 https://fhir.metrohealth.org/fhir_prd/api/FHIR/R4 | 
 |

 | 
 1983 | 
 MHS | 
 https://epicproxy.mhsjvl.org/FHIRproxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Miami Beach Community Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 6038 | 
 Middlesex Health | 
 https://epicproxy.et1124.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 17282 | 
 Midwestern University Clinics | 
 https://epicproxy.et1329.epichosted.com/APIProxyPRD/HOME/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Mille Lacs Band of Ojibwe | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Milwaukee Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMHS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Minidoka Memorial Hospital | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMINIDOKA/api/FHIR/R4 | 
 |

 | 
 1563 | 
 Minneapolis Clinic of Neurology MyChart | 
 https://minerva.northmemorial.com/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Minnesota Community Care | 
 https://webprd.ochin.org/prd-fhir/MCC/api/FHIR/R4 | 
 |

 | 
 1829 | 
 Minute Clinic | 
 https://retailepicfhir.cvshealth.com/FhirProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Mission Neighborhood Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMNHC/api/FHIR/R4 | 
 |

 | 
 572 | 
 Mississippi Pediatric Endocrine Care, PLLC | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 531 | 
 Mississippi State Department of Health | 
 https://soapproxy.umc.edu/FHIRProxy/MSDH/api/FHIR/R4 | 
 |

 | 
 405 | 
 Missoula Surgical Associates | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Missouri Ozarks | 
 https://webprd.ochin.org/prd-fhir/MISSOURIOZARKS/api/FHIR/R4 | 
 |

 | 
 572 | 
 Mitchell Family Medicine and The Ark Children's Clinic | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 3236 | 
 Mohawk Valley Health System | 
 https://fhir.mvhealthsystem.org/FHIRproxy/MVHS/api/FHIR/R4 | 
 |

 | 
 3084 | 
 Molina Healthcare | 
 https://epicproxy.et1057.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 912 | 
 Monarch Medicine | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 3049 | 
 Montage Health | 
 https://epicproxy.et1058.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 947 | 
 Montefiore Health System, Inc | 
 https://soapepic.montefiore.org/FhirProxyPrd/api/FHIR/R4 | 
 |

 | 
 476 | 
 Monterey County Health Department Clinic Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMCHD/api/FHIR/R4 | 
 |

 | 
 1600 | 
 Monument Health | 
 https://ehrmobile.monument.health/interconnect-prd-fhir/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Moonat Med Associates | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 2246 | 
 Morehouse Medicine | 
 https://epicproxy.et0905.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 14523 | 
 Mosaic Life Care | 
 https://epicproxy.et1274.epichosted.com/FHIRproxy/HOME/api/FHIR/R4 | 
 |

 | 
 476 | 
 Mosaic Medical | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMOSAIC/api/FHIR/R4 | 
 |

 | 
 2155 | 
 Mount Sinai Florida | 
 https://epicfhir.msmc.com/proxysite-prd/api/FHIR/R4 | 
 |

 | 
 375 | 
 Mount Sinai New York - Concierge Care | 
 https://epicsoapproxyprd.mountsinai.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Mountain Valleys Health Centers | 
 https://webprd.ochin.org/prd-fhir/MOUNTAINVALLEYSHEALTHCENTERS/api/FHIR/R4 | 
 |

 | 
 1948 | 
 Mountain West Surgical Specialists | 
 https://soap.crmcwy.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 623 | 
 Mountainside Medical Center | 
 https://epicproxy.ardenthealth.com/fhir/MMC/api/FHIR/R4 | 
 |

 | 
 375 | 
 MountSinai | 
 https://epicsoapproxyprd.mountsinai.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 1367 | 
 MRI of Louisiana | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 793 | 
 MTOSC | 
 https://epicproxy.et1015.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 403 | 
 MTS | 
 https://epic-fhir.mercy.net/prdfhirstl/api/FHIR/R4/ | 
 |

 | 
 1311 | 
 MultiCare | 
 https://soapprod.multicare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Multnomah County Health Department | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMULTCO/api/FHIR/R4 | 
 |

 | 
 862 | 
 Murray County Medical Center | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 996 | 
 MUSC Health | 
 https://fhirprod.musc.edu/fhirprod/api/FHIR/R4/ | 
 |

 | 
 13552 | 
 Muscogee Creek Nation | 
 https://epicproxy.et1221.epichosted.com/FHIRProxy/MCNDH/api/FHIR/R4 | 
 |

 | 
 476 | 
 Muslim Community and Health Care | 
 https://webprd.ochin.org/prd-fhir/MYCHARTMCHCWI/api/FHIR/R4 | 
 |

 | 
 16090 | 
 MY DR NOW | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/MDN/api/FHIR/R4 | 
 |

 | 
 434 | 
 MyConnect Health Portal | 
 https://proxy.lvh.com/FHIR/api/FHIR/R4 | 
 |

 | 
 1589 | 
 MyMichigan Health | 
 https://arrprod.midmichigan.net/ProdFHIR/api/FHIR/R4 | 
 |

 | 
 585 | 
 Myrtue Medical Center | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 516 | 
 National Jewish Health | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 850 | 
 Nationwide Children's Hospital | 
 https://hkc.nationwidechildrens.org/FHIR/MYCHART/api/FHIR/R4 | 
 |

 | 
 476 | 
 Native American Community Clinic | 
 https://webprd.ochin.org/prd-fhir/NACC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Native American Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTNAHC/api/FHIR/R4 | 
 |

 | 
 11509 | 
 NCH Healthcare System | 
 https://epicproxy.et1233.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Nehalem Bay Health Center | 
 https://webprd.ochin.org/prd-fhir/NEHALEMBAYHEALTH/api/FHIR/R4 | 
 |

 | 
 476 | 
 Neighborcare Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTNCH/api/FHIR/R4 | 
 |

 | 
 1861 | 
 NeighborHealth | 
 https://host8.ebnhc.org/FHIR/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Neighborhood Family Medicine | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/BKT/api/FHIR/R4 | 
 |

 | 
 476 | 
 Neighborhood Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTNHC/api/FHIR/R4 | 
 |

 | 
 982 | 
 Neighborhood Health Clinic | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 861 | 
 Nemours Children's Health | 
 https://iconnect.nemours.org/fhir/NEMOURS/api/FHIR/R4 | 
 |

 | 
 13877 | 
 NeoMed Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 902 | 
 Neuroscience Group | 
 https://arr.thedacare.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Nevada Health Centers | 
 https://webprd.ochin.org/prd-fhir/NVHC/api/FHIR/R4 | 
 |

 | 
 15680 | 
 New Bedford Community Health | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2255 | 
 New Life Clinic | 
 https://epicproxy.et1031.epichosted.com/FHIRProxy/NLC/api/FHIR/R4 | 
 |

 | 
 2475 | 
 New York Presbyterian | 
 https://epicproxy-pub.et1089.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 405 | 
 Newport Hospital & Health Services | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1589 | 
 Nimkee | 
 https://arrprod.midmichigan.net/ProdFHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 NOAH | 
 https://webprd.ochin.org/prd-fhir/NOAHHELPS/api/FHIR/R4 | 
 |

 | 
 16340 | 
 NOMS | 
 https://prdproxy.nomshealthcare.com/PRD-OAuth2/NOMS/api/FHIR/R4 | 
 |

 | 
 405 | 
 Nor-Lea Hospital District | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 20007 | 
 North Carolina Department of Health and Human Services | 
 https://epicproxy.et1364.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 16570 | 
 North East Medical Services | 
 https://epicproxy.et1332.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 North Lakes | 
 https://webprd.ochin.org/prd-fhir/MYCHARTNORTHLAKES/api/FHIR/R4 | 
 |

 | 
 1563 | 
 North Memorial | 
 https://minerva.northmemorial.com/fhir/api/FHIR/R4 | 
 |

 | 
 4211 | 
 North Mississippi Health Services | 
 https://eiclbext.nmhs.net/interconnect-generaloauth2services-prd/api/FHIR/R4 | 
 |

 | 
 1199 | 
 North Oaks Health System | 
 https://soapproxyprd.northoaks.org/NOHSFHIR/NOHS/api/FHIR/R4 | 
 |

 | 
 405 | 
 North Olympic Healthcare Network | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 15680 | 
 North Shore Community Health | 
 https://epicproxy.et1290.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1088 | 
 Northeast Georgia Health System | 
 https://wpprod.nghs.com/fhir/NGHS/api/FHIR/R4 | 
 |

 | 
 18931 | 
 Northwell Health | 
 https://call.api.northwell.io/epic-proxy/api/fhir/R4/ | 
 |

 | 
 19520 | 
 Northwest Orthopaedic Specialists | 
 https://epicproxy.et4006.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 1146 | 
 Northwestern Medicine | 
 https://nmepicproxy.nm.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 802 | 
 Norton Healthcare | 
 https://epicproxy.et0819.epichosted.com/APIPROXYPRD/Norton/api/FHIR/R4 | 
 |

 | 
 362 | 
 Novant | 
 https://epicproxy.et0798.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 362 | 
 Novant Health Partners | 
 https://epicproxy.et0798.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Nurture Women's Care | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 890 | 
 NYC Health and Hospitals | 
 https://epicproxypda.nychhc.org/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 635 | 
 NYU Langone | 
 https://epicfhir.nyumc.org/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 16090 | 
 OakLeaf Clinics – OakLeaf Medical Network | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/OAK/api/FHIR/R4 | 
 |

 | 
 405 | 
 Ocean Beach Hospital & Medical Center | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 OCHIN | 
 https://webprd.ochin.org/prd-fhir/MYCHART/api/FHIR/R4 | 
 |

 | 
 1927 | 
 Ochsner Health System | 
 https://myc.ochsner.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1927 | 
 Ochsner Health System Digital Medicine | 
 https://myc.ochsner.org/FHIR/api/FHIR/R4 | 
 |

 | 
 20088 | 
 Ohio Department of Behavioral Health | 
 https://epicproxy.et1316.epichosted.com/APIPROXYPRD/api/FHIR/R4 | 
 |

 | 
 1393 | 
 OhioHealth | 
 https://ccpintconfg.ohiohealth.com/Interconnect-PRD-OAUTH2/api/FHIR/R4 | 
 |

 | 
 19460 | 
 Oklahoma Heart Hospital | 
 https://epicrp.okheart.com/Oauth2Proxy/MYCHART/api/FHIR/R4 | 
 |

 | 
 623 | 
 Oklahoma Heart Institute | 
 https://epicproxy.ardenthealth.com/fhir/OHI/api/FHIR/R4 | 
 |

 | 
 1310 | 
 Oklahoma State University | 
 https://eprdsoap000.saintfrancis.Com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 3344 | 
 Olmsted Medical Center | 
 https://epicproxy.et1077.epichosted.com/APIPROXYPRD/HOME/api/FHIR/R4 | 
 |

 | 
 405 | 
 Olympic Medical Center | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 On Lok | 
 https://webprd.ochin.org/prd-fhir/MYCHARTOL/api/FHIR/R4 | 
 |

 | 
 676 | 
 One Brooklyn Health System | 
 https://epicproxy.et0883.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 One Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTOCH/api/FHIR/R4 | 
 |

 | 
 476 | 
 One Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTOCHOR/api/FHIR/R4 | 
 |

 | 
 410 | 
 OneChart | 
 https://ocsoapprd.nebraskamed.com/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 2204 | 
 Onvida | 
 https://yrmccare1.yumaregional.org/FHIR/Onvida/api/FHIR/R4 | 
 |

 | 
 476 | 
 Open Door Health Center | 
 https://webprd.ochin.org/prd-fhir/ODHCMYCHART/api/FHIR/R4 | 
 |

 | 
 476 | 
 OpenDoor Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTOPENDOOR/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Optimcurea Renal and Vascular Access Care | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 991 | 
 Optum Care Washington | 
 https://fhir.myeverettclinic.com/fhir/EVERETT/api/FHIR/R4 | 
 |

 | 
 6733 | 
 Optum Medical Care of Inland Empire and San Diego | 
 https://epicproxy.et1038.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Orange Blossom Family Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 Orange City Area Health System | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 405 | 
 Orange County Neurosurgical Associates | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Orange County Thoracic and Cardiovascular Surgeons | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 838 | 
 Oregon Health and Science University | 
 https://epicmobile.ohsu.edu/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 405 | 
 Oregon Heart Center | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 6210 | 
 Orlando Health | 
 https://epicproxy.et1131.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 10750 | 
 OrthoCarolina | 
 https://epwebapps.orthocarolina.com/fhir-prd/api/FHIR/R4 | 
 |

 | 
 597 | 
 Orthopaedic & Spine Center of the Rockies | 
 https://ss.uch.edu/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 568 | 
 Orthopedic Associates of Hartford | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 793 | 
 OrthoVirginia | 
 https://epicproxy.et1015.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 Ortonville Area Health Services | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 13552 | 
 Osage Nation Health System | 
 https://epicproxy.et1221.epichosted.com/FHIRProxy/OSAGE/api/FHIR/R4 | 
 |

 | 
 476 | 
 Osceola Medical Center | 
 https://webprd.ochin.org/prd-fhir/OMC/api/FHIR/R4 | 
 |

 | 
 746 | 
 OSF HealthCare | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 9511 | 
 OU Health | 
 https://epicproxy.et1181.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 982 | 
 Our Lady of the Lake LSU | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Outer Cape Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTOCHS/api/FHIR/R4 | 
 |

 | 
 777 | 
 Ovatient | 
 https://fhir.metrohealth.org/fhir_prd/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Over the Moon Pediatrics | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 759 | 
 Overlake | 
 https://sfd.overlakehospital.org/FHIRproxy/POSM/api/FHIR/R4 | 
 |

 | 
 1702 | 
 Owensboro | 
 https://fhir.omhs.org/rp-prd-fhir/api/FHIR/R4 | 
 |

 | 
 572 | 
 Oxford Neurology | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 405 | 
 Pacific Medical Center | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Pacific University Oregon | 
 https://webprd.ochin.org/prd-fhir/MYCHARTPUO/api/FHIR/R4 | 
 |

 | 
 874 | 
 Packard Health | 
 https://arrprd.metrohealth.net/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Palouse Specialty Physicians | 
 https://webprd.ochin.org/prd-fhir/PSP/api/FHIR/R4 | 
 |

 | 
 893 | 
 Parkland | 
 https://pmh-vmhaiku-01.pmh.org/FHIR/PARKLAND/api/FHIR/R4 | 
 |

 | 
 912 | 
 Parkview Health | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 902 | 
 Partnership Community Health | 
 https://arr.thedacare.org/FHIR/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Partnership Health Center | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 623 | 
 Pascack Valley Medical Center | 
 https://epicproxy.ardenthealth.com/fhir/PVC/api/FHIR/R4 | 
 |

 | 
 912 | 
 Paulding County Hospital | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 845 | 
 PeaceHealth | 
 https://soapproxy.peacehealth.org/FHIRProxy/PeaceHealth/api/FHIR/R4 | 
 |

 | 
 983 | 
 Peak Health | 
 https://apps.mywvuchart.com/FHIRproxy/WVUM/api/FHIR/R4 | 
 |

 | 
 476 | 
 Peak Vista | 
 https://webprd.ochin.org/prd-fhir/PEAKVISTA/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Pearland Family Wellness Clinic | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Pediatric Digestive Care | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 1436 | 
 Pediatric Physicians' Organization at Children's | 
 https://ppocrp.chppoc.org/fhir-external-prd/api/FHIR/R4 | 
 |

 | 
 754 | 
 PediaTrust | 
 https://epicproxy.et0301.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 346 | 
 Penn Medicine | 
 https://ssproxy.pennhealth.com/PRD-FHIR/HOME/api/FHIR/R4 | 
 |

 | 
 1367 | 
 Pennington Biomedical | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 476 | 
 People's Community Clinic | 
 https://webprd.ochin.org/prd-fhir/MYCHARTAUSTINPCC/api/FHIR/R4 | 
 |

 | 
 862 | 
 Perham Health | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1005 | 
 Perlman Clinic | 
 https://epicproxy.et0502.epichosted.com/FhirProxy/MPC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Petaluma Health Center | 
 https://webprd.ochin.org/prd-fhir/PHEALTHCENTER/api/FHIR/R4 | 
 |

 | 
 8305 | 
 Phelps Health | 
 https://epicproxy.et1134.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 568 | 
 Physicians Alliance of Connecticut | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1157 | 
 Piedmont Healthcare | 
 https://webproxy.piedmont.org/ARR-FHIR/api/FHIR/R4 | 
 |

 | 
 13207 | 
 Pikeville Medical Center | 
 https://epicproxy.et1225.epichosted.com/FHIRProxy/PMC/api/FHIR/R4 | 
 |

 | 
 3978 | 
 Pine Rest | 
 https://epicproxy.et1086.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Pine Springs Health | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/PSH/api/FHIR/R4 | 
 |

 | 
 476 | 
 Pines Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTPHS/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Pinnacle Primary Care | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 862 | 
 Pioneer Memorial Hospital | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 8826 | 
 Planned Parenthood | 
 https://epicproxy.et1154.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Planned Parenthood of Northern California | 
 https://webprd.ochin.org/prd-fhir/MYCHARTPPNORCAL/api/FHIR/R4 | 
 |

 | 
 434 | 
 Pocano Ambulatory Surgery Center | 
 https://proxy.lvh.com/FHIR/api/FHIR/R4 | 
 |

 | 
 623 | 
 Portneuf Medical Center | 
 https://epicproxy.ardenthealth.com/fhir/PMC/api/FHIR/R4 | 
 |

 | 
 2461 | 
 Powers Health | 
 https://webproxy.comhs.org/FHIR/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Pozitiv Wellness | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 1525 | 
 Prairie Cardiovascular | 
 https://scripts.prevea.com/FHIR-ARR-PRD/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Premier Community HealthCare | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 932 | 
 Premier Health | 
 https://rx.premierhealthpartners.org/fhir/PREMIER/api/FHIR/R4 | 
 |

 | 
 815 | 
 Premise Health | 
 https://epicproxy.et1052.epichosted.com/FHIRProxy/PREMISE/api/FHIR/R4 | 
 |

 | 
 1539 | 
 Presbyterian Healthcare Services | 
 https://epicfhir.phs.org/FHIR/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Prestige Medical Sai | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 1525 | 
 Prevea Health | 
 https://scripts.prevea.com/FHIR-ARR-PRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Primary Health Care | 
 https://webprd.ochin.org/prd-fhir/PHCIOWA/api/FHIR/R4 | 
 |

 | 
 476 | 
 Prime Health Plus | 
 https://webprd.ochin.org/prd-fhir/MYCHARTPRIMEHEALTHPLUS/api/FHIR/R4 | 
 |

 | 
 611 | 
 Prime Healthcare | 
 https://phsfhir.primehealthcare.com/PHS-PRD-FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Prince George's County Health Department | 
 https://webprd.ochin.org/prd-fhir/MYCHARTPGCHD/api/FHIR/R4 | 
 |

 | 
 745 | 
 Prisma Health | 
 https://epicproxy.et0915.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Progressive Community Health Centers | 
 https://webprd.ochin.org/prd-fhir/PROGRESSIVECHC/api/FHIR/R4 | 
 |

 | 
 1787 | 
 ProHealth Care | 
 https://soap.phci.org/Interconnect-FHIR/MYCHART/api/FHIR/R4 | 
 |

 | 
 739 | 
 ProHealth Physicians | 
 https://fhirprd.reliantmedicalgroup.org/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 405 | 
 Proliance Hand, Wrist & Elbow Physicians | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 759 | 
 Proliance Orthopedics & Sports Medicine | 
 https://sfd.overlakehospital.org/FHIRproxy/POSM/api/FHIR/R4 | 
 |

 | 
 796 | 
 ProMedica | 
 https://fhir.promedica.org/FHIR/MYCHART/api/FHIR/R4 | 
 |

 | 
 405 | 
 ProOrtho Orthopedics and Sports Medicine | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Prosser Memorial Health | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Providence Cedars Sinai Tarzana | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Providence Community Health Centers | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Providence Health & Services | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Providence Health & Services | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Providence Health & Services | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Providence Health & Services | 
 https://haikuak.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Providence Swedish Rehabilitation Hospital | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Public Health Management Corporation | 
 https://webprd.ochin.org/prd-fhir/MYPHMCHEALTH/api/FHIR/R4 | 
 |

 | 
 476 | 
 Pueblo Community Health Center | 
 https://webprd.ochin.org/prd-fhir/api/FHIR/R4 | 
 |

 | 
 700 | 
 Puget Sound Orthopaedics | 
 https://rp.catholichealth.net/fhir/api/FHIR/R4 | 
 |

 | 
 405 | 
 Pullman Regional Hospital | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 7851 | 
 Quadmed | 
 https://epicicfore.quadmedical.com/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Quality of Life Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTQOL/api/FHIR/R4 | 
 |

 | 
 827 | 
 Quartz | 
 https://epicproxy.hosp.wisc.edu/FhirProxy/QUARTZ/api/FHIR/R4 | 
 |

 | 
 1623 | 
 Queen's Connect | 
 https://mobileapps.queens.org/FHIR/MYCHART/api/FHIR/R4 | 
 |

 | 
 472 | 
 Quest Behavioral Health | 
 https://interconnect.wellspan.org/interconnect-prd-oauth2/api/FHIR/R4 | 
 |

 | 
 476 | 
 Radiant Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTRADIANTHEALTHCENTERS/api/FHIR/R4 | 
 |

 | 
 1797 | 
 Rady Children's | 
 https://epcppxl1.rchsd.org/fhirprd/api/FHIR/R4 | 
 |

 | 
 862 | 
 Rainy Lake Medical Center | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Ravenswood Family Health Network | 
 https://webprd.ochin.org/prd-fhir/MYCHARTRFHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Ray County Hospital and Healthcare | 
 https://webprd.ochin.org/prd-fhir/RCHH/api/FHIR/R4 | 
 |

 | 
 1375 | 
 RC Hospitals & Clinics | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 19520 | 
 Rebound Orthopedic and Neurosurgery | 
 https://epicproxy.et4006.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Redwoods Rural Health Center | 
 https://webprd.ochin.org/prd-fhir/RRHCMYCHART/api/FHIR/R4 | 
 |

 | 
 10792 | 
 Reid Health | 
 https://epicproxy.et1220.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 739 | 
 Reliant Medical Group | 
 https://fhirprd.reliantmedicalgroup.org/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 19520 | 
 Reno Orthopedic Center | 
 https://epicproxy.et4006.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 2088 | 
 Renown | 
 https://fhir.renown.org/FHIRProxy/RENOWN/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Rice Memorial Hospital | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Ritual Medical | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/RIT/api/FHIR/R4 | 
 |

 | 
 476 | 
 River Hills Community Health Center | 
 https://webprd.ochin.org/prd-fhir/RIVERHILLSHEALTH/api/FHIR/R4 | 
 |

 | 
 476 | 
 River People Health Center | 
 https://webprd.ochin.org/prd-fhir/RPHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 River Valley Primary Care Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTRVPCS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Riverland Community Health | 
 https://webprd.ochin.org/prd-fhir/RCHEALTH/api/FHIR/R4 | 
 |

 | 
 355 | 
 River's Edge Hospital & Clinic | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 1453 | 
 Riverside Health System | 
 https://ep-rpfg.rivhs.com/Interconnect-FHIR-PRD/RHSMYCHART/api/FHIR/R4 | 
 |

 | 
 2442 | 
 Riverside Medical Center | 
 https://RPPROD.riversidehealthcare.net/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 424 | 
 Riverside Medical Clinic | 
 https://SF1.rmcps.com/FHIRProxy/RMC/api/FHIR/R4 | 
 |

 | 
 687 | 
 Riverside University Health System | 
 https://prd.lluh.org/fhir/api/FHIR/R4 | 
 |

 | 
 912 | 
 Riverview Health | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 862 | 
 Riverview Health | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 403 | 
 RiverView Health | 
 https://epic-fhir.mercy.net/PRDFHIRSTL/RVH/api/FHIR/R4/ | 
 |

 | 
 476 | 
 Riverwood Healthcare Center | 
 https://webprd.ochin.org/prd-fhir/RWHEALTH/api/FHIR/R4 | 
 |

 | 
 337 | 
 Robeson Health Care | 
 https://epicfe.unch.unc.edu/FHIR/RHCC/api/FHIR/R4 | 
 |

 | 
 746 | 
 Rochelle Community Hospital | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 603 | 
 Rochester Regional Health | 
 https://epicarr.rochesterregional.org/FHIR/MYCARE/api/FHIR/R4 | 
 |

 | 
 405 | 
 Rocky Mountain ENT | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Rogue Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTROGUE/api/FHIR/R4 | 
 |

 | 
 476 | 
 Root Center for Advanced Recovery | 
 https://webprd.ochin.org/prd-fhir/ROOTCENTERMYCHART/api/FHIR/R4 | 
 |

 | 
 1752 | 
 Roper St. Francis | 
 https://carepath.health-partners.org/Proxy-FHIR/RSF/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Rukmini D. Kumar MD | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 396 | 
 Rush University Medical Center | 
 https://epicproxy.rush.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 8470 | 
 Rutgers Health University Behavioral Health Care | 
 https://epicproxy.et1157.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 8470 | 
 RWJBarnabas Health | 
 https://epicproxy.et1157.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Saban | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSABAN/api/FHIR/R4 | 
 |

 | 
 687 | 
 SAC Health System | 
 https://prd.lluh.org/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Sacramento County Public Health | 
 https://webprd.ochin.org/prd-fhir/SCPH/api/FHIR/R4 | 
 |

 | 
 1310 | 
 Saint Francis Health System | 
 https://eprdsoap000.saintfrancis.Com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1877 | 
 Saint Francis Healthcare System | 
 https://reverseproxy.sfmc.net/fhirproxyprd/api/FHIR/R4 | 
 |

 | 
 8470 | 
 Saint James Health | 
 https://epicproxy.et1157.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 557 | 
 Saint Luke's Health System | 
 https://epicmobile.corp.saint-lukes.org/FHIRPROXY/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Salem Clinic | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 679 | 
 Salem Health | 
 https://epicproxy.et0516.epichosted.com/APIProxyPRD/STANDARD/api/FHIR/R4 | 
 |

 | 
 746 | 
 Salem Township Hospital | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 7852 | 
 Salinas Valley Health | 
 https://epicproxy.et1146.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 7852 | 
 Salinas Valley Health Affiliates | 
 https://epicproxy.et1146.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1714 | 
 Samaritan Health Services | 
 https://fhir.samhealth.org/fhir-arr/api/FHIR/R4 | 
 |

 | 
 405 | 
 Samaritan Healthcare | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 San Francisco Community Clinic Consortium | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSFSOS/api/FHIR/R4 | 
 |

 | 
 476 | 
 San Francisco Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSFCHC/api/FHIR/R4 | 
 |

 | 
 3524 | 
 San Francisco Dept of Public Health | 
 https://epicproxy.et1082.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 San Luis Obispo Public Health Department | 
 https://webprd.ochin.org/prd-fhir/SLOPUBLICHEALTH/api/FHIR/R4 | 
 |

 | 
 18714 | 
 San Ysidro Health | 
 https://epicproxy.et1327.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 862 | 
 Sanford | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 862 | 
 Sanford Health Plan | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 856 | 
 Sansum | 
 https://wavesurescripts.sansumclinic.org/FHIR/api/FHIR/R4 | 
 |

 | 
 356 | 
 Santa Clara | 
 https://scvhhsfhir.sccgov.org/interconnect-oauth2/api/FHIR/R4 | 
 |

 | 
 476 | 
 Santa Cruz Community Health | 
 https://webprd.ochin.org/prd-fhir/SCHEALTHCENTERS/api/FHIR/R4 | 
 |

 | 
 866 | 
 Santa Fe Imaging | 
 https://proxy.christushealth.org/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 7852 | 
 Santa Lucia Medical Group | 
 https://epicproxy.et1146.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Santa Rosa Community Health | 
 https://webprd.ochin.org/prd-fhir/SRHEALTH/api/FHIR/R4 | 
 |

 | 
 904 | 
 Santiam Hospital | 
 https://epicproxy.et1030.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 476 | 
 Sawtooth Mountain Clinic | 
 https://webprd.ochin.org/prd-fhir/SMC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Scenic Rivers Health Services | 
 https://webprd.ochin.org/prd-fhir/SCENICRIVERSHEALTH/api/FHIR/R4 | 
 |

 | 
 2285 | 
 Scheurer | 
 https://epichaiku.chs-mi.com/FHIRPROXY/api/FHIR/R4 | 
 |

 | 
 476 | 
 School Health Clinics of Santa Clara County | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSHC/api/FHIR/R4 | 
 |

 | 
 2246 | 
 Scotland Health Care System | 
 https://epicproxy.et0905.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1750 | 
 Scripps Health | 
 https://epicproxy.et0964.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 1311 | 
 Sea Mar | 
 https://soapprod.multicare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2688 | 
 Seattle Childrens Community Connect | 
 https://fhir.seattlechildrens.org/fhir/api/FHIR/R4 | 
 |

 | 
 2688 | 
 Seattle Children's MyChart | 
 https://fhir.seattlechildrens.org/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Seattle Indian Health Board | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSIHB/api/FHIR/R4 | 
 |

 | 
 405 | 
 Seattle Medical Associates | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Seattle Premier Health | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Seattle Roots Community Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSEATTLEROOTS/api/FHIR/R4 | 
 |

 | 
 817 | 
 Select Medical | 
 https://epicproxy.et0948.epichosted.com/FhirProxy/api/FHIR/R4 | 
 |

 | 
 13441 | 
 Self Regional | 
 https://epicproxy.et1235.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 490 | 
 Sentara Health | 
 https://epicfhir.sentara.com/ARR-FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 623 | 
 Seton Medical Center and Wellstone Health Partners | 
 https://epicproxy.ardenthealth.com/fhir/SMC/api/FHIR/R4 | 
 |

 | 
 405 | 
 Seward Community Health Center | 
 https://haikuak.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1178 | 
 SGMC | 
 https://epicproxy.et1024.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2166 | 
 Shannon | 
 https://epicrpx.shannonhealth.org/FHIR_ARR/api/FHIR/R4/ | 
 |

 | 
 476 | 
 Share Our Selves | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSOS/api/FHIR/R4 | 
 |

 | 
 15027 | 
 Sharp Healthcare | 
 https://epicproxy.et1275.epichosted.com/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1157 | 
 Shepherd Center | 
 https://webproxy.piedmont.org/ARR-FHIR/api/FHIR/R4 | 
 |

 | 
 9392 | 
 Shepherd's Hope | 
 https://mobile.adventhealth.com/oauth2-PRD/api/FHIR/R4 | 
 |

 | 
 405 | 
 Shodair Children's Hospital | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 15516 | 
 Shriner's Childrens | 
 https://epicproxy.et1283.epichosted.com/FHIRProxy/SHC/api/FHIR/R4 | 
 |

 | 
 862 | 
 Sidney Health Center | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Signature Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSH/api/FHIR/R4 | 
 |

 | 
 1803 | 
 SIH Affiliates | 
 https://epicproxy.et0986.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 26387 | 
 Simpson General Hospital | 
 https://epicproxy.et1453.epichosted.com/FHIRProxyPRD/SIMPSON/api/FHIR/R4 | 
 |

 | 
 746 | 
 Sinai Chicago | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 378 | 
 Singing River Health System | 
 https://arr.mysrhs.com/FHIR/MYSRHS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Siouxland Community Health Center | 
 https://webprd.ochin.org/prd-fhir/SLANDCHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Sixteenth Street | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSCHC/api/FHIR/R4 | 
 |

 | 
 2299 | 
 Skagit | 
 https://epicproxy.et1005.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 358 | 
 Sky Lakes | 
 https://epicmobile.asante.org/FHIR-PRD/HOME/api/FHIR/R4 | 
 |

 | 
 3236 | 
 Slocum-Dickson Medical Group | 
 https://fhir.mvhealthsystem.org/FHIRproxy/api/FHIR/R4 | 
 |

 | 
 5965 | 
 Smile Generation MyChart | 
 https://epicproxy.et1079.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 759 | 
 Snoqualmie Valley Health | 
 https://sfd.overlakehospital.org/FHIRproxy/SVH/api/FHIR/R4 | 
 |

 | 
 476 | 
 SoHum Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSHCHD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Solano County | 
 https://webprd.ochin.org/prd-fhir/SOLANOCOUNTYHEALTH/api/FHIR/R4 | 
 |

 | 
 1308 | 
 SolutionHealth | 
 https://epicproxyprd.solutionhealth.org/FHIR_PRD/MYCHART/api/FHIR/R4 | 
 |

 | 
 476 | 
 Sonoma County Indian Health Project | 
 https://webprd.ochin.org/prd-fhir/SCIHP/api/FHIR/R4 | 
 |

 | 
 476 | 
 Sonoma Valley Community Health Center | 
 https://webprd.ochin.org/prd-fhir/SVCHC/api/FHIR/R4 | 
 |

 | 
 405 | 
 Sonoma Valley Hospital | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 South Boston Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSBCHC/api/FHIR/R4 | 
 |

 | 
 26387 | 
 South Central Regional Medical Center | 
 https://epicproxy.et1453.epichosted.com/FHIRProxyPRD/api/FHIR/R4/ | 
 |

 | 
 476 | 
 South of Market Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTEQUITYHEALTH/api/FHIR/R4 | 
 |

 | 
 405 | 
 South Peninsula Hospital | 
 https://haikuak.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2911 | 
 South Shore Health | 
 https://sshic.southshorehealth.org/FHIR/SSH/api/FHIR/R4 | 
 |

 | 
 405 | 
 South Tabor Family Physicians & Services | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 395 | 
 Southcoast Health System | 
 https://epicpproxy.southcoast.org/FHIR/api/FHIR/R4/ | 
 |

 | 
 9031 | 
 Southeast Health | 
 https://arrprd.southeasthealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 405 | 
 Southern California Multi Specialty Center | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Southern Coos Hospital & Health Center | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1803 | 
 Southern Illinois Healthcare | 
 https://epicproxy.et0986.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Southern Jersey Family Medical Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSJFMC/api/FHIR/R4 | 
 |

 | 
 405 | 
 Southern Oregon Orthopedics | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Southside Health Center | 
 https://webprd.ochin.org/prd-fhir/SOUTHSIDECHS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Southwest Community Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSWCHC/api/FHIR/R4 | 
 |

 | 
 982 | 
 Southwest Mississippi Regional Medical Center | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1511 | 
 Spartanburg Regional Healthcare System | 
 https://epicproxy.et0939.epichosted.com/FHIRProxy/SRMYCHART/api/FHIR/R4 | 
 |

 | 
 567 | 
 Specialty Physicians of Illinois | 
 https://ema.franciscanalliance.org/FHIR_PROXY/api/FHIR/R4/ | 
 |

 | 
 2054 | 
 Spooner Health | 
 https://m.essentiahealth.org/FHIR/AFFHOME/api/FHIR/R4 | 
 |

 | 
 777 | 
 Spry Health | 
 https://fhir.metrohealth.org/fhir_prd/api/FHIR/R4 | 
 |

 | 
 777 | 
 SprySenior | 
 https://fhir.metrohealth.org/fhir_prd/api/FHIR/R4 | 
 |

 | 
 489 | 
 SSM Health | 
 https://fhir.ssmhc.com/Fhir/MyChart/api/FHIR/R4 | 
 |

 | 
 432 | 
 St Luke's | 
 https://fhir.slhn.org/fhir/api/FHIR/R4 | 
 |

 | 
 1367 | 
 St Thomas Community Health Center | 
 https://interconnect.lcmchealth.org/FHIR/LCMC/api/FHIR/R4 | 
 |

 | 
 476 | 
 St. Anthony's | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSA/api/FHIR/R4 | 
 |

 | 
 17538 | 
 St. Barnabas Health | 
 https://sbhepicrevprox.barnabas.network/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 904 | 
 St. Charles Health System | 
 https://epicproxy.et1030.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 355 | 
 St. Croix Health | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 1882 | 
 St. David's | 
 https://stdavidsfhirprd.app.medcity.net/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 1444 | 
 St. Elizabeth Healthcare | 
 https://sehproxy.stelizabeth.com/arr-fhir/api/FHIR/R4 | 
 |

 | 
 1375 | 
 St. Gabriel's Health | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 12058 | 
 St. Jude | 
 https://rp.stjude.org/oauth2-prd/api/FHIR/R4 | 
 |

 | 
 351 | 
 St. Luke's | 
 https://epincoming.slhs.org/Interconnect-FHIR/api/FHIR/R4 | 
 |

 | 
 2246 | 
 St. Luke's Hospital | 
 https://epicproxy.et0905.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 516 | 
 St. Peter's Health | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/MOBILE/api/FHIR/R4 | 
 |

 | 
 1927 | 
 St. Tammany | 
 https://myc.ochsner.org/FHIR/api/FHIR/R4 | 
 |

 | 
 19771 | 
 Stamford Health | 
 https://epicproxy.et1378.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 520 | 
 Stanford | 
 https://sfd.stanfordmed.org/FHIR/api/FHIR/R4 | 
 |

 | 
 426 | 
 Stanford Children's Health | 
 https://epicproxy.et0857.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Star Valley Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTSVH/api/FHIR/R4 | 
 |

 | 
 568 | 
 Starling | 
 https://EpicProxy.hhchealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 831 | 
 Steindler Orthopedic Clinic | 
 https://eproxy.mercycare.org/oauth2/STEINDLER/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Stellis Health | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 1563 | 
 Stellis Health | 
 https://minerva.northmemorial.com/fhir/api/FHIR/R4 | 
 |

 | 
 1375 | 
 Stevens Community Medical Center | 
 https://epicmobile.centracare.com/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Stigler Health and Wellness Center | 
 https://webprd.ochin.org/prd-fhir/HEALTHWELLNSSOKMYCHART/api/FHIR/R4 | 
 |

 | 
 405 | 
 Stillaguamish Tribe of Indians | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2002 | 
 Stormont Vail Health Care | 
 https://epicsoap.stormontvail.org/FHIRproxy/HOME/api/FHIR/R4 | 
 |

 | 
 476 | 
 Sublette County Health | 
 https://webprd.ochin.org/prd-fhir/SUBLETTE/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Sugar Land Pain and Spine Specialists | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 14718 | 
 Summa Health | 
 https://epicproxy.et1289.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1193 | 
 Summit County Public Health | 
 https://haiku-canto-prod.chmca.org/ARR-FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 6709 | 
 Summit Health | 
 https://epicproxy.et1153.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2438 | 
 Summit Health - Oregon | 
 https://epicsoap.bmctotalcare.com/fhir/SUMMIT/api/FHIR/R4 | 
 |

 | 
 405 | 
 Summit Pacific Medical Center | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 686 | 
 Summit Surgical Center | 
 https://epicproxy.et1017.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 883 | 
 SUNY | 
 https://epicedge.upstate.edu/fhir/api/FHIR/R4 | 
 |

 | 
 572 | 
 Surgical Clinic Associates | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 960 | 
 Susquehanna Valley Medical Specialties | 
 https://geisapi.geisinger.edu/FHIR_PROD/api/FHIR/R4 | 
 |

 | 
 863 | 
 Sutter Health | 
 https://apiservices.sutterhealth.org/ifs/MHO/api/FHIR/R4 | 
 |

 | 
 405 | 
 Swedish | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 827 | 
 SwedishAmerican | 
 https://epicproxy.hosp.wisc.edu/FhirProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Syracuse Community Health | 
 https://webprd.ochin.org/prd-fhir/SYRACUSECOMMUNITYHEALTHMYCHART/api/FHIR/R4 | 
 |

 | 
 403 | 
 Tahoe Forest Health System | 
 https://epic-fhir.mercy.net/PRDFHIRAOK2/TAO/api/FHIR/R4/ | 
 |

 | 
 20574 | 
 Tallahassee Memorial Healthcare | 
 https://epicproxy.et1387.epichosted.com/FHIRProxyPRD/HOME/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Tampa Family Health Centers | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 380 | 
 Tampa General Hospital | 
 https://epicproxy.et0761.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 3119 | 
 Tanner Health System | 
 https://epicproxy.et1098.epichosted.com/APIProxyPRD/STANDARD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Tarzana Treatment Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTTTC/api/FHIR/R4 | 
 |

 | 
 13877 | 
 TCA Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 748 | 
 TempleHealth | 
 https://epicaccess.templehealth.org/FhirProxyPrd/MTH/api/FHIR/R4 | 
 |

 | 
 1927 | 
 Terrebonne General Medical Center | 
 https://myc.ochsner.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Terry Reilly Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTTRHS/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Texas A&M Health | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 357 | 
 Texas Children's | 
 https://mobileapps.texaschildrens.org/FHIR/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Texas Family Clinic | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 555 | 
 Texas Health Resources | 
 https://epproxy.texashealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 1442 | 
 Texas Scottish Rite Hospital for Children | 
 https://epicproxy.et0970.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 982 | 
 The Baton Rouge Clinic | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 19520 | 
 The Center | 
 https://epicproxy.et4006.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 The Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCHS/api/FHIR/R4 | 
 |

 | 
 418 | 
 The Christ Hospital | 
 https://soapproxyprod.thechristhospital.com/fhir/MOBILE/api/FHIR/R4 | 
 |

 | 
 375 | 
 The Health Center at Hudson Yards | 
 https://epicsoapproxyprd.mountsinai.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 1638 | 
 The Institute for Family Health | 
 https://epicproxy.institute.org/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 The NATIVE Project | 
 https://webprd.ochin.org/prd-fhir/NATIVEPROJECT/api/FHIR/R4 | 
 |

 | 
 410 | 
 The Nebraska Medical Center | 
 https://ocsoapprd.nebraskamed.com/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 528 | 
 The Ohio State University Wexner Medical Center | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 405 | 
 The Oregon Clinic | 
 https://haikuor.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 3726 | 
 The Pediatric Center Boulder | 
 https://prevprox.bch.org/FHIRproxyPRD/api/FHIR/R4/ | 
 |

 | 
 16090 | 
 The Portland Clinic | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 1623 | 
 The Queen's Health System | 
 https://mobileapps.queens.org/FHIR/MYCHART/api/FHIR/R4 | 
 |

 | 
 783 | 
 The University of Kansas Health System | 
 https://fhir.kansashealthsystem.com/interconnect-PRD_FHIR/api/FHIR/R4 | 
 |

 | 
 902 | 
 Thedacare | 
 https://arr.thedacare.org/FHIR/api/FHIR/R4 | 
 |

 | 
 391 | 
 Thomas Jefferson University Health System | 
 https://fhir.jefferson.edu/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 1948 | 
 Thunder Basin | 
 https://soap.crmcwy.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Tiburcio Vasquez Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTTIBURCIO/api/FHIR/R4 | 
 |

 | 
 1586 | 
 TidalHealth | 
 https://eweb.tidalhealth.org/Oauth2/MYCHART.TIDALHEALTH.ORG/api/FHIR/R4 | 
 |

 | 
 996 | 
 Tidelands Health | 
 https://fhirprod.musc.edu/fhirprod/TIDELANDS/api/FHIR/R4/ | 
 |

 | 
 476 | 
 Tillamook County Community Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTTILLAMOOK/api/FHIR/R4 | 
 |

 | 
 1927 | 
 Titus Regional Medical Center | 
 https://myc.ochsner.org/FHIR/api/FHIR/R4 | 
 |

 | 
 2154 | 
 Tomah Health | 
 https://scproxy.gundersenhealth.org/FHIRARR/GHS/api/FHIR/R4 | 
 |

 | 
 868 | 
 Tower Health | 
 https://epicsoap.readinghospital.org/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 13877 | 
 Treasure Coast Community Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Triad Adult & Pediatric Medicine | 
 https://webprd.ochin.org/prd-fhir/TAPMEDICINE/api/FHIR/R4 | 
 |

 | 
 425 | 
 TriHealth | 
 https://epicscripts.trihealth.com/fhirproxy/api/FHIR/R4 | 
 |

 | 
 2576 | 
 Trinity Health | 
 https://epic-ext.trinity-health.org/FHIR/api/FHIR/R4 | 
 |

 | 
 13877 | 
 True Health | 
 https://epicproxy.et1256.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 TrueCare | 
 https://webprd.ochin.org/prd-fhir/MYCHARTTC/api/FHIR/R4 | 
 |

 | 
 838 | 
 Tuality Healthcare | 
 https://epicmobile.ohsu.edu/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 2064 | 
 Tucson Independent Physicians and Surgeons | 
 https://fhir.tmcaz.com/FHIRProxy/TIPS/api/FHIR/R4 | 
 |

 | 
 2064 | 
 Tucson Medical Center | 
 https://fhir.tmcaz.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 11169 | 
 Tufts Medicine | 
 https://intconfg-p.well-net.org/PRD-OAUTH2/api/FHIR/R4 | 
 |

 | 
 405 | 
 Tulalip Health System | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 1310 | 
 Tulsa Bone and Joint Associates | 
 https://eprdsoap000.saintfrancis.Com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 623 | 
 Tulsa Spine & Specialty Hospital | 
 https://epicproxy.ardenthealth.com/fhir/TSSH/api/FHIR/R4 | 
 |

 | 
 940 | 
 UC Davis | 
 https://emrrp.ucdmc.ucdavis.edu/FHIR/api/FHIR/R4 | 
 |

 | 
 1116 | 
 UC Health | 
 https://epic-soap.uchealth.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 26468 | 
 UC Irvine | 
 https://epicproxy.et1448.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 1005 | 
 UC San Diego | 
 https://epicproxy.et0502.epichosted.com/FhirProxy/UCSD/api/FHIR/R4 | 
 |

 | 
 597 | 
 UCHealth | 
 https://ss.uch.edu/FHIRProxy/MHC/api/FHIR/R4 | 
 |

 | 
 597 | 
 UCHealth Affiliated Clinics and Hospitals MyChart | 
 https://ss.uch.edu/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1005 | 
 UCI Health Archive | 
 https://epicproxy.et0502.epichosted.com/FhirProxy/UCIHEALTH/api/FHIR/R4 | 
 |

 | 
 341 | 
 UCLA Health Medicare Advantage Plan | 
 https://arrprox.mednet.ucla.edu/FHIRPRD/HEALTHPLAN/api/FHIR/R4 | 
 |

 | 
 341 | 
 UCLA Medical Center | 
 https://arrprox.mednet.ucla.edu/FHIRPRD/api/FHIR/R4 | 
 |

 | 
 888 | 
 UConn Health | 
 https://epicproxy.et0996.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 353 | 
 UCSF | 
 https://unified-api.ucsf.edu/clinical/apex/api/FHIR/R4 | 
 |

 | 
 888 | 
 UHI | 
 https://epicproxy.et0996.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 4454 | 
 UI Health | 
 https://epicproxy.et1085.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 585 | 
 UIHC | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 8530 | 
 UK Healthcare | 
 https://ukepicproxy.mc.uky.edu/Interconnect-PRD-OAuth2/api/FHIR/R4 | 
 |

 | 
 2245 | 
 UK King's Daughters | 
 https://arrprd.kdmc.net/fhir/api/FHIR/R4 | 
 |

 | 
 922 | 
 UMass Memorial Health | 
 https://epicproxy.et0978.epichosted.com/FHIRProxy/HOMEPAGE/api/FHIR/R4 | 
 |

 | 
 26325 | 
 UMC Health System | 
 https://epicproxy.et1442.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 2588 | 
 UMC Southern Nevada | 
 https://epicproxy.et1023.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 337 | 
 UNC Health Care | 
 https://epicfe.unch.unc.edu/FHIR/api/FHIR/R4/ | 
 |

 | 
 862 | 
 UND Center for Family Medicine | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 United Community & Family Services Healthcare | 
 https://webprd.ochin.org/prd-fhir/MYCHARTUCFS/api/FHIR/R4 | 
 |

 | 
 476 | 
 United Community Health Center | 
 https://webprd.ochin.org/prd-fhir/UNITEDCOMMUNITYHEALTH/api/FHIR/R4 | 
 |

 | 
 4955 | 
 United Health Services | 
 https://epicproxy.et1127.epichosted.com/FHIRproxy/api/FHIR/R4 | 
 |

 | 
 862 | 
 United Hospital District | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 United Indian Health Services | 
 https://webprd.ochin.org/prd-fhir/UIHS/api/FHIR/R4 | 
 |

 | 
 3707 | 
 United Regional | 
 https://epicproxy.et1096.epichosted.com/FHIRProxy/URMYCHART/api/FHIR/R4 | 
 |

 | 
 476 | 
 Unity Care NW | 
 https://webprd.ochin.org/prd-fhir/UNITYCARENW/api/FHIR/R4 | 
 |

 | 
 27869 | 
 Unity Health Care | 
 https://epicproxy.et1432.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 326 | 
 UnityPoint Health | 
 https://epicfhir.unitypoint.org/ProdFHIR/api/FHIR/R4 | 
 |

 | 
 572 | 
 University Clinical Health | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 4797 | 
 University Health System | 
 https://epicproxy.et1130.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 1231 | 
 University Hospital | 
 https://epicproxy.et0434.epichosted.com/APIProxyPRD/UHNJ/api/FHIR/R4 | 
 |

 | 
 13429 | 
 University Hospitals Cleveland | 
 https://uhhsportal.uhhospitals.org/oauth2-prd/api/FHIR/R4 | 
 |

 | 
 651 | 
 University of Arkansas for Medical Sciences | 
 https://ucsoap.uams.edu/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 685 | 
 University of Chicago Hospitals | 
 https://epicproxy.et0169.epichosted.com/APIProxyPRD/UCM/api/FHIR/R4 | 
 |

 | 
 657 | 
 University of Florida | 
 https://epicsoap.shands.ufl.edu/FHIR/api/FHIR/R4/ | 
 |

 | 
 623 | 
 University of Kansas Health System | 
 https://epicproxy.ardenthealth.com/fhir/UKH/api/FHIR/R4 | 
 |

 | 
 9571 | 
 University of Louisville Physicians | 
 https://epicproxy.et1193.epichosted.com/FHIRProxy/ULP/api/FHIR/R4 | 
 |

 | 
 547 | 
 University of Maryland Medical System | 
 https://fhir.umm.edu/fhir/api/FHIR/R4/ | 
 |

 | 
 599 | 
 University of Miami | 
 https://epicproxy.et0747.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 869 | 
 University of Michigan Health | 
 https://mcproxyprd.med.umich.edu/FHIR-PRD/UMICH/api/FHIR/R4 | 
 |

 | 
 1104 | 
 University of Michigan Health-Sparrow | 
 https://haiku.sparrow.org/fhir-prd/api/FHIR/R4 | 
 |

 | 
 874 | 
 University of Michigan Health-West | 
 https://arrprd.metrohealth.net/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 University of Minnesota | 
 https://webprd.ochin.org/prd-fhir/MYCHARTCUHCC/api/FHIR/R4 | 
 |

 | 
 531 | 
 University of Mississippi Medical Center | 
 https://soapproxy.umc.edu/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 726 | 
 University of Rochester | 
 https://ercd-sproxy.urmc.rochester.edu/mips/api/FHIR/R4 | 
 |

 | 
 380 | 
 University of South Florida | 
 https://epicproxy.et0761.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 637 | 
 University of Texas MD Anderson Cancer Center | 
 https://epicproxy.et0909.epichosted.com/APIProxyPRD/api/FHIR/R4/ | 
 |

 | 
 12077 | 
 University of Toledo | 
 https://icon.utoledo.edu/ic-oa2-prd/api/FHIR/R4 | 
 |

 | 
 338 | 
 University of Utah | 
 https://webproxyprd.med.utah.edu/FHIRMyChart/api/FHIR/R4 | 
 |

 | 
 1266 | 
 University of Vermont Health Network | 
 https://epicproxy.uvmhealth.org/FHIR-ARR/UVMMYCHART/api/FHIR/R4 | 
 |

 | 
 1439 | 
 University of Virginia | 
 https://hscsesoap.hscs.virginia.edu/oauth2/UVAHEALTH/api/FHIR/R4 | 
 |

 | 
 2588 | 
 UNLV Health | 
 https://epicproxy.et1023.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 778 | 
 UPMC | 
 https://epic-fhir-prd.upmc.com/FHIR-PRD/api/FHIR/R4 | 
 |

 | 
 22483 | 
 UPMC Patient Portal | 
 https://epicent-prd-rp.upmc.com/PRD-OAUTH2/api/FHIR/R4 | 
 |

 | 
 516 | 
 Uptown Community Health Center | 
 https://epicproxy.et0645.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 11509 | 
 Upwell Primary Care | 
 https://epicproxy.et1233.epichosted.com/FHIRProxy/AFFILIATE/api/FHIR/R4 | 
 |

 | 
 982 | 
 Urgent Care - Lake/Lourdes/St. Francis | 
 https://epicproxy.et0830.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 623 | 
 UT Health East Texas | 
 https://epicproxy.ardenthealth.com/fhir/UTHET/api/FHIR/R4 | 
 |

 | 
 28383 | 
 UT Medicine | 
 https://interconnect.utmedicine.org/OAuth2-prd/api/FHIR/R4 | 
 |

 | 
 1313 | 
 UT Medicine San Antonio | 
 https://epicproxy.et0582.epichosted.com/FHIRProxy/UTHP/api/FHIR/R4 | 
 |

 | 
 8387 | 
 UTHealth Houston | 
 https://epicproxy.et1178.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 623 | 
 Utica Park Clinic | 
 https://epicproxy.ardenthealth.com/fhir/UPC/api/FHIR/R4 | 
 |

 | 
 1500 | 
 UTMB | 
 https://epic-arr.utmb.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 347 | 
 UTSW | 
 https://EpicIntprxyPRD.swmed.edu/FHIR/api/FHIR/R4 | 
 |

 | 
 827 | 
 UW Health | 
 https://epicproxy.hosp.wisc.edu/FhirProxy/api/FHIR/R4 | 
 |

 | 
 325 | 
 UW Medicine | 
 https://fhir.epic.medical.washington.edu/FHIR-Proxy/UWM/api/FHIR/R4 | 
 |

 | 
 4441 | 
 Valley Children's Hospital | 
 https://ic.valleychildrens.org/fhir/api/FHIR/R4 | 
 |

 | 
 476 | 
 Valley Family Health Care | 
 https://webprd.ochin.org/prd-fhir/MYCHARTVFHC/api/FHIR/R4 | 
 |

 | 
 14955 | 
 Valley Health | 
 https://api.valleyhealth.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 561 | 
 Valley Health | 
 https://epicproxy.et0816.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 434 | 
 Valley Health Partners | 
 https://proxy.lvh.com/FHIR/api/FHIR/R4 | 
 |

 | 
 16589 | 
 Valley Health System | 
 https://epicproxy.et1320.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 971 | 
 Valley Medical Center | 
 https://FHIR.valleymed.org/FHIR-PRD/VMC/api/FHIR/R4 | 
 |

 | 
 597 | 
 Valley View Hospital | 
 https://ss.uch.edu/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 588 | 
 Valleywise | 
 https://esoap.valleywisehealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 585 | 
 Van Buren County Hospital | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2687 | 
 Vancouver Clinic | 
 https://soapprod.tvc.org/ARR-FHIR/api/FHIR/R4 | 
 |

 | 
 333 | 
 Vanderbilt University Medical Center | 
 https://arr01.service.vumc.org/FHIR-PRD/MHAV/api/FHIR/R4 | 
 |

 | 
 476 | 
 Variety Care Health Centers | 
 https://webprd.ochin.org/prd-fhir/MYCHARTVCHC/api/FHIR/R4 | 
 |

 | 
 9265 | 
 VCU Health | 
 https://epicproxy.et1200.epichosted.com/oauth2-PRD/api/FHIR/R4 | 
 |

 | 
 2287 | 
 Vecino Health Centers | 
 https://fhir.harrishealth.org/fhir/api/FHIR/R4 | 
 |

 | 
 2154 | 
 Vernon Memorial Healthcare | 
 https://scproxy.gundersenhealth.org/FHIRARR/GHS/api/FHIR/R4 | 
 |

 | 
 585 | 
 Veterans Memorial Hospital | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 2097 | 
 VHC Health | 
 https://common.virginiahospitalcenter.com/FHIRPRD/VHC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Virginia Garcia Memorial Health Center | 
 https://webprd.ochin.org/prd-fhir/MYCHARTVG/api/FHIR/R4 | 
 |

 | 
 686 | 
 Virtua Health | 
 https://epicproxy.et1017.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 17297 | 
 Vitruvian Health | 
 https://epicproxy.et1336.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 476 | 
 Vivent Health | 
 https://webprd.ochin.org/prd-fhir/VIVENTHEALTH/api/FHIR/R4 | 
 |

 | 
 18931 | 
 Vivo Pharmacy | 
 https://call.api.northwell.io/epic-proxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 VNA Health Care | 
 https://webprd.ochin.org/prd-fhir/MYCHARTVNAHEALTH/api/FHIR/R4 | 
 |

 | 
 904 | 
 Volunteers in Medicine Cascades | 
 https://epicproxy.et1030.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 746 | 
 Wabash General Hospital | 
 https://ssproxy.osfhealthcare.org/fhir-proxy/api/FHIR/R4 | 
 |

 | 
 3331 | 
 Waco Family Medicine | 
 https://haiku.wacofhc.org/FHIR/api/FHIR/R4 | 
 |

 | 
 414 | 
 WakeMed Health and Hospitals | 
 https://epic-soap.wakemed.org/FHIR/api/FHIR/R4 | 
 |

 | 
 476 | 
 Wallace | 
 https://webprd.ochin.org/prd-fhir/MYCHARTWALLACE/api/FHIR/R4 | 
 |

 | 
 405 | 
 Wallowa Memorial Hospital and Medical Center | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Wallowa Valley Center for Wellness | 
 https://webprd.ochin.org/prd-fhir/WVCENTERFORWELLNESS/api/FHIR/R4 | 
 |

 | 
 585 | 
 Washington County Hospital and Clinics | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Washington County Public Health | 
 https://webprd.ochin.org/prd-fhir/MYCHARTWC/api/FHIR/R4 | 
 |

 | 
 2893 | 
 Washington Health | 
 https://psacesoap.whhs.com/interconnect-fhir-prd/WHHS/api/FHIR/R4 | 
 |

 | 
 26604 | 
 Washington Regional Medical System | 
 https://epicproxy.et1440.epichosted.com/APIProxyPRD/api/FHIR/R4 | 
 |

 | 
 476 | 
 Washoe Tribal Health Center | 
 https://webprd.ochin.org/prd-fhir/WASHOEMYCHART/api/FHIR/R4 | 
 |

 | 
 1805 | 
 Watson Clinic | 
 https://epic-arr.watsonclinicad.com/FHIRProxy/WATSONCLINIC/api/FHIR/R4 | 
 |

 | 
 2475 | 
 Weill Cornell Medicine | 
 https://epicproxy-pub.et1089.epichosted.com/FHIRProxy/api/FHIR/R4/ | 
 |

 | 
 355 | 
 Welia Health | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 476 | 
 WellSpace Health | 
 https://webprd.ochin.org/prd-fhir/WELLSPACEHEALTHMYCHART/api/FHIR/R4 | 
 |

 | 
 472 | 
 WellSpan | 
 https://interconnect.wellspan.org/interconnect-prd-oauth2/api/FHIR/R4 | 
 |

 | 
 533 | 
 WellStar | 
 https://epicsoap.wellstar.org/fhirproxy/HOME/api/FHIR/R4 | 
 |

 | 
 16090 | 
 West Bend Family Medicine | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/WBFM/api/FHIR/R4 | 
 |

 | 
 560 | 
 West Michigan Cancer Center | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 11701 | 
 West Tennessee Healthcare | 
 https://epicproxy.et1243.epichosted.com/OAuth2-PRD/HOME/api/FHIR/R4 | 
 |

 | 
 983 | 
 West Virginia University | 
 https://apps.mywvuchart.com/FHIRproxy/WVUM/api/FHIR/R4 | 
 |

 | 
 560 | 
 Western Michigan University | 
 https://hygieia.bronsonhg.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 405 | 
 Western Montana Clinics | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Western North Carolina Community Health Services | 
 https://webprd.ochin.org/prd-fhir/WNCCHS/api/FHIR/R4 | 
 |

 | 
 476 | 
 Western University | 
 https://webprd.ochin.org/prd-fhir/MYCHARTWESTERNU/api/FHIR/R4 | 
 |

 | 
 1311 | 
 Western Washington Medical Group | 
 https://soapprod.multicare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 355 | 
 Western Wisconsin Health | 
 https://webproxy.allina.com/FHIR/Cuyuna Regional Medical Center/api/FHIR/R4 | 
 |

 | 
 16090 | 
 Western Wisconsin Urology – OakLeaf Medical Network | 
 https://epicproxy.et4001.epichosted.com/APIProxyPRD/WWU/api/FHIR/R4 | 
 |

 | 
 476 | 
 Whatley Health Services | 
 https://webprd.ochin.org/prd-fhir/MYCHARTWHATLEYHEALTH/api/FHIR/R4 | 
 |

 | 
 405 | 
 Whitman Hospital Medical Clinics | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |

 | 
 27869 | 
 Whitman Walker Health | 
 https://epicproxy.et1432.epichosted.com/FHIRProxyPRD/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Whole Care Pediatrics | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 1311 | 
 Willapa Harbor Hospital | 
 https://soapprod.multicare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Wilmington Community Clinic | 
 https://webprd.ochin.org/prd-fhir/WILMINGTONCC/api/FHIR/R4 | 
 |

 | 
 528 | 
 Wilson Health System | 
 https://ihismufhir.osumc.edu/fhir-prd/api/FHIR/R4 | 
 |

 | 
 862 | 
 Windom Area Health | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 11509 | 
 Winmind Behavioral Health & Addiction Medicine | 
 https://epicproxy.et1233.epichosted.com/FHIRProxy/AFFILIATE/api/FHIR/R4 | 
 |

 | 
 862 | 
 Winner Regional Healthcare | 
 https://eprescribe.sanfordhealth.org/FHIR/api/FHIR/R4 | 
 |

 | 
 585 | 
 Winneshiek Medical Center | 
 https://myepicapps.uihealthcare.org/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 476 | 
 Winters Healthcare | 
 https://webprd.ochin.org/prd-fhir/WINTERSHEALTH/api/FHIR/R4 | 
 |

 | 
 1178 | 
 Wiregrass Student Health Clinic | 
 https://epicproxy.et1024.epichosted.com/FHIRProxy/api/FHIR/R4 | 
 |

 | 
 16991 | 
 Wishing Well Pediatrics | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 17354 | 
 Woman's | 
 https://epicproxy.et1339.epichosted.com/FHIRproxy/HOME/api/FHIR/R4 | 
 |

 | 
 912 | 
 Woodlawn Health | 
 https://epicprod-mobile.parkview.com/FHIR/api/FHIR/R4 | 
 |

 | 
 1752 | 
 Wyandot Memorial Hospital | 
 https://carepath.health-partners.org/Proxy-FHIR/WMH/api/FHIR/R4 | 
 |

 | 
 16991 | 
 XO Wellness | 
 https://epicproxy.et1326.epichosted.com/FHIRProxy/MHCC/api/FHIR/R4 | 
 |

 | 
 476 | 
 Yakima Neighborhood Health | 
 https://webprd.ochin.org/prd-fhir/api/FHIR/R4 | 
 |

 | 
 879 | 
 Yakima Valley Farm Workers Clinic | 
 https://epicproxy.et0943.epichosted.com/FHIRProxy/HOME/api/FHIR/R4 | 
 |

 | 
 381 | 
 Yale New Haven Health/Yale Medical Group | 
 https://patientfhirapis.ynhh.org/PFF/api/FHIR/R4 | 
 |

 | 
 572 | 
 Yazoo City Medical Clinic | 
 https://rxedi.bmhcc.org/prd-fhir/api/FHIR/R4/ | 
 |

 | 
 405 | 
 Yelm Family Medicine | 
 https://haikuwa.providence.org/fhirproxy/api/FHIR/R4 | 
 |