# Appointment - FHIR v4.0.1This records identifiers associated with this appointment concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)The overall status of the Appointment. Each of the participants has their own participation status which indicates their involvement in the process, however this status indicates the shared status (this element modifies the meaning of other elements)The free/busy status of an appointment. (Strength=Required)The coded reason for the appointment being cancelled. This is often used in reporting/billing/futher processing to determine if further actions are required, or specific fees apply (Strength=Example)A broad categorization of the service that is to be performed during this appointment (Strength=Example)The specific service that is to be performed during this appointment (Strength=Example)The specialty of a practitioner that would be required to perform the service requested in this appointment (Strength=Preferred)The style of appointment or patient that has been booked in the slot (not service type) (Strength=Preferred)The coded reason that this appointment is being scheduled. This is more clinical than administrativeThe Reason for the appointment to take place. (Strength=Preferred)Reason the appointment has been scheduled to take place, as specified using information from another resource. When the patient arrives and the encounter begins it may be used as the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a ProcedureThe priority of the appointment. Can be used to make informed decisions if needing to re-prioritize appointments. (The iCal Standard specifies 0 as undefined, 1 as highest, 9 as lowest priority)The brief description of the appointment as would be shown on a subject line in a meeting request, or appointment list. Detailed or expanded information should be put in the comment fieldAdditional information to support the appointment provided when making the appointmentDate/Time that the appointment is to take placeDate/Time that the appointment is to concludeNumber of minutes that the appointment is to take. This can be less than the duration between the start and end times.  For example, where the actual time of appointment is only an estimate or if a 30 minute appointment is being requested, but any time would work.  Also, if there is, for example, a planned 15 minute break in the middle of a long appointment, the duration may be 15 minutes less than the difference between the start and endThe slots from the participants' schedules that will be filled by the appointmentThe date that this appointment was initially created. This could be different to the meta.lastModified value on the initial entry, as this could have been before the resource was created on the FHIR server, and should remain unchanged over the lifespan of the appointmentAdditional comments about the appointmentWhile Appointment.comment contains information for internal use, Appointment.patientInstructions is used to capture patient facing information about the Appointment (e.g. please bring your referral or fast from 8pm night before)The service request this appointment is allocated to assess (e.g. incoming referral or procedure request)A set of date ranges (potentially including times) that the appointment is preferred to be scheduled within.

The duration (usually in minutes) could also be provided to indicate the length of the appointment to fill and populate the start/end times for the actual allocated time. However, in other situations the duration may be calculated by the scheduling systemRole of participant in the appointmentRole of participant in encounter. (Strength=Extensible)A Person, Location/HealthcareService or Device that is participating in the appointmentWhether this participant is required to be present at the meeting. This covers a use-case where two doctors need to meet to discuss the results for a specific patient, and the patient is not required to be presentIs the Participant required to attend the appointment. (Strength=Required)Participation status of the actorThe Participation status of an appointment. (Strength=Required)Participation period of the actorList of participants involved in the appointmentThis records identifiers associated with this appointment concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)The overall status of the Appointment. Each of the participants has their own participation status which indicates their involvement in the process, however this status indicates the shared status (this element modifies the meaning of other elements)The free/busy status of an appointment. (Strength=Required)The coded reason for the appointment being cancelled. This is often used in reporting/billing/futher processing to determine if further actions are required, or specific fees apply (Strength=Example)A broad categorization of the service that is to be performed during this appointment (Strength=Example)The specific service that is to be performed during this appointment (Strength=Example)The specialty of a practitioner that would be required to perform the service requested in this appointment (Strength=Preferred)The style of appointment or patient that has been booked in the slot (not service type) (Strength=Preferred)The coded reason that this appointment is being scheduled. This is more clinical than administrativeThe Reason for the appointment to take place. (Strength=Preferred)Reason the appointment has been scheduled to take place, as specified using information from another resource. When the patient arrives and the encounter begins it may be used as the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a ProcedureThe priority of the appointment. Can be used to make informed decisions if needing to re-prioritize appointments. (The iCal Standard specifies 0 as undefined, 1 as highest, 9 as lowest priority)The brief description of the appointment as would be shown on a subject line in a meeting request, or appointment list. Detailed or expanded information should be put in the comment fieldAdditional information to support the appointment provided when making the appointmentDate/Time that the appointment is to take placeDate/Time that the appointment is to concludeNumber of minutes that the appointment is to take. This can be less than the duration between the start and end times.  For example, where the actual time of appointment is only an estimate or if a 30 minute appointment is being requested, but any time would work.  Also, if there is, for example, a planned 15 minute break in the middle of a long appointment, the duration may be 15 minutes less than the difference between the start and endThe slots from the participants' schedules that will be filled by the appointmentThe date that this appointment was initially created. This could be different to the meta.lastModified value on the initial entry, as this could have been before the resource was created on the FHIR server, and should remain unchanged over the lifespan of the appointmentAdditional comments about the appointmentWhile Appointment.comment contains information for internal use, Appointment.patientInstructions is used to capture patient facing information about the Appointment (e.g. please bring your referral or fast from 8pm night before)The service request this appointment is allocated to assess (e.g. incoming referral or procedure request)A set of date ranges (potentially including times) that the appointment is preferred to be scheduled within.

The duration (usually in minutes) could also be provided to indicate the length of the appointment to fill and populate the start/end times for the actual allocated time. However, in other situations the duration may be calculated by the scheduling systemRole of participant in the appointmentRole of participant in encounter. (Strength=Extensible)A Person, Location/HealthcareService or Device that is participating in the appointmentWhether this participant is required to be present at the meeting. This covers a use-case where two doctors need to meet to discuss the results for a specific patient, and the patient is not required to be presentIs the Participant required to attend the appointment. (Strength=Required)Participation status of the actorThe Participation status of an appointment. (Strength=Required)Participation period of the actorList of participants involved in the appointment

> Source: https://hl7.org/fhir/R4/appointment.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/appointment.html) [R4B](http://hl7.org/fhir/R4B/appointment.html) **R4** [R3](http://hl7.org/fhir/STU3/appointment.html) [R2](http://hl7.org/fhir/DSTU2/appointment.html)
 

# 12.10 Resource Appointment - Content [
](appointment.html#12.10)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).

 
## 12.10.1 Scope and Usage [
](appointment.html#scope)

 
 Appointment resources are used to provide information about
 a planned meeting that may be in the future or past. The resource only describes a single meeting,
 a series of repeating visits would require multiple appointment resources to be created for each instance.
 Examples include a scheduled surgery, a follow-up for a
 clinical visit, a scheduled conference call between clinicians to discuss a case, the reservation
 of a piece of diagnostic equipment for a particular use, etc.
 The visit scheduled by an appointment
 may be in person or remote (by phone, video conference, etc.) All that matters is that the time and
 usage of one or more individuals, locations and/or pieces of equipment is being fully or partially
 reserved for a designated period of time.
 

 

 This definition takes the concepts of appointments in a clinical setting and also extends
 them to be relevant in the community healthcare space, and to ease exposure to other
 appointment / calendar standards widely used outside of healthcare.
 

 
### 12.10.1.1 The basic workflow to create an appointment [
](appointment.html#basic-workflow)

 

 - 
 **Discovery/Addressing**
 
 Before an appointment can be made, the address/endpoint details of the resource that we want 
 to schedule an appointment with must be determined. This is often based on the healthcare service type
 and any formatting information which indicates how to make the request.
 This is typically handled via the Schedule resource.
 

 

 - 
 **Checking Availability on the Schedule (optional)**
 

 This optional step permits the checking of any existing available times 
 ([Slot](slot.html) resources associated with a selected [Schedule](schedule.html)) that can be booked against.
 Just because a time is indicated as available doesn't guarantee that an appointment can be made.
 The booking system that is going to process the request may make other qualifying decisions to
 determine if the appointment can be made, such as permissions, assessments, availability of other
 resources, etc.
 

 

 This step is optional, as the creation of the appointment is never a guaranteed action.
 But by performing this availability check, you can increase the chances of making a successful
 booking.
 

 

 - 
 **Making the Appointment Request**
 

 When an appointment is required, a requester creates new Appointment resource with the Appointment.status="proposed".**
 All included participants (optional or mandatory) should have the status="needs-action" to allow filtering and displaying
 appointments to user-participants for accepting or rejecting new and updated requests. Based on internal system business rules,
 certain statuses may be automatically updated, for example: "reject because the requested participant is on vacation" or 
 "this type of user is not allowed to request those specific appointments".
 

 

 - 
 Replying to the request**
 

 The reply process is simply performed by the person/system handing the requests, updating
 the participant statuses on the appointment as needed. If there are multiple systems involved, then these
 will create AppointmentResponse entries with the desired statuses.
 

 

 Once all participants have their participation status created/updated
 (and the main system marking the appointment participant records with the AppointmentResponse
 statuses) then the overall status of the Appointment is updated.
 

 

 - 
 **Checking the overall status (Requester)**
 

 The requester (organizer) of the appointment checks for the overall status of the appointment
 (and appointment responses, where applicable) using FHIR pub-sub techniques.
 

 

 Where the participant statuses indicate that a re-scheduling is required, then the process may
 start again, with other systems replying to a new set of times.
 

 

 - 
 **Waitlisting the Appointment (optional)**
 

 This optional step permits creating a waitlisted appointment. This could occur if an
 appointment needs to be booked into a time that is not ideal for the patient due to lack of available
 time slots. In this workflow, there would be two appointments, the booked appointment in the time 
 slot that is currently available, and the waitlisted appointment with a requestedPeriod spanning the
 time that the patient would prefer if new slots become available.
 

 
 
 If new time slots become available during the requestedPeriod, the scheduling system, or staff
 at the scheduling organization, can notify the patient that a new time slot is available. If the patient
 chooses, the waitlisted appointment would then be booked into that specific slot, and the previously booked 
 appointment would be canceled. The specific business process for notifying patients of new availability is not
 specified, and is up to the implementing system to determine. 
 

 

 

 
### 12.10.1.2 There are 2 typical workflows that occur with appointments [
](appointment.html#workflow-types)

 

 - 
 **Outlook Style - Community**
 
 These types of requests are typically handled by selecting a specific time from a list of available slots,
 then making the request for that timeslot.
 

 

 - 
 **Hospital Scheduling - Clinical**
 

 Clinical scheduling is often far more complex in its requirements and processing.
 Often this involves checking multiple availabilities across multiple systems and
 timing with other internal systems, not just those exposed by the Slot resources.
 

 

 Consideration should be given to situations where scheduling needs to be handled
 in more of a queue-like process.
 

**
 Implementation Note:** 
 Note: This type of clinical appointment scheduling has not been specifically covered
 with this definition of the Appointment resource (and other related resources), however if you
 would like to contribute to the modification of this resource to cover these use cases,
 please contact the HL7 Patient Administration work-group.

 

 

 

 

 
## 12.10.2 Boundaries and Relationships [
](appointment.html#bnr)

 
### 12.10.2.1 Appointment Request/Response Pattern [](appointment.html#12.10.2.1)

 
 When using a request-response style of appointment this is done using Appointment 
 and AppointmentResponse resources.**
 The request is made in the form of an Appointment with a proposed or pending status,
 and the list of actors with a participation status of "needs-action".
 

 

 Participants in the appointment respond with their acceptance (or not) to the appointment
 by creating AppointmentResponse resources.

 Once all the participants have replied, then the Appointment resource is able to be
 updated with an overall status which collates the results of all the participants
 and presents the approved details of the appointment.
 

 

 The participant type property can be used to represent a specific role that a practitioner 
 is required to perform for the appointment. This could be specified without an actor when the actual
 practitioner is not known, and will be filled in closer to the scheduled time.

 This property must be the same between the Appointment-participant and the AppointmentResponse
 so that the appropriate values can be allocated.
 If you need multiple actors of a specific type, then multiple participants with that type value
 are included on the appointment.
 

 
### 12.10.2.2 Appointment Statuses and Encounters [
](appointment.html#statuses)

 
 Appointments can be considered as Administrative only, and the Encounter is expected to have
 clinical implications.
 

 

 In general, it is expected that appointments will result in the creation of an Encounter.
 The encounter is typically created when the service starts, not when the patient arrives.
 When the patient arrives, an appointment can be marked with a status of Arrived.
 

 

 In an Emergency Room context, the appointment Resource is probably not appropriate to be used.
 In these cases, an Encounter should be created.
 

 

 The Appointment request pattern used is different from the order-response pattern used elsewhere in FHIR.

 This is due to the close relationship to the iCal standard. Many non-clinical systems use generic
 non-health appointment systems which implement this standard, and the desire to integrate
 with the consumer who has no access to health based software is highly desirable.

 The mappings to the iCal standard have been provided to guide implementation of gateways between
 FHIR servers and iCal systems.
 

 
### 12.10.2.3 Appointment Locations and Participation [
](appointment.html#location)

 
 The location of the appointment is to be defined by using a participant that references a Location
 or HealthcareService resource.

 This permits the location to also have its availability checked via a schedule and any
 conflicts more easily managed.
 

 

This resource is referenced by [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [CarePlan](careplan.html#CarePlan), [Encounter](encounter.html#Encounter) and [ImagingStudy](imagingstudy.html#ImagingStudy)

## 12.10.3 
Resource Content
 [
](appointment.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Appointment](appointment-definitions.html#Appointment) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s)**+ Rule: Either start and end are specified, or neither
+ Rule: Only proposed or cancelled appointments can be missing start/end dates
+ Rule: Cancelation reason is only used for appointments that have been cancelled, or no-show
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](appointment-definitions.html#Appointment.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this item
 | |

| [status](appointment-definitions.html#Appointment.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
[AppointmentStatus](valueset-appointmentstatus.html) ([Required](terminologies.html#required)) | |

| [cancelationReason](appointment-definitions.html#Appointment.cancelationReason) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The coded reason for the appointment being cancelled
[Appointment cancellation reason](valueset-appointment-cancellation-reason.html) ([Example](terminologies.html#example)) | |

| [serviceCategory](appointment-definitions.html#Appointment.serviceCategory) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A broad categorization of the service that is to be performed during this appointment
[Service category](valueset-service-category.html) ([Example](terminologies.html#example))
 | |

| [serviceType](appointment-definitions.html#Appointment.serviceType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The specific service that is to be performed during this appointment
[Service type](valueset-service-type.html) ([Example](terminologies.html#example))
 | |

| [specialty](appointment-definitions.html#Appointment.specialty) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The specialty of a practitioner that would be required to perform the service requested in this appointment
[Practice Setting Code Value Set](valueset-c80-practice-codes.html) ([Preferred](terminologies.html#preferred))
 | |

| [appointmentType](appointment-definitions.html#Appointment.appointmentType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The style of appointment or patient that has been booked in the slot (not service type)
[v2 Appointment Reason Codes](v2/0276/index.html) ([Preferred](terminologies.html#preferred)) | |

| [reasonCode](appointment-definitions.html#Appointment.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason this appointment is scheduled
[Encounter Reason Codes](valueset-encounter-reason.html) ([Preferred](terminologies.html#preferred))
 | |

| [reasonReference](appointment-definitions.html#Appointment.reasonReference) | | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html) | [Observation](observation.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | Reason the appointment is to take place (resource)
 | |

| [priority](appointment-definitions.html#Appointment.priority) | | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Used to make informed decisions if needing to re-prioritize | |

| [description](appointment-definitions.html#Appointment.description) | | 0..1 | [string](datatypes.html#string) | Shown on a subject line in a meeting request, or appointment list | |

| [supportingInformation](appointment-definitions.html#Appointment.supportingInformation) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Additional information to support the appointment
 | |

| [start](appointment-definitions.html#Appointment.start) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [instant](datatypes.html#instant) | When appointment is to take place | |

| [end](appointment-definitions.html#Appointment.end) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [instant](datatypes.html#instant) | When appointment is to conclude | |

| [minutesDuration](appointment-definitions.html#Appointment.minutesDuration) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Can be less than start/end (e.g. estimate) | |

| [slot](appointment-definitions.html#Appointment.slot) | | 0..* | [Reference](references.html#Reference)([Slot](slot.html)) | The slots that this appointment is filling
 | |

| [created](appointment-definitions.html#Appointment.created) | | 0..1 | [dateTime](datatypes.html#dateTime) | The date that this appointment was initially created | |

| [comment](appointment-definitions.html#Appointment.comment) | | 0..1 | [string](datatypes.html#string) | Additional comments | |

| [patientInstruction](appointment-definitions.html#Appointment.patientInstruction) | | 0..1 | [string](datatypes.html#string) | Detailed information and instructions for the patient | |

| [basedOn](appointment-definitions.html#Appointment.basedOn) | | 0..* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | The service request this appointment is allocated to assess
 | |

| [participant](appointment-definitions.html#Appointment.participant) | [I](conformance-rules.html#constraints) | 1..* | [BackboneElement](backboneelement.html) | Participants involved in appointment
+ Rule: Either the type or actor on the participant SHALL be specified
 | |

| [type](appointment-definitions.html#Appointment.participant.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in the appointment
[Participant type](valueset-encounter-participant-type.html) ([Extensible](terminologies.html#extensible))
 | |

| [actor](appointment-definitions.html#Appointment.participant.actor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Device](device.html) | [HealthcareService](healthcareservice.html) | [Location](location.html)) | Person, Location/HealthcareService or Device | |

| [required](appointment-definitions.html#Appointment.participant.required) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | required | optional | information-only
[ParticipantRequired](valueset-participantrequired.html) ([Required](terminologies.html#required)) | |

| [status](appointment-definitions.html#Appointment.participant.status) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | accepted | declined | tentative | needs-action
[ParticipationStatus](valueset-participationstatus.html) ([Required](terminologies.html#required)) | |

| [period](appointment-definitions.html#Appointment.participant.period) | | 0..1 | [Period](datatypes.html#Period) | Participation period of the actor | |

| [requestedPeriod](appointment-definitions.html#Appointment.requestedPeriod) | | 0..* | [Period](datatypes.html#Period) | Potential date/time interval(s) requested to allocate the appointment within
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Appointment ([DomainResource](domainresource.html))[This records identifiers associated with this appointment concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)identifier](appointment-definitions.html#Appointment.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The overall status of the Appointment. Each of the participants has their own participation status which indicates their involvement in the process, however this status indicates the shared status (this element modifies the meaning of other elements)status](appointment-definitions.html#Appointment.status) : [code](datatypes.html#code) [1..1] « [The free/busy status of an appointment. (Strength=Required)AppointmentStatus](valueset-appointmentstatus.html)! »[The coded reason for the appointment being cancelled. This is often used in reporting/billing/futher processing to determine if further actions are required, or specific fees applycancelationReason](appointment-definitions.html#Appointment.cancelationReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [ (Strength=Example)](valueset-appointment-cancellation-reason.html) [AppointmentCancellationReason](valueset-appointment-cancellation-reason.html)?? »[A broad categorization of the service that is to be performed during this appointmentserviceCategory](appointment-definitions.html#Appointment.serviceCategory) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [ (Strength=Example)ServiceCategory](valueset-service-category.html)?? »[The specific service that is to be performed during this appointmentserviceType](appointment-definitions.html#Appointment.serviceType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [ (Strength=Example)ServiceType](valueset-service-type.html)?? »[The specialty of a practitioner that would be required to perform the service requested in this appointmentspecialty](appointment-definitions.html#Appointment.specialty) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [ (Strength=Preferred)PracticeSettingCodeValueSet](valueset-c80-practice-codes.html)? »[The style of appointment or patient that has been booked in the slot (not service type)appointmentType](appointment-definitions.html#Appointment.appointmentType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [ (Strength=Preferred)v2.0276](v2/0276/index.html)? »[The coded reason that this appointment is being scheduled. This is more clinical than administrativereasonCode](appointment-definitions.html#Appointment.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The Reason for the appointment to take place. (Strength=Preferred)EncounterReasonCodes](valueset-encounter-reason.html)? »[Reason the appointment has been scheduled to take place, as specified using information from another resource. When the patient arrives and the encounter begins it may be used as the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a ProcedurereasonReference](appointment-definitions.html#Appointment.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)| [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation) »[The priority of the appointment. Can be used to make informed decisions if needing to re-prioritize appointments. (The iCal Standard specifies 0 as undefined, 1 as highest, 9 as lowest priority)priority](appointment-definitions.html#Appointment.priority) : [unsignedInt](datatypes.html#unsignedInt) [0..1][The brief description of the appointment as would be shown on a subject line in a meeting request, or appointment list. Detailed or expanded information should be put in the comment fielddescription](appointment-definitions.html#Appointment.description) : [string](datatypes.html#string) [0..1][Additional information to support the appointment provided when making the appointmentsupportingInformation](appointment-definitions.html#Appointment.supportingInformation) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Date/Time that the appointment is to take placestart](appointment-definitions.html#Appointment.start) : [instant](datatypes.html#instant) [0..1][Date/Time that the appointment is to concludeend](appointment-definitions.html#Appointment.end) : [instant](datatypes.html#instant) [0..1][Number of minutes that the appointment is to take. This can be less than the duration between the start and end times. For example, where the actual time of appointment is only an estimate or if a 30 minute appointment is being requested, but any time would work. Also, if there is, for example, a planned 15 minute break in the middle of a long appointment, the duration may be 15 minutes less than the difference between the start and endminutesDuration](appointment-definitions.html#Appointment.minutesDuration) : [positiveInt](datatypes.html#positiveInt) [0..1][The slots from the participants' schedules that will be filled by the appointmentslot](appointment-definitions.html#Appointment.slot) : [Reference](references.html#Reference) [0..*] « [Slot](slot.html#Slot) »[The date that this appointment was initially created. This could be different to the meta.lastModified value on the initial entry, as this could have been before the resource was created on the FHIR server, and should remain unchanged over the lifespan of the appointmentcreated](appointment-definitions.html#Appointment.created) : [dateTime](datatypes.html#dateTime) [0..1][Additional comments about the appointmentcomment](appointment-definitions.html#Appointment.comment) : [string](datatypes.html#string) [0..1][While Appointment.comment contains information for internal use, Appointment.patientInstructions is used to capture patient facing information about the Appointment (e.g. please bring your referral or fast from 8pm night before)patientInstruction](appointment-definitions.html#Appointment.patientInstruction) : [string](datatypes.html#string) [0..1][The service request this appointment is allocated to assess (e.g. incoming referral or procedure request)basedOn](appointment-definitions.html#Appointment.basedOn) : [Reference](references.html#Reference) [0..*] « [ServiceRequest](servicerequest.html#ServiceRequest) »[A set of date ranges (potentially including times) that the appointment is preferred to be scheduled within.

The duration (usually in minutes) could also be provided to indicate the length of the appointment to fill and populate the start/end times for the actual allocated time. However, in other situations the duration may be calculated by the scheduling systemrequestedPeriod](appointment-definitions.html#Appointment.requestedPeriod) : [Period](datatypes.html#Period) [0..*]Participant[Role of participant in the appointmenttype](appointment-definitions.html#Appointment.participant.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Role of participant in encounter. (Strength=Extensible)ParticipantType](valueset-encounter-participant-type.html)+ »[A Person, Location/HealthcareService or Device that is participating in the appointmentactor](appointment-definitions.html#Appointment.participant.actor) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location) »[Whether this participant is required to be present at the meeting. This covers a use-case where two doctors need to meet to discuss the results for a specific patient, and the patient is not required to be presentrequired](appointment-definitions.html#Appointment.participant.required) : [code](datatypes.html#code) [0..1] « [Is the Participant required to attend the appointment. (Strength=Required)ParticipantRequired](valueset-participantrequired.html)! »[Participation status of the actorstatus](appointment-definitions.html#Appointment.participant.status) : [code](datatypes.html#code) [1..1] « [The Participation status of an appointment. (Strength=Required)ParticipationStatus](valueset-participationstatus.html)! »[Participation period of the actorperiod](appointment-definitions.html#Appointment.participant.period) : [Period](datatypes.html#Period) [0..1]
[List of participants involved in the appointmentparticipant](appointment-definitions.html#Appointment.participant)[1..*]
 

 

 

**XML Template**

 

 
```
<[**Appointment**](appointment-definitions.html#Appointment) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](appointment-definitions.html#Appointment.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External Ids for this item](terminologies.html#unbound) --></identifier>
 <[**status**](appointment-definitions.html#Appointment.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist](valueset-appointmentstatus.html) -->
 <[**cancelationReason**](appointment-definitions.html#Appointment.cancelationReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The coded reason for the appointment being cancelled](valueset-appointment-cancellation-reason.html) --></cancelationReason>
 <[**serviceCategory**](appointment-definitions.html#Appointment.serviceCategory)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A broad categorization of the service that is to be performed during this appointment](valueset-service-category.html) --></serviceCategory>
 <[**serviceType**](appointment-definitions.html#Appointment.serviceType)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [The specific service that is to be performed during this appointment](valueset-service-type.html) --></serviceType>
 <[**specialty**](appointment-definitions.html#Appointment.specialty)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [The specialty of a practitioner that would be required to perform the service requested in this appointment](valueset-c80-practice-codes.html) --></specialty>
 <[**appointmentType**](appointment-definitions.html#Appointment.appointmentType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The style of appointment or patient that has been booked in the slot (not service type)](v2/0276/index.html) --></appointmentType>
 <[**reasonCode**](appointment-definitions.html#Appointment.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Coded reason this appointment is scheduled](valueset-encounter-reason.html) --></reasonCode>
 <[**reasonReference**](appointment-definitions.html#Appointment.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) [Reason the appointment is to take place (resource)](terminologies.html#unbound) --></reasonReference>
 <[**priority**](appointment-definitions.html#Appointment.priority) value="[[unsignedInt](datatypes.html#unsignedInt)]"/><!-- **0..1** [Used to make informed decisions if needing to re-prioritize](terminologies.html#unbound) -->
 <[**description**](appointment-definitions.html#Appointment.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Shown on a subject line in a meeting request, or appointment list](terminologies.html#unbound) -->
 <[**supportingInformation**](appointment-definitions.html#Appointment.supportingInformation)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Additional information to support the appointment](terminologies.html#unbound) --></supportingInformation>
 <[**start**](appointment-definitions.html#Appointment.start) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [When appointment is to take place](terminologies.html#unbound) -->
 <[**end**](appointment-definitions.html#Appointment.end) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [When appointment is to conclude](terminologies.html#unbound) -->
 <[**minutesDuration**](appointment-definitions.html#Appointment.minutesDuration) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [Can be less than start/end (e.g. estimate)](terminologies.html#unbound) -->
 <[**slot**](appointment-definitions.html#Appointment.slot)><!-- **0..*** [Reference](references.html#Reference)([Slot](slot.html#Slot)) [The slots that this appointment is filling](terminologies.html#unbound) --></slot>
 <[**created**](appointment-definitions.html#Appointment.created) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [The date that this appointment was initially created](terminologies.html#unbound) -->
 <[**comment**](appointment-definitions.html#Appointment.comment) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional comments](terminologies.html#unbound) -->
 <[**patientInstruction**](appointment-definitions.html#Appointment.patientInstruction) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Detailed information and instructions for the patient](terminologies.html#unbound) -->
 <[**basedOn**](appointment-definitions.html#Appointment.basedOn)><!-- **0..*** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [The service request this appointment is allocated to assess](terminologies.html#unbound) --></basedOn>
 <[**participant**](appointment-definitions.html#Appointment.participant)> <!-- **1..*** Participants involved in appointment -->
 <[**type**](appointment-definitions.html#Appointment.participant.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Role of participant in the appointment](valueset-encounter-participant-type.html) --></type>
 <[**actor**](appointment-definitions.html#Appointment.participant.actor)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) [Person, Location/HealthcareService or Device](terminologies.html#unbound) --></actor>
 <[**required**](appointment-definitions.html#Appointment.participant.required) value="[[code](datatypes.html#code)]"/><!-- **0..1** [required | optional | information-only](valueset-participantrequired.html) -->
 <[**status**](appointment-definitions.html#Appointment.participant.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [accepted | declined | tentative | needs-action](valueset-participationstatus.html) -->
 <[**period**](appointment-definitions.html#Appointment.participant.period)><!-- **0..1** [Period](datatypes.html#Period) [Participation period of the actor](terminologies.html#unbound) --></period>
 </participant>
 <[**requestedPeriod**](appointment-definitions.html#Appointment.requestedPeriod)><!-- **0..*** [Period](datatypes.html#Period) [Potential date/time interval(s) requested to allocate the appointment within](terminologies.html#unbound) --></requestedPeriod>
</Appointment>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Appointment**](appointment-definitions.html#Appointment)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](appointment-definitions.html#Appointment.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this item](terminologies.html#unbound)
 "[status](appointment-definitions.html#Appointment.status)" : "<[code](datatypes.html#code)>", // **R!** [proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist](valueset-appointmentstatus.html)
 "[cancelationReason](appointment-definitions.html#Appointment.cancelationReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The coded reason for the appointment being cancelled](valueset-appointment-cancellation-reason.html)
 "[serviceCategory](appointment-definitions.html#Appointment.serviceCategory)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [A broad categorization of the service that is to be performed during this appointment](valueset-service-category.html)
 "[serviceType](appointment-definitions.html#Appointment.serviceType)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [The specific service that is to be performed during this appointment](valueset-service-type.html)
 "[specialty](appointment-definitions.html#Appointment.specialty)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [The specialty of a practitioner that would be required to perform the service requested in this appointment](valueset-c80-practice-codes.html)
 "[appointmentType](appointment-definitions.html#Appointment.appointmentType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The style of appointment or patient that has been booked in the slot (not service type)](v2/0276/index.html)
 "[reasonCode](appointment-definitions.html#Appointment.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Coded reason this appointment is scheduled](valueset-encounter-reason.html)
 "[reasonReference](appointment-definitions.html#Appointment.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) }], // [Reason the appointment is to take place (resource)](terminologies.html#unbound)
 "[priority](appointment-definitions.html#Appointment.priority)" : "<[unsignedInt](datatypes.html#unsignedInt)>", // [Used to make informed decisions if needing to re-prioritize](terminologies.html#unbound)
 "[description](appointment-definitions.html#Appointment.description)" : "<[string](datatypes.html#string)>", // [Shown on a subject line in a meeting request, or appointment list](terminologies.html#unbound)
 "[supportingInformation](appointment-definitions.html#Appointment.supportingInformation)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Additional information to support the appointment](terminologies.html#unbound)
 "[start](appointment-definitions.html#Appointment.start)" : "<[instant](datatypes.html#instant)>", // [When appointment is to take place](terminologies.html#unbound)
 "[end](appointment-definitions.html#Appointment.end)" : "<[instant](datatypes.html#instant)>", // [When appointment is to conclude](terminologies.html#unbound)
 "[minutesDuration](appointment-definitions.html#Appointment.minutesDuration)" : "<[positiveInt](datatypes.html#positiveInt)>", // [Can be less than start/end (e.g. estimate)](terminologies.html#unbound)
 "[slot](appointment-definitions.html#Appointment.slot)" : [{ [Reference](references.html#Reference)([Slot](slot.html#Slot)) }], // [The slots that this appointment is filling](terminologies.html#unbound)
 "[created](appointment-definitions.html#Appointment.created)" : "<[dateTime](datatypes.html#dateTime)>", // [The date that this appointment was initially created](terminologies.html#unbound)
 "[comment](appointment-definitions.html#Appointment.comment)" : "<[string](datatypes.html#string)>", // [Additional comments](terminologies.html#unbound)
 "[patientInstruction](appointment-definitions.html#Appointment.patientInstruction)" : "<[string](datatypes.html#string)>", // [Detailed information and instructions for the patient](terminologies.html#unbound)
 "[basedOn](appointment-definitions.html#Appointment.basedOn)" : [{ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }], // [The service request this appointment is allocated to assess](terminologies.html#unbound)
 "[participant](appointment-definitions.html#Appointment.participant)" : [{ // **R!** [Participants involved in appointment](terminologies.html#unbound)
 "[type](appointment-definitions.html#Appointment.participant.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Role of participant in the appointment](valueset-encounter-participant-type.html)
 "[actor](appointment-definitions.html#Appointment.participant.actor)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) }, // [Person, Location/HealthcareService or Device](terminologies.html#unbound)
 "[required](appointment-definitions.html#Appointment.participant.required)" : "<[code](datatypes.html#code)>", // [required | optional | information-only](valueset-participantrequired.html)
 "[status](appointment-definitions.html#Appointment.participant.status)" : "<[code](datatypes.html#code)>", // **R!** [accepted | declined | tentative | needs-action](valueset-participationstatus.html)
 "[period](appointment-definitions.html#Appointment.participant.period)" : { [Period](datatypes.html#Period) } // [Participation period of the actor](terminologies.html#unbound)
 }],
 "[requestedPeriod](appointment-definitions.html#Appointment.requestedPeriod)" : [{ [Period](datatypes.html#Period) }] // [Potential date/time interval(s) requested to allocate the appointment within](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Appointment**](appointment-definitions.html#Appointment);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Appointment.identifier](appointment-definitions.html#Appointment.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this item
 fhir:[Appointment.status](appointment-definitions.html#Appointment.status) [ [code](datatypes.html#code) ]; # 1..1 proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
 fhir:[Appointment.cancelationReason](appointment-definitions.html#Appointment.cancelationReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The coded reason for the appointment being cancelled
 fhir:[Appointment.serviceCategory](appointment-definitions.html#Appointment.serviceCategory) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A broad categorization of the service that is to be performed during this appointment
 fhir:[Appointment.serviceType](appointment-definitions.html#Appointment.serviceType) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* The specific service that is to be performed during this appointment
 fhir:[Appointment.specialty](appointment-definitions.html#Appointment.specialty) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* The specialty of a practitioner that would be required to perform the service requested in this appointment
 fhir:[Appointment.appointmentType](appointment-definitions.html#Appointment.appointmentType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The style of appointment or patient that has been booked in the slot (not service type)
 fhir:[Appointment.reasonCode](appointment-definitions.html#Appointment.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Coded reason this appointment is scheduled
 fhir:[Appointment.reasonReference](appointment-definitions.html#Appointment.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) ], ... ; # 0..* Reason the appointment is to take place (resource)
 fhir:[Appointment.priority](appointment-definitions.html#Appointment.priority) [ [unsignedInt](datatypes.html#unsignedInt) ]; # 0..1 Used to make informed decisions if needing to re-prioritize
 fhir:[Appointment.description](appointment-definitions.html#Appointment.description) [ [string](datatypes.html#string) ]; # 0..1 Shown on a subject line in a meeting request, or appointment list
 fhir:[Appointment.supportingInformation](appointment-definitions.html#Appointment.supportingInformation) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Additional information to support the appointment
 fhir:[Appointment.start](appointment-definitions.html#Appointment.start) [ [instant](datatypes.html#instant) ]; # 0..1 When appointment is to take place
 fhir:[Appointment.end](appointment-definitions.html#Appointment.end) [ [instant](datatypes.html#instant) ]; # 0..1 When appointment is to conclude
 fhir:[Appointment.minutesDuration](appointment-definitions.html#Appointment.minutesDuration) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Can be less than start/end (e.g. estimate)
 fhir:[Appointment.slot](appointment-definitions.html#Appointment.slot) [ [Reference](references.html#Reference)([Slot](slot.html#Slot)) ], ... ; # 0..* The slots that this appointment is filling
 fhir:[Appointment.created](appointment-definitions.html#Appointment.created) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 The date that this appointment was initially created
 fhir:[Appointment.comment](appointment-definitions.html#Appointment.comment) [ [string](datatypes.html#string) ]; # 0..1 Additional comments
 fhir:[Appointment.patientInstruction](appointment-definitions.html#Appointment.patientInstruction) [ [string](datatypes.html#string) ]; # 0..1 Detailed information and instructions for the patient
 fhir:[Appointment.basedOn](appointment-definitions.html#Appointment.basedOn) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ], ... ; # 0..* The service request this appointment is allocated to assess
 fhir:[Appointment.participant](appointment-definitions.html#Appointment.participant) [ # 1..* Participants involved in appointment
 fhir:[Appointment.participant.type](appointment-definitions.html#Appointment.participant.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Role of participant in the appointment
 fhir:[Appointment.participant.actor](appointment-definitions.html#Appointment.participant.actor) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|
 [Location](location.html#Location)) ]; # 0..1 Person, Location/HealthcareService or Device
 fhir:[Appointment.participant.required](appointment-definitions.html#Appointment.participant.required) [ [code](datatypes.html#code) ]; # 0..1 required | optional | information-only
 fhir:[Appointment.participant.status](appointment-definitions.html#Appointment.participant.status) [ [code](datatypes.html#code) ]; # 1..1 accepted | declined | tentative | needs-action
 fhir:[Appointment.participant.period](appointment-definitions.html#Appointment.participant.period) [ [Period](datatypes.html#Period) ]; # 0..1 Participation period of the actor
 ], ...;
 fhir:[Appointment.requestedPeriod](appointment-definitions.html#Appointment.requestedPeriod) [ [Period](datatypes.html#Period) ], ... ; # 0..* Potential date/time interval(s) requested to allocate the appointment within
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Appointment](appointment.html#Appointment)
 | 
 | 
 |

 | 
 Appointment.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/appointmentstatus to http://hl7.org/fhir/ValueSet/appointmentstatus|4.0.1

 

 | 
 |

 | 
 Appointment.cancelationReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.serviceCategory | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Appointment.reasonCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.reasonReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.patientInstruction | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.basedOn | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.participant.actor | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Appointment.participant.required | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/participantrequired to http://hl7.org/fhir/ValueSet/participantrequired|4.0.1

 

 | 
 |

 | 
 Appointment.participant.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/participationstatus to http://hl7.org/fhir/ValueSet/participationstatus|4.0.1

 

 | 
 |

 | 
 Appointment.participant.period | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.reason | 
 
 

 - deleted

 

 | 
 |

 | 
 Appointment.indication | 
 
 

 - deleted

 

 | 
 |

 | 
 Appointment.incomingReferral | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](appointment.diff.xml) or [JSON](appointment.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](appointment-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Appointment](appointment-definitions.html#Appointment) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s)**+ Rule: Either start and end are specified, or neither
+ Rule: Only proposed or cancelled appointments can be missing start/end dates
+ Rule: Cancelation reason is only used for appointments that have been cancelled, or no-show
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](appointment-definitions.html#Appointment.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this item
 | |

| [status](appointment-definitions.html#Appointment.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
[AppointmentStatus](valueset-appointmentstatus.html) ([Required](terminologies.html#required)) | |

| [cancelationReason](appointment-definitions.html#Appointment.cancelationReason) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The coded reason for the appointment being cancelled
[Appointment cancellation reason](valueset-appointment-cancellation-reason.html) ([Example](terminologies.html#example)) | |

| [serviceCategory](appointment-definitions.html#Appointment.serviceCategory) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | A broad categorization of the service that is to be performed during this appointment
[Service category](valueset-service-category.html) ([Example](terminologies.html#example))
 | |

| [serviceType](appointment-definitions.html#Appointment.serviceType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The specific service that is to be performed during this appointment
[Service type](valueset-service-type.html) ([Example](terminologies.html#example))
 | |

| [specialty](appointment-definitions.html#Appointment.specialty) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The specialty of a practitioner that would be required to perform the service requested in this appointment
[Practice Setting Code Value Set](valueset-c80-practice-codes.html) ([Preferred](terminologies.html#preferred))
 | |

| [appointmentType](appointment-definitions.html#Appointment.appointmentType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The style of appointment or patient that has been booked in the slot (not service type)
[v2 Appointment Reason Codes](v2/0276/index.html) ([Preferred](terminologies.html#preferred)) | |

| [reasonCode](appointment-definitions.html#Appointment.reasonCode) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Coded reason this appointment is scheduled
[Encounter Reason Codes](valueset-encounter-reason.html) ([Preferred](terminologies.html#preferred))
 | |

| [reasonReference](appointment-definitions.html#Appointment.reasonReference) | | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Procedure](procedure.html) | [Observation](observation.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | Reason the appointment is to take place (resource)
 | |

| [priority](appointment-definitions.html#Appointment.priority) | | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Used to make informed decisions if needing to re-prioritize | |

| [description](appointment-definitions.html#Appointment.description) | | 0..1 | [string](datatypes.html#string) | Shown on a subject line in a meeting request, or appointment list | |

| [supportingInformation](appointment-definitions.html#Appointment.supportingInformation) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Additional information to support the appointment
 | |

| [start](appointment-definitions.html#Appointment.start) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [instant](datatypes.html#instant) | When appointment is to take place | |

| [end](appointment-definitions.html#Appointment.end) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [instant](datatypes.html#instant) | When appointment is to conclude | |

| [minutesDuration](appointment-definitions.html#Appointment.minutesDuration) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Can be less than start/end (e.g. estimate) | |

| [slot](appointment-definitions.html#Appointment.slot) | | 0..* | [Reference](references.html#Reference)([Slot](slot.html)) | The slots that this appointment is filling
 | |

| [created](appointment-definitions.html#Appointment.created) | | 0..1 | [dateTime](datatypes.html#dateTime) | The date that this appointment was initially created | |

| [comment](appointment-definitions.html#Appointment.comment) | | 0..1 | [string](datatypes.html#string) | Additional comments | |

| [patientInstruction](appointment-definitions.html#Appointment.patientInstruction) | | 0..1 | [string](datatypes.html#string) | Detailed information and instructions for the patient | |

| [basedOn](appointment-definitions.html#Appointment.basedOn) | | 0..* | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | The service request this appointment is allocated to assess
 | |

| [participant](appointment-definitions.html#Appointment.participant) | [I](conformance-rules.html#constraints) | 1..* | [BackboneElement](backboneelement.html) | Participants involved in appointment
+ Rule: Either the type or actor on the participant SHALL be specified
 | |

| [type](appointment-definitions.html#Appointment.participant.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Role of participant in the appointment
[Participant type](valueset-encounter-participant-type.html) ([Extensible](terminologies.html#extensible))
 | |

| [actor](appointment-definitions.html#Appointment.participant.actor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Device](device.html) | [HealthcareService](healthcareservice.html) | [Location](location.html)) | Person, Location/HealthcareService or Device | |

| [required](appointment-definitions.html#Appointment.participant.required) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | required | optional | information-only
[ParticipantRequired](valueset-participantrequired.html) ([Required](terminologies.html#required)) | |

| [status](appointment-definitions.html#Appointment.participant.status) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | accepted | declined | tentative | needs-action
[ParticipationStatus](valueset-participationstatus.html) ([Required](terminologies.html#required)) | |

| [period](appointment-definitions.html#Appointment.participant.period) | | 0..1 | [Period](datatypes.html#Period) | Participation period of the actor | |

| [requestedPeriod](appointment-definitions.html#Appointment.requestedPeriod) | | 0..* | [Period](datatypes.html#Period) | Potential date/time interval(s) requested to allocate the appointment within
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Appointment ([DomainResource](domainresource.html))[This records identifiers associated with this appointment concern that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate (e.g. in CDA documents, or in written / printed documentation)identifier](appointment-definitions.html#Appointment.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The overall status of the Appointment. Each of the participants has their own participation status which indicates their involvement in the process, however this status indicates the shared status (this element modifies the meaning of other elements)status](appointment-definitions.html#Appointment.status) : [code](datatypes.html#code) [1..1] « [The free/busy status of an appointment. (Strength=Required)AppointmentStatus](valueset-appointmentstatus.html)! »[The coded reason for the appointment being cancelled. This is often used in reporting/billing/futher processing to determine if further actions are required, or specific fees applycancelationReason](appointment-definitions.html#Appointment.cancelationReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [ (Strength=Example)](valueset-appointment-cancellation-reason.html) [AppointmentCancellationReason](valueset-appointment-cancellation-reason.html)?? »[A broad categorization of the service that is to be performed during this appointmentserviceCategory](appointment-definitions.html#Appointment.serviceCategory) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [ (Strength=Example)ServiceCategory](valueset-service-category.html)?? »[The specific service that is to be performed during this appointmentserviceType](appointment-definitions.html#Appointment.serviceType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [ (Strength=Example)ServiceType](valueset-service-type.html)?? »[The specialty of a practitioner that would be required to perform the service requested in this appointmentspecialty](appointment-definitions.html#Appointment.specialty) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [ (Strength=Preferred)PracticeSettingCodeValueSet](valueset-c80-practice-codes.html)? »[The style of appointment or patient that has been booked in the slot (not service type)appointmentType](appointment-definitions.html#Appointment.appointmentType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [ (Strength=Preferred)v2.0276](v2/0276/index.html)? »[The coded reason that this appointment is being scheduled. This is more clinical than administrativereasonCode](appointment-definitions.html#Appointment.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The Reason for the appointment to take place. (Strength=Preferred)EncounterReasonCodes](valueset-encounter-reason.html)? »[Reason the appointment has been scheduled to take place, as specified using information from another resource. When the patient arrives and the encounter begins it may be used as the admission diagnosis. The indication will typically be a Condition (with other resources referenced in the evidence.detail), or a ProcedurereasonReference](appointment-definitions.html#Appointment.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)| [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation) »[The priority of the appointment. Can be used to make informed decisions if needing to re-prioritize appointments. (The iCal Standard specifies 0 as undefined, 1 as highest, 9 as lowest priority)priority](appointment-definitions.html#Appointment.priority) : [unsignedInt](datatypes.html#unsignedInt) [0..1][The brief description of the appointment as would be shown on a subject line in a meeting request, or appointment list. Detailed or expanded information should be put in the comment fielddescription](appointment-definitions.html#Appointment.description) : [string](datatypes.html#string) [0..1][Additional information to support the appointment provided when making the appointmentsupportingInformation](appointment-definitions.html#Appointment.supportingInformation) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[Date/Time that the appointment is to take placestart](appointment-definitions.html#Appointment.start) : [instant](datatypes.html#instant) [0..1][Date/Time that the appointment is to concludeend](appointment-definitions.html#Appointment.end) : [instant](datatypes.html#instant) [0..1][Number of minutes that the appointment is to take. This can be less than the duration between the start and end times. For example, where the actual time of appointment is only an estimate or if a 30 minute appointment is being requested, but any time would work. Also, if there is, for example, a planned 15 minute break in the middle of a long appointment, the duration may be 15 minutes less than the difference between the start and endminutesDuration](appointment-definitions.html#Appointment.minutesDuration) : [positiveInt](datatypes.html#positiveInt) [0..1][The slots from the participants' schedules that will be filled by the appointmentslot](appointment-definitions.html#Appointment.slot) : [Reference](references.html#Reference) [0..*] « [Slot](slot.html#Slot) »[The date that this appointment was initially created. This could be different to the meta.lastModified value on the initial entry, as this could have been before the resource was created on the FHIR server, and should remain unchanged over the lifespan of the appointmentcreated](appointment-definitions.html#Appointment.created) : [dateTime](datatypes.html#dateTime) [0..1][Additional comments about the appointmentcomment](appointment-definitions.html#Appointment.comment) : [string](datatypes.html#string) [0..1][While Appointment.comment contains information for internal use, Appointment.patientInstructions is used to capture patient facing information about the Appointment (e.g. please bring your referral or fast from 8pm night before)patientInstruction](appointment-definitions.html#Appointment.patientInstruction) : [string](datatypes.html#string) [0..1][The service request this appointment is allocated to assess (e.g. incoming referral or procedure request)basedOn](appointment-definitions.html#Appointment.basedOn) : [Reference](references.html#Reference) [0..*] « [ServiceRequest](servicerequest.html#ServiceRequest) »[A set of date ranges (potentially including times) that the appointment is preferred to be scheduled within.

The duration (usually in minutes) could also be provided to indicate the length of the appointment to fill and populate the start/end times for the actual allocated time. However, in other situations the duration may be calculated by the scheduling systemrequestedPeriod](appointment-definitions.html#Appointment.requestedPeriod) : [Period](datatypes.html#Period) [0..*]Participant[Role of participant in the appointmenttype](appointment-definitions.html#Appointment.participant.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Role of participant in encounter. (Strength=Extensible)ParticipantType](valueset-encounter-participant-type.html)+ »[A Person, Location/HealthcareService or Device that is participating in the appointmentactor](appointment-definitions.html#Appointment.participant.actor) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location) »[Whether this participant is required to be present at the meeting. This covers a use-case where two doctors need to meet to discuss the results for a specific patient, and the patient is not required to be presentrequired](appointment-definitions.html#Appointment.participant.required) : [code](datatypes.html#code) [0..1] « [Is the Participant required to attend the appointment. (Strength=Required)ParticipantRequired](valueset-participantrequired.html)! »[Participation status of the actorstatus](appointment-definitions.html#Appointment.participant.status) : [code](datatypes.html#code) [1..1] « [The Participation status of an appointment. (Strength=Required)ParticipationStatus](valueset-participationstatus.html)! »[Participation period of the actorperiod](appointment-definitions.html#Appointment.participant.period) : [Period](datatypes.html#Period) [0..1]
[List of participants involved in the appointmentparticipant](appointment-definitions.html#Appointment.participant)[1..*]
 

**XML Template**

 

 
```
<[**Appointment**](appointment-definitions.html#Appointment) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](appointment-definitions.html#Appointment.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External Ids for this item](terminologies.html#unbound) --></identifier>
 <[**status**](appointment-definitions.html#Appointment.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist](valueset-appointmentstatus.html) -->
 <[**cancelationReason**](appointment-definitions.html#Appointment.cancelationReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The coded reason for the appointment being cancelled](valueset-appointment-cancellation-reason.html) --></cancelationReason>
 <[**serviceCategory**](appointment-definitions.html#Appointment.serviceCategory)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [A broad categorization of the service that is to be performed during this appointment](valueset-service-category.html) --></serviceCategory>
 <[**serviceType**](appointment-definitions.html#Appointment.serviceType)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [The specific service that is to be performed during this appointment](valueset-service-type.html) --></serviceType>
 <[**specialty**](appointment-definitions.html#Appointment.specialty)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [The specialty of a practitioner that would be required to perform the service requested in this appointment](valueset-c80-practice-codes.html) --></specialty>
 <[**appointmentType**](appointment-definitions.html#Appointment.appointmentType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The style of appointment or patient that has been booked in the slot (not service type)](v2/0276/index.html) --></appointmentType>
 <[**reasonCode**](appointment-definitions.html#Appointment.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Coded reason this appointment is scheduled](valueset-encounter-reason.html) --></reasonCode>
 <[**reasonReference**](appointment-definitions.html#Appointment.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) [Reason the appointment is to take place (resource)](terminologies.html#unbound) --></reasonReference>
 <[**priority**](appointment-definitions.html#Appointment.priority) value="[[unsignedInt](datatypes.html#unsignedInt)]"/><!-- **0..1** [Used to make informed decisions if needing to re-prioritize](terminologies.html#unbound) -->
 <[**description**](appointment-definitions.html#Appointment.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Shown on a subject line in a meeting request, or appointment list](terminologies.html#unbound) -->
 <[**supportingInformation**](appointment-definitions.html#Appointment.supportingInformation)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Additional information to support the appointment](terminologies.html#unbound) --></supportingInformation>
 <[**start**](appointment-definitions.html#Appointment.start) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [When appointment is to take place](terminologies.html#unbound) -->
 <[**end**](appointment-definitions.html#Appointment.end) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [When appointment is to conclude](terminologies.html#unbound) -->
 <[**minutesDuration**](appointment-definitions.html#Appointment.minutesDuration) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [Can be less than start/end (e.g. estimate)](terminologies.html#unbound) -->
 <[**slot**](appointment-definitions.html#Appointment.slot)><!-- **0..*** [Reference](references.html#Reference)([Slot](slot.html#Slot)) [The slots that this appointment is filling](terminologies.html#unbound) --></slot>
 <[**created**](appointment-definitions.html#Appointment.created) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [The date that this appointment was initially created](terminologies.html#unbound) -->
 <[**comment**](appointment-definitions.html#Appointment.comment) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional comments](terminologies.html#unbound) -->
 <[**patientInstruction**](appointment-definitions.html#Appointment.patientInstruction) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Detailed information and instructions for the patient](terminologies.html#unbound) -->
 <[**basedOn**](appointment-definitions.html#Appointment.basedOn)><!-- **0..*** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [The service request this appointment is allocated to assess](terminologies.html#unbound) --></basedOn>
 <[**participant**](appointment-definitions.html#Appointment.participant)> <!-- **1..*** Participants involved in appointment -->
 <[**type**](appointment-definitions.html#Appointment.participant.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Role of participant in the appointment](valueset-encounter-participant-type.html) --></type>
 <[**actor**](appointment-definitions.html#Appointment.participant.actor)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) [Person, Location/HealthcareService or Device](terminologies.html#unbound) --></actor>
 <[**required**](appointment-definitions.html#Appointment.participant.required) value="[[code](datatypes.html#code)]"/><!-- **0..1** [required | optional | information-only](valueset-participantrequired.html) -->
 <[**status**](appointment-definitions.html#Appointment.participant.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [accepted | declined | tentative | needs-action](valueset-participationstatus.html) -->
 <[**period**](appointment-definitions.html#Appointment.participant.period)><!-- **0..1** [Period](datatypes.html#Period) [Participation period of the actor](terminologies.html#unbound) --></period>
 </participant>
 <[**requestedPeriod**](appointment-definitions.html#Appointment.requestedPeriod)><!-- **0..*** [Period](datatypes.html#Period) [Potential date/time interval(s) requested to allocate the appointment within](terminologies.html#unbound) --></requestedPeriod>
</Appointment>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Appointment**](appointment-definitions.html#Appointment)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](appointment-definitions.html#Appointment.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this item](terminologies.html#unbound)
 "[status](appointment-definitions.html#Appointment.status)" : "<[code](datatypes.html#code)>", // **R!** [proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist](valueset-appointmentstatus.html)
 "[cancelationReason](appointment-definitions.html#Appointment.cancelationReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The coded reason for the appointment being cancelled](valueset-appointment-cancellation-reason.html)
 "[serviceCategory](appointment-definitions.html#Appointment.serviceCategory)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [A broad categorization of the service that is to be performed during this appointment](valueset-service-category.html)
 "[serviceType](appointment-definitions.html#Appointment.serviceType)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [The specific service that is to be performed during this appointment](valueset-service-type.html)
 "[specialty](appointment-definitions.html#Appointment.specialty)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [The specialty of a practitioner that would be required to perform the service requested in this appointment](valueset-c80-practice-codes.html)
 "[appointmentType](appointment-definitions.html#Appointment.appointmentType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The style of appointment or patient that has been booked in the slot (not service type)](v2/0276/index.html)
 "[reasonCode](appointment-definitions.html#Appointment.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Coded reason this appointment is scheduled](valueset-encounter-reason.html)
 "[reasonReference](appointment-definitions.html#Appointment.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) }], // [Reason the appointment is to take place (resource)](terminologies.html#unbound)
 "[priority](appointment-definitions.html#Appointment.priority)" : "<[unsignedInt](datatypes.html#unsignedInt)>", // [Used to make informed decisions if needing to re-prioritize](terminologies.html#unbound)
 "[description](appointment-definitions.html#Appointment.description)" : "<[string](datatypes.html#string)>", // [Shown on a subject line in a meeting request, or appointment list](terminologies.html#unbound)
 "[supportingInformation](appointment-definitions.html#Appointment.supportingInformation)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Additional information to support the appointment](terminologies.html#unbound)
 "[start](appointment-definitions.html#Appointment.start)" : "<[instant](datatypes.html#instant)>", // [When appointment is to take place](terminologies.html#unbound)
 "[end](appointment-definitions.html#Appointment.end)" : "<[instant](datatypes.html#instant)>", // [When appointment is to conclude](terminologies.html#unbound)
 "[minutesDuration](appointment-definitions.html#Appointment.minutesDuration)" : "<[positiveInt](datatypes.html#positiveInt)>", // [Can be less than start/end (e.g. estimate)](terminologies.html#unbound)
 "[slot](appointment-definitions.html#Appointment.slot)" : [{ [Reference](references.html#Reference)([Slot](slot.html#Slot)) }], // [The slots that this appointment is filling](terminologies.html#unbound)
 "[created](appointment-definitions.html#Appointment.created)" : "<[dateTime](datatypes.html#dateTime)>", // [The date that this appointment was initially created](terminologies.html#unbound)
 "[comment](appointment-definitions.html#Appointment.comment)" : "<[string](datatypes.html#string)>", // [Additional comments](terminologies.html#unbound)
 "[patientInstruction](appointment-definitions.html#Appointment.patientInstruction)" : "<[string](datatypes.html#string)>", // [Detailed information and instructions for the patient](terminologies.html#unbound)
 "[basedOn](appointment-definitions.html#Appointment.basedOn)" : [{ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }], // [The service request this appointment is allocated to assess](terminologies.html#unbound)
 "[participant](appointment-definitions.html#Appointment.participant)" : [{ // **R!** [Participants involved in appointment](terminologies.html#unbound)
 "[type](appointment-definitions.html#Appointment.participant.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Role of participant in the appointment](valueset-encounter-participant-type.html)
 "[actor](appointment-definitions.html#Appointment.participant.actor)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|[Location](location.html#Location)) }, // [Person, Location/HealthcareService or Device](terminologies.html#unbound)
 "[required](appointment-definitions.html#Appointment.participant.required)" : "<[code](datatypes.html#code)>", // [required | optional | information-only](valueset-participantrequired.html)
 "[status](appointment-definitions.html#Appointment.participant.status)" : "<[code](datatypes.html#code)>", // **R!** [accepted | declined | tentative | needs-action](valueset-participationstatus.html)
 "[period](appointment-definitions.html#Appointment.participant.period)" : { [Period](datatypes.html#Period) } // [Participation period of the actor](terminologies.html#unbound)
 }],
 "[requestedPeriod](appointment-definitions.html#Appointment.requestedPeriod)" : [{ [Period](datatypes.html#Period) }] // [Potential date/time interval(s) requested to allocate the appointment within](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Appointment**](appointment-definitions.html#Appointment);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Appointment.identifier](appointment-definitions.html#Appointment.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this item
 fhir:[Appointment.status](appointment-definitions.html#Appointment.status) [ [code](datatypes.html#code) ]; # 1..1 proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist
 fhir:[Appointment.cancelationReason](appointment-definitions.html#Appointment.cancelationReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The coded reason for the appointment being cancelled
 fhir:[Appointment.serviceCategory](appointment-definitions.html#Appointment.serviceCategory) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* A broad categorization of the service that is to be performed during this appointment
 fhir:[Appointment.serviceType](appointment-definitions.html#Appointment.serviceType) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* The specific service that is to be performed during this appointment
 fhir:[Appointment.specialty](appointment-definitions.html#Appointment.specialty) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* The specialty of a practitioner that would be required to perform the service requested in this appointment
 fhir:[Appointment.appointmentType](appointment-definitions.html#Appointment.appointmentType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The style of appointment or patient that has been booked in the slot (not service type)
 fhir:[Appointment.reasonCode](appointment-definitions.html#Appointment.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Coded reason this appointment is scheduled
 fhir:[Appointment.reasonReference](appointment-definitions.html#Appointment.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Procedure](procedure.html#Procedure)|[Observation](observation.html#Observation)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) ], ... ; # 0..* Reason the appointment is to take place (resource)
 fhir:[Appointment.priority](appointment-definitions.html#Appointment.priority) [ [unsignedInt](datatypes.html#unsignedInt) ]; # 0..1 Used to make informed decisions if needing to re-prioritize
 fhir:[Appointment.description](appointment-definitions.html#Appointment.description) [ [string](datatypes.html#string) ]; # 0..1 Shown on a subject line in a meeting request, or appointment list
 fhir:[Appointment.supportingInformation](appointment-definitions.html#Appointment.supportingInformation) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Additional information to support the appointment
 fhir:[Appointment.start](appointment-definitions.html#Appointment.start) [ [instant](datatypes.html#instant) ]; # 0..1 When appointment is to take place
 fhir:[Appointment.end](appointment-definitions.html#Appointment.end) [ [instant](datatypes.html#instant) ]; # 0..1 When appointment is to conclude
 fhir:[Appointment.minutesDuration](appointment-definitions.html#Appointment.minutesDuration) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Can be less than start/end (e.g. estimate)
 fhir:[Appointment.slot](appointment-definitions.html#Appointment.slot) [ [Reference](references.html#Reference)([Slot](slot.html#Slot)) ], ... ; # 0..* The slots that this appointment is filling
 fhir:[Appointment.created](appointment-definitions.html#Appointment.created) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 The date that this appointment was initially created
 fhir:[Appointment.comment](appointment-definitions.html#Appointment.comment) [ [string](datatypes.html#string) ]; # 0..1 Additional comments
 fhir:[Appointment.patientInstruction](appointment-definitions.html#Appointment.patientInstruction) [ [string](datatypes.html#string) ]; # 0..1 Detailed information and instructions for the patient
 fhir:[Appointment.basedOn](appointment-definitions.html#Appointment.basedOn) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ], ... ; # 0..* The service request this appointment is allocated to assess
 fhir:[Appointment.participant](appointment-definitions.html#Appointment.participant) [ # 1..* Participants involved in appointment
 fhir:[Appointment.participant.type](appointment-definitions.html#Appointment.participant.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Role of participant in the appointment
 fhir:[Appointment.participant.actor](appointment-definitions.html#Appointment.participant.actor) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)|[HealthcareService](healthcareservice.html#HealthcareService)|
 [Location](location.html#Location)) ]; # 0..1 Person, Location/HealthcareService or Device
 fhir:[Appointment.participant.required](appointment-definitions.html#Appointment.participant.required) [ [code](datatypes.html#code) ]; # 0..1 required | optional | information-only
 fhir:[Appointment.participant.status](appointment-definitions.html#Appointment.participant.status) [ [code](datatypes.html#code) ]; # 1..1 accepted | declined | tentative | needs-action
 fhir:[Appointment.participant.period](appointment-definitions.html#Appointment.participant.period) [ [Period](datatypes.html#Period) ]; # 0..1 Participation period of the actor
 ], ...;
 fhir:[Appointment.requestedPeriod](appointment-definitions.html#Appointment.requestedPeriod) [ [Period](datatypes.html#Period) ], ... ; # 0..* Potential date/time interval(s) requested to allocate the appointment within
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Appointment](appointment.html#Appointment)
 | 
 | 
 |

 | 
 Appointment.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/appointmentstatus to http://hl7.org/fhir/ValueSet/appointmentstatus|4.0.1

 

 | 
 |

 | 
 Appointment.cancelationReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.serviceCategory | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Appointment.reasonCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.reasonReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.patientInstruction | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.basedOn | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.participant.actor | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Appointment.participant.required | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/participantrequired to http://hl7.org/fhir/ValueSet/participantrequired|4.0.1

 

 | 
 |

 | 
 Appointment.participant.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/participationstatus to http://hl7.org/fhir/ValueSet/participationstatus|4.0.1

 

 | 
 |

 | 
 Appointment.participant.period | 
 
 

 - Added Element

 

 | 
 |

 | 
 Appointment.reason | 
 
 

 - deleted

 

 | 
 |

 | 
 Appointment.indication | 
 
 

 - deleted

 

 | 
 |

 | 
 Appointment.incomingReferral | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](appointment.diff.xml) or [JSON](appointment.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](appointment-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](appointment-profiles.html) and the alternate definitions:
Master Definition [XML](appointment.profile.xml.html) + [JSON](appointment.profile.json.html),
[XML](xml.html) [Schema](appointment.xsd)/[Schematron](appointment.sch) + [JSON](json.html) 
[Schema](appointment.schema.json.html), [ShEx](appointment.shex.html) (for [Turtle](rdf.html)) + [see the extensions](appointment-profiles.html) & the [dependency analysis](appointment-dependencies.html)

### 12.10.3.1 
Terminology Bindings
 [
](appointment.html#tx)

 | Path | Definition | Type | Reference | |

 | Appointment.status | The free/busy status of an appointment. | [Required](terminologies.html#required) | [AppointmentStatus](valueset-appointmentstatus.html) | |

 | Appointment.cancelationReason | | [Example](terminologies.html#example) | [AppointmentCancellationReason](valueset-appointment-cancellation-reason.html) | |

 | Appointment.serviceCategory | | [Example](terminologies.html#example) | [ServiceCategory](valueset-service-category.html) | |

 | Appointment.serviceType | | [Example](terminologies.html#example) | [ServiceType](valueset-service-type.html) | |

 | Appointment.specialty | | [Preferred](terminologies.html#preferred) | [PracticeSettingCodeValueSet](valueset-c80-practice-codes.html) | |

 | Appointment.appointmentType | | [Preferred](terminologies.html#preferred) | [v2.0276](v2/0276/index.html) | |

 | Appointment.reasonCode | The Reason for the appointment to take place. | [Preferred](terminologies.html#preferred) | [EncounterReasonCodes](valueset-encounter-reason.html) | |

 | Appointment.participant.type | Role of participant in encounter. | [Extensible](terminologies.html#extensible) | [ParticipantType](valueset-encounter-participant-type.html) | |

 | Appointment.participant.required | Is the Participant required to attend the appointment. | [Required](terminologies.html#required) | [ParticipantRequired](valueset-participantrequired.html) | |

 | Appointment.participant.status | The Participation status of an appointment. | [Required](terminologies.html#required) | [ParticipationStatus](valueset-participationstatus.html) | |

 

 

### 12.10.3.2 Constraints [
](appointment.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **app-1** | [Rule](conformance-rules.html#rule) | Appointment.participant | Either the type or actor on the participant SHALL be specified | type.exists() or actor.exists() | |
| **app-2** | [Rule](conformance-rules.html#rule) | (base) | Either start and end are specified, or neither | start.exists() = end.exists() | |
| **app-3** | [Rule](conformance-rules.html#rule) | (base) | Only proposed or cancelled appointments can be missing start/end dates | (start.exists() and end.exists()) or (status in ('proposed' | 'cancelled' | 'waitlist')) | |
| **app-4** | [Rule](conformance-rules.html#rule) | (base) | Cancelation reason is only used for appointments that have been cancelled, or no-show | Appointment.cancelationReason.exists() implies (Appointment.status='no-show' or Appointment.status='cancelled') | |

 
## 12.10.4 Typical Status Transition Examples: [](appointment.html#typical)

 
### 12.10.4.1 Typical flow of statuses for an appointment: [](appointment.html#status-flow)

 

 | 
 Activity Description | 
 Slot | 
 Appointment | 
 Appointment Response | 
 Encounter | 
 |

 | 
 
 The schedule is created/published **(Role: Scheduler)
 | 
 
 freeBusyType = FREE | 
 
 | 
 
 | 
 
 | 
 
 |

 | 
 
 An appointment request is created after locating an available slot 
(Role: Requester)
 | 
 
 | 
 
 
 status = pending

 participant.status = needs-action
 | 
 
 | 
 
 | 
 
 |

 | 
 
 The appointment request is processed and the slot status updated
(Role: Scheduler)
 | 
 
 freeBusyType = BUSY-TENTATIVE | 
 
 | 
 
 | 
 
 | 
 
 |

 | 
 
 The appointment is accepted as described – by all participants 
(Role: Participant(s))
 | 
 
 | 
 
 | 
 
 participantStatus = accepted | 
 
 | 
 
 |

 | 
 
 The appointment is confirmed as accepted by all participants
(Role: Scheduler)
 | 
 
 freeBusyType = BUSY | 
 
 
 status = booked
participant.status = accepted
 | 
 
 | 
 
 | 
 
 |

 | 
 
 
 Optional: Preparation for the appointment begins – could be preparing a room for the appointment, etc.
(Role: Participants/Admin)
 *
 | 
 
 | 
 
 | 
 
 | 
 
 
 status = planned (optional)

 location.status = planned
 | 
 
 |

 | 
 
 The patient arrives for the appointment, often sitting in a waiting room
(Role: Admin)
 | 
 
 | 
 
 status = arrived | 
 
 | 
 
 
 status = arrived

 location.status = present
 | 
 
 |

 | 
 
 The practitioner and the patient meet and the provision of the service begins
(Role: Scheduler/Participant(s)/Admin)
 | 
 
 | 
 
 status = fulfilled | 
 
 | 
 
 status = in-progress | 
 
 |

 | 
 
 The encounter concludes
(Role: Scheduler/Participant(s)/Admin)
 | 
 
 | 
 
 | 
 
 | 
 
 status = finished | 
 
 |

 

 
### 12.10.4.2 Flow for the rejection/cancellation of an appointment [](appointment.html#reject-flow)

 

 | 
 Activity Description | 
 Slot | 
 Appointment | 
 Appointment Response | 
 |

 | 
 
 The schedule is created/published 
(Role: Scheduler)
 | 
 
 freeBusyType = FREE | 
 
 | 
 
 | 
 
 |

 | 
 
 An appointment request is created
(Role: Requester)
 | 
 
 | 
 
 
 status = pending

 participant.status = needs-action
 | 
 
 | 
 
 |

 | 
 
 The appointment request is processed and the slot status updated
(Role: Scheduler)
 | 
 
 freeBusyType = BUSY-TENTATIVE | 
 
 | 
 
 | 
 
 |

 | 
 
 Participant declines the Appointment
(Role: Participant)
 | 
 
 | 
 
 | 
 
 participantStatus = declined | 
 
 |

 | 
 
 The appointment is cancelled
(Role: Scheduler)
 | 
 
 freeBusyType = FREE | 
 
 
 status = cancelled

 participant.status = declined
 | 
 
 | 
 
 |

 

 
### 12.10.4.3 Flow for re-negotiation: [](appointment.html#negotiate-flow)

 

 | 
 Activity Description | 
 Slot | 
 Appointment | 
 Appointment Response | 
 |

 | 
 
 The schedule is created/published 
(Role: Scheduler)
 | 
 freeBusyType = FREE | 
 | 
 | 
 |

 | 
 
 An appointment is requested (e.g. with Brian and Peter)
(Role: Requester)
 | 
 | 
 
 status = proposed

 participant(Brian).status = needs-action

 participant(Peter).status = needs-action
 | 
 | 
 |

 | 
 
 The schedule is updated to inform others of interest in the slot
(Role: Scheduler)
 | 
 freeBusyType = BUSY-TENTATIVE | 
 | 
 | 
 |

 | 
 
 Brian accepts the appointment
(Role: Participant-Brian)
 | 
 | 
 | 
 (Brian).participantStatus = accepted | 
 |

 | 
 
 Appointment is updated with Brian's status
(Role: Scheduler)
 | 
 | 
 
 status = pending

 participant(Brian).status = accepted
 | 
 | 
 |

 | 
 
 Peter suggests a new time
(Role: Participant-Peter)
 | 
 | 
 | 
 (Peter).participantStatus = tentative
*(with new time)* | 
 |

 | 
 
 Appointment is updated with new time, and indicates that action is needed by both participants
(Role: Scheduler)
 | 
 | 
 
 *(new time details updated)*

 participant(Brian).status = needs-action

 participant(Peter).status = needs-action
 | 
 | 
 |

 | 
 
 Brian accepts the appointment
(Role: Participant-Brian)
 | 
 | 
 | 
 (Brian).participantStatus = accepted | 
 |

 | 
 
 Appointment updated
(Role: Scheduler)
 | 
 | 
 participant(Brian).status = accepted | 
 | 
 |

 | 
 
 
(Role: Participant-Peter)
 | 
 | 
 | 
 (Peter).participantStatus = accepted | 
 |

 | 
 
 Appointment updated
(Role: Scheduler)
 | 
 freeBusyType = BUSY | 
 
 status = booked

 participant(Peter).status = accepted
 | 
 | 
 |

 

 

 
### 12.10.4.4 Flow for a patient no-show: [](appointment.html#noshow-flow)

 

 | 
 Activity Description | 
 Slot | 
 Appointment | 
 Appointment Response | 
 Encounter | 
 |

 | 
 
 *(from typical status flow)*
 | 
 
 freeBusyType = BUSY | 
 
 
 status = booked

 participant.status = accepted
 | 
 
 | 
 
 | 
 
 |

 | 
 
 Appointment is updated as a noshow
(Role: Scheduler/Admin)
 | 
 
 | 
 
 status = noshow | 
 
 | 
 
 *(no encounter created)* | 
 
 |

 
 
 
 

 
### 12.10.4.5 Flow for a patient waitlist: [](appointment.html#waitlist-flow)

 

 | 
 Activity Description | 
 Appointment (inconvenient) | 
 Appointment (preferred) | 
 |

 | 
 An appointment is booked for an inconvenient time using a typical status flow | 
 
 
 status = booked

 participant.status = accepted
 | 
 
 | 
 
 |

 | 
 Waitlist appointment created | 
 
 
 status = booked

 participant.status = accepted
 | 
 
 
 status = waitlist

 requestedPeriod = *(more convenient time period)*
 | 
 
 |

 | 
 Patient notified of availability of a better slot | 
 
 
 status = booked
 | 
 
 
 status = proposed

 participant.status = needs-action
 | 
 
 |

 | 
 Patient accepts better slot | 
 
 
 status = cancelled
 | 
 
 
 status = booked

 participant.status = accepted
 | 
 
 |

 

 
 

 
## 12.10.5 Notes: [](appointment.html#notes)

 

 - Placer/Filler ([HL7 v2 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185))

 The appointment information is effectively the same between the filler and placer, and given the nature of the
 FHIR resource, there is only a single resource for both purposes. The placer is the actor that performs the
 PUT or POST operation on the resource, and the filler is the actor that receives these resource messages and
 processes the information and makes a decision if the appointment can be used.
 

 - Terminology - ServiceCategory, ServiceType and Specialty

 The 3 core clinical terminologies associated with the appointment may have relationships with each other
 through the terminology server, but not these might not be visible in the actual appointment resource or profile.
 

 - Interaction with other Standards

 The strong desire is that implementers of this resource should consider providing this resource
 in the iCalendar format as an alternative representation. Many 3rd party applications and component providers
 have parsers and user interface controls to display this information.
 This may lower the entry point to integrate outside the health-care specific applications, and into the
 consumer space. This would permit the easier creation of a mobile application that creates appointments
 in the devices native calendar.

 The iCalendar specification can be found at [http://www.ietf.org/rfc/rfc2445.txt ](http://www.ietf.org/rfc/rfc2445.txt).
 

 

 

> Trial-Use Note:**
Implementer feedback is sought on the values for Appointment.priority and how interoperable they are.
Using an extension to record a CodeableConcept for named values may be tested at a future Connectathon.**
Implementer feedback is also sought to clarify desired relationship linkages between ServiceCategory, 
ServiceType and Specialty, along with how they have approached the definition.

Feedback [here ](http://hl7.org/fhir-issues).

## 12.10.6 Search Parameters [
](appointment.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| Name** | **Type** | **Description** | **Expression** | **In Common** | |

| actor | [reference](search.html#reference) | Any one of the individuals participating in the appointment | Appointment.participant.actor
([Practitioner](practitioner.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html), [Location](location.html)) | | |

| appointment-type | [token](search.html#token) | The style of appointment or patient that has been booked in the slot (not service type) | Appointment.appointmentType | | |

| based-on | [reference](search.html#reference) | The service request this appointment is allocated to assess | Appointment.basedOn
([ServiceRequest](servicerequest.html)) | | |

| date | [date](search.html#date) | Appointment date/time. | Appointment.start | | |

| identifier | [token](search.html#token) | An Identifier of the Appointment | Appointment.identifier | | |

| location | [reference](search.html#reference) | This location is listed in the participants of the appointment | Appointment.participant.actor.where(resolve() is Location)
([Location](location.html)) | | |

| part-status | [token](search.html#token) | The Participation status of the subject, or other participant on the appointment. Can be used to locate participants that have not responded to meeting requests. | Appointment.participant.status | | |

| patient | [reference](search.html#reference) | One of the individuals of the appointment is this patient | Appointment.participant.actor.where(resolve() is Patient)
([Patient](patient.html)) | | |

| practitioner | [reference](search.html#reference) | One of the individuals of the appointment is this practitioner | Appointment.participant.actor.where(resolve() is Practitioner)
([Practitioner](practitioner.html)) | | |

| reason-code | [token](search.html#token) | Coded reason this appointment is scheduled | Appointment.reasonCode | | |

| reason-reference | [reference](search.html#reference) | Reason the appointment is to take place (resource) | Appointment.reasonReference
([Condition](condition.html), [Observation](observation.html), [Procedure](procedure.html), [ImmunizationRecommendation](immunizationrecommendation.html)) | | |

| service-category | [token](search.html#token) | A broad categorization of the service that is to be performed during this appointment | Appointment.serviceCategory | | |

| service-type | [token](search.html#token) | The specific service that is to be performed during this appointment | Appointment.serviceType | | |

| slot | [reference](search.html#reference) | The slots that this appointment is filling | Appointment.slot
([Slot](slot.html)) | | |

| specialty | [token](search.html#token) | The specialty of a practitioner that would be required to perform the service requested in this appointment | Appointment.specialty | | |

| status | [token](search.html#token) | The overall status of the appointment | Appointment.status | | |

| supporting-info | [reference](search.html#reference) | Additional information to support the appointment | Appointment.supportingInformation
(Any) | | |