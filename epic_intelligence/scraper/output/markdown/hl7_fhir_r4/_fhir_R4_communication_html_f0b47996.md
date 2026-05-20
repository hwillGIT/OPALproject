# Communication - FHIR v4.0.1Business identifiers assigned to this communication by the performer or other systems which remain constant as the resource is updated and propagates from server to serverThe URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationThe URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationAn order, proposal or plan fulfilled in whole or in part by this CommunicationPart of this actionPrior communication that this communication is in response toThe status of the transmission (this element modifies the meaning of other elements)The status of the communication. (Strength=Required)Captures the reason for the current state of the CommunicationCodes for the reason why a communication did not happen. (Strength=Example)The type of message conveyed such as alert, notification, reminder, instruction, etcCodes for general categories of communications such as alerts, instructions, etc. (Strength=Example)Characterizes how quickly the planned or in progress communication must be addressed. Includes concepts such as stat, urgent, routineCodes indicating the relative importance of a communication. (Strength=Required)A channel that was used for this communication (e.g. email, fax)Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)The patient or group that was the focus of this communicationDescription of the purpose/content, similar to a subject line in an emailCodes describing the purpose or content of the communication. (Strength=Example)Other resources that pertain to this communication and to which this communication should be associatedThe Encounter during which this Communication was created or to which the creation of this record is tightly associatedThe time when this communication was sentThe time when this communication arrived at the destinationThe entity (e.g. person, organization, clinical information system, care team or device) which was the target of the communication. If receipts need to be tracked by an individual, a separate resource instance will need to be created for each recipient.  Multiple recipient communications are intended where either receipts are not tracked (e.g. a mass mail-out) or a receipt is captured in aggregate (all emails confirmed received by a particular time)The entity (e.g. person, organization, clinical information system, or device) which was the source of the communicationThe reason or justification for the communicationCodes for describing reasons for the occurrence of a communication. (Strength=Example)Indicates another resource whose existence justifies this communicationAdditional notes or commentary about the communication by the sender, receiver or other interested partiesA communicated content (or for multi-part communications, one portion of the communication)Text, attachment(s), or resource(s) that was communicated to the recipientBusiness identifiers assigned to this communication by the performer or other systems which remain constant as the resource is updated and propagates from server to serverThe URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationThe URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationAn order, proposal or plan fulfilled in whole or in part by this CommunicationPart of this actionPrior communication that this communication is in response toThe status of the transmission (this element modifies the meaning of other elements)The status of the communication. (Strength=Required)Captures the reason for the current state of the CommunicationCodes for the reason why a communication did not happen. (Strength=Example)The type of message conveyed such as alert, notification, reminder, instruction, etcCodes for general categories of communications such as alerts, instructions, etc. (Strength=Example)Characterizes how quickly the planned or in progress communication must be addressed. Includes concepts such as stat, urgent, routineCodes indicating the relative importance of a communication. (Strength=Required)A channel that was used for this communication (e.g. email, fax)Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)The patient or group that was the focus of this communicationDescription of the purpose/content, similar to a subject line in an emailCodes describing the purpose or content of the communication. (Strength=Example)Other resources that pertain to this communication and to which this communication should be associatedThe Encounter during which this Communication was created or to which the creation of this record is tightly associatedThe time when this communication was sentThe time when this communication arrived at the destinationThe entity (e.g. person, organization, clinical information system, care team or device) which was the target of the communication. If receipts need to be tracked by an individual, a separate resource instance will need to be created for each recipient.  Multiple recipient communications are intended where either receipts are not tracked (e.g. a mass mail-out) or a receipt is captured in aggregate (all emails confirmed received by a particular time)The entity (e.g. person, organization, clinical information system, or device) which was the source of the communicationThe reason or justification for the communicationCodes for describing reasons for the occurrence of a communication. (Strength=Example)Indicates another resource whose existence justifies this communicationAdditional notes or commentary about the communication by the sender, receiver or other interested partiesA communicated content (or for multi-part communications, one portion of the communication)Text, attachment(s), or resource(s) that was communicated to the recipient

> Source: https://hl7.org/fhir/R4/communication.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/communication.html) [R4B](http://hl7.org/fhir/R4B/communication.html) **R4** [R3](http://hl7.org/fhir/STU3/communication.html) [R2](http://hl7.org/fhir/DSTU2/communication.html)
 

# 8.20 Resource Communication - Content [
](communication.html#8.20)

| [Patient Care ](http://www.hl7.org/Special/committees/patientcare/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.

## 8.20.1 Scope and Usage [
](communication.html#scope)

 
 
Communication is one of the [event](workflow.html#event) resources in the FHIR [workflow](workflow.html) specification.

 

This resource is a record of a communication even if it is planned or has failed. A communication is a conveyance of information from one entity, a sender, to another entity, a receiver. 
The sender and receivers may be patients, practitioners, related persons, organizations, or devices. Communication use cases include:

- A reminder or alert delivered to a responsible provider

- A recorded notification from the nurse to the on-call physician (or any other specified person) that a patient's temperature exceeds a value

- A notification to a public health agency of a patient presenting with a communicable disease reportable to the public health agency

- Patient educational material sent by a provider to a patient

- Unable to deliver lab results to ordering physician

Non-patient specific communication use cases may include:

- A nurse call from a hall bathroom

- Advisory for battery service from a pump

 

## 8.20.2 Boundaries and Relationships [
](communication.html#bnr)

This resource is a record of a communication that has occurred. It does not represent the actual flow of communication.
While [AuditEvent](auditevent.html) can track electronic disclosures of information, it cannot track conversations,
phone calls, letters and other interactions that are not system-to-system. And even for system-to-system communications, the
specific end recipients might not be known. Furthermore, [AuditEvents](auditevent.html) are not considered to be "part"
of the patient record, while **Communication** instances are. The **Communication** resource is not used as a general
audit mechanism to track every disclosure of every record. Rather, it is used when a clinician or other user wants to ensure
a record of a particular communication is itself maintained as part of the reviewable health record.

[Flag](flag.html) resources represent a continuous ongoing "communication" alerting anyone dealing with the patient
of certain precautions to take or issues to be aware of. The flags are continuously present as an ongoing reminder. This is 
distinct from **Communication** where there is a specific intended sender and receiver and the information is delivered only
once.

**Communication and Encounter**

The Communication is about the transfer of information (which might or might not occur as part of an encounter), while Encounter 
is about the coming together (in person or virtually) of a Patient with a Practitioner. Communication does not deal with 
the duration of a call, it represents the fact that information was transferred at a particular point in time.

The phone calls involving the Patient should be handled using [Encounter](encounter.html). Phone calls not involving the patient 
(e.g. between practitioners or practitioner to relative) that are tracked for billing or other purposes can use Communication 
to represent the information transferred but are not ideal to represent the call itself. 
A better mechanism for handling such calls will be explored in a future release.

 

This resource is referenced by itself

## 8.20.3 
Resource Content
 [
](communication.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Communication](communication-definitions.html#Communication) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A record of information transmitted from a sender to a receiver**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](communication-definitions.html#Communication.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Unique identifier
 | |

| [instantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html) | [ActivityDefinition](activitydefinition.html) | [Measure](measure.html) | [OperationDefinition](operationdefinition.html) | [Questionnaire](questionnaire.html)) | Instantiates FHIR protocol or definition
 | |

| [instantiatesUri](communication-definitions.html#Communication.instantiatesUri) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [uri](datatypes.html#uri) | Instantiates external protocol or definition
 | |

| [basedOn](communication-definitions.html#Communication.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Request fulfilled by this communication
 | |

| [partOf](communication-definitions.html#Communication.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Part of this action
 | |

| [inResponseTo](communication-definitions.html#Communication.inResponseTo) | | 0..* | [Reference](references.html#Reference)([Communication](communication.html)) | Reply to
 | |

| [status](communication-definitions.html#Communication.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
[EventStatus](valueset-event-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](communication-definitions.html#Communication.statusReason) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status
[CommunicationNotDoneReason](valueset-communication-not-done-reason.html) ([Example](terminologies.html#example)) | |

| [category](communication-definitions.html#Communication.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Message category
[CommunicationCategory](valueset-communication-category.html) ([Example](terminologies.html#example))
 | |

| [priority](communication-definitions.html#Communication.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [medium](communication-definitions.html#Communication.medium) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A channel of communication
[v3 Code System ParticipationMode](v3/ParticipationMode/vs.html) ([Example](terminologies.html#example))
 | |

| [subject](communication-definitions.html#Communication.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Focus of message | |

| [topic](communication-definitions.html#Communication.topic) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Description of the purpose/content
[CommunicationTopic](valueset-communication-topic.html) ([Example](terminologies.html#example)) | |

| [about](communication-definitions.html#Communication.about) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Resources that pertain to this communication
 | |

| [encounter](communication-definitions.html#Communication.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [sent](communication-definitions.html#Communication.sent) | | 0..1 | [dateTime](datatypes.html#dateTime) | When sent | |

| [received](communication-definitions.html#Communication.received) | | 0..1 | [dateTime](datatypes.html#dateTime) | When received | |

| [recipient](communication-definitions.html#Communication.recipient) | | 0..* | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Group](group.html) | [CareTeam](careteam.html) | [HealthcareService](healthcareservice.html)) | Message recipient
 | |

| [sender](communication-definitions.html#Communication.sender) | | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [HealthcareService](healthcareservice.html)) | Message sender | |

| [reasonCode](communication-definitions.html#Communication.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Indication for message
[SNOMED CT Clinical Findings](valueset-clinical-findings.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](communication-definitions.html#Communication.reasonReference) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html)) | Why was communication done?
 | |

| [payload](communication-definitions.html#Communication.payload) | | 0..* | [BackboneElement](backboneelement.html) | Message payload
 | |

| [content[x]](communication-definitions.html#Communication.payload.content_x_) | | 1..1 | | Message part content | |

| contentString | | | [string](datatypes.html#string) | | |

| contentAttachment | | | [Attachment](datatypes.html#Attachment) | | |

| contentReference | | | [Reference](references.html#Reference)([Any](resourcelist.html)) | | |

| [note](communication-definitions.html#Communication.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the communication
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Communication ([DomainResource](domainresource.html))[Business identifiers assigned to this communication by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](communication-definitions.html#Communication.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationinstantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..*] « [PlanDefinition](plandefinition.html#PlanDefinition)| [ActivityDefinition](activitydefinition.html#ActivityDefinition)|[Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire) »[The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationinstantiatesUri](communication-definitions.html#Communication.instantiatesUri) : [uri](datatypes.html#uri) [0..*][An order, proposal or plan fulfilled in whole or in part by this CommunicationbasedOn](communication-definitions.html#Communication.basedOn) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Part of this actionpartOf](communication-definitions.html#Communication.partOf) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Prior communication that this communication is in response toinResponseTo](communication-definitions.html#Communication.inResponseTo) : [Reference](references.html#Reference) [0..*] « [Communication](communication.html#Communication) »[The status of the transmission (this element modifies the meaning of other elements)status](communication-definitions.html#Communication.status) : [code](datatypes.html#code) [1..1] « [The status of the communication. (Strength=Required)EventStatus](valueset-event-status.html)! »[Captures the reason for the current state of the CommunicationstatusReason](communication-definitions.html#Communication.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the reason why a communication did not happen. (Strength=Example)CommunicationNotDoneReason](valueset-communication-not-done-reason.html)?? »[The type of message conveyed such as alert, notification, reminder, instruction, etccategory](communication-definitions.html#Communication.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for general categories of communications such as alerts, instructions, etc. (Strength=Example)CommunicationCategory](valueset-communication-category.html)?? »[Characterizes how quickly the planned or in progress communication must be addressed. Includes concepts such as stat, urgent, routinepriority](communication-definitions.html#Communication.priority) : [code](datatypes.html#code) [0..1] « [Codes indicating the relative importance of a communication. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[A channel that was used for this communication (e.g. email, fax)medium](communication-definitions.html#Communication.medium) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)v3.ParticipationMode](v3/ParticipationMode/vs.html)?? »[The patient or group that was the focus of this communicationsubject](communication-definitions.html#Communication.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[Description of the purpose/content, similar to a subject line in an emailtopic](communication-definitions.html#Communication.topic) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing the purpose or content of the communication. (Strength=Example)CommunicationTopic](valueset-communication-topic.html)?? »[Other resources that pertain to this communication and to which this communication should be associatedabout](communication-definitions.html#Communication.about) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[The Encounter during which this Communication was created or to which the creation of this record is tightly associatedencounter](communication-definitions.html#Communication.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The time when this communication was sentsent](communication-definitions.html#Communication.sent) : [dateTime](datatypes.html#dateTime) [0..1][The time when this communication arrived at the destinationreceived](communication-definitions.html#Communication.received) : [dateTime](datatypes.html#dateTime) [0..1][The entity (e.g. person, organization, clinical information system, care team or device) which was the target of the communication. If receipts need to be tracked by an individual, a separate resource instance will need to be created for each recipient. Multiple recipient communications are intended where either receipts are not tracked (e.g. a mass mail-out) or a receipt is captured in aggregate (all emails confirmed received by a particular time)recipient](communication-definitions.html#Communication.recipient) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)| [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)| [HealthcareService](healthcareservice.html#HealthcareService) »[The entity (e.g. person, organization, clinical information system, or device) which was the source of the communicationsender](communication-definitions.html#Communication.sender) : [Reference](references.html#Reference) [0..1] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService) »[The reason or justification for the communicationreasonCode](communication-definitions.html#Communication.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for describing reasons for the occurrence of a communication. (Strength=Example)SNOMEDCTClinicalFindings](valueset-clinical-findings.html)?? »[Indicates another resource whose existence justifies this communicationreasonReference](communication-definitions.html#Communication.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)| [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference) »[Additional notes or commentary about the communication by the sender, receiver or other interested partiesnote](communication-definitions.html#Communication.note) : [Annotation](datatypes.html#Annotation) [0..*]Payload[A communicated content (or for multi-part communications, one portion of the communication)content[x]](communication-definitions.html#Communication.payload.content_x_) : [Type](formats.html#umlchoice) [1..1] « [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html#Any)) »
[Text, attachment(s), or resource(s) that was communicated to the recipientpayload](communication-definitions.html#Communication.payload)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Communication**](communication-definitions.html#Communication) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](communication-definitions.html#Communication.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Unique identifier](terminologies.html#unbound) --></identifier>
 <[**instantiatesCanonical**](communication-definitions.html#Communication.instantiatesCanonical)><!-- **0..*** [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|
 [Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire)) [Instantiates FHIR protocol or definition](terminologies.html#unbound) --></instantiatesCanonical>
 <[**instantiatesUri**](communication-definitions.html#Communication.instantiatesUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Instantiates external protocol or definition](terminologies.html#unbound) -->
 <[**basedOn**](communication-definitions.html#Communication.basedOn)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Request fulfilled by this communication](terminologies.html#unbound) --></basedOn>
 <[**partOf**](communication-definitions.html#Communication.partOf)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Part of this action](terminologies.html#unbound) --></partOf>
 <[**inResponseTo**](communication-definitions.html#Communication.inResponseTo)><!-- **0..*** [Reference](references.html#Reference)([Communication](communication.html#Communication)) [Reply to](terminologies.html#unbound) --></inResponseTo>
 <[**status**](communication-definitions.html#Communication.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown](valueset-event-status.html) -->
 <[**statusReason**](communication-definitions.html#Communication.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](valueset-communication-not-done-reason.html) --></statusReason>
 <[**category**](communication-definitions.html#Communication.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Message category](valueset-communication-category.html) --></category>
 <[**priority**](communication-definitions.html#Communication.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**medium**](communication-definitions.html#Communication.medium)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A channel of communication](v3/ParticipationMode/vs.html) --></medium>
 <[**subject**](communication-definitions.html#Communication.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Focus of message](terminologies.html#unbound) --></subject>
 <[**topic**](communication-definitions.html#Communication.topic)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Description of the purpose/content](valueset-communication-topic.html) --></topic>
 <[**about**](communication-definitions.html#Communication.about)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Resources that pertain to this communication](terminologies.html#unbound) --></about>
 <[**encounter**](communication-definitions.html#Communication.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**sent**](communication-definitions.html#Communication.sent) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When sent](terminologies.html#unbound) -->
 <[**received**](communication-definitions.html#Communication.received) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When received](terminologies.html#unbound) -->
 <[**recipient**](communication-definitions.html#Communication.recipient)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message recipient](terminologies.html#unbound) --></recipient>
 <[**sender**](communication-definitions.html#Communication.sender)><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message sender](terminologies.html#unbound) --></sender>
 <[**reasonCode**](communication-definitions.html#Communication.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Indication for message](valueset-clinical-findings.html) --></reasonCode>
 <[**reasonReference**](communication-definitions.html#Communication.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) [Why was communication done?](terminologies.html#unbound) --></reasonReference>
 <[**payload**](communication-definitions.html#Communication.payload)> <!-- **0..*** Message payload -->
 <[**content[x]**](communication-definitions.html#Communication.payload.content[x])><!-- **1..1** [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html)) [Message part content](terminologies.html#unbound) --></content[x]>
 </payload>
 <[**note**](communication-definitions.html#Communication.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the communication](terminologies.html#unbound) --></note>
</Communication>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Communication**](communication-definitions.html#Communication)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](communication-definitions.html#Communication.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Unique identifier](terminologies.html#unbound)
 "[instantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical)" : [{ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|
 [Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire)) }], // [Instantiates FHIR protocol or definition](terminologies.html#unbound)
 "[instantiatesUri](communication-definitions.html#Communication.instantiatesUri)" : ["<[uri](datatypes.html#uri)>"], // [Instantiates external protocol or definition](terminologies.html#unbound)
 "[basedOn](communication-definitions.html#Communication.basedOn)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Request fulfilled by this communication](terminologies.html#unbound)
 "[partOf](communication-definitions.html#Communication.partOf)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Part of this action](terminologies.html#unbound)
 "[inResponseTo](communication-definitions.html#Communication.inResponseTo)" : [{ [Reference](references.html#Reference)([Communication](communication.html#Communication)) }], // [Reply to](terminologies.html#unbound)
 "[status](communication-definitions.html#Communication.status)" : "<[code](datatypes.html#code)>", // **R!** [preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown](valueset-event-status.html)
 "[statusReason](communication-definitions.html#Communication.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](valueset-communication-not-done-reason.html)
 "[category](communication-definitions.html#Communication.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Message category](valueset-communication-category.html)
 "[priority](communication-definitions.html#Communication.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[medium](communication-definitions.html#Communication.medium)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [A channel of communication](v3/ParticipationMode/vs.html)
 "[subject](communication-definitions.html#Communication.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [Focus of message](terminologies.html#unbound)
 "[topic](communication-definitions.html#Communication.topic)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Description of the purpose/content](valueset-communication-topic.html)
 "[about](communication-definitions.html#Communication.about)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Resources that pertain to this communication](terminologies.html#unbound)
 "[encounter](communication-definitions.html#Communication.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[sent](communication-definitions.html#Communication.sent)" : "<[dateTime](datatypes.html#dateTime)>", // [When sent](terminologies.html#unbound)
 "[received](communication-definitions.html#Communication.received)" : "<[dateTime](datatypes.html#dateTime)>", // [When received](terminologies.html#unbound)
 "[recipient](communication-definitions.html#Communication.recipient)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) }], // [Message recipient](terminologies.html#unbound)
 "[sender](communication-definitions.html#Communication.sender)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) }, // [Message sender](terminologies.html#unbound)
 "[reasonCode](communication-definitions.html#Communication.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Indication for message](valueset-clinical-findings.html)
 "[reasonReference](communication-definitions.html#Communication.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) }], // [Why was communication done?](terminologies.html#unbound)
 "[payload](communication-definitions.html#Communication.payload)" : [{ // [Message payload](terminologies.html#unbound)
 // content[x]: Message part content. One of these 3:
 "[contentString](communication-definitions.html#Communication.payload.contentString)" : "<[string](datatypes.html#string)>"
 "[contentAttachment](communication-definitions.html#Communication.payload.contentAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[contentReference](communication-definitions.html#Communication.payload.contentReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }
 }],
 "[note](communication-definitions.html#Communication.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about the communication](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Communication**](communication-definitions.html#Communication);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Communication.identifier](communication-definitions.html#Communication.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Unique identifier
 fhir:[Communication.instantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical) [ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|[Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire)) ], ... ; # 0..* Instantiates FHIR protocol or definition
 fhir:[Communication.instantiatesUri](communication-definitions.html#Communication.instantiatesUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Instantiates external protocol or definition
 fhir:[Communication.basedOn](communication-definitions.html#Communication.basedOn) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Request fulfilled by this communication
 fhir:[Communication.partOf](communication-definitions.html#Communication.partOf) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Part of this action
 fhir:[Communication.inResponseTo](communication-definitions.html#Communication.inResponseTo) [ [Reference](references.html#Reference)([Communication](communication.html#Communication)) ], ... ; # 0..* Reply to
 fhir:[Communication.status](communication-definitions.html#Communication.status) [ [code](datatypes.html#code) ]; # 1..1 preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
 fhir:[Communication.statusReason](communication-definitions.html#Communication.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[Communication.category](communication-definitions.html#Communication.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Message category
 fhir:[Communication.priority](communication-definitions.html#Communication.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[Communication.medium](communication-definitions.html#Communication.medium) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A channel of communication
 fhir:[Communication.subject](communication-definitions.html#Communication.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 Focus of message
 fhir:[Communication.topic](communication-definitions.html#Communication.topic) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Description of the purpose/content
 fhir:[Communication.about](communication-definitions.html#Communication.about) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Resources that pertain to this communication
 fhir:[Communication.encounter](communication-definitions.html#Communication.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[Communication.sent](communication-definitions.html#Communication.sent) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When sent
 fhir:[Communication.received](communication-definitions.html#Communication.received) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When received
 fhir:[Communication.recipient](communication-definitions.html#Communication.recipient) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|
 [CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) ], ... ; # 0..* Message recipient
 fhir:[Communication.sender](communication-definitions.html#Communication.sender) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [HealthcareService](healthcareservice.html#HealthcareService)) ]; # 0..1 Message sender
 fhir:[Communication.reasonCode](communication-definitions.html#Communication.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Indication for message
 fhir:[Communication.reasonReference](communication-definitions.html#Communication.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference)) ], ... ; # 0..* Why was communication done?
 fhir:[Communication.payload](communication-definitions.html#Communication.payload) [ # 0..* Message payload
 # [Communication.payload.content[x]](communication-definitions.html#Communication.payload.content[x]) : 1..1 Message part content. One of these 3
 fhir:[Communication.payload.contentString](communication-definitions.html#Communication.payload.contentString) [ [string](datatypes.html#string) ]
 fhir:[Communication.payload.contentAttachment](communication-definitions.html#Communication.payload.contentAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Communication.payload.contentReference](communication-definitions.html#Communication.payload.contentReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]
 ], ...;
 fhir:[Communication.note](communication-definitions.html#Communication.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the communication
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Communication](communication.html#Communication)
 | 
 | 
 |

 | 
 Communication.instantiatesCanonical | 
 
 

 Added Element

 

 | 
 |

 | 
 Communication.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.inResponseTo | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/event-status to http://hl7.org/fhir/ValueSet/event-status|4.0.1

 

 | 
 |

 | 
 Communication.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.priority | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.topic | 
 
 

 - Max Cardinality changed from * to 1

 - Type changed from Reference(Resource) to CodeableConcept

 

 | 
 |

 | 
 Communication.about | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.recipient | 
 
 

 - Type Reference: Added Target Types PractitionerRole, CareTeam, HealthcareService

 

 | 
 |

 | 
 Communication.sender | 
 
 

 - Type Reference: Added Target Types PractitionerRole, HealthcareService

 

 | 
 |

 | 
 Communication.reasonReference | 
 
 

 - Type Reference: Added Target Types DiagnosticReport, DocumentReference

 

 | 
 |

 | 
 Communication.definition | 
 
 

 - deleted

 

 | 
 |

 | 
 Communication.notDone | 
 
 

 - deleted

 

 | 
 |

 | 
 Communication.notDoneReason | 
 
 

 - deleted

 

 | 
 |

 | 
 Communication.context | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](communication.diff.xml) or [JSON](communication.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](communication-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and 2 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Communication](communication-definitions.html#Communication) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A record of information transmitted from a sender to a receiver**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](communication-definitions.html#Communication.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Unique identifier
 | |

| [instantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html) | [ActivityDefinition](activitydefinition.html) | [Measure](measure.html) | [OperationDefinition](operationdefinition.html) | [Questionnaire](questionnaire.html)) | Instantiates FHIR protocol or definition
 | |

| [instantiatesUri](communication-definitions.html#Communication.instantiatesUri) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [uri](datatypes.html#uri) | Instantiates external protocol or definition
 | |

| [basedOn](communication-definitions.html#Communication.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Request fulfilled by this communication
 | |

| [partOf](communication-definitions.html#Communication.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Part of this action
 | |

| [inResponseTo](communication-definitions.html#Communication.inResponseTo) | | 0..* | [Reference](references.html#Reference)([Communication](communication.html)) | Reply to
 | |

| [status](communication-definitions.html#Communication.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
[EventStatus](valueset-event-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](communication-definitions.html#Communication.statusReason) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status
[CommunicationNotDoneReason](valueset-communication-not-done-reason.html) ([Example](terminologies.html#example)) | |

| [category](communication-definitions.html#Communication.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Message category
[CommunicationCategory](valueset-communication-category.html) ([Example](terminologies.html#example))
 | |

| [priority](communication-definitions.html#Communication.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [medium](communication-definitions.html#Communication.medium) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A channel of communication
[v3 Code System ParticipationMode](v3/ParticipationMode/vs.html) ([Example](terminologies.html#example))
 | |

| [subject](communication-definitions.html#Communication.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Focus of message | |

| [topic](communication-definitions.html#Communication.topic) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Description of the purpose/content
[CommunicationTopic](valueset-communication-topic.html) ([Example](terminologies.html#example)) | |

| [about](communication-definitions.html#Communication.about) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Resources that pertain to this communication
 | |

| [encounter](communication-definitions.html#Communication.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [sent](communication-definitions.html#Communication.sent) | | 0..1 | [dateTime](datatypes.html#dateTime) | When sent | |

| [received](communication-definitions.html#Communication.received) | | 0..1 | [dateTime](datatypes.html#dateTime) | When received | |

| [recipient](communication-definitions.html#Communication.recipient) | | 0..* | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Group](group.html) | [CareTeam](careteam.html) | [HealthcareService](healthcareservice.html)) | Message recipient
 | |

| [sender](communication-definitions.html#Communication.sender) | | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [HealthcareService](healthcareservice.html)) | Message sender | |

| [reasonCode](communication-definitions.html#Communication.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Indication for message
[SNOMED CT Clinical Findings](valueset-clinical-findings.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](communication-definitions.html#Communication.reasonReference) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html)) | Why was communication done?
 | |

| [payload](communication-definitions.html#Communication.payload) | | 0..* | [BackboneElement](backboneelement.html) | Message payload
 | |

| [content[x]](communication-definitions.html#Communication.payload.content_x_) | | 1..1 | | Message part content | |

| contentString | | | [string](datatypes.html#string) | | |

| contentAttachment | | | [Attachment](datatypes.html#Attachment) | | |

| contentReference | | | [Reference](references.html#Reference)([Any](resourcelist.html)) | | |

| [note](communication-definitions.html#Communication.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the communication
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Communication ([DomainResource](domainresource.html))[Business identifiers assigned to this communication by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](communication-definitions.html#Communication.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The URL pointing to a FHIR-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationinstantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..*] « [PlanDefinition](plandefinition.html#PlanDefinition)| [ActivityDefinition](activitydefinition.html#ActivityDefinition)|[Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire) »[The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this CommunicationinstantiatesUri](communication-definitions.html#Communication.instantiatesUri) : [uri](datatypes.html#uri) [0..*][An order, proposal or plan fulfilled in whole or in part by this CommunicationbasedOn](communication-definitions.html#Communication.basedOn) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Part of this actionpartOf](communication-definitions.html#Communication.partOf) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Prior communication that this communication is in response toinResponseTo](communication-definitions.html#Communication.inResponseTo) : [Reference](references.html#Reference) [0..*] « [Communication](communication.html#Communication) »[The status of the transmission (this element modifies the meaning of other elements)status](communication-definitions.html#Communication.status) : [code](datatypes.html#code) [1..1] « [The status of the communication. (Strength=Required)EventStatus](valueset-event-status.html)! »[Captures the reason for the current state of the CommunicationstatusReason](communication-definitions.html#Communication.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the reason why a communication did not happen. (Strength=Example)CommunicationNotDoneReason](valueset-communication-not-done-reason.html)?? »[The type of message conveyed such as alert, notification, reminder, instruction, etccategory](communication-definitions.html#Communication.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for general categories of communications such as alerts, instructions, etc. (Strength=Example)CommunicationCategory](valueset-communication-category.html)?? »[Characterizes how quickly the planned or in progress communication must be addressed. Includes concepts such as stat, urgent, routinepriority](communication-definitions.html#Communication.priority) : [code](datatypes.html#code) [0..1] « [Codes indicating the relative importance of a communication. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[A channel that was used for this communication (e.g. email, fax)medium](communication-definitions.html#Communication.medium) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)v3.ParticipationMode](v3/ParticipationMode/vs.html)?? »[The patient or group that was the focus of this communicationsubject](communication-definitions.html#Communication.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[Description of the purpose/content, similar to a subject line in an emailtopic](communication-definitions.html#Communication.topic) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing the purpose or content of the communication. (Strength=Example)CommunicationTopic](valueset-communication-topic.html)?? »[Other resources that pertain to this communication and to which this communication should be associatedabout](communication-definitions.html#Communication.about) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[The Encounter during which this Communication was created or to which the creation of this record is tightly associatedencounter](communication-definitions.html#Communication.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The time when this communication was sentsent](communication-definitions.html#Communication.sent) : [dateTime](datatypes.html#dateTime) [0..1][The time when this communication arrived at the destinationreceived](communication-definitions.html#Communication.received) : [dateTime](datatypes.html#dateTime) [0..1][The entity (e.g. person, organization, clinical information system, care team or device) which was the target of the communication. If receipts need to be tracked by an individual, a separate resource instance will need to be created for each recipient. Multiple recipient communications are intended where either receipts are not tracked (e.g. a mass mail-out) or a receipt is captured in aggregate (all emails confirmed received by a particular time)recipient](communication-definitions.html#Communication.recipient) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)| [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)| [HealthcareService](healthcareservice.html#HealthcareService) »[The entity (e.g. person, organization, clinical information system, or device) which was the source of the communicationsender](communication-definitions.html#Communication.sender) : [Reference](references.html#Reference) [0..1] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService) »[The reason or justification for the communicationreasonCode](communication-definitions.html#Communication.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for describing reasons for the occurrence of a communication. (Strength=Example)SNOMEDCTClinicalFindings](valueset-clinical-findings.html)?? »[Indicates another resource whose existence justifies this communicationreasonReference](communication-definitions.html#Communication.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)| [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference) »[Additional notes or commentary about the communication by the sender, receiver or other interested partiesnote](communication-definitions.html#Communication.note) : [Annotation](datatypes.html#Annotation) [0..*]Payload[A communicated content (or for multi-part communications, one portion of the communication)content[x]](communication-definitions.html#Communication.payload.content_x_) : [Type](formats.html#umlchoice) [1..1] « [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html#Any)) »
[Text, attachment(s), or resource(s) that was communicated to the recipientpayload](communication-definitions.html#Communication.payload)[0..*]
 

**XML Template**

 

 
```
<[**Communication**](communication-definitions.html#Communication) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](communication-definitions.html#Communication.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Unique identifier](terminologies.html#unbound) --></identifier>
 <[**instantiatesCanonical**](communication-definitions.html#Communication.instantiatesCanonical)><!-- **0..*** [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|
 [Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire)) [Instantiates FHIR protocol or definition](terminologies.html#unbound) --></instantiatesCanonical>
 <[**instantiatesUri**](communication-definitions.html#Communication.instantiatesUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Instantiates external protocol or definition](terminologies.html#unbound) -->
 <[**basedOn**](communication-definitions.html#Communication.basedOn)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Request fulfilled by this communication](terminologies.html#unbound) --></basedOn>
 <[**partOf**](communication-definitions.html#Communication.partOf)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Part of this action](terminologies.html#unbound) --></partOf>
 <[**inResponseTo**](communication-definitions.html#Communication.inResponseTo)><!-- **0..*** [Reference](references.html#Reference)([Communication](communication.html#Communication)) [Reply to](terminologies.html#unbound) --></inResponseTo>
 <[**status**](communication-definitions.html#Communication.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown](valueset-event-status.html) -->
 <[**statusReason**](communication-definitions.html#Communication.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](valueset-communication-not-done-reason.html) --></statusReason>
 <[**category**](communication-definitions.html#Communication.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Message category](valueset-communication-category.html) --></category>
 <[**priority**](communication-definitions.html#Communication.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**medium**](communication-definitions.html#Communication.medium)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A channel of communication](v3/ParticipationMode/vs.html) --></medium>
 <[**subject**](communication-definitions.html#Communication.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Focus of message](terminologies.html#unbound) --></subject>
 <[**topic**](communication-definitions.html#Communication.topic)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Description of the purpose/content](valueset-communication-topic.html) --></topic>
 <[**about**](communication-definitions.html#Communication.about)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Resources that pertain to this communication](terminologies.html#unbound) --></about>
 <[**encounter**](communication-definitions.html#Communication.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**sent**](communication-definitions.html#Communication.sent) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When sent](terminologies.html#unbound) -->
 <[**received**](communication-definitions.html#Communication.received) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When received](terminologies.html#unbound) -->
 <[**recipient**](communication-definitions.html#Communication.recipient)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message recipient](terminologies.html#unbound) --></recipient>
 <[**sender**](communication-definitions.html#Communication.sender)><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message sender](terminologies.html#unbound) --></sender>
 <[**reasonCode**](communication-definitions.html#Communication.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Indication for message](valueset-clinical-findings.html) --></reasonCode>
 <[**reasonReference**](communication-definitions.html#Communication.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) [Why was communication done?](terminologies.html#unbound) --></reasonReference>
 <[**payload**](communication-definitions.html#Communication.payload)> <!-- **0..*** Message payload -->
 <[**content[x]**](communication-definitions.html#Communication.payload.content[x])><!-- **1..1** [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html)) [Message part content](terminologies.html#unbound) --></content[x]>
 </payload>
 <[**note**](communication-definitions.html#Communication.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the communication](terminologies.html#unbound) --></note>
</Communication>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Communication**](communication-definitions.html#Communication)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](communication-definitions.html#Communication.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Unique identifier](terminologies.html#unbound)
 "[instantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical)" : [{ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|
 [Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire)) }], // [Instantiates FHIR protocol or definition](terminologies.html#unbound)
 "[instantiatesUri](communication-definitions.html#Communication.instantiatesUri)" : ["<[uri](datatypes.html#uri)>"], // [Instantiates external protocol or definition](terminologies.html#unbound)
 "[basedOn](communication-definitions.html#Communication.basedOn)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Request fulfilled by this communication](terminologies.html#unbound)
 "[partOf](communication-definitions.html#Communication.partOf)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Part of this action](terminologies.html#unbound)
 "[inResponseTo](communication-definitions.html#Communication.inResponseTo)" : [{ [Reference](references.html#Reference)([Communication](communication.html#Communication)) }], // [Reply to](terminologies.html#unbound)
 "[status](communication-definitions.html#Communication.status)" : "<[code](datatypes.html#code)>", // **R!** [preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown](valueset-event-status.html)
 "[statusReason](communication-definitions.html#Communication.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](valueset-communication-not-done-reason.html)
 "[category](communication-definitions.html#Communication.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Message category](valueset-communication-category.html)
 "[priority](communication-definitions.html#Communication.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[medium](communication-definitions.html#Communication.medium)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [A channel of communication](v3/ParticipationMode/vs.html)
 "[subject](communication-definitions.html#Communication.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [Focus of message](terminologies.html#unbound)
 "[topic](communication-definitions.html#Communication.topic)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Description of the purpose/content](valueset-communication-topic.html)
 "[about](communication-definitions.html#Communication.about)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Resources that pertain to this communication](terminologies.html#unbound)
 "[encounter](communication-definitions.html#Communication.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[sent](communication-definitions.html#Communication.sent)" : "<[dateTime](datatypes.html#dateTime)>", // [When sent](terminologies.html#unbound)
 "[received](communication-definitions.html#Communication.received)" : "<[dateTime](datatypes.html#dateTime)>", // [When received](terminologies.html#unbound)
 "[recipient](communication-definitions.html#Communication.recipient)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) }], // [Message recipient](terminologies.html#unbound)
 "[sender](communication-definitions.html#Communication.sender)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) }, // [Message sender](terminologies.html#unbound)
 "[reasonCode](communication-definitions.html#Communication.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Indication for message](valueset-clinical-findings.html)
 "[reasonReference](communication-definitions.html#Communication.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) }], // [Why was communication done?](terminologies.html#unbound)
 "[payload](communication-definitions.html#Communication.payload)" : [{ // [Message payload](terminologies.html#unbound)
 // content[x]: Message part content. One of these 3:
 "[contentString](communication-definitions.html#Communication.payload.contentString)" : "<[string](datatypes.html#string)>"
 "[contentAttachment](communication-definitions.html#Communication.payload.contentAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[contentReference](communication-definitions.html#Communication.payload.contentReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }
 }],
 "[note](communication-definitions.html#Communication.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about the communication](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Communication**](communication-definitions.html#Communication);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Communication.identifier](communication-definitions.html#Communication.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Unique identifier
 fhir:[Communication.instantiatesCanonical](communication-definitions.html#Communication.instantiatesCanonical) [ [canonical](datatypes.html#canonical)([PlanDefinition](plandefinition.html#PlanDefinition)|[ActivityDefinition](activitydefinition.html#ActivityDefinition)|[Measure](measure.html#Measure)|[OperationDefinition](operationdefinition.html#OperationDefinition)|[Questionnaire](questionnaire.html#Questionnaire)) ], ... ; # 0..* Instantiates FHIR protocol or definition
 fhir:[Communication.instantiatesUri](communication-definitions.html#Communication.instantiatesUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Instantiates external protocol or definition
 fhir:[Communication.basedOn](communication-definitions.html#Communication.basedOn) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Request fulfilled by this communication
 fhir:[Communication.partOf](communication-definitions.html#Communication.partOf) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Part of this action
 fhir:[Communication.inResponseTo](communication-definitions.html#Communication.inResponseTo) [ [Reference](references.html#Reference)([Communication](communication.html#Communication)) ], ... ; # 0..* Reply to
 fhir:[Communication.status](communication-definitions.html#Communication.status) [ [code](datatypes.html#code) ]; # 1..1 preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
 fhir:[Communication.statusReason](communication-definitions.html#Communication.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[Communication.category](communication-definitions.html#Communication.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Message category
 fhir:[Communication.priority](communication-definitions.html#Communication.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[Communication.medium](communication-definitions.html#Communication.medium) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A channel of communication
 fhir:[Communication.subject](communication-definitions.html#Communication.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 Focus of message
 fhir:[Communication.topic](communication-definitions.html#Communication.topic) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Description of the purpose/content
 fhir:[Communication.about](communication-definitions.html#Communication.about) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Resources that pertain to this communication
 fhir:[Communication.encounter](communication-definitions.html#Communication.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[Communication.sent](communication-definitions.html#Communication.sent) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When sent
 fhir:[Communication.received](communication-definitions.html#Communication.received) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When received
 fhir:[Communication.recipient](communication-definitions.html#Communication.recipient) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|
 [CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) ], ... ; # 0..* Message recipient
 fhir:[Communication.sender](communication-definitions.html#Communication.sender) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [HealthcareService](healthcareservice.html#HealthcareService)) ]; # 0..1 Message sender
 fhir:[Communication.reasonCode](communication-definitions.html#Communication.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Indication for message
 fhir:[Communication.reasonReference](communication-definitions.html#Communication.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference)) ], ... ; # 0..* Why was communication done?
 fhir:[Communication.payload](communication-definitions.html#Communication.payload) [ # 0..* Message payload
 # [Communication.payload.content[x]](communication-definitions.html#Communication.payload.content[x]) : 1..1 Message part content. One of these 3
 fhir:[Communication.payload.contentString](communication-definitions.html#Communication.payload.contentString) [ [string](datatypes.html#string) ]
 fhir:[Communication.payload.contentAttachment](communication-definitions.html#Communication.payload.contentAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Communication.payload.contentReference](communication-definitions.html#Communication.payload.contentReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]
 ], ...;
 fhir:[Communication.note](communication-definitions.html#Communication.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the communication
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Communication](communication.html#Communication)
 | 
 | 
 |

 | 
 Communication.instantiatesCanonical | 
 
 

 Added Element

 

 | 
 |

 | 
 Communication.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.inResponseTo | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/event-status to http://hl7.org/fhir/ValueSet/event-status|4.0.1

 

 | 
 |

 | 
 Communication.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.priority | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.topic | 
 
 

 - Max Cardinality changed from * to 1

 - Type changed from Reference(Resource) to CodeableConcept

 

 | 
 |

 | 
 Communication.about | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 Communication.recipient | 
 
 

 - Type Reference: Added Target Types PractitionerRole, CareTeam, HealthcareService

 

 | 
 |

 | 
 Communication.sender | 
 
 

 - Type Reference: Added Target Types PractitionerRole, HealthcareService

 

 | 
 |

 | 
 Communication.reasonReference | 
 
 

 - Type Reference: Added Target Types DiagnosticReport, DocumentReference

 

 | 
 |

 | 
 Communication.definition | 
 
 

 - deleted

 

 | 
 |

 | 
 Communication.notDone | 
 
 

 - deleted

 

 | 
 |

 | 
 Communication.notDoneReason | 
 
 

 - deleted

 

 | 
 |

 | 
 Communication.context | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](communication.diff.xml) or [JSON](communication.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](communication-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and 2 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](communication-profiles.html) and the alternate definitions:
Master Definition [XML](communication.profile.xml.html) + [JSON](communication.profile.json.html),
[XML](xml.html) [Schema](communication.xsd)/[Schematron](communication.sch) + [JSON](json.html) 
[Schema](communication.schema.json.html), [ShEx](communication.shex.html) (for [Turtle](rdf.html)) + [see the extensions](communication-profiles.html) & the [dependency analysis](communication-dependencies.html)

### 8.20.3.1 
Terminology Bindings
 [
](communication.html#tx)

 | Path | Definition | Type | Reference | |

 | Communication.status | The status of the communication. | [Required](terminologies.html#required) | [EventStatus](valueset-event-status.html) | |

 | Communication.statusReason | Codes for the reason why a communication did not happen. | [Example](terminologies.html#example) | [CommunicationNotDoneReason](valueset-communication-not-done-reason.html) | |

 | Communication.category | Codes for general categories of communications such as alerts, instructions, etc. | [Example](terminologies.html#example) | [CommunicationCategory](valueset-communication-category.html) | |

 | Communication.priority | Codes indicating the relative importance of a communication. | [Required](terminologies.html#required) | [RequestPriority](valueset-request-priority.html) | |

 | Communication.medium | Codes for communication mediums such as phone, fax, email, in person, etc. | [Example](terminologies.html#example) | [v3.ParticipationMode](v3/ParticipationMode/vs.html) | |

 | Communication.topic | Codes describing the purpose or content of the communication. | [Example](terminologies.html#example) | [CommunicationTopic](valueset-communication-topic.html) | |

 | Communication.reasonCode | Codes for describing reasons for the occurrence of a communication. | [Example](terminologies.html#example) | [SNOMEDCTClinicalFindings](valueset-clinical-findings.html) | |

 

 
 

 **Notes to reviewers:**
 

 

 At this time, the code bindings are placeholders to be fleshed out upon further review by the community.*
 

### 8.20.3.2 Communication.sender and Communication.recipient [
](communication.html#8.20.3.2)

 Communication.sender allows Device | Organization | Patient | Practitioner | PractitionerRole | RelatedPerson | HealthcareService and Communication.recipient allows Device | Organization | Patient | Practitioner | PractitionerRole | RelatedPerson | Group | CareTeam | HealthcareService - but it is not unusual to have a communication target - even a defined one - where it is unknown what kind of role the person is playing.
 

 

 If the communication is to or from an individual whose role is not known (practitioner, patient or related person) -
 for example, only email address is captured in the system - then RelatedPerson should be used by default.
 

## 8.20.4 Search Parameters [
](communication.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| based-on | [reference](search.html#reference) | Request fulfilled by this communication | Communication.basedOn
(Any) | | |

| category | [token](search.html#token) | Message category | Communication.category | | |

| encounter | [reference](search.html#reference) | Encounter created as part of | Communication.encounter
([Encounter](encounter.html)) | | |

| identifier | [token](search.html#token) | Unique identifier | Communication.identifier | | |

| instantiates-canonical | [reference](search.html#reference) | Instantiates FHIR protocol or definition | Communication.instantiatesCanonical
([Questionnaire](questionnaire.html), [Measure](measure.html), [PlanDefinition](plandefinition.html), [OperationDefinition](operationdefinition.html), [ActivityDefinition](activitydefinition.html)) | | |

| instantiates-uri | [uri](search.html#uri) | Instantiates external protocol or definition | Communication.instantiatesUri | | |

| medium | [token](search.html#token) | A channel of communication | Communication.medium | | |

| part-of | [reference](search.html#reference) | Part of this action | Communication.partOf
(Any) | | |

| patient | [reference](search.html#reference) | Focus of message | Communication.subject.where(resolve() is Patient)
([Patient](patient.html)) | | |

| received | [date](search.html#date) | When received | Communication.received | | |

| recipient | [reference](search.html#reference) | Message recipient | Communication.recipient
([Practitioner](practitioner.html), [Group](group.html), [Organization](organization.html), [CareTeam](careteam.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| sender | [reference](search.html#reference) | Message sender | Communication.sender
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| sent | [date](search.html#date) | When sent | Communication.sent | | |

| status | [token](search.html#token) | preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown | Communication.status | | |

| subject | [reference](search.html#reference) | Focus of message | Communication.subject
([Group](group.html), [Patient](patient.html)) | | |