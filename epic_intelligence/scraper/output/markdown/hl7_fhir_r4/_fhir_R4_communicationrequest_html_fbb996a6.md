# CommunicationRequest - FHIR v4.0.1Business identifiers assigned to this communication request by the performer or other systems which remain constant as the resource is updated and propagates from server to serverA plan or proposal that is fulfilled in whole or in part by this requestCompleted or terminated request(s) whose function is taken by this new requestA shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar formThe status of the proposal or order (this element modifies the meaning of other elements)The status of the communication request. (Strength=Required)Captures the reason for the current state of the CommunicationRequestThe type of message to be sent such as alert, notification, reminder, instruction, etcCodes for general categories of communications such as alerts, instruction, etc. (Strength=Example)Characterizes how quickly the proposed act must be initiated. Includes concepts such as stat, urgent, routineCodes indicating the relative importance of a communication request. (Strength=Required)If true indicates that the CommunicationRequest is asking for the specified action to *not* occur (this element modifies the meaning of other elements)A channel that was used for this communication (e.g. email, fax)Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)The patient or group that is the focus of this communication requestOther resources that pertain to this communication request and to which this communication request should be associatedThe Encounter during which this CommunicationRequest was created or to which the creation of this record is tightly associatedThe time when this communication is to occurFor draft requests, indicates the date of initial creation.  For requests with other statuses, indicates the date of activationThe device, individual, or organization who initiated the request and has responsibility for its activationThe entity (e.g. person, organization, clinical information system, device, group, or care team) which is the intended target of the communicationThe entity (e.g. person, organization, clinical information system, or device) which is to be the source of the communicationDescribes why the request is being made in coded or textual formCodes for describing reasons for the occurrence of a communication. (Strength=Example)Indicates another resource whose existence justifies this requestComments made about the request by the requester, sender, recipient, subject or other participantsThe communicated content (or for multi-part communications, one portion of the communication)Text, attachment(s), or resource(s) to be communicated to the recipientBusiness identifiers assigned to this communication request by the performer or other systems which remain constant as the resource is updated and propagates from server to serverA plan or proposal that is fulfilled in whole or in part by this requestCompleted or terminated request(s) whose function is taken by this new requestA shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar formThe status of the proposal or order (this element modifies the meaning of other elements)The status of the communication request. (Strength=Required)Captures the reason for the current state of the CommunicationRequestThe type of message to be sent such as alert, notification, reminder, instruction, etcCodes for general categories of communications such as alerts, instruction, etc. (Strength=Example)Characterizes how quickly the proposed act must be initiated. Includes concepts such as stat, urgent, routineCodes indicating the relative importance of a communication request. (Strength=Required)If true indicates that the CommunicationRequest is asking for the specified action to *not* occur (this element modifies the meaning of other elements)A channel that was used for this communication (e.g. email, fax)Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)The patient or group that is the focus of this communication requestOther resources that pertain to this communication request and to which this communication request should be associatedThe Encounter during which this CommunicationRequest was created or to which the creation of this record is tightly associatedThe time when this communication is to occurFor draft requests, indicates the date of initial creation.  For requests with other statuses, indicates the date of activationThe device, individual, or organization who initiated the request and has responsibility for its activationThe entity (e.g. person, organization, clinical information system, device, group, or care team) which is the intended target of the communicationThe entity (e.g. person, organization, clinical information system, or device) which is to be the source of the communicationDescribes why the request is being made in coded or textual formCodes for describing reasons for the occurrence of a communication. (Strength=Example)Indicates another resource whose existence justifies this requestComments made about the request by the requester, sender, recipient, subject or other participantsThe communicated content (or for multi-part communications, one portion of the communication)Text, attachment(s), or resource(s) to be communicated to the recipient

> Source: https://hl7.org/fhir/R4/communicationrequest.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/communicationrequest.html) [R4B](http://hl7.org/fhir/R4B/communicationrequest.html) **R4** [R3](http://hl7.org/fhir/STU3/communicationrequest.html) [R2](http://hl7.org/fhir/DSTU2/communicationrequest.html)
 

# 8.21 Resource CommunicationRequest - Content [
](communicationrequest.html#8.21)

| [Patient Care ](http://www.hl7.org/Special/committees/patientcare/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.

## 8.21.1 Scope and Usage [
](communicationrequest.html#scope)

 

CommunicationRequest is one of the [request](workflow.html#request) resources in the FHIR [workflow](workflow.html) specification.

This resource is a record of a request for a communication to be performed. A communication is a conveyance of information from one entity, a sender, to another entity, a receiver. The requester requests the sender to send the payload to the recipient. The sender and receivers may be patients, practitioners, related persons, organizations, and devices. Uses of communication request include:

- A computer-based decision-support system requesting a reminder or alert be delivered to a responsible provider

- A physician requesting notification from the nurse if a patient's temperature exceeds a value

- A monitoring system or a provider requesting a staff member or department to notify a public health agency of a patient presenting with a communicable disease reportable to the public health agency

- A computer-based decision-support system proposes to send educational material to a patient

 

## 8.21.2 Boundaries and Relationships [
](communicationrequest.html#bnr)

This resource is a record of a request. It does not represent the actual flow of communication.

The use of **CommunicationRequest** excludes requests for referrals and requests for therapy or counseling which would be handled by the [ServiceRequest](servicerequest.html) resource.
The performance of a **CommunicationRequest** may result in a [Communication](communication.html) resource.

 

This resource is referenced by [CarePlan](careplan.html#CarePlan), [ClaimResponse](claimresponse.html#ClaimResponse) and itself

## 8.21.3 
Resource Content
 [
](communicationrequest.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [CommunicationRequest](communicationrequest-definitions.html#CommunicationRequest) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A request for information to be sent to a receiver**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](communicationrequest-definitions.html#CommunicationRequest.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Unique identifier
 | |

| [basedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Fulfills plan or proposal
 | |

| [replaces](communicationrequest-definitions.html#CommunicationRequest.replaces) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html)) | Request(s) replaced by this request
 | |

| [groupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Composite request this is part of | |

| [status](communicationrequest-definitions.html#CommunicationRequest.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | draft | active | on-hold | revoked | completed | entered-in-error | unknown
[RequestStatus](valueset-request-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status | |

| [category](communicationrequest-definitions.html#CommunicationRequest.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Message category
[CommunicationCategory](valueset-communication-category.html) ([Example](terminologies.html#example))
 | |

| [priority](communicationrequest-definitions.html#CommunicationRequest.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | True if request is prohibiting action | |

| [medium](communicationrequest-definitions.html#CommunicationRequest.medium) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A channel of communication
[v3 Code System ParticipationMode](v3/ParticipationMode/vs.html) ([Example](terminologies.html#example))
 | |

| [subject](communicationrequest-definitions.html#CommunicationRequest.subject) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Focus of message | |

| [about](communicationrequest-definitions.html#CommunicationRequest.about) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Resources that pertain to this communication request
 | |

| [encounter](communicationrequest-definitions.html#CommunicationRequest.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [payload](communicationrequest-definitions.html#CommunicationRequest.payload) | | 0..* | [BackboneElement](backboneelement.html) | Message payload
 | |

| [content[x]](communicationrequest-definitions.html#CommunicationRequest.payload.content_x_) | | 1..1 | | Message part content | |

| contentString | | | [string](datatypes.html#string) | | |

| contentAttachment | | | [Attachment](datatypes.html#Attachment) | | |

| contentReference | | | [Reference](references.html#Reference)([Any](resourcelist.html)) | | |

| [occurrence[x]](communicationrequest-definitions.html#CommunicationRequest.occurrence_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | When scheduled | |

| occurrenceDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| occurrencePeriod | | | [Period](datatypes.html#Period) | | |

| [authoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When request transitioned to being actionable | |

| [requester](communicationrequest-definitions.html#CommunicationRequest.requester) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Device](device.html)) | Who/what is requesting service | |

| [recipient](communicationrequest-definitions.html#CommunicationRequest.recipient) | | 0..* | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Group](group.html) | [CareTeam](careteam.html) | [HealthcareService](healthcareservice.html)) | Message recipient
 | |

| [sender](communicationrequest-definitions.html#CommunicationRequest.sender) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [HealthcareService](healthcareservice.html)) | Message sender | |

| [reasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Why is communication needed?
[v3 Code System ActReason](v3/ActReason/vs.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html)) | Why is communication needed?
 | |

| [note](communicationrequest-definitions.html#CommunicationRequest.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about communication request
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - CommunicationRequest ([DomainResource](domainresource.html))[Business identifiers assigned to this communication request by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](communicationrequest-definitions.html#CommunicationRequest.identifier) : [Identifier](datatypes.html#Identifier) [0..*][A plan or proposal that is fulfilled in whole or in part by this requestbasedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Completed or terminated request(s) whose function is taken by this new requestreplaces](communicationrequest-definitions.html#CommunicationRequest.replaces) : [Reference](references.html#Reference) [0..*] « [CommunicationRequest](communicationrequest.html#CommunicationRequest) »[A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar formgroupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][The status of the proposal or order (this element modifies the meaning of other elements)status](communicationrequest-definitions.html#CommunicationRequest.status) : [code](datatypes.html#code) [1..1] « [The status of the communication request. (Strength=Required)RequestStatus](valueset-request-status.html)! »[Captures the reason for the current state of the CommunicationRequeststatusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][The type of message to be sent such as alert, notification, reminder, instruction, etccategory](communicationrequest-definitions.html#CommunicationRequest.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for general categories of communications such as alerts, instruction, etc. (Strength=Example)CommunicationCategory](valueset-communication-category.html)?? »[Characterizes how quickly the proposed act must be initiated. Includes concepts such as stat, urgent, routinepriority](communicationrequest-definitions.html#CommunicationRequest.priority) : [code](datatypes.html#code) [0..1] « [Codes indicating the relative importance of a communication request. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[If true indicates that the CommunicationRequest is asking for the specified action to *not* occur (this element modifies the meaning of other elements)doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) : [boolean](datatypes.html#boolean) [0..1][A channel that was used for this communication (e.g. email, fax)medium](communicationrequest-definitions.html#CommunicationRequest.medium) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)v3.ParticipationMode](v3/ParticipationMode/vs.html)?? »[The patient or group that is the focus of this communication requestsubject](communicationrequest-definitions.html#CommunicationRequest.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[Other resources that pertain to this communication request and to which this communication request should be associatedabout](communicationrequest-definitions.html#CommunicationRequest.about) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[The Encounter during which this CommunicationRequest was created or to which the creation of this record is tightly associatedencounter](communicationrequest-definitions.html#CommunicationRequest.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The time when this communication is to occuroccurrence[x]](communicationrequest-definitions.html#CommunicationRequest.occurrence_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »[For draft requests, indicates the date of initial creation. For requests with other statuses, indicates the date of activationauthoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn) : [dateTime](datatypes.html#dateTime) [0..1][The device, individual, or organization who initiated the request and has responsibility for its activationrequester](communicationrequest-definitions.html#CommunicationRequest.requester) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device) »[The entity (e.g. person, organization, clinical information system, device, group, or care team) which is the intended target of the communicationrecipient](communicationrequest-definitions.html#CommunicationRequest.recipient) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)| [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)| [HealthcareService](healthcareservice.html#HealthcareService) »[The entity (e.g. person, organization, clinical information system, or device) which is to be the source of the communicationsender](communicationrequest-definitions.html#CommunicationRequest.sender) : [Reference](references.html#Reference) [0..1] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService) »[Describes why the request is being made in coded or textual formreasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for describing reasons for the occurrence of a communication. (Strength=Example)v3.ActReason](v3/ActReason/vs.html)?? »[Indicates another resource whose existence justifies this requestreasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)| [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference) »[Comments made about the request by the requester, sender, recipient, subject or other participantsnote](communicationrequest-definitions.html#CommunicationRequest.note) : [Annotation](datatypes.html#Annotation) [0..*]Payload[The communicated content (or for multi-part communications, one portion of the communication)content[x]](communicationrequest-definitions.html#CommunicationRequest.payload.content_x_) : [Type](formats.html#umlchoice) [1..1] « [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html#Any)) »
[Text, attachment(s), or resource(s) to be communicated to the recipientpayload](communicationrequest-definitions.html#CommunicationRequest.payload)[0..*]
 

 

 

**XML Template**

 

 
```
<[**CommunicationRequest**](communicationrequest-definitions.html#CommunicationRequest) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](communicationrequest-definitions.html#CommunicationRequest.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Unique identifier](terminologies.html#unbound) --></identifier>
 <[**basedOn**](communicationrequest-definitions.html#CommunicationRequest.basedOn)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Fulfills plan or proposal](terminologies.html#unbound) --></basedOn>
 <[**replaces**](communicationrequest-definitions.html#CommunicationRequest.replaces)><!-- **0..*** [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) [Request(s) replaced by this request](terminologies.html#unbound) --></replaces>
 <[**groupIdentifier**](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Composite request this is part of](terminologies.html#unbound) --></groupIdentifier>
 <[**status**](communicationrequest-definitions.html#CommunicationRequest.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [draft | active | on-hold | revoked | completed | entered-in-error | unknown](valueset-request-status.html) -->
 <[**statusReason**](communicationrequest-definitions.html#CommunicationRequest.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](terminologies.html#unbound) --></statusReason>
 <[**category**](communicationrequest-definitions.html#CommunicationRequest.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Message category](valueset-communication-category.html) --></category>
 <[**priority**](communicationrequest-definitions.html#CommunicationRequest.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**doNotPerform**](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [True if request is prohibiting action](terminologies.html#unbound) -->
 <[**medium**](communicationrequest-definitions.html#CommunicationRequest.medium)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A channel of communication](v3/ParticipationMode/vs.html) --></medium>
 <[**subject**](communicationrequest-definitions.html#CommunicationRequest.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Focus of message](terminologies.html#unbound) --></subject>
 <[**about**](communicationrequest-definitions.html#CommunicationRequest.about)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Resources that pertain to this communication request](terminologies.html#unbound) --></about>
 <[**encounter**](communicationrequest-definitions.html#CommunicationRequest.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**payload**](communicationrequest-definitions.html#CommunicationRequest.payload)> <!-- **0..*** Message payload -->
 <[**content[x]**](communicationrequest-definitions.html#CommunicationRequest.payload.content[x])><!-- **1..1** [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html)) [Message part content](terminologies.html#unbound) --></content[x]>
 </payload>
 <[**occurrence[x]**](communicationrequest-definitions.html#CommunicationRequest.occurrence[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [When scheduled](terminologies.html#unbound) --></occurrence[x]>
 <[**authoredOn**](communicationrequest-definitions.html#CommunicationRequest.authoredOn) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When request transitioned to being actionable](terminologies.html#unbound) -->
 <[**requester**](communicationrequest-definitions.html#CommunicationRequest.requester)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) [Who/what is requesting service](terminologies.html#unbound) --></requester>
 <[**recipient**](communicationrequest-definitions.html#CommunicationRequest.recipient)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message recipient](terminologies.html#unbound) --></recipient>
 <[**sender**](communicationrequest-definitions.html#CommunicationRequest.sender)><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message sender](terminologies.html#unbound) --></sender>
 <[**reasonCode**](communicationrequest-definitions.html#CommunicationRequest.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Why is communication needed?](v3/ActReason/vs.html) --></reasonCode>
 <[**reasonReference**](communicationrequest-definitions.html#CommunicationRequest.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) [Why is communication needed?](terminologies.html#unbound) --></reasonReference>
 <[**note**](communicationrequest-definitions.html#CommunicationRequest.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about communication request](terminologies.html#unbound) --></note>
</CommunicationRequest>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**CommunicationRequest**](communicationrequest-definitions.html#CommunicationRequest)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](communicationrequest-definitions.html#CommunicationRequest.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Unique identifier](terminologies.html#unbound)
 "[basedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Fulfills plan or proposal](terminologies.html#unbound)
 "[replaces](communicationrequest-definitions.html#CommunicationRequest.replaces)" : [{ [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) }], // [Request(s) replaced by this request](terminologies.html#unbound)
 "[groupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Composite request this is part of](terminologies.html#unbound)
 "[status](communicationrequest-definitions.html#CommunicationRequest.status)" : "<[code](datatypes.html#code)>", // **R!** [draft | active | on-hold | revoked | completed | entered-in-error | unknown](valueset-request-status.html)
 "[statusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](terminologies.html#unbound)
 "[category](communicationrequest-definitions.html#CommunicationRequest.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Message category](valueset-communication-category.html)
 "[priority](communicationrequest-definitions.html#CommunicationRequest.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform)" : <[boolean](datatypes.html#boolean)>, // [True if request is prohibiting action](terminologies.html#unbound)
 "[medium](communicationrequest-definitions.html#CommunicationRequest.medium)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [A channel of communication](v3/ParticipationMode/vs.html)
 "[subject](communicationrequest-definitions.html#CommunicationRequest.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [Focus of message](terminologies.html#unbound)
 "[about](communicationrequest-definitions.html#CommunicationRequest.about)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Resources that pertain to this communication request](terminologies.html#unbound)
 "[encounter](communicationrequest-definitions.html#CommunicationRequest.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[payload](communicationrequest-definitions.html#CommunicationRequest.payload)" : [{ // [Message payload](terminologies.html#unbound)
 // content[x]: Message part content. One of these 3:
 "[contentString](communicationrequest-definitions.html#CommunicationRequest.payload.contentString)" : "<[string](datatypes.html#string)>"
 "[contentAttachment](communicationrequest-definitions.html#CommunicationRequest.payload.contentAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[contentReference](communicationrequest-definitions.html#CommunicationRequest.payload.contentReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }
 }],
 // occurrence[x]: When scheduled. One of these 2:
 "[occurrenceDateTime](communicationrequest-definitions.html#CommunicationRequest.occurrenceDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[occurrencePeriod](communicationrequest-definitions.html#CommunicationRequest.occurrencePeriod)" : { [Period](datatypes.html#Period) },
 "[authoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn)" : "<[dateTime](datatypes.html#dateTime)>", // [When request transitioned to being actionable](terminologies.html#unbound)
 "[requester](communicationrequest-definitions.html#CommunicationRequest.requester)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) }, // [Who/what is requesting service](terminologies.html#unbound)
 "[recipient](communicationrequest-definitions.html#CommunicationRequest.recipient)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) }], // [Message recipient](terminologies.html#unbound)
 "[sender](communicationrequest-definitions.html#CommunicationRequest.sender)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) }, // [Message sender](terminologies.html#unbound)
 "[reasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Why is communication needed?](v3/ActReason/vs.html)
 "[reasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) }], // [Why is communication needed?](terminologies.html#unbound)
 "[note](communicationrequest-definitions.html#CommunicationRequest.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about communication request](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**CommunicationRequest**](communicationrequest-definitions.html#CommunicationRequest);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[CommunicationRequest.identifier](communicationrequest-definitions.html#CommunicationRequest.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Unique identifier
 fhir:[CommunicationRequest.basedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Fulfills plan or proposal
 fhir:[CommunicationRequest.replaces](communicationrequest-definitions.html#CommunicationRequest.replaces) [ [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) ], ... ; # 0..* Request(s) replaced by this request
 fhir:[CommunicationRequest.groupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Composite request this is part of
 fhir:[CommunicationRequest.status](communicationrequest-definitions.html#CommunicationRequest.status) [ [code](datatypes.html#code) ]; # 1..1 draft | active | on-hold | revoked | completed | entered-in-error | unknown
 fhir:[CommunicationRequest.statusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[CommunicationRequest.category](communicationrequest-definitions.html#CommunicationRequest.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Message category
 fhir:[CommunicationRequest.priority](communicationrequest-definitions.html#CommunicationRequest.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[CommunicationRequest.doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) [ [boolean](datatypes.html#boolean) ]; # 0..1 True if request is prohibiting action
 fhir:[CommunicationRequest.medium](communicationrequest-definitions.html#CommunicationRequest.medium) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A channel of communication
 fhir:[CommunicationRequest.subject](communicationrequest-definitions.html#CommunicationRequest.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 Focus of message
 fhir:[CommunicationRequest.about](communicationrequest-definitions.html#CommunicationRequest.about) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Resources that pertain to this communication request
 fhir:[CommunicationRequest.encounter](communicationrequest-definitions.html#CommunicationRequest.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[CommunicationRequest.payload](communicationrequest-definitions.html#CommunicationRequest.payload) [ # 0..* Message payload
 # [CommunicationRequest.payload.content[x]](communicationrequest-definitions.html#CommunicationRequest.payload.content[x]) : 1..1 Message part content. One of these 3
 fhir:[CommunicationRequest.payload.contentString](communicationrequest-definitions.html#CommunicationRequest.payload.contentString) [ [string](datatypes.html#string) ]
 fhir:[CommunicationRequest.payload.contentAttachment](communicationrequest-definitions.html#CommunicationRequest.payload.contentAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[CommunicationRequest.payload.contentReference](communicationrequest-definitions.html#CommunicationRequest.payload.contentReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]
 ], ...;
 # [CommunicationRequest.occurrence[x]](communicationrequest-definitions.html#CommunicationRequest.occurrence[x]) : 0..1 When scheduled. One of these 2
 fhir:[CommunicationRequest.occurrenceDateTime](communicationrequest-definitions.html#CommunicationRequest.occurrenceDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[CommunicationRequest.occurrencePeriod](communicationrequest-definitions.html#CommunicationRequest.occurrencePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[CommunicationRequest.authoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When request transitioned to being actionable
 fhir:[CommunicationRequest.requester](communicationrequest-definitions.html#CommunicationRequest.requester) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) ]; # 0..1 Who/what is requesting service
 fhir:[CommunicationRequest.recipient](communicationrequest-definitions.html#CommunicationRequest.recipient) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|
 [CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) ], ... ; # 0..* Message recipient
 fhir:[CommunicationRequest.sender](communicationrequest-definitions.html#CommunicationRequest.sender) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [HealthcareService](healthcareservice.html#HealthcareService)) ]; # 0..1 Message sender
 fhir:[CommunicationRequest.reasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Why is communication needed?
 fhir:[CommunicationRequest.reasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference)) ], ... ; # 0..* Why is communication needed?
 fhir:[CommunicationRequest.note](communicationrequest-definitions.html#CommunicationRequest.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about communication request
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [CommunicationRequest](communicationrequest.html#CommunicationRequest)
 | 
 | 
 |

 | 
 CommunicationRequest.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/request-status to http://hl7.org/fhir/ValueSet/request-status|4.0.1

 

 | 
 |

 | 
 CommunicationRequest.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.priority | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/request-priority to http://hl7.org/fhir/ValueSet/request-priority|4.0.1

 

 | 
 |

 | 
 CommunicationRequest.doNotPerform | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.about | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.requester | 
 
 

 - Type changed from BackboneElement to Reference(Practitioner | PractitionerRole | Organization | Patient | RelatedPerson | Device)

 

 | 
 |

 | 
 CommunicationRequest.recipient | 
 
 

 - Type Reference: Added Target Types PractitionerRole, HealthcareService

 

 | 
 |

 | 
 CommunicationRequest.sender | 
 
 

 - Type Reference: Added Target Types PractitionerRole, HealthcareService

 

 | 
 |

 | 
 CommunicationRequest.reasonReference | 
 
 

 - Type Reference: Added Target Types DiagnosticReport, DocumentReference

 

 | 
 |

 | 
 CommunicationRequest.topic | 
 
 

 - deleted

 

 | 
 |

 | 
 CommunicationRequest.context | 
 
 

 - deleted

 

 | 
 |

 | 
 CommunicationRequest.requester.agent | 
 
 

 - deleted

 

 | 
 |

 | 
 CommunicationRequest.requester.onBehalfOf | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](communicationrequest.diff.xml) or [JSON](communicationrequest.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](communicationrequest-version-maps.html) (status = 2 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [CommunicationRequest](communicationrequest-definitions.html#CommunicationRequest) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A request for information to be sent to a receiver**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](communicationrequest-definitions.html#CommunicationRequest.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Unique identifier
 | |

| [basedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Fulfills plan or proposal
 | |

| [replaces](communicationrequest-definitions.html#CommunicationRequest.replaces) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html)) | Request(s) replaced by this request
 | |

| [groupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Composite request this is part of | |

| [status](communicationrequest-definitions.html#CommunicationRequest.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | draft | active | on-hold | revoked | completed | entered-in-error | unknown
[RequestStatus](valueset-request-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status | |

| [category](communicationrequest-definitions.html#CommunicationRequest.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Message category
[CommunicationCategory](valueset-communication-category.html) ([Example](terminologies.html#example))
 | |

| [priority](communicationrequest-definitions.html#CommunicationRequest.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | True if request is prohibiting action | |

| [medium](communicationrequest-definitions.html#CommunicationRequest.medium) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A channel of communication
[v3 Code System ParticipationMode](v3/ParticipationMode/vs.html) ([Example](terminologies.html#example))
 | |

| [subject](communicationrequest-definitions.html#CommunicationRequest.subject) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Focus of message | |

| [about](communicationrequest-definitions.html#CommunicationRequest.about) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Resources that pertain to this communication request
 | |

| [encounter](communicationrequest-definitions.html#CommunicationRequest.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [payload](communicationrequest-definitions.html#CommunicationRequest.payload) | | 0..* | [BackboneElement](backboneelement.html) | Message payload
 | |

| [content[x]](communicationrequest-definitions.html#CommunicationRequest.payload.content_x_) | | 1..1 | | Message part content | |

| contentString | | | [string](datatypes.html#string) | | |

| contentAttachment | | | [Attachment](datatypes.html#Attachment) | | |

| contentReference | | | [Reference](references.html#Reference)([Any](resourcelist.html)) | | |

| [occurrence[x]](communicationrequest-definitions.html#CommunicationRequest.occurrence_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | When scheduled | |

| occurrenceDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| occurrencePeriod | | | [Period](datatypes.html#Period) | | |

| [authoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When request transitioned to being actionable | |

| [requester](communicationrequest-definitions.html#CommunicationRequest.requester) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Device](device.html)) | Who/what is requesting service | |

| [recipient](communicationrequest-definitions.html#CommunicationRequest.recipient) | | 0..* | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Group](group.html) | [CareTeam](careteam.html) | [HealthcareService](healthcareservice.html)) | Message recipient
 | |

| [sender](communicationrequest-definitions.html#CommunicationRequest.sender) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [HealthcareService](healthcareservice.html)) | Message sender | |

| [reasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Why is communication needed?
[v3 Code System ActReason](v3/ActReason/vs.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html) | [DiagnosticReport](diagnosticreport.html) | [DocumentReference](documentreference.html)) | Why is communication needed?
 | |

| [note](communicationrequest-definitions.html#CommunicationRequest.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about communication request
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - CommunicationRequest ([DomainResource](domainresource.html))[Business identifiers assigned to this communication request by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](communicationrequest-definitions.html#CommunicationRequest.identifier) : [Identifier](datatypes.html#Identifier) [0..*][A plan or proposal that is fulfilled in whole or in part by this requestbasedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Completed or terminated request(s) whose function is taken by this new requestreplaces](communicationrequest-definitions.html#CommunicationRequest.replaces) : [Reference](references.html#Reference) [0..*] « [CommunicationRequest](communicationrequest.html#CommunicationRequest) »[A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition, prescription or similar formgroupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][The status of the proposal or order (this element modifies the meaning of other elements)status](communicationrequest-definitions.html#CommunicationRequest.status) : [code](datatypes.html#code) [1..1] « [The status of the communication request. (Strength=Required)RequestStatus](valueset-request-status.html)! »[Captures the reason for the current state of the CommunicationRequeststatusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][The type of message to be sent such as alert, notification, reminder, instruction, etccategory](communicationrequest-definitions.html#CommunicationRequest.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for general categories of communications such as alerts, instruction, etc. (Strength=Example)CommunicationCategory](valueset-communication-category.html)?? »[Characterizes how quickly the proposed act must be initiated. Includes concepts such as stat, urgent, routinepriority](communicationrequest-definitions.html#CommunicationRequest.priority) : [code](datatypes.html#code) [0..1] « [Codes indicating the relative importance of a communication request. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[If true indicates that the CommunicationRequest is asking for the specified action to *not* occur (this element modifies the meaning of other elements)doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) : [boolean](datatypes.html#boolean) [0..1][A channel that was used for this communication (e.g. email, fax)medium](communicationrequest-definitions.html#CommunicationRequest.medium) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for communication mediums such as phone, fax, email, in person, etc. (Strength=Example)v3.ParticipationMode](v3/ParticipationMode/vs.html)?? »[The patient or group that is the focus of this communication requestsubject](communicationrequest-definitions.html#CommunicationRequest.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[Other resources that pertain to this communication request and to which this communication request should be associatedabout](communicationrequest-definitions.html#CommunicationRequest.about) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[The Encounter during which this CommunicationRequest was created or to which the creation of this record is tightly associatedencounter](communicationrequest-definitions.html#CommunicationRequest.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The time when this communication is to occuroccurrence[x]](communicationrequest-definitions.html#CommunicationRequest.occurrence_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) »[For draft requests, indicates the date of initial creation. For requests with other statuses, indicates the date of activationauthoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn) : [dateTime](datatypes.html#dateTime) [0..1][The device, individual, or organization who initiated the request and has responsibility for its activationrequester](communicationrequest-definitions.html#CommunicationRequest.requester) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device) »[The entity (e.g. person, organization, clinical information system, device, group, or care team) which is the intended target of the communicationrecipient](communicationrequest-definitions.html#CommunicationRequest.recipient) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)| [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)| [HealthcareService](healthcareservice.html#HealthcareService) »[The entity (e.g. person, organization, clinical information system, or device) which is to be the source of the communicationsender](communicationrequest-definitions.html#CommunicationRequest.sender) : [Reference](references.html#Reference) [0..1] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService) »[Describes why the request is being made in coded or textual formreasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes for describing reasons for the occurrence of a communication. (Strength=Example)v3.ActReason](v3/ActReason/vs.html)?? »[Indicates another resource whose existence justifies this requestreasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation)| [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference) »[Comments made about the request by the requester, sender, recipient, subject or other participantsnote](communicationrequest-definitions.html#CommunicationRequest.note) : [Annotation](datatypes.html#Annotation) [0..*]Payload[The communicated content (or for multi-part communications, one portion of the communication)content[x]](communicationrequest-definitions.html#CommunicationRequest.payload.content_x_) : [Type](formats.html#umlchoice) [1..1] « [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html#Any)) »
[Text, attachment(s), or resource(s) to be communicated to the recipientpayload](communicationrequest-definitions.html#CommunicationRequest.payload)[0..*]
 

**XML Template**

 

 
```
<[**CommunicationRequest**](communicationrequest-definitions.html#CommunicationRequest) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](communicationrequest-definitions.html#CommunicationRequest.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Unique identifier](terminologies.html#unbound) --></identifier>
 <[**basedOn**](communicationrequest-definitions.html#CommunicationRequest.basedOn)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Fulfills plan or proposal](terminologies.html#unbound) --></basedOn>
 <[**replaces**](communicationrequest-definitions.html#CommunicationRequest.replaces)><!-- **0..*** [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) [Request(s) replaced by this request](terminologies.html#unbound) --></replaces>
 <[**groupIdentifier**](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Composite request this is part of](terminologies.html#unbound) --></groupIdentifier>
 <[**status**](communicationrequest-definitions.html#CommunicationRequest.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [draft | active | on-hold | revoked | completed | entered-in-error | unknown](valueset-request-status.html) -->
 <[**statusReason**](communicationrequest-definitions.html#CommunicationRequest.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](terminologies.html#unbound) --></statusReason>
 <[**category**](communicationrequest-definitions.html#CommunicationRequest.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Message category](valueset-communication-category.html) --></category>
 <[**priority**](communicationrequest-definitions.html#CommunicationRequest.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**doNotPerform**](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [True if request is prohibiting action](terminologies.html#unbound) -->
 <[**medium**](communicationrequest-definitions.html#CommunicationRequest.medium)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A channel of communication](v3/ParticipationMode/vs.html) --></medium>
 <[**subject**](communicationrequest-definitions.html#CommunicationRequest.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Focus of message](terminologies.html#unbound) --></subject>
 <[**about**](communicationrequest-definitions.html#CommunicationRequest.about)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Resources that pertain to this communication request](terminologies.html#unbound) --></about>
 <[**encounter**](communicationrequest-definitions.html#CommunicationRequest.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**payload**](communicationrequest-definitions.html#CommunicationRequest.payload)> <!-- **0..*** Message payload -->
 <[**content[x]**](communicationrequest-definitions.html#CommunicationRequest.payload.content[x])><!-- **1..1** [string](datatypes.html#string)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html)) [Message part content](terminologies.html#unbound) --></content[x]>
 </payload>
 <[**occurrence[x]**](communicationrequest-definitions.html#CommunicationRequest.occurrence[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period) [When scheduled](terminologies.html#unbound) --></occurrence[x]>
 <[**authoredOn**](communicationrequest-definitions.html#CommunicationRequest.authoredOn) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When request transitioned to being actionable](terminologies.html#unbound) -->
 <[**requester**](communicationrequest-definitions.html#CommunicationRequest.requester)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) [Who/what is requesting service](terminologies.html#unbound) --></requester>
 <[**recipient**](communicationrequest-definitions.html#CommunicationRequest.recipient)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message recipient](terminologies.html#unbound) --></recipient>
 <[**sender**](communicationrequest-definitions.html#CommunicationRequest.sender)><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) [Message sender](terminologies.html#unbound) --></sender>
 <[**reasonCode**](communicationrequest-definitions.html#CommunicationRequest.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Why is communication needed?](v3/ActReason/vs.html) --></reasonCode>
 <[**reasonReference**](communicationrequest-definitions.html#CommunicationRequest.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) [Why is communication needed?](terminologies.html#unbound) --></reasonReference>
 <[**note**](communicationrequest-definitions.html#CommunicationRequest.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about communication request](terminologies.html#unbound) --></note>
</CommunicationRequest>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**CommunicationRequest**](communicationrequest-definitions.html#CommunicationRequest)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](communicationrequest-definitions.html#CommunicationRequest.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Unique identifier](terminologies.html#unbound)
 "[basedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Fulfills plan or proposal](terminologies.html#unbound)
 "[replaces](communicationrequest-definitions.html#CommunicationRequest.replaces)" : [{ [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) }], // [Request(s) replaced by this request](terminologies.html#unbound)
 "[groupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Composite request this is part of](terminologies.html#unbound)
 "[status](communicationrequest-definitions.html#CommunicationRequest.status)" : "<[code](datatypes.html#code)>", // **R!** [draft | active | on-hold | revoked | completed | entered-in-error | unknown](valueset-request-status.html)
 "[statusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](terminologies.html#unbound)
 "[category](communicationrequest-definitions.html#CommunicationRequest.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Message category](valueset-communication-category.html)
 "[priority](communicationrequest-definitions.html#CommunicationRequest.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform)" : <[boolean](datatypes.html#boolean)>, // [True if request is prohibiting action](terminologies.html#unbound)
 "[medium](communicationrequest-definitions.html#CommunicationRequest.medium)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [A channel of communication](v3/ParticipationMode/vs.html)
 "[subject](communicationrequest-definitions.html#CommunicationRequest.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [Focus of message](terminologies.html#unbound)
 "[about](communicationrequest-definitions.html#CommunicationRequest.about)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Resources that pertain to this communication request](terminologies.html#unbound)
 "[encounter](communicationrequest-definitions.html#CommunicationRequest.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[payload](communicationrequest-definitions.html#CommunicationRequest.payload)" : [{ // [Message payload](terminologies.html#unbound)
 // content[x]: Message part content. One of these 3:
 "[contentString](communicationrequest-definitions.html#CommunicationRequest.payload.contentString)" : "<[string](datatypes.html#string)>"
 "[contentAttachment](communicationrequest-definitions.html#CommunicationRequest.payload.contentAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[contentReference](communicationrequest-definitions.html#CommunicationRequest.payload.contentReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }
 }],
 // occurrence[x]: When scheduled. One of these 2:
 "[occurrenceDateTime](communicationrequest-definitions.html#CommunicationRequest.occurrenceDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[occurrencePeriod](communicationrequest-definitions.html#CommunicationRequest.occurrencePeriod)" : { [Period](datatypes.html#Period) },
 "[authoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn)" : "<[dateTime](datatypes.html#dateTime)>", // [When request transitioned to being actionable](terminologies.html#unbound)
 "[requester](communicationrequest-definitions.html#CommunicationRequest.requester)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) }, // [Who/what is requesting service](terminologies.html#unbound)
 "[recipient](communicationrequest-definitions.html#CommunicationRequest.recipient)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) }], // [Message recipient](terminologies.html#unbound)
 "[sender](communicationrequest-definitions.html#CommunicationRequest.sender)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[HealthcareService](healthcareservice.html#HealthcareService)) }, // [Message sender](terminologies.html#unbound)
 "[reasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Why is communication needed?](v3/ActReason/vs.html)
 "[reasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|
 [DocumentReference](documentreference.html#DocumentReference)) }], // [Why is communication needed?](terminologies.html#unbound)
 "[note](communicationrequest-definitions.html#CommunicationRequest.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about communication request](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**CommunicationRequest**](communicationrequest-definitions.html#CommunicationRequest);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[CommunicationRequest.identifier](communicationrequest-definitions.html#CommunicationRequest.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Unique identifier
 fhir:[CommunicationRequest.basedOn](communicationrequest-definitions.html#CommunicationRequest.basedOn) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Fulfills plan or proposal
 fhir:[CommunicationRequest.replaces](communicationrequest-definitions.html#CommunicationRequest.replaces) [ [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) ], ... ; # 0..* Request(s) replaced by this request
 fhir:[CommunicationRequest.groupIdentifier](communicationrequest-definitions.html#CommunicationRequest.groupIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Composite request this is part of
 fhir:[CommunicationRequest.status](communicationrequest-definitions.html#CommunicationRequest.status) [ [code](datatypes.html#code) ]; # 1..1 draft | active | on-hold | revoked | completed | entered-in-error | unknown
 fhir:[CommunicationRequest.statusReason](communicationrequest-definitions.html#CommunicationRequest.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[CommunicationRequest.category](communicationrequest-definitions.html#CommunicationRequest.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Message category
 fhir:[CommunicationRequest.priority](communicationrequest-definitions.html#CommunicationRequest.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[CommunicationRequest.doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform) [ [boolean](datatypes.html#boolean) ]; # 0..1 True if request is prohibiting action
 fhir:[CommunicationRequest.medium](communicationrequest-definitions.html#CommunicationRequest.medium) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A channel of communication
 fhir:[CommunicationRequest.subject](communicationrequest-definitions.html#CommunicationRequest.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 Focus of message
 fhir:[CommunicationRequest.about](communicationrequest-definitions.html#CommunicationRequest.about) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Resources that pertain to this communication request
 fhir:[CommunicationRequest.encounter](communicationrequest-definitions.html#CommunicationRequest.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[CommunicationRequest.payload](communicationrequest-definitions.html#CommunicationRequest.payload) [ # 0..* Message payload
 # [CommunicationRequest.payload.content[x]](communicationrequest-definitions.html#CommunicationRequest.payload.content[x]) : 1..1 Message part content. One of these 3
 fhir:[CommunicationRequest.payload.contentString](communicationrequest-definitions.html#CommunicationRequest.payload.contentString) [ [string](datatypes.html#string) ]
 fhir:[CommunicationRequest.payload.contentAttachment](communicationrequest-definitions.html#CommunicationRequest.payload.contentAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[CommunicationRequest.payload.contentReference](communicationrequest-definitions.html#CommunicationRequest.payload.contentReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]
 ], ...;
 # [CommunicationRequest.occurrence[x]](communicationrequest-definitions.html#CommunicationRequest.occurrence[x]) : 0..1 When scheduled. One of these 2
 fhir:[CommunicationRequest.occurrenceDateTime](communicationrequest-definitions.html#CommunicationRequest.occurrenceDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[CommunicationRequest.occurrencePeriod](communicationrequest-definitions.html#CommunicationRequest.occurrencePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[CommunicationRequest.authoredOn](communicationrequest-definitions.html#CommunicationRequest.authoredOn) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When request transitioned to being actionable
 fhir:[CommunicationRequest.requester](communicationrequest-definitions.html#CommunicationRequest.requester) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) ]; # 0..1 Who/what is requesting service
 fhir:[CommunicationRequest.recipient](communicationrequest-definitions.html#CommunicationRequest.recipient) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|
 [CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)) ], ... ; # 0..* Message recipient
 fhir:[CommunicationRequest.sender](communicationrequest-definitions.html#CommunicationRequest.sender) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [HealthcareService](healthcareservice.html#HealthcareService)) ]; # 0..1 Message sender
 fhir:[CommunicationRequest.reasonCode](communicationrequest-definitions.html#CommunicationRequest.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Why is communication needed?
 fhir:[CommunicationRequest.reasonReference](communicationrequest-definitions.html#CommunicationRequest.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)|[DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[DocumentReference](documentreference.html#DocumentReference)) ], ... ; # 0..* Why is communication needed?
 fhir:[CommunicationRequest.note](communicationrequest-definitions.html#CommunicationRequest.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about communication request
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [CommunicationRequest](communicationrequest.html#CommunicationRequest)
 | 
 | 
 |

 | 
 CommunicationRequest.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/request-status to http://hl7.org/fhir/ValueSet/request-status|4.0.1

 

 | 
 |

 | 
 CommunicationRequest.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.priority | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/request-priority to http://hl7.org/fhir/ValueSet/request-priority|4.0.1

 

 | 
 |

 | 
 CommunicationRequest.doNotPerform | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.about | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 CommunicationRequest.requester | 
 
 

 - Type changed from BackboneElement to Reference(Practitioner | PractitionerRole | Organization | Patient | RelatedPerson | Device)

 

 | 
 |

 | 
 CommunicationRequest.recipient | 
 
 

 - Type Reference: Added Target Types PractitionerRole, HealthcareService

 

 | 
 |

 | 
 CommunicationRequest.sender | 
 
 

 - Type Reference: Added Target Types PractitionerRole, HealthcareService

 

 | 
 |

 | 
 CommunicationRequest.reasonReference | 
 
 

 - Type Reference: Added Target Types DiagnosticReport, DocumentReference

 

 | 
 |

 | 
 CommunicationRequest.topic | 
 
 

 - deleted

 

 | 
 |

 | 
 CommunicationRequest.context | 
 
 

 - deleted

 

 | 
 |

 | 
 CommunicationRequest.requester.agent | 
 
 

 - deleted

 

 | 
 |

 | 
 CommunicationRequest.requester.onBehalfOf | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](communicationrequest.diff.xml) or [JSON](communicationrequest.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](communicationrequest-version-maps.html) (status = 2 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](communicationrequest-profiles.html) and the alternate definitions:
Master Definition [XML](communicationrequest.profile.xml.html) + [JSON](communicationrequest.profile.json.html),
[XML](xml.html) [Schema](communicationrequest.xsd)/[Schematron](communicationrequest.sch) + [JSON](json.html) 
[Schema](communicationrequest.schema.json.html), [ShEx](communicationrequest.shex.html) (for [Turtle](rdf.html)) + [see the extensions](communicationrequest-profiles.html) & the [dependency analysis](communicationrequest-dependencies.html)

### 8.21.3.1 
Terminology Bindings
 [
](communicationrequest.html#tx)

 | Path | Definition | Type | Reference | |

 | CommunicationRequest.status | The status of the communication request. | [Required](terminologies.html#required) | [RequestStatus](valueset-request-status.html) | |

 | CommunicationRequest.statusReason | Codes identifying the reason for the current state of a request. | Unknown | No details provided yet | |

 | CommunicationRequest.category | Codes for general categories of communications such as alerts, instruction, etc. | [Example](terminologies.html#example) | [CommunicationCategory](valueset-communication-category.html) | |

 | CommunicationRequest.priority | Codes indicating the relative importance of a communication request. | [Required](terminologies.html#required) | [RequestPriority](valueset-request-priority.html) | |

 | CommunicationRequest.medium | Codes for communication mediums such as phone, fax, email, in person, etc. | [Example](terminologies.html#example) | [v3.ParticipationMode](v3/ParticipationMode/vs.html) | |

 | CommunicationRequest.reasonCode | Codes for describing reasons for the occurrence of a communication. | [Example](terminologies.html#example) | [v3.ActReason](v3/ActReason/vs.html) | |

 

 
 

 **Notes to reviewers:**
 

 

 At this time, the code bindings are placeholders to be fleshed out upon further review by the community.*
 

 
### 8.21.3.2 CommunicationRequest.sender and CommunicationRequest.recepient [
](communicationrequest.html#8.21.3.2)

 CommunicationRequest.sender allows Device | Organization | Patient | Practitioner | PractitionerRole | RelatedPerson | HealthcareService and CommunicationRequest.recipient allows Device | Organization | Patient | Practitioner | PractitionerRole | RelatedPerson | Group | CareTeam | HealthcareService - but it is not unusual to have a communication target - even a defined one - where it is unknown what kind of role the person is playing.
 

 

 If the communication request is to or from an individual, whose role is not known (practitioner, patient or related person), -
 for example, only email address is captured in the system; then RelatedPerson should be used by default.
 

## 8.21.4 Search Parameters [
](communicationrequest.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| authored | [date](search.html#date) | When request transitioned to being actionable | CommunicationRequest.authoredOn | | |

| based-on | [reference](search.html#reference) | Fulfills plan or proposal | CommunicationRequest.basedOn
(Any) | | |

| category | [token](search.html#token) | Message category | CommunicationRequest.category | | |

| encounter | [reference](search.html#reference) | Encounter created as part of | CommunicationRequest.encounter
([Encounter](encounter.html)) | | |

| group-identifier | [token](search.html#token) | Composite request this is part of | CommunicationRequest.groupIdentifier | | |

| identifier | [token](search.html#token) | Unique identifier | CommunicationRequest.identifier | | |

| medium | [token](search.html#token) | A channel of communication | CommunicationRequest.medium | | |

| occurrence | [date](search.html#date) | When scheduled | (CommunicationRequest.occurrence as dateTime) | | |

| patient | [reference](search.html#reference) | Focus of message | CommunicationRequest.subject.where(resolve() is Patient)
([Patient](patient.html)) | | |

| priority | [token](search.html#token) | routine | urgent | asap | stat | CommunicationRequest.priority | | |

| recipient | [reference](search.html#reference) | Message recipient | CommunicationRequest.recipient
([Practitioner](practitioner.html), [Group](group.html), [Organization](organization.html), [CareTeam](careteam.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| replaces | [reference](search.html#reference) | Request(s) replaced by this request | CommunicationRequest.replaces
([CommunicationRequest](communicationrequest.html)) | | |

| requester | [reference](search.html#reference) | Who/what is requesting service | CommunicationRequest.requester
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| sender | [reference](search.html#reference) | Message sender | CommunicationRequest.sender
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| status | [token](search.html#token) | draft | active | on-hold | revoked | completed | entered-in-error | unknown | CommunicationRequest.status | | |

| subject | [reference](search.html#reference) | Focus of message | CommunicationRequest.subject
([Group](group.html), [Patient](patient.html)) | | |