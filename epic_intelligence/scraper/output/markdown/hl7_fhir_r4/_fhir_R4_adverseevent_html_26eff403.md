# AdverseEvent - FHIR v4.0.1Business identifiers assigned to this adverse event by the performer or other systems which remain constant as the resource is updated and propagates from server to serverWhether the event actually happened, or just had the potential to. Note that this is independent of whether anyone was affected or harmed or how severely (this element modifies the meaning of other elements)Overall nature of the adverse event, e.g. real or potential. (Strength=Required)The overall type of event, intended for search and filtering purposesOverall categorization of the event, e.g. product-related or situational. (Strength=Extensible)This element defines the specific type of event that occurred or that was prevented from occurringDetailed type of event. (Strength=Example)This subject or group impacted by the eventThe Encounter during which AdverseEvent was created or to which the creation of this record is tightly associatedThe date (and perhaps time) when the adverse event occurredEstimated or actual date the AdverseEvent began, in the opinion of the reporterThe date on which the existence of the AdverseEvent was first recordedIncludes information about the reaction that occurred as a result of exposure to a substance (for example, a drug or a chemical)The information about where the adverse event occurredAssessment whether this event was of real importanceOverall seriousness of this event for the patient. (Strength=Example)Describes the severity of the adverse event, in relation to the subject. Contrast to AdverseEvent.seriousness - a severe rash might not be serious, but a mild heart problem isThe severity of the adverse event itself, in direct relation to the subject. (Strength=Required)Describes the type of outcome from the adverse eventTODO (and should this be required?). (Strength=Required)Information on who recorded the adverse event.  May be the patient or a practitionerParties that may or should contribute or have contributed information to the adverse event, which can consist of one or more activities.  Such information includes information leading to the decision to perform the activity and how to perform the activity (e.g. consultant), information that the activity itself seeks to reveal (e.g. informant of clinical history), or information about what activity was performed (e.g. informant witness)AdverseEvent.subjectMedicalHistoryAdverseEvent.referenceDocumentAdverseEvent.studyIdentifies the actual instance of what caused the adverse event.  May be a substance, medication, medication administration, medication statement or a deviceAssessment of if the entity caused the eventCodes for the assessment of whether the entity caused the event. (Strength=Example)AdverseEvent.suspectEntity.causalityProductRelatednessAdverseEvent.suspectEntity.causalityAuthorProbabilityScale | Bayesian | ChecklistTODO. (Strength=Example)Information on the possible cause of the eventDescribes the entity that is suspected to have caused the adverse eventBusiness identifiers assigned to this adverse event by the performer or other systems which remain constant as the resource is updated and propagates from server to serverWhether the event actually happened, or just had the potential to. Note that this is independent of whether anyone was affected or harmed or how severely (this element modifies the meaning of other elements)Overall nature of the adverse event, e.g. real or potential. (Strength=Required)The overall type of event, intended for search and filtering purposesOverall categorization of the event, e.g. product-related or situational. (Strength=Extensible)This element defines the specific type of event that occurred or that was prevented from occurringDetailed type of event. (Strength=Example)This subject or group impacted by the eventThe Encounter during which AdverseEvent was created or to which the creation of this record is tightly associatedThe date (and perhaps time) when the adverse event occurredEstimated or actual date the AdverseEvent began, in the opinion of the reporterThe date on which the existence of the AdverseEvent was first recordedIncludes information about the reaction that occurred as a result of exposure to a substance (for example, a drug or a chemical)The information about where the adverse event occurredAssessment whether this event was of real importanceOverall seriousness of this event for the patient. (Strength=Example)Describes the severity of the adverse event, in relation to the subject. Contrast to AdverseEvent.seriousness - a severe rash might not be serious, but a mild heart problem isThe severity of the adverse event itself, in direct relation to the subject. (Strength=Required)Describes the type of outcome from the adverse eventTODO (and should this be required?). (Strength=Required)Information on who recorded the adverse event.  May be the patient or a practitionerParties that may or should contribute or have contributed information to the adverse event, which can consist of one or more activities.  Such information includes information leading to the decision to perform the activity and how to perform the activity (e.g. consultant), information that the activity itself seeks to reveal (e.g. informant of clinical history), or information about what activity was performed (e.g. informant witness)AdverseEvent.subjectMedicalHistoryAdverseEvent.referenceDocumentAdverseEvent.studyIdentifies the actual instance of what caused the adverse event.  May be a substance, medication, medication administration, medication statement or a deviceAssessment of if the entity caused the eventCodes for the assessment of whether the entity caused the event. (Strength=Example)AdverseEvent.suspectEntity.causalityProductRelatednessAdverseEvent.suspectEntity.causalityAuthorProbabilityScale | Bayesian | ChecklistTODO. (Strength=Example)Information on the possible cause of the eventDescribes the entity that is suspected to have caused the adverse event

> Source: https://hl7.org/fhir/R4/adverseevent.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/adverseevent.html) [R4B](http://hl7.org/fhir/R4B/adverseevent.html) **R4** [R3](http://hl7.org/fhir/STU3/adverseevent.html)
 

# 9.9 Resource AdverseEvent - Content [
](adverseevent.html#9.9)

| [Patient Care ](http://www.hl7.org/Special/committees/patientcare/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 0 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

Actual or potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death.

 
 
## 9.9.1 Scope and Usage [
](adverseevent.html#scope)

 
 AdverseEvent is an event resource from a FHIR workflow perspective - see [Workflow Event](workflow.html#event)
 

 

 This resource applies to events that occur during the course of medical care or medical research which may impact an individual as the recipient of care or the participant in a research study. There are also events that occur within a care setting that might or might not impact an individual but had the potential to cause an adverse event. Health care organizations monitor and report both adverse events as well as events that had the potential to cause patient harm. Data are often aggregated for reporting purposes. 
 

 

 An adverse event is the result of an intervention that caused unintentional harm to a specific subject or group of subjects. Examples of adverse events include the administration of an incorrect drug or an incorrect dose of a drug causing an adverse reaction, the use of an implanted device that causes an infection, or a biologic used during a research study that causes unanticipated renal failure. These events are characterized by the need to capture cause and effect (although they might not be known at the time of the event), severity, and outcome. 
 

 

 The context of an adverse event is also important. A subject may have condition(s) or current treatments (medications, diet, devices) that impact their response to a newly introduced medication, device or procedure. Knowledge of these variables is essential in establishing a cause and effect relationship for an adverse event. 
 

 

 A potential adverse event may also be called a near miss or an error. These are also events but because they were detected did not cause harm to a subject. Examples of potential adverse events include a product problem such as a faulty pacemaker that is detected prior implantation, a doctor working simultaneously on two electronic health records realizing the order for a drug was entered on the incorrect patient and then canceling the order, or a patient with a peanut allergy notices that his hospital dinner tray includes peanuts, and he does not eat the peanuts. 
 

 

 

 
 
## 9.9.2 Boundaries and Relationships [
](adverseevent.html#bnr)

 
 The AdverseEvent resource is designed to represent events that have a harmful impact on a subject, or had the potential to cause harm to a subject but were avoided. In the course of medical care there are many actions that may impact how a subject responds to a particular treatment impacting patient safety. Therefore the AdverseEvent resource may reference multiple other resources to represent the context or details of an adverse event including but not limited to Observation, Condition, MedicationAdminsitration, Immunization, Procedure, or ResearchStudy. 
 

 

 A DetectedIssue reference is also related to the context of an AdverseEvent to the extent that a known risk for a potential issue such as a drug-drug interaction is documented. If in the context of a known issue, and adverse event occurs, citing this relationship is important for preventing such an occurrence in the future.
 

 

 The AdverseEvent resource should not be used when a more specific resource exists. 
 

 

 - The AllergyIntolerance resource is a case specific means of capturing the condition of an allergy or intolerance and the criticality (or potential for future harm) based on the response of a particular individual.

 - The Clinical Reasoning module provides resources and operations to enable the representation, distribution, and evaluation of clinical knowledge artifacts such as clinical decision support rules, quality measures, order sets, and protocols. The suite of resources within the clinical reasoning module should be used to capture clinical quality measures and clinical protocols that help drive clinical best practices.

 - The AdverseEvent resource is not intended to be used to capture potential subject risk in a prospective manner. A more appropriate resource for this purpose would be Risk Assessment which captures predicted outcomes for a patient or population on the basis of source information. Examples include a prognosis statement for a particular condition, risk of health outcome (heart attack, particular type of cancer) on the basis of lifestyle factors and/or family history or list of potential health risks based on a patient's genetic analysis.

 

 

## 9.9.3 
Resource Content
 [
](adverseevent.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [AdverseEvent](adverseevent-definitions.html#AdverseEvent) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Medical care, research study or other healthcare event causing physical injury**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](adverseevent-definitions.html#AdverseEvent.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Business identifier for the event | |

| [actuality](adverseevent-definitions.html#AdverseEvent.actuality) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | actual | potential
[AdverseEventActuality](valueset-adverse-event-actuality.html) ([Required](terminologies.html#required)) | |

| [category](adverseevent-definitions.html#AdverseEvent.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | product-problem | product-quality | product-use-error | wrong-dose | incorrect-prescribing-information | wrong-technique | wrong-route-of-administration | wrong-rate | wrong-duration | wrong-time | expired-drug | medical-device-use-error | problem-different-manufacturer | unsafe-physical-environment
[AdverseEventCategory](valueset-adverse-event-category.html) ([Extensible](terminologies.html#extensible))
 | |

| [event](adverseevent-definitions.html#AdverseEvent.event) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of the event itself in relation to the subject
[SNOMED CT Clinical Findings](valueset-adverse-event-type.html) ([Example](terminologies.html#example)) | |

| [subject](adverseevent-definitions.html#AdverseEvent.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html) | [Practitioner](practitioner.html) | [RelatedPerson](relatedperson.html)) | Subject impacted by event | |

| [encounter](adverseevent-definitions.html#AdverseEvent.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [date](adverseevent-definitions.html#AdverseEvent.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When the event occurred | |

| [detected](adverseevent-definitions.html#AdverseEvent.detected) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When the event was detected | |

| [recordedDate](adverseevent-definitions.html#AdverseEvent.recordedDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When the event was recorded | |

| [resultingCondition](adverseevent-definitions.html#AdverseEvent.resultingCondition) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html)) | Effect on the subject due to this event
 | |

| [location](adverseevent-definitions.html#AdverseEvent.location) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Location where adverse event occurred | |

| [seriousness](adverseevent-definitions.html#AdverseEvent.seriousness) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Seriousness of the event
[AdverseEventSeriousness](valueset-adverse-event-seriousness.html) ([Example](terminologies.html#example)) | |

| [severity](adverseevent-definitions.html#AdverseEvent.severity) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | mild | moderate | severe
[AdverseEventSeverity](valueset-adverse-event-severity.html) ([Required](terminologies.html#required)) | |

| [outcome](adverseevent-definitions.html#AdverseEvent.outcome) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | resolved | recovering | ongoing | resolvedWithSequelae | fatal | unknown
[AdverseEventOutcome](valueset-adverse-event-outcome.html) ([Required](terminologies.html#required)) | |

| [recorder](adverseevent-definitions.html#AdverseEvent.recorder) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html)) | Who recorded the adverse event | |

| [contributor](adverseevent-definitions.html#AdverseEvent.contributor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Device](device.html)) | Who was involved in the adverse event or the potential adverse event
 | |

| [suspectEntity](adverseevent-definitions.html#AdverseEvent.suspectEntity) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | The suspected agent causing the adverse event
 | |

| [instance](adverseevent-definitions.html#AdverseEvent.suspectEntity.instance) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Immunization](immunization.html) | [Procedure](procedure.html) | [Substance](substance.html) | [Medication](medication.html) | [MedicationAdministration](medicationadministration.html) | [MedicationStatement](medicationstatement.html) | [Device](device.html)) | Refers to the specific entity that caused the adverse event | |

| [causality](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | Information on the possible cause of the event
 | |

| [assessment](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.assessment) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Assessment of if the entity caused the event
[AdverseEventCausalityAssessment](valueset-adverse-event-causality-assess.html) ([Example](terminologies.html#example)) | |

| [productRelatedness](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.productRelatedness) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | AdverseEvent.suspectEntity.causalityProductRelatedness | |

| [author](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | AdverseEvent.suspectEntity.causalityAuthor | |

| [method](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.method) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | ProbabilityScale | Bayesian | Checklist
[AdverseEventCausalityMethod](valueset-adverse-event-causality-method.html) ([Example](terminologies.html#example)) | |

| [subjectMedicalHistory](adverseevent-definitions.html#AdverseEvent.subjectMedicalHistory) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [AllergyIntolerance](allergyintolerance.html) | [FamilyMemberHistory](familymemberhistory.html) | [Immunization](immunization.html) | [Procedure](procedure.html) | [Media](media.html) | [DocumentReference](documentreference.html)) | AdverseEvent.subjectMedicalHistory
 | |

| [referenceDocument](adverseevent-definitions.html#AdverseEvent.referenceDocument) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([DocumentReference](documentreference.html)) | AdverseEvent.referenceDocument
 | |

| [study](adverseevent-definitions.html#AdverseEvent.study) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([ResearchStudy](researchstudy.html)) | AdverseEvent.study
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - AdverseEvent ([DomainResource](domainresource.html))[Business identifiers assigned to this adverse event by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](adverseevent-definitions.html#AdverseEvent.identifier) : [Identifier](datatypes.html#Identifier) [0..1][Whether the event actually happened, or just had the potential to. Note that this is independent of whether anyone was affected or harmed or how severely (this element modifies the meaning of other elements)actuality](adverseevent-definitions.html#AdverseEvent.actuality) : [code](datatypes.html#code) [1..1] « [Overall nature of the adverse event, e.g. real or potential. (Strength=Required)AdverseEventActuality](valueset-adverse-event-actuality.html)! »[The overall type of event, intended for search and filtering purposescategory](adverseevent-definitions.html#AdverseEvent.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Overall categorization of the event, e.g. product-related or situational. (Strength=Extensible)AdverseEventCategory](valueset-adverse-event-category.html)+ »[This element defines the specific type of event that occurred or that was prevented from occurringevent](adverseevent-definitions.html#AdverseEvent.event) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Detailed type of event. (Strength=Example)SNOMEDCTClinicalFindings](valueset-adverse-event-type.html)?? »[This subject or group impacted by the eventsubject](adverseevent-definitions.html#AdverseEvent.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group)|[Practitioner](practitioner.html#Practitioner)| [RelatedPerson](relatedperson.html#RelatedPerson) »[The Encounter during which AdverseEvent was created or to which the creation of this record is tightly associatedencounter](adverseevent-definitions.html#AdverseEvent.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The date (and perhaps time) when the adverse event occurreddate](adverseevent-definitions.html#AdverseEvent.date) : [dateTime](datatypes.html#dateTime) [0..1][Estimated or actual date the AdverseEvent began, in the opinion of the reporterdetected](adverseevent-definitions.html#AdverseEvent.detected) : [dateTime](datatypes.html#dateTime) [0..1][The date on which the existence of the AdverseEvent was first recordedrecordedDate](adverseevent-definitions.html#AdverseEvent.recordedDate) : [dateTime](datatypes.html#dateTime) [0..1][Includes information about the reaction that occurred as a result of exposure to a substance (for example, a drug or a chemical)resultingCondition](adverseevent-definitions.html#AdverseEvent.resultingCondition) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition) »[The information about where the adverse event occurredlocation](adverseevent-definitions.html#AdverseEvent.location) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location) »[Assessment whether this event was of real importanceseriousness](adverseevent-definitions.html#AdverseEvent.seriousness) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Overall seriousness of this event for the patient. (Strength=Example)AdverseEventSeriousness](valueset-adverse-event-seriousness.html)?? »[Describes the severity of the adverse event, in relation to the subject. Contrast to AdverseEvent.seriousness - a severe rash might not be serious, but a mild heart problem isseverity](adverseevent-definitions.html#AdverseEvent.severity) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The severity of the adverse event itself, in direct relation to the subject. (Strength=Required)AdverseEventSeverity](valueset-adverse-event-severity.html)! »[Describes the type of outcome from the adverse eventoutcome](adverseevent-definitions.html#AdverseEvent.outcome) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [TODO (and should this be required?). (Strength=Required)AdverseEventOutcome](valueset-adverse-event-outcome.html)! »[Information on who recorded the adverse event. May be the patient or a practitionerrecorder](adverseevent-definitions.html#AdverseEvent.recorder) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson) »[Parties that may or should contribute or have contributed information to the adverse event, which can consist of one or more activities. Such information includes information leading to the decision to perform the activity and how to perform the activity (e.g. consultant), information that the activity itself seeks to reveal (e.g. informant of clinical history), or information about what activity was performed (e.g. informant witness)contributor](adverseevent-definitions.html#AdverseEvent.contributor) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Device](device.html#Device) »[AdverseEvent.subjectMedicalHistorysubjectMedicalHistory](adverseevent-definitions.html#AdverseEvent.subjectMedicalHistory) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)| [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|[Immunization](immunization.html#Immunization)|[Procedure](procedure.html#Procedure)| [Media](media.html#Media)|[DocumentReference](documentreference.html#DocumentReference) »[AdverseEvent.referenceDocumentreferenceDocument](adverseevent-definitions.html#AdverseEvent.referenceDocument) : [Reference](references.html#Reference) [0..*] « [DocumentReference](documentreference.html#DocumentReference) »[AdverseEvent.studystudy](adverseevent-definitions.html#AdverseEvent.study) : [Reference](references.html#Reference) [0..*] « [ResearchStudy](researchstudy.html#ResearchStudy) »SuspectEntity[Identifies the actual instance of what caused the adverse event. May be a substance, medication, medication administration, medication statement or a deviceinstance](adverseevent-definitions.html#AdverseEvent.suspectEntity.instance) : [Reference](references.html#Reference) [1..1] « [Immunization](immunization.html#Immunization)|[Procedure](procedure.html#Procedure)|[Substance](substance.html#Substance)| [Medication](medication.html#Medication)|[MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationStatement](medicationstatement.html#MedicationStatement)|[Device](device.html#Device) »Causality[Assessment of if the entity caused the eventassessment](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.assessment) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the assessment of whether the entity caused the event. (Strength=Example)](valueset-adverse-event-causality-assess.html) [AdverseEventCausalityAssessme...](valueset-adverse-event-causality-assess.html)?? »[AdverseEvent.suspectEntity.causalityProductRelatednessproductRelatedness](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.productRelatedness) : [string](datatypes.html#string) [0..1][AdverseEvent.suspectEntity.causalityAuthorauthor](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.author) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[ProbabilityScale | Bayesian | Checklistmethod](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.method) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [TODO. (Strength=Example)AdverseEventCausalityMethod](valueset-adverse-event-causality-method.html)?? »
[Information on the possible cause of the eventcausality](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality)[0..*][Describes the entity that is suspected to have caused the adverse eventsuspectEntity](adverseevent-definitions.html#AdverseEvent.suspectEntity)[0..*]
 

 

 

**XML Template**

 

 
```
http://hl7.org/fhir/ValueSet/adverse-event-causality
```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**AdverseEvent**](adverseevent-definitions.html#AdverseEvent)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](adverseevent-definitions.html#AdverseEvent.identifier)" : { [Identifier](datatypes.html#Identifier) }, // [Business identifier for the event](terminologies.html#unbound)
 "[actuality](adverseevent-definitions.html#AdverseEvent.actuality)" : "<[code](datatypes.html#code)>", // **R!** [actual | potential](valueset-adverse-event-actuality.html)
 "[category](adverseevent-definitions.html#AdverseEvent.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [product-problem | product-quality | product-use-error | wrong-dose | incorrect-prescribing-information | wrong-technique | wrong-route-of-administration | wrong-rate | wrong-duration | wrong-time | expired-drug | medical-device-use-error | problem-different-manufacturer | unsafe-physical-environment](valueset-adverse-event-category.html)
 "[event](adverseevent-definitions.html#AdverseEvent.event)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Type of the event itself in relation to the subject](valueset-adverse-event-type.html)
 "[subject](adverseevent-definitions.html#AdverseEvent.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)|[Practitioner](practitioner.html#Practitioner)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // **R!** [Subject impacted by event](terminologies.html#unbound)
 "[encounter](adverseevent-definitions.html#AdverseEvent.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[date](adverseevent-definitions.html#AdverseEvent.date)" : "<[dateTime](datatypes.html#dateTime)>", // [When the event occurred](terminologies.html#unbound)
 "[detected](adverseevent-definitions.html#AdverseEvent.detected)" : "<[dateTime](datatypes.html#dateTime)>", // [When the event was detected](terminologies.html#unbound)
 "[recordedDate](adverseevent-definitions.html#AdverseEvent.recordedDate)" : "<[dateTime](datatypes.html#dateTime)>", // [When the event was recorded](terminologies.html#unbound)
 "[resultingCondition](adverseevent-definitions.html#AdverseEvent.resultingCondition)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)) }], // [Effect on the subject due to this event](terminologies.html#unbound)
 "[location](adverseevent-definitions.html#AdverseEvent.location)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // [Location where adverse event occurred](terminologies.html#unbound)
 "[seriousness](adverseevent-definitions.html#AdverseEvent.seriousness)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Seriousness of the event](valueset-adverse-event-seriousness.html)
 "[severity](adverseevent-definitions.html#AdverseEvent.severity)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [mild | moderate | severe](valueset-adverse-event-severity.html)
 "[outcome](adverseevent-definitions.html#AdverseEvent.outcome)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [resolved | recovering | ongoing | resolvedWithSequelae | fatal | unknown](valueset-adverse-event-outcome.html)
 "[recorder](adverseevent-definitions.html#AdverseEvent.recorder)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Who recorded the adverse event](terminologies.html#unbound)
 "[contributor](adverseevent-definitions.html#AdverseEvent.contributor)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)) }], // [Who was involved in the adverse event or the potential adverse event](terminologies.html#unbound)
 "[suspectEntity](adverseevent-definitions.html#AdverseEvent.suspectEntity)" : [{ // [The suspected agent causing the adverse event](terminologies.html#unbound)
 "[instance](adverseevent-definitions.html#AdverseEvent.suspectEntity.instance)" : { [Reference](references.html#Reference)([Immunization](immunization.html#Immunization)|[Procedure](procedure.html#Procedure)|[Substance](substance.html#Substance)|[Medication](medication.html#Medication)|
 [MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationStatement](medicationstatement.html#MedicationStatement)|[Device](device.html#Device)) }, // **R!** [Refers to the specific entity that caused the adverse event](terminologies.html#unbound)
 "[causality](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality)" : [{ // [Information on the possible cause of the event](terminologies.html#unbound)
 "[assessment](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.assessment)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Assessment of if the entity caused the event](valueset-adverse-event-causality-assess.html)
 "[productRelatedness](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.productRelatedness)" : "<[string](datatypes.html#string)>", // [AdverseEvent.suspectEntity.causalityProductRelatedness](terminologies.html#unbound)
 "[author](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.author)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [AdverseEvent.suspectEntity.causalityAuthor](terminologies.html#unbound)
 "[method](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.method)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [ProbabilityScale | Bayesian | Checklist](valueset-adverse-event-causality-method.html)
 }]
 }],
 "[subjectMedicalHistory](adverseevent-definitions.html#AdverseEvent.subjectMedicalHistory)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|
 [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|[Immunization](immunization.html#Immunization)|[Procedure](procedure.html#Procedure)|[Media](media.html#Media)|
 [DocumentReference](documentreference.html#DocumentReference)) }], // [AdverseEvent.subjectMedicalHistory](terminologies.html#unbound)
 "[referenceDocument](adverseevent-definitions.html#AdverseEvent.referenceDocument)" : [{ [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) }], // [AdverseEvent.referenceDocument](terminologies.html#unbound)
 "[study](adverseevent-definitions.html#AdverseEvent.study)" : [{ [Reference](references.html#Reference)([ResearchStudy](researchstudy.html#ResearchStudy)) }] // [AdverseEvent.study](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**AdverseEvent**](adverseevent-definitions.html#AdverseEvent);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[AdverseEvent.identifier](adverseevent-definitions.html#AdverseEvent.identifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Business identifier for the event
 fhir:[AdverseEvent.actuality](adverseevent-definitions.html#AdverseEvent.actuality) [ [code](datatypes.html#code) ]; # 1..1 actual | potential
 fhir:[AdverseEvent.category](adverseevent-definitions.html#AdverseEvent.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* product-problem | product-quality | product-use-error | wrong-dose | incorrect-prescribing-information | wrong-technique | wrong-route-of-administration | wrong-rate | wrong-duration | wrong-time | expired-drug | medical-device-use-error | problem-different-manufacturer | unsafe-physical-environment
 fhir:[AdverseEvent.event](adverseevent-definitions.html#AdverseEvent.event) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Type of the event itself in relation to the subject
 fhir:[AdverseEvent.subject](adverseevent-definitions.html#AdverseEvent.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)|[Practitioner](practitioner.html#Practitioner)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 1..1 Subject impacted by event
 fhir:[AdverseEvent.encounter](adverseevent-definitions.html#AdverseEvent.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[AdverseEvent.date](adverseevent-definitions.html#AdverseEvent.date) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the event occurred
 fhir:[AdverseEvent.detected](adverseevent-definitions.html#AdverseEvent.detected) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the event was detected
 fhir:[AdverseEvent.recordedDate](adverseevent-definitions.html#AdverseEvent.recordedDate) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the event was recorded
 fhir:[AdverseEvent.resultingCondition](adverseevent-definitions.html#AdverseEvent.resultingCondition) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)) ], ... ; # 0..* Effect on the subject due to this event
 fhir:[AdverseEvent.location](adverseevent-definitions.html#AdverseEvent.location) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 0..1 Location where adverse event occurred
 fhir:[AdverseEvent.seriousness](adverseevent-definitions.html#AdverseEvent.seriousness) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Seriousness of the event
 fhir:[AdverseEvent.severity](adverseevent-definitions.html#AdverseEvent.severity) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 mild | moderate | severe
 fhir:[AdverseEvent.outcome](adverseevent-definitions.html#AdverseEvent.outcome) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 resolved | recovering | ongoing | resolvedWithSequelae | fatal | unknown
 fhir:[AdverseEvent.recorder](adverseevent-definitions.html#AdverseEvent.recorder) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Who recorded the adverse event
 fhir:[AdverseEvent.contributor](adverseevent-definitions.html#AdverseEvent.contributor) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)) ], ... ; # 0..* Who was involved in the adverse event or the potential adverse event
 fhir:[AdverseEvent.suspectEntity](adverseevent-definitions.html#AdverseEvent.suspectEntity) [ # 0..* The suspected agent causing the adverse event
 fhir:[AdverseEvent.suspectEntity.instance](adverseevent-definitions.html#AdverseEvent.suspectEntity.instance) [ [Reference](references.html#Reference)([Immunization](immunization.html#Immunization)|[Procedure](procedure.html#Procedure)|[Substance](substance.html#Substance)|[Medication](medication.html#Medication)|[MedicationAdministration](medicationadministration.html#MedicationAdministration)|
 [MedicationStatement](medicationstatement.html#MedicationStatement)|[Device](device.html#Device)) ]; # 1..1 Refers to the specific entity that caused the adverse event
 fhir:[AdverseEvent.suspectEntity.causality](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality) [ # 0..* Information on the possible cause of the event
 fhir:[AdverseEvent.suspectEntity.causality.assessment](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.assessment) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Assessment of if the entity caused the event
 fhir:[AdverseEvent.suspectEntity.causality.productRelatedness](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.productRelatedness) [ [string](datatypes.html#string) ]; # 0..1 AdverseEvent.suspectEntity.causalityProductRelatedness
 fhir:[AdverseEvent.suspectEntity.causality.author](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 AdverseEvent.suspectEntity.causalityAuthor
 fhir:[AdverseEvent.suspectEntity.causality.method](adverseevent-definitions.html#AdverseEvent.suspectEntity.causality.method) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 ProbabilityScale | Bayesian | Checklist
 ], ...;
 ], ...;
 fhir:[AdverseEvent.subjectMedicalHistory](adverseevent-definitions.html#AdverseEvent.subjectMedicalHistory) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[AllergyIntolerance](allergyintolerance.html#AllergyIntolerance)|[FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory)|[Immunization](immunization.html#Immunization)|
 [Procedure](procedure.html#Procedure)|[Media](media.html#Media)|[DocumentReference](documentreference.html#DocumentReference)) ], ... ; # 0..* AdverseEvent.subjectMedicalHistory
 fhir:[AdverseEvent.referenceDocument](adverseevent-definitions.html#AdverseEvent.referenceDocument) [ [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) ], ... ; # 0..* AdverseEvent.referenceDocument
 fhir:[AdverseEvent.study](adverseevent-definitions.html#AdverseEvent.study) [ [Reference](references.html#Reference)([ResearchStudy](researchstudy.html#ResearchStudy)) ], ... ; # 0..* AdverseEvent.study
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [AdverseEvent](adverseevent.html#AdverseEvent)
 | 
 | 
 |

 | 
 AdverseEvent.actuality | 
 
 

 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 AdverseEvent.category | 
 
 

 - Max Cardinality changed from 1 to *

 - Type changed from code to CodeableConcept

 - Change binding strength from required to extensible

 

 | 
 |

 | 
 AdverseEvent.event | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.subject | 
 
 

 - Min Cardinality changed from 0 to 1

 - Type Reference: Added Target Types Group, Practitioner, RelatedPerson

 - Type Reference: Removed Target Types ResearchSubject, Medication, Device

 

 | 
 |

 | 
 AdverseEvent.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.detected | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.recordedDate | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.resultingCondition | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.severity | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.outcome | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/adverse-event-outcome to http://hl7.org/fhir/ValueSet/adverse-event-outcome|4.0.1

 

 | 
 |

 | 
 AdverseEvent.recorder | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 AdverseEvent.contributor | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.instance | 
 
 

 - Type Reference: Added Target Types Immunization, Procedure

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causality | 
 
 

 - Max Cardinality changed from 1 to *

 - Type changed from code to BackboneElement

 - 
Remove Binding `http://hl7.org/fhir/ValueSet/adverse-event-causality` (required)
 

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causality.assessment | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causality.productRelatedness | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causality.author | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causality.method | 
 
 

 - Added Element

 

 | 
 |

 | 
 AdverseEvent.subjectMedicalHistory | 
 
 

 - Type Reference: Added Target Types Media, DocumentReference

 

 | 
 |

 | 
 AdverseEvent.type | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.reaction | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.eventParticipant | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.description | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causalityAssessment | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causalityProductRelatedness | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causalityMethod | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causalityAuthor | 
 
 

 - deleted

 

 | 
 |

 | 
 AdverseEvent.suspectEntity.causalityResult | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](adverseevent.diff.xml) or [JSON](adverseevent.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](adverseevent-version-maps.html) (status = 1 test that all execute ok. 1 fail round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](adverseevent-profiles.html) and the alternate definitions:
Master Definition [XML](adverseevent.profile.xml.html) + [JSON](adverseevent.profile.json.html),
[XML](xml.html) [Schema](adverseevent.xsd)/[Schematron](adverseevent.sch) + [JSON](json.html) 
[Schema](adverseevent.schema.json.html), [ShEx](adverseevent.shex.html) (for [Turtle](rdf.html)) + [see the extensions](adverseevent-profiles.html) & the [dependency analysis](adverseevent-dependencies.html)

### 9.9.3.1 
Terminology Bindings
 [
](adverseevent.html#tx)

 | Path | Definition | Type | Reference | |

 | AdverseEvent.actuality | Overall nature of the adverse event, e.g. real or potential. | [Required](terminologies.html#required) | [AdverseEventActuality](valueset-adverse-event-actuality.html) | |

 | AdverseEvent.category | Overall categorization of the event, e.g. product-related or situational. | [Extensible](terminologies.html#extensible) | [AdverseEventCategory](valueset-adverse-event-category.html) | |

 | AdverseEvent.event | Detailed type of event. | [Example](terminologies.html#example) | [SNOMEDCTClinicalFindings](valueset-adverse-event-type.html) | |

 | AdverseEvent.seriousness | Overall seriousness of this event for the patient. | [Example](terminologies.html#example) | [AdverseEventSeriousness](valueset-adverse-event-seriousness.html) | |

 | AdverseEvent.severity | The severity of the adverse event itself, in direct relation to the subject. | [Required](terminologies.html#required) | [AdverseEventSeverity](valueset-adverse-event-severity.html) | |

 | AdverseEvent.outcome | TODO (and should this be required?). | [Required](terminologies.html#required) | [AdverseEventOutcome](valueset-adverse-event-outcome.html) | |

 | AdverseEvent.suspectEntity.causality.assessment | Codes for the assessment of whether the entity caused the event. | [Example](terminologies.html#example) | [AdverseEventCausalityAssessment](valueset-adverse-event-causality-assess.html) | |

 | AdverseEvent.suspectEntity.causality.method | TODO. | [Example](terminologies.html#example) | [AdverseEventCausalityMethod](valueset-adverse-event-causality-method.html) | |

 

 

## 9.9.4 Search Parameters [
](adverseevent.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| actuality | [token](search.html#token) | actual | potential | AdverseEvent.actuality | | |

| category | [token](search.html#token) | product-problem | product-quality | product-use-error | wrong-dose | incorrect-prescribing-information | wrong-technique | wrong-route-of-administration | wrong-rate | wrong-duration | wrong-time | expired-drug | medical-device-use-error | problem-different-manufacturer | unsafe-physical-environment | AdverseEvent.category | | |

| date | [date](search.html#date) | When the event occurred | AdverseEvent.date | | |

| event | [token](search.html#token) | Type of the event itself in relation to the subject | AdverseEvent.event | | |

| location | [reference](search.html#reference) | Location where adverse event occurred | AdverseEvent.location
([Location](location.html)) | | |

| recorder | [reference](search.html#reference) | Who recorded the adverse event | AdverseEvent.recorder
([Practitioner](practitioner.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| resultingcondition | [reference](search.html#reference) | Effect on the subject due to this event | AdverseEvent.resultingCondition
([Condition](condition.html)) | | |

| seriousness | [token](search.html#token) | Seriousness of the event | AdverseEvent.seriousness | | |

| severity | [token](search.html#token) | mild | moderate | severe | AdverseEvent.severity | | |

| study | [reference](search.html#reference) | AdverseEvent.study | AdverseEvent.study
([ResearchStudy](researchstudy.html)) | | |

| subject | [reference](search.html#reference) | Subject impacted by event | AdverseEvent.subject
([Practitioner](practitioner.html), [Group](group.html), [Patient](patient.html), [RelatedPerson](relatedperson.html)) | | |

| substance | [reference](search.html#reference) | Refers to the specific entity that caused the adverse event | AdverseEvent.suspectEntity.instance
([Immunization](immunization.html), [Device](device.html), [Medication](medication.html), [Procedure](procedure.html), [Substance](substance.html), [MedicationAdministration](medicationadministration.html), [MedicationStatement](medicationstatement.html)) | | |