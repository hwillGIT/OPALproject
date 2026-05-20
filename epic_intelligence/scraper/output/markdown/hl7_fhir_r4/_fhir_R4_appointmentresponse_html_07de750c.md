# AppointmentResponse - FHIR v4.0.1This records identifiers associated with this appointment response concern that are defined by business processes and/ or used to refer to it when a direct URL reference to the resource itself is not appropriateAppointment that this response is replying toDate/Time that the appointment is to take place, or requested new start timeThis may be either the same as the appointment request to confirm the details of the appointment, or alternately a new time to request a re-negotiation of the end timeRole of participant in the appointmentRole of participant in encounter. (Strength=Extensible)A Person, Location, HealthcareService, or Device that is participating in the appointmentParticipation status of the participant. When the status is declined or tentative if the start/end times are different to the appointment, then these times should be interpreted as a requested time change. When the status is accepted, the times can either be the time of the appointment (as a confirmation of the time) or can be empty (this element modifies the meaning of other elements)The Participation status of an appointment. (Strength=Required)Additional comments about the appointmentThis records identifiers associated with this appointment response concern that are defined by business processes and/ or used to refer to it when a direct URL reference to the resource itself is not appropriateAppointment that this response is replying toDate/Time that the appointment is to take place, or requested new start timeThis may be either the same as the appointment request to confirm the details of the appointment, or alternately a new time to request a re-negotiation of the end timeRole of participant in the appointmentRole of participant in encounter. (Strength=Extensible)A Person, Location, HealthcareService, or Device that is participating in the appointmentParticipation status of the participant. When the status is declined or tentative if the start/end times are different to the appointment, then these times should be interpreted as a requested time change. When the status is accepted, the times can either be the time of the appointment (as a confirmation of the time) or can be empty (this element modifies the meaning of other elements)The Participation status of an appointment. (Strength=Required)Additional comments about the appointment

> Source: https://hl7.org/fhir/R4/appointmentresponse.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/appointmentresponse.html) [R4B](http://hl7.org/fhir/R4B/appointmentresponse.html) **R4** [R3](http://hl7.org/fhir/STU3/appointmentresponse.html) [R2](http://hl7.org/fhir/DSTU2/appointmentresponse.html)
 

# 12.11 Resource AppointmentResponse - Content [
](appointmentresponse.html#12.11)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.

 
 
## 12.11.1 Scope and Usage [
](appointmentresponse.html#scope)

 
 Appointment resources are used to provide information about 
 a planned meeting that may be in the future or past. They may be for a single meeting or
 for a series of repeating visits. Examples include a scheduled surgery, a follow-up for a
 clinical visit, a scheduled conference call between clinicians to discuss a case, the reservation
 of a piece of diagnostic equipment for a particular use, etc. The visit scheduled by an appointment
 may be in person or remote (by phone, video conference, etc.) All that matters is that the time and
 usage of one or more individuals, locations and/or pieces of equipment is being fully or partially
 reserved for a designated period of time.
 

 

 This definition takes the concepts of appointments in a clinical setting and also extends
 them to be relevant in the community healthcare space, and also ease exposure to other
 appointment / calendar standards widely used outside of Healthcare.
 

 
 
### 12.11.1.1 The basic workflow to create an appointment [
](appointmentresponse.html#basic-workflow)

 

 - 
 **Making the Appointment Request**
 
 When an appointment is required, a requester creates new Appointment resource with the Appointment.status="proposed".**
 All included participants (optional or mandatory) should have the status="needs-action" to allow filtering and displaying
 appointments to user-participants for accepting or rejecting new and updated requests. Based on internal system business rules,
 certain statuses may be automatically updated, for example: "reject because the requested participant is on vacation" or 
 "this type of user is not allowed to request those specific appointments".
 

 

 - 
 Replying to the request**
 

 The reply process is simply performed by the person/system handing the requests updating
 the participant statuses as needed. If there are multiple systems involved, then these
 will create AppointmentResponse entries with the desired statuses.
 

 

 Once all participants have their participation status created/updated
 (and the main system marking the appointment participant records with the AppointmentResponse
 statuses) then the overall status of the Appointment is updated.
 

 

 

 

This resource is referenced by [ImagingStudy](imagingstudy.html#ImagingStudy)

## 12.11.2 
Resource Content
 [
](appointmentresponse.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [AppointmentResponse](appointmentresponse-definitions.html#AppointmentResponse) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection**+ Rule: Either the participantType or actor must be specified
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](appointmentresponse-definitions.html#AppointmentResponse.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this item
 | |

| [appointment](appointmentresponse-definitions.html#AppointmentResponse.appointment) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Appointment](appointment.html)) | Appointment this response relates to | |

| [start](appointmentresponse-definitions.html#AppointmentResponse.start) | | 0..1 | [instant](datatypes.html#instant) | Time from appointment, or requested new start time | |

| [end](appointmentresponse-definitions.html#AppointmentResponse.end) | | 0..1 | [instant](datatypes.html#instant) | Time from appointment, or requested new end time | |

| [participantType](appointmentresponse-definitions.html#AppointmentResponse.participantType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in the appointment
[Participant type](valueset-encounter-participant-type.html) ([Extensible](terminologies.html#extensible))
 | |

| [actor](appointmentresponse-definitions.html#AppointmentResponse.actor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Device](device.html) | [HealthcareService](healthcareservice.html) | [Location](location.html)) | Person, Location, HealthcareService, or Device | |

| [participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | accepted | declined | tentative | needs-action
[ParticipationStatus](valueset-participationstatus.html) ([Required](terminologies.html#required)) | |

| [comment](appointmentresponse-definitions.html#AppointmentResponse.comment) | | 0..1 | [string](datatypes.html#string) | Additional comments | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - AppointmentResponse ([DomainResource](domainresource.html))[This records identifiers associated with this appointment response concern that are defined by business processes and/ or used to refer to it when a direct URL reference to the resource itself is not appropriateidentifier](appointmentresponse-definitions.html#AppointmentResponse.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Appointment that this response is replying toappointment](appointmentresponse-definitions.html#AppointmentResponse.appointment) : [Reference](references.html#Reference) [1..1] « [Appointment](appointment.html#Appointment) »[Date/Time that the appointment is to take place, or requested new start timestart](appointmentresponse-definitions.html#AppointmentResponse.start) : [instant](datatypes.html#instant) [0..1][This may be either the same as the appointment request to confirm the details of the appointment, or alternately a new time to request a re-negotiation of the end timeend](appointmentresponse-definitions.html#AppointmentResponse.end) : [instant](datatypes.html#instant) [0..1][Role of participant in the appointmentparticipantType](appointmentresponse-definitions.html#AppointmentResponse.participantType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Role of participant in encounter. (Strength=Extensible)ParticipantType](valueset-encounter-participant-type.html)+ »[A Person, Location, HealthcareService, or Device that is participating in the appointmentactor](appointmentresponse-definitions.html#AppointmentResponse.actor) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location) »[Participation status of the participant. When the status is declined or tentative if the start/end times are different to the appointment, then these times should be interpreted as a requested time change. When the status is accepted, the times can either be the time of the appointment (as a confirmation of the time) or can be empty (this element modifies the meaning of other elements)participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) : [code](datatypes.html#code) [1..1] « [The Participation status of an appointment. (Strength=Required)ParticipationStatus](valueset-participationstatus.html)! »[Additional comments about the appointmentcomment](appointmentresponse-definitions.html#AppointmentResponse.comment) : [string](datatypes.html#string) [0..1]
 

 

 

**XML Template**

 

 
```
<[**AppointmentResponse**](appointmentresponse-definitions.html#AppointmentResponse) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](appointmentresponse-definitions.html#AppointmentResponse.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External Ids for this item](terminologies.html#unbound) --></identifier>
 <[**appointment**](appointmentresponse-definitions.html#AppointmentResponse.appointment)><!-- **1..1** [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) [Appointment this response relates to](terminologies.html#unbound) --></appointment>
 <[**start**](appointmentresponse-definitions.html#AppointmentResponse.start) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [Time from appointment, or requested new start time](terminologies.html#unbound) -->
 <[**end**](appointmentresponse-definitions.html#AppointmentResponse.end) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [Time from appointment, or requested new end time](terminologies.html#unbound) -->
 <[**participantType**](appointmentresponse-definitions.html#AppointmentResponse.participantType)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Role of participant in the appointment](valueset-encounter-participant-type.html) --></participantType>
 <[**actor**](appointmentresponse-definitions.html#AppointmentResponse.actor)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) [Person, Location, HealthcareService, or Device](terminologies.html#unbound) --></actor>
 <[**participantStatus**](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) value="[[code](datatypes.html#code)]"/><!-- **1..1** [accepted | declined | tentative | needs-action](valueset-participationstatus.html) -->
 <[**comment**](appointmentresponse-definitions.html#AppointmentResponse.comment) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional comments](terminologies.html#unbound) -->
</AppointmentResponse>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**AppointmentResponse**](appointmentresponse-definitions.html#AppointmentResponse)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](appointmentresponse-definitions.html#AppointmentResponse.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this item](terminologies.html#unbound)
 "[appointment](appointmentresponse-definitions.html#AppointmentResponse.appointment)" : { [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) }, // **R!** [Appointment this response relates to](terminologies.html#unbound)
 "[start](appointmentresponse-definitions.html#AppointmentResponse.start)" : "<[instant](datatypes.html#instant)>", // [Time from appointment, or requested new start time](terminologies.html#unbound)
 "[end](appointmentresponse-definitions.html#AppointmentResponse.end)" : "<[instant](datatypes.html#instant)>", // [Time from appointment, or requested new end time](terminologies.html#unbound)
 "[participantType](appointmentresponse-definitions.html#AppointmentResponse.participantType)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Role of participant in the appointment](valueset-encounter-participant-type.html)
 "[actor](appointmentresponse-definitions.html#AppointmentResponse.actor)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) }, // [Person, Location, HealthcareService, or Device](terminologies.html#unbound)
 "[participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus)" : "<[code](datatypes.html#code)>", // **R!** [accepted | declined | tentative | needs-action](valueset-participationstatus.html)
 "[comment](appointmentresponse-definitions.html#AppointmentResponse.comment)" : "<[string](datatypes.html#string)>" // [Additional comments](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**AppointmentResponse**](appointmentresponse-definitions.html#AppointmentResponse);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[AppointmentResponse.identifier](appointmentresponse-definitions.html#AppointmentResponse.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this item
 fhir:[AppointmentResponse.appointment](appointmentresponse-definitions.html#AppointmentResponse.appointment) [ [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) ]; # 1..1 Appointment this response relates to
 fhir:[AppointmentResponse.start](appointmentresponse-definitions.html#AppointmentResponse.start) [ [instant](datatypes.html#instant) ]; # 0..1 Time from appointment, or requested new start time
 fhir:[AppointmentResponse.end](appointmentresponse-definitions.html#AppointmentResponse.end) [ [instant](datatypes.html#instant) ]; # 0..1 Time from appointment, or requested new end time
 fhir:[AppointmentResponse.participantType](appointmentresponse-definitions.html#AppointmentResponse.participantType) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Role of participant in the appointment
 fhir:[AppointmentResponse.actor](appointmentresponse-definitions.html#AppointmentResponse.actor) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|
 [Location](location.html#Location)) ]; # 0..1 Person, Location, HealthcareService, or Device
 fhir:[AppointmentResponse.participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) [ [code](datatypes.html#code) ]; # 1..1 accepted | declined | tentative | needs-action
 fhir:[AppointmentResponse.comment](appointmentresponse-definitions.html#AppointmentResponse.comment) [ [string](datatypes.html#string) ]; # 0..1 Additional comments
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [AppointmentResponse](appointmentresponse.html#AppointmentResponse)
 | 
 | 
 |

 | 
 AppointmentResponse.actor | 
 
 

 Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 AppointmentResponse.participantStatus | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/participationstatus to http://hl7.org/fhir/ValueSet/participationstatus|4.0.1

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](appointmentresponse.diff.xml) or [JSON](appointmentresponse.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](appointmentresponse-version-maps.html) (status = 2 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [AppointmentResponse](appointmentresponse-definitions.html#AppointmentResponse) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection**+ Rule: Either the participantType or actor must be specified
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](appointmentresponse-definitions.html#AppointmentResponse.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this item
 | |

| [appointment](appointmentresponse-definitions.html#AppointmentResponse.appointment) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Appointment](appointment.html)) | Appointment this response relates to | |

| [start](appointmentresponse-definitions.html#AppointmentResponse.start) | | 0..1 | [instant](datatypes.html#instant) | Time from appointment, or requested new start time | |

| [end](appointmentresponse-definitions.html#AppointmentResponse.end) | | 0..1 | [instant](datatypes.html#instant) | Time from appointment, or requested new end time | |

| [participantType](appointmentresponse-definitions.html#AppointmentResponse.participantType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in the appointment
[Participant type](valueset-encounter-participant-type.html) ([Extensible](terminologies.html#extensible))
 | |

| [actor](appointmentresponse-definitions.html#AppointmentResponse.actor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Device](device.html) | [HealthcareService](healthcareservice.html) | [Location](location.html)) | Person, Location, HealthcareService, or Device | |

| [participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | accepted | declined | tentative | needs-action
[ParticipationStatus](valueset-participationstatus.html) ([Required](terminologies.html#required)) | |

| [comment](appointmentresponse-definitions.html#AppointmentResponse.comment) | | 0..1 | [string](datatypes.html#string) | Additional comments | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - AppointmentResponse ([DomainResource](domainresource.html))[This records identifiers associated with this appointment response concern that are defined by business processes and/ or used to refer to it when a direct URL reference to the resource itself is not appropriateidentifier](appointmentresponse-definitions.html#AppointmentResponse.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Appointment that this response is replying toappointment](appointmentresponse-definitions.html#AppointmentResponse.appointment) : [Reference](references.html#Reference) [1..1] « [Appointment](appointment.html#Appointment) »[Date/Time that the appointment is to take place, or requested new start timestart](appointmentresponse-definitions.html#AppointmentResponse.start) : [instant](datatypes.html#instant) [0..1][This may be either the same as the appointment request to confirm the details of the appointment, or alternately a new time to request a re-negotiation of the end timeend](appointmentresponse-definitions.html#AppointmentResponse.end) : [instant](datatypes.html#instant) [0..1][Role of participant in the appointmentparticipantType](appointmentresponse-definitions.html#AppointmentResponse.participantType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Role of participant in encounter. (Strength=Extensible)ParticipantType](valueset-encounter-participant-type.html)+ »[A Person, Location, HealthcareService, or Device that is participating in the appointmentactor](appointmentresponse-definitions.html#AppointmentResponse.actor) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location) »[Participation status of the participant. When the status is declined or tentative if the start/end times are different to the appointment, then these times should be interpreted as a requested time change. When the status is accepted, the times can either be the time of the appointment (as a confirmation of the time) or can be empty (this element modifies the meaning of other elements)participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) : [code](datatypes.html#code) [1..1] « [The Participation status of an appointment. (Strength=Required)ParticipationStatus](valueset-participationstatus.html)! »[Additional comments about the appointmentcomment](appointmentresponse-definitions.html#AppointmentResponse.comment) : [string](datatypes.html#string) [0..1]
 

**XML Template**

 

 
```
<[**AppointmentResponse**](appointmentresponse-definitions.html#AppointmentResponse) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](appointmentresponse-definitions.html#AppointmentResponse.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External Ids for this item](terminologies.html#unbound) --></identifier>
 <[**appointment**](appointmentresponse-definitions.html#AppointmentResponse.appointment)><!-- **1..1** [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) [Appointment this response relates to](terminologies.html#unbound) --></appointment>
 <[**start**](appointmentresponse-definitions.html#AppointmentResponse.start) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [Time from appointment, or requested new start time](terminologies.html#unbound) -->
 <[**end**](appointmentresponse-definitions.html#AppointmentResponse.end) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [Time from appointment, or requested new end time](terminologies.html#unbound) -->
 <[**participantType**](appointmentresponse-definitions.html#AppointmentResponse.participantType)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Role of participant in the appointment](valueset-encounter-participant-type.html) --></participantType>
 <[**actor**](appointmentresponse-definitions.html#AppointmentResponse.actor)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) [Person, Location, HealthcareService, or Device](terminologies.html#unbound) --></actor>
 <[**participantStatus**](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) value="[[code](datatypes.html#code)]"/><!-- **1..1** [accepted | declined | tentative | needs-action](valueset-participationstatus.html) -->
 <[**comment**](appointmentresponse-definitions.html#AppointmentResponse.comment) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional comments](terminologies.html#unbound) -->
</AppointmentResponse>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**AppointmentResponse**](appointmentresponse-definitions.html#AppointmentResponse)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](appointmentresponse-definitions.html#AppointmentResponse.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this item](terminologies.html#unbound)
 "[appointment](appointmentresponse-definitions.html#AppointmentResponse.appointment)" : { [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) }, // **R!** [Appointment this response relates to](terminologies.html#unbound)
 "[start](appointmentresponse-definitions.html#AppointmentResponse.start)" : "<[instant](datatypes.html#instant)>", // [Time from appointment, or requested new start time](terminologies.html#unbound)
 "[end](appointmentresponse-definitions.html#AppointmentResponse.end)" : "<[instant](datatypes.html#instant)>", // [Time from appointment, or requested new end time](terminologies.html#unbound)
 "[participantType](appointmentresponse-definitions.html#AppointmentResponse.participantType)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Role of participant in the appointment](valueset-encounter-participant-type.html)
 "[actor](appointmentresponse-definitions.html#AppointmentResponse.actor)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) }, // [Person, Location, HealthcareService, or Device](terminologies.html#unbound)
 "[participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus)" : "<[code](datatypes.html#code)>", // **R!** [accepted | declined | tentative | needs-action](valueset-participationstatus.html)
 "[comment](appointmentresponse-definitions.html#AppointmentResponse.comment)" : "<[string](datatypes.html#string)>" // [Additional comments](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**AppointmentResponse**](appointmentresponse-definitions.html#AppointmentResponse);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[AppointmentResponse.identifier](appointmentresponse-definitions.html#AppointmentResponse.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this item
 fhir:[AppointmentResponse.appointment](appointmentresponse-definitions.html#AppointmentResponse.appointment) [ [Reference](references.html#Reference)([Appointment](appointment.html#Appointment)) ]; # 1..1 Appointment this response relates to
 fhir:[AppointmentResponse.start](appointmentresponse-definitions.html#AppointmentResponse.start) [ [instant](datatypes.html#instant) ]; # 0..1 Time from appointment, or requested new start time
 fhir:[AppointmentResponse.end](appointmentresponse-definitions.html#AppointmentResponse.end) [ [instant](datatypes.html#instant) ]; # 0..1 Time from appointment, or requested new end time
 fhir:[AppointmentResponse.participantType](appointmentresponse-definitions.html#AppointmentResponse.participantType) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Role of participant in the appointment
 fhir:[AppointmentResponse.actor](appointmentresponse-definitions.html#AppointmentResponse.actor) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|
 [Location](location.html#Location)) ]; # 0..1 Person, Location, HealthcareService, or Device
 fhir:[AppointmentResponse.participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus) [ [code](datatypes.html#code) ]; # 1..1 accepted | declined | tentative | needs-action
 fhir:[AppointmentResponse.comment](appointmentresponse-definitions.html#AppointmentResponse.comment) [ [string](datatypes.html#string) ]; # 0..1 Additional comments
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [AppointmentResponse](appointmentresponse.html#AppointmentResponse)
 | 
 | 
 |

 | 
 AppointmentResponse.actor | 
 
 

 Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 AppointmentResponse.participantStatus | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/participationstatus to http://hl7.org/fhir/ValueSet/participationstatus|4.0.1

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](appointmentresponse.diff.xml) or [JSON](appointmentresponse.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](appointmentresponse-version-maps.html) (status = 2 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](appointmentresponse-profiles.html) and the alternate definitions:
Master Definition [XML](appointmentresponse.profile.xml.html) + [JSON](appointmentresponse.profile.json.html),
[XML](xml.html) [Schema](appointmentresponse.xsd)/[Schematron](appointmentresponse.sch) + [JSON](json.html) 
[Schema](appointmentresponse.schema.json.html), [ShEx](appointmentresponse.shex.html) (for [Turtle](rdf.html)) + [see the extensions](appointmentresponse-profiles.html) & the [dependency analysis](appointmentresponse-dependencies.html)

### 12.11.2.1 
Terminology Bindings
 [
](appointmentresponse.html#tx)

 | Path | Definition | Type | Reference | |

 | AppointmentResponse.participantType | Role of participant in encounter. | [Extensible](terminologies.html#extensible) | [ParticipantType](valueset-encounter-participant-type.html) | |

 | AppointmentResponse.participantStatus | The Participation status of an appointment. | [Required](terminologies.html#required) | [ParticipationStatus](valueset-participationstatus.html) | |

 

 

### 12.11.2.2 Constraints [
](appointmentresponse.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **apr-1** | [Rule](conformance-rules.html#rule) | (base) | Either the participantType or actor must be specified | participantType.exists() or actor.exists() | |

 
## 12.11.3 Notes: [](appointmentresponse.html#notes)

 
### 12.11.3.1 Time zones and recurring appointments [](appointmentresponse.html#12.11.3.1)

 Recurring appointments need to have the time zone defined in which the values were entered.
 Knowing that the start time was at 9:00:00Z+10 does not mean that the same time in 2 weeks is actually the same. 
 

 

 For example, if this was a time in Brisbane Australia, this time would be the same (in respect to its offset from UTC),
 however if this was for Melbourne Australia, during the daylight savings period Melbourne time zone becomes +11.
 So, without the additional information as to which time zone it was created in, scheduling a 9am appointment every
 Wednesday would not be possible.
 

## 12.11.4 Search Parameters [
](appointmentresponse.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| actor | [reference](search.html#reference) | The Person, Location/HealthcareService or Device that this appointment response replies for | AppointmentResponse.actor
([Practitioner](practitioner.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html), [Location](location.html)) | | |

| appointment | [reference](search.html#reference) | The appointment that the response is attached to | AppointmentResponse.appointment
([Appointment](appointment.html)) | | |

| identifier | [token](search.html#token) | An Identifier in this appointment response | AppointmentResponse.identifier | | |

| location | [reference](search.html#reference) | This Response is for this Location | AppointmentResponse.actor.where(resolve() is Location)
([Location](location.html)) | | |

| part-status | [token](search.html#token) | The participants acceptance status for this appointment | AppointmentResponse.participantStatus | | |

| patient | [reference](search.html#reference) | This Response is for this Patient | AppointmentResponse.actor.where(resolve() is Patient)
([Patient](patient.html)) | | |

| practitioner | [reference](search.html#reference) | This Response is for this Practitioner | AppointmentResponse.actor.where(resolve() is Practitioner)
([Practitioner](practitioner.html)) | | |