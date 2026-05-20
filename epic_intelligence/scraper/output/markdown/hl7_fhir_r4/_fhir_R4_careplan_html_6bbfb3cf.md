# CarePlan - FHIR v4.0.1Business identifiers assigned to this care plan by the performer or other systems which remain constant as the resource is updated and propagates from server to serverThe URL pointing to a FHIR-defined protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlanThe URL pointing to an externally maintained protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlanA care plan that is fulfilled in whole or in part by this care planCompleted or terminated care plan whose function is taken by this new care planA larger care plan of which this particular care plan is a component or stepIndicates whether the plan is currently being acted upon, represents future intentions or is now a historical record (this element modifies the meaning of other elements)Indicates whether the plan is currently being acted upon, represents future intentions or is now a historical record. (Strength=Required)Indicates the level of authority/intentionality associated with the care plan and where the care plan fits into the workflow chain (this element modifies the meaning of other elements)Codes indicating the degree of authority/intentionality associated with a care plan. (Strength=Required)Identifies what "kind" of plan this is to support differentiation between multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma", "disease management", "wellness plan", etcIdentifies what "kind" of plan this is to support differentiation between multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma", "disease management", etc. (Strength=Example)Human-friendly name for the care planA description of the scope and nature of the planIdentifies the patient or group whose intended care is described by the planThe Encounter during which this CarePlan was created or to which the creation of this record is tightly associatedIndicates when the plan did (or is intended to) come into effect and endRepresents when this particular CarePlan record was created in the system, which is often a system-generated dateWhen populated, the author is responsible for the care plan.  The care plan is attributed to the authorIdentifies the individual(s) or organization who provided the contents of the care planIdentifies all people and organizations who are expected to be involved in the care envisioned by this planIdentifies the conditions/problems/concerns/diagnoses/etc. whose management and/or mitigation are handled by this planIdentifies portions of the patient's record that specifically influenced the formation of the plan.  These might include comorbidities, recent procedures, limitations, recent assessments, etcDescribes the intended objective(s) of carrying out the care planGeneral notes about the care plan not covered elsewhereIdentifies the outcome at the point when the status of the activity is assessed.  For example, the outcome of an education activity could be patient understands (or not)Identifies the results of the activity. (Strength=Example)Details of the outcome or action resulting from the activity.  The reference to an "event" resource, such as Procedure or Encounter or Observation, is the result/outcome of the activity itself.  The activity can be conveyed using CarePlan.activity.detail OR using the CarePlan.activity.reference (a reference to a “request” resource)Notes about the adherence/status/progress of the activityThe details of the proposed activity represented in a specific resourceA description of the kind of resource the in-line definition of a care plan activity is representing.  The CarePlan.activity.detail is an in-line definition when a resource is not referenced using CarePlan.activity.reference.  For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequestResource types defined as part of FHIR that can be represented as in-line definitions of a care plan activity. (Strength=Required)The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activityThe URL pointing to an externally maintained protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activityDetailed description of the type of planned activity; e.g. what lab test, what procedure, what kind of encounterDetailed description of the type of activity; e.g. What lab test, what procedure, what kind of encounter. (Strength=Example)Provides the rationale that drove the inclusion of this particular activity as part of the plan or the reason why the activity was prohibitedIdentifies why a care plan activity is needed.  Can include any health condition codes as well as such concepts as "general wellness", prophylaxis, surgical preparation, etc. (Strength=Example)Indicates another resource, such as the health condition(s), whose existence justifies this request and drove the inclusion of this particular activity as part of the planInternal reference that identifies the goals that this activity is intended to contribute towards meetingIdentifies what progress is being made for the specific activity (this element modifies the meaning of other elements)Codes that reflect the current state of a care plan activity within its overall life cycle. (Strength=Required)Provides reason why the activity isn't yet started, is on hold, was cancelled, etcIf true, indicates that the described activity is one that must NOT be engaged in when following the plan.  If false, or missing, indicates that the described activity is one that should be engaged in when following the plan (this element modifies the meaning of other elements)The period, timing or frequency upon which the described activity is to occurIdentifies the facility where the activity will occur; e.g. home, hospital, specific clinic, etcIdentifies who's expected to be involved in the activityIdentifies the food, drug or other product to be consumed or supplied in the activityA product supplied or administered as part of a care plan activity. (Strength=Example)Identifies the quantity expected to be consumed in a given dayIdentifies the quantity expected to be supplied, administered or consumed by the subjectThis provides a textual description of constraints on the intended activity occurrence, including relation to other activities.  It may also include objectives, pre-conditions and end-conditions.  Finally, it may convey specifics about the activity such as body site, method, route, etcA simple summary of a planned activity suitable for a general care plan system (e.g. form driven) that doesn't know about specific resources such as procedure etcIdentifies a planned action to occur as part of the plan.  For example, a medication to be used, lab tests to perform, self-monitoring, education, etcBusiness identifiers assigned to this care plan by the performer or other systems which remain constant as the resource is updated and propagates from server to serverThe URL pointing to a FHIR-defined protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlanThe URL pointing to an externally maintained protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlanA care plan that is fulfilled in whole or in part by this care planCompleted or terminated care plan whose function is taken by this new care planA larger care plan of which this particular care plan is a component or stepIndicates whether the plan is currently being acted upon, represents future intentions or is now a historical record (this element modifies the meaning of other elements)Indicates whether the plan is currently being acted upon, represents future intentions or is now a historical record. (Strength=Required)Indicates the level of authority/intentionality associated with the care plan and where the care plan fits into the workflow chain (this element modifies the meaning of other elements)Codes indicating the degree of authority/intentionality associated with a care plan. (Strength=Required)Identifies what "kind" of plan this is to support differentiation between multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma", "disease management", "wellness plan", etcIdentifies what "kind" of plan this is to support differentiation between multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma", "disease management", etc. (Strength=Example)Human-friendly name for the care planA description of the scope and nature of the planIdentifies the patient or group whose intended care is described by the planThe Encounter during which this CarePlan was created or to which the creation of this record is tightly associatedIndicates when the plan did (or is intended to) come into effect and endRepresents when this particular CarePlan record was created in the system, which is often a system-generated dateWhen populated, the author is responsible for the care plan.  The care plan is attributed to the authorIdentifies the individual(s) or organization who provided the contents of the care planIdentifies all people and organizations who are expected to be involved in the care envisioned by this planIdentifies the conditions/problems/concerns/diagnoses/etc. whose management and/or mitigation are handled by this planIdentifies portions of the patient's record that specifically influenced the formation of the plan.  These might include comorbidities, recent procedures, limitations, recent assessments, etcDescribes the intended objective(s) of carrying out the care planGeneral notes about the care plan not covered elsewhereIdentifies the outcome at the point when the status of the activity is assessed.  For example, the outcome of an education activity could be patient understands (or not)Identifies the results of the activity. (Strength=Example)Details of the outcome or action resulting from the activity.  The reference to an "event" resource, such as Procedure or Encounter or Observation, is the result/outcome of the activity itself.  The activity can be conveyed using CarePlan.activity.detail OR using the CarePlan.activity.reference (a reference to a “request” resource)Notes about the adherence/status/progress of the activityThe details of the proposed activity represented in a specific resourceA description of the kind of resource the in-line definition of a care plan activity is representing.  The CarePlan.activity.detail is an in-line definition when a resource is not referenced using CarePlan.activity.reference.  For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequestResource types defined as part of FHIR that can be represented as in-line definitions of a care plan activity. (Strength=Required)The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activityThe URL pointing to an externally maintained protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activityDetailed description of the type of planned activity; e.g. what lab test, what procedure, what kind of encounterDetailed description of the type of activity; e.g. What lab test, what procedure, what kind of encounter. (Strength=Example)Provides the rationale that drove the inclusion of this particular activity as part of the plan or the reason why the activity was prohibitedIdentifies why a care plan activity is needed.  Can include any health condition codes as well as such concepts as "general wellness", prophylaxis, surgical preparation, etc. (Strength=Example)Indicates another resource, such as the health condition(s), whose existence justifies this request and drove the inclusion of this particular activity as part of the planInternal reference that identifies the goals that this activity is intended to contribute towards meetingIdentifies what progress is being made for the specific activity (this element modifies the meaning of other elements)Codes that reflect the current state of a care plan activity within its overall life cycle. (Strength=Required)Provides reason why the activity isn't yet started, is on hold, was cancelled, etcIf true, indicates that the described activity is one that must NOT be engaged in when following the plan.  If false, or missing, indicates that the described activity is one that should be engaged in when following the plan (this element modifies the meaning of other elements)The period, timing or frequency upon which the described activity is to occurIdentifies the facility where the activity will occur; e.g. home, hospital, specific clinic, etcIdentifies who's expected to be involved in the activityIdentifies the food, drug or other product to be consumed or supplied in the activityA product supplied or administered as part of a care plan activity. (Strength=Example)Identifies the quantity expected to be consumed in a given dayIdentifies the quantity expected to be supplied, administered or consumed by the subjectThis provides a textual description of constraints on the intended activity occurrence, including relation to other activities.  It may also include objectives, pre-conditions and end-conditions.  Finally, it may convey specifics about the activity such as body site, method, route, etcA simple summary of a planned activity suitable for a general care plan system (e.g. form driven) that doesn't know about specific resources such as procedure etcIdentifies a planned action to occur as part of the plan.  For example, a medication to be used, lab tests to perform, self-monitoring, education, etc

> Source: https://hl7.org/fhir/R4/careplan.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/careplan.html) [R4B](http://hl7.org/fhir/R4B/careplan.html) **R4** [R3](http://hl7.org/fhir/STU3/careplan.html) [R2](http://hl7.org/fhir/DSTU2/careplan.html)
 

# 9.5 Resource CarePlan - Content [
](careplan.html#9.5)

| [Patient Care ](http://www.hl7.org/Special/committees/patientcare/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.

## 9.5.1 Scope and Usage [
](careplan.html#scope)

CarePlan is one of the [request](workflow.html#request) resources in the FHIR [workflow](workflow.html) specification.

 
Care Plans are used in many areas of healthcare with a variety of scopes.
They can be as simple as a general practitioner keeping track of when their 
patient is next due for a tetanus immunization through to a detailed plan for
an oncology patient covering diet, chemotherapy, radiation, lab work and
counseling with detailed timing relationships, pre-conditions and goals. They may
be used in veterinary care or clinical research to describe the care of a herd or
other collection of animals. In public health, they may describe education or
immunization campaigns.

This resource takes an intermediate approach to complexity. It captures basic details about
who is involved and what actions are intended without dealing in discrete data
about dependencies and timing relationships. These can be supported where
necessary using the extension mechanism.

The scope of care plans may vary widely. Examples include:

- 
Multi-disciplinary cross-organizational care plans; e.g. An oncology plan including the 
oncologist, home nursing staff, pharmacy and others

- 
Plans to manage specific disease/condition(s) (e.g. nutritional plan for a patient post bowel 
resection, neurological plan post head injury, pre-natal plan, post-partum plan, grief management 
plan, etc.)

- 
Decision support generated plans following specific practice guidelines (e.g. stroke care plan, 
diabetes plan, falls prevention, etc.)

- 
Self-maintained patient or care-giver authored plans identifying their goals and an integrated
understanding of actions to be taken

This resource can be used to represent both proposed plans (for example, recommendations from
a decision support engine or returned as part of a consult report) as well as active plans. The
nature of the plan is communicated by the status. Some systems may need to filter CarePlans to ensure
that only appropriate plans are exposed via a given user interface.

## 9.5.2 Boundaries and Relationships [
](careplan.html#bnr)

For simplicity's sake, CarePlan allows the inline definition of activities as part of a plan using 
the `activity.detail` element. However, activities can also be defined using references
to the various "request" resources. These references could be to resources with a status of
"planned" or to an active order. It is possible for planned activities to exist (e.g. appointments)
without needing a CarePlan at all. CarePlans are used when there's a need to group activities,
goals and/or participants together to provide some degree of context.

CarePlans can be tied to specific [Conditions](condition.html), however they can also be 
condition-independent and instead focused on a particular type of care (e.g. psychological, nutritional)
or the care delivered by a particular practitioner or group of practitioners.

An [ImmunizationRecommendation](immunizationrecommendation.html) can be interpreted as a narrow
type of CarePlan dealing only with immunization events. Where such information could appear in either
resource, the immunization-specific resource is preferred.

CarePlans represent a specific plan instance for a particular patient or group. It is not intended to be used to define generic plans or protocols that are independent of a
specific individual or group. CarePlan represents a specific intent, not a general definition. Protocols and order sets are supported through [PlanDefinition](plandefinition.html).

This resource is referenced by itself, [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Media](media.html#Media), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [Observation](observation.html#Observation), [Procedure](procedure.html#Procedure), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse) and [ServiceRequest](servicerequest.html#ServiceRequest)

## 9.5.3 
Resource Content
 [
](careplan.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [CarePlan](careplan-definitions.html#CarePlan) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Healthcare plan for patient or group**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](careplan-definitions.html#CarePlan.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this plan
 | |

| [instantiatesCanonical](careplan-definitions.html#CarePlan.instantiatesCanonical) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html) | [Questionnaire](questionnaire.html) | [Measure](measure.html) | [ActivityDefinition](activitydefinition.html) | [OperationDefinition](operationdefinition.html)) | Instantiates FHIR protocol or definition
 | |

| [instantiatesUri](careplan-definitions.html#CarePlan.instantiatesUri) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [uri](datatypes.html#uri) | Instantiates external protocol or definition
 | |

| [basedOn](careplan-definitions.html#CarePlan.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CarePlan](careplan.html)) | Fulfills CarePlan
 | |

| [replaces](careplan-definitions.html#CarePlan.replaces) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CarePlan](careplan.html)) | CarePlan replaced by this CarePlan
 | |

| [partOf](careplan-definitions.html#CarePlan.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CarePlan](careplan.html)) | Part of referenced CarePlan
 | |

| [status](careplan-definitions.html#CarePlan.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | draft | active | on-hold | revoked | completed | entered-in-error | unknown
[RequestStatus](valueset-request-status.html) ([Required](terminologies.html#required)) | |

| [intent](careplan-definitions.html#CarePlan.intent) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | proposal | plan | order | option
[Care Plan Intent](valueset-care-plan-intent.html) ([Required](terminologies.html#required)) | |

| [category](careplan-definitions.html#CarePlan.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of plan
[Care Plan Category](valueset-care-plan-category.html) ([Example](terminologies.html#example))
 | |

| [title](careplan-definitions.html#CarePlan.title) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human-friendly name for the care plan | |

| [description](careplan-definitions.html#CarePlan.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Summary of nature of plan | |

| [subject](careplan-definitions.html#CarePlan.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who the care plan is for | |

| [encounter](careplan-definitions.html#CarePlan.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [period](careplan-definitions.html#CarePlan.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Time period plan covers | |

| [created](careplan-definitions.html#CarePlan.created) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | Date record was first recorded | |

| [author](careplan-definitions.html#CarePlan.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Device](device.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html) | [CareTeam](careteam.html)) | Who is the designated responsible party | |

| [contributor](careplan-definitions.html#CarePlan.contributor) | | 0..* | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Device](device.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html) | [CareTeam](careteam.html)) | Who provided the content of the care plan
 | |

| [careTeam](careplan-definitions.html#CarePlan.careTeam) | | 0..* | [Reference](references.html#Reference)([CareTeam](careteam.html)) | Who's involved in plan?
 | |

| [addresses](careplan-definitions.html#CarePlan.addresses) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html)) | Health issues this plan addresses
 | |

| [supportingInfo](careplan-definitions.html#CarePlan.supportingInfo) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Information considered as part of plan
 | |

| [goal](careplan-definitions.html#CarePlan.goal) | | 0..* | [Reference](references.html#Reference)([Goal](goal.html)) | Desired outcome of plan
 | |

| [activity](careplan-definitions.html#CarePlan.activity) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Action to occur as part of plan
+ Rule: Provide a reference or detail, not both
 | |

| [outcomeCodeableConcept](careplan-definitions.html#CarePlan.activity.outcomeCodeableConcept) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Results of the activity
[Care Plan Activity Outcome](valueset-care-plan-activity-outcome.html) ([Example](terminologies.html#example))
 | |

| [outcomeReference](careplan-definitions.html#CarePlan.activity.outcomeReference) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Appointment, Encounter, Procedure, etc.
 | |

| [progress](careplan-definitions.html#CarePlan.activity.progress) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments about the activity status/progress
 | |

| [reference](careplan-definitions.html#CarePlan.activity.reference) | [I](conformance-rules.html#constraints) | 0..1 | [Reference](references.html#Reference)([Appointment](appointment.html) | [CommunicationRequest](communicationrequest.html) | [DeviceRequest](devicerequest.html) | [MedicationRequest](medicationrequest.html) | [NutritionOrder](nutritionorder.html) | [Task](task.html) | [ServiceRequest](servicerequest.html) | [VisionPrescription](visionprescription.html) | [RequestGroup](requestgroup.html)) | Activity details defined in specific resource | |

| [detail](careplan-definitions.html#CarePlan.activity.detail) | [I](conformance-rules.html#constraints) | 0..1 | [BackboneElement](backboneelement.html) | In-line definition of activity | |

| [kind](careplan-definitions.html#CarePlan.activity.detail.kind) | | 0..1 | [code](datatypes.html#code) | Appointment | CommunicationRequest | DeviceRequest | MedicationRequest | NutritionOrder | Task | ServiceRequest | VisionPrescription
[Care Plan Activity Kind](valueset-care-plan-activity-kind.html) ([Required](terminologies.html#required)) | |

| [instantiatesCanonical](careplan-definitions.html#CarePlan.activity.detail.instantiatesCanonical) | | 0..* | [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html) | [ActivityDefinition](activitydefinition.html) | [Questionnaire](questionnaire.html) | [Measure](measure.html) | [OperationDefinition](operationdefinition.html)) | Instantiates FHIR protocol or definition
 | |

| [instantiatesUri](careplan-definitions.html#CarePlan.activity.detail.instantiatesUri) | | 0..* | [uri](datatypes.html#uri) | Instantiates external protocol or definition
 | |

| [code](careplan-definitions.html#CarePlan.activity.detail.code) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Detail type of activity
[Procedure Codes (SNOMED CT)](valueset-procedure-code.html) ([Example](terminologies.html#example)) | |

| [reasonCode](careplan-definitions.html#CarePlan.activity.detail.reasonCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Why activity should be done or why activity was prohibited
[SNOMED CT Clinical Findings](valueset-clinical-findings.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](careplan-definitions.html#CarePlan.activity.detail.reasonReference) | | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html)) | Why activity is needed
 | |

| [goal](careplan-definitions.html#CarePlan.activity.detail.goal) | | 0..* | [Reference](references.html#Reference)([Goal](goal.html)) | Goals this activity relates to
 | |

| [status](careplan-definitions.html#CarePlan.activity.detail.status) | [?!](conformance-rules.html#isModifier) | 1..1 | [code](datatypes.html#code) | not-started | scheduled | in-progress | on-hold | completed | cancelled | stopped | unknown | entered-in-error
[CarePlanActivityStatus](valueset-care-plan-activity-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](careplan-definitions.html#CarePlan.activity.detail.statusReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status | |

| [doNotPerform](careplan-definitions.html#CarePlan.activity.detail.doNotPerform) | [?!](conformance-rules.html#isModifier) | 0..1 | [boolean](datatypes.html#boolean) | If true, activity is prohibiting action | |

| [scheduled[x]](careplan-definitions.html#CarePlan.activity.detail.scheduled_x_) | | 0..1 | | When activity is to occur | |

| scheduledTiming | | | [Timing](datatypes.html#Timing) | | |

| scheduledPeriod | | | [Period](datatypes.html#Period) | | |

| scheduledString | | | [string](datatypes.html#string) | | |

| [location](careplan-definitions.html#CarePlan.activity.detail.location) | | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Where it should happen | |

| [performer](careplan-definitions.html#CarePlan.activity.detail.performer) | | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [CareTeam](careteam.html) | [HealthcareService](healthcareservice.html) | [Device](device.html)) | Who will be responsible?
 | |

| [product[x]](careplan-definitions.html#CarePlan.activity.detail.product_x_) | | 0..1 | | What is to be administered/supplied
[SNOMED CT Medication Codes](valueset-medication-codes.html) ([Example](terminologies.html#example)) | |

| productCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| productReference | | | [Reference](references.html#Reference)([Medication](medication.html) | [Substance](substance.html)) | | |

| [dailyAmount](careplan-definitions.html#CarePlan.activity.detail.dailyAmount) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | How to consume/day? | |

| [quantity](careplan-definitions.html#CarePlan.activity.detail.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | How much to administer/supply/consume | |

| [description](careplan-definitions.html#CarePlan.activity.detail.description) | | 0..1 | [string](datatypes.html#string) | Extra info describing activity to perform | |

| [note](careplan-definitions.html#CarePlan.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments about the plan
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - CarePlan ([DomainResource](domainresource.html))[Business identifiers assigned to this care plan by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](careplan-definitions.html#CarePlan.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlaninstantiatesCanonical](careplan-definitions.html#CarePlan.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..*] « [PlanDefinition](plandefinition.html#PlanDefinition)| [Questionnaire](questionnaire.html#Questionnaire)|[Measure](measure.html#Measure)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|[OperationDefinition](operationdefinition.html#OperationDefinition) »[The URL pointing to an externally maintained protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlaninstantiatesUri](careplan-definitions.html#CarePlan.instantiatesUri) : [uri](datatypes.html#uri) [0..*][A care plan that is fulfilled in whole or in part by this care planbasedOn](careplan-definitions.html#CarePlan.basedOn) : [Reference](references.html#Reference) [0..*] « [CarePlan](careplan.html#CarePlan) »[Completed or terminated care plan whose function is taken by this new care planreplaces](careplan-definitions.html#CarePlan.replaces) : [Reference](references.html#Reference) [0..*] « [CarePlan](careplan.html#CarePlan) »[A larger care plan of which this particular care plan is a component or steppartOf](careplan-definitions.html#CarePlan.partOf) : [Reference](references.html#Reference) [0..*] « [CarePlan](careplan.html#CarePlan) »[Indicates whether the plan is currently being acted upon, represents future intentions or is now a historical record (this element modifies the meaning of other elements)status](careplan-definitions.html#CarePlan.status) : [code](datatypes.html#code) [1..1] « [Indicates whether the plan is currently being acted upon, represents future intentions or is now a historical record. (Strength=Required)RequestStatus](valueset-request-status.html)! »[Indicates the level of authority/intentionality associated with the care plan and where the care plan fits into the workflow chain (this element modifies the meaning of other elements)intent](careplan-definitions.html#CarePlan.intent) : [code](datatypes.html#code) [1..1] « [Codes indicating the degree of authority/intentionality associated with a care plan. (Strength=Required)CarePlanIntent](valueset-care-plan-intent.html)! »[Identifies what "kind" of plan this is to support differentiation between multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma", "disease management", "wellness plan", etccategory](careplan-definitions.html#CarePlan.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Identifies what "kind" of plan this is to support differentiation between multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma", "disease management", etc. (Strength=Example)CarePlanCategory](valueset-care-plan-category.html)?? »[Human-friendly name for the care plantitle](careplan-definitions.html#CarePlan.title) : [string](datatypes.html#string) [0..1][A description of the scope and nature of the plandescription](careplan-definitions.html#CarePlan.description) : [string](datatypes.html#string) [0..1][Identifies the patient or group whose intended care is described by the plansubject](careplan-definitions.html#CarePlan.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this CarePlan was created or to which the creation of this record is tightly associatedencounter](careplan-definitions.html#CarePlan.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Indicates when the plan did (or is intended to) come into effect and endperiod](careplan-definitions.html#CarePlan.period) : [Period](datatypes.html#Period) [0..1][Represents when this particular CarePlan record was created in the system, which is often a system-generated datecreated](careplan-definitions.html#CarePlan.created) : [dateTime](datatypes.html#dateTime) [0..1][When populated, the author is responsible for the care plan. The care plan is attributed to the authorauthor](careplan-definitions.html#CarePlan.author) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam) »[Identifies the individual(s) or organization who provided the contents of the care plancontributor](careplan-definitions.html#CarePlan.contributor) : [Reference](references.html#Reference) [0..*] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam) »[Identifies all people and organizations who are expected to be involved in the care envisioned by this plancareTeam](careplan-definitions.html#CarePlan.careTeam) : [Reference](references.html#Reference) [0..*] « [CareTeam](careteam.html#CareTeam) »[Identifies the conditions/problems/concerns/diagnoses/etc. whose management and/or mitigation are handled by this planaddresses](careplan-definitions.html#CarePlan.addresses) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition) »[Identifies portions of the patient's record that specifically influenced the formation of the plan. These might include comorbidities, recent procedures, limitations, recent assessments, etcsupportingInfo](careplan-definitions.html#CarePlan.supportingInfo) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Describes the intended objective(s) of carrying out the care plangoal](careplan-definitions.html#CarePlan.goal) : [Reference](references.html#Reference) [0..*] « [Goal](goal.html#Goal) »[General notes about the care plan not covered elsewherenote](careplan-definitions.html#CarePlan.note) : [Annotation](datatypes.html#Annotation) [0..*]Activity[Identifies the outcome at the point when the status of the activity is assessed. For example, the outcome of an education activity could be patient understands (or not)outcomeCodeableConcept](careplan-definitions.html#CarePlan.activity.outcomeCodeableConcept) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Identifies the results of the activity. (Strength=Example)](valueset-care-plan-activity-outcome.html) [CarePlanActivityOutcome](valueset-care-plan-activity-outcome.html)?? »[Details of the outcome or action resulting from the activity. The reference to an "event" resource, such as Procedure or Encounter or Observation, is the result/outcome of the activity itself. The activity can be conveyed using CarePlan.activity.detail OR using the CarePlan.activity.reference (a reference to a “request” resource)outcomeReference](careplan-definitions.html#CarePlan.activity.outcomeReference) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Notes about the adherence/status/progress of the activityprogress](careplan-definitions.html#CarePlan.activity.progress) : [Annotation](datatypes.html#Annotation) [0..*][The details of the proposed activity represented in a specific resourcereference](careplan-definitions.html#CarePlan.activity.reference) : [Reference](references.html#Reference) [0..1] « [Appointment](appointment.html#Appointment)|[CommunicationRequest](communicationrequest.html#CommunicationRequest)| [DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[NutritionOrder](nutritionorder.html#NutritionOrder)|[Task](task.html#Task)| [ServiceRequest](servicerequest.html#ServiceRequest)|[VisionPrescription](visionprescription.html#VisionPrescription)|[RequestGroup](requestgroup.html#RequestGroup) »Detail[A description of the kind of resource the in-line definition of a care plan activity is representing. The CarePlan.activity.detail is an in-line definition when a resource is not referenced using CarePlan.activity.reference. For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequestkind](careplan-definitions.html#CarePlan.activity.detail.kind) : [code](datatypes.html#code) [0..1] « [Resource types defined as part of FHIR that can be represented as in-line definitions of a care plan activity. (Strength=Required)CarePlanActivityKind](valueset-care-plan-activity-kind.html)! »[The URL pointing to a FHIR-defined protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activityinstantiatesCanonical](careplan-definitions.html#CarePlan.activity.detail.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..*] « [PlanDefinition](plandefinition.html#PlanDefinition)| [ActivityDefinition](activitydefinition.html#ActivityDefinition)|[Questionnaire](questionnaire.html#Questionnaire)|[Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition) »[The URL pointing to an externally maintained protocol, guideline, questionnaire or other definition that is adhered to in whole or in part by this CarePlan activityinstantiatesUri](careplan-definitions.html#CarePlan.activity.detail.instantiatesUri) : [uri](datatypes.html#uri) [0..*][Detailed description of the type of planned activity; e.g. what lab test, what procedure, what kind of encountercode](careplan-definitions.html#CarePlan.activity.detail.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Detailed description of the type of activity; e.g. What lab test, what procedure, what kind of encounter. (Strength=Example)ProcedureCodes(SNOMEDCT)](valueset-procedure-code.html)?? »[Provides the rationale that drove the inclusion of this particular activity as part of the plan or the reason why the activity was prohibitedreasonCode](careplan-definitions.html#CarePlan.activity.detail.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Identifies why a care plan activity is needed. Can include any health condition codes as well as such concepts as "general wellness", prophylaxis, surgical preparation, etc. (Strength=Example)SNOMEDCTClinicalFindings](valueset-clinical-findings.html)?? »[Indicates another resource, such as the health condition(s), whose existence justifies this request and drove the inclusion of this particular activity as part of the planreasonReference](careplan-definitions.html#CarePlan.activity.detail.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)| [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference) »[Internal reference that identifies the goals that this activity is intended to contribute towards meetinggoal](careplan-definitions.html#CarePlan.activity.detail.goal) : [Reference](references.html#Reference) [0..*] « [Goal](goal.html#Goal) »[Identifies what progress is being made for the specific activity (this element modifies the meaning of other elements)status](careplan-definitions.html#CarePlan.activity.detail.status) : [code](datatypes.html#code) [1..1] « [Codes that reflect the current state of a care plan activity within its overall life cycle. (Strength=Required)CarePlanActivityStatus](valueset-care-plan-activity-status.html)! »[Provides reason why the activity isn't yet started, is on hold, was cancelled, etcstatusReason](careplan-definitions.html#CarePlan.activity.detail.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][If true, indicates that the described activity is one that must NOT be engaged in when following the plan. If false, or missing, indicates that the described activity is one that should be engaged in when following the plan (this element modifies the meaning of other elements)doNotPerform](careplan-definitions.html#CarePlan.activity.detail.doNotPerform) : [boolean](datatypes.html#boolean) [0..1][The period, timing or frequency upon which the described activity is to occurscheduled[x]](careplan-definitions.html#CarePlan.activity.detail.scheduled_x_) : [Type](formats.html#umlchoice) [0..1] « [Timing](datatypes.html#Timing)|[Period](datatypes.html#Period)|[string](datatypes.html#string) »[Identifies the facility where the activity will occur; e.g. home, hospital, specific clinic, etclocation](careplan-definitions.html#CarePlan.activity.detail.location) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location) »[Identifies who's expected to be involved in the activityperformer](careplan-definitions.html#CarePlan.activity.detail.performer) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)| [Device](device.html#Device) »[Identifies the food, drug or other product to be consumed or supplied in the activityproduct[x]](careplan-definitions.html#CarePlan.activity.detail.product_x_) : [Type](formats.html#umlchoice) [0..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Medication](medication.html#Medication)| [Substance](substance.html#Substance)); [A product supplied or administered as part of a care plan activity. (Strength=Example)SNOMEDCTMedicationCodes](valueset-medication-codes.html)?? »[Identifies the quantity expected to be consumed in a given daydailyAmount](careplan-definitions.html#CarePlan.activity.detail.dailyAmount) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][Identifies the quantity expected to be supplied, administered or consumed by the subjectquantity](careplan-definitions.html#CarePlan.activity.detail.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][This provides a textual description of constraints on the intended activity occurrence, including relation to other activities. It may also include objectives, pre-conditions and end-conditions. Finally, it may convey specifics about the activity such as body site, method, route, etcdescription](careplan-definitions.html#CarePlan.activity.detail.description) : [string](datatypes.html#string) [0..1]
[A simple summary of a planned activity suitable for a general care plan system (e.g. form driven) that doesn't know about specific resources such as procedure etcdetail](careplan-definitions.html#CarePlan.activity.detail)[0..1][Identifies a planned action to occur as part of the plan. For example, a medication to be used, lab tests to perform, self-monitoring, education, etcactivity](careplan-definitions.html#CarePlan.activity)[0..*]
 

 

 

**XML Template**

 

 
```
http://hl7.org/fhir/ValueSet/care-plan-activity-kind|4.0.1
```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**CarePlan**](careplan-definitions.html#CarePlan)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](careplan-definitions.html#CarePlan.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this plan](terminologies.html#unbound)
 "[instantiatesCanonical](careplan-definitions.html#CarePlan.instantiatesCanonical)" : [{ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[Questionnaire](questionnaire.html#Questionnaire)|[Measure](measure.html#Measure)|
 [ActivityDefinition](activitydefinition.html#ActivityDefinition)|[OperationDefinition](operationdefinition.html#OperationDefinition)) }], // [Instantiates FHIR protocol or definition](terminologies.html#unbound)
 "[instantiatesUri](careplan-definitions.html#CarePlan.instantiatesUri)" : ["<[uri](datatypes.html#uri)>"], // [Instantiates external protocol or definition](terminologies.html#unbound)
 "[basedOn](careplan-definitions.html#CarePlan.basedOn)" : [{ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)) }], // [Fulfills CarePlan](terminologies.html#unbound)
 "[replaces](careplan-definitions.html#CarePlan.replaces)" : [{ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)) }], // [CarePlan replaced by this CarePlan](terminologies.html#unbound)
 "[partOf](careplan-definitions.html#CarePlan.partOf)" : [{ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)) }], // [Part of referenced CarePlan](terminologies.html#unbound)
 "[status](careplan-definitions.html#CarePlan.status)" : "<[code](datatypes.html#code)>", // **R!** [draft | active | on-hold | revoked | completed | entered-in-error | unknown](valueset-request-status.html)
 "[intent](careplan-definitions.html#CarePlan.intent)" : "<[code](datatypes.html#code)>", // **R!** [proposal | plan | order | option](valueset-care-plan-intent.html)
 "[category](careplan-definitions.html#CarePlan.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Type of plan](valueset-care-plan-category.html)
 "[title](careplan-definitions.html#CarePlan.title)" : "<[string](datatypes.html#string)>", // [Human-friendly name for the care plan](terminologies.html#unbound)
 "[description](careplan-definitions.html#CarePlan.description)" : "<[string](datatypes.html#string)>", // [Summary of nature of plan](terminologies.html#unbound)
 "[subject](careplan-definitions.html#CarePlan.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Who the care plan is for](terminologies.html#unbound)
 "[encounter](careplan-definitions.html#CarePlan.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[period](careplan-definitions.html#CarePlan.period)" : { [Period](datatypes.html#Period) }, // [Time period plan covers](terminologies.html#unbound)
 "[created](careplan-definitions.html#CarePlan.created)" : "<[dateTime](datatypes.html#dateTime)>", // [Date record was first recorded](terminologies.html#unbound)
 "[author](careplan-definitions.html#CarePlan.author)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) }, // [Who is the designated responsible party](terminologies.html#unbound)
 "[contributor](careplan-definitions.html#CarePlan.contributor)" : [{ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) }], // [Who provided the content of the care plan](terminologies.html#unbound)
 "[careTeam](careplan-definitions.html#CarePlan.careTeam)" : [{ [Reference](references.html#Reference)([CareTeam](careteam.html#CareTeam)) }], // [Who's involved in plan?](terminologies.html#unbound)
 "[addresses](careplan-definitions.html#CarePlan.addresses)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)) }], // [Health issues this plan addresses](terminologies.html#unbound)
 "[supportingInfo](careplan-definitions.html#CarePlan.supportingInfo)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Information considered as part of plan](terminologies.html#unbound)
 "[goal](careplan-definitions.html#CarePlan.goal)" : [{ [Reference](references.html#Reference)([Goal](goal.html#Goal)) }], // [Desired outcome of plan](terminologies.html#unbound)
 "[activity](careplan-definitions.html#CarePlan.activity)" : [{ // [Action to occur as part of plan](terminologies.html#unbound)
 "[outcomeCodeableConcept](careplan-definitions.html#CarePlan.activity.outcomeCodeableConcept)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Results of the activity](valueset-care-plan-activity-outcome.html)
 "[outcomeReference](careplan-definitions.html#CarePlan.activity.outcomeReference)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Appointment, Encounter, Procedure, etc.](terminologies.html#unbound)
 "[progress](careplan-definitions.html#CarePlan.activity.progress)" : [{ [Annotation](datatypes.html#Annotation) }], // [Comments about the activity status/progress](terminologies.html#unbound)
 "[reference](careplan-definitions.html#CarePlan.activity.reference)" : { [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)|[CommunicationRequest](communicationrequest.html#CommunicationRequest)|[DeviceRequest](devicerequest.html#DeviceRequest)|
 [MedicationRequest](medicationrequest.html#MedicationRequest)|[NutritionOrder](nutritionorder.html#NutritionOrder)|[Task](task.html#Task)|[ServiceRequest](servicerequest.html#ServiceRequest)|[VisionPrescription](visionprescription.html#VisionPrescription)|
 [RequestGroup](requestgroup.html#RequestGroup)) }, // **C?** [Activity details defined in specific resource](terminologies.html#unbound)
 "[detail](careplan-definitions.html#CarePlan.activity.detail)" : { // **C?** [In-line definition of activity](terminologies.html#unbound)
 "[kind](careplan-definitions.html#CarePlan.activity.detail.kind)" : "<[code](datatypes.html#code)>", // [Appointment | CommunicationRequest | DeviceRequest | MedicationRequest | NutritionOrder | Task | ServiceRequest | VisionPrescription](valueset-care-plan-activity-kind.html)
 "[instantiatesCanonical](careplan-definitions.html#CarePlan.activity.detail.instantiatesCanonical)" : [{ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|
 [Questionnaire](questionnaire.html#Questionnaire)|[Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)) }], // [Instantiates FHIR protocol or definition](terminologies.html#unbound)
 "[instantiatesUri](careplan-definitions.html#CarePlan.activity.detail.instantiatesUri)" : ["<[uri](datatypes.html#uri)>"], // [Instantiates external protocol or definition](terminologies.html#unbound)
 "[code](careplan-definitions.html#CarePlan.activity.detail.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Detail type of activity](valueset-procedure-code.html)
 "[reasonCode](careplan-definitions.html#CarePlan.activity.detail.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Why activity should be done or why activity was prohibited](valueset-clinical-findings.html)
 "[reasonReference](careplan-definitions.html#CarePlan.activity.detail.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) }], // [Why activity is needed](terminologies.html#unbound)
 "[goal](careplan-definitions.html#CarePlan.activity.detail.goal)" : [{ [Reference](references.html#Reference)([Goal](goal.html#Goal)) }], // [Goals this activity relates to](terminologies.html#unbound)
 "[status](careplan-definitions.html#CarePlan.activity.detail.status)" : "<[code](datatypes.html#code)>", // **R!** [not-started | scheduled | in-progress | on-hold | completed | cancelled | stopped | unknown | entered-in-error](valueset-care-plan-activity-status.html)
 "[statusReason](careplan-definitions.html#CarePlan.activity.detail.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](terminologies.html#unbound)
 "[doNotPerform](careplan-definitions.html#CarePlan.activity.detail.doNotPerform)" : <[boolean](datatypes.html#boolean)>, // [If true, activity is prohibiting action](terminologies.html#unbound)
 // scheduled[x]: When activity is to occur. One of these 3:
 "[scheduledTiming](careplan-definitions.html#CarePlan.activity.detail.scheduledTiming)" : { [Timing](datatypes.html#Timing) },
 "[scheduledPeriod](careplan-definitions.html#CarePlan.activity.detail.scheduledPeriod)" : { [Period](datatypes.html#Period) },
 "[scheduledString](careplan-definitions.html#CarePlan.activity.detail.scheduledString)" : "<[string](datatypes.html#string)>",
 "[location](careplan-definitions.html#CarePlan.activity.detail.location)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // [Where it should happen](terminologies.html#unbound)
 "[performer](careplan-definitions.html#CarePlan.activity.detail.performer)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)|[Device](device.html#Device)) }], // [Who will be responsible?](terminologies.html#unbound)
 // product[x]: What is to be administered/supplied. One of these 2:
 "[productCodeableConcept](careplan-definitions.html#CarePlan.activity.detail.productCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[productReference](careplan-definitions.html#CarePlan.activity.detail.productReference)" : { [Reference](references.html#Reference)([Medication](medication.html#Medication)|[Substance](substance.html#Substance)) },
 "[dailyAmount](careplan-definitions.html#CarePlan.activity.detail.dailyAmount)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [How to consume/day?](terminologies.html#unbound)
 "[quantity](careplan-definitions.html#CarePlan.activity.detail.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [How much to administer/supply/consume](terminologies.html#unbound)
 "[description](careplan-definitions.html#CarePlan.activity.detail.description)" : "<[string](datatypes.html#string)>" // [Extra info describing activity to perform](terminologies.html#unbound)
 }
 }],
 "[note](careplan-definitions.html#CarePlan.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments about the plan](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**CarePlan**](careplan-definitions.html#CarePlan);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[CarePlan.identifier](careplan-definitions.html#CarePlan.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this plan
 fhir:[CarePlan.instantiatesCanonical](careplan-definitions.html#CarePlan.instantiatesCanonical) [ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[Questionnaire](questionnaire.html#Questionnaire)|[Measure](measure.html#Measure)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|[OperationDefinition](operationdefinition.html#OperationDefinition)) ], ... ; # 0..* Instantiates FHIR protocol or definition
 fhir:[CarePlan.instantiatesUri](careplan-definitions.html#CarePlan.instantiatesUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Instantiates external protocol or definition
 fhir:[CarePlan.basedOn](careplan-definitions.html#CarePlan.basedOn) [ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)) ], ... ; # 0..* Fulfills CarePlan
 fhir:[CarePlan.replaces](careplan-definitions.html#CarePlan.replaces) [ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)) ], ... ; # 0..* CarePlan replaced by this CarePlan
 fhir:[CarePlan.partOf](careplan-definitions.html#CarePlan.partOf) [ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)) ], ... ; # 0..* Part of referenced CarePlan
 fhir:[CarePlan.status](careplan-definitions.html#CarePlan.status) [ [code](datatypes.html#code) ]; # 1..1 draft | active | on-hold | revoked | completed | entered-in-error | unknown
 fhir:[CarePlan.intent](careplan-definitions.html#CarePlan.intent) [ [code](datatypes.html#code) ]; # 1..1 proposal | plan | order | option
 fhir:[CarePlan.category](careplan-definitions.html#CarePlan.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Type of plan
 fhir:[CarePlan.title](careplan-definitions.html#CarePlan.title) [ [string](datatypes.html#string) ]; # 0..1 Human-friendly name for the care plan
 fhir:[CarePlan.description](careplan-definitions.html#CarePlan.description) [ [string](datatypes.html#string) ]; # 0..1 Summary of nature of plan
 fhir:[CarePlan.subject](careplan-definitions.html#CarePlan.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Who the care plan is for
 fhir:[CarePlan.encounter](careplan-definitions.html#CarePlan.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[CarePlan.period](careplan-definitions.html#CarePlan.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time period plan covers
 fhir:[CarePlan.created](careplan-definitions.html#CarePlan.created) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Date record was first recorded
 fhir:[CarePlan.author](careplan-definitions.html#CarePlan.author) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) ]; # 0..1 Who is the designated responsible party
 fhir:[CarePlan.contributor](careplan-definitions.html#CarePlan.contributor) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) ], ... ; # 0..* Who provided the content of the care plan
 fhir:[CarePlan.careTeam](careplan-definitions.html#CarePlan.careTeam) [ [Reference](references.html#Reference)([CareTeam](careteam.html#CareTeam)) ], ... ; # 0..* Who's involved in plan?
 fhir:[CarePlan.addresses](careplan-definitions.html#CarePlan.addresses) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)) ], ... ; # 0..* Health issues this plan addresses
 fhir:[CarePlan.supportingInfo](careplan-definitions.html#CarePlan.supportingInfo) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Information considered as part of plan
 fhir:[CarePlan.goal](careplan-definitions.html#CarePlan.goal) [ [Reference](references.html#Reference)([Goal](goal.html#Goal)) ], ... ; # 0..* Desired outcome of plan
 fhir:[CarePlan.activity](careplan-definitions.html#CarePlan.activity) [ # 0..* Action to occur as part of plan
 fhir:[CarePlan.activity.outcomeCodeableConcept](careplan-definitions.html#CarePlan.activity.outcomeCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Results of the activity
 fhir:[CarePlan.activity.outcomeReference](careplan-definitions.html#CarePlan.activity.outcomeReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Appointment, Encounter, Procedure, etc.
 fhir:[CarePlan.activity.progress](careplan-definitions.html#CarePlan.activity.progress) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments about the activity status/progress
 fhir:[CarePlan.activity.reference](careplan-definitions.html#CarePlan.activity.reference) [ [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)|[CommunicationRequest](communicationrequest.html#CommunicationRequest)|[DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[NutritionOrder](nutritionorder.html#NutritionOrder)|
 [Task](task.html#Task)|[ServiceRequest](servicerequest.html#ServiceRequest)|[VisionPrescription](visionprescription.html#VisionPrescription)|[RequestGroup](requestgroup.html#RequestGroup)) ]; # 0..1 Activity details defined in specific resource
 fhir:[CarePlan.activity.detail](careplan-definitions.html#CarePlan.activity.detail) [ # 0..1 In-line definition of activity
 fhir:[CarePlan.activity.detail.kind](careplan-definitions.html#CarePlan.activity.detail.kind) [ [code](datatypes.html#code) ]; # 0..1 Appointment | CommunicationRequest | DeviceRequest | MedicationRequest | NutritionOrder | Task | ServiceRequest | VisionPrescription
 fhir:[CarePlan.activity.detail.instantiatesCanonical](careplan-definitions.html#CarePlan.activity.detail.instantiatesCanonical) [ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|[Questionnaire](questionnaire.html#Questionnaire)|[Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)) ], ... ; # 0..* Instantiates FHIR protocol or definition
 fhir:[CarePlan.activity.detail.instantiatesUri](careplan-definitions.html#CarePlan.activity.detail.instantiatesUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Instantiates external protocol or definition
 fhir:[CarePlan.activity.detail.code](careplan-definitions.html#CarePlan.activity.detail.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Detail type of activity
 fhir:[CarePlan.activity.detail.reasonCode](careplan-definitions.html#CarePlan.activity.detail.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Why activity should be done or why activity was prohibited
 fhir:[CarePlan.activity.detail.reasonReference](careplan-definitions.html#CarePlan.activity.detail.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference)) ], ... ; # 0..* Why activity is needed
 fhir:[CarePlan.activity.detail.goal](careplan-definitions.html#CarePlan.activity.detail.goal) [ [Reference](references.html#Reference)([Goal](goal.html#Goal)) ], ... ; # 0..* Goals this activity relates to
 fhir:[CarePlan.activity.detail.status](careplan-definitions.html#CarePlan.activity.detail.status) [ [code](datatypes.html#code) ]; # 1..1 not-started | scheduled | in-progress | on-hold | completed | cancelled | stopped | unknown | entered-in-error
 fhir:[CarePlan.activity.detail.statusReason](careplan-definitions.html#CarePlan.activity.detail.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[CarePlan.activity.detail.doNotPerform](careplan-definitions.html#CarePlan.activity.detail.doNotPerform) [ [boolean](datatypes.html#boolean) ]; # 0..1 If true, activity is prohibiting action
 # [CarePlan.activity.detail.scheduled[x]](careplan-definitions.html#CarePlan.activity.detail.scheduled[x]) : 0..1 When activity is to occur. One of these 3
 fhir:[CarePlan.activity.detail.scheduledTiming](careplan-definitions.html#CarePlan.activity.detail.scheduledTiming) [ [Timing](datatypes.html#Timing) ]
 fhir:[CarePlan.activity.detail.scheduledPeriod](careplan-definitions.html#CarePlan.activity.detail.scheduledPeriod) [ [Period](datatypes.html#Period) ]
 fhir:[CarePlan.activity.detail.scheduledString](careplan-definitions.html#CarePlan.activity.detail.scheduledString) [ [string](datatypes.html#string) ]
 fhir:[CarePlan.activity.detail.location](careplan-definitions.html#CarePlan.activity.detail.location) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 0..1 Where it should happen
 fhir:[CarePlan.activity.detail.performer](careplan-definitions.html#CarePlan.activity.detail.performer) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[CareTeam](careteam.html#CareTeam)|
 [HealthcareService](healthcareservice.html#HealthcareService)|[Device](device.html#Device)) ], ... ; # 0..* Who will be responsible?
 # [CarePlan.activity.detail.product[x]](careplan-definitions.html#CarePlan.activity.detail.product[x]) : 0..1 What is to be administered/supplied. One of these 2
 fhir:[CarePlan.activity.detail.productCodeableConcept](careplan-definitions.html#CarePlan.activity.detail.productCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[CarePlan.activity.detail.productReference](careplan-definitions.html#CarePlan.activity.detail.productReference) [ [Reference](references.html#Reference)([Medication](medication.html#Medication)|[Substance](substance.html#Substance)) ]
 fhir:[CarePlan.activity.detail.dailyAmount](careplan-definitions.html#CarePlan.activity.detail.dailyAmount) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 How to consume/day?
 fhir:[CarePlan.activity.detail.quantity](careplan-definitions.html#CarePlan.activity.detail.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 How much to administer/supply/consume
 fhir:[CarePlan.activity.detail.description](careplan-definitions.html#CarePlan.activity.detail.description) [ [string](datatypes.html#string) ]; # 0..1 Extra info describing activity to perform
 ];
 ], ...;
 fhir:[CarePlan.note](careplan-definitions.html#CarePlan.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments about the plan
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [CarePlan](careplan.html#CarePlan)
 | 
 | 
 |

 | 
 CarePlan.instantiatesCanonical | 
 
 

 Added Element

 

 | 
 |

 | 
 CarePlan.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 CarePlan.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/care-plan-status to http://hl7.org/fhir/ValueSet/request-status|4.0.1

 

 | 
 |

 | 
 CarePlan.intent | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/care-plan-intent to http://hl7.org/fhir/ValueSet/care-plan-intent|4.0.1

 

 | 
 |

 | 
 CarePlan.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 CarePlan.created | 
 
 

 - Added Element

 

 | 
 |

 | 
 CarePlan.author | 
 
 

 - Max Cardinality changed from * to 1

 - Type Reference: Added Target Types PractitionerRole, Device

 

 | 
 |

 | 
 CarePlan.contributor | 
 
 

 - Added Element

 

 | 
 |

 | 
 CarePlan.activity.reference | 
 
 

 - Type Reference: Added Target Type ServiceRequest

 - Type Reference: Removed Target Types ProcedureRequest, ReferralRequest

 

 | 
 |

 | 
 CarePlan.activity.detail.kind | 
 
 

 - Renamed from category to kind

 - Type changed from CodeableConcept to code

 - 
Add Binding `http://hl7.org/fhir/ValueSet/care-plan-activity-kind|4.0.1` (required)
 

 

 | 
 |

 | 
 CarePlan.activity.detail.instantiatesCanonical | 
 
 

 - Added Element

 

 | 
 |

 | 
 CarePlan.activity.detail.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 CarePlan.activity.detail.reasonReference | 
 
 

 - Type Reference: Added Target Types Observation, DiagnosticReport, DocumentReference

 

 | 
 |

 | 
 CarePlan.activity.detail.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/care-plan-activity-status to http://hl7.org/fhir/ValueSet/care-plan-activity-status|4.0.1

 

 | 
 |

 | 
 CarePlan.activity.detail.statusReason | 
 
 

 - Type changed from string to CodeableConcept

 

 | 
 |

 | 
 CarePlan.activity.detail.doNotPerform | 
 
 

 - Renamed from prohibited to doNotPerform

 - Default Value "false" removed

 

 | 
 |

 | 
 CarePlan.activity.detail.performer | 
 
 

 - Type Reference: Added Target Types PractitionerRole, HealthcareService, Device

 

 | 
 |

 | 
 CarePlan.definition | 
 
 

 - deleted

 

 | 
 |

 | 
 CarePlan.context | 
 
 

 - deleted

 

 | 
 |

 | 
 CarePlan.activity.detail.definition | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](careplan.diff.xml) or [JSON](careplan.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](careplan-version-maps.html) (status = 11 tests that all execute ok. All tests pass round-trip testing and 10 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](careplan-profiles.html) and the alternate definitions:
Master Definition [XML](careplan.profile.xml.html) + [JSON](careplan.profile.json.html),
[XML](xml.html) [Schema](careplan.xsd)/[Schematron](careplan.sch) + [JSON](json.html) 
[Schema](careplan.schema.json.html), [ShEx](careplan.shex.html) (for [Turtle](rdf.html)) + [see the extensions](careplan-profiles.html) & the [dependency analysis](careplan-dependencies.html)

### 9.5.3.1 
Terminology Bindings
 [
](careplan.html#tx)

 | Path | Definition | Type | Reference | |

 | CarePlan.status | Indicates whether the plan is currently being acted upon, represents future intentions or is now a historical record. | [Required](terminologies.html#required) | [RequestStatus](valueset-request-status.html) | |

 | CarePlan.intent | Codes indicating the degree of authority/intentionality associated with a care plan. | [Required](terminologies.html#required) | [CarePlanIntent](valueset-care-plan-intent.html) | |

 | CarePlan.category | Identifies what "kind" of plan this is to support differentiation between multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma", "disease management", etc. | [Example](terminologies.html#example) | [CarePlanCategory](valueset-care-plan-category.html) | |

 | CarePlan.activity.outcomeCodeableConcept | Identifies the results of the activity. | [Example](terminologies.html#example) | [CarePlanActivityOutcome](valueset-care-plan-activity-outcome.html) | |

 | CarePlan.activity.detail.kind | Resource types defined as part of FHIR that can be represented as in-line definitions of a care plan activity. | [Required](terminologies.html#required) | [CarePlanActivityKind](valueset-care-plan-activity-kind.html) | |

 | CarePlan.activity.detail.code | Detailed description of the type of activity; e.g. What lab test, what procedure, what kind of encounter. | [Example](terminologies.html#example) | [ProcedureCodes(SNOMEDCT)](valueset-procedure-code.html) | |

 | CarePlan.activity.detail.reasonCode | Identifies why a care plan activity is needed. Can include any health condition codes as well as such concepts as "general wellness", prophylaxis, surgical preparation, etc. | [Example](terminologies.html#example) | [SNOMEDCTClinicalFindings](valueset-clinical-findings.html) | |

 | CarePlan.activity.detail.status | Codes that reflect the current state of a care plan activity within its overall life cycle. | [Required](terminologies.html#required) | [CarePlanActivityStatus](valueset-care-plan-activity-status.html) | |

 | CarePlan.activity.detail.product[x] | A product supplied or administered as part of a care plan activity. | [Example](terminologies.html#example) | [SNOMEDCTMedicationCodes](valueset-medication-codes.html) | |

 

 

### 9.5.3.2 Constraints [
](careplan.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **cpl-3** | [Rule](conformance-rules.html#rule) | CarePlan.activity | Provide a reference or detail, not both | detail.empty() or reference.empty() | |

### 9.5.3.3 Notes [](careplan.html#9.5.3.3)

The [Provenance](provenance.html) resource can be used for detailed review information, such as when the care plan was last reviewed and by whom. 

## 9.5.4 Open Issues [
](careplan.html#open)

 

## 9.5.5 Search Parameters [](careplan.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| activity-code | [token](search.html#token) | Detail type of activity | CarePlan.activity.detail.code | | |

| activity-date | [date](search.html#date) | Specified date occurs within period specified by CarePlan.activity.detail.scheduled[x] | CarePlan.activity.detail.scheduled | | |

| activity-reference | [reference](search.html#reference) | Activity details defined in specific resource | CarePlan.activity.reference
([Appointment](appointment.html), [MedicationRequest](medicationrequest.html), [Task](task.html), [NutritionOrder](nutritionorder.html), [RequestGroup](requestgroup.html), [VisionPrescription](visionprescription.html), [DeviceRequest](devicerequest.html), [ServiceRequest](servicerequest.html), [CommunicationRequest](communicationrequest.html)) | | |

| based-on | [reference](search.html#reference) | Fulfills CarePlan | CarePlan.basedOn
([CarePlan](careplan.html)) | | |

| care-team | [reference](search.html#reference) | Who's involved in plan? | CarePlan.careTeam
([CareTeam](careteam.html)) | | |

| category | [token](search.html#token) | Type of plan | CarePlan.category | | |

| condition | [reference](search.html#reference) | Health issues this plan addresses | CarePlan.addresses
([Condition](condition.html)) | | |

| date | [date](search.html#date) | Time period plan covers | CarePlan.period | [17 Resources](searchparameter-registry.html#clinical-date) | |

| encounter | [reference](search.html#reference) | Encounter created as part of | CarePlan.encounter
([Encounter](encounter.html)) | | |

| goal | [reference](search.html#reference) | Desired outcome of plan | CarePlan.goal
([Goal](goal.html)) | | |

| identifier | [token](search.html#token) | External Ids for this plan | CarePlan.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| instantiates-canonical | [reference](search.html#reference) | Instantiates FHIR protocol or definition | CarePlan.instantiatesCanonical
([Questionnaire](questionnaire.html), [Measure](measure.html), [PlanDefinition](plandefinition.html), [OperationDefinition](operationdefinition.html), [ActivityDefinition](activitydefinition.html)) | | |

| instantiates-uri | [uri](search.html#uri) | Instantiates external protocol or definition | CarePlan.instantiatesUri | | |

| intent | [token](search.html#token) | proposal | plan | order | option | CarePlan.intent | | |

| part-of | [reference](search.html#reference) | Part of referenced CarePlan | CarePlan.partOf
([CarePlan](careplan.html)) | | |

| patient | [reference](search.html#reference) | Who the care plan is for | CarePlan.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| performer | [reference](search.html#reference) | Matches if the practitioner is listed as a performer in any of the "simple" activities. (For performers of the detailed activities, chain through the activitydetail search parameter.) | CarePlan.activity.detail.performer
([Practitioner](practitioner.html), [Organization](organization.html), [CareTeam](careteam.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| replaces | [reference](search.html#reference) | CarePlan replaced by this CarePlan | CarePlan.replaces
([CarePlan](careplan.html)) | | |

| status | [token](search.html#token) | draft | active | on-hold | revoked | completed | entered-in-error | unknown | CarePlan.status | | |

| subject | [reference](search.html#reference) | Who the care plan is for | CarePlan.subject
([Group](group.html), [Patient](patient.html)) | | |