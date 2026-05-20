# Practitioner - FHIR v4.0.1An identifier that applies to this person in this roleWhether this practitioner's record is in active useThe name(s) associated with the practitionerA contact detail for the practitioner, e.g. a telephone number or an email addressAddress(es) of the practitioner that are not role specific (typically home address). 
Work addresses are not typically entered in this property as they are usually role dependentAdministrative Gender - the gender that the person is considered to have for administration and record keeping purposesThe gender of a person used for administrative purposes. (Strength=Required)The date of birth for the practitionerImage of the personA language the practitioner can use in patient communicationA human language. (Strength=Preferred)An identifier that applies to this person's qualification in this roleCoded representation of the qualificationSpecific qualification the practitioner has to provide a service. (Strength=Example)Period during which the qualification is validOrganization that regulates and issues the qualificationThe official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner.  For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian localityAn identifier that applies to this person in this roleWhether this practitioner's record is in active useThe name(s) associated with the practitionerA contact detail for the practitioner, e.g. a telephone number or an email addressAddress(es) of the practitioner that are not role specific (typically home address). 
Work addresses are not typically entered in this property as they are usually role dependentAdministrative Gender - the gender that the person is considered to have for administration and record keeping purposesThe gender of a person used for administrative purposes. (Strength=Required)The date of birth for the practitionerImage of the personA language the practitioner can use in patient communicationA human language. (Strength=Preferred)An identifier that applies to this person's qualification in this roleCoded representation of the qualificationSpecific qualification the practitioner has to provide a service. (Strength=Example)Period during which the qualification is validOrganization that regulates and issues the qualificationThe official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner.  For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian locality

> Source: https://hl7.org/fhir/R4/practitioner.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/practitioner.html) [R4B](http://hl7.org/fhir/R4B/practitioner.html) **R4** [R3](http://hl7.org/fhir/STU3/practitioner.html) [R2](http://hl7.org/fhir/DSTU2/practitioner.html)
 

# 8.4 Resource Practitioner - Content [
](practitioner.html#8.4)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Individual | [Compartments](compartmentdefinition.html): [Practitioner](compartmentdefinition-practitioner.html) | |

A person who is directly or indirectly involved in the provisioning of healthcare.

## 8.4.1 Scope and Usage [
](practitioner.html#scope)

Practitioner covers all individuals who are engaged in the healthcare process and healthcare-related services as part of their formal 
responsibilities and this Resource is used for attribution of activities and responsibilities to these individuals.

Practitioners include (but are not limited to):

- physicians, dentists, pharmacists

- physician assistants, nurses, scribes

- midwives, dietitians, therapists, optometrists, paramedics

- medical technicians, laboratory scientists, prosthetic technicians, radiographers

- social workers, professional homecare providers, official volunteers

- receptionists handling patient registration

- IT personnel merging or unmerging patient records

- Service animal (e.g., ward assigned dog capable of detecting cancer in patients)

## 8.4.2 Boundaries and Relationships [
](practitioner.html#bnr)

The Resource SHALL NOT be used for persons involved without a formal responsibility like individuals taking care for friends, 
relatives or neighbors. These can be registered as a Patient's Contact. If performing some action or being referenced by another
resource, use the [RelatedPerson](relatedperson.html) resource.

 The primary distinction between a Practitioner and a RelatedPerson is based on whether:

- 
 The person/animal operates on behalf of the care delivery organization over multiple patients (Practitioner) or,

- 
 Where the person/animal is not associated with the organization, and instead is
 allocated tasks specifically for the RelatedPerson's Patient (RelatedPerson).

 A standard extension [animalSpecies](extension-practitioner-animalspecies.html) can be used to indicate the species of a service animal.

 The [PractitionerRole](practitionerrole.html) resource provides the details of roles that the practitioner 
 is approved to perform for which organizations (and at which locations, and optionally what services too).

 Practitioners are also often grouped into [CareTeams](careteam.html) independently of roles, where the CareTeam
 defines what specific role that they are fulfilling within the team, and might or might not have actual practitioner role resources
 created for the practitioner (and in the care team context, the organization the practitioner is representing)

## 8.4.3 Background and Context [
](practitioner.html#bnc)

Practitioner performs different roles within the same or even different organizations. Depending on jurisdiction and custom, 
it may be necessary to maintain a specific Practitioner Resource for each such role or have a single Practitioner with multiple roles.
The role can be limited to a specific period, after which authorization for this role ends. Note that the represented organization
need not necessarily be the (direct) employer of a Practitioner.

This resource is referenced by [Annotation](datatypes.html#Annotation), [Signature](datatypes.html#Signature), [Account](account.html#Account), [AdverseEvent](adverseevent.html#AdverseEvent), [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance), [Appointment](appointment.html#Appointment), [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [AuditEvent](auditevent.html#AuditEvent), [Basic](basic.html#Basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [CatalogEntry](catalogentry.html#CatalogEntry), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Condition](condition.html#Condition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [DetectedIssue](detectedissue.html#DetectedIssue), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [Encounter](encounter.html#Encounter), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [EnrollmentResponse](enrollmentresponse.html#EnrollmentResponse), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [Goal](goal.html#Goal), [Group](group.html#Group), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [Invoice](invoice.html#Invoice), [Linkage](linkage.html#Linkage), [List](list.html#List), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MessageHeader](messageheader.html#MessageHeader), [NutritionOrder](nutritionorder.html#NutritionOrder), [Observation](observation.html#Observation), [Patient](patient.html#Patient), [PaymentNotice](paymentnotice.html#PaymentNotice), [PaymentReconciliation](paymentreconciliation.html#PaymentReconciliation), [Person](person.html#Person), [PractitionerRole](practitionerrole.html#PractitionerRole), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [ResearchStudy](researchstudy.html#ResearchStudy), [RiskAssessment](riskassessment.html#RiskAssessment), [Schedule](schedule.html#Schedule), [ServiceRequest](servicerequest.html#ServiceRequest), [Specimen](specimen.html#Specimen), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest), [Task](task.html#Task), [VerificationResult](verificationresult.html#VerificationResult) and [VisionPrescription](visionprescription.html#VisionPrescription)

## 8.4.4 
Resource Content
 [
](practitioner.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Practitioner](practitioner-definitions.html#Practitioner) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A person with a formal responsibility in the provisioning of healthcare or related services**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](practitioner-definitions.html#Practitioner.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | An identifier for the person as this agent
 | |

| [active](practitioner-definitions.html#Practitioner.active) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether this practitioner's record is in active use | |

| [name](practitioner-definitions.html#Practitioner.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [HumanName](datatypes.html#HumanName) | The name(s) associated with the practitioner
 | |

| [telecom](practitioner-definitions.html#Practitioner.telecom) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the practitioner (that apply to all roles)
 | |

| [address](practitioner-definitions.html#Practitioner.address) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Address](datatypes.html#Address) | Address(es) of the practitioner that are not role specific (typically home address)
 | |

| [gender](practitioner-definitions.html#Practitioner.gender) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | male | female | other | unknown
[AdministrativeGender](valueset-administrative-gender.html) ([Required](terminologies.html#required)) | |

| [birthDate](practitioner-definitions.html#Practitioner.birthDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [date](datatypes.html#date) | The date on which the practitioner was born | |

| [photo](practitioner-definitions.html#Practitioner.photo) | | 0..* | [Attachment](datatypes.html#Attachment) | Image of the person
 | |

| [qualification](practitioner-definitions.html#Practitioner.qualification) | | 0..* | [BackboneElement](backboneelement.html) | Certification, licenses, or training pertaining to the provision of care
 | |

| [identifier](practitioner-definitions.html#Practitioner.qualification.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | An identifier for this qualification for the practitioner
 | |

| [code](practitioner-definitions.html#Practitioner.qualification.code) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Coded representation of the qualification
[v2 table 0360, Version 2.7](v2/0360/2.7/index.html) ([Example](terminologies.html#example)) | |

| [period](practitioner-definitions.html#Practitioner.qualification.period) | | 0..1 | [Period](datatypes.html#Period) | Period during which the qualification is valid | |

| [issuer](practitioner-definitions.html#Practitioner.qualification.issuer) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that regulates and issues the qualification | |

| [communication](practitioner-definitions.html#Practitioner.communication) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A language the practitioner can use in patient communication
[Common Languages](valueset-languages.html) ([Preferred](terminologies.html#preferred) but limited to [AllLanguages](valueset-all-languages.html))
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Practitioner ([DomainResource](domainresource.html))[An identifier that applies to this person in this roleidentifier](practitioner-definitions.html#Practitioner.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether this practitioner's record is in active useactive](practitioner-definitions.html#Practitioner.active) : [boolean](datatypes.html#boolean) [0..1][The name(s) associated with the practitionername](practitioner-definitions.html#Practitioner.name) : [HumanName](datatypes.html#HumanName) [0..*][A contact detail for the practitioner, e.g. a telephone number or an email addresstelecom](practitioner-definitions.html#Practitioner.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Address(es) of the practitioner that are not role specific (typically home address). 
Work addresses are not typically entered in this property as they are usually role dependentaddress](practitioner-definitions.html#Practitioner.address) : [Address](datatypes.html#Address) [0..*][Administrative Gender - the gender that the person is considered to have for administration and record keeping purposesgender](practitioner-definitions.html#Practitioner.gender) : [code](datatypes.html#code) [0..1] « [The gender of a person used for administrative purposes. (Strength=Required)AdministrativeGender](valueset-administrative-gender.html)! »[The date of birth for the practitionerbirthDate](practitioner-definitions.html#Practitioner.birthDate) : [date](datatypes.html#date) [0..1][Image of the personphoto](practitioner-definitions.html#Practitioner.photo) : [Attachment](datatypes.html#Attachment) [0..*][A language the practitioner can use in patient communicationcommunication](practitioner-definitions.html#Practitioner.communication) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [A human language. (Strength=Preferred)CommonLanguages](valueset-languages.html)? »Qualification[An identifier that applies to this person's qualification in this roleidentifier](practitioner-definitions.html#Practitioner.qualification.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Coded representation of the qualificationcode](practitioner-definitions.html#Practitioner.qualification.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Specific qualification the practitioner has to provide a service. (Strength=Example)v2.0360.2.7](v2/0360/2.7/index.html)?? »[Period during which the qualification is validperiod](practitioner-definitions.html#Practitioner.qualification.period) : [Period](datatypes.html#Period) [0..1][Organization that regulates and issues the qualificationissuer](practitioner-definitions.html#Practitioner.qualification.issuer) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »
[The official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner. For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian localityqualification](practitioner-definitions.html#Practitioner.qualification)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Practitioner**](practitioner-definitions.html#Practitioner) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](practitioner-definitions.html#Practitioner.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [An identifier for the person as this agent](terminologies.html#unbound) --></identifier>
 <[**active**](practitioner-definitions.html#Practitioner.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether this practitioner's record is in active use](terminologies.html#unbound) -->
 <[**name**](practitioner-definitions.html#Practitioner.name)><!-- **0..*** [HumanName](datatypes.html#HumanName) [The name(s) associated with the practitioner](terminologies.html#unbound) --></name>
 <[**telecom**](practitioner-definitions.html#Practitioner.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the practitioner (that apply to all roles)](terminologies.html#unbound) --></telecom>
 <[**address**](practitioner-definitions.html#Practitioner.address)><!-- **0..*** [Address](datatypes.html#Address) [Address(es) of the practitioner that are not role specific (typically home address)](terminologies.html#unbound) --></address>
 <[**gender**](practitioner-definitions.html#Practitioner.gender) value="[[code](datatypes.html#code)]"/><!-- **0..1** [male | female | other | unknown](valueset-administrative-gender.html) -->
 <[**birthDate**](practitioner-definitions.html#Practitioner.birthDate) value="[[date](datatypes.html#date)]"/><!-- **0..1** [The date on which the practitioner was born](terminologies.html#unbound) -->
 <[**photo**](practitioner-definitions.html#Practitioner.photo)><!-- **0..*** [Attachment](datatypes.html#Attachment) [Image of the person](terminologies.html#unbound) --></photo>
 <[**qualification**](practitioner-definitions.html#Practitioner.qualification)> <!-- **0..*** Certification, licenses, or training pertaining to the provision of care -->
 <[**identifier**](practitioner-definitions.html#Practitioner.qualification.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [An identifier for this qualification for the practitioner](terminologies.html#unbound) --></identifier>
 <[**code**](practitioner-definitions.html#Practitioner.qualification.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Coded representation of the qualification](v2/0360/2.7/index.html) --></code>
 <[**period**](practitioner-definitions.html#Practitioner.qualification.period)><!-- **0..1** [Period](datatypes.html#Period) [Period during which the qualification is valid](terminologies.html#unbound) --></period>
 <[**issuer**](practitioner-definitions.html#Practitioner.qualification.issuer)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that regulates and issues the qualification](terminologies.html#unbound) --></issuer>
 </qualification>
 <[**communication**](practitioner-definitions.html#Practitioner.communication)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A language the practitioner can use in patient communication](valueset-languages.html) --></communication>
</Practitioner>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Practitioner**](practitioner-definitions.html#Practitioner)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](practitioner-definitions.html#Practitioner.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [An identifier for the person as this agent](terminologies.html#unbound)
 "[active](practitioner-definitions.html#Practitioner.active)" : <[boolean](datatypes.html#boolean)>, // [Whether this practitioner's record is in active use](terminologies.html#unbound)
 "[name](practitioner-definitions.html#Practitioner.name)" : [{ [HumanName](datatypes.html#HumanName) }], // [The name(s) associated with the practitioner](terminologies.html#unbound)
 "[telecom](practitioner-definitions.html#Practitioner.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the practitioner (that apply to all roles)](terminologies.html#unbound)
 "[address](practitioner-definitions.html#Practitioner.address)" : [{ [Address](datatypes.html#Address) }], // [Address(es) of the practitioner that are not role specific (typically home address)](terminologies.html#unbound)
 "[gender](practitioner-definitions.html#Practitioner.gender)" : "<[code](datatypes.html#code)>", // [male | female | other | unknown](valueset-administrative-gender.html)
 "[birthDate](practitioner-definitions.html#Practitioner.birthDate)" : "<[date](datatypes.html#date)>", // [The date on which the practitioner was born](terminologies.html#unbound)
 "[photo](practitioner-definitions.html#Practitioner.photo)" : [{ [Attachment](datatypes.html#Attachment) }], // [Image of the person](terminologies.html#unbound)
 "[qualification](practitioner-definitions.html#Practitioner.qualification)" : [{ // [Certification, licenses, or training pertaining to the provision of care](terminologies.html#unbound)
 "[identifier](practitioner-definitions.html#Practitioner.qualification.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [An identifier for this qualification for the practitioner](terminologies.html#unbound)
 "[code](practitioner-definitions.html#Practitioner.qualification.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Coded representation of the qualification](v2/0360/2.7/index.html)
 "[period](practitioner-definitions.html#Practitioner.qualification.period)" : { [Period](datatypes.html#Period) }, // [Period during which the qualification is valid](terminologies.html#unbound)
 "[issuer](practitioner-definitions.html#Practitioner.qualification.issuer)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) } // [Organization that regulates and issues the qualification](terminologies.html#unbound)
 }],
 "[communication](practitioner-definitions.html#Practitioner.communication)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }] // [A language the practitioner can use in patient communication](valueset-languages.html)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Practitioner**](practitioner-definitions.html#Practitioner);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Practitioner.identifier](practitioner-definitions.html#Practitioner.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* An identifier for the person as this agent
 fhir:[Practitioner.active](practitioner-definitions.html#Practitioner.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether this practitioner's record is in active use
 fhir:[Practitioner.name](practitioner-definitions.html#Practitioner.name) [ [HumanName](datatypes.html#HumanName) ], ... ; # 0..* The name(s) associated with the practitioner
 fhir:[Practitioner.telecom](practitioner-definitions.html#Practitioner.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the practitioner (that apply to all roles)
 fhir:[Practitioner.address](practitioner-definitions.html#Practitioner.address) [ [Address](datatypes.html#Address) ], ... ; # 0..* Address(es) of the practitioner that are not role specific (typically home address)
 fhir:[Practitioner.gender](practitioner-definitions.html#Practitioner.gender) [ [code](datatypes.html#code) ]; # 0..1 male | female | other | unknown
 fhir:[Practitioner.birthDate](practitioner-definitions.html#Practitioner.birthDate) [ [date](datatypes.html#date) ]; # 0..1 The date on which the practitioner was born
 fhir:[Practitioner.photo](practitioner-definitions.html#Practitioner.photo) [ [Attachment](datatypes.html#Attachment) ], ... ; # 0..* Image of the person
 fhir:[Practitioner.qualification](practitioner-definitions.html#Practitioner.qualification) [ # 0..* Certification, licenses, or training pertaining to the provision of care
 fhir:[Practitioner.qualification.identifier](practitioner-definitions.html#Practitioner.qualification.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* An identifier for this qualification for the practitioner
 fhir:[Practitioner.qualification.code](practitioner-definitions.html#Practitioner.qualification.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Coded representation of the qualification
 fhir:[Practitioner.qualification.period](practitioner-definitions.html#Practitioner.qualification.period) [ [Period](datatypes.html#Period) ]; # 0..1 Period during which the qualification is valid
 fhir:[Practitioner.qualification.issuer](practitioner-definitions.html#Practitioner.qualification.issuer) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that regulates and issues the qualification
 ], ...;
 fhir:[Practitioner.communication](practitioner-definitions.html#Practitioner.communication) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A language the practitioner can use in patient communication
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Practitioner](practitioner.html#Practitioner)
 | 
 | 
 |

 | 
 Practitioner.active | 
 
 

 Default Value "true" removed

 

 | 
 |

 | 
 Practitioner.gender | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1

 

 | 
 |

 | 
 Practitioner.communication | 
 
 

 - Change binding strength from extensible to preferred

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](practitioner.diff.xml) or [JSON](practitioner.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](practitioner-version-maps.html) (status = 14 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Practitioner](practitioner-definitions.html#Practitioner) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A person with a formal responsibility in the provisioning of healthcare or related services**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](practitioner-definitions.html#Practitioner.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | An identifier for the person as this agent
 | |

| [active](practitioner-definitions.html#Practitioner.active) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether this practitioner's record is in active use | |

| [name](practitioner-definitions.html#Practitioner.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [HumanName](datatypes.html#HumanName) | The name(s) associated with the practitioner
 | |

| [telecom](practitioner-definitions.html#Practitioner.telecom) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the practitioner (that apply to all roles)
 | |

| [address](practitioner-definitions.html#Practitioner.address) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Address](datatypes.html#Address) | Address(es) of the practitioner that are not role specific (typically home address)
 | |

| [gender](practitioner-definitions.html#Practitioner.gender) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | male | female | other | unknown
[AdministrativeGender](valueset-administrative-gender.html) ([Required](terminologies.html#required)) | |

| [birthDate](practitioner-definitions.html#Practitioner.birthDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [date](datatypes.html#date) | The date on which the practitioner was born | |

| [photo](practitioner-definitions.html#Practitioner.photo) | | 0..* | [Attachment](datatypes.html#Attachment) | Image of the person
 | |

| [qualification](practitioner-definitions.html#Practitioner.qualification) | | 0..* | [BackboneElement](backboneelement.html) | Certification, licenses, or training pertaining to the provision of care
 | |

| [identifier](practitioner-definitions.html#Practitioner.qualification.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | An identifier for this qualification for the practitioner
 | |

| [code](practitioner-definitions.html#Practitioner.qualification.code) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Coded representation of the qualification
[v2 table 0360, Version 2.7](v2/0360/2.7/index.html) ([Example](terminologies.html#example)) | |

| [period](practitioner-definitions.html#Practitioner.qualification.period) | | 0..1 | [Period](datatypes.html#Period) | Period during which the qualification is valid | |

| [issuer](practitioner-definitions.html#Practitioner.qualification.issuer) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that regulates and issues the qualification | |

| [communication](practitioner-definitions.html#Practitioner.communication) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A language the practitioner can use in patient communication
[Common Languages](valueset-languages.html) ([Preferred](terminologies.html#preferred) but limited to [AllLanguages](valueset-all-languages.html))
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Practitioner ([DomainResource](domainresource.html))[An identifier that applies to this person in this roleidentifier](practitioner-definitions.html#Practitioner.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether this practitioner's record is in active useactive](practitioner-definitions.html#Practitioner.active) : [boolean](datatypes.html#boolean) [0..1][The name(s) associated with the practitionername](practitioner-definitions.html#Practitioner.name) : [HumanName](datatypes.html#HumanName) [0..*][A contact detail for the practitioner, e.g. a telephone number or an email addresstelecom](practitioner-definitions.html#Practitioner.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Address(es) of the practitioner that are not role specific (typically home address). 
Work addresses are not typically entered in this property as they are usually role dependentaddress](practitioner-definitions.html#Practitioner.address) : [Address](datatypes.html#Address) [0..*][Administrative Gender - the gender that the person is considered to have for administration and record keeping purposesgender](practitioner-definitions.html#Practitioner.gender) : [code](datatypes.html#code) [0..1] « [The gender of a person used for administrative purposes. (Strength=Required)AdministrativeGender](valueset-administrative-gender.html)! »[The date of birth for the practitionerbirthDate](practitioner-definitions.html#Practitioner.birthDate) : [date](datatypes.html#date) [0..1][Image of the personphoto](practitioner-definitions.html#Practitioner.photo) : [Attachment](datatypes.html#Attachment) [0..*][A language the practitioner can use in patient communicationcommunication](practitioner-definitions.html#Practitioner.communication) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [A human language. (Strength=Preferred)CommonLanguages](valueset-languages.html)? »Qualification[An identifier that applies to this person's qualification in this roleidentifier](practitioner-definitions.html#Practitioner.qualification.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Coded representation of the qualificationcode](practitioner-definitions.html#Practitioner.qualification.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Specific qualification the practitioner has to provide a service. (Strength=Example)v2.0360.2.7](v2/0360/2.7/index.html)?? »[Period during which the qualification is validperiod](practitioner-definitions.html#Practitioner.qualification.period) : [Period](datatypes.html#Period) [0..1][Organization that regulates and issues the qualificationissuer](practitioner-definitions.html#Practitioner.qualification.issuer) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »
[The official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner. For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian localityqualification](practitioner-definitions.html#Practitioner.qualification)[0..*]
 

**XML Template**

 

 
```
<[**Practitioner**](practitioner-definitions.html#Practitioner) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](practitioner-definitions.html#Practitioner.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [An identifier for the person as this agent](terminologies.html#unbound) --></identifier>
 <[**active**](practitioner-definitions.html#Practitioner.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether this practitioner's record is in active use](terminologies.html#unbound) -->
 <[**name**](practitioner-definitions.html#Practitioner.name)><!-- **0..*** [HumanName](datatypes.html#HumanName) [The name(s) associated with the practitioner](terminologies.html#unbound) --></name>
 <[**telecom**](practitioner-definitions.html#Practitioner.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the practitioner (that apply to all roles)](terminologies.html#unbound) --></telecom>
 <[**address**](practitioner-definitions.html#Practitioner.address)><!-- **0..*** [Address](datatypes.html#Address) [Address(es) of the practitioner that are not role specific (typically home address)](terminologies.html#unbound) --></address>
 <[**gender**](practitioner-definitions.html#Practitioner.gender) value="[[code](datatypes.html#code)]"/><!-- **0..1** [male | female | other | unknown](valueset-administrative-gender.html) -->
 <[**birthDate**](practitioner-definitions.html#Practitioner.birthDate) value="[[date](datatypes.html#date)]"/><!-- **0..1** [The date on which the practitioner was born](terminologies.html#unbound) -->
 <[**photo**](practitioner-definitions.html#Practitioner.photo)><!-- **0..*** [Attachment](datatypes.html#Attachment) [Image of the person](terminologies.html#unbound) --></photo>
 <[**qualification**](practitioner-definitions.html#Practitioner.qualification)> <!-- **0..*** Certification, licenses, or training pertaining to the provision of care -->
 <[**identifier**](practitioner-definitions.html#Practitioner.qualification.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [An identifier for this qualification for the practitioner](terminologies.html#unbound) --></identifier>
 <[**code**](practitioner-definitions.html#Practitioner.qualification.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Coded representation of the qualification](v2/0360/2.7/index.html) --></code>
 <[**period**](practitioner-definitions.html#Practitioner.qualification.period)><!-- **0..1** [Period](datatypes.html#Period) [Period during which the qualification is valid](terminologies.html#unbound) --></period>
 <[**issuer**](practitioner-definitions.html#Practitioner.qualification.issuer)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that regulates and issues the qualification](terminologies.html#unbound) --></issuer>
 </qualification>
 <[**communication**](practitioner-definitions.html#Practitioner.communication)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A language the practitioner can use in patient communication](valueset-languages.html) --></communication>
</Practitioner>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Practitioner**](practitioner-definitions.html#Practitioner)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](practitioner-definitions.html#Practitioner.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [An identifier for the person as this agent](terminologies.html#unbound)
 "[active](practitioner-definitions.html#Practitioner.active)" : <[boolean](datatypes.html#boolean)>, // [Whether this practitioner's record is in active use](terminologies.html#unbound)
 "[name](practitioner-definitions.html#Practitioner.name)" : [{ [HumanName](datatypes.html#HumanName) }], // [The name(s) associated with the practitioner](terminologies.html#unbound)
 "[telecom](practitioner-definitions.html#Practitioner.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the practitioner (that apply to all roles)](terminologies.html#unbound)
 "[address](practitioner-definitions.html#Practitioner.address)" : [{ [Address](datatypes.html#Address) }], // [Address(es) of the practitioner that are not role specific (typically home address)](terminologies.html#unbound)
 "[gender](practitioner-definitions.html#Practitioner.gender)" : "<[code](datatypes.html#code)>", // [male | female | other | unknown](valueset-administrative-gender.html)
 "[birthDate](practitioner-definitions.html#Practitioner.birthDate)" : "<[date](datatypes.html#date)>", // [The date on which the practitioner was born](terminologies.html#unbound)
 "[photo](practitioner-definitions.html#Practitioner.photo)" : [{ [Attachment](datatypes.html#Attachment) }], // [Image of the person](terminologies.html#unbound)
 "[qualification](practitioner-definitions.html#Practitioner.qualification)" : [{ // [Certification, licenses, or training pertaining to the provision of care](terminologies.html#unbound)
 "[identifier](practitioner-definitions.html#Practitioner.qualification.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [An identifier for this qualification for the practitioner](terminologies.html#unbound)
 "[code](practitioner-definitions.html#Practitioner.qualification.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Coded representation of the qualification](v2/0360/2.7/index.html)
 "[period](practitioner-definitions.html#Practitioner.qualification.period)" : { [Period](datatypes.html#Period) }, // [Period during which the qualification is valid](terminologies.html#unbound)
 "[issuer](practitioner-definitions.html#Practitioner.qualification.issuer)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) } // [Organization that regulates and issues the qualification](terminologies.html#unbound)
 }],
 "[communication](practitioner-definitions.html#Practitioner.communication)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }] // [A language the practitioner can use in patient communication](valueset-languages.html)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Practitioner**](practitioner-definitions.html#Practitioner);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Practitioner.identifier](practitioner-definitions.html#Practitioner.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* An identifier for the person as this agent
 fhir:[Practitioner.active](practitioner-definitions.html#Practitioner.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether this practitioner's record is in active use
 fhir:[Practitioner.name](practitioner-definitions.html#Practitioner.name) [ [HumanName](datatypes.html#HumanName) ], ... ; # 0..* The name(s) associated with the practitioner
 fhir:[Practitioner.telecom](practitioner-definitions.html#Practitioner.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the practitioner (that apply to all roles)
 fhir:[Practitioner.address](practitioner-definitions.html#Practitioner.address) [ [Address](datatypes.html#Address) ], ... ; # 0..* Address(es) of the practitioner that are not role specific (typically home address)
 fhir:[Practitioner.gender](practitioner-definitions.html#Practitioner.gender) [ [code](datatypes.html#code) ]; # 0..1 male | female | other | unknown
 fhir:[Practitioner.birthDate](practitioner-definitions.html#Practitioner.birthDate) [ [date](datatypes.html#date) ]; # 0..1 The date on which the practitioner was born
 fhir:[Practitioner.photo](practitioner-definitions.html#Practitioner.photo) [ [Attachment](datatypes.html#Attachment) ], ... ; # 0..* Image of the person
 fhir:[Practitioner.qualification](practitioner-definitions.html#Practitioner.qualification) [ # 0..* Certification, licenses, or training pertaining to the provision of care
 fhir:[Practitioner.qualification.identifier](practitioner-definitions.html#Practitioner.qualification.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* An identifier for this qualification for the practitioner
 fhir:[Practitioner.qualification.code](practitioner-definitions.html#Practitioner.qualification.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Coded representation of the qualification
 fhir:[Practitioner.qualification.period](practitioner-definitions.html#Practitioner.qualification.period) [ [Period](datatypes.html#Period) ]; # 0..1 Period during which the qualification is valid
 fhir:[Practitioner.qualification.issuer](practitioner-definitions.html#Practitioner.qualification.issuer) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that regulates and issues the qualification
 ], ...;
 fhir:[Practitioner.communication](practitioner-definitions.html#Practitioner.communication) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A language the practitioner can use in patient communication
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Practitioner](practitioner.html#Practitioner)
 | 
 | 
 |

 | 
 Practitioner.active | 
 
 

 Default Value "true" removed

 

 | 
 |

 | 
 Practitioner.gender | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1

 

 | 
 |

 | 
 Practitioner.communication | 
 
 

 - Change binding strength from extensible to preferred

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](practitioner.diff.xml) or [JSON](practitioner.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](practitioner-version-maps.html) (status = 14 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](practitioner-profiles.html) and the alternate definitions:
Master Definition [XML](practitioner.profile.xml.html) + [JSON](practitioner.profile.json.html),
[XML](xml.html) [Schema](practitioner.xsd)/[Schematron](practitioner.sch) + [JSON](json.html) 
[Schema](practitioner.schema.json.html), [ShEx](practitioner.shex.html) (for [Turtle](rdf.html)) + [see the extensions](practitioner-profiles.html) & the [dependency analysis](practitioner-dependencies.html)

### 8.4.4.1 
Terminology Bindings
 [
](practitioner.html#tx)

 | Path | Definition | Type | Reference | |

 | Practitioner.gender | The gender of a person used for administrative purposes. | [Required](terminologies.html#required) | [AdministrativeGender](valueset-administrative-gender.html) | |

 | Practitioner.qualification.code | Specific qualification the practitioner has to provide a service. | [Example](terminologies.html#example) | [v2.0360.2.7](v2/0360/2.7/index.html) | |

 | Practitioner.communication | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) | |

 

## 8.4.5 
Notes:
 [
](practitioner.html#notes)

 

 - The practitioner's Qualifications are acquired by the practitioner independent of any organization or role, 
 and do not imply that they are allowed/authorized to perform roles relevant to the qualification at any specific Organization/Location.

 

## 8.4.6 Search Parameters [](practitioner.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| active | [token](search.html#token) | Whether the practitioner record is active | Practitioner.active | | |

| address | [string](search.html#string) | A server defined search that may match any of the string fields in the Address, including line, city, district, state, country, postalCode, and/or text | Practitioner.address | [3 Resources](searchparameter-registry.html#individual-address) | |

| address-city | [string](search.html#string) | A city specified in an address | Practitioner.address.city | [3 Resources](searchparameter-registry.html#individual-address-city) | |

| address-country | [string](search.html#string) | A country specified in an address | Practitioner.address.country | [3 Resources](searchparameter-registry.html#individual-address-country) | |

| address-postalcode | [string](search.html#string) | A postalCode specified in an address | Practitioner.address.postalCode | [3 Resources](searchparameter-registry.html#individual-address-postalcode) | |

| address-state | [string](search.html#string) | A state specified in an address | Practitioner.address.state | [3 Resources](searchparameter-registry.html#individual-address-state) | |

| address-use | [token](search.html#token) | A use code specified in an address | Practitioner.address.use | [3 Resources](searchparameter-registry.html#individual-address-use) | |

| communication | [token](search.html#token) | One of the languages that the practitioner can communicate with | Practitioner.communication | | |

| email | [token](search.html#token) | A value in an email contact | Practitioner.telecom.where(system='email') | [4 Resources](searchparameter-registry.html#individual-email) | |

| family | [string](search.html#string) | A portion of the family name | Practitioner.name.family | [1 Resources](searchparameter-registry.html#individual-family) | |

| gender | [token](search.html#token) | Gender of the practitioner | Practitioner.gender | [3 Resources](searchparameter-registry.html#individual-gender) | |

| given | [string](search.html#string) | A portion of the given name | Practitioner.name.given | [1 Resources](searchparameter-registry.html#individual-given) | |

| identifier | [token](search.html#token) | A practitioner's Identifier | Practitioner.identifier | | |

| name | [string](search.html#string) | A server defined search that may match any of the string fields in the HumanName, including family, give, prefix, suffix, suffix, and/or text | Practitioner.name | | |

| phone | [token](search.html#token) | A value in a phone contact | Practitioner.telecom.where(system='phone') | [4 Resources](searchparameter-registry.html#individual-phone) | |

| phonetic | [string](search.html#string) | A portion of either family or given name using some kind of phonetic matching algorithm | Practitioner.name | [3 Resources](searchparameter-registry.html#individual-phonetic) | |

| telecom | [token](search.html#token) | The value in any kind of contact | Practitioner.telecom | [4 Resources](searchparameter-registry.html#individual-telecom) | |