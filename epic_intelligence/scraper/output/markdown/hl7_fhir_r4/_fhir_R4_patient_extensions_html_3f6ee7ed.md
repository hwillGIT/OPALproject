# Patient-extensions - FHIR v4.0.1

> Source: https://hl7.org/fhir/R4/patient-extensions.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: **R4** [R3](http://hl7.org/fhir/STU3/patient-extensions.html) [R2](http://hl7.org/fhir/DSTU2/patient-extensions.html)
 

## 8.1.19 Patient HL7 Extensions [
](patient-extensions.html#8.1.19)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): N/A | [Standards Status](versions.html#levels): Informative | | |

Defines common extensions used with or related to the Patient resource

### 8.1.19.1 Content [](patient-extensions.html#content)

| **Extensions**: | |
| [patient-mothersMaidenName](extension-patient-mothersmaidenname.html) | **mothersMaidenName** : Mother's maiden (unmarried) name, commonly collected to help verify patient identity.

 | |
| [patient-birthPlace](extension-patient-birthplace.html) | **birthPlace** : 
The registered place of birth of the patient. A sytem may use the address.text if they don't store the birthPlace address in discrete elements.

 | |
| [patient-birthTime](extension-patient-birthtime.html) | **birthTime** : 
The time of day that the Patient was born. This includes the date to ensure that the timezone information can be communicated effectively.

 | |
| [patient-nationality](extension-patient-nationality.html) | **nationality** : 
The nationality of the patient.

 | |
| [patient-citizenship](extension-patient-citizenship.html) | **citizenship** : 
The patient's legal status as citizen of a country.

 | |
| [patient-cadavericDonor](extension-patient-cadavericdonor.html) | **cadavericDonor** : 
Flag indicating whether the patient authorized the donation of body parts after death.

 | |
| [patient-congregation](extension-patient-congregation.html) | **congregation** : 
A group or place of religious practice that may provide services to the patient.

 | |
| [patient-adoptionInfo](extension-patient-adoptioninfo.html) | **adoptionInfo** : 
Code indication the adoption status of the patient.

 | |
| [patient-disability](extension-patient-disability.html) | **disability** : 
Value(s) identifying physical or mental condition(s) that limits a person's movements, senses, or activities.

 | |
| [patient-importance](extension-patient-importance.html) | **importance** : 
The importance of the patient (e.g. VIP).

 | |
| [patient-interpreterRequired](extension-patient-interpreterrequired.html) | **interpreterRequired** : 
This Patient requires an interpreter to communicate healthcare information to the practitioner.

 | |
| [patient-religion](extension-patient-religion.html) | **religion** : 
The patient's professed religious affiliations.

 | |
| [patient-relatedPerson](extension-patient-relatedperson.html) | **relatedPerson** : 
In some cases a Patient.contact will also be populated as a RelatedPerson resource. This linkage permits the linkage between the 2 resources to be able to accurately indicate a representation of the same individual, and updating details between could be appropriate.

 | |
| [patient-genderIdentity](extension-patient-genderidentity.html) | **genderIdentity** : 
The gender the patient identifies with. The Patient's gender identity is used as guidance (e.g. for staff) about how to interact with the patient.

 | |
| [patient-preferenceType](extension-patient-preferencetype.html) | **preferenceType** : 
Indicates what mode of communication the patient prefers to use for the indicated language.

 | |
| [patient-animal](extension-patient-animal.html) | **animal** : 
This patient is known to be an animal.

 | |
| [patient-proficiency](extension-patient-proficiency.html) | **proficiency** : 
Proficiency level of the communication.

 | |

 

### 8.1.19.2 Search Parameters [
](patient-extensions.html#search)

Search parameters defined by this package. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Paths** | **Source** | |

| age | [number](search.html#number) | Searches for patients based on age as calculated based on current date and date of birth. Deceased patients are excluded from the search. | f:Patient/f:birthDate | [XML](patient-extensions-Patient-age.xml.html) / [JSON](patient-extensions-Patient-age.json.html) | |

| birthOrderBoolean | [token](search.html#token) | Search based on whether a patient was part of a multiple birth or not. | f:Patient/f:multipleBirthBoolean | f:Patient/f:multipleBirthInteger | [XML](patient-extensions-Patient-birthOrderBoolean.xml.html) / [JSON](patient-extensions-Patient-birthOrderBoolean.json.html) | |

| mothersMaidenName | [string](search.html#string) | Search based on patient's mother's maiden name | | [XML](patient-extensions-Patient-mothersMaidenName.xml.html) / [JSON](patient-extensions-Patient-mothersMaidenName.json.html) | |