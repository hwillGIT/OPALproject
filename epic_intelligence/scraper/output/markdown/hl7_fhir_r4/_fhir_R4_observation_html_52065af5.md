# Observation - FHIR v4.0.1A unique identifier assigned to this observationA plan, proposal or order that is fulfilled in whole or in part by this event.  For example, a MedicationRequest may require a patient to have laboratory test performed before  it is dispensedA larger event of which this particular Observation is a component or step.  For example,  an observation as part of a procedureThe status of the result value (this element modifies the meaning of other elements)Codes providing the status of an observation. (Strength=Required)A code that classifies the general type of observation being madeCodes for high level observation categories. (Strength=Preferred)Describes what was observed. Sometimes this is called the observation "name"Codes identifying names of simple observations. (Strength=Example)The patient, or group of patients, location, or device this observation is about and into whose record the observation is placed. If the actual focus of the observation is different from the subject (or a sample of, part, or region of the subject), the `focus` element or the `code` itself specifies the actual focus of the observationThe actual focus of an observation when it is not the patient of record representing something or someone associated with the patient such as a spouse, parent, fetus, or donor. For example, fetus observations in a mother's record.  The focus of an observation could also be an existing condition,  an intervention, the subject's diet,  another observation of the subject,  or a body structure such as tumor or implanted device.   An example use case would be using the Observation resource to capture whether the mother is trained to change her child's tracheostomy tube. In this example, the child is the patient of record and the mother is the focusThe healthcare event  (e.g. a patient and healthcare provider interaction) during which this observation is madeThe time or time-period the observed value is asserted as being true. For biological subjects - e.g. human patients - this is usually called the "physiologically relevant time". This is usually either the time of the procedure or of specimen collection, but very often the source of the date/time is not known, only the date/time itselfThe date and time this version of the observation was made available to providers, typically after the results have been reviewed and verifiedWho was responsible for asserting the observed value as "true"The information determined as a result of making the observation, if the information has a simple valueProvides a reason why the expected value in the element Observation.value[x] is missingCodes specifying why the result (`Observation.value[x]`) is missing. (Strength=Extensible)A categorical assessment of an observation value.  For example, high, low, normalCodes identifying interpretations of observations. (Strength=Extensible)Comments about the observation or the resultsIndicates the site on the subject's body where the observation was made (i.e. the target site)Codes describing anatomical locations. May include laterality. (Strength=Example)Indicates the mechanism used to perform the observationMethods for simple observations. (Strength=Example)The specimen that was used when this observation was madeThe device used to generate the observation dataThis observation is a group observation (e.g. a battery, a panel of tests, a set of vital sign measurements) that includes the target as a member of the groupThe target resource that represents a measurement from which this observation value is derived. For example, a calculated anion gap or a fetal measurement based on an ultrasound imageThe value of the low bound of the reference range.  The low bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless (e.g. reference range is <=2.3)The value of the high bound of the reference range.  The high bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless (e.g. reference range is >= 2.3)Codes to indicate the what part of the targeted reference population it applies to. For example, the normal or therapeutic rangeCode for the meaning of a reference range. (Strength=Preferred)Codes to indicate the target population this reference range applies to.  For example, a reference range may be based on the normal population or a particular sex or race.  Multiple `appliesTo`  are interpreted as an "AND" of the target populations.  For example, to represent a target population of African American females, both a code of female and a code for African American would be usedCodes identifying the population the reference range applies to. (Strength=Example)The age at which this reference range is applicable. This is a neonatal age (e.g. number of weeks at term) if the meaning says soText based reference range in an observation which may be used when a quantitative range is not appropriate for an observation.  An example would be a reference value of "Negative" or a list or table of "normals"Describes what was observed. Sometimes this is called the observation "code"Codes identifying names of simple observations. (Strength=Example)The information determined as a result of making the observation, if the information has a simple valueProvides a reason why the expected value in the element Observation.component.value[x] is missingCodes specifying why the result (`Observation.value[x]`) is missing. (Strength=Extensible)A categorical assessment of an observation value.  For example, high, low, normalCodes identifying interpretations of observations. (Strength=Extensible)Guidance on how to interpret the value by comparison to a normal or recommended range.  Multiple reference ranges are interpreted as an "OR".   In other words, to represent two distinct target populations, two `referenceRange` elements would be usedGuidance on how to interpret the value by comparison to a normal or recommended rangeSome observations have multiple component observations.  These component observations are expressed as separate code value pairs that share the same attributes.  Examples include systolic and diastolic component observations for blood pressure measurement and multiple component observations for genetics observationsA unique identifier assigned to this observationA plan, proposal or order that is fulfilled in whole or in part by this event.  For example, a MedicationRequest may require a patient to have laboratory test performed before  it is dispensedA larger event of which this particular Observation is a component or step.  For example,  an observation as part of a procedureThe status of the result value (this element modifies the meaning of other elements)Codes providing the status of an observation. (Strength=Required)A code that classifies the general type of observation being madeCodes for high level observation categories. (Strength=Preferred)Describes what was observed. Sometimes this is called the observation "name"Codes identifying names of simple observations. (Strength=Example)The patient, or group of patients, location, or device this observation is about and into whose record the observation is placed. If the actual focus of the observation is different from the subject (or a sample of, part, or region of the subject), the `focus` element or the `code` itself specifies the actual focus of the observationThe actual focus of an observation when it is not the patient of record representing something or someone associated with the patient such as a spouse, parent, fetus, or donor. For example, fetus observations in a mother's record.  The focus of an observation could also be an existing condition,  an intervention, the subject's diet,  another observation of the subject,  or a body structure such as tumor or implanted device.   An example use case would be using the Observation resource to capture whether the mother is trained to change her child's tracheostomy tube. In this example, the child is the patient of record and the mother is the focusThe healthcare event  (e.g. a patient and healthcare provider interaction) during which this observation is madeThe time or time-period the observed value is asserted as being true. For biological subjects - e.g. human patients - this is usually called the "physiologically relevant time". This is usually either the time of the procedure or of specimen collection, but very often the source of the date/time is not known, only the date/time itselfThe date and time this version of the observation was made available to providers, typically after the results have been reviewed and verifiedWho was responsible for asserting the observed value as "true"The information determined as a result of making the observation, if the information has a simple valueProvides a reason why the expected value in the element Observation.value[x] is missingCodes specifying why the result (`Observation.value[x]`) is missing. (Strength=Extensible)A categorical assessment of an observation value.  For example, high, low, normalCodes identifying interpretations of observations. (Strength=Extensible)Comments about the observation or the resultsIndicates the site on the subject's body where the observation was made (i.e. the target site)Codes describing anatomical locations. May include laterality. (Strength=Example)Indicates the mechanism used to perform the observationMethods for simple observations. (Strength=Example)The specimen that was used when this observation was madeThe device used to generate the observation dataThis observation is a group observation (e.g. a battery, a panel of tests, a set of vital sign measurements) that includes the target as a member of the groupThe target resource that represents a measurement from which this observation value is derived. For example, a calculated anion gap or a fetal measurement based on an ultrasound imageThe value of the low bound of the reference range.  The low bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless (e.g. reference range is <=2.3)The value of the high bound of the reference range.  The high bound of the reference range endpoint is inclusive of the value (e.g.  reference range is >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless (e.g. reference range is >= 2.3)Codes to indicate the what part of the targeted reference population it applies to. For example, the normal or therapeutic rangeCode for the meaning of a reference range. (Strength=Preferred)Codes to indicate the target population this reference range applies to.  For example, a reference range may be based on the normal population or a particular sex or race.  Multiple `appliesTo`  are interpreted as an "AND" of the target populations.  For example, to represent a target population of African American females, both a code of female and a code for African American would be usedCodes identifying the population the reference range applies to. (Strength=Example)The age at which this reference range is applicable. This is a neonatal age (e.g. number of weeks at term) if the meaning says soText based reference range in an observation which may be used when a quantitative range is not appropriate for an observation.  An example would be a reference value of "Negative" or a list or table of "normals"Describes what was observed. Sometimes this is called the observation "code"Codes identifying names of simple observations. (Strength=Example)The information determined as a result of making the observation, if the information has a simple valueProvides a reason why the expected value in the element Observation.component.value[x] is missingCodes specifying why the result (`Observation.value[x]`) is missing. (Strength=Extensible)A categorical assessment of an observation value.  For example, high, low, normalCodes identifying interpretations of observations. (Strength=Extensible)Guidance on how to interpret the value by comparison to a normal or recommended range.  Multiple reference ranges are interpreted as an "OR".   In other words, to represent two distinct target populations, two `referenceRange` elements would be usedGuidance on how to interpret the value by comparison to a normal or recommended rangeSome observations have multiple component observations.  These component observations are expressed as separate code value pairs that share the same attributes.  Examples include systolic and diastolic component observations for blood pressure measurement and multiple component observations for genetics observations

> Source: https://hl7.org/fhir/R4/observation.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/observation.html) [R4B](http://hl7.org/fhir/R4B/observation.html) **R4** [R3](http://hl7.org/fhir/STU3/observation.html) [R2](http://hl7.org/fhir/DSTU2/observation.html)
 

# 10.1 Resource Observation - Content [
](observation.html#10.1)

| [Orders and Observations ](http://www.hl7.org/Special/committees/orders/index.cfm) Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) | [Normative](versions.html#std-process) (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

 | 
 
 
 | 
 
 This page has been approved as part of an [ANSI ](https://www.ansi.org/) standard.
 See the [Observation](ansi-observation.html) Package for further details.
 | 
 |

Measurements and simple assertions made about a patient, device or other subject.

 
## 10.1.1 Scope and Usage [
](observation.html#10.1.1)

 This resource is an [
 *event resource*
 ](workflow.html#event) from a FHIR workflow perspective - see [Workflow](workflow.html).

 
Observations are a central element in healthcare, used to support diagnosis, monitor progress, determine baselines and patterns and even capture demographic characteristics. Most observations are simple name/value pair assertions with some metadata, but some observations group other observations together logically, or even are multi-component observations. Note that the [DiagnosticReport](diagnosticreport.html) resource provides a clinical or workflow context for a set of observations and the Observation resource is referenced by DiagnosticReport to represent laboratory, imaging, and other clinical and diagnostic data to form a complete report. 

 
Uses for the Observation resource include:

 

 - Vital signs such as [body weight](observation-example.html), [blood pressure](observation-example-bloodpressure.html), and [temperature](observation-example-f202-temperature.html)
 

 - Laboratory Data like [blood glucose](observation-example-f001-glucose.html), or an [estimated GFR](observation-example-f205-egfr.html)
 

 - Imaging results like [bone density](observation-example-bmd.html) or fetal measurements

 - Clinical Findings* such as [abdominal tenderness](observation-example-abdo-tender.html)
 

 - Device measurements such as [EKG data](observation-example-sample-data.html) or [Pulse Oximetry data](observation-example-satO2.html)
 

 - Clinical assessment tools such as [APGAR](observation-example-5minute-apgar-score.html) or a [Glasgow Coma Score](observation-example-glasgow.html)
 

 - Personal characteristics: such as [eye-color](observation-example-eye-color.html)
 

 - Social history like tobacco use, family support, or cognitive status

 - Core characteristics like pregnancy status, or a death assertion

 

 

 *The boundaries between clinical findings and disorders remains a challenge in medical ontology. Refer the [Boundaries](#bnr) section below and in [Condition](condition.html#bnr) for general guidance. These boundaries can be clarified by profiling Observation for a particular use case.
 

 
 
### 10.1.1.1 Core Profiles for Observation [Trial Use](versions.html#std-process) [
](observation.html#core)

 The following core [profiles](profiling.html) for the Observation resource have been defined as well. If implementations use this Resource when expressing the profile-specific concepts as structured data, they **SHALL** conform to the following profiles:

 

 
 | 
 Profile | 
 Description | 
 |

 
 
 | 
 
 [Vital signs](observation-vitalsigns.html)
 | 
 The FHIR Vital Signs profile sets minimum expectations for the Observation Resource to record, search and fetch the vital signs (e.g. temperature, blood pressure, respiration rate, etc.) associated with a patient | 
 |

 
 

 

 

 
 
 
## 10.1.2 Boundaries and Relationships [
](observation.html#bnr)

 
At its core, Observation allows expressing a name-value pair or structured collection of name-value pairs. As such, it can support conveying any type of information desired. However, that is not its intent. Observation is intended for capturing measurements and subjective point-in-time assessments. It is not intended to be used for those specific contexts and use cases already covered by other FHIR resources. For example, the [AllergyIntolerance](allergyintolerance.html) resource represents a patient allergies, [MedicationStatement](medicationstatement.html) resource: medications taken by a patient, [ FamilyMemberHistory](familymemberhistory.html) resource: a patient's family history, [Procedure](procedure.html) resource: information about a procedure, and [QuestionnaireResponse](questionnaireresponse.html) resource: a set of answers to a set of questions. The Observation resource should not be used to record clinical diagnosis about a patient or subject that are typically captured in the [Condition](condition.html) resource or the ClinicalImpression resource. The Observation resource is often referenced by the Condition resource to provide specific subjective and objective data to support its assertions. There will however be situations of overlap. For example, a response to a question of "have you ever taken illicit drugs" could in principle be represented using MedicationStatement, but most systems would treat such an assertion as an Observation. In some cases, such as when source data is coming from an [HL7 v2 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) feed, a system might not have information that allows it to distinguish diagnosis, allergy and other "specialized" types of observations from laboratory, vital sign and other observation types intended to be conveyed with this resource. In those circumstances, such specialized observations may also appear using this resource. Adhering to such convention is an appropriate use of Observation. If implementers are uncertain whether a proposed use of Observation is appropriate, they're encouraged to consult with implementers on [ chat.fhir.org implementer's stream ](https://chat.fhir.org/)
 

 

 The [Media](media.html) resource captures a specific type of observation whose value is audio, video or image data. This resource is used instead of Observation to represent such forms of information as it exposes the metadata relevant for interpreting the information. See Media's [boundaries section](media.html#bnr) to see how Media (and Observation) differs from [ImagingStudy](imagingstudy.html) and [DocumentReference](documentreference.html).
 

 

 In contrast to the Observation resource, the [DiagnosticReport](diagnosticreport.html) resource typically includes additional clinical context and some mix of atomic results, images, imaging reports, textual and coded interpretation, and formatted representations. Laboratory reports, pathology reports, and imaging reports should be represented using the DiagnosticReport resource. The Observation resource is referenced by the DiagnosticReport to provide the atomic results for a particular investigation. "Laboratories routinely have a variable that is summative across a series of discrete variables - these are usually called 'impressions' or 'interpretations'. Sometimes they are algorithmically specified and sometimes they have the imprimatur of pathologists and they are conveyed in Observation or DiagnosticReport instead of the [Clinical Impression](clinicalimpression.html) resource. The Observation resource should not be used to record clinical diagnosis about a patient or subject as discussed above.
 

 

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [Appointment](appointment.html#Appointment), [CarePlan](careplan.html#CarePlan), [ChargeItem](chargeitem.html#ChargeItem), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Condition](condition.html#Condition), [Contract](contract.html#Contract), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [Encounter](encounter.html#Encounter), [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory), [Goal](goal.html#Goal), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MolecularSequence](molecularsequence.html#MolecularSequence), itself, [Procedure](procedure.html#Procedure), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [ServiceRequest](servicerequest.html#ServiceRequest) and [SupplyRequest](supplyrequest.html#SupplyRequest)

## 10.1.3 
Resource Content
 [
](observation.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Observation](observation-definitions.html#Observation) | [I](conformance-rules.html#constraints)[N](versions.html#std-process) | | [DomainResource](domainresource.html) | Measurements and simple assertions**+ Rule: dataAbsentReason SHALL only be present if Observation.value[x] is not present
+ Rule: If Observation.code is the same as an Observation.component.code then the value element associated with the code SHALL NOT be present
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](observation-definitions.html#Observation.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for observation
 | |

| [basedOn](observation-definitions.html#Observation.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CarePlan](careplan.html) | [DeviceRequest](devicerequest.html) | [ImmunizationRecommendation](immunizationrecommendation.html) | [MedicationRequest](medicationrequest.html) | [NutritionOrder](nutritionorder.html) | [ServiceRequest](servicerequest.html)) | Fulfills plan, proposal or order
 | |

| [partOf](observation-definitions.html#Observation.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([MedicationAdministration](medicationadministration.html) | [MedicationDispense](medicationdispense.html) | [MedicationStatement](medicationstatement.html) | [Procedure](procedure.html) | [Immunization](immunization.html) | [ImagingStudy](imagingstudy.html)) | Part of referenced event
 | |

| [status](observation-definitions.html#Observation.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | registered | preliminary | final | amended +
[ObservationStatus](valueset-observation-status.html) ([Required](terminologies.html#required)) | |

| [category](observation-definitions.html#Observation.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of type of observation
[Observation Category Codes](valueset-observation-category.html) ([Preferred](terminologies.html#preferred))
 | |

| [code](observation-definitions.html#Observation.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of observation (code / type)
[LOINC Codes](valueset-observation-codes.html) ([Example](terminologies.html#example)) | |

| [subject](observation-definitions.html#Observation.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html) | [Device](device.html) | [Location](location.html)) | Who and/or what the observation is about | |

| [focus](observation-definitions.html#Observation.focus) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[TU](versions.html#std-process) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | What the observation is about, when it is not about the subject of record
 | |

| [encounter](observation-definitions.html#Observation.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Healthcare event during which this observation is made | |

| [effective[x]](observation-definitions.html#Observation.effective_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Clinically relevant time/time-period for observation | |

| effectiveDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| effectivePeriod | | | [Period](datatypes.html#Period) | | |

| effectiveTiming | | | [Timing](datatypes.html#Timing) | | |

| effectiveInstant | | | [instant](datatypes.html#instant) | | |

| [issued](observation-definitions.html#Observation.issued) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [instant](datatypes.html#instant) | Date/Time this version was made available | |

| [performer](observation-definitions.html#Observation.performer) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [CareTeam](careteam.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who is responsible for the observation
 | |

| [value[x]](observation-definitions.html#Observation.value_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..1 | | Actual result | |

| valueQuantity | | | [Quantity](datatypes.html#Quantity) | | |

| valueCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| valueString | | | [string](datatypes.html#string) | | |

| valueBoolean | | | [boolean](datatypes.html#boolean) | | |

| valueInteger | | | [integer](datatypes.html#integer) | | |

| valueRange | | | [Range](datatypes.html#Range) | | |

| valueRatio | | | [Ratio](datatypes.html#Ratio) | | |

| valueSampledData | | | [SampledData](datatypes.html#SampledData) | | |

| valueTime | | | [time](datatypes.html#time) | | |

| valueDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| valuePeriod | | | [Period](datatypes.html#Period) | | |

| [dataAbsentReason](observation-definitions.html#Observation.dataAbsentReason) | [I](conformance-rules.html#constraints) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the result is missing
[DataAbsentReason](valueset-data-absent-reason.html) ([Extensible](terminologies.html#extensible)) | |

| [interpretation](observation-definitions.html#Observation.interpretation) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | High, low, normal, etc.
[Observation Interpretation Codes](valueset-observation-interpretation.html) ([Extensible](terminologies.html#extensible))
 | |

| [note](observation-definitions.html#Observation.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments about the observation
 | |

| [bodySite](observation-definitions.html#Observation.bodySite) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Observed body part
[SNOMED CT Body Structures](valueset-body-site.html) ([Example](terminologies.html#example)) | |

| [method](observation-definitions.html#Observation.method) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How it was done
[Observation Methods](valueset-observation-methods.html) ([Example](terminologies.html#example)) | |

| [specimen](observation-definitions.html#Observation.specimen) | | 0..1 | [Reference](references.html#Reference)([Specimen](specimen.html)) | Specimen used for this observation | |

| [device](observation-definitions.html#Observation.device) | | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [DeviceMetric](devicemetric.html)) | (Measurement) Device | |

| [referenceRange](observation-definitions.html#Observation.referenceRange) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Provides guide for interpretation
+ Rule: Must have at least a low or a high or text
 | |

| [=5 - low](observation-definitions.html#Observation.referenceRange.low) | [I](conformance-rules.html#constraints) | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Low Range, if relevant | |

| [=5 - = 2.3).">high](observation-definitions.html#Observation.referenceRange.high) | [I](conformance-rules.html#constraints) | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | High Range, if relevant | |

| [type](observation-definitions.html#Observation.referenceRange.type) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reference range qualifier
[Observation Reference Range Meaning Codes](valueset-referencerange-meaning.html) ([Preferred](terminologies.html#preferred)) | |

| [appliesTo](observation-definitions.html#Observation.referenceRange.appliesTo) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Reference range population
[Observation Reference Range Applies To Codes](valueset-referencerange-appliesto.html) ([Example](terminologies.html#example))
 | |

| [age](observation-definitions.html#Observation.referenceRange.age) | | 0..1 | [Range](datatypes.html#Range) | Applicable age range, if relevant | |

| [text](observation-definitions.html#Observation.referenceRange.text) | | 0..1 | [string](datatypes.html#string) | Text based reference range in an observation | |

| [hasMember](observation-definitions.html#Observation.hasMember) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Observation](observation.html) | [QuestionnaireResponse](questionnaireresponse.html) | [MolecularSequence](molecularsequence.html)) | Related resource that belongs to the Observation group
 | |

| [derivedFrom](observation-definitions.html#Observation.derivedFrom) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([DocumentReference](documentreference.html) | [ImagingStudy](imagingstudy.html) | [Media](media.html) | [QuestionnaireResponse](questionnaireresponse.html) | [Observation](observation.html) | [MolecularSequence](molecularsequence.html)) | Related measurements the observation is made from
 | |

| [component](observation-definitions.html#Observation.component) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | Component results
 | |

| [code](observation-definitions.html#Observation.component.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of component observation (code / type)
[LOINC Codes](valueset-observation-codes.html) ([Example](terminologies.html#example)) | |

| [value[x]](observation-definitions.html#Observation.component.value_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Actual component result | |

| valueQuantity | | | [Quantity](datatypes.html#Quantity) | | |

| valueCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| valueString | | | [string](datatypes.html#string) | | |

| valueBoolean | | | [boolean](datatypes.html#boolean) | | |

| valueInteger | | | [integer](datatypes.html#integer) | | |

| valueRange | | | [Range](datatypes.html#Range) | | |

| valueRatio | | | [Ratio](datatypes.html#Ratio) | | |

| valueSampledData | | | [SampledData](datatypes.html#SampledData) | | |

| valueTime | | | [time](datatypes.html#time) | | |

| valueDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| valuePeriod | | | [Period](datatypes.html#Period) | | |

| [dataAbsentReason](observation-definitions.html#Observation.component.dataAbsentReason) | [I](conformance-rules.html#constraints) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the component result is missing
[DataAbsentReason](valueset-data-absent-reason.html) ([Extensible](terminologies.html#extensible)) | |

| [interpretation](observation-definitions.html#Observation.component.interpretation) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | High, low, normal, etc.
[Observation Interpretation Codes](valueset-observation-interpretation.html) ([Extensible](terminologies.html#extensible))
 | |

| [referenceRange](observation-definitions.html#Observation.component.referenceRange) | | 0..* | see [referenceRange](#Observation.referenceRange) | Provides guide for interpretation of component result
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Observation ([DomainResource](domainresource.html))[A unique identifier assigned to this observationidentifier](observation-definitions.html#Observation.identifier) : [Identifier](datatypes.html#Identifier) [0..*][A plan, proposal or order that is fulfilled in whole or in part by this event. For example, a MedicationRequest may require a patient to have laboratory test performed before it is dispensedbasedOn](observation-definitions.html#Observation.basedOn) : [Reference](references.html#Reference) [0..*] « [CarePlan](careplan.html#CarePlan)|[DeviceRequest](devicerequest.html#DeviceRequest)| [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[NutritionOrder](nutritionorder.html#NutritionOrder)| [ServiceRequest](servicerequest.html#ServiceRequest) »[A larger event of which this particular Observation is a component or step. For example, an observation as part of a procedurepartOf](observation-definitions.html#Observation.partOf) : [Reference](references.html#Reference) [0..*] « [MedicationAdministration](medicationadministration.html#MedicationAdministration)| [MedicationDispense](medicationdispense.html#MedicationDispense)|[MedicationStatement](medicationstatement.html#MedicationStatement)|[Procedure](procedure.html#Procedure)|[Immunization](immunization.html#Immunization)| [ImagingStudy](imagingstudy.html#ImagingStudy) »[The status of the result value (this element modifies the meaning of other elements)status](observation-definitions.html#Observation.status) : [code](datatypes.html#code) [1..1] « [Codes providing the status of an observation. (Strength=Required)ObservationStatus](valueset-observation-status.html)! »[A code that classifies the general type of observation being madecategory](observation-definitions.html#Observation.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for high level observation categories. (Strength=Preferred)ObservationCategoryCodes](valueset-observation-category.html)? »[Describes what was observed. Sometimes this is called the observation "name"code](observation-definitions.html#Observation.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Codes identifying names of simple observations. (Strength=Example)LOINCCodes](valueset-observation-codes.html)?? »[The patient, or group of patients, location, or device this observation is about and into whose record the observation is placed. If the actual focus of the observation is different from the subject (or a sample of, part, or region of the subject), the `focus` element or the `code` itself specifies the actual focus of the observationsubject](observation-definitions.html#Observation.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group)|[Device](device.html#Device)|[Location](location.html#Location) »[The actual focus of an observation when it is not the patient of record representing something or someone associated with the patient such as a spouse, parent, fetus, or donor. For example, fetus observations in a mother's record. The focus of an observation could also be an existing condition, an intervention, the subject's diet, another observation of the subject, or a body structure such as tumor or implanted device. An example use case would be using the Observation resource to capture whether the mother is trained to change her child's tracheostomy tube. In this example, the child is the patient of record and the mother is the focusfocus](observation-definitions.html#Observation.focus) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[The healthcare event (e.g. a patient and healthcare provider interaction) during which this observation is madeencounter](observation-definitions.html#Observation.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The time or time-period the observed value is asserted as being true. For biological subjects - e.g. human patients - this is usually called the "physiologically relevant time". This is usually either the time of the procedure or of specimen collection, but very often the source of the date/time is not known, only the date/time itselfeffective[x]](observation-definitions.html#Observation.effective_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period)|[Timing](datatypes.html#Timing)|[instant](datatypes.html#instant) »[The date and time this version of the observation was made available to providers, typically after the results have been reviewed and verifiedissued](observation-definitions.html#Observation.issued) : [instant](datatypes.html#instant) [0..1][Who was responsible for asserting the observed value as "true"performer](observation-definitions.html#Observation.performer) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »[The information determined as a result of making the observation, if the information has a simple valuevalue[x]](observation-definitions.html#Observation.value_x_) : [Type](formats.html#umlchoice) [0..1] « [Quantity](datatypes.html#Quantity)|[CodeableConcept](datatypes.html#CodeableConcept)|[string](datatypes.html#string)|[boolean](datatypes.html#boolean)| [integer](datatypes.html#integer)|[Range](datatypes.html#Range)|[Ratio](datatypes.html#Ratio)|[SampledData](datatypes.html#SampledData)|[time](datatypes.html#time)|[dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »[Provides a reason why the expected value in the element Observation.value[x] is missingdataAbsentReason](observation-definitions.html#Observation.dataAbsentReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes specifying why the result (`Observation.value[x]`) is missing. (Strength=Extensible)DataAbsentReason](valueset-data-absent-reason.html)+ »[A categorical assessment of an observation value. For example, high, low, normalinterpretation](observation-definitions.html#Observation.interpretation) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes identifying interpretations of observations. (Strength=Extensible)](valueset-observation-interpretation.html) [ObservationInterpretationCodes](valueset-observation-interpretation.html)+ »[Comments about the observation or the resultsnote](observation-definitions.html#Observation.note) : [Annotation](datatypes.html#Annotation) [0..*][Indicates the site on the subject's body where the observation was made (i.e. the target site)bodySite](observation-definitions.html#Observation.bodySite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing anatomical locations. May include laterality. (Strength=Example)SNOMEDCTBodyStructures](valueset-body-site.html)?? »[Indicates the mechanism used to perform the observationmethod](observation-definitions.html#Observation.method) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Methods for simple observations. (Strength=Example)ObservationMethods](valueset-observation-methods.html)?? »[The specimen that was used when this observation was madespecimen](observation-definitions.html#Observation.specimen) : [Reference](references.html#Reference) [0..1] « [Specimen](specimen.html#Specimen) »[The device used to generate the observation datadevice](observation-definitions.html#Observation.device) : [Reference](references.html#Reference) [0..1] « [Device](device.html#Device)|[DeviceMetric](devicemetric.html#DeviceMetric) »[This observation is a group observation (e.g. a battery, a panel of tests, a set of vital sign measurements) that includes the target as a member of the grouphasMember](observation-definitions.html#Observation.hasMember) : [Reference](references.html#Reference) [0..*] « [Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)| [MolecularSequence](molecularsequence.html#MolecularSequence) »[The target resource that represents a measurement from which this observation value is derived. For example, a calculated anion gap or a fetal measurement based on an ultrasound imagederivedFrom](observation-definitions.html#Observation.derivedFrom) : [Reference](references.html#Reference) [0..*] « [DocumentReference](documentreference.html#DocumentReference)|[ImagingStudy](imagingstudy.html#ImagingStudy)| [Media](media.html#Media)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)|[Observation](observation.html#Observation)|[MolecularSequence](molecularsequence.html#MolecularSequence) »ReferenceRange[The value of the low bound of the reference range. The low bound of the reference range endpoint is inclusive of the value (e.g. reference range is >=5 - <=9). If the low bound is omitted, it is assumed to be meaningless (e.g. reference range is <=2.3)low](observation-definitions.html#Observation.referenceRange.low) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][The value of the high bound of the reference range. The high bound of the reference range endpoint is inclusive of the value (e.g. reference range is >=5 - <=9). If the high bound is omitted, it is assumed to be meaningless (e.g. reference range is >= 2.3)high](observation-definitions.html#Observation.referenceRange.high) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][Codes to indicate the what part of the targeted reference population it applies to. For example, the normal or therapeutic rangetype](observation-definitions.html#Observation.referenceRange.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Code for the meaning of a reference range. (Strength=Preferred)ObservationReferenceRangeMean...](valueset-referencerange-meaning.html)? »[Codes to indicate the target population this reference range applies to. For example, a reference range may be based on the normal population or a particular sex or race. Multiple `appliesTo` are interpreted as an "AND" of the target populations. For example, to represent a target population of African American females, both a code of female and a code for African American would be usedappliesTo](observation-definitions.html#Observation.referenceRange.appliesTo) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes identifying the population the reference range applies to. (Strength=Example)](valueset-referencerange-appliesto.html) [ObservationReferenceRangeAppl...](valueset-referencerange-appliesto.html)?? »[The age at which this reference range is applicable. This is a neonatal age (e.g. number of weeks at term) if the meaning says soage](observation-definitions.html#Observation.referenceRange.age) : [Range](datatypes.html#Range) [0..1][Text based reference range in an observation which may be used when a quantitative range is not appropriate for an observation. An example would be a reference value of "Negative" or a list or table of "normals"text](observation-definitions.html#Observation.referenceRange.text) : [string](datatypes.html#string) [0..1]Component[Describes what was observed. Sometimes this is called the observation "code"code](observation-definitions.html#Observation.component.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Codes identifying names of simple observations. (Strength=Example)LOINCCodes](valueset-observation-codes.html)?? »[The information determined as a result of making the observation, if the information has a simple valuevalue[x]](observation-definitions.html#Observation.component.value_x_) : [Type](formats.html#umlchoice) [0..1] « [Quantity](datatypes.html#Quantity)|[CodeableConcept](datatypes.html#CodeableConcept)|[string](datatypes.html#string)|[boolean](datatypes.html#boolean)| [integer](datatypes.html#integer)|[Range](datatypes.html#Range)|[Ratio](datatypes.html#Ratio)|[SampledData](datatypes.html#SampledData)|[time](datatypes.html#time)|[dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »[Provides a reason why the expected value in the element Observation.component.value[x] is missingdataAbsentReason](observation-definitions.html#Observation.component.dataAbsentReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes specifying why the result (`Observation.value[x]`) is missing. (Strength=Extensible)DataAbsentReason](valueset-data-absent-reason.html)+ »[A categorical assessment of an observation value. For example, high, low, normalinterpretation](observation-definitions.html#Observation.component.interpretation) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes identifying interpretations of observations. (Strength=Extensible)](valueset-observation-interpretation.html) [ObservationInterpretationCodes](valueset-observation-interpretation.html)+ »
[Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges are interpreted as an "OR". In other words, to represent two distinct target populations, two `referenceRange` elements would be usedreferenceRange](observation-definitions.html#Observation.referenceRange)[0..*][Guidance on how to interpret the value by comparison to a normal or recommended rangereferenceRange](observation-definitions.html#Observation.component.referenceRange)[0..*][Some observations have multiple component observations. These component observations are expressed as separate code value pairs that share the same attributes. Examples include systolic and diastolic component observations for blood pressure measurement and multiple component observations for genetics observationscomponent](observation-definitions.html#Observation.component)[0..*]
 

 

 

**XML Template**

 

 
```
http://hl7.org/fhir/ValueSet/referencerange-meaning
```

 

**JSON Template**

 

 
```
http://hl7.org/fhir/ValueSet/referencerange-meaning
```

 
 
#### 10.1.4.4.2 Text values for coded results: [
](observation.html#text)

 When the data element is usually coded or the type associated with the `code` element defines a coded value, use `valueCodeableConcept`
 *even if* there is no appropriate code and only free text is available. For example using text only, the `valueCodeableConcept` element would be:

 
```
valueCodeableConcept.text
```

 
 
 
 
#### 10.1.4.4.3 Interoperability Issues using code value pairs in FHIR [
](observation.html#code-interop)

 A recurring issue for many observation events, regardless of the particular pattern, is determining how to populate observation.code and observation.value. While this is typically straight-forward for laboratory observations, it can get blurry for other types of observations, such as findings and disorders, family history observations, etc. This discussion focuses on the way in which the coded representation of such statements is expressed using the `Observation.code` and `Observation.value` elements. 

 
There are two distinct facets that are central to a FHIR Observations:

 

 The action taken to make the finding and/or the property about which the property was observed. For example: measurement of blood hemoglobin.
 

 - The result of the observation. For example: 14 g/dl.
 

 

 
Several different ways of representing the same information exist using different combinations of the `Observation.code` and `Observation.value`. Unconstrained use of the alternatives presents a major challenge for computation of semantic equivalence and for safe interpretation of observations originating from different applications and users. The following four patterns could reasonably represent the same case. Considering that the Observation resource needs to support many use cases, the appropriate place to define the specific pattern is expected to be done through profiles and implementation guides as specified by the jurisdictions and/or organizations implementing FHIR:

 

 - 
 `Observation.code` represents the nature of the observation and the `Observation.value` a code represents the non-numeric result value. These are two distinct facets that are central to a FHIR Observations. For example:
 

 code=[Examination] 

 - value=[Abdomen tender]

 

 
 - 
 `Observation.code` is nearly identical to 1) above, but the level of granularity is shifted from the value to code. For example:
 

 code=[Abdominal examination] 

 - value=[Tenderness]

 

 
 - 
 The `Observation.code` is also expressed in a way that does not specify the observation action but indicates a statement about findings reduced to a single name (or term), as in the above item. In this example, the `Observation.value` is present and "qualifies" the finding typically confirming or refuting it. For example:
 

 code=[Abdominal tenderness] 

 - value=[found/true]

 

 
 - 
 in this example the `Observation.code` is expressed in a way that does not specify the observation action but indicates a statement about findings reduced to a single name (or term). In this particular example in that context, the `Observation.value` is omitted. For example:
 

 code=[Abdominal tenderness]

 - value element is omitted

 

 
 

 
 
#### 10.1.4.4.4 Guidance: [
](observation.html#guidance)

 

 - Recommended rules for case 1 and 2 patterns:
 

 The Observation.code is preferably a [LOINC ](https://loinc.org/) concept code.
 

 If a [SNOMED CT ](http://snomed.info/sct) concept code is used, the expression SHOULD represent a 363787002 (Observable entity(Observable entity)) or 386053000 (Evaluation procedure(evaluation procedure))
 

 

 
 - For non-numeric values, the Observation.value is preferably a SNOMED CT concept code.
 

 

 
 - Recommended rules for case 3 pattern:
 

 The Observation.code is preferably a LOINC or SNOMED CT concept code.
 

 If a SNOMED CT concept code is used, the expression SHOULD represent a 404684003 (Clinical finding (finding)) , 413350009 (Finding with explicit context(finding)), or 272379006 (Event(event)).
 

 

 
 - The Observation.value is represented by either
 

 valueBoolean

 - valueCodeableConcept preferably using:
 

 
 SNOMED CT where concept is-a 362981000 (Qualifier value (qualifier value))
 

 - 
 [v2 Yes/no Indicator](v2/0136/index.html)
 

 - 
 [v2 Expanded Yes/no Indicator](v2/0136/index.html) (unfortunately is missing 'not given')
 

 

 
 

 
 

 
 - Recommended rules for case 4 pattern:
 

 The Observation.code is preferably a SNOMED CT concept code where the concept is-a 404684003 (Clinical finding (finding)) , 413350009 (Finding with explicit context(finding)), or 272379006 (Event(event)).
 

 - The Observation.value is omitted. The default interpretation is the concept (single code or expression) represented in Observation.code is present in the patient. An Observation.dataAbsentReason value of 'clinical-finding' SHOULD be used to indicate why the expected value is missing.

 

 
 - SHOULD NOT use the *Assertion* pattern as described in [HL7 Version 3 Implementation Guide: TermInfo - Using SNOMED CT in CDA R2 Models, Release 1 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=418). ( The code is 'ASSERTION' and the value is a SNOMED CT concept or expression )
 

 

 
 
 
### 10.1.4.5 Refining the interpretation of an Observation using additional codes or Observations [](observation.html#refine)

 The following list provides guidance on using codes or other observations to provide additional context that may alter how an observation is interpreted.: 

 

 - 
 
If possible, use the most specific code you can

 
e.g.:

 
```
value[x]
```

If the value was "NaN" (i.e. an error) the `valueCodeableConcept` element would be absent and `dataAbsentReason` element would be:

```
 "dataAbsentReason": {
 "coding": [
 {
 "system": "http://terminology.hl7.org/CodeSystem/data-absent-reason",
 "code": "NaN",
 "display": "Not a Number"
 }
 ]
 }
 
```

 

 - Because there are multiple types allowed for the value* element, multiple value search parameters are defined. There is no standard parameter for searching values of type Ratio 

 

 
 
### 10.1.4.7 Physiologically Relevant Time of the Observation [
](observation.html#time)

 The effectiveDateTime or effectivePeriod is the time that the observation is most relevant as an observation of the subject. For a biological subject (e.g. a human patient), this is the physiologically relevant time of the observation. In the case of an observation using a specimen, this represents the start and end of the specimen collection (e.g. 24-hour Urine Sodium), but if the collection time is sufficiently short, this is reported as a point in time value (e.g. normal venipuncture). In the case of an observation obtained directly from a subject (e.g. BP, Chest X-ray), this is the start and end time of the observation process, which again, is often reported as a single point in time.

 
 
### 10.1.4.8 Reference Range [
](observation.html#refrange)

 Most common observations will only have one generic reference range. Reference ranges may be useful for laboratory tests and other measures like systolic blood pressure but will have little relevance for something like "pregnancy status". Systems MAY choose to restrict to only supplying the relevant reference range based on knowledge about the patient (e.g. specific to the patient's age, gender, weight and other factors), but this might not be possible or appropriate. Whenever more than one reference range is supplied, the differences between them SHOULD be provided in the reference range and/or age properties. 

 
 
### 10.1.4.9 Canceled or Aborted Observations [
](observation.html#cancelled)

 If a measurement or test could not be completed (for example if the specimen is unsatisfactory or the provider cancelled the order), then the status value should be updated to "cancelled" and the specific details given - preferably as coded values in the dataAbsentReason or valueCodeableConcept element. Additional information may be provided in the `note` element as well. The [specimen reject example](observation-example-unsat.html) demonstrates this using a coded value for unsatisfactory specimen in dataAbsentReason.

 
 
 
 
### 10.1.4.10 Genetic Observations [
](observation.html#genetics)

 Genetic reporting makes heavy use of the DiagnosticReport and Observation resources. An implementation guide describing how to represent genetic results can be found [here ](http://hl7.org/fhir/uv/genomics-reporting/index.html).

 
## 10.1.5 Operations defined for Observation [
](observation.html#ops)

 
 
 
### 10.1.5.1 Searching for the Last N Observations [](observation.html#lastn)

 The *lastn* query operation meets the common need for searching for the most recent or "last known" Observations for a subject. Examples where this query could be used:

 

 - Fetch the last 5 temperatures for a patient to view trends

 - Get the most recent laboratory results for patient

 - Fetch the last 3 results for all vitals for a patient

 

 
See the [Last N Observations Query](observation-operation-lastn.html) section in the Observation resource operations page for more information and examples

 

 

 
 
 
### 10.1.5.2 Retrieving Statistics for Laboratory Observations [
](observation.html#stats)

 The *stats* operation performs a set of statistical calculations on a set of clinical measurements such as a blood pressure as stored on the server. This operation is focused on Observation resources with valueQuantity elements that have UCUM unit codes. Examples where this operation could be used:

 

 - Get the average, min, max and count of a series of BP measurements for a patient

 - Determine 20th or 80th percentile on a set of measurements over a time period

 
See the [Observation Statistics](observation-operation-stats.html) section in the Observation resource operations page for more information and examples

 

## 10.1.6 Search Parameters [
](observation.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| based-on [TU](versions.html#std-process) | [reference](search.html#reference) | Reference to the service request. | Observation.basedOn
([CarePlan](careplan.html), [MedicationRequest](medicationrequest.html), [NutritionOrder](nutritionorder.html), [DeviceRequest](devicerequest.html), [ServiceRequest](servicerequest.html), [ImmunizationRecommendation](immunizationrecommendation.html)) | | |

| category [TU](versions.html#std-process) | [token](search.html#token) | The classification of the type of observation | Observation.category | | |

| code [TU](versions.html#std-process) | [token](search.html#token) | The code of the observation type | Observation.code | [13 Resources](searchparameter-registry.html#clinical-code) | |

| code-value-concept [TU](versions.html#std-process) | [composite](search.html#composite) | Code and coded value parameter pair | On Observation:
 code: code
 value-concept: value.as(CodeableConcept) | | |

| code-value-date [TU](versions.html#std-process) | [composite](search.html#composite) | Code and date/time value parameter pair | On Observation:
 code: code
 value-date: value.as(DateTime) | value.as(Period) | | |

| code-value-quantity [TU](versions.html#std-process) | [composite](search.html#composite) | Code and quantity value parameter pair | On Observation:
 code: code
 value-quantity: value.as(Quantity) | | |

| code-value-string [TU](versions.html#std-process) | [composite](search.html#composite) | Code and string value parameter pair | On Observation:
 code: code
 value-string: value.as(string) | | |

| combo-code [TU](versions.html#std-process) | [token](search.html#token) | The code of the observation type or component type | Observation.code | Observation.component.code | | |

| combo-code-value-concept [TU](versions.html#std-process) | [composite](search.html#composite) | Code and coded value parameter pair, including in components | On Observation | Observation.component:
 combo-code: code
 combo-value-concept: value.as(CodeableConcept) | | |

| combo-code-value-quantity [TU](versions.html#std-process) | [composite](search.html#composite) | Code and quantity value parameter pair, including in components | On Observation | Observation.component:
 combo-code: code
 combo-value-quantity: value.as(Quantity) | | |

| combo-data-absent-reason [TU](versions.html#std-process) | [token](search.html#token) | The reason why the expected value in the element Observation.value[x] or Observation.component.value[x] is missing. | Observation.dataAbsentReason | Observation.component.dataAbsentReason | | |

| combo-value-concept [TU](versions.html#std-process) | [token](search.html#token) | The value or component value of the observation, if the value is a CodeableConcept | (Observation.value as CodeableConcept) | (Observation.component.value as CodeableConcept) | | |

| combo-value-quantity [TU](versions.html#std-process) | [quantity](search.html#quantity) | The value or component value of the observation, if the value is a Quantity, or a SampledData (just search on the bounds of the values in sampled data) | (Observation.value as Quantity) | (Observation.value as SampledData) | (Observation.component.value as Quantity) | (Observation.component.value as SampledData) | | |

| component-code [TU](versions.html#std-process) | [token](search.html#token) | The component code of the observation type | Observation.component.code | | |

| component-code-value-concept [TU](versions.html#std-process) | [composite](search.html#composite) | Component code and component coded value parameter pair | On Observation.component:
 component-code: code
 component-value-concept: value.as(CodeableConcept) | | |

| component-code-value-quantity [TU](versions.html#std-process) | [composite](search.html#composite) | Component code and component quantity value parameter pair | On Observation.component:
 component-code: code
 component-value-quantity: value.as(Quantity) | | |

| component-data-absent-reason [TU](versions.html#std-process) | [token](search.html#token) | The reason why the expected value in the element Observation.component.value[x] is missing. | Observation.component.dataAbsentReason | | |

| component-value-concept [TU](versions.html#std-process) | [token](search.html#token) | The value of the component observation, if the value is a CodeableConcept | (Observation.component.value as CodeableConcept) | | |

| component-value-quantity [TU](versions.html#std-process) | [quantity](search.html#quantity) | The value of the component observation, if the value is a Quantity, or a SampledData (just search on the bounds of the values in sampled data) | (Observation.component.value as Quantity) | (Observation.component.value as SampledData) | | |

| data-absent-reason [TU](versions.html#std-process) | [token](search.html#token) | The reason why the expected value in the element Observation.value[x] is missing. | Observation.dataAbsentReason | | |

| date [TU](versions.html#std-process) | [date](search.html#date) | Obtained date/time. If the obtained element is a period, a date that falls in the period | Observation.effective | [17 Resources](searchparameter-registry.html#clinical-date) | |

| derived-from [TU](versions.html#std-process) | [reference](search.html#reference) | Related measurements the observation is made from | Observation.derivedFrom
([Media](media.html), [Observation](observation.html), [ImagingStudy](imagingstudy.html), [MolecularSequence](molecularsequence.html), [QuestionnaireResponse](questionnaireresponse.html), [DocumentReference](documentreference.html)) | | |

| device [TU](versions.html#std-process) | [reference](search.html#reference) | The Device that generated the observation data. | Observation.device
([Device](device.html), [DeviceMetric](devicemetric.html)) | | |

| encounter [TU](versions.html#std-process) | [reference](search.html#reference) | Encounter related to the observation | Observation.encounter
([Encounter](encounter.html)) | [12 Resources](searchparameter-registry.html#clinical-encounter) | |

| focus [TU](versions.html#std-process) | [reference](search.html#reference) | The focus of an observation when the focus is not the patient of record. | Observation.focus
(Any) | | |

| has-member [TU](versions.html#std-process) | [reference](search.html#reference) | Related resource that belongs to the Observation group | Observation.hasMember
([Observation](observation.html), [MolecularSequence](molecularsequence.html), [QuestionnaireResponse](questionnaireresponse.html)) | | |

| identifier [TU](versions.html#std-process) | [token](search.html#token) | The unique id for a particular observation | Observation.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| method [TU](versions.html#std-process) | [token](search.html#token) | The method used for the observation | Observation.method | | |

| part-of [TU](versions.html#std-process) | [reference](search.html#reference) | Part of referenced event | Observation.partOf
([Immunization](immunization.html), [MedicationDispense](medicationdispense.html), [MedicationAdministration](medicationadministration.html), [Procedure](procedure.html), [ImagingStudy](imagingstudy.html), [MedicationStatement](medicationstatement.html)) | | |

| patient [TU](versions.html#std-process) | [reference](search.html#reference) | The subject that the observation is about (if patient) | Observation.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| performer [TU](versions.html#std-process) | [reference](search.html#reference) | Who performed the observation | Observation.performer
([Practitioner](practitioner.html), [Organization](organization.html), [CareTeam](careteam.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| specimen [TU](versions.html#std-process) | [reference](search.html#reference) | Specimen used for this observation | Observation.specimen
([Specimen](specimen.html)) | | |

| status [TU](versions.html#std-process) | [token](search.html#token) | The status of the observation | Observation.status | | |

| subject [TU](versions.html#std-process) | [reference](search.html#reference) | The subject that the observation is about | Observation.subject
([Group](group.html), [Device](device.html), [Patient](patient.html), [Location](location.html)) | | |

| value-concept [TU](versions.html#std-process) | [token](search.html#token) | The value of the observation, if the value is a CodeableConcept | (Observation.value as CodeableConcept) | | |

| value-date [TU](versions.html#std-process) | [date](search.html#date) | The value of the observation, if the value is a date or period of time | (Observation.value as dateTime) | (Observation.value as Period) | | |

| value-quantity [TU](versions.html#std-process) | [quantity](search.html#quantity) | The value of the observation, if the value is a Quantity, or a SampledData (just search on the bounds of the values in sampled data) | (Observation.value as Quantity) | (Observation.value as SampledData) | | |

| value-string [TU](versions.html#std-process) | [string](search.html#string) | The value of the observation, if the value is a string, and also searches in CodeableConcept.text | (Observation.value as string) | (Observation.value as CodeableConcept).text | | |