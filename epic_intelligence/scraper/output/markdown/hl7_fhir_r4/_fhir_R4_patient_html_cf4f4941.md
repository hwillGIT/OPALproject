# Patient - FHIR v4.0.1An identifier for this patientWhether this patient record is in active use. 
Many systems use this property to mark as non-current patients, such as those that have not been seen for a period of time based on an organization's business rules.

It is often used to filter patient lists to exclude inactive patients

Deceased patients may also be marked as inactive for the same reasons, but may be active for some time after death (this element modifies the meaning of other elements)A name associated with the individualA contact detail (e.g. a telephone number or an email address) by which the individual may be contactedAdministrative Gender - the gender that the patient is considered to have for administration and record keeping purposesThe gender of a person used for administrative purposes. (Strength=Required)The date of birth for the individualIndicates if the individual is deceased or not (this element modifies the meaning of other elements)An address for the individualThis field contains a patient's most recent marital (civil) statusThe domestic partnership status of a person. (Strength=Extensible)Indicates whether the patient is part of a multiple (boolean) or indicates the actual birth order (integer)Image of the patientPatient's nominated care providerOrganization that is the custodian of the patient recordThe nature of the relationship between the patient and the contact personThe nature of the relationship between a patient and a contact person for that patient. (Strength=Extensible)A name associated with the contact personA contact detail for the person, e.g. a telephone number or an email addressAddress for the contact personAdministrative Gender - the gender that the contact person is considered to have for administration and record keeping purposesThe gender of a person used for administrative purposes. (Strength=Required)Organization on behalf of which the contact is acting or for which the contact is workingThe period during which this contact person or organization is valid to be contacted relating to this patientThe ISO-639-1 alpha 2 code in lower case for the language, optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g. "en" for English, or "en-US" for American English versus "en-EN" for England EnglishA human language. (Strength=Preferred)Indicates whether or not the patient prefers this language (over other languages he masters up a certain level)The other patient resource that the link refers toThe type of link between this patient resource and another patient resourceThe type of link between this patient resource and another patient resource. (Strength=Required)A contact party (e.g. guardian, partner, friend) for the patientA language which may be used to communicate with the patient about his or her healthLink to another patient resource that concerns the same actual patient (this element modifies the meaning of other elements)An identifier for this patientWhether this patient record is in active use. 
Many systems use this property to mark as non-current patients, such as those that have not been seen for a period of time based on an organization's business rules.

It is often used to filter patient lists to exclude inactive patients

Deceased patients may also be marked as inactive for the same reasons, but may be active for some time after death (this element modifies the meaning of other elements)A name associated with the individualA contact detail (e.g. a telephone number or an email address) by which the individual may be contactedAdministrative Gender - the gender that the patient is considered to have for administration and record keeping purposesThe gender of a person used for administrative purposes. (Strength=Required)The date of birth for the individualIndicates if the individual is deceased or not (this element modifies the meaning of other elements)An address for the individualThis field contains a patient's most recent marital (civil) statusThe domestic partnership status of a person. (Strength=Extensible)Indicates whether the patient is part of a multiple (boolean) or indicates the actual birth order (integer)Image of the patientPatient's nominated care providerOrganization that is the custodian of the patient recordThe nature of the relationship between the patient and the contact personThe nature of the relationship between a patient and a contact person for that patient. (Strength=Extensible)A name associated with the contact personA contact detail for the person, e.g. a telephone number or an email addressAddress for the contact personAdministrative Gender - the gender that the contact person is considered to have for administration and record keeping purposesThe gender of a person used for administrative purposes. (Strength=Required)Organization on behalf of which the contact is acting or for which the contact is workingThe period during which this contact person or organization is valid to be contacted relating to this patientThe ISO-639-1 alpha 2 code in lower case for the language, optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g. "en" for English, or "en-US" for American English versus "en-EN" for England EnglishA human language. (Strength=Preferred)Indicates whether or not the patient prefers this language (over other languages he masters up a certain level)The other patient resource that the link refers toThe type of link between this patient resource and another patient resourceThe type of link between this patient resource and another patient resource. (Strength=Required)A contact party (e.g. guardian, partner, friend) for the patientA language which may be used to communicate with the patient about his or her healthLink to another patient resource that concerns the same actual patient (this element modifies the meaning of other elements)

> Source: https://hl7.org/fhir/R4/patient.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/patient.html) [R4B](http://hl7.org/fhir/R4B/patient.html) **R4** [R3](http://hl7.org/fhir/STU3/patient.html) [R2](http://hl7.org/fhir/DSTU2/patient.html)
 

# 8.1 Resource Patient - Content [
](patient.html#8.1)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) | [Normative](versions.html#std-process) (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

 | 
 
 
 | 
 
 This page has been approved as part of an [ANSI ](https://www.ansi.org/) standard.
 See the [Patient](ansi-patient.html) Package for further details.
 | 
 |

Demographics and other administrative information about an individual or animal receiving care or other health-related services.

## 8.1.1 Scope and Usage [
](patient.html#scope)

This Resource covers data about patients and animals involved in a wide range of health-related activities, including:

- Curative activities

- Psychiatric care

- Social services

- Pregnancy care

- Nursing and assisted living

- Dietary services

- Tracking of personal health and exercise data

The data in the Resource covers the "who" information about the patient: its attributes are focused on the demographic
information necessary to support the administrative, financial and logistic procedures. A Patient record is generally 
created and maintained by each organization providing care for a patient. A patient or animal receiving care at multiple
organizations may therefore have its information present in multiple Patient Resources.

Not all concepts are included within the base resource (such as race, ethnicity, organ donor status, nationality, etc.), 
but may be found in [profiles](patient-profiles.html) defined for specific jurisdictions (e.g., US Meaningful Use Program) 
or [standard extensions](patient-extensions.html). Such fields vary widely between jurisdictions and often have different 
names and valuesets for the similar concepts, but they are not similar enough to be able to map and exchange.

This resource is referenced by [Annotation](datatypes.html#Annotation), [Signature](datatypes.html#Signature), [Account](account.html#Account), [AdverseEvent](adverseevent.html#AdverseEvent), [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance), [Appointment](appointment.html#Appointment), [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [AuditEvent](auditevent.html#AuditEvent), [Basic](basic.html#Basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct), [BodyStructure](bodystructure.html#BodyStructure), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Condition](condition.html#Condition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [Coverage](coverage.html#Coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [DetectedIssue](detectedissue.html#DetectedIssue), [Device](device.html#Device), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [Encounter](encounter.html#Encounter), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory), [Flag](flag.html#Flag), [Goal](goal.html#Goal), [Group](group.html#Group), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [ImmunizationEvaluation](immunizationevaluation.html#ImmunizationEvaluation), [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation), [Invoice](invoice.html#Invoice), [List](list.html#List), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MolecularSequence](molecularsequence.html#MolecularSequence), [NutritionOrder](nutritionorder.html#NutritionOrder), [Observation](observation.html#Observation), itself, [Person](person.html#Person), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RelatedPerson](relatedperson.html#RelatedPerson), [RequestGroup](requestgroup.html#RequestGroup), [ResearchSubject](researchsubject.html#ResearchSubject), [RiskAssessment](riskassessment.html#RiskAssessment), [Schedule](schedule.html#Schedule), [ServiceRequest](servicerequest.html#ServiceRequest), [Specimen](specimen.html#Specimen), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest), [Task](task.html#Task) and [VisionPrescription](visionprescription.html#VisionPrescription)

## 8.1.2 
Resource Content
 [
](patient.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Patient](patient-definitions.html#Patient) | [N](versions.html#std-process) | | [DomainResource](domainresource.html) | Information about an individual or animal receiving health care services**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](patient-definitions.html#Patient.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | An identifier for this patient
 | |

| [active](patient-definitions.html#Patient.active) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether this patient's record is in active use | |

| [name](patient-definitions.html#Patient.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [HumanName](datatypes.html#HumanName) | A name associated with the patient
 | |

| [telecom](patient-definitions.html#Patient.telecom) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the individual
 | |

| [gender](patient-definitions.html#Patient.gender) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | male | female | other | unknown
[AdministrativeGender](valueset-administrative-gender.html) ([Required](terminologies.html#required)) | |

| [birthDate](patient-definitions.html#Patient.birthDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [date](datatypes.html#date) | The date of birth for the individual | |

| [deceased[x]](patient-definitions.html#Patient.deceased_x_) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Indicates if the individual is deceased or not | |

| deceasedBoolean | | | [boolean](datatypes.html#boolean) | | |

| deceasedDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| [address](patient-definitions.html#Patient.address) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Address](datatypes.html#Address) | An address for the individual
 | |

| [maritalStatus](patient-definitions.html#Patient.maritalStatus) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Marital (civil) status of a patient
[MaritalStatus](valueset-marital-status.html) ([Extensible](terminologies.html#extensible)) | |

| [multipleBirth[x]](patient-definitions.html#Patient.multipleBirth_x_) | | 0..1 | | Whether patient is part of a multiple birth | |

| multipleBirthBoolean | | | [boolean](datatypes.html#boolean) | | |

| multipleBirthInteger | | | [integer](datatypes.html#integer) | | |

| [photo](patient-definitions.html#Patient.photo) | | 0..* | [Attachment](datatypes.html#Attachment) | Image of the patient
 | |

| [contact](patient-definitions.html#Patient.contact) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | A contact party (e.g. guardian, partner, friend) for the patient
+ Rule: SHALL at least contain a contact's details or a reference to an organization
 | |

| [relationship](patient-definitions.html#Patient.contact.relationship) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The kind of relationship
[Patient Contact Relationship ](valueset-patient-contactrelationship.html) ([Extensible](terminologies.html#extensible))
 | |

| [name](patient-definitions.html#Patient.contact.name) | | 0..1 | [HumanName](datatypes.html#HumanName) | A name associated with the contact person | |

| [telecom](patient-definitions.html#Patient.contact.telecom) | | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the person
 | |

| [address](patient-definitions.html#Patient.contact.address) | | 0..1 | [Address](datatypes.html#Address) | Address for the contact person | |

| [gender](patient-definitions.html#Patient.contact.gender) | | 0..1 | [code](datatypes.html#code) | male | female | other | unknown
[AdministrativeGender](valueset-administrative-gender.html) ([Required](terminologies.html#required)) | |

| [organization](patient-definitions.html#Patient.contact.organization) | [I](conformance-rules.html#constraints) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that is associated with the contact | |

| [period](patient-definitions.html#Patient.contact.period) | | 0..1 | [Period](datatypes.html#Period) | The period during which this contact person or organization is valid to be contacted relating to this patient | |

| [communication](patient-definitions.html#Patient.communication) | | 0..* | [BackboneElement](backboneelement.html) | A language which may be used to communicate with the patient about his or her health
 | |

| [language](patient-definitions.html#Patient.communication.language) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The language which can be used to communicate with the patient about his or her health
[Common Languages](valueset-languages.html) ([Preferred](terminologies.html#preferred) but limited to [AllLanguages](valueset-all-languages.html)) | |

| [preferred](patient-definitions.html#Patient.communication.preferred) | | 0..1 | [boolean](datatypes.html#boolean) | Language preference indicator | |

| [generalPractitioner](patient-definitions.html#Patient.generalPractitioner) | | 0..* | [Reference](references.html#Reference)([Organization](organization.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Patient's nominated primary care provider
 | |

| [managingOrganization](patient-definitions.html#Patient.managingOrganization) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that is the custodian of the patient record | |

| [link](patient-definitions.html#Patient.link) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | Link to another patient resource that concerns the same actual person
 | |

| [other](patient-definitions.html#Patient.link.other) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html)) | The other patient or related person resource that the link refers to | |

| [type](patient-definitions.html#Patient.link.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | replaced-by | replaces | refer | seealso
[LinkType](valueset-link-type.html) ([Required](terminologies.html#required)) | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Patient ([DomainResource](domainresource.html))[An identifier for this patientidentifier](patient-definitions.html#Patient.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether this patient record is in active use. 
Many systems use this property to mark as non-current patients, such as those that have not been seen for a period of time based on an organization's business rules.

It is often used to filter patient lists to exclude inactive patients

Deceased patients may also be marked as inactive for the same reasons, but may be active for some time after death (this element modifies the meaning of other elements)active](patient-definitions.html#Patient.active) : [boolean](datatypes.html#boolean) [0..1][A name associated with the individualname](patient-definitions.html#Patient.name) : [HumanName](datatypes.html#HumanName) [0..*][A contact detail (e.g. a telephone number or an email address) by which the individual may be contactedtelecom](patient-definitions.html#Patient.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Administrative Gender - the gender that the patient is considered to have for administration and record keeping purposesgender](patient-definitions.html#Patient.gender) : [code](datatypes.html#code) [0..1] « [The gender of a person used for administrative purposes. (Strength=Required)AdministrativeGender](valueset-administrative-gender.html)! »[The date of birth for the individualbirthDate](patient-definitions.html#Patient.birthDate) : [date](datatypes.html#date) [0..1][Indicates if the individual is deceased or not (this element modifies the meaning of other elements)deceased[x]](patient-definitions.html#Patient.deceased_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[dateTime](datatypes.html#dateTime) »[An address for the individualaddress](patient-definitions.html#Patient.address) : [Address](datatypes.html#Address) [0..*][This field contains a patient's most recent marital (civil) statusmaritalStatus](patient-definitions.html#Patient.maritalStatus) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The domestic partnership status of a person. (Strength=Extensible)Marital Status ](valueset-marital-status.html)+ »[Indicates whether the patient is part of a multiple (boolean) or indicates the actual birth order (integer)multipleBirth[x]](patient-definitions.html#Patient.multipleBirth_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[integer](datatypes.html#integer) »[Image of the patientphoto](patient-definitions.html#Patient.photo) : [Attachment](datatypes.html#Attachment) [0..*][Patient's nominated care providergeneralPractitioner](patient-definitions.html#Patient.generalPractitioner) : [Reference](references.html#Reference) [0..*] « [Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole) »[Organization that is the custodian of the patient recordmanagingOrganization](patient-definitions.html#Patient.managingOrganization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »Contact[The nature of the relationship between the patient and the contact personrelationship](patient-definitions.html#Patient.contact.relationship) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The nature of the relationship between a patient and a contact person for that patient. (Strength=Extensible)PatientContactRelationship](valueset-patient-contactrelationship.html)+ »[A name associated with the contact personname](patient-definitions.html#Patient.contact.name) : [HumanName](datatypes.html#HumanName) [0..1][A contact detail for the person, e.g. a telephone number or an email addresstelecom](patient-definitions.html#Patient.contact.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Address for the contact personaddress](patient-definitions.html#Patient.contact.address) : [Address](datatypes.html#Address) [0..1][Administrative Gender - the gender that the contact person is considered to have for administration and record keeping purposesgender](patient-definitions.html#Patient.contact.gender) : [code](datatypes.html#code) [0..1] « [The gender of a person used for administrative purposes. (Strength=Required)AdministrativeGender](valueset-administrative-gender.html)! »[Organization on behalf of which the contact is acting or for which the contact is workingorganization](patient-definitions.html#Patient.contact.organization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The period during which this contact person or organization is valid to be contacted relating to this patientperiod](patient-definitions.html#Patient.contact.period) : [Period](datatypes.html#Period) [0..1]Communication[The ISO-639-1 alpha 2 code in lower case for the language, optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g. "en" for English, or "en-US" for American English versus "en-EN" for England Englishlanguage](patient-definitions.html#Patient.communication.language) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [A human language. (Strength=Preferred)CommonLanguages](valueset-languages.html)? »[Indicates whether or not the patient prefers this language (over other languages he masters up a certain level)preferred](patient-definitions.html#Patient.communication.preferred) : [boolean](datatypes.html#boolean) [0..1]Link[The other patient resource that the link refers toother](patient-definitions.html#Patient.link.other) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »[The type of link between this patient resource and another patient resourcetype](patient-definitions.html#Patient.link.type) : [code](datatypes.html#code) [1..1] « [The type of link between this patient resource and another patient resource. (Strength=Required)LinkType](valueset-link-type.html)! »
[A contact party (e.g. guardian, partner, friend) for the patientcontact](patient-definitions.html#Patient.contact)[0..*][A language which may be used to communicate with the patient about his or her healthcommunication](patient-definitions.html#Patient.communication)[0..*][Link to another patient resource that concerns the same actual patient (this element modifies the meaning of other elements)link](patient-definitions.html#Patient.link)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Patient**](patient-definitions.html#Patient) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](patient-definitions.html#Patient.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [An identifier for this patient](terminologies.html#unbound) --></identifier>
 <[**active**](patient-definitions.html#Patient.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether this patient's record is in active use](terminologies.html#unbound) -->
 <[**name**](patient-definitions.html#Patient.name)><!-- **0..*** [HumanName](datatypes.html#HumanName) [A name associated with the patient](terminologies.html#unbound) --></name>
 <[**telecom**](patient-definitions.html#Patient.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the individual](terminologies.html#unbound) --></telecom>
 <[**gender**](patient-definitions.html#Patient.gender) value="[[code](datatypes.html#code)]"/><!-- **0..1** [male | female | other | unknown](valueset-administrative-gender.html) -->
 <[**birthDate**](patient-definitions.html#Patient.birthDate) value="[[date](datatypes.html#date)]"/><!-- **0..1** [The date of birth for the individual](terminologies.html#unbound) -->
 <[**deceased[x]**](patient-definitions.html#Patient.deceased[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[dateTime](datatypes.html#dateTime) [Indicates if the individual is deceased or not](terminologies.html#unbound) --></deceased[x]>
 <[**address**](patient-definitions.html#Patient.address)><!-- **0..*** [Address](datatypes.html#Address) [An address for the individual](terminologies.html#unbound) --></address>
 <[**maritalStatus**](patient-definitions.html#Patient.maritalStatus)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Marital (civil) status of a patient](valueset-marital-status.html) --></maritalStatus>
 <[**multipleBirth[x]**](patient-definitions.html#Patient.multipleBirth[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[integer](datatypes.html#integer) [Whether patient is part of a multiple birth](terminologies.html#unbound) --></multipleBirth[x]>
 <[**photo**](patient-definitions.html#Patient.photo)><!-- **0..*** [Attachment](datatypes.html#Attachment) [Image of the patient](terminologies.html#unbound) --></photo>
 <[**contact**](patient-definitions.html#Patient.contact)> <!-- **0..*** A contact party (e.g. guardian, partner, friend) for the patient -->
 <[**relationship**](patient-definitions.html#Patient.contact.relationship)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [The kind of relationship](valueset-patient-contactrelationship.html) --></relationship>
 <[**name**](patient-definitions.html#Patient.contact.name)><!-- **0..1** [HumanName](datatypes.html#HumanName) [A name associated with the contact person](terminologies.html#unbound) --></name>
 <[**telecom**](patient-definitions.html#Patient.contact.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the person](terminologies.html#unbound) --></telecom>
 <[**address**](patient-definitions.html#Patient.contact.address)><!-- **0..1** [Address](datatypes.html#Address) [Address for the contact person](terminologies.html#unbound) --></address>
 <[**gender**](patient-definitions.html#Patient.contact.gender) value="[[code](datatypes.html#code)]"/><!-- **0..1** [male | female | other | unknown](valueset-administrative-gender.html) -->
 <[**organization**](patient-definitions.html#Patient.contact.organization)><!-- ** 0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that is associated with the contact](terminologies.html#unbound) --></organization>
 <[**period**](patient-definitions.html#Patient.contact.period)><!-- **0..1** [Period](datatypes.html#Period) [The period during which this contact person or organization is valid to be contacted relating to this patient](terminologies.html#unbound) --></period>
 </contact>
 <[**communication**](patient-definitions.html#Patient.communication)> <!-- **0..*** A language which may be used to communicate with the patient about his or her health -->
 <[**language**](patient-definitions.html#Patient.communication.language)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [The language which can be used to communicate with the patient about his or her health](valueset-languages.html) --></language>
 <[**preferred**](patient-definitions.html#Patient.communication.preferred) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Language preference indicator](terminologies.html#unbound) -->
 </communication>
 <[**generalPractitioner**](patient-definitions.html#Patient.generalPractitioner)><!-- **0..*** [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)) [Patient's nominated primary care provider](terminologies.html#unbound) --></generalPractitioner>
 <[**managingOrganization**](patient-definitions.html#Patient.managingOrganization)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that is the custodian of the patient record](terminologies.html#unbound) --></managingOrganization>
 <[**link**](patient-definitions.html#Patient.link)> <!-- **0..*** Link to another patient resource that concerns the same actual person -->
 <[**other**](patient-definitions.html#Patient.link.other)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) [The other patient or related person resource that the link refers to](terminologies.html#unbound) --></other>
 <[**type**](patient-definitions.html#Patient.link.type) value="[[code](datatypes.html#code)]"/><!-- **1..1** [replaced-by | replaces | refer | seealso](valueset-link-type.html) -->
 </link>
</Patient>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Patient**](patient-definitions.html#Patient)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](patient-definitions.html#Patient.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [An identifier for this patient](terminologies.html#unbound)
 "[active](patient-definitions.html#Patient.active)" : <[boolean](datatypes.html#boolean)>, // [Whether this patient's record is in active use](terminologies.html#unbound)
 "[name](patient-definitions.html#Patient.name)" : [{ [HumanName](datatypes.html#HumanName) }], // [A name associated with the patient](terminologies.html#unbound)
 "[telecom](patient-definitions.html#Patient.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the individual](terminologies.html#unbound)
 "[gender](patient-definitions.html#Patient.gender)" : "<[code](datatypes.html#code)>", // [male | female | other | unknown](valueset-administrative-gender.html)
 "[birthDate](patient-definitions.html#Patient.birthDate)" : "<[date](datatypes.html#date)>", // [The date of birth for the individual](terminologies.html#unbound)
 // deceased[x]: Indicates if the individual is deceased or not. One of these 2:
 "[deceasedBoolean](patient-definitions.html#Patient.deceasedBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[deceasedDateTime](patient-definitions.html#Patient.deceasedDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[address](patient-definitions.html#Patient.address)" : [{ [Address](datatypes.html#Address) }], // [An address for the individual](terminologies.html#unbound)
 "[maritalStatus](patient-definitions.html#Patient.maritalStatus)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Marital (civil) status of a patient](valueset-marital-status.html)
 // multipleBirth[x]: Whether patient is part of a multiple birth. One of these 2:
 "[multipleBirthBoolean](patient-definitions.html#Patient.multipleBirthBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[multipleBirthInteger](patient-definitions.html#Patient.multipleBirthInteger)" : <[integer](datatypes.html#integer)>,
 "[photo](patient-definitions.html#Patient.photo)" : [{ [Attachment](datatypes.html#Attachment) }], // [Image of the patient](terminologies.html#unbound)
 "[contact](patient-definitions.html#Patient.contact)" : [{ // [A contact party (e.g. guardian, partner, friend) for the patient](terminologies.html#unbound)
 "[relationship](patient-definitions.html#Patient.contact.relationship)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [The kind of relationship](valueset-patient-contactrelationship.html)
 "[name](patient-definitions.html#Patient.contact.name)" : { [HumanName](datatypes.html#HumanName) }, // [A name associated with the contact person](terminologies.html#unbound)
 "[telecom](patient-definitions.html#Patient.contact.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the person](terminologies.html#unbound)
 "[address](patient-definitions.html#Patient.contact.address)" : { [Address](datatypes.html#Address) }, // [Address for the contact person](terminologies.html#unbound)
 "[gender](patient-definitions.html#Patient.contact.gender)" : "<[code](datatypes.html#code)>", // [male | female | other | unknown](valueset-administrative-gender.html)
 "[organization](patient-definitions.html#Patient.contact.organization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // **C?** [Organization that is associated with the contact](terminologies.html#unbound)
 "[period](patient-definitions.html#Patient.contact.period)" : { [Period](datatypes.html#Period) } // [The period during which this contact person or organization is valid to be contacted relating to this patient](terminologies.html#unbound)
 }],
 "[communication](patient-definitions.html#Patient.communication)" : [{ // [A language which may be used to communicate with the patient about his or her health](terminologies.html#unbound)
 "[language](patient-definitions.html#Patient.communication.language)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [The language which can be used to communicate with the patient about his or her health](valueset-languages.html)
 "[preferred](patient-definitions.html#Patient.communication.preferred)" : <[boolean](datatypes.html#boolean)> // [Language preference indicator](terminologies.html#unbound)
 }],
 "[generalPractitioner](patient-definitions.html#Patient.generalPractitioner)" : [{ [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)) }], // [Patient's nominated primary care provider](terminologies.html#unbound)
 "[managingOrganization](patient-definitions.html#Patient.managingOrganization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization that is the custodian of the patient record](terminologies.html#unbound)
 "[link](patient-definitions.html#Patient.link)" : [{ // [Link to another patient resource that concerns the same actual person](terminologies.html#unbound)
 "[other](patient-definitions.html#Patient.link.other)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // **R!** [The other patient or related person resource that the link refers to](terminologies.html#unbound)
 "[type](patient-definitions.html#Patient.link.type)" : "<[code](datatypes.html#code)>" // **R!** [replaced-by | replaces | refer | seealso](valueset-link-type.html)
 }]
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Patient**](patient-definitions.html#Patient);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Patient.identifier](patient-definitions.html#Patient.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* An identifier for this patient
 fhir:[Patient.active](patient-definitions.html#Patient.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether this patient's record is in active use
 fhir:[Patient.name](patient-definitions.html#Patient.name) [ [HumanName](datatypes.html#HumanName) ], ... ; # 0..* A name associated with the patient
 fhir:[Patient.telecom](patient-definitions.html#Patient.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the individual
 fhir:[Patient.gender](patient-definitions.html#Patient.gender) [ [code](datatypes.html#code) ]; # 0..1 male | female | other | unknown
 fhir:[Patient.birthDate](patient-definitions.html#Patient.birthDate) [ [date](datatypes.html#date) ]; # 0..1 The date of birth for the individual
 # [Patient.deceased[x]](patient-definitions.html#Patient.deceased[x]) : 0..1 Indicates if the individual is deceased or not. One of these 2
 fhir:[Patient.deceasedBoolean](patient-definitions.html#Patient.deceasedBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Patient.deceasedDateTime](patient-definitions.html#Patient.deceasedDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Patient.address](patient-definitions.html#Patient.address) [ [Address](datatypes.html#Address) ], ... ; # 0..* An address for the individual
 fhir:[Patient.maritalStatus](patient-definitions.html#Patient.maritalStatus) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Marital (civil) status of a patient
 # [Patient.multipleBirth[x]](patient-definitions.html#Patient.multipleBirth[x]) : 0..1 Whether patient is part of a multiple birth. One of these 2
 fhir:[Patient.multipleBirthBoolean](patient-definitions.html#Patient.multipleBirthBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Patient.multipleBirthInteger](patient-definitions.html#Patient.multipleBirthInteger) [ [integer](datatypes.html#integer) ]
 fhir:[Patient.photo](patient-definitions.html#Patient.photo) [ [Attachment](datatypes.html#Attachment) ], ... ; # 0..* Image of the patient
 fhir:[Patient.contact](patient-definitions.html#Patient.contact) [ # 0..* A contact party (e.g. guardian, partner, friend) for the patient
 fhir:[Patient.contact.relationship](patient-definitions.html#Patient.contact.relationship) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* The kind of relationship
 fhir:[Patient.contact.name](patient-definitions.html#Patient.contact.name) [ [HumanName](datatypes.html#HumanName) ]; # 0..1 A name associated with the contact person
 fhir:[Patient.contact.telecom](patient-definitions.html#Patient.contact.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the person
 fhir:[Patient.contact.address](patient-definitions.html#Patient.contact.address) [ [Address](datatypes.html#Address) ]; # 0..1 Address for the contact person
 fhir:[Patient.contact.gender](patient-definitions.html#Patient.contact.gender) [ [code](datatypes.html#code) ]; # 0..1 male | female | other | unknown
 fhir:[Patient.contact.organization](patient-definitions.html#Patient.contact.organization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that is associated with the contact
 fhir:[Patient.contact.period](patient-definitions.html#Patient.contact.period) [ [Period](datatypes.html#Period) ]; # 0..1 The period during which this contact person or organization is valid to be contacted relating to this patient
 ], ...;
 fhir:[Patient.communication](patient-definitions.html#Patient.communication) [ # 0..* A language which may be used to communicate with the patient about his or her health
 fhir:[Patient.communication.language](patient-definitions.html#Patient.communication.language) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 The language which can be used to communicate with the patient about his or her health
 fhir:[Patient.communication.preferred](patient-definitions.html#Patient.communication.preferred) [ [boolean](datatypes.html#boolean) ]; # 0..1 Language preference indicator
 ], ...;
 fhir:[Patient.generalPractitioner](patient-definitions.html#Patient.generalPractitioner) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ], ... ; # 0..* Patient's nominated primary care provider
 fhir:[Patient.managingOrganization](patient-definitions.html#Patient.managingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that is the custodian of the patient record
 fhir:[Patient.link](patient-definitions.html#Patient.link) [ # 0..* Link to another patient resource that concerns the same actual person
 fhir:[Patient.link.other](patient-definitions.html#Patient.link.other) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 1..1 The other patient or related person resource that the link refers to
 fhir:[Patient.link.type](patient-definitions.html#Patient.link.type) [ [code](datatypes.html#code) ]; # 1..1 replaced-by | replaces | refer | seealso
 ], ...;
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Patient](patient.html#Patient)
 | 
 | 
 |

 | 
 Patient.active | 
 
 

 Default Value "true" removed

 

 | 
 |

 | 
 Patient.gender | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1

 

 | 
 |

 | 
 Patient.contact.relationship | 
 
 

 - Change value set from http://terminology.hl7.org/ValueSet/v2-0131 to http://hl7.org/fhir/ValueSet/patient-contactrelationship

 

 | 
 |

 | 
 Patient.contact.gender | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1

 

 | 
 |

 | 
 Patient.communication.language | 
 
 

 - Change binding strength from extensible to preferred

 

 | 
 |

 | 
 Patient.generalPractitioner | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Patient.link.type | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/link-type to http://hl7.org/fhir/ValueSet/link-type|4.0.1

 

 | 
 |

 | 
 Patient.animal | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](patient.diff.xml) or [JSON](patient.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](patient-version-maps.html) (status = 16 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Patient](patient-definitions.html#Patient) | [N](versions.html#std-process) | | [DomainResource](domainresource.html) | Information about an individual or animal receiving health care services**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](patient-definitions.html#Patient.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | An identifier for this patient
 | |

| [active](patient-definitions.html#Patient.active) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether this patient's record is in active use | |

| [name](patient-definitions.html#Patient.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [HumanName](datatypes.html#HumanName) | A name associated with the patient
 | |

| [telecom](patient-definitions.html#Patient.telecom) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the individual
 | |

| [gender](patient-definitions.html#Patient.gender) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | male | female | other | unknown
[AdministrativeGender](valueset-administrative-gender.html) ([Required](terminologies.html#required)) | |

| [birthDate](patient-definitions.html#Patient.birthDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [date](datatypes.html#date) | The date of birth for the individual | |

| [deceased[x]](patient-definitions.html#Patient.deceased_x_) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Indicates if the individual is deceased or not | |

| deceasedBoolean | | | [boolean](datatypes.html#boolean) | | |

| deceasedDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| [address](patient-definitions.html#Patient.address) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Address](datatypes.html#Address) | An address for the individual
 | |

| [maritalStatus](patient-definitions.html#Patient.maritalStatus) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Marital (civil) status of a patient
[MaritalStatus](valueset-marital-status.html) ([Extensible](terminologies.html#extensible)) | |

| [multipleBirth[x]](patient-definitions.html#Patient.multipleBirth_x_) | | 0..1 | | Whether patient is part of a multiple birth | |

| multipleBirthBoolean | | | [boolean](datatypes.html#boolean) | | |

| multipleBirthInteger | | | [integer](datatypes.html#integer) | | |

| [photo](patient-definitions.html#Patient.photo) | | 0..* | [Attachment](datatypes.html#Attachment) | Image of the patient
 | |

| [contact](patient-definitions.html#Patient.contact) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | A contact party (e.g. guardian, partner, friend) for the patient
+ Rule: SHALL at least contain a contact's details or a reference to an organization
 | |

| [relationship](patient-definitions.html#Patient.contact.relationship) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The kind of relationship
[Patient Contact Relationship ](valueset-patient-contactrelationship.html) ([Extensible](terminologies.html#extensible))
 | |

| [name](patient-definitions.html#Patient.contact.name) | | 0..1 | [HumanName](datatypes.html#HumanName) | A name associated with the contact person | |

| [telecom](patient-definitions.html#Patient.contact.telecom) | | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the person
 | |

| [address](patient-definitions.html#Patient.contact.address) | | 0..1 | [Address](datatypes.html#Address) | Address for the contact person | |

| [gender](patient-definitions.html#Patient.contact.gender) | | 0..1 | [code](datatypes.html#code) | male | female | other | unknown
[AdministrativeGender](valueset-administrative-gender.html) ([Required](terminologies.html#required)) | |

| [organization](patient-definitions.html#Patient.contact.organization) | [I](conformance-rules.html#constraints) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that is associated with the contact | |

| [period](patient-definitions.html#Patient.contact.period) | | 0..1 | [Period](datatypes.html#Period) | The period during which this contact person or organization is valid to be contacted relating to this patient | |

| [communication](patient-definitions.html#Patient.communication) | | 0..* | [BackboneElement](backboneelement.html) | A language which may be used to communicate with the patient about his or her health
 | |

| [language](patient-definitions.html#Patient.communication.language) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The language which can be used to communicate with the patient about his or her health
[Common Languages](valueset-languages.html) ([Preferred](terminologies.html#preferred) but limited to [AllLanguages](valueset-all-languages.html)) | |

| [preferred](patient-definitions.html#Patient.communication.preferred) | | 0..1 | [boolean](datatypes.html#boolean) | Language preference indicator | |

| [generalPractitioner](patient-definitions.html#Patient.generalPractitioner) | | 0..* | [Reference](references.html#Reference)([Organization](organization.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Patient's nominated primary care provider
 | |

| [managingOrganization](patient-definitions.html#Patient.managingOrganization) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that is the custodian of the patient record | |

| [link](patient-definitions.html#Patient.link) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | Link to another patient resource that concerns the same actual person
 | |

| [other](patient-definitions.html#Patient.link.other) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html)) | The other patient or related person resource that the link refers to | |

| [type](patient-definitions.html#Patient.link.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | replaced-by | replaces | refer | seealso
[LinkType](valueset-link-type.html) ([Required](terminologies.html#required)) | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Patient ([DomainResource](domainresource.html))[An identifier for this patientidentifier](patient-definitions.html#Patient.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether this patient record is in active use. 
Many systems use this property to mark as non-current patients, such as those that have not been seen for a period of time based on an organization's business rules.

It is often used to filter patient lists to exclude inactive patients

Deceased patients may also be marked as inactive for the same reasons, but may be active for some time after death (this element modifies the meaning of other elements)active](patient-definitions.html#Patient.active) : [boolean](datatypes.html#boolean) [0..1][A name associated with the individualname](patient-definitions.html#Patient.name) : [HumanName](datatypes.html#HumanName) [0..*][A contact detail (e.g. a telephone number or an email address) by which the individual may be contactedtelecom](patient-definitions.html#Patient.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Administrative Gender - the gender that the patient is considered to have for administration and record keeping purposesgender](patient-definitions.html#Patient.gender) : [code](datatypes.html#code) [0..1] « [The gender of a person used for administrative purposes. (Strength=Required)AdministrativeGender](valueset-administrative-gender.html)! »[The date of birth for the individualbirthDate](patient-definitions.html#Patient.birthDate) : [date](datatypes.html#date) [0..1][Indicates if the individual is deceased or not (this element modifies the meaning of other elements)deceased[x]](patient-definitions.html#Patient.deceased_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[dateTime](datatypes.html#dateTime) »[An address for the individualaddress](patient-definitions.html#Patient.address) : [Address](datatypes.html#Address) [0..*][This field contains a patient's most recent marital (civil) statusmaritalStatus](patient-definitions.html#Patient.maritalStatus) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The domestic partnership status of a person. (Strength=Extensible)Marital Status ](valueset-marital-status.html)+ »[Indicates whether the patient is part of a multiple (boolean) or indicates the actual birth order (integer)multipleBirth[x]](patient-definitions.html#Patient.multipleBirth_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[integer](datatypes.html#integer) »[Image of the patientphoto](patient-definitions.html#Patient.photo) : [Attachment](datatypes.html#Attachment) [0..*][Patient's nominated care providergeneralPractitioner](patient-definitions.html#Patient.generalPractitioner) : [Reference](references.html#Reference) [0..*] « [Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole) »[Organization that is the custodian of the patient recordmanagingOrganization](patient-definitions.html#Patient.managingOrganization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »Contact[The nature of the relationship between the patient and the contact personrelationship](patient-definitions.html#Patient.contact.relationship) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The nature of the relationship between a patient and a contact person for that patient. (Strength=Extensible)PatientContactRelationship](valueset-patient-contactrelationship.html)+ »[A name associated with the contact personname](patient-definitions.html#Patient.contact.name) : [HumanName](datatypes.html#HumanName) [0..1][A contact detail for the person, e.g. a telephone number or an email addresstelecom](patient-definitions.html#Patient.contact.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Address for the contact personaddress](patient-definitions.html#Patient.contact.address) : [Address](datatypes.html#Address) [0..1][Administrative Gender - the gender that the contact person is considered to have for administration and record keeping purposesgender](patient-definitions.html#Patient.contact.gender) : [code](datatypes.html#code) [0..1] « [The gender of a person used for administrative purposes. (Strength=Required)AdministrativeGender](valueset-administrative-gender.html)! »[Organization on behalf of which the contact is acting or for which the contact is workingorganization](patient-definitions.html#Patient.contact.organization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The period during which this contact person or organization is valid to be contacted relating to this patientperiod](patient-definitions.html#Patient.contact.period) : [Period](datatypes.html#Period) [0..1]Communication[The ISO-639-1 alpha 2 code in lower case for the language, optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g. "en" for English, or "en-US" for American English versus "en-EN" for England Englishlanguage](patient-definitions.html#Patient.communication.language) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [A human language. (Strength=Preferred)CommonLanguages](valueset-languages.html)? »[Indicates whether or not the patient prefers this language (over other languages he masters up a certain level)preferred](patient-definitions.html#Patient.communication.preferred) : [boolean](datatypes.html#boolean) [0..1]Link[The other patient resource that the link refers toother](patient-definitions.html#Patient.link.other) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »[The type of link between this patient resource and another patient resourcetype](patient-definitions.html#Patient.link.type) : [code](datatypes.html#code) [1..1] « [The type of link between this patient resource and another patient resource. (Strength=Required)LinkType](valueset-link-type.html)! »
[A contact party (e.g. guardian, partner, friend) for the patientcontact](patient-definitions.html#Patient.contact)[0..*][A language which may be used to communicate with the patient about his or her healthcommunication](patient-definitions.html#Patient.communication)[0..*][Link to another patient resource that concerns the same actual patient (this element modifies the meaning of other elements)link](patient-definitions.html#Patient.link)[0..*]
 

**XML Template**

 

 
```
<[**Patient**](patient-definitions.html#Patient) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](patient-definitions.html#Patient.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [An identifier for this patient](terminologies.html#unbound) --></identifier>
 <[**active**](patient-definitions.html#Patient.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether this patient's record is in active use](terminologies.html#unbound) -->
 <[**name**](patient-definitions.html#Patient.name)><!-- **0..*** [HumanName](datatypes.html#HumanName) [A name associated with the patient](terminologies.html#unbound) --></name>
 <[**telecom**](patient-definitions.html#Patient.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the individual](terminologies.html#unbound) --></telecom>
 <[**gender**](patient-definitions.html#Patient.gender) value="[[code](datatypes.html#code)]"/><!-- **0..1** [male | female | other | unknown](valueset-administrative-gender.html) -->
 <[**birthDate**](patient-definitions.html#Patient.birthDate) value="[[date](datatypes.html#date)]"/><!-- **0..1** [The date of birth for the individual](terminologies.html#unbound) -->
 <[**deceased[x]**](patient-definitions.html#Patient.deceased[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[dateTime](datatypes.html#dateTime) [Indicates if the individual is deceased or not](terminologies.html#unbound) --></deceased[x]>
 <[**address**](patient-definitions.html#Patient.address)><!-- **0..*** [Address](datatypes.html#Address) [An address for the individual](terminologies.html#unbound) --></address>
 <[**maritalStatus**](patient-definitions.html#Patient.maritalStatus)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Marital (civil) status of a patient](valueset-marital-status.html) --></maritalStatus>
 <[**multipleBirth[x]**](patient-definitions.html#Patient.multipleBirth[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[integer](datatypes.html#integer) [Whether patient is part of a multiple birth](terminologies.html#unbound) --></multipleBirth[x]>
 <[**photo**](patient-definitions.html#Patient.photo)><!-- **0..*** [Attachment](datatypes.html#Attachment) [Image of the patient](terminologies.html#unbound) --></photo>
 <[**contact**](patient-definitions.html#Patient.contact)> <!-- **0..*** A contact party (e.g. guardian, partner, friend) for the patient -->
 <[**relationship**](patient-definitions.html#Patient.contact.relationship)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [The kind of relationship](valueset-patient-contactrelationship.html) --></relationship>
 <[**name**](patient-definitions.html#Patient.contact.name)><!-- **0..1** [HumanName](datatypes.html#HumanName) [A name associated with the contact person](terminologies.html#unbound) --></name>
 <[**telecom**](patient-definitions.html#Patient.contact.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the person](terminologies.html#unbound) --></telecom>
 <[**address**](patient-definitions.html#Patient.contact.address)><!-- **0..1** [Address](datatypes.html#Address) [Address for the contact person](terminologies.html#unbound) --></address>
 <[**gender**](patient-definitions.html#Patient.contact.gender) value="[[code](datatypes.html#code)]"/><!-- **0..1** [male | female | other | unknown](valueset-administrative-gender.html) -->
 <[**organization**](patient-definitions.html#Patient.contact.organization)><!-- ** 0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that is associated with the contact](terminologies.html#unbound) --></organization>
 <[**period**](patient-definitions.html#Patient.contact.period)><!-- **0..1** [Period](datatypes.html#Period) [The period during which this contact person or organization is valid to be contacted relating to this patient](terminologies.html#unbound) --></period>
 </contact>
 <[**communication**](patient-definitions.html#Patient.communication)> <!-- **0..*** A language which may be used to communicate with the patient about his or her health -->
 <[**language**](patient-definitions.html#Patient.communication.language)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [The language which can be used to communicate with the patient about his or her health](valueset-languages.html) --></language>
 <[**preferred**](patient-definitions.html#Patient.communication.preferred) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Language preference indicator](terminologies.html#unbound) -->
 </communication>
 <[**generalPractitioner**](patient-definitions.html#Patient.generalPractitioner)><!-- **0..*** [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)) [Patient's nominated primary care provider](terminologies.html#unbound) --></generalPractitioner>
 <[**managingOrganization**](patient-definitions.html#Patient.managingOrganization)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that is the custodian of the patient record](terminologies.html#unbound) --></managingOrganization>
 <[**link**](patient-definitions.html#Patient.link)> <!-- **0..*** Link to another patient resource that concerns the same actual person -->
 <[**other**](patient-definitions.html#Patient.link.other)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) [The other patient or related person resource that the link refers to](terminologies.html#unbound) --></other>
 <[**type**](patient-definitions.html#Patient.link.type) value="[[code](datatypes.html#code)]"/><!-- **1..1** [replaced-by | replaces | refer | seealso](valueset-link-type.html) -->
 </link>
</Patient>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Patient**](patient-definitions.html#Patient)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](patient-definitions.html#Patient.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [An identifier for this patient](terminologies.html#unbound)
 "[active](patient-definitions.html#Patient.active)" : <[boolean](datatypes.html#boolean)>, // [Whether this patient's record is in active use](terminologies.html#unbound)
 "[name](patient-definitions.html#Patient.name)" : [{ [HumanName](datatypes.html#HumanName) }], // [A name associated with the patient](terminologies.html#unbound)
 "[telecom](patient-definitions.html#Patient.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the individual](terminologies.html#unbound)
 "[gender](patient-definitions.html#Patient.gender)" : "<[code](datatypes.html#code)>", // [male | female | other | unknown](valueset-administrative-gender.html)
 "[birthDate](patient-definitions.html#Patient.birthDate)" : "<[date](datatypes.html#date)>", // [The date of birth for the individual](terminologies.html#unbound)
 // deceased[x]: Indicates if the individual is deceased or not. One of these 2:
 "[deceasedBoolean](patient-definitions.html#Patient.deceasedBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[deceasedDateTime](patient-definitions.html#Patient.deceasedDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[address](patient-definitions.html#Patient.address)" : [{ [Address](datatypes.html#Address) }], // [An address for the individual](terminologies.html#unbound)
 "[maritalStatus](patient-definitions.html#Patient.maritalStatus)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Marital (civil) status of a patient](valueset-marital-status.html)
 // multipleBirth[x]: Whether patient is part of a multiple birth. One of these 2:
 "[multipleBirthBoolean](patient-definitions.html#Patient.multipleBirthBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[multipleBirthInteger](patient-definitions.html#Patient.multipleBirthInteger)" : <[integer](datatypes.html#integer)>,
 "[photo](patient-definitions.html#Patient.photo)" : [{ [Attachment](datatypes.html#Attachment) }], // [Image of the patient](terminologies.html#unbound)
 "[contact](patient-definitions.html#Patient.contact)" : [{ // [A contact party (e.g. guardian, partner, friend) for the patient](terminologies.html#unbound)
 "[relationship](patient-definitions.html#Patient.contact.relationship)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [The kind of relationship](valueset-patient-contactrelationship.html)
 "[name](patient-definitions.html#Patient.contact.name)" : { [HumanName](datatypes.html#HumanName) }, // [A name associated with the contact person](terminologies.html#unbound)
 "[telecom](patient-definitions.html#Patient.contact.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the person](terminologies.html#unbound)
 "[address](patient-definitions.html#Patient.contact.address)" : { [Address](datatypes.html#Address) }, // [Address for the contact person](terminologies.html#unbound)
 "[gender](patient-definitions.html#Patient.contact.gender)" : "<[code](datatypes.html#code)>", // [male | female | other | unknown](valueset-administrative-gender.html)
 "[organization](patient-definitions.html#Patient.contact.organization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // **C?** [Organization that is associated with the contact](terminologies.html#unbound)
 "[period](patient-definitions.html#Patient.contact.period)" : { [Period](datatypes.html#Period) } // [The period during which this contact person or organization is valid to be contacted relating to this patient](terminologies.html#unbound)
 }],
 "[communication](patient-definitions.html#Patient.communication)" : [{ // [A language which may be used to communicate with the patient about his or her health](terminologies.html#unbound)
 "[language](patient-definitions.html#Patient.communication.language)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [The language which can be used to communicate with the patient about his or her health](valueset-languages.html)
 "[preferred](patient-definitions.html#Patient.communication.preferred)" : <[boolean](datatypes.html#boolean)> // [Language preference indicator](terminologies.html#unbound)
 }],
 "[generalPractitioner](patient-definitions.html#Patient.generalPractitioner)" : [{ [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)) }], // [Patient's nominated primary care provider](terminologies.html#unbound)
 "[managingOrganization](patient-definitions.html#Patient.managingOrganization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization that is the custodian of the patient record](terminologies.html#unbound)
 "[link](patient-definitions.html#Patient.link)" : [{ // [Link to another patient resource that concerns the same actual person](terminologies.html#unbound)
 "[other](patient-definitions.html#Patient.link.other)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // **R!** [The other patient or related person resource that the link refers to](terminologies.html#unbound)
 "[type](patient-definitions.html#Patient.link.type)" : "<[code](datatypes.html#code)>" // **R!** [replaced-by | replaces | refer | seealso](valueset-link-type.html)
 }]
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Patient**](patient-definitions.html#Patient);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Patient.identifier](patient-definitions.html#Patient.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* An identifier for this patient
 fhir:[Patient.active](patient-definitions.html#Patient.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether this patient's record is in active use
 fhir:[Patient.name](patient-definitions.html#Patient.name) [ [HumanName](datatypes.html#HumanName) ], ... ; # 0..* A name associated with the patient
 fhir:[Patient.telecom](patient-definitions.html#Patient.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the individual
 fhir:[Patient.gender](patient-definitions.html#Patient.gender) [ [code](datatypes.html#code) ]; # 0..1 male | female | other | unknown
 fhir:[Patient.birthDate](patient-definitions.html#Patient.birthDate) [ [date](datatypes.html#date) ]; # 0..1 The date of birth for the individual
 # [Patient.deceased[x]](patient-definitions.html#Patient.deceased[x]) : 0..1 Indicates if the individual is deceased or not. One of these 2
 fhir:[Patient.deceasedBoolean](patient-definitions.html#Patient.deceasedBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Patient.deceasedDateTime](patient-definitions.html#Patient.deceasedDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Patient.address](patient-definitions.html#Patient.address) [ [Address](datatypes.html#Address) ], ... ; # 0..* An address for the individual
 fhir:[Patient.maritalStatus](patient-definitions.html#Patient.maritalStatus) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Marital (civil) status of a patient
 # [Patient.multipleBirth[x]](patient-definitions.html#Patient.multipleBirth[x]) : 0..1 Whether patient is part of a multiple birth. One of these 2
 fhir:[Patient.multipleBirthBoolean](patient-definitions.html#Patient.multipleBirthBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Patient.multipleBirthInteger](patient-definitions.html#Patient.multipleBirthInteger) [ [integer](datatypes.html#integer) ]
 fhir:[Patient.photo](patient-definitions.html#Patient.photo) [ [Attachment](datatypes.html#Attachment) ], ... ; # 0..* Image of the patient
 fhir:[Patient.contact](patient-definitions.html#Patient.contact) [ # 0..* A contact party (e.g. guardian, partner, friend) for the patient
 fhir:[Patient.contact.relationship](patient-definitions.html#Patient.contact.relationship) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* The kind of relationship
 fhir:[Patient.contact.name](patient-definitions.html#Patient.contact.name) [ [HumanName](datatypes.html#HumanName) ]; # 0..1 A name associated with the contact person
 fhir:[Patient.contact.telecom](patient-definitions.html#Patient.contact.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the person
 fhir:[Patient.contact.address](patient-definitions.html#Patient.contact.address) [ [Address](datatypes.html#Address) ]; # 0..1 Address for the contact person
 fhir:[Patient.contact.gender](patient-definitions.html#Patient.contact.gender) [ [code](datatypes.html#code) ]; # 0..1 male | female | other | unknown
 fhir:[Patient.contact.organization](patient-definitions.html#Patient.contact.organization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that is associated with the contact
 fhir:[Patient.contact.period](patient-definitions.html#Patient.contact.period) [ [Period](datatypes.html#Period) ]; # 0..1 The period during which this contact person or organization is valid to be contacted relating to this patient
 ], ...;
 fhir:[Patient.communication](patient-definitions.html#Patient.communication) [ # 0..* A language which may be used to communicate with the patient about his or her health
 fhir:[Patient.communication.language](patient-definitions.html#Patient.communication.language) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 The language which can be used to communicate with the patient about his or her health
 fhir:[Patient.communication.preferred](patient-definitions.html#Patient.communication.preferred) [ [boolean](datatypes.html#boolean) ]; # 0..1 Language preference indicator
 ], ...;
 fhir:[Patient.generalPractitioner](patient-definitions.html#Patient.generalPractitioner) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ], ... ; # 0..* Patient's nominated primary care provider
 fhir:[Patient.managingOrganization](patient-definitions.html#Patient.managingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that is the custodian of the patient record
 fhir:[Patient.link](patient-definitions.html#Patient.link) [ # 0..* Link to another patient resource that concerns the same actual person
 fhir:[Patient.link.other](patient-definitions.html#Patient.link.other) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 1..1 The other patient or related person resource that the link refers to
 fhir:[Patient.link.type](patient-definitions.html#Patient.link.type) [ [code](datatypes.html#code) ]; # 1..1 replaced-by | replaces | refer | seealso
 ], ...;
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Patient](patient.html#Patient)
 | 
 | 
 |

 | 
 Patient.active | 
 
 

 Default Value "true" removed

 

 | 
 |

 | 
 Patient.gender | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1

 

 | 
 |

 | 
 Patient.contact.relationship | 
 
 

 - Change value set from http://terminology.hl7.org/ValueSet/v2-0131 to http://hl7.org/fhir/ValueSet/patient-contactrelationship

 

 | 
 |

 | 
 Patient.contact.gender | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1

 

 | 
 |

 | 
 Patient.communication.language | 
 
 

 - Change binding strength from extensible to preferred

 

 | 
 |

 | 
 Patient.generalPractitioner | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Patient.link.type | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/link-type to http://hl7.org/fhir/ValueSet/link-type|4.0.1

 

 | 
 |

 | 
 Patient.animal | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](patient.diff.xml) or [JSON](patient.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](patient-version-maps.html) (status = 16 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](patient-profiles.html) and the alternate definitions:
Master Definition [XML](patient.profile.xml.html) + [JSON](patient.profile.json.html),
[XML](xml.html) [Schema](patient.xsd)/[Schematron](patient.sch) + [JSON](json.html) 
[Schema](patient.schema.json.html), [ShEx](patient.shex.html) (for [Turtle](rdf.html)) + [see the extensions](patient-profiles.html) & the [dependency analysis](patient-dependencies.html)

### 8.1.2.1 
Terminology Bindings
 [
](patient.html#tx)

 | Path | Definition | Type | Reference | |

 | Patient.gender**Patient.contact.gender | The gender of a person used for administrative purposes. | [Required](terminologies.html#required) | [AdministrativeGender](valueset-administrative-gender.html) | |

 | Patient.maritalStatus | The domestic partnership status of a person. | [Extensible](terminologies.html#extensible) | [Marital Status Codes](valueset-marital-status.html) | |

 | Patient.contact.relationship | The nature of the relationship between a patient and a contact person for that patient. | [Extensible](terminologies.html#extensible) | [PatientContactRelationship](valueset-patient-contactrelationship.html) | |

 | Patient.communication.language | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) | |

 | Patient.link.type | The type of link between this patient resource and another patient resource. | [Required](terminologies.html#required) | [LinkType](valueset-link-type.html) | |

 

 

### 8.1.2.2 Constraints [
](patient.html#invs)

| id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **pat-1** | [Rule](conformance-rules.html#rule) | Patient.contact | SHALL at least contain a contact's details or a reference to an organization | name.exists() or telecom.exists() or address.exists() or organization.exists() | |

Notes:

- multipleBirth can be either expressed as a Boolean (just indicating whether the patient is part of a multiple birth) or as an integer, indicating the actual birth order.

- Patient records may only be in one of two statuses: in use (active=true) and not in use (active=false). 
A normal record is active, i.e. it is in use. Active is set to 'false' when a record is created as a duplicate or in error. 
A record does not need to be linked to be inactivated.

- The link* element is used to assert that two or more Patient resources are both about the same actual patient. 
See below for further discussion

- There should be only one preferred language (Language.preference = true) per mode of expression.

- The Contact for a Patient has an element *organization*, this is for use with guardians or business related contacts where just the organization is relevant.

## 8.1.3 Patient ids and Patient resource ids [
](patient.html#ids)

A Patient record's [Resource Id](resource.html#id) can never change. For this reason, the identifiers with 
which humans are concerned (often called MRN - Medical Record Number, or UR - Unit Record) should not 
be used for the resource's id, since MRN's may change, i.e. as a result of having duplicate records of
the same patient. Instead they should be represented in the *Patient.identifier* 
list where they can be managed. This is also useful for the case of institutions that have acquired 
multiple numbers because of mergers of patient record systems over time.

Where there is a need to implement an automated MRN Identifier created for a patient record, this could be achieved by providing an identifier in the patient with an appropriate assigner, MRN Type and/or system but with *no value* assigned. Internal business rules can then detect this and replace/populate this identifier with 1 or more identifiers (as required).

## 8.1.4 Linking Patients [
](patient.html#links)

The *link* element is used to assert that patient resources refer to the same patient. This element is used
to support the following scenarios where multiple patient records exist:

### 8.1.4.1 Duplicate Patient records [
](patient.html#dup-records)

Managing Patient registration is a well-known difficult problem. Around 2% of registrations are in error, 
mostly duplicate records. Sometimes the duplicate record is caught fairly quickly and retired before much 
data is accumulated. In other cases, substantial amounts of data may accumulate. By using a link of type 'replaced-by',
the record containing such a link is marked as a duplicate and the link points forward to a record that should
be used instead. Note that the record pointed to may in its turn have been identified as created in error and forward
to yet another Patient resource. Records that replace another record *may* use a link type of 'replaces' pointing to the old record.

### 8.1.4.2 Patient record in a Patient index [
](patient.html#rec-ind)

A Patient record may be present in a system that acts as a Patient Index: it maintains a (summary of) patient data and
a list of one or more servers that are known to hold a more comprehensive and/or authoritative record of the same patient.
The link type 'refer' is used to denote such a link. Note that linked records may contain contradictory information. The
record referred to does not point back to the referring record.

### 8.1.4.3 Distributed Patient record [
](patient.html#distributed)

In a distributed architecture, multiple systems keep separate patient records concerning the same patient. These
records are not considered duplicates, but contain a distributed, potentially overlapping view of the patient's data.
Each such record may have its own focus or maintaining organization and there need not be a sense of one record
being more complete or more authoritative than another. In such cases, links of type 'see also' can be used to point to
other patient records. It is not a requirement that such links are bilateral. 

## 8.1.5 Patient vs. Person vs. Patient.Link vs. Linkage [
](patient.html#linking)

The Person resource on the surface appears to be very similar to the Patient resource, and the usage for it is very similar
to using the Patient.Link capability.**
The intention of the Person resource is to be able to link instances of resources together that are believed to be the same
individual. This includes across resource types, such as RelatedPerson, Practitioner, Patient and even other Person resources.

The Patient Link however is only intended to be used for Patient resources.

The primary use case for the Person resource is to be able to support person registries that do not necessarily have a
healthcare context, and are able to identify and quantify confidence levels that this is the same person.

This could include consumer portals where the maintainer of the person information is the actual person themselves.

A system could use the Person entry to cross check changes to information applied to one part of a record to values in another
system; e.g., when moving, a consumer updates his contact numbers and address in his person record, and then a Patient Administration
system is able to see that this data is changed and prompt the organization to follow up with the patient that was linked to
the person record if they want their details updated, or if they no longer need services and they should be cancelled, 
as they've moved from the area.

The [Linkage](linkage.html) resource and the Patient.link property conceptually perform similar functions in FHIR, 
both provide an assertion of linkages between multiple resource instances that are referring to the same underlying individual.

When a Patient resource is linked/merged then it needs to have an internal indication that there is another
patient resource that should be considered when referencing other records, which is achieved using the patient.link property.

Not detecting/checking for a potential linkage could mean that related clinical records are not discovered, potentially impacting patient safety.
(which is why using the Linkage resource is not appropriate, as its use in this manner would force the use of either another
query to potentially locate other patient resources to consider, or use _revinclude)

## 8.1.6 Patient.contact vs. RelatedPerson [
](patient.html#contact)

The contact element on the Patient resource should be used for storing the details of people to contact. This information always travels with the Patient resource, and cannot be used as the target of a reference.

Where related people need to be referenced by other resources (e.g. CarePlan.participant, Encounter.participant, DocumentReference.author, Appointment.participant), the RelatedPerson resource must be used.

It is not expected that these records will be used for recording the primary care provider; this information should be stored in
the Patient.generalPractitioner field.

## 8.1.7 Patient Gender and Sex [
](patient.html#gender)

Many systems and organizations only provide for a single attribute that aspires to represent all aspects of a patient's gender and sex with a single value. However, there are many considerations around sex and gender documentation and interoperability. Listed below are the various social and biological attributes that are relevant in the healthcare setting, as well as information on how each can be communicated.

 - Administrative Gender** - in order to interoperate with systems that use a single generic property, the basic [Patient.gender](patient-definitions.html#Patient.gender) property represents an administrative gender: the gender that the patient is considered to have for administration and record keeping purposes. This property is often used as an input to patient matching algorithms, for example.

In addition to this administrative gender, other kinds of gender or sex properties may be represented:

 - **Clinical Sex** - a testable observation about a biological property of the patient. There are several different types of clinical sex, including karyotypic/genetic/chromosomal, gonadal, ductal, phenotypic, etc. Clinical sex observations should be represented using [Observation](observation.html), qualified with the appropriate clinical codes from LOINC and/or SNOMED.
 

 - **Clinical Gender** - an observation about the patient, often collected as part of social history documentation, and represented as an [Observation](observation.html)([example](observation-example-clinical-gender.html)) using, for example, the LOINC code [76691-5 ](http://loinc.org/76691-5). Clinical gender observations can provide both history and confidentiality, where the [genderIdentity](extension-patient-genderidentity.html) extension does not. 
 

 - **Gender Identity** - an indication from the patient about what gender they consider themselves to be. This can influence how the patient prefers to be addressed by care providers and other individuals. The standard [genderIdentity](extension-patient-genderidentity.html) extension may be used to communicate this property. This extension is appropriate when the gender identity is openly known.
 

 - **Sex assigned at Birth** - the sex assigned at birth, as documented on the birth registration. Some countries allow variations such as not yet determined, unknown, or undifferentiated, while others do not. Some countries also allow birth registration information to be updated. The US realm defines a US specific extension for this property.
 Alternatively, if you were representing this concept with an observation, you could use the LOINC code [76689-9 ](http://loinc.org/76689-9).
 

 - **Legal Sex** - regional and national entities often categorize citizens using a single legal sex value. The legal sex of a patient can vary from region to region and country to country. A single patient may have multiple legal sex values at the same time in different jurisdictions. In case where the Patient.gender administrative property is not sufficient to communicate legal sex, realm specific extensions should be used.
 

For veterinary use, the animal extension also includes the genderStatus which indicates sterility information.

## 8.1.8 Mother and newborn relationships [
](patient.html#maternity)

There are several ways to represent the relationship between a mother and a child.
This is due to the when it is recorded and the purpose for which it is recorded:

 

 - To express the family relationship and legal responsibility thereof for 
 administrative purposes: use the Patient/RelatedPerson structure.**
 This structure is consistent over time.

 - To relate the encounters of a mother and her baby in a maternity encounter,
 for administrative and billing purposes: use the [encounter.partof](encounter-definitions.html#Encounter.partOf) property

 - To collect information about the patient's relatives that might be relevant
 to the patient's medical condition: use the [FamilyMemberHistory](familymemberhistory.html) resource

 

During a maternity encounter, the Patient and Encounter resources for the mother will be present.
After the child is born, new Patient, Encounter and RelatedPerson (for the mother) records will be created.
The Child's encounter should reference the Mother's encounter using the partOf property.

The Patient/RelatedPerson structure should also be created for ongoing usage, as shown in this example:

```
<Patient>
 <id value="child"/>
 <!-- The details of the child -->
</Patient>
<RelatedPerson>
 <id value="rp-mom"/>
 <patient>
 <reference value="Patient/child"/>
 </patient>
</RelatedPerson>
<Patient>
 <id value="pat-mom"/>
 <!-- The details of the mom -->
 <link>
 <other value="rp-mom"/>
 <type value="see-also"/>
 </link>
</Patient>
<Encounter>
 <id value="mom-enc"/>
 <status value="in-progress"/>
 <class value="inpatient"/>
 <patient>
 <reference value="Patient/mom"/>
 </patient>
</Encounter>
<Encounter>
 <id value="child-enc"/>
 <status value="in-progress"/>
 <class value="inpatient"/>
 <patient>
 <reference value="Patient/child"/>
 </patient>
 <partOf>
 <reference value="Encounter/mom-enc"/>
 </partOf>
</Encounter>

```

 

## 8.1.9 Merging records [
](patient.html#merge)

This specification does not specify merge functionality: if multiple patient records are found to be 
duplicates, they can be linked together, as described above. These links merely express the relationship
between records, and in the case of a replacement link, indicate a "master" record. This specification
does not mandate that FHIR servers migrate information between such records on finding such a link. Note:

 - Health information administrators may call the process "merging", but it is often implemented as "linking" at the record level

 - Servers are allowed to implement merging/record migration even though it is not mandated. 

> 

Note:** We are seeking input from the implementer community on what effect linking/merging/unlinking should have on 
other functionality such as the GET operation, searching, reverse includes, etc.;**
How should an unlink behavior be done?

How will the patient compartment interact with the merge?

This functionality and related behaviors is subject to ongoing experimentation and implementation testing, 
with a definition to be proposed in a future version of this specification.

Feedback [here ](http://hl7.org/fhir-issues).

## 8.1.10 Patient Matching using an MPI [
](patient.html#match)

A Master Patient Index ([MPI ](http://en.wikipedia.org/wiki/Enterprise_master_patient_index))
is a service used to manage patient identification in a context
where multiple patient databases exist. Healthcare applications and middleware use the 
MPI to match patients between the databases, and as new patient details are encountered.
MPIs are highly specialized applications, often tailored extensively to the institution's 
particular mix of patients. MPIs can also be run on a regional and national basis. 

To ask an MPI to match a patient, clients call the patient [$match](patient-operation-match.html) operation,
which processes a parameters resource containing a complete or fragment of a patient resource, along with some other control parameters.

This provided patient resource does not need to pass full validation (mandatory fields, or invariants) as the resource will not be stored,
it does however need to be a parsable instance.
 
The MPI can then use the properties of the resource as MPI inputs, and process them using an internal MPI algorithm of some kind to determine the most appropriate matches 
in the patient set. It does not have to use all the properties provided, and may ignore others provided quietly.

A specific profile (with the required fields/invariants) can be used to define what parameters the MPI algorithm requires.

```
 POST [base]/Patient/$match
 [some headers including content-type xml or json]
 [parameters body with patient resource inside]

```

The response from an MPI $match operation is a set of patient records, ordered from most
likely to least likely. If there are not patient matches, the MPI SHALL return 
an empty search set with no error, but may include an [operation outcome](operationoutcome.html) with 
further advice. All patient records should have a score from 0 to 1, where
1 is the most certain match, along with an [extension](extensibility.html)
["match-grade"](extension-match-grade.html) that indicates the MPI's position on the match quality:

```
 <entry> 
 <resource>
 <Patient>
 <!-- patient details -->
 </Patient>
 </resource>
 <search>
 <extension url="http://hl7.org/fhir/StructureDefinition/match-grade">
 <valueCode value="probable"/>
 </extension>
 <score value="0.80"/>
 </search>
 </entry> 

```

The match-grade extension has one of the [following codes](valueset-match-grade.html):

 | certain | This record meets the matching criteria to be automatically considered as a full match. | |

 | probable | This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required before using this as a match. | |

 | possible | This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as a match. | |

 | certainly-not | This record is known not to be a match. Note that usually non-matching records are not returned, but in some cases records previously or likely considered as a match may specifically be negated by the matching engine. | |

 The purpose of using an MPI search versus a regular search is that the MPI search is really intended to target and 
 find a specific single patient for recording information about reducing errors through incorrectly selecting the
 wrong patient. Often MPIs won't return data if there is insufficient search parameter data, such as a partial surname.

 This compares to a regular search which can be used for finding lists of patients, such as to locate a group of patients
 that share a property in common, such as live in a specific location, or fit within an age range for performing population analysis.

 

A [formal definition](operation-patient-match.html) for the MPI $match operation is published.

## 8.1.11 Veterinary Care [
](patient.html#veterinary)

Veterinary care is very much within the scope of FHIR, and the Patient resource can be used to communicate information about animal patients. To support this, there is a standard [patient-animal extension](extension-patient-animal.html) which can be used for recording details about species, breed, and gender status. This extension is not intended to cover all relevant properties for veterinary care, and the use of additional domain-relevant extensions is expected for areas such as laboratory, zoological and livestock care.

The veterinary client ("owner") is represented using the RelatedPerson resource.

## 8.1.12 Search Parameters [
](patient.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| Name** | **Type** | **Description** | **Expression** | **In Common** | |

| active [TU](versions.html#std-process) | [token](search.html#token) | Whether the patient record is active | Patient.active | | |

| address [TU](versions.html#std-process) | [string](search.html#string) | A server defined search that may match any of the string fields in the Address, including line, city, district, state, country, postalCode, and/or text | Patient.address | [3 Resources](searchparameter-registry.html#individual-address) | |

| address-city [TU](versions.html#std-process) | [string](search.html#string) | A city specified in an address | Patient.address.city | [3 Resources](searchparameter-registry.html#individual-address-city) | |

| address-country [TU](versions.html#std-process) | [string](search.html#string) | A country specified in an address | Patient.address.country | [3 Resources](searchparameter-registry.html#individual-address-country) | |

| address-postalcode [TU](versions.html#std-process) | [string](search.html#string) | A postalCode specified in an address | Patient.address.postalCode | [3 Resources](searchparameter-registry.html#individual-address-postalcode) | |

| address-state [TU](versions.html#std-process) | [string](search.html#string) | A state specified in an address | Patient.address.state | [3 Resources](searchparameter-registry.html#individual-address-state) | |

| address-use [TU](versions.html#std-process) | [token](search.html#token) | A use code specified in an address | Patient.address.use | [3 Resources](searchparameter-registry.html#individual-address-use) | |

| birthdate [TU](versions.html#std-process) | [date](search.html#date) | The patient's date of birth | Patient.birthDate | [2 Resources](searchparameter-registry.html#individual-birthdate) | |

| death-date [TU](versions.html#std-process) | [date](search.html#date) | The date of death has been provided and satisfies this search value | (Patient.deceased as dateTime) | | |

| deceased [TU](versions.html#std-process) | [token](search.html#token) | This patient has been marked as deceased, or as a death date entered | Patient.deceased.exists() and Patient.deceased != false | | |

| email [TU](versions.html#std-process) | [token](search.html#token) | A value in an email contact | Patient.telecom.where(system='email') | [4 Resources](searchparameter-registry.html#individual-email) | |

| family [TU](versions.html#std-process) | [string](search.html#string) | A portion of the family name of the patient | Patient.name.family | [1 Resources](searchparameter-registry.html#individual-family) | |

| gender [TU](versions.html#std-process) | [token](search.html#token) | Gender of the patient | Patient.gender | [3 Resources](searchparameter-registry.html#individual-gender) | |

| general-practitioner [TU](versions.html#std-process) | [reference](search.html#reference) | Patient's nominated general practitioner, not the organization that manages the record | Patient.generalPractitioner
([Practitioner](practitioner.html), [Organization](organization.html), [PractitionerRole](practitionerrole.html)) | | |

| given [TU](versions.html#std-process) | [string](search.html#string) | A portion of the given name of the patient | Patient.name.given | [1 Resources](searchparameter-registry.html#individual-given) | |

| identifier [TU](versions.html#std-process) | [token](search.html#token) | A patient identifier | Patient.identifier | | |

| language [TU](versions.html#std-process) | [token](search.html#token) | Language code (irrespective of use value) | Patient.communication.language | | |

| link [TU](versions.html#std-process) | [reference](search.html#reference) | All patients linked to the given patient | Patient.link.other
([Patient](patient.html), [RelatedPerson](relatedperson.html)) | | |

| name [TU](versions.html#std-process) | [string](search.html#string) | A server defined search that may match any of the string fields in the HumanName, including family, give, prefix, suffix, suffix, and/or text | Patient.name | | |

| organization [TU](versions.html#std-process) | [reference](search.html#reference) | The organization that is the custodian of the patient record | Patient.managingOrganization
([Organization](organization.html)) | | |

| phone [TU](versions.html#std-process) | [token](search.html#token) | A value in a phone contact | Patient.telecom.where(system='phone') | [4 Resources](searchparameter-registry.html#individual-phone) | |

| phonetic [TU](versions.html#std-process) | [string](search.html#string) | A portion of either family or given name using some kind of phonetic matching algorithm | Patient.name | [3 Resources](searchparameter-registry.html#individual-phonetic) | |

| telecom [TU](versions.html#std-process) | [token](search.html#token) | The value in any kind of telecom details of the patient | Patient.telecom | [4 Resources](searchparameter-registry.html#individual-telecom) | |