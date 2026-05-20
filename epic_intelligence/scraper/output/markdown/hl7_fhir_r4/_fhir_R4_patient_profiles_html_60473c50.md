# Patient - FHIR v4.0.1

> Source: https://hl7.org/fhir/R4/patient-profiles.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/patient-profiles.html) [R4B](http://hl7.org/fhir/R4B/patient-profiles.html) **R4** [R3](http://hl7.org/fhir/STU3/patient-profiles.html) [R2](http://hl7.org/fhir/DSTU2/patient-profiles.html)
 

## 8.1.16 Resource Patient - Extensions & Profiles [
](patient-profiles.html#8.1.16)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): N/A | [Standards Status](versions.html#std-process): Informative | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

This table lists profiles and extensions for the Patient resource. For background information, see
[Profiling Resources](profiling.html#resources) and [Extensibility](extensibility.html).
Additional profiles and extensions may be found in published
[Implementation Guides ](https://registry.fhir.org/guides), or in the
[Conformance resource registry ](http://registry.fhir.org).

### 8.1.16.1 Profiles [
](patient-profiles.html#profiles)

No Profiles defined for this resource

### 8.1.16.2 Extensions [
](patient-profiles.html#extensions)

 | 
 [patient-adoptionInfo](extension-patient-adoptioninfo.html) | 
 `Patient` | 
 adoptionInfo | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-animal](extension-patient-animal.html) | 
 `Patient` | 
 animal | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-birthPlace](extension-patient-birthplace.html) | 
 `Patient` | 
 birthPlace | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-birthTime](extension-patient-birthtime.html) | 
 `Patient.birthDate` | 
 birthTime | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-cadavericDonor](extension-patient-cadavericdonor.html) | 
 `Patient` | 
 cadavericDonor | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-citizenship](extension-patient-citizenship.html) | 
 `Patient` | 
 citizenship | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-congregation](extension-patient-congregation.html) | 
 `Patient` | 
 congregation | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-disability](extension-patient-disability.html) | 
 `Patient` | 
 disability | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-genderIdentity](extension-patient-genderidentity.html) | 
 `Patient` | 
 genderIdentity | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-importance](extension-patient-importance.html) | 
 `Patient` | 
 importance | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-interpreterRequired](extension-patient-interpreterrequired.html) | 
 `Patient` | 
 interpreterRequired | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-mothersMaidenName](extension-patient-mothersmaidenname.html) | 
 `Patient` | 
 mothersMaidenName | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-nationality](extension-patient-nationality.html) | 
 `Patient` | 
 nationality | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-preferenceType](extension-patient-preferencetype.html) | 
 `Patient.communication.preferred` | 
 preferenceType | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-proficiency](extension-patient-proficiency.html) | 
 `Patient.communication` | 
 proficiency | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-relatedPerson](extension-patient-relatedperson.html) | 
 `Patient.contact` | 
 relatedPerson | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

 | 
 [patient-religion](extension-patient-religion.html) | 
 `Patient` | 
 religion | 
 for [Patient HL7 Extensions](patient-extensions.html) | 
 |

| Extensions for all resources or elements | |
 | 
 [resource-pertainsToGoal](extension-resource-pertainstogoal.html) | 
 pertainsToGoal | 
 for [Resource HL7 Extensions](resource-extensions.html) | 
 |

Extensions that reference this resource:

 | 
 [consent-Transcriber](extension-consent-transcriber.html) | 
 Transcriber | 
 for [Consent HL7 Extensions](consent-extensions.html) | 
 |

 | 
 [consent-Witness](extension-consent-witness.html) | 
 Witness | 
 for [Consent HL7 Extensions](consent-extensions.html) | 
 |

 | 
 [cqf-initiatingPerson](extension-cqf-initiatingperson.html) | 
 initiatingPerson | 
 for [Clinical Reasoning Extensions](clinicalreasoning-extensions.html) | 
 |

 | 
 [cqf-receivingPerson](extension-cqf-receivingperson.html) | 
 receivingPerson | 
 for [Clinical Reasoning Extensions](clinicalreasoning-extensions.html) | 
 |

 | 
 [familymemberhistory-patient-record](extension-familymemberhistory-patient-record.html) | 
 patient-record | 
 for [Family Member History HL7 Extensions](familymemberhistory-extensions.html) | 
 |

 | 
 [goal-acceptance](extension-goal-acceptance.html) | 
 acceptance | 
 for [FHIR Core Goal Profile](goal-extensions.html) | 
 |

 | 
 [procedure-directedBy](extension-procedure-directedby.html) | 
 directedBy | 
 for [Procedure HL7 Extensions](procedure-extensions.html) | 
 |

 | 
 [questionnaireresponse-author](extension-questionnaireresponse-author.html) | 
 author | 
 for [Core extensions for QuestionnaireResponse](questionnaireresponse-extensions.html) | 
 |

 | 
 [task-candidateList](extension-task-candidatelist.html) | 
 candidateList | 
 for [Task HL7 Extensions](task-extensions.html) | 
 |

| Extensions that refer to Any resource | |
 | 
 [cqf-relativeDateTime](extension-cqf-relativedatetime.html) | 
 relativeDateTime | 
 for [Clinical Reasoning Extensions](clinicalreasoning-extensions.html) | 
 |

 | 
 [event-basedOn](extension-event-basedon.html) | 
 basedOn | 
 for [Event Pattern HL7 Extensions](event-extensions.html) | 
 |

 | 
 [event-partOf](extension-event-partof.html) | 
 partOf | 
 for [Event Pattern HL7 Extensions](event-extensions.html) | 
 |

 | 
 [flag-detail](extension-flag-detail.html) | 
 detail | 
 for [Flag HL7 Extensions](flag-extensions.html) | 
 |

 | 
 [relative-date](extension-relative-date.html) | 
 Relative Date Criteria | 
 for [General Extensions for use by FHIR Implementers](general-extensions.html) | 
 |

 | 
 [replaces](extension-replaces.html) | 
 replaces | 
 for [General Extensions for use by FHIR Implementers](general-extensions.html) | 
 |

 | 
 [request-replaces](extension-request-replaces.html) | 
 replaces | 
 for [Request Pattern HL7 Extensions](request-extensions.html) | 
 |

 | 
 [workflow-supportingInfo](extension-workflow-supportinginfo.html) | 
 supportingInfo | 
 for [Workflow Pattern HL7 Extensions](workflow-extensions.html) | 
 |

### 8.1.16.3 Search Extensions [](patient-profiles.html#search)

| age | [number](search.html#number) | Searches for patients based on age as calculated based on current date and date of birth. Deceased patients are excluded from the search.**Expression:** | |

| birthOrderBoolean | [token](search.html#token) | Search based on whether a patient was part of a multiple birth or not.**Expression:** | |

| mothersMaidenName | [string](search.html#string) | Search based on patient's mother's maiden name**Expression:** Patient.extension('http://hl7.org/fhir/StructureDefinition/patient-extensions-Patient-mothersMaidenName') | |