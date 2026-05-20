# Condition - FHIR v4.0.1Business identifiers assigned to this condition by the performer or other systems which remain constant as the resource is updated and propagates from server to serverThe clinical status of the condition (this element modifies the meaning of other elements)The clinical status of the condition or diagnosis. (Strength=Required)The verification status to support the clinical status of the condition (this element modifies the meaning of other elements)The verification status to support or decline the clinical status of the condition or diagnosis. (Strength=Required)A category assigned to the conditionA category assigned to the condition. (Strength=Extensible)A subjective assessment of the severity of the condition as evaluated by the clinicianA subjective assessment of the severity of the condition as evaluated by the clinician. (Strength=Preferred)Identification of the condition, problem or diagnosisIdentification of the condition or diagnosis. (Strength=Example)The anatomical location where this condition manifests itselfCodes describing anatomical locations. May include laterality. (Strength=Example)Indicates the patient or group who the condition record is associated withThe Encounter during which this Condition was created or to which the creation of this record is tightly associatedEstimated or actual date or date-time  the condition began, in the opinion of the clinicianThe date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abateThe recordedDate represents when this particular Condition record was created in the system, which is often a system-generated dateIndividual who recorded the record and takes responsibility for its contentIndividual who is making the condition statementAdditional information about the Condition. This is a general notes/comments entry  for description of the Condition, its diagnosis and prognosisA simple summary of the stage such as "Stage 3". The determination of the stage is disease-specificCodes describing condition stages (e.g. Cancer stages). (Strength=Example)Reference to a formal record of the evidence on which the staging assessment is basedThe kind of staging, such as pathological or clinical stagingCodes describing the kind of condition staging (e.g. clinical or pathological). (Strength=Example)A manifestation or symptom that led to the recording of this conditionCodes that describe the manifestation or symptoms of a condition. (Strength=Example)Links to other relevant information, including pathology reportsClinical stage or grade of a condition. May include formal severity assessmentsSupporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the conditionBusiness identifiers assigned to this condition by the performer or other systems which remain constant as the resource is updated and propagates from server to serverThe clinical status of the condition (this element modifies the meaning of other elements)The clinical status of the condition or diagnosis. (Strength=Required)The verification status to support the clinical status of the condition (this element modifies the meaning of other elements)The verification status to support or decline the clinical status of the condition or diagnosis. (Strength=Required)A category assigned to the conditionA category assigned to the condition. (Strength=Extensible)A subjective assessment of the severity of the condition as evaluated by the clinicianA subjective assessment of the severity of the condition as evaluated by the clinician. (Strength=Preferred)Identification of the condition, problem or diagnosisIdentification of the condition or diagnosis. (Strength=Example)The anatomical location where this condition manifests itselfCodes describing anatomical locations. May include laterality. (Strength=Example)Indicates the patient or group who the condition record is associated withThe Encounter during which this Condition was created or to which the creation of this record is tightly associatedEstimated or actual date or date-time  the condition began, in the opinion of the clinicianThe date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abateThe recordedDate represents when this particular Condition record was created in the system, which is often a system-generated dateIndividual who recorded the record and takes responsibility for its contentIndividual who is making the condition statementAdditional information about the Condition. This is a general notes/comments entry  for description of the Condition, its diagnosis and prognosisA simple summary of the stage such as "Stage 3". The determination of the stage is disease-specificCodes describing condition stages (e.g. Cancer stages). (Strength=Example)Reference to a formal record of the evidence on which the staging assessment is basedThe kind of staging, such as pathological or clinical stagingCodes describing the kind of condition staging (e.g. clinical or pathological). (Strength=Example)A manifestation or symptom that led to the recording of this conditionCodes that describe the manifestation or symptoms of a condition. (Strength=Example)Links to other relevant information, including pathology reportsClinical stage or grade of a condition. May include formal severity assessmentsSupporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the condition

> Source: https://hl7.org/fhir/R4/condition.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/condition.html) [R4B](http://hl7.org/fhir/R4B/condition.html) **R4** [R3](http://hl7.org/fhir/STU3/condition.html) [R2](http://hl7.org/fhir/DSTU2/condition.html)
 

# 9.2 Resource Condition - Content [
](condition.html#9.2)

| [Patient Care ](http://www.hl7.org/Special/committees/patientcare/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.

## 9.2.1 Scope and Usage [
](condition.html#scope)

Condition is one of the [event](workflow.html#event) resources in the FHIR [workflow](workflow.html) specification.

This resource is used to record detailed information about a condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern. The condition could be a point in time diagnosis in context of an encounter, it could be an item on the practitioner’s Problem List, or it could be a concern that doesn’t exist on the practitioner’s Problem List. Often times, a condition is about a clinician's assessment and assertion of a particular aspect of a patient's state of health. It can be used to record information about a disease/illness identified from application of clinical reasoning over the pathologic and pathophysiologic findings (diagnosis), or identification of health issues/situations that a practitioner considers harmful, potentially harmful and may be investigated and managed (problem), or other health issue/situation that may require ongoing monitoring and/or management (health issue/concern).

The condition resource may be used to record a certain health state of a patient which does not normally present a negative outcome, e.g. pregnancy. The condition resource may be used to record a condition following a procedure, such as the condition of Amputee-BKA following an amputation procedure.

While conditions are frequently a result of a clinician's assessment and assertion of a particular aspect of a patient's state of health, conditions can also be expressed by the patient, related person, or any care team member. A clinician may have a concern about a patient condition (e.g. anorexia) that the patient is not concerned about. Likewise, the patient may have a condition (e.g. hair loss) that does not rise to the level of importance such that it belongs on a practitioner’s Problem List.

For example, each of the following conditions could rise to the level of importance such that it belongs on a problem or concern list due to its direct or indirect impact on the patient’s health. These examples may also be represented using other resources, such as [FamilyMemberHistory](familymemberhistory.html), [Observation](observation.html), or [Procedure](procedure.html).

- Unemployed

- Without transportation (or other barriers)

- Susceptibility to falls

- Exposure to communicable disease

- Family History of cardiovascular disease

- Fear of cancer

- Cardiac pacemaker

- Amputee-BKA

- Risk of Zika virus following travel to a country 

- Former smoker

- Travel to a country planned (that warrants immunizations)

- Motor Vehicle Accident

- Patient has had coronary bypass graft

## 9.2.2 Boundaries and Relationships [
](condition.html#bnr)

 The condition resource may be referenced by other resources as "reasons" for an action (e.g. [MedicationRequest](medicationrequest.html),
[Procedure](procedure.html), [ServiceRequest](servicerequest.html), etc.)

This resource is not typically used to record information about subjective and objective information that might lead to the recording of a Condition resource. Such signs and symptoms are typically captured using the [Observation](observation.html) resource;
although in some cases a persistent symptom, e.g. fever, headache may be captured as a condition before a definitive diagnosis can be discerned by a clinician. By contrast, headache may be captured as an Observation when it contributes to the establishment of a meningitis Condition.

Use the [Observation](observation.html) resource when a symptom is resolved without long term management, tracking, or when a symptom contributes to the establishment of a condition.

Use Condition when a symptom requires long term management, tracking, or is used as a proxy for a diagnosis or problem that is not yet determined.

When the diagnosis is related to an allergy or intolerance, the Condition and [AllergyIntolerance](allergyintolerance.html) resources can both be used. However, to be actionable for decision support, using Condition alone is not sufficient as the allergy or intolerance condition needs to be represented as an [AllergyIntolerance](allergyintolerance.html).

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [Appointment](appointment.html#Appointment), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [Claim](claim.html#Claim), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Contract](contract.html#Contract), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [Encounter](encounter.html#Encounter), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory), [Goal](goal.html#Goal), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [Procedure](procedure.html#Procedure), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [ServiceRequest](servicerequest.html#ServiceRequest) and [SupplyRequest](supplyrequest.html#SupplyRequest)

## 9.2.3 
Resource Content
 [
](condition.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Condition](condition-definitions.html#Condition) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Detailed information about conditions, problems or diagnoses**+ Guideline: Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item
+ Rule: If condition is abated, then clinicalStatus must be either inactive, resolved, or remission
+ Rule: Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](condition-definitions.html#Condition.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this condition
 | |

| [clinicalStatus](condition-definitions.html#Condition.clinicalStatus) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | active | recurrence | relapse | inactive | remission | resolved
[Condition Clinical Status Codes](valueset-condition-clinical.html) ([Required](terminologies.html#required)) | |

| [verificationStatus](condition-definitions.html#Condition.verificationStatus) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
[ConditionVerificationStatus](valueset-condition-ver-status.html) ([Required](terminologies.html#required)) | |

| [category](condition-definitions.html#Condition.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | problem-list-item | encounter-diagnosis
[Condition Category Codes](valueset-condition-category.html) ([Extensible](terminologies.html#extensible))
 | |

| [severity](condition-definitions.html#Condition.severity) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Subjective severity of condition
[Condition/Diagnosis Severity](valueset-condition-severity.html) ([Preferred](terminologies.html#preferred)) | |

| [code](condition-definitions.html#Condition.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Identification of the condition, problem or diagnosis
[Condition/Problem/Diagnosis Codes](valueset-condition-code.html) ([Example](terminologies.html#example)) | |

| [bodySite](condition-definitions.html#Condition.bodySite) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location, if relevant
[SNOMED CT Body Structures](valueset-body-site.html) ([Example](terminologies.html#example))
 | |

| [subject](condition-definitions.html#Condition.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who has the condition? | |

| [encounter](condition-definitions.html#Condition.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [onset[x]](condition-definitions.html#Condition.onset_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Estimated or actual date, date-time, or age | |

| onsetDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| onsetAge | | | [Age](datatypes.html#Age) | | |

| onsetPeriod | | | [Period](datatypes.html#Period) | | |

| onsetRange | | | [Range](datatypes.html#Range) | | |

| onsetString | | | [string](datatypes.html#string) | | |

| [abatement[x]](condition-definitions.html#Condition.abatement_x_) | [I](conformance-rules.html#constraints) | 0..1 | | When in resolution/remission | |

| abatementDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| abatementAge | | | [Age](datatypes.html#Age) | | |

| abatementPeriod | | | [Period](datatypes.html#Period) | | |

| abatementRange | | | [Range](datatypes.html#Range) | | |

| abatementString | | | [string](datatypes.html#string) | | |

| [recordedDate](condition-definitions.html#Condition.recordedDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | Date record was first recorded | |

| [recorder](condition-definitions.html#Condition.recorder) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who recorded the condition | |

| [asserter](condition-definitions.html#Condition.asserter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Person who asserts this condition | |

| [stage](condition-definitions.html#Condition.stage) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Stage/grade, usually assessed formally
+ Rule: Stage SHALL have summary or assessment
 | |

| [summary](condition-definitions.html#Condition.stage.summary) | [I](conformance-rules.html#constraints) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Simple summary (disease specific)
[Condition Stage](valueset-condition-stage.html) ([Example](terminologies.html#example)) | |

| [assessment](condition-definitions.html#Condition.stage.assessment) | [I](conformance-rules.html#constraints) | 0..* | [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html) | [DiagnosticReport](diagnosticreport.html) | [Observation](observation.html)) | Formal record of assessment
 | |

| [type](condition-definitions.html#Condition.stage.type) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of staging
[Condition Stage Type](valueset-condition-stage-type.html) ([Example](terminologies.html#example)) | |

| [evidence](condition-definitions.html#Condition.evidence) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Supporting evidence
+ Rule: evidence SHALL have code or details
 | |

| [code](condition-definitions.html#Condition.evidence.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Manifestation/symptom
[Manifestation and Symptom Codes](valueset-manifestation-or-symptom.html) ([Example](terminologies.html#example))
 | |

| [detail](condition-definitions.html#Condition.evidence.detail) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Supporting information found elsewhere
 | |

| [note](condition-definitions.html#Condition.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Additional information about the Condition
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Condition ([DomainResource](domainresource.html))[Business identifiers assigned to this condition by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](condition-definitions.html#Condition.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The clinical status of the condition (this element modifies the meaning of other elements)clinicalStatus](condition-definitions.html#Condition.clinicalStatus) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The clinical status of the condition or diagnosis. (Strength=Required)](valueset-condition-clinical.html) [ConditionClinicalStatusCodes](valueset-condition-clinical.html)! »[The verification status to support the clinical status of the condition (this element modifies the meaning of other elements)verificationStatus](condition-definitions.html#Condition.verificationStatus) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The verification status to support or decline the clinical status of the condition or diagnosis. (Strength=Required)](valueset-condition-ver-status.html) [ConditionVerificationStatus](valueset-condition-ver-status.html)! »[A category assigned to the conditioncategory](condition-definitions.html#Condition.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [A category assigned to the condition. (Strength=Extensible)ConditionCategoryCodes](valueset-condition-category.html)+ »[A subjective assessment of the severity of the condition as evaluated by the clinicianseverity](condition-definitions.html#Condition.severity) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A subjective assessment of the severity of the condition as evaluated by the clinician. (Strength=Preferred)Condition/DiagnosisSeverity](valueset-condition-severity.html)? »[Identification of the condition, problem or diagnosiscode](condition-definitions.html#Condition.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identification of the condition or diagnosis. (Strength=Example)Condition/Problem/DiagnosisCo...](valueset-condition-code.html)?? »[The anatomical location where this condition manifests itselfbodySite](condition-definitions.html#Condition.bodySite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes describing anatomical locations. May include laterality. (Strength=Example)SNOMEDCTBodyStructures](valueset-body-site.html)?? »[Indicates the patient or group who the condition record is associated withsubject](condition-definitions.html#Condition.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this Condition was created or to which the creation of this record is tightly associatedencounter](condition-definitions.html#Condition.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Estimated or actual date or date-time the condition began, in the opinion of the clinicianonset[x]](condition-definitions.html#Condition.onset_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Age](datatypes.html#Age)|[Period](datatypes.html#Period)|[Range](datatypes.html#Range)|[string](datatypes.html#string) »[The date or estimated date that the condition resolved or went into remission. This is called "abatement" because of the many overloaded connotations associated with "remission" or "resolution" - Conditions are never really resolved, but they can abateabatement[x]](condition-definitions.html#Condition.abatement_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Age](datatypes.html#Age)|[Period](datatypes.html#Period)|[Range](datatypes.html#Range)|[string](datatypes.html#string) »[The recordedDate represents when this particular Condition record was created in the system, which is often a system-generated daterecordedDate](condition-definitions.html#Condition.recordedDate) : [dateTime](datatypes.html#dateTime) [0..1][Individual who recorded the record and takes responsibility for its contentrecorder](condition-definitions.html#Condition.recorder) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)| [RelatedPerson](relatedperson.html#RelatedPerson) »[Individual who is making the condition statementasserter](condition-definitions.html#Condition.asserter) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)| [RelatedPerson](relatedperson.html#RelatedPerson) »[Additional information about the Condition. This is a general notes/comments entry for description of the Condition, its diagnosis and prognosisnote](condition-definitions.html#Condition.note) : [Annotation](datatypes.html#Annotation) [0..*]Stage[A simple summary of the stage such as "Stage 3". The determination of the stage is disease-specificsummary](condition-definitions.html#Condition.stage.summary) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing condition stages (e.g. Cancer stages). (Strength=Example)ConditionStage](valueset-condition-stage.html)?? »[Reference to a formal record of the evidence on which the staging assessment is basedassessment](condition-definitions.html#Condition.stage.assessment) : [Reference](references.html#Reference) [0..*] « [ClinicalImpression](clinicalimpression.html#ClinicalImpression)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)| [Observation](observation.html#Observation) »[The kind of staging, such as pathological or clinical stagingtype](condition-definitions.html#Condition.stage.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing the kind of condition staging (e.g. clinical or pathological). (Strength=Example)ConditionStageType](valueset-condition-stage-type.html)?? »Evidence[A manifestation or symptom that led to the recording of this conditioncode](condition-definitions.html#Condition.evidence.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes that describe the manifestation or symptoms of a condition. (Strength=Example)ManifestationAndSymptomCodes](valueset-manifestation-or-symptom.html)?? »[Links to other relevant information, including pathology reportsdetail](condition-definitions.html#Condition.evidence.detail) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »
[Clinical stage or grade of a condition. May include formal severity assessmentsstage](condition-definitions.html#Condition.stage)[0..*][Supporting evidence / manifestations that are the basis of the Condition's verification status, such as evidence that confirmed or refuted the conditionevidence](condition-definitions.html#Condition.evidence)[0..*]
 

 

 

**XML Template**

 

 
```
http://hl7.org/fhir/ValueSet/condition-category
```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Condition**](condition-definitions.html#Condition)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](condition-definitions.html#Condition.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this condition](terminologies.html#unbound)
 "[clinicalStatus](condition-definitions.html#Condition.clinicalStatus)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **C?** [active | recurrence | relapse | inactive | remission | resolved](valueset-condition-clinical.html)
 "[verificationStatus](condition-definitions.html#Condition.verificationStatus)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **C?** [unconfirmed | provisional | differential | confirmed | refuted | entered-in-error](valueset-condition-ver-status.html)
 "[category](condition-definitions.html#Condition.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [problem-list-item | encounter-diagnosis](valueset-condition-category.html)
 "[severity](condition-definitions.html#Condition.severity)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Subjective severity of condition](valueset-condition-severity.html)
 "[code](condition-definitions.html#Condition.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Identification of the condition, problem or diagnosis](valueset-condition-code.html)
 "[bodySite](condition-definitions.html#Condition.bodySite)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Anatomical location, if relevant](valueset-body-site.html)
 "[subject](condition-definitions.html#Condition.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Who has the condition?](terminologies.html#unbound)
 "[encounter](condition-definitions.html#Condition.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 // onset[x]: Estimated or actual date, date-time, or age. One of these 5:
 "[onsetDateTime](condition-definitions.html#Condition.onsetDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[onsetAge](condition-definitions.html#Condition.onsetAge)" : { [Age](datatypes.html#Age) },
 "[onsetPeriod](condition-definitions.html#Condition.onsetPeriod)" : { [Period](datatypes.html#Period) },
 "[onsetRange](condition-definitions.html#Condition.onsetRange)" : { [Range](datatypes.html#Range) },
 "[onsetString](condition-definitions.html#Condition.onsetString)" : "<[string](datatypes.html#string)>",
 // abatement[x]: When in resolution/remission. One of these 5:
 "[abatementDateTime](condition-definitions.html#Condition.abatementDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[abatementAge](condition-definitions.html#Condition.abatementAge)" : { [Age](datatypes.html#Age) },
 "[abatementPeriod](condition-definitions.html#Condition.abatementPeriod)" : { [Period](datatypes.html#Period) },
 "[abatementRange](condition-definitions.html#Condition.abatementRange)" : { [Range](datatypes.html#Range) },
 "[abatementString](condition-definitions.html#Condition.abatementString)" : "<[string](datatypes.html#string)>",
 "[recordedDate](condition-definitions.html#Condition.recordedDate)" : "<[dateTime](datatypes.html#dateTime)>", // [Date record was first recorded](terminologies.html#unbound)
 "[recorder](condition-definitions.html#Condition.recorder)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Who recorded the condition](terminologies.html#unbound)
 "[asserter](condition-definitions.html#Condition.asserter)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Person who asserts this condition](terminologies.html#unbound)
 "[stage](condition-definitions.html#Condition.stage)" : [{ // [Stage/grade, usually assessed formally](terminologies.html#unbound)
 "[summary](condition-definitions.html#Condition.stage.summary)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **C?** [Simple summary (disease specific)](valueset-condition-stage.html)
 "[assessment](condition-definitions.html#Condition.stage.assessment)" : [{ [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[Observation](observation.html#Observation)) }], // **C?** [Formal record of assessment](terminologies.html#unbound)
 "[type](condition-definitions.html#Condition.stage.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Kind of staging](valueset-condition-stage-type.html)
 }],
 "[evidence](condition-definitions.html#Condition.evidence)" : [{ // [Supporting evidence](terminologies.html#unbound)
 "[code](condition-definitions.html#Condition.evidence.code)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // **C?** [Manifestation/symptom](valueset-manifestation-or-symptom.html)
 "[detail](condition-definitions.html#Condition.evidence.detail)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }] // **C?** [Supporting information found elsewhere](terminologies.html#unbound)
 }],
 "[note](condition-definitions.html#Condition.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Additional information about the Condition](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Condition**](condition-definitions.html#Condition);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Condition.identifier](condition-definitions.html#Condition.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this condition
 fhir:[Condition.clinicalStatus](condition-definitions.html#Condition.clinicalStatus) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 active | recurrence | relapse | inactive | remission | resolved
 fhir:[Condition.verificationStatus](condition-definitions.html#Condition.verificationStatus) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 unconfirmed | provisional | differential | confirmed | refuted | entered-in-error
 fhir:[Condition.category](condition-definitions.html#Condition.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* problem-list-item | encounter-diagnosis
 fhir:[Condition.severity](condition-definitions.html#Condition.severity) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Subjective severity of condition
 fhir:[Condition.code](condition-definitions.html#Condition.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Identification of the condition, problem or diagnosis
 fhir:[Condition.bodySite](condition-definitions.html#Condition.bodySite) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Anatomical location, if relevant
 fhir:[Condition.subject](condition-definitions.html#Condition.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Who has the condition?
 fhir:[Condition.encounter](condition-definitions.html#Condition.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 # [Condition.onset[x]](condition-definitions.html#Condition.onset[x]) : 0..1 Estimated or actual date, date-time, or age. One of these 5
 fhir:[Condition.onsetDateTime](condition-definitions.html#Condition.onsetDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Condition.onsetAge](condition-definitions.html#Condition.onsetAge) [ [Age](datatypes.html#Age) ]
 fhir:[Condition.onsetPeriod](condition-definitions.html#Condition.onsetPeriod) [ [Period](datatypes.html#Period) ]
 fhir:[Condition.onsetRange](condition-definitions.html#Condition.onsetRange) [ [Range](datatypes.html#Range) ]
 fhir:[Condition.onsetString](condition-definitions.html#Condition.onsetString) [ [string](datatypes.html#string) ]
 # [Condition.abatement[x]](condition-definitions.html#Condition.abatement[x]) : 0..1 When in resolution/remission. One of these 5
 fhir:[Condition.abatementDateTime](condition-definitions.html#Condition.abatementDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Condition.abatementAge](condition-definitions.html#Condition.abatementAge) [ [Age](datatypes.html#Age) ]
 fhir:[Condition.abatementPeriod](condition-definitions.html#Condition.abatementPeriod) [ [Period](datatypes.html#Period) ]
 fhir:[Condition.abatementRange](condition-definitions.html#Condition.abatementRange) [ [Range](datatypes.html#Range) ]
 fhir:[Condition.abatementString](condition-definitions.html#Condition.abatementString) [ [string](datatypes.html#string) ]
 fhir:[Condition.recordedDate](condition-definitions.html#Condition.recordedDate) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Date record was first recorded
 fhir:[Condition.recorder](condition-definitions.html#Condition.recorder) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Who recorded the condition
 fhir:[Condition.asserter](condition-definitions.html#Condition.asserter) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Person who asserts this condition
 fhir:[Condition.stage](condition-definitions.html#Condition.stage) [ # 0..* Stage/grade, usually assessed formally
 fhir:[Condition.stage.summary](condition-definitions.html#Condition.stage.summary) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Simple summary (disease specific)
 fhir:[Condition.stage.assessment](condition-definitions.html#Condition.stage.assessment) [ [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[Observation](observation.html#Observation)) ], ... ; # 0..* Formal record of assessment
 fhir:[Condition.stage.type](condition-definitions.html#Condition.stage.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of staging
 ], ...;
 fhir:[Condition.evidence](condition-definitions.html#Condition.evidence) [ # 0..* Supporting evidence
 fhir:[Condition.evidence.code](condition-definitions.html#Condition.evidence.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Manifestation/symptom
 fhir:[Condition.evidence.detail](condition-definitions.html#Condition.evidence.detail) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Supporting information found elsewhere
 ], ...;
 fhir:[Condition.note](condition-definitions.html#Condition.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Additional information about the Condition
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Condition](condition.html#Condition)
 | 
 | 
 |

 | 
 Condition.clinicalStatus | 
 
 

 Type changed from code to CodeableConcept

 - Change value set from http://hl7.org/fhir/ValueSet/condition-clinical to http://hl7.org/fhir/ValueSet/condition-clinical|4.0.1

 

 | 
 |

 | 
 Condition.verificationStatus | 
 
 

 - Type changed from code to CodeableConcept

 - Change value set from http://hl7.org/fhir/ValueSet/condition-ver-status to http://hl7.org/fhir/ValueSet/condition-ver-status|4.0.1

 - Default Value "unknown" removed

 

 | 
 |

 | 
 Condition.category | 
 
 

 - 
Add Binding `http://hl7.org/fhir/ValueSet/condition-category` (extensible)
 

 

 | 
 |

 | 
 Condition.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 Condition.abatement[x] | 
 
 

 - Remove Type boolean

 

 | 
 |

 | 
 Condition.recordedDate | 
 
 

 - Renamed from assertedDate to recordedDate

 

 | 
 |

 | 
 Condition.recorder | 
 
 

 - Added Element

 

 | 
 |

 | 
 Condition.asserter | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Condition.stage | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Condition.stage.type | 
 
 

 - Added Element

 

 | 
 |

 | 
 Condition.context | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](condition.diff.xml) or [JSON](condition.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](condition-version-maps.html) (status = 12 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](condition-profiles.html) and the alternate definitions:
Master Definition [XML](condition.profile.xml.html) + [JSON](condition.profile.json.html),
[XML](xml.html) [Schema](condition.xsd)/[Schematron](condition.sch) + [JSON](json.html) 
[Schema](condition.schema.json.html), [ShEx](condition.shex.html) (for [Turtle](rdf.html)) + [see the extensions](condition-profiles.html) & the [dependency analysis](condition-dependencies.html)

### 9.2.3.1 
Terminology Bindings
 [
](condition.html#tx)

 | Path | Definition | Type | Reference | |

 | Condition.clinicalStatus | The clinical status of the condition or diagnosis. | [Required](terminologies.html#required) | [ConditionClinicalStatusCodes](valueset-condition-clinical.html) | |

 | Condition.verificationStatus | The verification status to support or decline the clinical status of the condition or diagnosis. | [Required](terminologies.html#required) | [ConditionVerificationStatus](valueset-condition-ver-status.html) | |

 | Condition.category | A category assigned to the condition. | [Extensible](terminologies.html#extensible) | [ConditionCategoryCodes](valueset-condition-category.html) | |

 | Condition.severity | A subjective assessment of the severity of the condition as evaluated by the clinician. | [Preferred](terminologies.html#preferred) | [Condition/DiagnosisSeverity](valueset-condition-severity.html) | |

 | Condition.code | Identification of the condition or diagnosis. | [Example](terminologies.html#example) | [Condition/Problem/DiagnosisCodes](valueset-condition-code.html) | |

 | Condition.bodySite | Codes describing anatomical locations. May include laterality. | [Example](terminologies.html#example) | [SNOMEDCTBodyStructures](valueset-body-site.html) | |

 | Condition.stage.summary | Codes describing condition stages (e.g. Cancer stages). | [Example](terminologies.html#example) | [ConditionStage](valueset-condition-stage.html) | |

 | Condition.stage.type | Codes describing the kind of condition staging (e.g. clinical or pathological). | [Example](terminologies.html#example) | [ConditionStageType](valueset-condition-stage-type.html) | |

 | Condition.evidence.code | Codes that describe the manifestation or symptoms of a condition. | [Example](terminologies.html#example) | [ManifestationAndSymptomCodes](valueset-manifestation-or-symptom.html) | |

 

 

### 9.2.3.2 Constraints [
](condition.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **con-1** | [Rule](conformance-rules.html#rule) | Condition.stage | Stage SHALL have summary or assessment | summary.exists() or assessment.exists() | |
| **con-2** | [Rule](conformance-rules.html#rule) | Condition.evidence | evidence SHALL have code or details | code.exists() or detail.exists() | |
| **con-3** | [Guideline](conformance-rules.html#best-practice) | (base) | Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item | clinicalStatus.exists() or verificationStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-ver-status' and code = 'entered-in-error').exists() or category.select($this='problem-list-item').empty()**This is (only) a best practice guideline because: 
> Most systems will expect a clinicalStatus to be valued for problem-list-items that are managed over time, but might not need a clinicalStatus for point in time encounter-diagnosis.

 | |
| con-4** | [Rule](conformance-rules.html#rule) | (base) | If condition is abated, then clinicalStatus must be either inactive, resolved, or remission | abatement.empty() or clinicalStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-clinical' and (code='resolved' or code='remission' or code='inactive')).exists() | |
| **con-5** | [Rule](conformance-rules.html#rule) | (base) | Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error | verificationStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-ver-status' and code='entered-in-error').empty() or clinicalStatus.empty() | |

### 9.2.3.3 Use of Condition.code [
](condition.html#9.2.3.3)

Many of the code systems used for coding conditions will provide codes that define not only the condition itself, but may 
also specify a particular stage, location, or causality as part of the code. This is particularly true if 
SNOMED CT is used for the condition, and especially if expressions are allowed. 

The Condition.code may also include such concepts as "history of X" and "good health", where it is useful or appropriate to make such assertions. 
It can also be used to capture "risk of" and "fear of", in addition to physical conditions, as well as "no known problems" or "negated" conditions (e.g., "no X" or "no history of X" - see the following section for "No Known Problems" and Negated Conditions).

When the Condition.code specifies additional properties of the condition, the other properties are not given 
a value - instead, the value must be understood from the Condition.code. 

### 9.2.3.4 "No Known Problems" and Negated Conditions [
](condition.html#9.2.3.4)

 
 **Conditions/Problems Not Reviewed, Not Asked**
 

 
When a sending system does not have any information about conditions/problems being reviewed or the statement is about conditions/problems not yet being asked, then the [List](list.html) resource should be used to indicate the List.emptyReason.code="notasked".
 

 

 
**Conditions/Problems Reviewed, None Identified**

 
Systems may use the List.emptyReason when a statement is about the full scope of the list (i.e. the patient has no conditions/problems of any type). However, it may be preferred to use a code for "no known problems" (e.g., SNOMED CT: 160245001 |No current problems or disability (situation)|), so that all condition/problem data will be available and queryable from Condition resource instances.
 

 
Also note that care should be used when adding new Condition resources to a list to ensure that any negation statements that are voided by the addition of a new record are removed from the list. E.g. If the list contains a "no known problems" record and you add a "diabetes" condition record, then be sure that you remove the "no known problems" record.
 

**
Trial-Use Note:**
There are two primary ways of reporting "no known problems" in the current specification: using the CodeableConcept,
as described above, or using the [List](list.html) resource with emptyReason. During the STU period, [feedback ](http://hl7.org/fhir-issues) is sought regarding the preferred approach.

Provide feedback [here ](http://hl7.org/fhir-issues).

 

 **Patient Denies Condition**
 

 
When the patient denies a condition, that can be annotated in the Condition.note element.

 

### 9.2.3.5 Assertions of Condition Absence [
](condition.html#9.2.3.5)

Generally, electronic records do not contain assertions of conditions that a patient does not have. There are however two exceptions:

- It is appropriate to capture a "refuted" Condition record if the patient or anyone else had reason to believe that a patient did have a condition for a period of time and subsequent evidence has demonstrated that belief was mistaken. In this case, a concrete statement acknowledging the belief as well as the refutation of it is useful.

- It is common as part of checklists prior to admission, surgery, enrollment in trials, etc. to ask questions such as "are you pregnant", "do you have a history of hypertension", etc. This information should NOT be captured using the Condition resource but should instead be captured using QuestionnaireResponse or Observation. In this case, the combination of the question and answer would convey that a particular condition was not present.

### 9.2.3.6 Use of Condition.evidence [
](condition.html#9.2.3.6)

The Condition.evidence provides the basis for whatever is present in Condition.code.

### 9.2.3.7 Use of Condition.abatementRange [
](condition.html#9.2.3.7)

A range is used to communicate age period of subject at time of abatement. 

### 9.2.3.8 Use of Condition.asserter [
](condition.html#9.2.3.8)

If the data enterer is different from the asserter and needs to be known, this could be captured using a Provenance instance pointing to the Condition.
For example, it is possible that a nurse records the condition on behalf of a physician. The physician is taking responsibility, despite the nurse entering it into the medical record.

### 9.2.3.9 Use of Condition.clinicalStatus [
](condition.html#9.2.3.9)

The Condition.stage and Condition.clinicalStatus may have interdependencies. For example, some "stages" of cancer, etc. will be different for a remission than for the initial occurrence.

### 9.2.3.10 Diagnosis Role and Rank within an Encounter [
](condition.html#9.2.3.10)

To represent the role of the diagnosis within an encounter, such as admission diagnosis or discharge diagnosis, use [Encounter.diagnosis.role](encounter-definitions.html#Encounter.diagnosis.role).

 
To represent the numeric ranking of the diagnosis within an encounter, such as primary, secondary, or tertiary, use [Encounter.diagnosis.rank](encounter-definitions.html#Encounter.diagnosis.rank).

### 9.2.3.11 Known Issue [
](condition.html#9.2.3.11)

 A known issue exists with circular references between Condition and ClinicalImpression, which is due to the low maturity level of ClinicalImpression. The Patient Care work group intends to address this issue when ClinicalImpression is considered substantially complete and ready for implementation.

## 9.2.4 Search Parameters [
](condition.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| abatement-age | [quantity](search.html#quantity) | Abatement as age or age range | Condition.abatement.as(Age) | Condition.abatement.as(Range) | | |

| abatement-date | [date](search.html#date) | Date-related abatements (dateTime and period) | Condition.abatement.as(dateTime) | Condition.abatement.as(Period) | | |

| abatement-string | [string](search.html#string) | Abatement as a string | Condition.abatement.as(string) | | |

| asserter | [reference](search.html#reference) | Person who asserts this condition | Condition.asserter
([Practitioner](practitioner.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| body-site | [token](search.html#token) | Anatomical location, if relevant | Condition.bodySite | | |

| category | [token](search.html#token) | The category of the condition | Condition.category | | |

| clinical-status | [token](search.html#token) | The clinical status of the condition | Condition.clinicalStatus | | |

| code | [token](search.html#token) | Code for the condition | Condition.code | [13 Resources](searchparameter-registry.html#clinical-code) | |

| encounter | [reference](search.html#reference) | Encounter created as part of | Condition.encounter
([Encounter](encounter.html)) | | |

| evidence | [token](search.html#token) | Manifestation/symptom | Condition.evidence.code | | |

| evidence-detail | [reference](search.html#reference) | Supporting information found elsewhere | Condition.evidence.detail
(Any) | | |

| identifier | [token](search.html#token) | A unique identifier of the condition record | Condition.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| onset-age | [quantity](search.html#quantity) | Onsets as age or age range | Condition.onset.as(Age) | Condition.onset.as(Range) | | |

| onset-date | [date](search.html#date) | Date related onsets (dateTime and Period) | Condition.onset.as(dateTime) | Condition.onset.as(Period) | | |

| onset-info | [string](search.html#string) | Onsets as a string | Condition.onset.as(string) | | |

| patient | [reference](search.html#reference) | Who has the condition? | Condition.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| recorded-date | [date](search.html#date) | Date record was first recorded | Condition.recordedDate | | |

| severity | [token](search.html#token) | The severity of the condition | Condition.severity | | |

| stage | [token](search.html#token) | Simple summary (disease specific) | Condition.stage.summary | | |

| subject | [reference](search.html#reference) | Who has the condition? | Condition.subject
([Group](group.html), [Patient](patient.html)) | | |

| verification-status | [token](search.html#token) | unconfirmed | provisional | differential | confirmed | refuted | entered-in-error | Condition.verificationStatus | | |