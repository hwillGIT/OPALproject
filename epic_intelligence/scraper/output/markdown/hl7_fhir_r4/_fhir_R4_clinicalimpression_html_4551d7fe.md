# ClinicalImpression - FHIR v4.0.1Business identifiers assigned to this clinical impression by the performer or other systems which remain constant as the resource is updated and propagates from server to serverIdentifies the workflow status of the assessment (this element modifies the meaning of other elements)The workflow state of a clinical impression. (Strength=Required)Captures the reason for the current state of the ClinicalImpressionCategorizes the type of clinical assessment performedA summary of the context and/or cause of the assessment - why / where it was performed, and what patient events/status prompted itThe patient or group of individuals assessed as part of this recordThe Encounter during which this ClinicalImpression was created or to which the creation of this record is tightly associatedThe point in time or period over which the subject was assessedIndicates when the documentation of the assessment was completeThe clinician performing the assessmentA reference to the last assessment that was conducted on this patient. Assessments are often/usually ongoing in nature; a care provider (practitioner or team) will make new assessments on an ongoing basis as new data arises or the patient's conditions changesA list of the relevant problems/conditions for a patientReference to a specific published clinical protocol that was followed during this assessment, and/or that provides evidence in support of the diagnosisA text summary of the investigations and the diagnosisEstimate of likely outcomePrognosis or outlook findings. (Strength=Example)RiskAssessment expressing likely outcomeInformation supporting the clinical impressionCommentary about the impression, typically recorded after the impression itself was made, though supplemental notes by the original author could also appearA name/code for the group ("set") of investigations. Typically, this will be something like "signs", "symptoms", "clinical", "diagnostic", but the list is not constrained, and others such groups such as (exposure|family|travel|nutritional) history may be usedA name/code for a set of investigations. (Strength=Example)A record of a specific investigation that was undertakenSpecific text or code for finding or diagnosis, which may include ruled-out or resolved conditionsIdentification of the Condition or diagnosis. (Strength=Example)Specific reference for finding or diagnosis, which may include ruled-out or resolved conditionsWhich investigations support finding or diagnosisOne or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomesSpecific findings or diagnoses that were considered likely or relevant to ongoing treatmentBusiness identifiers assigned to this clinical impression by the performer or other systems which remain constant as the resource is updated and propagates from server to serverIdentifies the workflow status of the assessment (this element modifies the meaning of other elements)The workflow state of a clinical impression. (Strength=Required)Captures the reason for the current state of the ClinicalImpressionCategorizes the type of clinical assessment performedA summary of the context and/or cause of the assessment - why / where it was performed, and what patient events/status prompted itThe patient or group of individuals assessed as part of this recordThe Encounter during which this ClinicalImpression was created or to which the creation of this record is tightly associatedThe point in time or period over which the subject was assessedIndicates when the documentation of the assessment was completeThe clinician performing the assessmentA reference to the last assessment that was conducted on this patient. Assessments are often/usually ongoing in nature; a care provider (practitioner or team) will make new assessments on an ongoing basis as new data arises or the patient's conditions changesA list of the relevant problems/conditions for a patientReference to a specific published clinical protocol that was followed during this assessment, and/or that provides evidence in support of the diagnosisA text summary of the investigations and the diagnosisEstimate of likely outcomePrognosis or outlook findings. (Strength=Example)RiskAssessment expressing likely outcomeInformation supporting the clinical impressionCommentary about the impression, typically recorded after the impression itself was made, though supplemental notes by the original author could also appearA name/code for the group ("set") of investigations. Typically, this will be something like "signs", "symptoms", "clinical", "diagnostic", but the list is not constrained, and others such groups such as (exposure|family|travel|nutritional) history may be usedA name/code for a set of investigations. (Strength=Example)A record of a specific investigation that was undertakenSpecific text or code for finding or diagnosis, which may include ruled-out or resolved conditionsIdentification of the Condition or diagnosis. (Strength=Example)Specific reference for finding or diagnosis, which may include ruled-out or resolved conditionsWhich investigations support finding or diagnosisOne or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomesSpecific findings or diagnoses that were considered likely or relevant to ongoing treatment

> Source: https://hl7.org/fhir/R4/clinicalimpression.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/clinicalimpression.html) [R4B](http://hl7.org/fhir/R4B/clinicalimpression.html) **R4** [R3](http://hl7.org/fhir/STU3/clinicalimpression.html) [R2](http://hl7.org/fhir/DSTU2/clinicalimpression.html)
 

# 9.8 Resource ClinicalImpression - Content [
](clinicalimpression.html#9.8)

| [Patient Care ](http://www.hl7.org/Special/committees/patientcare/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 0 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html) | |

A record of a clinical assessment performed to determine what problem(s) may affect the patient and before planning the treatments or management strategies that are best to manage a patient's condition. Assessments are often 1:1 with a clinical consultation / encounter, but this varies greatly depending on the clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the recording of assessment tools such as Apgar score.

## 9.8.1 Scope and Usage [
](clinicalimpression.html#scope)

Performing a clinical assessment is a fundamental part of a clinician's workflow, performed repeatedly throughout the day. 
In spite of this - or perhaps, because of it - there is wide variance in how clinical impressions are recorded. 
Some clinical assessments simply result in an impression recorded as a single text note in the patient 'record' (e.g. "Progress satisfactory, 
continue with treatment"), while others are associated with careful, detailed record keeping of the 
evidence gathered and the reasoning leading to a differential diagnosis, and there is a continuum between these. This resource is intended to be 
used to cover all these use cases.

The assessment is intimately linked to the process of care. It may occur in the context of a care plan,
and it very often results in a new (or revised) care plan. Normally, clinical assessments are part of an 
ongoing process of care, and the patient will be re-assessed repeatedly. For this reason, the clinical
impression can explicitly reference both care plans (preceding and resulting) and reference a previous
impression that this impression follows.

 
An impression is a clinical summation of information and/or an opinion formed, which is the outcome of the clinical assessment process. The ClinicalImpression may lead to a statement of a Condition about a patient.

 
 
In FHIR, an assessment is typically an instrument or tool used to collect information about a patient.

**
Trial-Use Note:**
Unlike many other resources, there is little prior art with regard to exchanging records of 
clinical assessments. For this reason, this resource should be regarded as particularly 
prone to ongoing revision. In terms of scope and usage, the Patient Care workgroup wishes to
draw the attention of reviewers and implementers to the following issues: 

 - When is an existing clinical impression revised, rather than a new one created (that references the existing one)? How does that affect the status? what's the interplay between the status of the diagnosis and the status of the impression? (e.g. for a 'provisional' impression, which bit is provisional?)

 - This structure doesn't differentiate between a working and a final diagnosis. Given an answer to the previous question, should it?

 - Further clarify around the relationship between care plan and impression is needed. Both answers to the previous questions and ongoing discussions around revisions to the care plan will influence the design of clinical impression

 - Should prognosis be represented, and if so, how much structure should it have?

 - Should an impression reference other impressions that are related? (how related?)

 - Investigations - the specification needs a good value set for the code for the group, and will be considering the name "investigations" further

 

Feedback is welcome [here ](http://hl7.org/fhir-issues).

## 9.8.2 Boundaries and Relationships [
](clinicalimpression.html#bnr)

ClinicalImpression is the equivalent of the "A" in Weed SOAP. It is the outcome of the clinical assessment process. The ClinicalImpression may lead to a statement of a Condition about a patient.

There is another related clinical concept often called an "assessment": assessment Tools such as Apgar (also known as "Assessment Scales").
This is not what the ClinicalImpression resource is about; assessment tools such as Apgar are represented as 
[Observations](observation.html), and [Questionnaires](questionnaire.html) may be used to help 
generate these. Clinical Impressions may refer to these assessment tools as one of the investigations that was performed
during the assessment process.

## 9.8.3 Background and Context [
](clinicalimpression.html#bnc)

An important background to understanding this resource is [the FHIR Confluence page for clinical assessment ](https://confluence.hl7.org/display/PC/Clinical+Assessment). In particular,
the storyboards there drove the design of the resource, and will be the basis for all examples created.

**PLANNED CHANGE:**

**ClinicalImpression** is one of the [Event](workflow.html#event) resources in the FHIR [Workflow](workflow.html) specification. As such, it
is expected to be adjusted to align with the [Event](event.html) workflow pattern which will involve adding a number of additional data elements and potentially
renaming a few elements. Any concerns about performing such alignment are welcome as ballot comments and/or tracker items.

This resource is referenced by itself and [Condition](condition.html#Condition)

## 9.8.4 
Resource Content
 [
](clinicalimpression.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [ClinicalImpression](clinicalimpression-definitions.html#ClinicalImpression) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A clinical assessment performed when planning treatments and management strategies for a patient**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](clinicalimpression-definitions.html#ClinicalImpression.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business identifier
 | |

| [status](clinicalimpression-definitions.html#ClinicalImpression.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | in-progress | completed | entered-in-error
[Clinical Impression Status](valueset-clinicalimpression-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status | |

| [code](clinicalimpression-definitions.html#ClinicalImpression.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of assessment performed | |

| [description](clinicalimpression-definitions.html#ClinicalImpression.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Why/how the assessment was performed | |

| [subject](clinicalimpression-definitions.html#ClinicalImpression.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Patient or group assessed | |

| [encounter](clinicalimpression-definitions.html#ClinicalImpression.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [effective[x]](clinicalimpression-definitions.html#ClinicalImpression.effective_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Time of assessment | |

| effectiveDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| effectivePeriod | | | [Period](datatypes.html#Period) | | |

| [date](clinicalimpression-definitions.html#ClinicalImpression.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When the assessment was documented | |

| [assessor](clinicalimpression-definitions.html#ClinicalImpression.assessor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | The clinician performing the assessment | |

| [previous](clinicalimpression-definitions.html#ClinicalImpression.previous) | | 0..1 | [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html)) | Reference to last assessment | |

| [problem](clinicalimpression-definitions.html#ClinicalImpression.problem) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [AllergyIntolerance](allergyintolerance.html)) | Relevant impressions of patient state
 | |

| [investigation](clinicalimpression-definitions.html#ClinicalImpression.investigation) | | 0..* | [BackboneElement](backboneelement.html) | One or more sets of investigations (signs, symptoms, etc.)
 | |

| [code](clinicalimpression-definitions.html#ClinicalImpression.investigation.code) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | A name/code for the set
[Investigation Type](valueset-investigation-sets.html) ([Example](terminologies.html#example)) | |

| [item](clinicalimpression-definitions.html#ClinicalImpression.investigation.item) | | 0..* | [Reference](references.html#Reference)([Observation](observation.html) | [QuestionnaireResponse](questionnaireresponse.html) | [FamilyMemberHistory](familymemberhistory.html) | [DiagnosticReport](diagnosticreport.html) | [RiskAssessment](riskassessment.html) | [ImagingStudy](imagingstudy.html) | [Media](media.html)) | Record of a specific investigation
 | |

| [protocol](clinicalimpression-definitions.html#ClinicalImpression.protocol) | | 0..* | [uri](datatypes.html#uri) | Clinical Protocol followed
 | |

| [summary](clinicalimpression-definitions.html#ClinicalImpression.summary) | | 0..1 | [string](datatypes.html#string) | Summary of the assessment | |

| [finding](clinicalimpression-definitions.html#ClinicalImpression.finding) | | 0..* | [BackboneElement](backboneelement.html) | Possible or likely findings and diagnoses
 | |

| [itemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What was found
[Condition/Problem/Diagnosis Codes](valueset-condition-code.html) ([Example](terminologies.html#example)) | |

| [itemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference) | | 0..1 | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [Media](media.html)) | What was found | |

| [basis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) | | 0..1 | [string](datatypes.html#string) | Which investigations support finding | |

| [prognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Estimate of likely outcome
[Clinical Impression Prognosis](valueset-clinicalimpression-prognosis.html) ([Example](terminologies.html#example))
 | |

| [prognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference) | | 0..* | [Reference](references.html#Reference)([RiskAssessment](riskassessment.html)) | RiskAssessment expressing likely outcome
 | |

| [supportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Information supporting the clinical impression
 | |

| [note](clinicalimpression-definitions.html#ClinicalImpression.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the ClinicalImpression
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - ClinicalImpression ([DomainResource](domainresource.html))[Business identifiers assigned to this clinical impression by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](clinicalimpression-definitions.html#ClinicalImpression.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Identifies the workflow status of the assessment (this element modifies the meaning of other elements)status](clinicalimpression-definitions.html#ClinicalImpression.status) : [code](datatypes.html#code) [1..1] « [The workflow state of a clinical impression. (Strength=Required)ClinicalImpressionStatus](valueset-clinicalimpression-status.html)! »[Captures the reason for the current state of the ClinicalImpressionstatusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Categorizes the type of clinical assessment performedcode](clinicalimpression-definitions.html#ClinicalImpression.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][A summary of the context and/or cause of the assessment - why / where it was performed, and what patient events/status prompted itdescription](clinicalimpression-definitions.html#ClinicalImpression.description) : [string](datatypes.html#string) [0..1][The patient or group of individuals assessed as part of this recordsubject](clinicalimpression-definitions.html#ClinicalImpression.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this ClinicalImpression was created or to which the creation of this record is tightly associatedencounter](clinicalimpression-definitions.html#ClinicalImpression.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The point in time or period over which the subject was assessedeffective[x]](clinicalimpression-definitions.html#ClinicalImpression.effective_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »[Indicates when the documentation of the assessment was completedate](clinicalimpression-definitions.html#ClinicalImpression.date) : [dateTime](datatypes.html#dateTime) [0..1][The clinician performing the assessmentassessor](clinicalimpression-definitions.html#ClinicalImpression.assessor) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[A reference to the last assessment that was conducted on this patient. Assessments are often/usually ongoing in nature; a care provider (practitioner or team) will make new assessments on an ongoing basis as new data arises or the patient's conditions changesprevious](clinicalimpression-definitions.html#ClinicalImpression.previous) : [Reference](references.html#Reference) [0..1] « [ClinicalImpression](clinicalimpression.html#ClinicalImpression) »[A list of the relevant problems/conditions for a patientproblem](clinicalimpression-definitions.html#ClinicalImpression.problem) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance) »[Reference to a specific published clinical protocol that was followed during this assessment, and/or that provides evidence in support of the diagnosisprotocol](clinicalimpression-definitions.html#ClinicalImpression.protocol) : [uri](datatypes.html#uri) [0..*][A text summary of the investigations and the diagnosissummary](clinicalimpression-definitions.html#ClinicalImpression.summary) : [string](datatypes.html#string) [0..1][Estimate of likely outcomeprognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Prognosis or outlook findings. (Strength=Example)](valueset-clinicalimpression-prognosis.html) [ClinicalImpressionPrognosis](valueset-clinicalimpression-prognosis.html)?? »[RiskAssessment expressing likely outcomeprognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference) : [Reference](references.html#Reference) [0..*] « [RiskAssessment](riskassessment.html#RiskAssessment) »[Information supporting the clinical impressionsupportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Commentary about the impression, typically recorded after the impression itself was made, though supplemental notes by the original author could also appearnote](clinicalimpression-definitions.html#ClinicalImpression.note) : [Annotation](datatypes.html#Annotation) [0..*]Investigation[A name/code for the group ("set") of investigations. Typically, this will be something like "signs", "symptoms", "clinical", "diagnostic", but the list is not constrained, and others such groups such as (exposure|family|travel|nutritional) history may be usedcode](clinicalimpression-definitions.html#ClinicalImpression.investigation.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [A name/code for a set of investigations. (Strength=Example)InvestigationType](valueset-investigation-sets.html)?? »[A record of a specific investigation that was undertakenitem](clinicalimpression-definitions.html#ClinicalImpression.investigation.item) : [Reference](references.html#Reference) [0..*] « [Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)| [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[RiskAssessment](riskassessment.html#RiskAssessment)| [ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media) »Finding[Specific text or code for finding or diagnosis, which may include ruled-out or resolved conditionsitemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identification of the Condition or diagnosis. (Strength=Example)](valueset-condition-code.html) [Condition/Problem/DiagnosisCo...](valueset-condition-code.html)?? »[Specific reference for finding or diagnosis, which may include ruled-out or resolved conditionsitemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference) : [Reference](references.html#Reference) [0..1] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media) »[Which investigations support finding or diagnosisbasis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) : [string](datatypes.html#string) [0..1]
[One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomesinvestigation](clinicalimpression-definitions.html#ClinicalImpression.investigation)[0..*][Specific findings or diagnoses that were considered likely or relevant to ongoing treatmentfinding](clinicalimpression-definitions.html#ClinicalImpression.finding)[0..*]
 

 

 

**XML Template**

 

 
```
<[**ClinicalImpression**](clinicalimpression-definitions.html#ClinicalImpression) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](clinicalimpression-definitions.html#ClinicalImpression.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business identifier](terminologies.html#unbound) --></identifier>
 <[**status**](clinicalimpression-definitions.html#ClinicalImpression.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [in-progress | completed | entered-in-error](valueset-clinicalimpression-status.html) -->
 <[**statusReason**](clinicalimpression-definitions.html#ClinicalImpression.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](terminologies.html#unbound) --></statusReason>
 <[**code**](clinicalimpression-definitions.html#ClinicalImpression.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of assessment performed](terminologies.html#unbound) --></code>
 <[**description**](clinicalimpression-definitions.html#ClinicalImpression.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Why/how the assessment was performed](terminologies.html#unbound) -->
 <[**subject**](clinicalimpression-definitions.html#ClinicalImpression.subject)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Patient or group assessed](terminologies.html#unbound) --></subject>
 <[**encounter**](clinicalimpression-definitions.html#ClinicalImpression.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**effective[x]**](clinicalimpression-definitions.html#ClinicalImpression.effective[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of assessment](terminologies.html#unbound) --></effective[x]>
 <[**date**](clinicalimpression-definitions.html#ClinicalImpression.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When the assessment was documented](terminologies.html#unbound) -->
 <[**assessor**](clinicalimpression-definitions.html#ClinicalImpression.assessor)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [The clinician performing the assessment](terminologies.html#unbound) --></assessor>
 <[**previous**](clinicalimpression-definitions.html#ClinicalImpression.previous)><!-- **0..1** [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)) [Reference to last assessment](terminologies.html#unbound) --></previous>
 <[**problem**](clinicalimpression-definitions.html#ClinicalImpression.problem)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)) [Relevant impressions of patient state](terminologies.html#unbound) --></problem>
 <[**investigation**](clinicalimpression-definitions.html#ClinicalImpression.investigation)> <!-- **0..*** One or more sets of investigations (signs, symptoms, etc.) -->
 <[**code**](clinicalimpression-definitions.html#ClinicalImpression.investigation.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [A name/code for the set](valueset-investigation-sets.html) --></code>
 <[**item**](clinicalimpression-definitions.html#ClinicalImpression.investigation.item)><!-- **0..*** [Reference](references.html#Reference)([Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|
 [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[RiskAssessment](riskassessment.html#RiskAssessment)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media)) [Record of a specific investigation](terminologies.html#unbound) --></item>
 </investigation>
 <[**protocol**](clinicalimpression-definitions.html#ClinicalImpression.protocol) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Clinical Protocol followed](terminologies.html#unbound) -->
 <[**summary**](clinicalimpression-definitions.html#ClinicalImpression.summary) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Summary of the assessment](terminologies.html#unbound) -->
 <[**finding**](clinicalimpression-definitions.html#ClinicalImpression.finding)> <!-- **0..*** Possible or likely findings and diagnoses -->
 <[**itemCodeableConcept**](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [What was found](valueset-condition-code.html) --></itemCodeableConcept>
 <[**itemReference**](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference)><!-- **0..1** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media)) [What was found](terminologies.html#unbound) --></itemReference>
 <[**basis**](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Which investigations support finding](terminologies.html#unbound) -->
 </finding>
 <[**prognosisCodeableConcept**](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Estimate of likely outcome](valueset-clinicalimpression-prognosis.html) --></prognosisCodeableConcept>
 <[**prognosisReference**](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference)><!-- **0..*** [Reference](references.html#Reference)([RiskAssessment](riskassessment.html#RiskAssessment)) [RiskAssessment expressing likely outcome](terminologies.html#unbound) --></prognosisReference>
 <[**supportingInfo**](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Information supporting the clinical impression](terminologies.html#unbound) --></supportingInfo>
 <[**note**](clinicalimpression-definitions.html#ClinicalImpression.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the ClinicalImpression](terminologies.html#unbound) --></note>
</ClinicalImpression>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**ClinicalImpression**](clinicalimpression-definitions.html#ClinicalImpression)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](clinicalimpression-definitions.html#ClinicalImpression.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business identifier](terminologies.html#unbound)
 "[status](clinicalimpression-definitions.html#ClinicalImpression.status)" : "<[code](datatypes.html#code)>", // **R!** [in-progress | completed | entered-in-error](valueset-clinicalimpression-status.html)
 "[statusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](terminologies.html#unbound)
 "[code](clinicalimpression-definitions.html#ClinicalImpression.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of assessment performed](terminologies.html#unbound)
 "[description](clinicalimpression-definitions.html#ClinicalImpression.description)" : "<[string](datatypes.html#string)>", // [Why/how the assessment was performed](terminologies.html#unbound)
 "[subject](clinicalimpression-definitions.html#ClinicalImpression.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Patient or group assessed](terminologies.html#unbound)
 "[encounter](clinicalimpression-definitions.html#ClinicalImpression.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 // effective[x]: Time of assessment. One of these 2:
 "[effectiveDateTime](clinicalimpression-definitions.html#ClinicalImpression.effectiveDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[effectivePeriod](clinicalimpression-definitions.html#ClinicalImpression.effectivePeriod)" : { [Period](datatypes.html#Period) },
 "[date](clinicalimpression-definitions.html#ClinicalImpression.date)" : "<[dateTime](datatypes.html#dateTime)>", // [When the assessment was documented](terminologies.html#unbound)
 "[assessor](clinicalimpression-definitions.html#ClinicalImpression.assessor)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [The clinician performing the assessment](terminologies.html#unbound)
 "[previous](clinicalimpression-definitions.html#ClinicalImpression.previous)" : { [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)) }, // [Reference to last assessment](terminologies.html#unbound)
 "[problem](clinicalimpression-definitions.html#ClinicalImpression.problem)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)) }], // [Relevant impressions of patient state](terminologies.html#unbound)
 "[investigation](clinicalimpression-definitions.html#ClinicalImpression.investigation)" : [{ // [One or more sets of investigations (signs, symptoms, etc.)](terminologies.html#unbound)
 "[code](clinicalimpression-definitions.html#ClinicalImpression.investigation.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [A name/code for the set](valueset-investigation-sets.html)
 "[item](clinicalimpression-definitions.html#ClinicalImpression.investigation.item)" : [{ [Reference](references.html#Reference)([Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|
 [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[RiskAssessment](riskassessment.html#RiskAssessment)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media)) }] // [Record of a specific investigation](terminologies.html#unbound)
 }],
 "[protocol](clinicalimpression-definitions.html#ClinicalImpression.protocol)" : ["<[uri](datatypes.html#uri)>"], // [Clinical Protocol followed](terminologies.html#unbound)
 "[summary](clinicalimpression-definitions.html#ClinicalImpression.summary)" : "<[string](datatypes.html#string)>", // [Summary of the assessment](terminologies.html#unbound)
 "[finding](clinicalimpression-definitions.html#ClinicalImpression.finding)" : [{ // [Possible or likely findings and diagnoses](terminologies.html#unbound)
 "[itemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [What was found](valueset-condition-code.html)
 "[itemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference)" : { [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media)) }, // [What was found](terminologies.html#unbound)
 "[basis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis)" : "<[string](datatypes.html#string)>" // [Which investigations support finding](terminologies.html#unbound)
 }],
 "[prognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Estimate of likely outcome](valueset-clinicalimpression-prognosis.html)
 "[prognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference)" : [{ [Reference](references.html#Reference)([RiskAssessment](riskassessment.html#RiskAssessment)) }], // [RiskAssessment expressing likely outcome](terminologies.html#unbound)
 "[supportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Information supporting the clinical impression](terminologies.html#unbound)
 "[note](clinicalimpression-definitions.html#ClinicalImpression.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about the ClinicalImpression](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**ClinicalImpression**](clinicalimpression-definitions.html#ClinicalImpression);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[ClinicalImpression.identifier](clinicalimpression-definitions.html#ClinicalImpression.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business identifier
 fhir:[ClinicalImpression.status](clinicalimpression-definitions.html#ClinicalImpression.status) [ [code](datatypes.html#code) ]; # 1..1 in-progress | completed | entered-in-error
 fhir:[ClinicalImpression.statusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[ClinicalImpression.code](clinicalimpression-definitions.html#ClinicalImpression.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of assessment performed
 fhir:[ClinicalImpression.description](clinicalimpression-definitions.html#ClinicalImpression.description) [ [string](datatypes.html#string) ]; # 0..1 Why/how the assessment was performed
 fhir:[ClinicalImpression.subject](clinicalimpression-definitions.html#ClinicalImpression.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Patient or group assessed
 fhir:[ClinicalImpression.encounter](clinicalimpression-definitions.html#ClinicalImpression.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 # [ClinicalImpression.effective[x]](clinicalimpression-definitions.html#ClinicalImpression.effective[x]) : 0..1 Time of assessment. One of these 2
 fhir:[ClinicalImpression.effectiveDateTime](clinicalimpression-definitions.html#ClinicalImpression.effectiveDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[ClinicalImpression.effectivePeriod](clinicalimpression-definitions.html#ClinicalImpression.effectivePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[ClinicalImpression.date](clinicalimpression-definitions.html#ClinicalImpression.date) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the assessment was documented
 fhir:[ClinicalImpression.assessor](clinicalimpression-definitions.html#ClinicalImpression.assessor) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 The clinician performing the assessment
 fhir:[ClinicalImpression.previous](clinicalimpression-definitions.html#ClinicalImpression.previous) [ [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)) ]; # 0..1 Reference to last assessment
 fhir:[ClinicalImpression.problem](clinicalimpression-definitions.html#ClinicalImpression.problem) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)) ], ... ; # 0..* Relevant impressions of patient state
 fhir:[ClinicalImpression.investigation](clinicalimpression-definitions.html#ClinicalImpression.investigation) [ # 0..* One or more sets of investigations (signs, symptoms, etc.)
 fhir:[ClinicalImpression.investigation.code](clinicalimpression-definitions.html#ClinicalImpression.investigation.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 A name/code for the set
 fhir:[ClinicalImpression.investigation.item](clinicalimpression-definitions.html#ClinicalImpression.investigation.item) [ [Reference](references.html#Reference)([Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [RiskAssessment](riskassessment.html#RiskAssessment)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media)) ], ... ; # 0..* Record of a specific investigation
 ], ...;
 fhir:[ClinicalImpression.protocol](clinicalimpression-definitions.html#ClinicalImpression.protocol) [ [uri](datatypes.html#uri) ], ... ; # 0..* Clinical Protocol followed
 fhir:[ClinicalImpression.summary](clinicalimpression-definitions.html#ClinicalImpression.summary) [ [string](datatypes.html#string) ]; # 0..1 Summary of the assessment
 fhir:[ClinicalImpression.finding](clinicalimpression-definitions.html#ClinicalImpression.finding) [ # 0..* Possible or likely findings and diagnoses
 fhir:[ClinicalImpression.finding.itemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 What was found
 fhir:[ClinicalImpression.finding.itemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media)) ]; # 0..1 What was found
 fhir:[ClinicalImpression.finding.basis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) [ [string](datatypes.html#string) ]; # 0..1 Which investigations support finding
 ], ...;
 fhir:[ClinicalImpression.prognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Estimate of likely outcome
 fhir:[ClinicalImpression.prognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference) [ [Reference](references.html#Reference)([RiskAssessment](riskassessment.html#RiskAssessment)) ], ... ; # 0..* RiskAssessment expressing likely outcome
 fhir:[ClinicalImpression.supportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Information supporting the clinical impression
 fhir:[ClinicalImpression.note](clinicalimpression-definitions.html#ClinicalImpression.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the ClinicalImpression
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [ClinicalImpression](clinicalimpression.html#ClinicalImpression)
 | 
 | 
 |

 | 
 ClinicalImpression.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/clinical-impression-status to http://hl7.org/fhir/ValueSet/clinicalimpression-status|4.0.1

 

 | 
 |

 | 
 ClinicalImpression.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.assessor | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 ClinicalImpression.investigation.item | 
 
 

 - Type Reference: Added Target Type Media

 

 | 
 |

 | 
 ClinicalImpression.finding.itemCodeableConcept | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.finding.itemReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.supportingInfo | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.context | 
 
 

 - deleted

 

 | 
 |

 | 
 ClinicalImpression.finding.item[x] | 
 
 

 - deleted

 

 | 
 |

 | 
 ClinicalImpression.action | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](clinicalimpression.diff.xml) or [JSON](clinicalimpression.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](clinicalimpression-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [ClinicalImpression](clinicalimpression-definitions.html#ClinicalImpression) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A clinical assessment performed when planning treatments and management strategies for a patient**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](clinicalimpression-definitions.html#ClinicalImpression.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business identifier
 | |

| [status](clinicalimpression-definitions.html#ClinicalImpression.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | in-progress | completed | entered-in-error
[Clinical Impression Status](valueset-clinicalimpression-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status | |

| [code](clinicalimpression-definitions.html#ClinicalImpression.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of assessment performed | |

| [description](clinicalimpression-definitions.html#ClinicalImpression.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Why/how the assessment was performed | |

| [subject](clinicalimpression-definitions.html#ClinicalImpression.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Patient or group assessed | |

| [encounter](clinicalimpression-definitions.html#ClinicalImpression.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [effective[x]](clinicalimpression-definitions.html#ClinicalImpression.effective_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Time of assessment | |

| effectiveDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| effectivePeriod | | | [Period](datatypes.html#Period) | | |

| [date](clinicalimpression-definitions.html#ClinicalImpression.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When the assessment was documented | |

| [assessor](clinicalimpression-definitions.html#ClinicalImpression.assessor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | The clinician performing the assessment | |

| [previous](clinicalimpression-definitions.html#ClinicalImpression.previous) | | 0..1 | [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html)) | Reference to last assessment | |

| [problem](clinicalimpression-definitions.html#ClinicalImpression.problem) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [AllergyIntolerance](allergyintolerance.html)) | Relevant impressions of patient state
 | |

| [investigation](clinicalimpression-definitions.html#ClinicalImpression.investigation) | | 0..* | [BackboneElement](backboneelement.html) | One or more sets of investigations (signs, symptoms, etc.)
 | |

| [code](clinicalimpression-definitions.html#ClinicalImpression.investigation.code) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | A name/code for the set
[Investigation Type](valueset-investigation-sets.html) ([Example](terminologies.html#example)) | |

| [item](clinicalimpression-definitions.html#ClinicalImpression.investigation.item) | | 0..* | [Reference](references.html#Reference)([Observation](observation.html) | [QuestionnaireResponse](questionnaireresponse.html) | [FamilyMemberHistory](familymemberhistory.html) | [DiagnosticReport](diagnosticreport.html) | [RiskAssessment](riskassessment.html) | [ImagingStudy](imagingstudy.html) | [Media](media.html)) | Record of a specific investigation
 | |

| [protocol](clinicalimpression-definitions.html#ClinicalImpression.protocol) | | 0..* | [uri](datatypes.html#uri) | Clinical Protocol followed
 | |

| [summary](clinicalimpression-definitions.html#ClinicalImpression.summary) | | 0..1 | [string](datatypes.html#string) | Summary of the assessment | |

| [finding](clinicalimpression-definitions.html#ClinicalImpression.finding) | | 0..* | [BackboneElement](backboneelement.html) | Possible or likely findings and diagnoses
 | |

| [itemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What was found
[Condition/Problem/Diagnosis Codes](valueset-condition-code.html) ([Example](terminologies.html#example)) | |

| [itemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference) | | 0..1 | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [Media](media.html)) | What was found | |

| [basis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) | | 0..1 | [string](datatypes.html#string) | Which investigations support finding | |

| [prognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Estimate of likely outcome
[Clinical Impression Prognosis](valueset-clinicalimpression-prognosis.html) ([Example](terminologies.html#example))
 | |

| [prognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference) | | 0..* | [Reference](references.html#Reference)([RiskAssessment](riskassessment.html)) | RiskAssessment expressing likely outcome
 | |

| [supportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Information supporting the clinical impression
 | |

| [note](clinicalimpression-definitions.html#ClinicalImpression.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the ClinicalImpression
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - ClinicalImpression ([DomainResource](domainresource.html))[Business identifiers assigned to this clinical impression by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](clinicalimpression-definitions.html#ClinicalImpression.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Identifies the workflow status of the assessment (this element modifies the meaning of other elements)status](clinicalimpression-definitions.html#ClinicalImpression.status) : [code](datatypes.html#code) [1..1] « [The workflow state of a clinical impression. (Strength=Required)ClinicalImpressionStatus](valueset-clinicalimpression-status.html)! »[Captures the reason for the current state of the ClinicalImpressionstatusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Categorizes the type of clinical assessment performedcode](clinicalimpression-definitions.html#ClinicalImpression.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][A summary of the context and/or cause of the assessment - why / where it was performed, and what patient events/status prompted itdescription](clinicalimpression-definitions.html#ClinicalImpression.description) : [string](datatypes.html#string) [0..1][The patient or group of individuals assessed as part of this recordsubject](clinicalimpression-definitions.html#ClinicalImpression.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this ClinicalImpression was created or to which the creation of this record is tightly associatedencounter](clinicalimpression-definitions.html#ClinicalImpression.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The point in time or period over which the subject was assessedeffective[x]](clinicalimpression-definitions.html#ClinicalImpression.effective_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »[Indicates when the documentation of the assessment was completedate](clinicalimpression-definitions.html#ClinicalImpression.date) : [dateTime](datatypes.html#dateTime) [0..1][The clinician performing the assessmentassessor](clinicalimpression-definitions.html#ClinicalImpression.assessor) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[A reference to the last assessment that was conducted on this patient. Assessments are often/usually ongoing in nature; a care provider (practitioner or team) will make new assessments on an ongoing basis as new data arises or the patient's conditions changesprevious](clinicalimpression-definitions.html#ClinicalImpression.previous) : [Reference](references.html#Reference) [0..1] « [ClinicalImpression](clinicalimpression.html#ClinicalImpression) »[A list of the relevant problems/conditions for a patientproblem](clinicalimpression-definitions.html#ClinicalImpression.problem) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance) »[Reference to a specific published clinical protocol that was followed during this assessment, and/or that provides evidence in support of the diagnosisprotocol](clinicalimpression-definitions.html#ClinicalImpression.protocol) : [uri](datatypes.html#uri) [0..*][A text summary of the investigations and the diagnosissummary](clinicalimpression-definitions.html#ClinicalImpression.summary) : [string](datatypes.html#string) [0..1][Estimate of likely outcomeprognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Prognosis or outlook findings. (Strength=Example)](valueset-clinicalimpression-prognosis.html) [ClinicalImpressionPrognosis](valueset-clinicalimpression-prognosis.html)?? »[RiskAssessment expressing likely outcomeprognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference) : [Reference](references.html#Reference) [0..*] « [RiskAssessment](riskassessment.html#RiskAssessment) »[Information supporting the clinical impressionsupportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Commentary about the impression, typically recorded after the impression itself was made, though supplemental notes by the original author could also appearnote](clinicalimpression-definitions.html#ClinicalImpression.note) : [Annotation](datatypes.html#Annotation) [0..*]Investigation[A name/code for the group ("set") of investigations. Typically, this will be something like "signs", "symptoms", "clinical", "diagnostic", but the list is not constrained, and others such groups such as (exposure|family|travel|nutritional) history may be usedcode](clinicalimpression-definitions.html#ClinicalImpression.investigation.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [A name/code for a set of investigations. (Strength=Example)InvestigationType](valueset-investigation-sets.html)?? »[A record of a specific investigation that was undertakenitem](clinicalimpression-definitions.html#ClinicalImpression.investigation.item) : [Reference](references.html#Reference) [0..*] « [Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)| [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[RiskAssessment](riskassessment.html#RiskAssessment)| [ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media) »Finding[Specific text or code for finding or diagnosis, which may include ruled-out or resolved conditionsitemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identification of the Condition or diagnosis. (Strength=Example)](valueset-condition-code.html) [Condition/Problem/DiagnosisCo...](valueset-condition-code.html)?? »[Specific reference for finding or diagnosis, which may include ruled-out or resolved conditionsitemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference) : [Reference](references.html#Reference) [0..1] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media) »[Which investigations support finding or diagnosisbasis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) : [string](datatypes.html#string) [0..1]
[One or more sets of investigations (signs, symptoms, etc.). The actual grouping of investigations varies greatly depending on the type and context of the assessment. These investigations may include data generated during the assessment process, or data previously generated and recorded that is pertinent to the outcomesinvestigation](clinicalimpression-definitions.html#ClinicalImpression.investigation)[0..*][Specific findings or diagnoses that were considered likely or relevant to ongoing treatmentfinding](clinicalimpression-definitions.html#ClinicalImpression.finding)[0..*]
 

**XML Template**

 

 
```
<[**ClinicalImpression**](clinicalimpression-definitions.html#ClinicalImpression) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](clinicalimpression-definitions.html#ClinicalImpression.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business identifier](terminologies.html#unbound) --></identifier>
 <[**status**](clinicalimpression-definitions.html#ClinicalImpression.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [in-progress | completed | entered-in-error](valueset-clinicalimpression-status.html) -->
 <[**statusReason**](clinicalimpression-definitions.html#ClinicalImpression.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](terminologies.html#unbound) --></statusReason>
 <[**code**](clinicalimpression-definitions.html#ClinicalImpression.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of assessment performed](terminologies.html#unbound) --></code>
 <[**description**](clinicalimpression-definitions.html#ClinicalImpression.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Why/how the assessment was performed](terminologies.html#unbound) -->
 <[**subject**](clinicalimpression-definitions.html#ClinicalImpression.subject)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Patient or group assessed](terminologies.html#unbound) --></subject>
 <[**encounter**](clinicalimpression-definitions.html#ClinicalImpression.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**effective[x]**](clinicalimpression-definitions.html#ClinicalImpression.effective[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [Time of assessment](terminologies.html#unbound) --></effective[x]>
 <[**date**](clinicalimpression-definitions.html#ClinicalImpression.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When the assessment was documented](terminologies.html#unbound) -->
 <[**assessor**](clinicalimpression-definitions.html#ClinicalImpression.assessor)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [The clinician performing the assessment](terminologies.html#unbound) --></assessor>
 <[**previous**](clinicalimpression-definitions.html#ClinicalImpression.previous)><!-- **0..1** [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)) [Reference to last assessment](terminologies.html#unbound) --></previous>
 <[**problem**](clinicalimpression-definitions.html#ClinicalImpression.problem)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)) [Relevant impressions of patient state](terminologies.html#unbound) --></problem>
 <[**investigation**](clinicalimpression-definitions.html#ClinicalImpression.investigation)> <!-- **0..*** One or more sets of investigations (signs, symptoms, etc.) -->
 <[**code**](clinicalimpression-definitions.html#ClinicalImpression.investigation.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [A name/code for the set](valueset-investigation-sets.html) --></code>
 <[**item**](clinicalimpression-definitions.html#ClinicalImpression.investigation.item)><!-- **0..*** [Reference](references.html#Reference)([Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|
 [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[RiskAssessment](riskassessment.html#RiskAssessment)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media)) [Record of a specific investigation](terminologies.html#unbound) --></item>
 </investigation>
 <[**protocol**](clinicalimpression-definitions.html#ClinicalImpression.protocol) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Clinical Protocol followed](terminologies.html#unbound) -->
 <[**summary**](clinicalimpression-definitions.html#ClinicalImpression.summary) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Summary of the assessment](terminologies.html#unbound) -->
 <[**finding**](clinicalimpression-definitions.html#ClinicalImpression.finding)> <!-- **0..*** Possible or likely findings and diagnoses -->
 <[**itemCodeableConcept**](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [What was found](valueset-condition-code.html) --></itemCodeableConcept>
 <[**itemReference**](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference)><!-- **0..1** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media)) [What was found](terminologies.html#unbound) --></itemReference>
 <[**basis**](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Which investigations support finding](terminologies.html#unbound) -->
 </finding>
 <[**prognosisCodeableConcept**](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Estimate of likely outcome](valueset-clinicalimpression-prognosis.html) --></prognosisCodeableConcept>
 <[**prognosisReference**](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference)><!-- **0..*** [Reference](references.html#Reference)([RiskAssessment](riskassessment.html#RiskAssessment)) [RiskAssessment expressing likely outcome](terminologies.html#unbound) --></prognosisReference>
 <[**supportingInfo**](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Information supporting the clinical impression](terminologies.html#unbound) --></supportingInfo>
 <[**note**](clinicalimpression-definitions.html#ClinicalImpression.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the ClinicalImpression](terminologies.html#unbound) --></note>
</ClinicalImpression>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**ClinicalImpression**](clinicalimpression-definitions.html#ClinicalImpression)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](clinicalimpression-definitions.html#ClinicalImpression.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business identifier](terminologies.html#unbound)
 "[status](clinicalimpression-definitions.html#ClinicalImpression.status)" : "<[code](datatypes.html#code)>", // **R!** [in-progress | completed | entered-in-error](valueset-clinicalimpression-status.html)
 "[statusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](terminologies.html#unbound)
 "[code](clinicalimpression-definitions.html#ClinicalImpression.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of assessment performed](terminologies.html#unbound)
 "[description](clinicalimpression-definitions.html#ClinicalImpression.description)" : "<[string](datatypes.html#string)>", // [Why/how the assessment was performed](terminologies.html#unbound)
 "[subject](clinicalimpression-definitions.html#ClinicalImpression.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Patient or group assessed](terminologies.html#unbound)
 "[encounter](clinicalimpression-definitions.html#ClinicalImpression.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 // effective[x]: Time of assessment. One of these 2:
 "[effectiveDateTime](clinicalimpression-definitions.html#ClinicalImpression.effectiveDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[effectivePeriod](clinicalimpression-definitions.html#ClinicalImpression.effectivePeriod)" : { [Period](datatypes.html#Period) },
 "[date](clinicalimpression-definitions.html#ClinicalImpression.date)" : "<[dateTime](datatypes.html#dateTime)>", // [When the assessment was documented](terminologies.html#unbound)
 "[assessor](clinicalimpression-definitions.html#ClinicalImpression.assessor)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [The clinician performing the assessment](terminologies.html#unbound)
 "[previous](clinicalimpression-definitions.html#ClinicalImpression.previous)" : { [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)) }, // [Reference to last assessment](terminologies.html#unbound)
 "[problem](clinicalimpression-definitions.html#ClinicalImpression.problem)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)) }], // [Relevant impressions of patient state](terminologies.html#unbound)
 "[investigation](clinicalimpression-definitions.html#ClinicalImpression.investigation)" : [{ // [One or more sets of investigations (signs, symptoms, etc.)](terminologies.html#unbound)
 "[code](clinicalimpression-definitions.html#ClinicalImpression.investigation.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [A name/code for the set](valueset-investigation-sets.html)
 "[item](clinicalimpression-definitions.html#ClinicalImpression.investigation.item)" : [{ [Reference](references.html#Reference)([Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|
 [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[RiskAssessment](riskassessment.html#RiskAssessment)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media)) }] // [Record of a specific investigation](terminologies.html#unbound)
 }],
 "[protocol](clinicalimpression-definitions.html#ClinicalImpression.protocol)" : ["<[uri](datatypes.html#uri)>"], // [Clinical Protocol followed](terminologies.html#unbound)
 "[summary](clinicalimpression-definitions.html#ClinicalImpression.summary)" : "<[string](datatypes.html#string)>", // [Summary of the assessment](terminologies.html#unbound)
 "[finding](clinicalimpression-definitions.html#ClinicalImpression.finding)" : [{ // [Possible or likely findings and diagnoses](terminologies.html#unbound)
 "[itemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [What was found](valueset-condition-code.html)
 "[itemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference)" : { [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media)) }, // [What was found](terminologies.html#unbound)
 "[basis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis)" : "<[string](datatypes.html#string)>" // [Which investigations support finding](terminologies.html#unbound)
 }],
 "[prognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Estimate of likely outcome](valueset-clinicalimpression-prognosis.html)
 "[prognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference)" : [{ [Reference](references.html#Reference)([RiskAssessment](riskassessment.html#RiskAssessment)) }], // [RiskAssessment expressing likely outcome](terminologies.html#unbound)
 "[supportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Information supporting the clinical impression](terminologies.html#unbound)
 "[note](clinicalimpression-definitions.html#ClinicalImpression.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about the ClinicalImpression](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**ClinicalImpression**](clinicalimpression-definitions.html#ClinicalImpression);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[ClinicalImpression.identifier](clinicalimpression-definitions.html#ClinicalImpression.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business identifier
 fhir:[ClinicalImpression.status](clinicalimpression-definitions.html#ClinicalImpression.status) [ [code](datatypes.html#code) ]; # 1..1 in-progress | completed | entered-in-error
 fhir:[ClinicalImpression.statusReason](clinicalimpression-definitions.html#ClinicalImpression.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[ClinicalImpression.code](clinicalimpression-definitions.html#ClinicalImpression.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of assessment performed
 fhir:[ClinicalImpression.description](clinicalimpression-definitions.html#ClinicalImpression.description) [ [string](datatypes.html#string) ]; # 0..1 Why/how the assessment was performed
 fhir:[ClinicalImpression.subject](clinicalimpression-definitions.html#ClinicalImpression.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Patient or group assessed
 fhir:[ClinicalImpression.encounter](clinicalimpression-definitions.html#ClinicalImpression.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 # [ClinicalImpression.effective[x]](clinicalimpression-definitions.html#ClinicalImpression.effective[x]) : 0..1 Time of assessment. One of these 2
 fhir:[ClinicalImpression.effectiveDateTime](clinicalimpression-definitions.html#ClinicalImpression.effectiveDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[ClinicalImpression.effectivePeriod](clinicalimpression-definitions.html#ClinicalImpression.effectivePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[ClinicalImpression.date](clinicalimpression-definitions.html#ClinicalImpression.date) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the assessment was documented
 fhir:[ClinicalImpression.assessor](clinicalimpression-definitions.html#ClinicalImpression.assessor) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 The clinician performing the assessment
 fhir:[ClinicalImpression.previous](clinicalimpression-definitions.html#ClinicalImpression.previous) [ [Reference](references.html#Reference)([ClinicalImpression](clinicalimpression.html#ClinicalImpression)) ]; # 0..1 Reference to last assessment
 fhir:[ClinicalImpression.problem](clinicalimpression-definitions.html#ClinicalImpression.problem) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)) ], ... ; # 0..* Relevant impressions of patient state
 fhir:[ClinicalImpression.investigation](clinicalimpression-definitions.html#ClinicalImpression.investigation) [ # 0..* One or more sets of investigations (signs, symptoms, etc.)
 fhir:[ClinicalImpression.investigation.code](clinicalimpression-definitions.html#ClinicalImpression.investigation.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 A name/code for the set
 fhir:[ClinicalImpression.investigation.item](clinicalimpression-definitions.html#ClinicalImpression.investigation.item) [ [Reference](references.html#Reference)([Observation](observation.html#Observation)|[QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [RiskAssessment](riskassessment.html#RiskAssessment)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Media](media.html#Media)) ], ... ; # 0..* Record of a specific investigation
 ], ...;
 fhir:[ClinicalImpression.protocol](clinicalimpression-definitions.html#ClinicalImpression.protocol) [ [uri](datatypes.html#uri) ], ... ; # 0..* Clinical Protocol followed
 fhir:[ClinicalImpression.summary](clinicalimpression-definitions.html#ClinicalImpression.summary) [ [string](datatypes.html#string) ]; # 0..1 Summary of the assessment
 fhir:[ClinicalImpression.finding](clinicalimpression-definitions.html#ClinicalImpression.finding) [ # 0..* Possible or likely findings and diagnoses
 fhir:[ClinicalImpression.finding.itemCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.finding.itemCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 What was found
 fhir:[ClinicalImpression.finding.itemReference](clinicalimpression-definitions.html#ClinicalImpression.finding.itemReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[Media](media.html#Media)) ]; # 0..1 What was found
 fhir:[ClinicalImpression.finding.basis](clinicalimpression-definitions.html#ClinicalImpression.finding.basis) [ [string](datatypes.html#string) ]; # 0..1 Which investigations support finding
 ], ...;
 fhir:[ClinicalImpression.prognosisCodeableConcept](clinicalimpression-definitions.html#ClinicalImpression.prognosisCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Estimate of likely outcome
 fhir:[ClinicalImpression.prognosisReference](clinicalimpression-definitions.html#ClinicalImpression.prognosisReference) [ [Reference](references.html#Reference)([RiskAssessment](riskassessment.html#RiskAssessment)) ], ... ; # 0..* RiskAssessment expressing likely outcome
 fhir:[ClinicalImpression.supportingInfo](clinicalimpression-definitions.html#ClinicalImpression.supportingInfo) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Information supporting the clinical impression
 fhir:[ClinicalImpression.note](clinicalimpression-definitions.html#ClinicalImpression.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the ClinicalImpression
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [ClinicalImpression](clinicalimpression.html#ClinicalImpression)
 | 
 | 
 |

 | 
 ClinicalImpression.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/clinical-impression-status to http://hl7.org/fhir/ValueSet/clinicalimpression-status|4.0.1

 

 | 
 |

 | 
 ClinicalImpression.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.assessor | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 ClinicalImpression.investigation.item | 
 
 

 - Type Reference: Added Target Type Media

 

 | 
 |

 | 
 ClinicalImpression.finding.itemCodeableConcept | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.finding.itemReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.supportingInfo | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClinicalImpression.context | 
 
 

 - deleted

 

 | 
 |

 | 
 ClinicalImpression.finding.item[x] | 
 
 

 - deleted

 

 | 
 |

 | 
 ClinicalImpression.action | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](clinicalimpression.diff.xml) or [JSON](clinicalimpression.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](clinicalimpression-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](clinicalimpression-profiles.html) and the alternate definitions:
Master Definition [XML](clinicalimpression.profile.xml.html) + [JSON](clinicalimpression.profile.json.html),
[XML](xml.html) [Schema](clinicalimpression.xsd)/[Schematron](clinicalimpression.sch) + [JSON](json.html) 
[Schema](clinicalimpression.schema.json.html), [ShEx](clinicalimpression.shex.html) (for [Turtle](rdf.html)) + [see the extensions](clinicalimpression-profiles.html) & the [dependency analysis](clinicalimpression-dependencies.html)

### 9.8.4.1 
Terminology Bindings
 [
](clinicalimpression.html#tx)

 | Path | Definition | Type | Reference | |

 | ClinicalImpression.status | The workflow state of a clinical impression. | [Required](terminologies.html#required) | [ClinicalImpressionStatus](valueset-clinicalimpression-status.html) | |

 | ClinicalImpression.statusReason | Codes identifying the reason for the current state of a clinical impression. | Unknown | No details provided yet | |

 | ClinicalImpression.code | Identifies categories of clinical impressions. This is a place-holder only. It may be removed. | Unknown | No details provided yet | |

 | ClinicalImpression.investigation.code | A name/code for a set of investigations. | [Example](terminologies.html#example) | [InvestigationType](valueset-investigation-sets.html) | |

 | ClinicalImpression.finding.itemCodeableConcept | Identification of the Condition or diagnosis. | [Example](terminologies.html#example) | [Condition/Problem/DiagnosisCodes](valueset-condition-code.html) | |

 | ClinicalImpression.prognosisCodeableConcept | Prognosis or outlook findings. | [Example](terminologies.html#example) | [ClinicalImpressionPrognosis](valueset-clinicalimpression-prognosis.html) | |

 

### 9.8.4.2 Known Issue [
](clinicalimpression.html#9.8.4.2)

 A known issue exists with circular references between Condition and ClinicalImpression, which is due to the low maturity level of ClinicalImpression. The Patient Care work group intends to address this issue when ClinicalImpression is considered substantially complete and ready for implementation.

## 9.8.5 Search Parameters [
](clinicalimpression.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| assessor | [reference](search.html#reference) | The clinician performing the assessment | ClinicalImpression.assessor
([Practitioner](practitioner.html), [PractitionerRole](practitionerrole.html)) | | |

| date | [date](search.html#date) | When the assessment was documented | ClinicalImpression.date | [17 Resources](searchparameter-registry.html#clinical-date) | |

| encounter | [reference](search.html#reference) | Encounter created as part of | ClinicalImpression.encounter
([Encounter](encounter.html)) | | |

| finding-code | [token](search.html#token) | What was found | ClinicalImpression.finding.itemCodeableConcept | | |

| finding-ref | [reference](search.html#reference) | What was found | ClinicalImpression.finding.itemReference
([Condition](condition.html), [Observation](observation.html), [Media](media.html)) | | |

| identifier | [token](search.html#token) | Business identifier | ClinicalImpression.identifier | | |

| investigation | [reference](search.html#reference) | Record of a specific investigation | ClinicalImpression.investigation.item
([RiskAssessment](riskassessment.html), [FamilyMemberHistory](familymemberhistory.html), [Observation](observation.html), [Media](media.html), [DiagnosticReport](diagnosticreport.html), [ImagingStudy](imagingstudy.html), [QuestionnaireResponse](questionnaireresponse.html)) | | |

| patient | [reference](search.html#reference) | Patient or group assessed | ClinicalImpression.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| previous | [reference](search.html#reference) | Reference to last assessment | ClinicalImpression.previous
([ClinicalImpression](clinicalimpression.html)) | | |

| problem | [reference](search.html#reference) | Relevant impressions of patient state | ClinicalImpression.problem
([Condition](condition.html), [AllergyIntolerance](allergyintolerance.html)) | | |

| status | [token](search.html#token) | in-progress | completed | entered-in-error | ClinicalImpression.status | | |

| subject | [reference](search.html#reference) | Patient or group assessed | ClinicalImpression.subject
([Group](group.html), [Patient](patient.html)) | | |

| supporting-info | [reference](search.html#reference) | Information supporting the clinical impression | ClinicalImpression.supportingInfo
(Any) | | |