# Encounter - FHIR v4.0.1Identifier(s) by which this encounter is knownplanned | arrived | triaged | in-progress | onleave | finished | cancelled + (this element modifies the meaning of other elements)Current state of the encounter. (Strength=Required)Concepts representing classification of patient encounter such as ambulatory (outpatient), inpatient, emergency, home health or others due to local variationsClassification of the encounter. (Strength=Extensible)Specific type of encounter (e.g. e-mail consultation, surgical day-care, skilled nursing, rehabilitation)The type of encounter. (Strength=Example)Broad categorization of the service that is to be provided (e.g. cardiology)Broad categorization of the service that is to be provided. (Strength=Example)Indicates the urgency of the encounterIndicates the urgency of the encounter. (Strength=Example)The patient or group present at the encounterWhere a specific encounter should be classified as a part of a specific episode(s) of care this field should be used. This association can facilitate grouping of related encounters together for a specific purpose, such as government reporting, issue tracking, association via a common problem.  The association is recorded on the encounter as these are typically created after the episode of care and grouped on entry rather than editing the episode of care to append another encounter to it (the episode of care could span years)The request this encounter satisfies (e.g. incoming referral or procedure request)The appointment that scheduled this encounterThe start and end time of the encounterQuantity of time the encounter lasted. This excludes the time during leaves of absenceReason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisReason why the encounter takes place. (Strength=Preferred)Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisThe set of accounts that may be used for billing for this EncounterThe organization that is primarily responsible for this Encounter's services. This MAY be the same as the organization on the Patient record, however it could be different, such as if the actor performing the services was from an external organization (which may be billed seperately) for an external consultation.  Refer to the example bundle showing an abbreviated set of Encounters for a colonoscopyAnother Encounter of which this encounter is a part of (administratively or in time)planned | arrived | triaged | in-progress | onleave | finished | cancelled +Current state of the encounter. (Strength=Required)The time that the episode was in the specified statusinpatient | outpatient | ambulatory | emergency +Classification of the encounter. (Strength=Extensible)The time that the episode was in the specified classRole of participant in encounterRole of participant in encounter. (Strength=Extensible)The period of time that the specified participant participated in the encounter. These can overlap or be sub-sets of the overall encounter's periodPersons involved in the encounter other than the patientReason the encounter takes place, as specified using information from another resource. For admissions, this is the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a ProcedureRole that this diagnosis has within the encounter (e.g. admission, billing, discharge …)The type of diagnosis this condition represents. (Strength=Preferred)Ranking of the diagnosis (for each role type)Pre-admission identifierThe location/organization from which the patient came before admissionFrom where patient was admitted (physician referral, transfer)From where the patient was admitted. (Strength=Preferred)Whether this hospitalization is a readmission and why if knownThe reason for re-admission of this hospitalization encounter. (Strength=Example)Diet preferences reported by the patientMedical, cultural or ethical food preferences to help with catering requirements. (Strength=Example)Special courtesies (VIP, board member)Special courtesies. (Strength=Preferred)Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other thingsSpecial arrangements. (Strength=Preferred)Location/organization to which the patient is dischargedCategory or kind of location after dischargeDischarge Disposition. (Strength=Example)The location where the encounter takes placeThe status of the participants' presence at the specified location during the period specified. If the participant is no longer at the location, then the period will have an end date/timeThe status of the location. (Strength=Required)This will be used to specify the required levels (bed/ward/room/etc.) desired to be recorded to simplify either messaging or queryPhysical form of the location. (Strength=Example)Time period during which the patient was present at the locationThe status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store themThe class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatientThe list of people responsible for providing the serviceThe list of diagnosis relevant to this encounterDetails about the admission to a healthcare serviceList of locations where  the patient has been during this encounterIdentifier(s) by which this encounter is knownplanned | arrived | triaged | in-progress | onleave | finished | cancelled + (this element modifies the meaning of other elements)Current state of the encounter. (Strength=Required)Concepts representing classification of patient encounter such as ambulatory (outpatient), inpatient, emergency, home health or others due to local variationsClassification of the encounter. (Strength=Extensible)Specific type of encounter (e.g. e-mail consultation, surgical day-care, skilled nursing, rehabilitation)The type of encounter. (Strength=Example)Broad categorization of the service that is to be provided (e.g. cardiology)Broad categorization of the service that is to be provided. (Strength=Example)Indicates the urgency of the encounterIndicates the urgency of the encounter. (Strength=Example)The patient or group present at the encounterWhere a specific encounter should be classified as a part of a specific episode(s) of care this field should be used. This association can facilitate grouping of related encounters together for a specific purpose, such as government reporting, issue tracking, association via a common problem.  The association is recorded on the encounter as these are typically created after the episode of care and grouped on entry rather than editing the episode of care to append another encounter to it (the episode of care could span years)The request this encounter satisfies (e.g. incoming referral or procedure request)The appointment that scheduled this encounterThe start and end time of the encounterQuantity of time the encounter lasted. This excludes the time during leaves of absenceReason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisReason why the encounter takes place. (Strength=Preferred)Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisThe set of accounts that may be used for billing for this EncounterThe organization that is primarily responsible for this Encounter's services. This MAY be the same as the organization on the Patient record, however it could be different, such as if the actor performing the services was from an external organization (which may be billed seperately) for an external consultation.  Refer to the example bundle showing an abbreviated set of Encounters for a colonoscopyAnother Encounter of which this encounter is a part of (administratively or in time)planned | arrived | triaged | in-progress | onleave | finished | cancelled +Current state of the encounter. (Strength=Required)The time that the episode was in the specified statusinpatient | outpatient | ambulatory | emergency +Classification of the encounter. (Strength=Extensible)The time that the episode was in the specified classRole of participant in encounterRole of participant in encounter. (Strength=Extensible)The period of time that the specified participant participated in the encounter. These can overlap or be sub-sets of the overall encounter's periodPersons involved in the encounter other than the patientReason the encounter takes place, as specified using information from another resource. For admissions, this is the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a ProcedureRole that this diagnosis has within the encounter (e.g. admission, billing, discharge …)The type of diagnosis this condition represents. (Strength=Preferred)Ranking of the diagnosis (for each role type)Pre-admission identifierThe location/organization from which the patient came before admissionFrom where patient was admitted (physician referral, transfer)From where the patient was admitted. (Strength=Preferred)Whether this hospitalization is a readmission and why if knownThe reason for re-admission of this hospitalization encounter. (Strength=Example)Diet preferences reported by the patientMedical, cultural or ethical food preferences to help with catering requirements. (Strength=Example)Special courtesies (VIP, board member)Special courtesies. (Strength=Preferred)Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other thingsSpecial arrangements. (Strength=Preferred)Location/organization to which the patient is dischargedCategory or kind of location after dischargeDischarge Disposition. (Strength=Example)The location where the encounter takes placeThe status of the participants' presence at the specified location during the period specified. If the participant is no longer at the location, then the period will have an end date/timeThe status of the location. (Strength=Required)This will be used to specify the required levels (bed/ward/room/etc.) desired to be recorded to simplify either messaging or queryPhysical form of the location. (Strength=Example)Time period during which the patient was present at the locationThe status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store themThe class history permits the tracking of the encounters transitions without needing to go  through the resource history.  This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatientThe list of people responsible for providing the serviceThe list of diagnosis relevant to this encounterDetails about the admission to a healthcare serviceList of locations where  the patient has been during this encounter

> Source: https://hl7.org/fhir/R4/encounter.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/encounter.html) [R4B](http://hl7.org/fhir/R4B/encounter.html) **R4** [R3](http://hl7.org/fhir/STU3/encounter.html) [R2](http://hl7.org/fhir/DSTU2/encounter.html)
 

# 8.11 Resource Encounter - Content [
](encounter.html#8.11)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.

## 8.11.1 Scope and Usage [
](encounter.html#scope)

 
A patient encounter is further characterized by the setting in which it takes place. Amongst them are ambulatory,
 emergency, home health, inpatient and virtual encounters. An Encounter encompasses the lifecycle from pre-admission, 
 the actual encounter (for ambulatory encounters), and admission, stay and discharge (for inpatient encounters). 
During the encounter the patient may move from practitioner to practitioner and location to location.

Because of the broad scope of Encounter, not all elements will be relevant in all settings. For this reason, 
admission/discharge related information is kept in a separate Hospitalization component within Encounter. 
The class* element is used to distinguish between these settings, which will guide further validation and
application of business rules.

There is also substantial variance from organization to organization (and between jurisdictions and countries) 
on which business events translate to the start of a new Encounter, or what level of aggregation is used for Encounter. For example, each
single visit of a practitioner during a hospitalization may lead to a new instance of Encounter, but depending on
local practice and the systems involved, it may well be that this is aggregated to a single instance for a whole hospitalization.
Even more aggregation may occur where jurisdictions introduce groups of Encounters for financial or other reasons.
Encounters can be aggregated or grouped under other Encounters using the *partOf* element. 
See [below](#examples) for examples.

Encounter instances may exist before the actual encounter takes place to convey pre-admission information, including
using Encounters elements to reflect the planned start date or planned encounter locations. In 
this case the *status* element is set to 'planned'.

The Hospitalization component is intended to store the extended information relating to a hospitalization event.
It is always expected to be the same period as the encounter itself. Where the period is different, another
encounter instance should be used to capture this information as a partOf this encounter instance.

The Procedure and encounter have references to each other, and these should be to different procedures;
one for the procedure that was performed during the encounter (stored in Procedure.encounter), and another for cases
where an encounter is a result of another procedure (stored in Encounter.indication) such as a follow-up encounter to
resolve complications from an earlier procedure.

### 8.11.1.1 Status Management [
](encounter.html#8.11.1.1)

During the life-cycle of an encounter it will pass through many statuses. Typically these are in order or the
organization's workflow: planned, in-progress, finished/cancelled.**
This status information is often used for other things, and often an analysis of the status history is required.
This could be done by scanning through all the versions of the encounter, checking the period of each,
and then doing some form of post processing. To ease the burden of this (or where a system doesn't support resource
histories) a status history component is included.

There is no direct indication purely by the status field as to whether an encounter is considered "admitted".

The context of the encounter and business practices/policies/workflows/types can influence this definition.
(e.g., acute care facility, aged care center, outpatient clinic, emergency department, community-based clinic).

Statuses of "arrived", "triaged" or "in progress" could be considered the start of the admission, and also have the 
presence of the hospitalization sub-component entered.

The "on leave" status might or might not be a part of the admission, for example if the patient 
was permitted to go home for a weekend or some other form of external event.

The location is also likely to be filled in with a location status of "present".

For other examples such as an outpatient visit (day procedure - colonoscopy), the patient could also be 
considered to be admitted, hence the encounter doesn't have a fixed definition of admitted.
At a minimum, we do believe that a patient IS admitted when the status is in-progress.

## 8.11.2 Boundaries and Relationships [
](encounter.html#bnr)

 
The Encounter resource is not to be used to store appointment information, the Appointment resource is intended to be used for that.
Note that in many systems outpatient encounters (which are in scope for Encounter) and Appointment are used 
concurrently. In FHIR, Appointment is used for establishing a date for the encounter, while Encounter is 
applicable to information about the actual Encounter, i.e., the patient showing up.

As such, an encounter in the "planned" status is not identical to the appointment that scheduled it,
but it is the encounter prior to its actual occurrence, with the expectation that encounter will be
updated as it progresses to completion. Patient arrival at a location does not necessarily mean the
start of the encounter (e.g. a patient arrives an hour earlier than he is actually seen by a practitioner).

An appointment is normally used for the planning stage of an appointment, searching, locating an available time, then
making the appointment. Once this process is completed and the appointment is about to start, then the appointment
will be marked as fulfilled, and linked to the newly created encounter.

This new encounter may start in an "arrived" status when they are admitted at a location of the facility, and then will
move to the ward where another part-of encounter may begin.

Communication resources are used for a simultaneous interaction between a practitioner and a patient where there is no
direct contact. Examples include a phone message, or transmission of some correspondence documentation.

There is no duration recorded for a communication resource, but it could contain sent and received times.

Standard Extension: Associated Encounter****
This extension should be used to reference an encounter where there is no property that already defines this association on the resource.

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Condition](condition.html#Condition), [Contract](contract.html#Contract), [DeviceRequest](devicerequest.html#DeviceRequest), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentReference](documentreference.html#DocumentReference), itself, [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [List](list.html#List), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [NutritionOrder](nutritionorder.html#NutritionOrder), [Observation](observation.html#Observation), [Procedure](procedure.html#Procedure), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [ServiceRequest](servicerequest.html#ServiceRequest), [Task](task.html#Task) and [VisionPrescription](visionprescription.html#VisionPrescription)

## 8.11.3 
Resource Content
 [
](encounter.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[*](formats.html#table) | |
| [Encounter](encounter-definitions.html#Encounter) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | An interaction during which services are provided to the patient**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](encounter-definitions.html#Encounter.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Identifier(s) by which this encounter is known
 | |

| [status](encounter-definitions.html#Encounter.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled +
[EncounterStatus](valueset-encounter-status.html) ([Required](terminologies.html#required)) | |

| [statusHistory](encounter-definitions.html#Encounter.statusHistory) | | 0..* | [BackboneElement](backboneelement.html) | List of past encounter statuses
 | |

| [status](encounter-definitions.html#Encounter.statusHistory.status) | | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled +
[EncounterStatus](valueset-encounter-status.html) ([Required](terminologies.html#required)) | |

| [period](encounter-definitions.html#Encounter.statusHistory.period) | | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified status | |

| [class](encounter-definitions.html#Encounter.class) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Coding](datatypes.html#Coding) | Classification of patient encounter
[V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html) ([Extensible](terminologies.html#extensible)) | |

| [classHistory](encounter-definitions.html#Encounter.classHistory) | | 0..* | [BackboneElement](backboneelement.html) | List of past encounter classes
 | |

| [class](encounter-definitions.html#Encounter.classHistory.class) | | 1..1 | [Coding](datatypes.html#Coding) | inpatient | outpatient | ambulatory | emergency +
[V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html) ([Extensible](terminologies.html#extensible)) | |

| [period](encounter-definitions.html#Encounter.classHistory.period) | | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified class | |

| [type](encounter-definitions.html#Encounter.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of encounter
[Encounter type](valueset-encounter-type.html) ([Example](terminologies.html#example))
 | |

| [serviceType](encounter-definitions.html#Encounter.serviceType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of service
[Service type](valueset-service-type.html) ([Example](terminologies.html#example)) | |

| [priority](encounter-definitions.html#Encounter.priority) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Indicates the urgency of the encounter
[v3 Code System ActPriority](v3/ActPriority/vs.html) ([Example](terminologies.html#example)) | |

| [subject](encounter-definitions.html#Encounter.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | The patient or group present at the encounter | |

| [episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html)) | Episode(s) of care that this encounter should be recorded against
 | |

| [basedOn](encounter-definitions.html#Encounter.basedOn) | | 0..* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | The ServiceRequest that initiated this encounter
 | |

| [participant](encounter-definitions.html#Encounter.participant) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | List of participants involved in the encounter
 | |

| [type](encounter-definitions.html#Encounter.participant.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in encounter
[Participant type](valueset-encounter-participant-type.html) ([Extensible](terminologies.html#extensible))
 | |

| [period](encounter-definitions.html#Encounter.participant.period) | | 0..1 | [Period](datatypes.html#Period) | Period of time during the encounter that the participant participated | |

| [individual](encounter-definitions.html#Encounter.participant.individual) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html)) | Persons involved in the encounter other than the patient | |

| [appointment](encounter-definitions.html#Encounter.appointment) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Appointment](appointment.html)) | The appointment that scheduled this encounter
 | |

| [period](encounter-definitions.html#Encounter.period) | | 0..1 | [Period](datatypes.html#Period) | The start and end time of the encounter | |

| [length](encounter-definitions.html#Encounter.length) | | 0..1 | [Duration](datatypes.html#Duration) | Quantity of time the encounter lasted (less time absent) | |

| [reasonCode](encounter-definitions.html#Encounter.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason the encounter takes place
[Encounter Reason Codes](valueset-encounter-reason.html) ([Preferred](terminologies.html#preferred))
 | |

| [reasonReference](encounter-definitions.html#Encounter.reasonReference) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html) | [Observation](observation.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | Reason the encounter takes place (reference)
 | |

| [diagnosis](encounter-definitions.html#Encounter.diagnosis) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | The list of diagnosis relevant to this encounter
 | |

| [condition](encounter-definitions.html#Encounter.diagnosis.condition) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html)) | The diagnosis or procedure relevant to the encounter | |

| [use](encounter-definitions.html#Encounter.diagnosis.use) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
[DiagnosisRole](valueset-diagnosis-role.html) ([Preferred](terminologies.html#preferred)) | |

| [rank](encounter-definitions.html#Encounter.diagnosis.rank) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Ranking of the diagnosis (for each role type) | |

| [account](encounter-definitions.html#Encounter.account) | | 0..* | [Reference](references.html#Reference)([Account](account.html)) | The set of accounts that may be used for billing for this Encounter
 | |

| [hospitalization](encounter-definitions.html#Encounter.hospitalization) | | 0..1 | [BackboneElement](backboneelement.html) | Details about the admission to a healthcare service | |

| [preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier) | | 0..1 | [Identifier](datatypes.html#Identifier) | Pre-admission identifier | |

| [origin](encounter-definitions.html#Encounter.hospitalization.origin) | | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | The location/organization from which the patient came before admission | |

| [admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | From where patient was admitted (physician referral, transfer)
[Admit source](valueset-encounter-admit-source.html) ([Preferred](terminologies.html#preferred)) | |

| [reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
[v2 RE-ADMISSION INDICATOR](v2/0092/index.html) ([Example](terminologies.html#example)) | |

| [dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Diet preferences reported by the patient
[Diet](valueset-encounter-diet.html) ([Example](terminologies.html#example))
 | |

| [specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Special courtesies (VIP, board member)
[Special courtesy](valueset-encounter-special-courtesy.html) ([Preferred](terminologies.html#preferred))
 | |

| [specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Wheelchair, translator, stretcher, etc.
[Special arrangements](valueset-encounter-special-arrangements.html) ([Preferred](terminologies.html#preferred))
 | |

| [destination](encounter-definitions.html#Encounter.hospitalization.destination) | | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | Location/organization to which the patient is discharged | |

| [dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category or kind of location after discharge
[Discharge disposition](valueset-encounter-discharge-disposition.html) ([Example](terminologies.html#example)) | |

| [location](encounter-definitions.html#Encounter.location) | | 0..* | [BackboneElement](backboneelement.html) | List of locations where the patient has been
 | |

| [location](encounter-definitions.html#Encounter.location.location) | | 1..1 | [Reference](references.html#Reference)([Location](location.html)) | Location the encounter takes place | |

| [status](encounter-definitions.html#Encounter.location.status) | | 0..1 | [code](datatypes.html#code) | planned | active | reserved | completed
[EncounterLocationStatus](valueset-encounter-location-status.html) ([Required](terminologies.html#required)) | |

| [physicalType](encounter-definitions.html#Encounter.location.physicalType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
[Location type](valueset-location-physical-type.html) ([Example](terminologies.html#example)) | |

| [period](encounter-definitions.html#Encounter.location.period) | | 0..1 | [Period](datatypes.html#Period) | Time period during which the patient was present at the location | |

| [serviceProvider](encounter-definitions.html#Encounter.serviceProvider) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization (facility) responsible for this encounter | |

| [partOf](encounter-definitions.html#Encounter.partOf) | | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Another Encounter this encounter is part of | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Encounter ([DomainResource](domainresource.html))[Identifier(s) by which this encounter is knownidentifier](encounter-definitions.html#Encounter.identifier) : [Identifier](datatypes.html#Identifier) [0..*][planned | arrived | triaged | in-progress | onleave | finished | cancelled + (this element modifies the meaning of other elements)status](encounter-definitions.html#Encounter.status) : [code](datatypes.html#code) [1..1] « [Current state of the encounter. (Strength=Required)EncounterStatus](valueset-encounter-status.html)! »[Concepts representing classification of patient encounter such as ambulatory (outpatient), inpatient, emergency, home health or others due to local variationsclass](encounter-definitions.html#Encounter.class) : [Coding](datatypes.html#Coding) [1..1] « [Classification of the encounter. (Strength=Extensible)v3.ActEncounterCode](v3/ActEncounterCode/vs.html)+ »[Specific type of encounter (e.g. e-mail consultation, surgical day-care, skilled nursing, rehabilitation)type](encounter-definitions.html#Encounter.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The type of encounter. (Strength=Example)EncounterType](valueset-encounter-type.html)?? »[Broad categorization of the service that is to be provided (e.g. cardiology)serviceType](encounter-definitions.html#Encounter.serviceType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Broad categorization of the service that is to be provided. (Strength=Example)ServiceType](valueset-service-type.html)?? »[Indicates the urgency of the encounterpriority](encounter-definitions.html#Encounter.priority) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Indicates the urgency of the encounter. (Strength=Example)v3.ActPriority](v3/ActPriority/vs.html)?? »[The patient or group present at the encountersubject](encounter-definitions.html#Encounter.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[Where a specific encounter should be classified as a part of a specific episode(s) of care this field should be used. This association can facilitate grouping of related encounters together for a specific purpose, such as government reporting, issue tracking, association via a common problem. The association is recorded on the encounter as these are typically created after the episode of care and grouped on entry rather than editing the episode of care to append another encounter to it (the episode of care could span years)episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare) : [Reference](references.html#Reference) [0..*] « [EpisodeOfCare](episodeofcare.html#EpisodeOfCare) »[The request this encounter satisfies (e.g. incoming referral or procedure request)basedOn](encounter-definitions.html#Encounter.basedOn) : [Reference](references.html#Reference) [0..*] « [ServiceRequest](servicerequest.html#ServiceRequest) »[The appointment that scheduled this encounterappointment](encounter-definitions.html#Encounter.appointment) : [Reference](references.html#Reference) [0..*] « [Appointment](appointment.html#Appointment) »[The start and end time of the encounterperiod](encounter-definitions.html#Encounter.period) : [Period](datatypes.html#Period) [0..1][Quantity of time the encounter lasted. This excludes the time during leaves of absencelength](encounter-definitions.html#Encounter.length) : [Duration](datatypes.html#Duration) [0..1][Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisreasonCode](encounter-definitions.html#Encounter.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Reason why the encounter takes place. (Strength=Preferred)EncounterReasonCodes](valueset-encounter-reason.html)? »[Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisreasonReference](encounter-definitions.html#Encounter.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)| [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation) »[The set of accounts that may be used for billing for this Encounteraccount](encounter-definitions.html#Encounter.account) : [Reference](references.html#Reference) [0..*] « [Account](account.html#Account) »[The organization that is primarily responsible for this Encounter's services. This MAY be the same as the organization on the Patient record, however it could be different, such as if the actor performing the services was from an external organization (which may be billed seperately) for an external consultation. Refer to the example bundle showing an abbreviated set of Encounters for a colonoscopyserviceProvider](encounter-definitions.html#Encounter.serviceProvider) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Another Encounter of which this encounter is a part of (administratively or in time)partOf](encounter-definitions.html#Encounter.partOf) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »StatusHistory[planned | arrived | triaged | in-progress | onleave | finished | cancelled +status](encounter-definitions.html#Encounter.statusHistory.status) : [code](datatypes.html#code) [1..1] « [Current state of the encounter. (Strength=Required)EncounterStatus](valueset-encounter-status.html)! »[The time that the episode was in the specified statusperiod](encounter-definitions.html#Encounter.statusHistory.period) : [Period](datatypes.html#Period) [1..1]ClassHistory[inpatient | outpatient | ambulatory | emergency +class](encounter-definitions.html#Encounter.classHistory.class) : [Coding](datatypes.html#Coding) [1..1] « [Classification of the encounter. (Strength=Extensible)v3.ActEncounterCode](v3/ActEncounterCode/vs.html)+ »[The time that the episode was in the specified classperiod](encounter-definitions.html#Encounter.classHistory.period) : [Period](datatypes.html#Period) [1..1]Participant[Role of participant in encountertype](encounter-definitions.html#Encounter.participant.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Role of participant in encounter. (Strength=Extensible)ParticipantType](valueset-encounter-participant-type.html)+ »[The period of time that the specified participant participated in the encounter. These can overlap or be sub-sets of the overall encounter's periodperiod](encounter-definitions.html#Encounter.participant.period) : [Period](datatypes.html#Period) [0..1][Persons involved in the encounter other than the patientindividual](encounter-definitions.html#Encounter.participant.individual) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson) »Diagnosis[Reason the encounter takes place, as specified using information from another resource. For admissions, this is the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a Procedurecondition](encounter-definitions.html#Encounter.diagnosis.condition) : [Reference](references.html#Reference) [1..1] « [Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure) »[Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)use](encounter-definitions.html#Encounter.diagnosis.use) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The type of diagnosis this condition represents. (Strength=Preferred)DiagnosisRole](valueset-diagnosis-role.html)? »[Ranking of the diagnosis (for each role type)rank](encounter-definitions.html#Encounter.diagnosis.rank) : [positiveInt](datatypes.html#positiveInt) [0..1]Hospitalization[Pre-admission identifierpreAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][The location/organization from which the patient came before admissionorigin](encounter-definitions.html#Encounter.hospitalization.origin) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location)|[Organization](organization.html#Organization) »[From where patient was admitted (physician referral, transfer)admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [From where the patient was admitted. (Strength=Preferred)AdmitSource](valueset-encounter-admit-source.html)? »[Whether this hospitalization is a readmission and why if knownreAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The reason for re-admission of this hospitalization encounter. (Strength=Example)v2.0092](v2/0092/index.html)?? »[Diet preferences reported by the patientdietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Medical, cultural or ethical food preferences to help with catering requirements. (Strength=Example)Diet](valueset-encounter-diet.html)?? »[Special courtesies (VIP, board member)specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Special courtesies. (Strength=Preferred)SpecialCourtesy](valueset-encounter-special-courtesy.html)? »[Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other thingsspecialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Special arrangements. (Strength=Preferred)SpecialArrangements](valueset-encounter-special-arrangements.html)? »[Location/organization to which the patient is dischargeddestination](encounter-definitions.html#Encounter.hospitalization.destination) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location)|[Organization](organization.html#Organization) »[Category or kind of location after dischargedischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Discharge Disposition. (Strength=Example)DischargeDisposition](valueset-encounter-discharge-disposition.html)?? »Location[The location where the encounter takes placelocation](encounter-definitions.html#Encounter.location.location) : [Reference](references.html#Reference) [1..1] « [Location](location.html#Location) »[The status of the participants' presence at the specified location during the period specified. If the participant is no longer at the location, then the period will have an end date/timestatus](encounter-definitions.html#Encounter.location.status) : [code](datatypes.html#code) [0..1] « [The status of the location. (Strength=Required)EncounterLocationStatus](valueset-encounter-location-status.html)! »[This will be used to specify the required levels (bed/ward/room/etc.) desired to be recorded to simplify either messaging or queryphysicalType](encounter-definitions.html#Encounter.location.physicalType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Physical form of the location. (Strength=Example)LocationType](valueset-location-physical-type.html)?? »[Time period during which the patient was present at the locationperiod](encounter-definitions.html#Encounter.location.period) : [Period](datatypes.html#Period) [0..1]
[The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store themstatusHistory](encounter-definitions.html#Encounter.statusHistory)[0..*][The class history permits the tracking of the encounters transitions without needing to go through the resource history. This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatientclassHistory](encounter-definitions.html#Encounter.classHistory)[0..*][The list of people responsible for providing the serviceparticipant](encounter-definitions.html#Encounter.participant)[0..*][The list of diagnosis relevant to this encounterdiagnosis](encounter-definitions.html#Encounter.diagnosis)[0..*][Details about the admission to a healthcare servicehospitalization](encounter-definitions.html#Encounter.hospitalization)[0..1][List of locations where the patient has been during this encounterlocation](encounter-definitions.html#Encounter.location)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Encounter**](encounter-definitions.html#Encounter) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](encounter-definitions.html#Encounter.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Identifier(s) by which this encounter is known](terminologies.html#unbound) --></identifier>
 <[**status**](encounter-definitions.html#Encounter.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html) -->
 <[**statusHistory**](encounter-definitions.html#Encounter.statusHistory)> <!-- **0..*** List of past encounter statuses -->
 <[**status**](encounter-definitions.html#Encounter.statusHistory.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html) -->
 <[**period**](encounter-definitions.html#Encounter.statusHistory.period)><!-- **1..1** [Period](datatypes.html#Period) [The time that the episode was in the specified status](terminologies.html#unbound) --></period>
 </statusHistory>
 <[**class**](encounter-definitions.html#Encounter.class)><!-- **1..1** [Coding](datatypes.html#Coding) [Classification of patient encounter](v3/ActEncounterCode/vs.html) --></class>
 <[**classHistory**](encounter-definitions.html#Encounter.classHistory)> <!-- **0..*** List of past encounter classes -->
 <[**class**](encounter-definitions.html#Encounter.classHistory.class)><!-- **1..1** [Coding](datatypes.html#Coding) [inpatient | outpatient | ambulatory | emergency +](v3/ActEncounterCode/vs.html) --></class>
 <[**period**](encounter-definitions.html#Encounter.classHistory.period)><!-- **1..1** [Period](datatypes.html#Period) [The time that the episode was in the specified class](terminologies.html#unbound) --></period>
 </classHistory>
 <[**type**](encounter-definitions.html#Encounter.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Specific type of encounter](valueset-encounter-type.html) --></type>
 <[**serviceType**](encounter-definitions.html#Encounter.serviceType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Specific type of service](valueset-service-type.html) --></serviceType>
 <[**priority**](encounter-definitions.html#Encounter.priority)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Indicates the urgency of the encounter](v3/ActPriority/vs.html) --></priority>
 <[**subject**](encounter-definitions.html#Encounter.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [The patient or group present at the encounter](terminologies.html#unbound) --></subject>
 <[**episodeOfCare**](encounter-definitions.html#Encounter.episodeOfCare)><!-- **0..*** [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) [Episode(s) of care that this encounter should be recorded against](terminologies.html#unbound) --></episodeOfCare>
 <[**basedOn**](encounter-definitions.html#Encounter.basedOn)><!-- **0..*** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [The ServiceRequest that initiated this encounter](terminologies.html#unbound) --></basedOn>
 <[**participant**](encounter-definitions.html#Encounter.participant)> <!-- **0..*** List of participants involved in the encounter -->
 <[**type**](encounter-definitions.html#Encounter.participant.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Role of participant in encounter](valueset-encounter-participant-type.html) --></type>
 <[**period**](encounter-definitions.html#Encounter.participant.period)><!-- **0..1** [Period](datatypes.html#Period) [Period of time during the encounter that the participant participated](terminologies.html#unbound) --></period>
 <[**individual**](encounter-definitions.html#Encounter.participant.individual)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Persons involved in the encounter other than the patient](terminologies.html#unbound) --></individual>
 </participant>
 <[**appointment**](encounter-definitions.html#Encounter.appointment)><!-- **0..*** [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) [The appointment that scheduled this encounter](terminologies.html#unbound) --></appointment>
 <[**period**](encounter-definitions.html#Encounter.period)><!-- **0..1** [Period](datatypes.html#Period) [The start and end time of the encounter](terminologies.html#unbound) --></period>
 <[**length**](encounter-definitions.html#Encounter.length)><!-- **0..1** [Duration](datatypes.html#Duration) [Quantity of time the encounter lasted (less time absent)](terminologies.html#unbound) --></length>
 <[**reasonCode**](encounter-definitions.html#Encounter.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Coded reason the encounter takes place](valueset-encounter-reason.html) --></reasonCode>
 <[**reasonReference**](encounter-definitions.html#Encounter.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) [Reason the encounter takes place (reference)](terminologies.html#unbound) --></reasonReference>
 <[**diagnosis**](encounter-definitions.html#Encounter.diagnosis)> <!-- **0..*** The list of diagnosis relevant to this encounter -->
 <[**condition**](encounter-definitions.html#Encounter.diagnosis.condition)><!-- **1..1** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)) [The diagnosis or procedure relevant to the encounter](terminologies.html#unbound) --></condition>
 <[**use**](encounter-definitions.html#Encounter.diagnosis.use)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)](valueset-diagnosis-role.html) --></use>
 <[**rank**](encounter-definitions.html#Encounter.diagnosis.rank) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [Ranking of the diagnosis (for each role type)](terminologies.html#unbound) -->
 </diagnosis>
 <[**account**](encounter-definitions.html#Encounter.account)><!-- **0..*** [Reference](references.html#Reference)([Account](account.html#Account)) [The set of accounts that may be used for billing for this Encounter](terminologies.html#unbound) --></account>
 <[**hospitalization**](encounter-definitions.html#Encounter.hospitalization)> <!-- **0..1** Details about the admission to a healthcare service -->
 <[**preAdmissionIdentifier**](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Pre-admission identifier](terminologies.html#unbound) --></preAdmissionIdentifier>
 <[**origin**](encounter-definitions.html#Encounter.hospitalization.origin)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) [The location/organization from which the patient came before admission](terminologies.html#unbound) --></origin>
 <[**admitSource**](encounter-definitions.html#Encounter.hospitalization.admitSource)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [From where patient was admitted (physician referral, transfer)](valueset-encounter-admit-source.html) --></admitSource>
 <[**reAdmission**](encounter-definitions.html#Encounter.hospitalization.reAdmission)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission](v2/0092/index.html) --></reAdmission>
 <[**dietPreference**](encounter-definitions.html#Encounter.hospitalization.dietPreference)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Diet preferences reported by the patient](valueset-encounter-diet.html) --></dietPreference>
 <[**specialCourtesy**](encounter-definitions.html#Encounter.hospitalization.specialCourtesy)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Special courtesies (VIP, board member)](valueset-encounter-special-courtesy.html) --></specialCourtesy>
 <[**specialArrangement**](encounter-definitions.html#Encounter.hospitalization.specialArrangement)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Wheelchair, translator, stretcher, etc.](valueset-encounter-special-arrangements.html) --></specialArrangement>
 <[**destination**](encounter-definitions.html#Encounter.hospitalization.destination)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) [Location/organization to which the patient is discharged](terminologies.html#unbound) --></destination>
 <[**dischargeDisposition**](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Category or kind of location after discharge](valueset-encounter-discharge-disposition.html) --></dischargeDisposition>
 </hospitalization>
 <[**location**](encounter-definitions.html#Encounter.location)> <!-- **0..*** List of locations where the patient has been -->
 <[**location**](encounter-definitions.html#Encounter.location.location)><!-- **1..1** [Reference](references.html#Reference)([Location](location.html#Location)) [Location the encounter takes place](terminologies.html#unbound) --></location>
 <[**status**](encounter-definitions.html#Encounter.location.status) value="[[code](datatypes.html#code)]"/><!-- **0..1** [planned | active | reserved | completed](valueset-encounter-location-status.html) -->
 <[**physicalType**](encounter-definitions.html#Encounter.location.physicalType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The physical type of the location (usually the level in the location hierachy - bed room ward etc.)](valueset-location-physical-type.html) --></physicalType>
 <[**period**](encounter-definitions.html#Encounter.location.period)><!-- **0..1** [Period](datatypes.html#Period) [Time period during which the patient was present at the location](terminologies.html#unbound) --></period>
 </location>
 <[**serviceProvider**](encounter-definitions.html#Encounter.serviceProvider)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [The organization (facility) responsible for this encounter](terminologies.html#unbound) --></serviceProvider>
 <[**partOf**](encounter-definitions.html#Encounter.partOf)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Another Encounter this encounter is part of](terminologies.html#unbound) --></partOf>
</Encounter>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Encounter**](encounter-definitions.html#Encounter)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](encounter-definitions.html#Encounter.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Identifier(s) by which this encounter is known](terminologies.html#unbound)
 "[status](encounter-definitions.html#Encounter.status)" : "<[code](datatypes.html#code)>", // **R!** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html)
 "[statusHistory](encounter-definitions.html#Encounter.statusHistory)" : [{ // [List of past encounter statuses](terminologies.html#unbound)
 "[status](encounter-definitions.html#Encounter.statusHistory.status)" : "<[code](datatypes.html#code)>", // **R!** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html)
 "[period](encounter-definitions.html#Encounter.statusHistory.period)" : { [Period](datatypes.html#Period) } // **R!** [The time that the episode was in the specified status](terminologies.html#unbound)
 }],
 "[class](encounter-definitions.html#Encounter.class)" : { [Coding](datatypes.html#Coding) }, // **R!** [Classification of patient encounter](v3/ActEncounterCode/vs.html)
 "[classHistory](encounter-definitions.html#Encounter.classHistory)" : [{ // [List of past encounter classes](terminologies.html#unbound)
 "[class](encounter-definitions.html#Encounter.classHistory.class)" : { [Coding](datatypes.html#Coding) }, // **R!** [inpatient | outpatient | ambulatory | emergency +](v3/ActEncounterCode/vs.html)
 "[period](encounter-definitions.html#Encounter.classHistory.period)" : { [Period](datatypes.html#Period) } // **R!** [The time that the episode was in the specified class](terminologies.html#unbound)
 }],
 "[type](encounter-definitions.html#Encounter.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Specific type of encounter](valueset-encounter-type.html)
 "[serviceType](encounter-definitions.html#Encounter.serviceType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Specific type of service](valueset-service-type.html)
 "[priority](encounter-definitions.html#Encounter.priority)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Indicates the urgency of the encounter](v3/ActPriority/vs.html)
 "[subject](encounter-definitions.html#Encounter.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [The patient or group present at the encounter](terminologies.html#unbound)
 "[episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare)" : [{ [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) }], // [Episode(s) of care that this encounter should be recorded against](terminologies.html#unbound)
 "[basedOn](encounter-definitions.html#Encounter.basedOn)" : [{ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }], // [The ServiceRequest that initiated this encounter](terminologies.html#unbound)
 "[participant](encounter-definitions.html#Encounter.participant)" : [{ // [List of participants involved in the encounter](terminologies.html#unbound)
 "[type](encounter-definitions.html#Encounter.participant.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Role of participant in encounter](valueset-encounter-participant-type.html)
 "[period](encounter-definitions.html#Encounter.participant.period)" : { [Period](datatypes.html#Period) }, // [Period of time during the encounter that the participant participated](terminologies.html#unbound)
 "[individual](encounter-definitions.html#Encounter.participant.individual)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) } // [Persons involved in the encounter other than the patient](terminologies.html#unbound)
 }],
 "[appointment](encounter-definitions.html#Encounter.appointment)" : [{ [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) }], // [The appointment that scheduled this encounter](terminologies.html#unbound)
 "[period](encounter-definitions.html#Encounter.period)" : { [Period](datatypes.html#Period) }, // [The start and end time of the encounter](terminologies.html#unbound)
 "[length](encounter-definitions.html#Encounter.length)" : { [Duration](datatypes.html#Duration) }, // [Quantity of time the encounter lasted (less time absent)](terminologies.html#unbound)
 "[reasonCode](encounter-definitions.html#Encounter.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Coded reason the encounter takes place](valueset-encounter-reason.html)
 "[reasonReference](encounter-definitions.html#Encounter.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) }], // [Reason the encounter takes place (reference)](terminologies.html#unbound)
 "[diagnosis](encounter-definitions.html#Encounter.diagnosis)" : [{ // [The list of diagnosis relevant to this encounter](terminologies.html#unbound)
 "[condition](encounter-definitions.html#Encounter.diagnosis.condition)" : { [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)) }, // **R!** [The diagnosis or procedure relevant to the encounter](terminologies.html#unbound)
 "[use](encounter-definitions.html#Encounter.diagnosis.use)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)](valueset-diagnosis-role.html)
 "[rank](encounter-definitions.html#Encounter.diagnosis.rank)" : "<[positiveInt](datatypes.html#positiveInt)>" // [Ranking of the diagnosis (for each role type)](terminologies.html#unbound)
 }],
 "[account](encounter-definitions.html#Encounter.account)" : [{ [Reference](references.html#Reference)([Account](account.html#Account)) }], // [The set of accounts that may be used for billing for this Encounter](terminologies.html#unbound)
 "[hospitalization](encounter-definitions.html#Encounter.hospitalization)" : { // [Details about the admission to a healthcare service](terminologies.html#unbound)
 "[preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Pre-admission identifier](terminologies.html#unbound)
 "[origin](encounter-definitions.html#Encounter.hospitalization.origin)" : { [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) }, // [The location/organization from which the patient came before admission](terminologies.html#unbound)
 "[admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [From where patient was admitted (physician referral, transfer)](valueset-encounter-admit-source.html)
 "[reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission](v2/0092/index.html)
 "[dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Diet preferences reported by the patient](valueset-encounter-diet.html)
 "[specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Special courtesies (VIP, board member)](valueset-encounter-special-courtesy.html)
 "[specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Wheelchair, translator, stretcher, etc.](valueset-encounter-special-arrangements.html)
 "[destination](encounter-definitions.html#Encounter.hospitalization.destination)" : { [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) }, // [Location/organization to which the patient is discharged](terminologies.html#unbound)
 "[dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Category or kind of location after discharge](valueset-encounter-discharge-disposition.html)
 },
 "[location](encounter-definitions.html#Encounter.location)" : [{ // [List of locations where the patient has been](terminologies.html#unbound)
 "[location](encounter-definitions.html#Encounter.location.location)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // **R!** [Location the encounter takes place](terminologies.html#unbound)
 "[status](encounter-definitions.html#Encounter.location.status)" : "<[code](datatypes.html#code)>", // [planned | active | reserved | completed](valueset-encounter-location-status.html)
 "[physicalType](encounter-definitions.html#Encounter.location.physicalType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The physical type of the location (usually the level in the location hierachy - bed room ward etc.)](valueset-location-physical-type.html)
 "[period](encounter-definitions.html#Encounter.location.period)" : { [Period](datatypes.html#Period) } // [Time period during which the patient was present at the location](terminologies.html#unbound)
 }],
 "[serviceProvider](encounter-definitions.html#Encounter.serviceProvider)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [The organization (facility) responsible for this encounter](terminologies.html#unbound)
 "[partOf](encounter-definitions.html#Encounter.partOf)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) } // [Another Encounter this encounter is part of](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Encounter**](encounter-definitions.html#Encounter);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Encounter.identifier](encounter-definitions.html#Encounter.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Identifier(s) by which this encounter is known
 fhir:[Encounter.status](encounter-definitions.html#Encounter.status) [ [code](datatypes.html#code) ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
 fhir:[Encounter.statusHistory](encounter-definitions.html#Encounter.statusHistory) [ # 0..* List of past encounter statuses
 fhir:[Encounter.statusHistory.status](encounter-definitions.html#Encounter.statusHistory.status) [ [code](datatypes.html#code) ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
 fhir:[Encounter.statusHistory.period](encounter-definitions.html#Encounter.statusHistory.period) [ [Period](datatypes.html#Period) ]; # 1..1 The time that the episode was in the specified status
 ], ...;
 fhir:[Encounter.class](encounter-definitions.html#Encounter.class) [ [Coding](datatypes.html#Coding) ]; # 1..1 Classification of patient encounter
 fhir:[Encounter.classHistory](encounter-definitions.html#Encounter.classHistory) [ # 0..* List of past encounter classes
 fhir:[Encounter.classHistory.class](encounter-definitions.html#Encounter.classHistory.class) [ [Coding](datatypes.html#Coding) ]; # 1..1 inpatient | outpatient | ambulatory | emergency +
 fhir:[Encounter.classHistory.period](encounter-definitions.html#Encounter.classHistory.period) [ [Period](datatypes.html#Period) ]; # 1..1 The time that the episode was in the specified class
 ], ...;
 fhir:[Encounter.type](encounter-definitions.html#Encounter.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Specific type of encounter
 fhir:[Encounter.serviceType](encounter-definitions.html#Encounter.serviceType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Specific type of service
 fhir:[Encounter.priority](encounter-definitions.html#Encounter.priority) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Indicates the urgency of the encounter
 fhir:[Encounter.subject](encounter-definitions.html#Encounter.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 The patient or group present at the encounter
 fhir:[Encounter.episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare) [ [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) ], ... ; # 0..* Episode(s) of care that this encounter should be recorded against
 fhir:[Encounter.basedOn](encounter-definitions.html#Encounter.basedOn) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ], ... ; # 0..* The ServiceRequest that initiated this encounter
 fhir:[Encounter.participant](encounter-definitions.html#Encounter.participant) [ # 0..* List of participants involved in the encounter
 fhir:[Encounter.participant.type](encounter-definitions.html#Encounter.participant.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Role of participant in encounter
 fhir:[Encounter.participant.period](encounter-definitions.html#Encounter.participant.period) [ [Period](datatypes.html#Period) ]; # 0..1 Period of time during the encounter that the participant participated
 fhir:[Encounter.participant.individual](encounter-definitions.html#Encounter.participant.individual) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Persons involved in the encounter other than the patient
 ], ...;
 fhir:[Encounter.appointment](encounter-definitions.html#Encounter.appointment) [ [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) ], ... ; # 0..* The appointment that scheduled this encounter
 fhir:[Encounter.period](encounter-definitions.html#Encounter.period) [ [Period](datatypes.html#Period) ]; # 0..1 The start and end time of the encounter
 fhir:[Encounter.length](encounter-definitions.html#Encounter.length) [ [Duration](datatypes.html#Duration) ]; # 0..1 Quantity of time the encounter lasted (less time absent)
 fhir:[Encounter.reasonCode](encounter-definitions.html#Encounter.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Coded reason the encounter takes place
 fhir:[Encounter.reasonReference](encounter-definitions.html#Encounter.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) ], ... ; # 0..* Reason the encounter takes place (reference)
 fhir:[Encounter.diagnosis](encounter-definitions.html#Encounter.diagnosis) [ # 0..* The list of diagnosis relevant to this encounter
 fhir:[Encounter.diagnosis.condition](encounter-definitions.html#Encounter.diagnosis.condition) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)) ]; # 1..1 The diagnosis or procedure relevant to the encounter
 fhir:[Encounter.diagnosis.use](encounter-definitions.html#Encounter.diagnosis.use) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)
 fhir:[Encounter.diagnosis.rank](encounter-definitions.html#Encounter.diagnosis.rank) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Ranking of the diagnosis (for each role type)
 ], ...;
 fhir:[Encounter.account](encounter-definitions.html#Encounter.account) [ [Reference](references.html#Reference)([Account](account.html#Account)) ], ... ; # 0..* The set of accounts that may be used for billing for this Encounter
 fhir:[Encounter.hospitalization](encounter-definitions.html#Encounter.hospitalization) [ # 0..1 Details about the admission to a healthcare service
 fhir:[Encounter.hospitalization.preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Pre-admission identifier
 fhir:[Encounter.hospitalization.origin](encounter-definitions.html#Encounter.hospitalization.origin) [ [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) ]; # 0..1 The location/organization from which the patient came before admission
 fhir:[Encounter.hospitalization.admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 From where patient was admitted (physician referral, transfer)
 fhir:[Encounter.hospitalization.reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
 fhir:[Encounter.hospitalization.dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Diet preferences reported by the patient
 fhir:[Encounter.hospitalization.specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Special courtesies (VIP, board member)
 fhir:[Encounter.hospitalization.specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Wheelchair, translator, stretcher, etc.
 fhir:[Encounter.hospitalization.destination](encounter-definitions.html#Encounter.hospitalization.destination) [ [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) ]; # 0..1 Location/organization to which the patient is discharged
 fhir:[Encounter.hospitalization.dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Category or kind of location after discharge
 ];
 fhir:[Encounter.location](encounter-definitions.html#Encounter.location) [ # 0..* List of locations where the patient has been
 fhir:[Encounter.location.location](encounter-definitions.html#Encounter.location.location) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 1..1 Location the encounter takes place
 fhir:[Encounter.location.status](encounter-definitions.html#Encounter.location.status) [ [code](datatypes.html#code) ]; # 0..1 planned | active | reserved | completed
 fhir:[Encounter.location.physicalType](encounter-definitions.html#Encounter.location.physicalType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
 fhir:[Encounter.location.period](encounter-definitions.html#Encounter.location.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time period during which the patient was present at the location
 ], ...;
 fhir:[Encounter.serviceProvider](encounter-definitions.html#Encounter.serviceProvider) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 The organization (facility) responsible for this encounter
 fhir:[Encounter.partOf](encounter-definitions.html#Encounter.partOf) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Another Encounter this encounter is part of
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Encounter](encounter.html#Encounter)
 | 
 | 
 |

 | 
 Encounter.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1

 

 | 
 |

 | 
 Encounter.statusHistory.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1

 

 | 
 |

 | 
 Encounter.class | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Encounter.serviceType | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.basedOn | 
 
 

 - Renamed from incomingReferral to basedOn

 - Type Reference: Added Target Type ServiceRequest

 - Type Reference: Removed Target Type ReferralRequest

 

 | 
 |

 | 
 Encounter.participant.individual | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Encounter.appointment | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Encounter.reasonCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.reasonReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.diagnosis.use | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.hospitalization.origin | 
 
 

 - Type Reference: Added Target Type Organization

 

 | 
 |

 | 
 Encounter.hospitalization.destination | 
 
 

 - Type Reference: Added Target Type Organization

 

 | 
 |

 | 
 Encounter.location.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/encounter-location-status to http://hl7.org/fhir/ValueSet/encounter-location-status|4.0.1

 

 | 
 |

 | 
 Encounter.location.physicalType | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.reason | 
 
 

 - deleted

 

 | 
 |

 | 
 Encounter.diagnosis.role | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](encounter.diff.xml) or [JSON](encounter.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](encounter-version-maps.html) (status = 10 tests that all execute ok. All tests pass round-trip testing and 3 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Encounter](encounter-definitions.html#Encounter) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | An interaction during which services are provided to the patient**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](encounter-definitions.html#Encounter.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Identifier(s) by which this encounter is known
 | |

| [status](encounter-definitions.html#Encounter.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled +
[EncounterStatus](valueset-encounter-status.html) ([Required](terminologies.html#required)) | |

| [statusHistory](encounter-definitions.html#Encounter.statusHistory) | | 0..* | [BackboneElement](backboneelement.html) | List of past encounter statuses
 | |

| [status](encounter-definitions.html#Encounter.statusHistory.status) | | 1..1 | [code](datatypes.html#code) | planned | arrived | triaged | in-progress | onleave | finished | cancelled +
[EncounterStatus](valueset-encounter-status.html) ([Required](terminologies.html#required)) | |

| [period](encounter-definitions.html#Encounter.statusHistory.period) | | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified status | |

| [class](encounter-definitions.html#Encounter.class) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Coding](datatypes.html#Coding) | Classification of patient encounter
[V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html) ([Extensible](terminologies.html#extensible)) | |

| [classHistory](encounter-definitions.html#Encounter.classHistory) | | 0..* | [BackboneElement](backboneelement.html) | List of past encounter classes
 | |

| [class](encounter-definitions.html#Encounter.classHistory.class) | | 1..1 | [Coding](datatypes.html#Coding) | inpatient | outpatient | ambulatory | emergency +
[V3 Value SetActEncounterCode](v3/ActEncounterCode/vs.html) ([Extensible](terminologies.html#extensible)) | |

| [period](encounter-definitions.html#Encounter.classHistory.period) | | 1..1 | [Period](datatypes.html#Period) | The time that the episode was in the specified class | |

| [type](encounter-definitions.html#Encounter.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of encounter
[Encounter type](valueset-encounter-type.html) ([Example](terminologies.html#example))
 | |

| [serviceType](encounter-definitions.html#Encounter.serviceType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Specific type of service
[Service type](valueset-service-type.html) ([Example](terminologies.html#example)) | |

| [priority](encounter-definitions.html#Encounter.priority) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Indicates the urgency of the encounter
[v3 Code System ActPriority](v3/ActPriority/vs.html) ([Example](terminologies.html#example)) | |

| [subject](encounter-definitions.html#Encounter.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | The patient or group present at the encounter | |

| [episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html)) | Episode(s) of care that this encounter should be recorded against
 | |

| [basedOn](encounter-definitions.html#Encounter.basedOn) | | 0..* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | The ServiceRequest that initiated this encounter
 | |

| [participant](encounter-definitions.html#Encounter.participant) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | List of participants involved in the encounter
 | |

| [type](encounter-definitions.html#Encounter.participant.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in encounter
[Participant type](valueset-encounter-participant-type.html) ([Extensible](terminologies.html#extensible))
 | |

| [period](encounter-definitions.html#Encounter.participant.period) | | 0..1 | [Period](datatypes.html#Period) | Period of time during the encounter that the participant participated | |

| [individual](encounter-definitions.html#Encounter.participant.individual) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html)) | Persons involved in the encounter other than the patient | |

| [appointment](encounter-definitions.html#Encounter.appointment) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Appointment](appointment.html)) | The appointment that scheduled this encounter
 | |

| [period](encounter-definitions.html#Encounter.period) | | 0..1 | [Period](datatypes.html#Period) | The start and end time of the encounter | |

| [length](encounter-definitions.html#Encounter.length) | | 0..1 | [Duration](datatypes.html#Duration) | Quantity of time the encounter lasted (less time absent) | |

| [reasonCode](encounter-definitions.html#Encounter.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason the encounter takes place
[Encounter Reason Codes](valueset-encounter-reason.html) ([Preferred](terminologies.html#preferred))
 | |

| [reasonReference](encounter-definitions.html#Encounter.reasonReference) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html) | [Observation](observation.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | Reason the encounter takes place (reference)
 | |

| [diagnosis](encounter-definitions.html#Encounter.diagnosis) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | The list of diagnosis relevant to this encounter
 | |

| [condition](encounter-definitions.html#Encounter.diagnosis.condition) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html)) | The diagnosis or procedure relevant to the encounter | |

| [use](encounter-definitions.html#Encounter.diagnosis.use) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)
[DiagnosisRole](valueset-diagnosis-role.html) ([Preferred](terminologies.html#preferred)) | |

| [rank](encounter-definitions.html#Encounter.diagnosis.rank) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Ranking of the diagnosis (for each role type) | |

| [account](encounter-definitions.html#Encounter.account) | | 0..* | [Reference](references.html#Reference)([Account](account.html)) | The set of accounts that may be used for billing for this Encounter
 | |

| [hospitalization](encounter-definitions.html#Encounter.hospitalization) | | 0..1 | [BackboneElement](backboneelement.html) | Details about the admission to a healthcare service | |

| [preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier) | | 0..1 | [Identifier](datatypes.html#Identifier) | Pre-admission identifier | |

| [origin](encounter-definitions.html#Encounter.hospitalization.origin) | | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | The location/organization from which the patient came before admission | |

| [admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | From where patient was admitted (physician referral, transfer)
[Admit source](valueset-encounter-admit-source.html) ([Preferred](terminologies.html#preferred)) | |

| [reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
[v2 RE-ADMISSION INDICATOR](v2/0092/index.html) ([Example](terminologies.html#example)) | |

| [dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Diet preferences reported by the patient
[Diet](valueset-encounter-diet.html) ([Example](terminologies.html#example))
 | |

| [specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Special courtesies (VIP, board member)
[Special courtesy](valueset-encounter-special-courtesy.html) ([Preferred](terminologies.html#preferred))
 | |

| [specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Wheelchair, translator, stretcher, etc.
[Special arrangements](valueset-encounter-special-arrangements.html) ([Preferred](terminologies.html#preferred))
 | |

| [destination](encounter-definitions.html#Encounter.hospitalization.destination) | | 0..1 | [Reference](references.html#Reference)([Location](location.html) | [Organization](organization.html)) | Location/organization to which the patient is discharged | |

| [dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category or kind of location after discharge
[Discharge disposition](valueset-encounter-discharge-disposition.html) ([Example](terminologies.html#example)) | |

| [location](encounter-definitions.html#Encounter.location) | | 0..* | [BackboneElement](backboneelement.html) | List of locations where the patient has been
 | |

| [location](encounter-definitions.html#Encounter.location.location) | | 1..1 | [Reference](references.html#Reference)([Location](location.html)) | Location the encounter takes place | |

| [status](encounter-definitions.html#Encounter.location.status) | | 0..1 | [code](datatypes.html#code) | planned | active | reserved | completed
[EncounterLocationStatus](valueset-encounter-location-status.html) ([Required](terminologies.html#required)) | |

| [physicalType](encounter-definitions.html#Encounter.location.physicalType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
[Location type](valueset-location-physical-type.html) ([Example](terminologies.html#example)) | |

| [period](encounter-definitions.html#Encounter.location.period) | | 0..1 | [Period](datatypes.html#Period) | Time period during which the patient was present at the location | |

| [serviceProvider](encounter-definitions.html#Encounter.serviceProvider) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization (facility) responsible for this encounter | |

| [partOf](encounter-definitions.html#Encounter.partOf) | | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Another Encounter this encounter is part of | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Encounter ([DomainResource](domainresource.html))[Identifier(s) by which this encounter is knownidentifier](encounter-definitions.html#Encounter.identifier) : [Identifier](datatypes.html#Identifier) [0..*][planned | arrived | triaged | in-progress | onleave | finished | cancelled + (this element modifies the meaning of other elements)status](encounter-definitions.html#Encounter.status) : [code](datatypes.html#code) [1..1] « [Current state of the encounter. (Strength=Required)EncounterStatus](valueset-encounter-status.html)! »[Concepts representing classification of patient encounter such as ambulatory (outpatient), inpatient, emergency, home health or others due to local variationsclass](encounter-definitions.html#Encounter.class) : [Coding](datatypes.html#Coding) [1..1] « [Classification of the encounter. (Strength=Extensible)v3.ActEncounterCode](v3/ActEncounterCode/vs.html)+ »[Specific type of encounter (e.g. e-mail consultation, surgical day-care, skilled nursing, rehabilitation)type](encounter-definitions.html#Encounter.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The type of encounter. (Strength=Example)EncounterType](valueset-encounter-type.html)?? »[Broad categorization of the service that is to be provided (e.g. cardiology)serviceType](encounter-definitions.html#Encounter.serviceType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Broad categorization of the service that is to be provided. (Strength=Example)ServiceType](valueset-service-type.html)?? »[Indicates the urgency of the encounterpriority](encounter-definitions.html#Encounter.priority) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Indicates the urgency of the encounter. (Strength=Example)v3.ActPriority](v3/ActPriority/vs.html)?? »[The patient or group present at the encountersubject](encounter-definitions.html#Encounter.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[Where a specific encounter should be classified as a part of a specific episode(s) of care this field should be used. This association can facilitate grouping of related encounters together for a specific purpose, such as government reporting, issue tracking, association via a common problem. The association is recorded on the encounter as these are typically created after the episode of care and grouped on entry rather than editing the episode of care to append another encounter to it (the episode of care could span years)episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare) : [Reference](references.html#Reference) [0..*] « [EpisodeOfCare](episodeofcare.html#EpisodeOfCare) »[The request this encounter satisfies (e.g. incoming referral or procedure request)basedOn](encounter-definitions.html#Encounter.basedOn) : [Reference](references.html#Reference) [0..*] « [ServiceRequest](servicerequest.html#ServiceRequest) »[The appointment that scheduled this encounterappointment](encounter-definitions.html#Encounter.appointment) : [Reference](references.html#Reference) [0..*] « [Appointment](appointment.html#Appointment) »[The start and end time of the encounterperiod](encounter-definitions.html#Encounter.period) : [Period](datatypes.html#Period) [0..1][Quantity of time the encounter lasted. This excludes the time during leaves of absencelength](encounter-definitions.html#Encounter.length) : [Duration](datatypes.html#Duration) [0..1][Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisreasonCode](encounter-definitions.html#Encounter.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Reason why the encounter takes place. (Strength=Preferred)EncounterReasonCodes](valueset-encounter-reason.html)? »[Reason the encounter takes place, expressed as a code. For admissions, this can be used for a coded admission diagnosisreasonReference](encounter-definitions.html#Encounter.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)| [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation) »[The set of accounts that may be used for billing for this Encounteraccount](encounter-definitions.html#Encounter.account) : [Reference](references.html#Reference) [0..*] « [Account](account.html#Account) »[The organization that is primarily responsible for this Encounter's services. This MAY be the same as the organization on the Patient record, however it could be different, such as if the actor performing the services was from an external organization (which may be billed seperately) for an external consultation. Refer to the example bundle showing an abbreviated set of Encounters for a colonoscopyserviceProvider](encounter-definitions.html#Encounter.serviceProvider) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Another Encounter of which this encounter is a part of (administratively or in time)partOf](encounter-definitions.html#Encounter.partOf) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »StatusHistory[planned | arrived | triaged | in-progress | onleave | finished | cancelled +status](encounter-definitions.html#Encounter.statusHistory.status) : [code](datatypes.html#code) [1..1] « [Current state of the encounter. (Strength=Required)EncounterStatus](valueset-encounter-status.html)! »[The time that the episode was in the specified statusperiod](encounter-definitions.html#Encounter.statusHistory.period) : [Period](datatypes.html#Period) [1..1]ClassHistory[inpatient | outpatient | ambulatory | emergency +class](encounter-definitions.html#Encounter.classHistory.class) : [Coding](datatypes.html#Coding) [1..1] « [Classification of the encounter. (Strength=Extensible)v3.ActEncounterCode](v3/ActEncounterCode/vs.html)+ »[The time that the episode was in the specified classperiod](encounter-definitions.html#Encounter.classHistory.period) : [Period](datatypes.html#Period) [1..1]Participant[Role of participant in encountertype](encounter-definitions.html#Encounter.participant.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Role of participant in encounter. (Strength=Extensible)ParticipantType](valueset-encounter-participant-type.html)+ »[The period of time that the specified participant participated in the encounter. These can overlap or be sub-sets of the overall encounter's periodperiod](encounter-definitions.html#Encounter.participant.period) : [Period](datatypes.html#Period) [0..1][Persons involved in the encounter other than the patientindividual](encounter-definitions.html#Encounter.participant.individual) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson) »Diagnosis[Reason the encounter takes place, as specified using information from another resource. For admissions, this is the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a Procedurecondition](encounter-definitions.html#Encounter.diagnosis.condition) : [Reference](references.html#Reference) [1..1] « [Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure) »[Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …)use](encounter-definitions.html#Encounter.diagnosis.use) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The type of diagnosis this condition represents. (Strength=Preferred)DiagnosisRole](valueset-diagnosis-role.html)? »[Ranking of the diagnosis (for each role type)rank](encounter-definitions.html#Encounter.diagnosis.rank) : [positiveInt](datatypes.html#positiveInt) [0..1]Hospitalization[Pre-admission identifierpreAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][The location/organization from which the patient came before admissionorigin](encounter-definitions.html#Encounter.hospitalization.origin) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location)|[Organization](organization.html#Organization) »[From where patient was admitted (physician referral, transfer)admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [From where the patient was admitted. (Strength=Preferred)AdmitSource](valueset-encounter-admit-source.html)? »[Whether this hospitalization is a readmission and why if knownreAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The reason for re-admission of this hospitalization encounter. (Strength=Example)v2.0092](v2/0092/index.html)?? »[Diet preferences reported by the patientdietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Medical, cultural or ethical food preferences to help with catering requirements. (Strength=Example)Diet](valueset-encounter-diet.html)?? »[Special courtesies (VIP, board member)specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Special courtesies. (Strength=Preferred)SpecialCourtesy](valueset-encounter-special-courtesy.html)? »[Any special requests that have been made for this hospitalization encounter, such as the provision of specific equipment or other thingsspecialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Special arrangements. (Strength=Preferred)SpecialArrangements](valueset-encounter-special-arrangements.html)? »[Location/organization to which the patient is dischargeddestination](encounter-definitions.html#Encounter.hospitalization.destination) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location)|[Organization](organization.html#Organization) »[Category or kind of location after dischargedischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Discharge Disposition. (Strength=Example)DischargeDisposition](valueset-encounter-discharge-disposition.html)?? »Location[The location where the encounter takes placelocation](encounter-definitions.html#Encounter.location.location) : [Reference](references.html#Reference) [1..1] « [Location](location.html#Location) »[The status of the participants' presence at the specified location during the period specified. If the participant is no longer at the location, then the period will have an end date/timestatus](encounter-definitions.html#Encounter.location.status) : [code](datatypes.html#code) [0..1] « [The status of the location. (Strength=Required)EncounterLocationStatus](valueset-encounter-location-status.html)! »[This will be used to specify the required levels (bed/ward/room/etc.) desired to be recorded to simplify either messaging or queryphysicalType](encounter-definitions.html#Encounter.location.physicalType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Physical form of the location. (Strength=Example)LocationType](valueset-location-physical-type.html)?? »[Time period during which the patient was present at the locationperiod](encounter-definitions.html#Encounter.location.period) : [Period](datatypes.html#Period) [0..1]
[The status history permits the encounter resource to contain the status history without needing to read through the historical versions of the resource, or even have the server store themstatusHistory](encounter-definitions.html#Encounter.statusHistory)[0..*][The class history permits the tracking of the encounters transitions without needing to go through the resource history. This would be used for a case where an admission starts of as an emergency encounter, then transitions into an inpatient scenario. Doing this and not restarting a new encounter ensures that any lab/diagnostic results can more easily follow the patient and not require re-processing and not get lost or cancelled during a kind of discharge from emergency to inpatientclassHistory](encounter-definitions.html#Encounter.classHistory)[0..*][The list of people responsible for providing the serviceparticipant](encounter-definitions.html#Encounter.participant)[0..*][The list of diagnosis relevant to this encounterdiagnosis](encounter-definitions.html#Encounter.diagnosis)[0..*][Details about the admission to a healthcare servicehospitalization](encounter-definitions.html#Encounter.hospitalization)[0..1][List of locations where the patient has been during this encounterlocation](encounter-definitions.html#Encounter.location)[0..*]
 

**XML Template**

 

 
```
<[**Encounter**](encounter-definitions.html#Encounter) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](encounter-definitions.html#Encounter.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Identifier(s) by which this encounter is known](terminologies.html#unbound) --></identifier>
 <[**status**](encounter-definitions.html#Encounter.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html) -->
 <[**statusHistory**](encounter-definitions.html#Encounter.statusHistory)> <!-- **0..*** List of past encounter statuses -->
 <[**status**](encounter-definitions.html#Encounter.statusHistory.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html) -->
 <[**period**](encounter-definitions.html#Encounter.statusHistory.period)><!-- **1..1** [Period](datatypes.html#Period) [The time that the episode was in the specified status](terminologies.html#unbound) --></period>
 </statusHistory>
 <[**class**](encounter-definitions.html#Encounter.class)><!-- **1..1** [Coding](datatypes.html#Coding) [Classification of patient encounter](v3/ActEncounterCode/vs.html) --></class>
 <[**classHistory**](encounter-definitions.html#Encounter.classHistory)> <!-- **0..*** List of past encounter classes -->
 <[**class**](encounter-definitions.html#Encounter.classHistory.class)><!-- **1..1** [Coding](datatypes.html#Coding) [inpatient | outpatient | ambulatory | emergency +](v3/ActEncounterCode/vs.html) --></class>
 <[**period**](encounter-definitions.html#Encounter.classHistory.period)><!-- **1..1** [Period](datatypes.html#Period) [The time that the episode was in the specified class](terminologies.html#unbound) --></period>
 </classHistory>
 <[**type**](encounter-definitions.html#Encounter.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Specific type of encounter](valueset-encounter-type.html) --></type>
 <[**serviceType**](encounter-definitions.html#Encounter.serviceType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Specific type of service](valueset-service-type.html) --></serviceType>
 <[**priority**](encounter-definitions.html#Encounter.priority)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Indicates the urgency of the encounter](v3/ActPriority/vs.html) --></priority>
 <[**subject**](encounter-definitions.html#Encounter.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [The patient or group present at the encounter](terminologies.html#unbound) --></subject>
 <[**episodeOfCare**](encounter-definitions.html#Encounter.episodeOfCare)><!-- **0..*** [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) [Episode(s) of care that this encounter should be recorded against](terminologies.html#unbound) --></episodeOfCare>
 <[**basedOn**](encounter-definitions.html#Encounter.basedOn)><!-- **0..*** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [The ServiceRequest that initiated this encounter](terminologies.html#unbound) --></basedOn>
 <[**participant**](encounter-definitions.html#Encounter.participant)> <!-- **0..*** List of participants involved in the encounter -->
 <[**type**](encounter-definitions.html#Encounter.participant.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Role of participant in encounter](valueset-encounter-participant-type.html) --></type>
 <[**period**](encounter-definitions.html#Encounter.participant.period)><!-- **0..1** [Period](datatypes.html#Period) [Period of time during the encounter that the participant participated](terminologies.html#unbound) --></period>
 <[**individual**](encounter-definitions.html#Encounter.participant.individual)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Persons involved in the encounter other than the patient](terminologies.html#unbound) --></individual>
 </participant>
 <[**appointment**](encounter-definitions.html#Encounter.appointment)><!-- **0..*** [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) [The appointment that scheduled this encounter](terminologies.html#unbound) --></appointment>
 <[**period**](encounter-definitions.html#Encounter.period)><!-- **0..1** [Period](datatypes.html#Period) [The start and end time of the encounter](terminologies.html#unbound) --></period>
 <[**length**](encounter-definitions.html#Encounter.length)><!-- **0..1** [Duration](datatypes.html#Duration) [Quantity of time the encounter lasted (less time absent)](terminologies.html#unbound) --></length>
 <[**reasonCode**](encounter-definitions.html#Encounter.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Coded reason the encounter takes place](valueset-encounter-reason.html) --></reasonCode>
 <[**reasonReference**](encounter-definitions.html#Encounter.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) [Reason the encounter takes place (reference)](terminologies.html#unbound) --></reasonReference>
 <[**diagnosis**](encounter-definitions.html#Encounter.diagnosis)> <!-- **0..*** The list of diagnosis relevant to this encounter -->
 <[**condition**](encounter-definitions.html#Encounter.diagnosis.condition)><!-- **1..1** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)) [The diagnosis or procedure relevant to the encounter](terminologies.html#unbound) --></condition>
 <[**use**](encounter-definitions.html#Encounter.diagnosis.use)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)](valueset-diagnosis-role.html) --></use>
 <[**rank**](encounter-definitions.html#Encounter.diagnosis.rank) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [Ranking of the diagnosis (for each role type)](terminologies.html#unbound) -->
 </diagnosis>
 <[**account**](encounter-definitions.html#Encounter.account)><!-- **0..*** [Reference](references.html#Reference)([Account](account.html#Account)) [The set of accounts that may be used for billing for this Encounter](terminologies.html#unbound) --></account>
 <[**hospitalization**](encounter-definitions.html#Encounter.hospitalization)> <!-- **0..1** Details about the admission to a healthcare service -->
 <[**preAdmissionIdentifier**](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Pre-admission identifier](terminologies.html#unbound) --></preAdmissionIdentifier>
 <[**origin**](encounter-definitions.html#Encounter.hospitalization.origin)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) [The location/organization from which the patient came before admission](terminologies.html#unbound) --></origin>
 <[**admitSource**](encounter-definitions.html#Encounter.hospitalization.admitSource)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [From where patient was admitted (physician referral, transfer)](valueset-encounter-admit-source.html) --></admitSource>
 <[**reAdmission**](encounter-definitions.html#Encounter.hospitalization.reAdmission)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission](v2/0092/index.html) --></reAdmission>
 <[**dietPreference**](encounter-definitions.html#Encounter.hospitalization.dietPreference)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Diet preferences reported by the patient](valueset-encounter-diet.html) --></dietPreference>
 <[**specialCourtesy**](encounter-definitions.html#Encounter.hospitalization.specialCourtesy)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Special courtesies (VIP, board member)](valueset-encounter-special-courtesy.html) --></specialCourtesy>
 <[**specialArrangement**](encounter-definitions.html#Encounter.hospitalization.specialArrangement)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Wheelchair, translator, stretcher, etc.](valueset-encounter-special-arrangements.html) --></specialArrangement>
 <[**destination**](encounter-definitions.html#Encounter.hospitalization.destination)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) [Location/organization to which the patient is discharged](terminologies.html#unbound) --></destination>
 <[**dischargeDisposition**](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Category or kind of location after discharge](valueset-encounter-discharge-disposition.html) --></dischargeDisposition>
 </hospitalization>
 <[**location**](encounter-definitions.html#Encounter.location)> <!-- **0..*** List of locations where the patient has been -->
 <[**location**](encounter-definitions.html#Encounter.location.location)><!-- **1..1** [Reference](references.html#Reference)([Location](location.html#Location)) [Location the encounter takes place](terminologies.html#unbound) --></location>
 <[**status**](encounter-definitions.html#Encounter.location.status) value="[[code](datatypes.html#code)]"/><!-- **0..1** [planned | active | reserved | completed](valueset-encounter-location-status.html) -->
 <[**physicalType**](encounter-definitions.html#Encounter.location.physicalType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The physical type of the location (usually the level in the location hierachy - bed room ward etc.)](valueset-location-physical-type.html) --></physicalType>
 <[**period**](encounter-definitions.html#Encounter.location.period)><!-- **0..1** [Period](datatypes.html#Period) [Time period during which the patient was present at the location](terminologies.html#unbound) --></period>
 </location>
 <[**serviceProvider**](encounter-definitions.html#Encounter.serviceProvider)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [The organization (facility) responsible for this encounter](terminologies.html#unbound) --></serviceProvider>
 <[**partOf**](encounter-definitions.html#Encounter.partOf)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Another Encounter this encounter is part of](terminologies.html#unbound) --></partOf>
</Encounter>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Encounter**](encounter-definitions.html#Encounter)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](encounter-definitions.html#Encounter.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Identifier(s) by which this encounter is known](terminologies.html#unbound)
 "[status](encounter-definitions.html#Encounter.status)" : "<[code](datatypes.html#code)>", // **R!** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html)
 "[statusHistory](encounter-definitions.html#Encounter.statusHistory)" : [{ // [List of past encounter statuses](terminologies.html#unbound)
 "[status](encounter-definitions.html#Encounter.statusHistory.status)" : "<[code](datatypes.html#code)>", // **R!** [planned | arrived | triaged | in-progress | onleave | finished | cancelled +](valueset-encounter-status.html)
 "[period](encounter-definitions.html#Encounter.statusHistory.period)" : { [Period](datatypes.html#Period) } // **R!** [The time that the episode was in the specified status](terminologies.html#unbound)
 }],
 "[class](encounter-definitions.html#Encounter.class)" : { [Coding](datatypes.html#Coding) }, // **R!** [Classification of patient encounter](v3/ActEncounterCode/vs.html)
 "[classHistory](encounter-definitions.html#Encounter.classHistory)" : [{ // [List of past encounter classes](terminologies.html#unbound)
 "[class](encounter-definitions.html#Encounter.classHistory.class)" : { [Coding](datatypes.html#Coding) }, // **R!** [inpatient | outpatient | ambulatory | emergency +](v3/ActEncounterCode/vs.html)
 "[period](encounter-definitions.html#Encounter.classHistory.period)" : { [Period](datatypes.html#Period) } // **R!** [The time that the episode was in the specified class](terminologies.html#unbound)
 }],
 "[type](encounter-definitions.html#Encounter.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Specific type of encounter](valueset-encounter-type.html)
 "[serviceType](encounter-definitions.html#Encounter.serviceType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Specific type of service](valueset-service-type.html)
 "[priority](encounter-definitions.html#Encounter.priority)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Indicates the urgency of the encounter](v3/ActPriority/vs.html)
 "[subject](encounter-definitions.html#Encounter.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [The patient or group present at the encounter](terminologies.html#unbound)
 "[episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare)" : [{ [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) }], // [Episode(s) of care that this encounter should be recorded against](terminologies.html#unbound)
 "[basedOn](encounter-definitions.html#Encounter.basedOn)" : [{ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }], // [The ServiceRequest that initiated this encounter](terminologies.html#unbound)
 "[participant](encounter-definitions.html#Encounter.participant)" : [{ // [List of participants involved in the encounter](terminologies.html#unbound)
 "[type](encounter-definitions.html#Encounter.participant.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Role of participant in encounter](valueset-encounter-participant-type.html)
 "[period](encounter-definitions.html#Encounter.participant.period)" : { [Period](datatypes.html#Period) }, // [Period of time during the encounter that the participant participated](terminologies.html#unbound)
 "[individual](encounter-definitions.html#Encounter.participant.individual)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) } // [Persons involved in the encounter other than the patient](terminologies.html#unbound)
 }],
 "[appointment](encounter-definitions.html#Encounter.appointment)" : [{ [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) }], // [The appointment that scheduled this encounter](terminologies.html#unbound)
 "[period](encounter-definitions.html#Encounter.period)" : { [Period](datatypes.html#Period) }, // [The start and end time of the encounter](terminologies.html#unbound)
 "[length](encounter-definitions.html#Encounter.length)" : { [Duration](datatypes.html#Duration) }, // [Quantity of time the encounter lasted (less time absent)](terminologies.html#unbound)
 "[reasonCode](encounter-definitions.html#Encounter.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Coded reason the encounter takes place](valueset-encounter-reason.html)
 "[reasonReference](encounter-definitions.html#Encounter.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) }], // [Reason the encounter takes place (reference)](terminologies.html#unbound)
 "[diagnosis](encounter-definitions.html#Encounter.diagnosis)" : [{ // [The list of diagnosis relevant to this encounter](terminologies.html#unbound)
 "[condition](encounter-definitions.html#Encounter.diagnosis.condition)" : { [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)) }, // **R!** [The diagnosis or procedure relevant to the encounter](terminologies.html#unbound)
 "[use](encounter-definitions.html#Encounter.diagnosis.use)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)](valueset-diagnosis-role.html)
 "[rank](encounter-definitions.html#Encounter.diagnosis.rank)" : "<[positiveInt](datatypes.html#positiveInt)>" // [Ranking of the diagnosis (for each role type)](terminologies.html#unbound)
 }],
 "[account](encounter-definitions.html#Encounter.account)" : [{ [Reference](references.html#Reference)([Account](account.html#Account)) }], // [The set of accounts that may be used for billing for this Encounter](terminologies.html#unbound)
 "[hospitalization](encounter-definitions.html#Encounter.hospitalization)" : { // [Details about the admission to a healthcare service](terminologies.html#unbound)
 "[preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Pre-admission identifier](terminologies.html#unbound)
 "[origin](encounter-definitions.html#Encounter.hospitalization.origin)" : { [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) }, // [The location/organization from which the patient came before admission](terminologies.html#unbound)
 "[admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [From where patient was admitted (physician referral, transfer)](valueset-encounter-admit-source.html)
 "[reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission](v2/0092/index.html)
 "[dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Diet preferences reported by the patient](valueset-encounter-diet.html)
 "[specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Special courtesies (VIP, board member)](valueset-encounter-special-courtesy.html)
 "[specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Wheelchair, translator, stretcher, etc.](valueset-encounter-special-arrangements.html)
 "[destination](encounter-definitions.html#Encounter.hospitalization.destination)" : { [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) }, // [Location/organization to which the patient is discharged](terminologies.html#unbound)
 "[dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Category or kind of location after discharge](valueset-encounter-discharge-disposition.html)
 },
 "[location](encounter-definitions.html#Encounter.location)" : [{ // [List of locations where the patient has been](terminologies.html#unbound)
 "[location](encounter-definitions.html#Encounter.location.location)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // **R!** [Location the encounter takes place](terminologies.html#unbound)
 "[status](encounter-definitions.html#Encounter.location.status)" : "<[code](datatypes.html#code)>", // [planned | active | reserved | completed](valueset-encounter-location-status.html)
 "[physicalType](encounter-definitions.html#Encounter.location.physicalType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The physical type of the location (usually the level in the location hierachy - bed room ward etc.)](valueset-location-physical-type.html)
 "[period](encounter-definitions.html#Encounter.location.period)" : { [Period](datatypes.html#Period) } // [Time period during which the patient was present at the location](terminologies.html#unbound)
 }],
 "[serviceProvider](encounter-definitions.html#Encounter.serviceProvider)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [The organization (facility) responsible for this encounter](terminologies.html#unbound)
 "[partOf](encounter-definitions.html#Encounter.partOf)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) } // [Another Encounter this encounter is part of](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Encounter**](encounter-definitions.html#Encounter);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Encounter.identifier](encounter-definitions.html#Encounter.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Identifier(s) by which this encounter is known
 fhir:[Encounter.status](encounter-definitions.html#Encounter.status) [ [code](datatypes.html#code) ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
 fhir:[Encounter.statusHistory](encounter-definitions.html#Encounter.statusHistory) [ # 0..* List of past encounter statuses
 fhir:[Encounter.statusHistory.status](encounter-definitions.html#Encounter.statusHistory.status) [ [code](datatypes.html#code) ]; # 1..1 planned | arrived | triaged | in-progress | onleave | finished | cancelled +
 fhir:[Encounter.statusHistory.period](encounter-definitions.html#Encounter.statusHistory.period) [ [Period](datatypes.html#Period) ]; # 1..1 The time that the episode was in the specified status
 ], ...;
 fhir:[Encounter.class](encounter-definitions.html#Encounter.class) [ [Coding](datatypes.html#Coding) ]; # 1..1 Classification of patient encounter
 fhir:[Encounter.classHistory](encounter-definitions.html#Encounter.classHistory) [ # 0..* List of past encounter classes
 fhir:[Encounter.classHistory.class](encounter-definitions.html#Encounter.classHistory.class) [ [Coding](datatypes.html#Coding) ]; # 1..1 inpatient | outpatient | ambulatory | emergency +
 fhir:[Encounter.classHistory.period](encounter-definitions.html#Encounter.classHistory.period) [ [Period](datatypes.html#Period) ]; # 1..1 The time that the episode was in the specified class
 ], ...;
 fhir:[Encounter.type](encounter-definitions.html#Encounter.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Specific type of encounter
 fhir:[Encounter.serviceType](encounter-definitions.html#Encounter.serviceType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Specific type of service
 fhir:[Encounter.priority](encounter-definitions.html#Encounter.priority) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Indicates the urgency of the encounter
 fhir:[Encounter.subject](encounter-definitions.html#Encounter.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 The patient or group present at the encounter
 fhir:[Encounter.episodeOfCare](encounter-definitions.html#Encounter.episodeOfCare) [ [Reference](references.html#Reference)([EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) ], ... ; # 0..* Episode(s) of care that this encounter should be recorded against
 fhir:[Encounter.basedOn](encounter-definitions.html#Encounter.basedOn) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ], ... ; # 0..* The ServiceRequest that initiated this encounter
 fhir:[Encounter.participant](encounter-definitions.html#Encounter.participant) [ # 0..* List of participants involved in the encounter
 fhir:[Encounter.participant.type](encounter-definitions.html#Encounter.participant.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Role of participant in encounter
 fhir:[Encounter.participant.period](encounter-definitions.html#Encounter.participant.period) [ [Period](datatypes.html#Period) ]; # 0..1 Period of time during the encounter that the participant participated
 fhir:[Encounter.participant.individual](encounter-definitions.html#Encounter.participant.individual) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Persons involved in the encounter other than the patient
 ], ...;
 fhir:[Encounter.appointment](encounter-definitions.html#Encounter.appointment) [ [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) ], ... ; # 0..* The appointment that scheduled this encounter
 fhir:[Encounter.period](encounter-definitions.html#Encounter.period) [ [Period](datatypes.html#Period) ]; # 0..1 The start and end time of the encounter
 fhir:[Encounter.length](encounter-definitions.html#Encounter.length) [ [Duration](datatypes.html#Duration) ]; # 0..1 Quantity of time the encounter lasted (less time absent)
 fhir:[Encounter.reasonCode](encounter-definitions.html#Encounter.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Coded reason the encounter takes place
 fhir:[Encounter.reasonReference](encounter-definitions.html#Encounter.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) ], ... ; # 0..* Reason the encounter takes place (reference)
 fhir:[Encounter.diagnosis](encounter-definitions.html#Encounter.diagnosis) [ # 0..* The list of diagnosis relevant to this encounter
 fhir:[Encounter.diagnosis.condition](encounter-definitions.html#Encounter.diagnosis.condition) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)) ]; # 1..1 The diagnosis or procedure relevant to the encounter
 fhir:[Encounter.diagnosis.use](encounter-definitions.html#Encounter.diagnosis.use) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Role that this diagnosis has within the encounter (e.g. admission, billing, discharge â€¦)
 fhir:[Encounter.diagnosis.rank](encounter-definitions.html#Encounter.diagnosis.rank) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Ranking of the diagnosis (for each role type)
 ], ...;
 fhir:[Encounter.account](encounter-definitions.html#Encounter.account) [ [Reference](references.html#Reference)([Account](account.html#Account)) ], ... ; # 0..* The set of accounts that may be used for billing for this Encounter
 fhir:[Encounter.hospitalization](encounter-definitions.html#Encounter.hospitalization) [ # 0..1 Details about the admission to a healthcare service
 fhir:[Encounter.hospitalization.preAdmissionIdentifier](encounter-definitions.html#Encounter.hospitalization.preAdmissionIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Pre-admission identifier
 fhir:[Encounter.hospitalization.origin](encounter-definitions.html#Encounter.hospitalization.origin) [ [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) ]; # 0..1 The location/organization from which the patient came before admission
 fhir:[Encounter.hospitalization.admitSource](encounter-definitions.html#Encounter.hospitalization.admitSource) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 From where patient was admitted (physician referral, transfer)
 fhir:[Encounter.hospitalization.reAdmission](encounter-definitions.html#Encounter.hospitalization.reAdmission) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The type of hospital re-admission that has occurred (if any). If the value is absent, then this is not identified as a readmission
 fhir:[Encounter.hospitalization.dietPreference](encounter-definitions.html#Encounter.hospitalization.dietPreference) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Diet preferences reported by the patient
 fhir:[Encounter.hospitalization.specialCourtesy](encounter-definitions.html#Encounter.hospitalization.specialCourtesy) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Special courtesies (VIP, board member)
 fhir:[Encounter.hospitalization.specialArrangement](encounter-definitions.html#Encounter.hospitalization.specialArrangement) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Wheelchair, translator, stretcher, etc.
 fhir:[Encounter.hospitalization.destination](encounter-definitions.html#Encounter.hospitalization.destination) [ [Reference](references.html#Reference)([Location](location.html#Location)|[Organization](organization.html#Organization)) ]; # 0..1 Location/organization to which the patient is discharged
 fhir:[Encounter.hospitalization.dischargeDisposition](encounter-definitions.html#Encounter.hospitalization.dischargeDisposition) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Category or kind of location after discharge
 ];
 fhir:[Encounter.location](encounter-definitions.html#Encounter.location) [ # 0..* List of locations where the patient has been
 fhir:[Encounter.location.location](encounter-definitions.html#Encounter.location.location) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 1..1 Location the encounter takes place
 fhir:[Encounter.location.status](encounter-definitions.html#Encounter.location.status) [ [code](datatypes.html#code) ]; # 0..1 planned | active | reserved | completed
 fhir:[Encounter.location.physicalType](encounter-definitions.html#Encounter.location.physicalType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The physical type of the location (usually the level in the location hierachy - bed room ward etc.)
 fhir:[Encounter.location.period](encounter-definitions.html#Encounter.location.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time period during which the patient was present at the location
 ], ...;
 fhir:[Encounter.serviceProvider](encounter-definitions.html#Encounter.serviceProvider) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 The organization (facility) responsible for this encounter
 fhir:[Encounter.partOf](encounter-definitions.html#Encounter.partOf) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Another Encounter this encounter is part of
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Encounter](encounter.html#Encounter)
 | 
 | 
 |

 | 
 Encounter.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1

 

 | 
 |

 | 
 Encounter.statusHistory.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/encounter-status to http://hl7.org/fhir/ValueSet/encounter-status|4.0.1

 

 | 
 |

 | 
 Encounter.class | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Encounter.serviceType | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.basedOn | 
 
 

 - Renamed from incomingReferral to basedOn

 - Type Reference: Added Target Type ServiceRequest

 - Type Reference: Removed Target Type ReferralRequest

 

 | 
 |

 | 
 Encounter.participant.individual | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Encounter.appointment | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Encounter.reasonCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.reasonReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.diagnosis.use | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.hospitalization.origin | 
 
 

 - Type Reference: Added Target Type Organization

 

 | 
 |

 | 
 Encounter.hospitalization.destination | 
 
 

 - Type Reference: Added Target Type Organization

 

 | 
 |

 | 
 Encounter.location.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/encounter-location-status to http://hl7.org/fhir/ValueSet/encounter-location-status|4.0.1

 

 | 
 |

 | 
 Encounter.location.physicalType | 
 
 

 - Added Element

 

 | 
 |

 | 
 Encounter.reason | 
 
 

 - deleted

 

 | 
 |

 | 
 Encounter.diagnosis.role | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](encounter.diff.xml) or [JSON](encounter.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](encounter-version-maps.html) (status = 10 tests that all execute ok. All tests pass round-trip testing and 3 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](encounter-profiles.html) and the alternate definitions:
Master Definition [XML](encounter.profile.xml.html) + [JSON](encounter.profile.json.html),
[XML](xml.html) [Schema](encounter.xsd)/[Schematron](encounter.sch) + [JSON](json.html) 
[Schema](encounter.schema.json.html), [ShEx](encounter.shex.html) (for [Turtle](rdf.html)) + [see the extensions](encounter-profiles.html) & the [dependency analysis](encounter-dependencies.html)

### 8.11.3.1 
Terminology Bindings
 [
](encounter.html#tx)

 | Path | Definition | Type | Reference | |

 | Encounter.status**Encounter.statusHistory.status | Current state of the encounter. | [Required](terminologies.html#required) | [EncounterStatus](valueset-encounter-status.html) | |

 | Encounter.class
Encounter.classHistory.class | Classification of the encounter. | [Extensible](terminologies.html#extensible) | [v3.ActEncounterCode](v3/ActEncounterCode/vs.html) | |

 | Encounter.type | The type of encounter. | [Example](terminologies.html#example) | [EncounterType](valueset-encounter-type.html) | |

 | Encounter.serviceType | Broad categorization of the service that is to be provided. | [Example](terminologies.html#example) | [ServiceType](valueset-service-type.html) | |

 | Encounter.priority | Indicates the urgency of the encounter. | [Example](terminologies.html#example) | [v3.ActPriority](v3/ActPriority/vs.html) | |

 | Encounter.participant.type | Role of participant in encounter. | [Extensible](terminologies.html#extensible) | [ParticipantType](valueset-encounter-participant-type.html) | |

 | Encounter.reasonCode | Reason why the encounter takes place. | [Preferred](terminologies.html#preferred) | [EncounterReasonCodes](valueset-encounter-reason.html) | |

 | Encounter.diagnosis.use | The type of diagnosis this condition represents. | [Preferred](terminologies.html#preferred) | [DiagnosisRole](valueset-diagnosis-role.html) | |

 | Encounter.hospitalization.admitSource | From where the patient was admitted. | [Preferred](terminologies.html#preferred) | [AdmitSource](valueset-encounter-admit-source.html) | |

 | Encounter.hospitalization.reAdmission | The reason for re-admission of this hospitalization encounter. | [Example](terminologies.html#example) | [v2.0092](v2/0092/index.html) | |

 | Encounter.hospitalization.dietPreference | Medical, cultural or ethical food preferences to help with catering requirements. | [Example](terminologies.html#example) | [Diet](valueset-encounter-diet.html) | |

 | Encounter.hospitalization.specialCourtesy | Special courtesies. | [Preferred](terminologies.html#preferred) | [SpecialCourtesy](valueset-encounter-special-courtesy.html) | |

 | Encounter.hospitalization.specialArrangement | Special arrangements. | [Preferred](terminologies.html#preferred) | [SpecialArrangements](valueset-encounter-special-arrangements.html) | |

 | Encounter.hospitalization.dischargeDisposition | Discharge Disposition. | [Example](terminologies.html#example) | [DischargeDisposition](valueset-encounter-discharge-disposition.html) | |

 | Encounter.location.status | The status of the location. | [Required](terminologies.html#required) | [EncounterLocationStatus](valueset-encounter-location-status.html) | |

 | Encounter.location.physicalType | Physical form of the location. | [Example](terminologies.html#example) | [LocationType](valueset-location-physical-type.html) | |

 

## 8.11.4 Notes [
](encounter.html#notes)

- The class* element describes the setting (in/outpatient etc.) in which the Encounter took place. Since this is important for 
interpreting the context of the encounter, choosing the appropriate business rules to enforce and for the management of the process, this element
is required.

- In future versions of FHIR, some kind of charge posting vehicle (e.g. Account) will be added.

## 8.11.5 Example usage [
](encounter.html#examples)

As stated, Encounter allows a flexible nesting of Encounters using the partOf element. For example:

- A patient is admitted for two weeks - This could be modeled using a single Encounter instance,
in which the start and length are given for the duration of the whole stay. The admitting doctor and
the responsible doctor during the stay are specified using the Participant component.

- During the encounter, the patient moves from the admitting department to the Intensive Care unit and back - 
Three more detailed additional Encounters can be created, one for each location in which the patient stayed.
Each of these Encounters has a single location (twice the admitting department and once
the Intensive Care unit) and one or more participants at that location. These Encounters may use the partOf 
relationship to indicate these movements occurred during the longer overarching Encounter.

- During the last part of the stay, the patient is visited by the members of the multi-disciplinary team that
treated him for final evaluation - If relevant, for each of these short visits, an Encounter may be created
with a single participant. Since these took place during the last part of the stay, the partOf element can be
used to associate these short visits with either the third patient movement or the bigger overall encounter.

Exactly how the Encounter is used depends on information available in the source system, the relevance of exchange
of each level of Encounter and demands specific to the communicating partners. The expectation is that for each
domain of exchange, profiles are used to limit the flexibility of Encounter to meet the demands of the use case.

## 8.11.6 Search Parameters [
](encounter.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| Name** | **Type** | **Description** | **Expression** | **In Common** | |

| account | [reference](search.html#reference) | The set of accounts that may be used for billing for this Encounter | Encounter.account
([Account](account.html)) | | |

| appointment | [reference](search.html#reference) | The appointment that scheduled this encounter | Encounter.appointment
([Appointment](appointment.html)) | | |

| based-on | [reference](search.html#reference) | The ServiceRequest that initiated this encounter | Encounter.basedOn
([ServiceRequest](servicerequest.html)) | | |

| class | [token](search.html#token) | Classification of patient encounter | Encounter.class | | |

| date | [date](search.html#date) | A date within the period the Encounter lasted | Encounter.period | [17 Resources](searchparameter-registry.html#clinical-date) | |

| diagnosis | [reference](search.html#reference) | The diagnosis or procedure relevant to the encounter | Encounter.diagnosis.condition
([Condition](condition.html), [Procedure](procedure.html)) | | |

| episode-of-care | [reference](search.html#reference) | Episode(s) of care that this encounter should be recorded against | Encounter.episodeOfCare
([EpisodeOfCare](episodeofcare.html)) | | |

| identifier | [token](search.html#token) | Identifier(s) by which this encounter is known | Encounter.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| length | [quantity](search.html#quantity) | Length of encounter in days | Encounter.length | | |

| location | [reference](search.html#reference) | Location the encounter takes place | Encounter.location.location
([Location](location.html)) | | |

| location-period | [date](search.html#date) | Time period during which the patient was present at the location | Encounter.location.period | | |

| part-of | [reference](search.html#reference) | Another Encounter this encounter is part of | Encounter.partOf
([Encounter](encounter.html)) | | |

| participant | [reference](search.html#reference) | Persons involved in the encounter other than the patient | Encounter.participant.individual
([Practitioner](practitioner.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| participant-type | [token](search.html#token) | Role of participant in encounter | Encounter.participant.type | | |

| patient | [reference](search.html#reference) | The patient or group present at the encounter | Encounter.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| practitioner | [reference](search.html#reference) | Persons involved in the encounter other than the patient | Encounter.participant.individual.where(resolve() is Practitioner)
([Practitioner](practitioner.html)) | | |

| reason-code | [token](search.html#token) | Coded reason the encounter takes place | Encounter.reasonCode | | |

| reason-reference | [reference](search.html#reference) | Reason the encounter takes place (reference) | Encounter.reasonReference
([Condition](condition.html), [Observation](observation.html), [Procedure](procedure.html), [ImmunizationRecommendation](immunizationrecommendation.html)) | | |

| service-provider | [reference](search.html#reference) | The organization (facility) responsible for this encounter | Encounter.serviceProvider
([Organization](organization.html)) | | |

| special-arrangement | [token](search.html#token) | Wheelchair, translator, stretcher, etc. | Encounter.hospitalization.specialArrangement | | |

| status | [token](search.html#token) | planned | arrived | triaged | in-progress | onleave | finished | cancelled + | Encounter.status | | |

| subject | [reference](search.html#reference) | The patient or group present at the encounter | Encounter.subject
([Group](group.html), [Patient](patient.html)) | | |

| type | [token](search.html#token) | Specific type of encounter | Encounter.type | [5 Resources](searchparameter-registry.html#clinical-type) | |