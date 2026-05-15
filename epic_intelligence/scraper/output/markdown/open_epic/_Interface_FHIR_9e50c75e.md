# open.epic :: Explore By Interface Type

> Source: https://open.epic.com/Interface/FHIR

---

# 
 By Interface Type

 

 

 
 

 

 
 

 
 

 
 
 

## FHIR

 
FHIR, or Fast Healthcare Interoperability Resources, provides a lightweight REST-based access layer for standard HL7-defined data models. If you're looking for more than specs, check out [FHIR development sandbox](https://fhir.epic.com) for how you can get client IDs and testing support. 

### 
 $submit-attachment (Prior Auth) (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11276)

 

 

 

This web service is used by providers to submit additional information to facilitate the payer's prior authorization review process.

The current types of additional information that are supported include QuestionnaireResponse Bundles and DocumentReference in the form of PDFs.

This is generally used in conjunction with [Claim.$submit (Prior Auth) (R4)](https://fhir.epic.com/specifications?api=11274) as a way to add details to a specific submission.

This incoming web service enables submission of additional information to the payer's UM system using FHIR. Refer to [Operation Definition of $submit-attachment v2.1.0](https://www.hl7.org/fhir/us/davinci-cdex/STU2.1/OperationDefinition-submit-attachment.html) and CDex Parameters Submit Attachment Profile v2.1.0 for more information.
 

 

 

### 
 Account

 

 

 

The Account resource acts as a central record against which charges, payments, and adjustments are applied. It contains information about which parties are responsible for payment of the account.

Technical Specifications:

- [Account.Read (Premium Billing) (R4)](https://fhir.epic.com//Sandbox?api=10505)
- [Account.Search (Premium Billing) (R4)](https://fhir.epic.com//Sandbox?api=10508)

 

 

### 
 AdverseEvent

 

 

 

The AdverseEvent resource returns data about an event that caused unintended physical injury resulting from or contributed to by medical care, a research study, or other healthcare setting factors. These events might require additional monitoring, treatment, or hospitalization, or might result in the death of a patient.

Technical Specifications:

- [AdverseEvent.Read (R4)](https://fhir.epic.com//Sandbox?api=981)
- [AdverseEvent.Search (R4)](https://fhir.epic.com//Sandbox?api=982)

 

 

### 
 AGL ScanViewing Action
 [read the spec](https://fhir.epic.com//Sandbox?api=10592)

 

 

 

 

 

### 
 AGL ScanViewing Closing

 [read the spec](https://fhir.epic.com//Sandbox?api=10593)

 

 

 

 

 

### 
 AGL ScanViewing DocumentDisplay

 [read the spec](https://fhir.epic.com//Sandbox?api=10591)

 

 

 

 

 

### 
 AGL ScanViewing Handshake

 [read the spec](https://fhir.epic.com//Sandbox?api=10590)

 

 

 

 

 

### 
 AGL TelephoneAlert
 [read the spec](https://fhir.epic.com//Sandbox?api=11125)

 

 

 

 

 

### 
 AllergyIntolerance

 

 

 

The AllergyIntolerance data models describe a patient's intolerance to a foreign substance and an associated reaction that occurs from exposure.

Technical Specifications:

- [AllergyIntolerance.Read (DSTU2)](https://fhir.epic.com//Sandbox?api=1)
- [AllergyIntolerance.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=2)
- [AllergyIntolerance.Create (STU3)](https://fhir.epic.com//Sandbox?api=463)
- [AllergyIntolerance.Read (STU3)](https://fhir.epic.com//Sandbox?api=464)
- [AllergyIntolerance.Search (STU3)](https://fhir.epic.com//Sandbox?api=465)
- [AllergyIntolerance.Create (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=945)
- [AllergyIntolerance.Read (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=946)
- [AllergyIntolerance.Search (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=947)
- [AllergyIntolerance.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11363)
- [AllergyIntolerance.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11365)

 

 

### 
 Appointment, Schedule, Slot

 

 

 

Appointment describes a patient's scheduled visit with a health care provider. The slot resource provides time-slots that can be booked using an appointment. They do not provide any information about appointments that are available, just the time, and optionally what the time can be used for. The Schedule resource is the link from a slot to a practitioner and location for an appointment.

Technical Specifications:

- [Appointment.Read (Appointments) (STU3)](https://fhir.epic.com//Sandbox?api=466)
- [Schedule.Read (STU3)](https://fhir.epic.com//Sandbox?api=500)
- [Appointment.$book (STU3)](https://fhir.epic.com//Sandbox?api=839)
- [Appointment.$find (STU3)](https://fhir.epic.com//Sandbox?api=840)
- [Slot.Read (STU3)](https://fhir.epic.com//Sandbox?api=862)
- [Appointment.Search (Appointments) (STU3)](https://fhir.epic.com//Sandbox?api=10189)
- [Appointment.Read (Appointments) (R4)](https://fhir.epic.com//Sandbox?api=10468)
- [Appointment.Search (Appointments) (R4)](https://fhir.epic.com//Sandbox?api=10469)
- [Appointment.Read (Scheduled Surgeries) (R4)](https://fhir.epic.com//Sandbox?api=10471)
- [Appointment.Search (Scheduled Surgeries) (R4)](https://fhir.epic.com//Sandbox?api=10478)
- [Appointment.Read (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11269)
- [Appointment.Search (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11270)

 

 

### 
 Authentication and Single Sign-On (SSO)

 

 

 Epic recommends and supports the HL7 SMART on FHIR profile of OAuth 2.0, including the EHR launch and standalone launch for both patients and providers, as well as backend services. Epic also supports basic authentication. 

[See Tutorial](../Tutorial/OAuth)
 

 

### 
 Binary

 

 

 

Binary provides the ability to retreive a particular document.

Technical Specifications:

- [Binary.Read (Generated CCDA) (DSTU2)](https://fhir.epic.com//Sandbox?api=3)
- [Binary.Read (Clinical Notes) (STU3)](https://fhir.epic.com//Sandbox?api=841)
- [Binary.Read (Provider Photo) (R4)](https://fhir.epic.com//Sandbox?api=983)
- [Binary.Read (Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=1044)
- [Binary.Read (Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10013)
- [Binary.Read (OASIS) (R4)](https://fhir.epic.com//Sandbox?api=10136)
- [Binary.Read (HIS) (R4)](https://fhir.epic.com//Sandbox?api=10137)
- [Binary.Read (Handoff) (R4)](https://fhir.epic.com//Sandbox?api=10138)
- [Binary.Read (Labs) (R4)](https://fhir.epic.com//Sandbox?api=10139)
- [Binary.Read (External CCDA) (R4)](https://fhir.epic.com//Sandbox?api=10183)
- [Binary.Read (Radiology Results) (R4)](https://fhir.epic.com//Sandbox?api=10230)
- [Binary.Read (Correspondences) (R4)](https://fhir.epic.com//Sandbox?api=10231)
- [Binary.Read (Radiology Results) (STU3)](https://fhir.epic.com//Sandbox?api=10232)
- [Binary.Read (Correspondences) (STU3)](https://fhir.epic.com//Sandbox?api=10233)
- [Binary.Read (IRF-PAI) (R4)](https://fhir.epic.com//Sandbox?api=10285)
- [Binary.Read (Minimum Data Set) (R4)](https://fhir.epic.com//Sandbox?api=10290)
- [Binary.Read (Clinical References) (R4)](https://fhir.epic.com//Sandbox?api=10308)
- [Binary.Read (Patient-Entered Questionnaires) (STU3)](https://fhir.epic.com//Sandbox?api=10437)
- [Binary.Read (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10438)
- [Binary.Read (Generated CDAs) (R4)](https://fhir.epic.com//Sandbox?api=10501)
- [Binary.Search (Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=10533)
- [Binary.Search (Handoff) (R4)](https://fhir.epic.com//Sandbox?api=10550)
- [Binary.Search (Clinical References) (R4)](https://fhir.epic.com//Sandbox?api=10551)
- [Binary.Search (HIS) (R4)](https://fhir.epic.com//Sandbox?api=10552)
- [Binary.Search (IRF-PAI) (R4)](https://fhir.epic.com//Sandbox?api=10553)
- [Binary.Search (Labs) (R4)](https://fhir.epic.com//Sandbox?api=10554)
- [Binary.Search (Provider Photo) (R4)](https://fhir.epic.com//Sandbox?api=10555)
- [Binary.Search (Correspondences) (R4)](https://fhir.epic.com//Sandbox?api=10556)
- [Binary.Search (Generated CDAs) (R4)](https://fhir.epic.com//Sandbox?api=10557)
- [Binary.Search (External CCDA) (R4)](https://fhir.epic.com//Sandbox?api=10558)
- [Binary.Search (Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10559)
- [Binary.Search (Minimum Data Set) (R4)](https://fhir.epic.com//Sandbox?api=10560)
- [Binary.Search (OASIS) (R4)](https://fhir.epic.com//Sandbox?api=10561)
- [Binary.Search (Radiology Results) (R4)](https://fhir.epic.com//Sandbox?api=10562)
- [Binary.Search (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10563)
- [Binary.Read (Practitioner Photo) (STU3)](https://fhir.epic.com//Sandbox?api=10570)
- [Binary.Read (Outside Record - Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=10996)
- [Binary.Search (Outside Record - Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=10997)
- [Binary.Read (Study) (R4)](https://fhir.epic.com//Sandbox?api=11002)
- [Binary.Read (Prior Auth Supporting Info) (R4)](https://fhir.epic.com//Sandbox?api=11398)

 

 

### 
 BodyStructure

 

 

 

BodyStructure describes anatomical details about a specimen or body part, including patient information, descriptions, and images. For example, this resource can return tooth information from the patient record.

Technical Specifications:

- [BodyStructure.Read (Tooth) (R4)](https://fhir.epic.com//Sandbox?api=10068)
- [BodyStructure.Search (Tooth) (R4)](https://fhir.epic.com//Sandbox?api=10069)
- [BodyStructure.Read (Organ) (R4)](https://fhir.epic.com//Sandbox?api=10280)
- [BodyStructure.Search (Organ) (R4)](https://fhir.epic.com//Sandbox?api=10281)
- [Bodystructure.Create (Radiotherapy Volume) (R4)](https://fhir.epic.com//Sandbox?api=11040)
- [Bodystructure.Read (Radiotherapy Volume) (R4)](https://fhir.epic.com//Sandbox?api=11041)
- [Bodystructure.Search (Radiotherapy Volume) (R4)](https://fhir.epic.com//Sandbox?api=11042)
- [Bodystructure.Update (Radiotherapy Volume) (R4)](https://fhir.epic.com//Sandbox?api=11043)

 

 

### 
 Bulk Data Access

 

 

 

FHIR Bulk Data Access, also known as Flat FHIR, is a framework for efficiently accessing large volumes of information about a group of individuals. For more information, refer to the [HL7 specification](https://hl7.org/fhir/uv/bulkdata/), or Epic's [FHIR Bulk Data Access Tutorial](https://fhir.epic.com/Documentation?docId=fhir_bulk_data).

Technical Specifications:

- [Bulk Data Kick-off](https://fhir.epic.com//Sandbox?api=10169)
- [Bulk Data Status Request](https://fhir.epic.com//Sandbox?api=10170)
- [Bulk Data File Request](https://fhir.epic.com//Sandbox?api=10171)
- [Bulk Data Delete Request](https://fhir.epic.com//Sandbox?api=10172)

 

 

### 
 CarePlan, Goal

 

 

 

Careplan describes the assessment and treatment plan for a particular patient. Goal describes provider-documented targeted outcomes for a patient to achieve.

Technical Specifications:

- [CarePlan.Read (Encounter-Level) (DSTU2)](https://fhir.epic.com//Sandbox?api=4)
- [CarePlan.Search (Encounter-Level) (DSTU2)](https://fhir.epic.com//Sandbox?api=5)
- [Goal.Read (Patient) (DSTU2)](https://fhir.epic.com//Sandbox?api=19)
- [Goal.Search (Patient) (DSTU2)](https://fhir.epic.com//Sandbox?api=20)
- [Goal.Read (Patient) (STU3)](https://fhir.epic.com//Sandbox?api=877)
- [Goal.Create (Patient) (STU3)](https://fhir.epic.com//Sandbox?api=878)
- [Goal.Search (Patient) (STU3)](https://fhir.epic.com//Sandbox?api=924)
- [Goal.Read (Patient) (R4)](https://fhir.epic.com//Sandbox?api=959)
- [Goal.Search (Patient) (R4)](https://fhir.epic.com//Sandbox?api=960)
- [CarePlan.Read (Longitudinal) (R4)](https://fhir.epic.com//Sandbox?api=1064)
- [CarePlan.Search (Longitudinal) (R4)](https://fhir.epic.com//Sandbox?api=1065)
- [CarePlan.Read (Encounter) (R4)](https://fhir.epic.com//Sandbox?api=1066)
- [CarePlan.Search (Encounter) (R4)](https://fhir.epic.com//Sandbox?api=1067)
- [CarePlan.Read (Dental) (R4)](https://fhir.epic.com//Sandbox?api=10016)
- [CarePlan.Search (Dental) (R4)](https://fhir.epic.com//Sandbox?api=10017)
- [CarePlan.Read (Questionnaires Due) (R4)](https://fhir.epic.com//Sandbox?api=10022)
- [CarePlan.Search (Questionnaires Due) (R4)](https://fhir.epic.com//Sandbox?api=10028)
- [CarePlan.Read (Inpatient) (R4)](https://fhir.epic.com//Sandbox?api=10043)
- [CarePlan.Search (Inpatient) (R4)](https://fhir.epic.com//Sandbox?api=10044)
- [CarePlan.Read (Outpatient) (R4)](https://fhir.epic.com//Sandbox?api=10045)
- [CarePlan.Search (Outpatient) (R4)](https://fhir.epic.com//Sandbox?api=10046)
- [Goal.Read (Care Plan Goal) (R4)](https://fhir.epic.com//Sandbox?api=10052)
- [Goal.Search (Care Plan Goal) (R4)](https://fhir.epic.com//Sandbox?api=10053)
- [CarePlan.Read (Oncology) (R4)](https://fhir.epic.com//Sandbox?api=10073)
- [CarePlan.Search (Oncology) (R4)](https://fhir.epic.com//Sandbox?api=10074)
- [Goal.Read (Pathway Step) (R4)](https://fhir.epic.com//Sandbox?api=10099)
- [Goal.Search (Pathway Step) (R4)](https://fhir.epic.com//Sandbox?api=10100)
- [CarePlan.Read (Inpatient Pathway) (R4)](https://fhir.epic.com//Sandbox?api=10101)
- [CarePlan.Search (Inpatient Pathway) (R4)](https://fhir.epic.com//Sandbox?api=10102)
- [CarePlan.Read (Care Path) (R4)](https://fhir.epic.com//Sandbox?api=10305)
- [CarePlan.Search (Care Path) (R4)](https://fhir.epic.com//Sandbox?api=10309)
- [Goal.Read (Care Path) (R4)](https://fhir.epic.com//Sandbox?api=10311)
- [Goal.Search (Care Path) (R4)](https://fhir.epic.com//Sandbox?api=10312)
- [CarePlan.Read (Patient Education) (R4)](https://fhir.epic.com//Sandbox?api=10321)
- [CarePlan.Search (Patient Education) (R4)](https://fhir.epic.com//Sandbox?api=10322)
- [Goal.Search (Care Plan) (STU3)](https://fhir.epic.com//Sandbox?api=10458)
- [Goal.Read (Care Plan) (STU3)](https://fhir.epic.com//Sandbox?api=10459)
- [CarePlan.Read (Longitudinal) (DSTU2)](https://fhir.epic.com//Sandbox?api=10572)
- [CarePlan.Search (Longitudinal) (DSTU2)](https://fhir.epic.com//Sandbox?api=10573)
- [Goal.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11411)
- [Goal.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11413)
- [CarePlan.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11457)
- [CarePlan.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11458)

 

 

### 
 CareTeam

 

 

 

The CareTeam resource returns information about a patient’s care team and care team members. The care team includes longitudinal care team assignments as well as providers who have had recent visits with the patient. The patient's inpatient treatment team is not included in this resource. Inpatient treatment team members are instead included as participants in the relevant Encounter resource.

Technical Specifications:

- [CareTeam.Read (Longitudinal CareTeam) (R4)](https://fhir.epic.com//Sandbox?api=1068)
- [CareTeam.Search (Longitudinal CareTeam) (R4)](https://fhir.epic.com//Sandbox?api=1069)
- [CareTeam.Read (Episode) (R4)](https://fhir.epic.com//Sandbox?api=10154)
- [CareTeam.Search (Episode) (R4)](https://fhir.epic.com//Sandbox?api=10155)
- [CareTeam.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11367)
- [CareTeam.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11369)

 

 

### 
 CDS Hooks
 [read the spec](/Tech/TechSpec?spec=5413)

 

 

 CDS Hooks is an HL7 standard for in-workflow, real-time, provider-facing decision support integration between Electronic Health Record systems and external Decision Support Services. A summary understanding of the specification is necessary for the discussion of state of Epic support for CDS Hooks, so check out the [HL7 published specification](https://cds-hooks.hl7.org/) and [current draft specification](https://cds-hooks.org/). Epic recommends against using this feature for other purposes; if you need only a notification, we instead recommend using an event based interface. 
 

 

### 
 Claim.$inquire (Prior Auth) (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11275)

 

 

 

This web service enables providers to inquire about the status of existing prior authorization requests in the utilization management system using FHIR technology. It is an alternative to the traditional ANSI X12 278 transaction, which is the EDI standard historically used by payers and providers to exchange prior authorization requests and inquiries electronically. 

Providers can use this service to check the current review status, retrieve pended authorization details, or confirm approved/denied outcomes for previously submitted prior authorization requests. This API functions similarly to the incoming 278 inquiry API but, instead, uses the FHIR specification defined in [the Da Vinci Prior Authorization Support implementation guide](https://hl7.org/fhir/us/davinci-pas).

 

 

### 
 Claim.$submit (Prior Auth) (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11274)

 

 

 

This web service enables providers to submit prior authorization requests to the utilization management system using FHIR technology. It is an alternative to an ANSI X12 278 Health Care Services Request For Review message, which is the EDI standard historically used by payers and providers to exchange prior authorization requests electronically. 

Providers can use this service as standalone, following Coverage Requirements Discovery (CRD) when prior authorization is determined necessary, or after Documentation Templates and Rules (DTR) interactions to submit QuestionnaireResponse resources alongside the initial authorization request. This API functions similarly to the incoming 278 request API but, instead, uses the FHIR specification defined in [Da Vinci Prior Authorization Support (PAS) implementation guide v2.1.0 for PAS Claim](https://hl7.org/fhir/us/davinci-pas/STU2.1/StructureDefinition-profile-claim.html).

 

 

### 
 Communication

 

 

 

The Communication resource represents a record of communication. This resource can convey details about messages between health systems and community-based organizations about referral requests made through continued care and services workflows in Epic, such as a post-discharge service request for durable medical equipment (DME) or social services.

Technical Specifications:

- [Communication.Read (Community Resource Communication) (R4)](https://fhir.epic.com//Sandbox?api=10088)
- [Communication.Search (Community Resource Communication) (R4)](https://fhir.epic.com//Sandbox?api=10089)
- [Communication.Create (Community Resource Communication) (R4)](https://fhir.epic.com//Sandbox?api=10090)
- [Communication.Read (Patient Education) (R4)](https://fhir.epic.com//Sandbox?api=10319)
- [Communication.Search (Patient Education) (R4)](https://fhir.epic.com//Sandbox?api=10320)
- [Communication.Read (Customer Relationship Management) (R4)](https://fhir.epic.com//Sandbox?api=10408)

 

 

### 
 Computer-Telephony Integration (Incoming)

 

 

 

Epic integrates with your organization’s phone system to automatically open the appropriate chart or another activity in Epic when calls are received.

 

 

### 
 Computer-Telephony Integration (Outgoing)

 

 

 

Epic integrates with your organization’s phone system so users can place or end a call directly from a patient chart or another activity in Epic, and details about the call are logged. Your phone system can also update Epic with the call identifier after the call.

 

 

### 
 Condition

 

 

 

Conditions can encompass acute and chronic problems and conditions, as well as encounter diagnoses.

Technical Specifications:

- [Condition.Read (Problems) (DSTU2)](https://fhir.epic.com//Sandbox?api=6)
- [Condition.Search (Problems) (DSTU2)](https://fhir.epic.com//Sandbox?api=7)
- [Condition.Create (Problems) (STU3)](https://fhir.epic.com//Sandbox?api=467)
- [Condition.Read (Encounter Diagnosis, Problems) (STU3)](https://fhir.epic.com//Sandbox?api=468)
- [Condition.Search (Encounter Diagnosis, Problems) (STU3)](https://fhir.epic.com//Sandbox?api=469)
- [Condition.Create (Problems) (R4)](https://fhir.epic.com//Sandbox?api=949)
- [Condition.Read (Encounter Diagnosis) (R4)](https://fhir.epic.com//Sandbox?api=950)
- [Condition.Read (Problems) (R4)](https://fhir.epic.com//Sandbox?api=951)
- [Condition.Search (Encounter Diagnosis) (R4)](https://fhir.epic.com//Sandbox?api=952)
- [Condition.Search (Problems) (R4)](https://fhir.epic.com//Sandbox?api=953)
- [Condition.Read (Health Concerns) (R4)](https://fhir.epic.com//Sandbox?api=984)
- [Condition.Search (Health Concerns) (R4)](https://fhir.epic.com//Sandbox?api=985)
- [CDS Hooks Condition.Create (Problems) (R4)](https://fhir.epic.com//Sandbox?api=1057)
- [CDS Hooks Condition.Create (Encounter Diagnosis) (R4)](https://fhir.epic.com//Sandbox?api=1058)
- [CDS Hooks Condition.Create (Encounter Diagnosis, Problems) (STU3)](https://fhir.epic.com//Sandbox?api=1059)
- [Condition.Read (Genomics) (R4)](https://fhir.epic.com//Sandbox?api=1074)
- [Condition.Search (Genomics) (R4)](https://fhir.epic.com//Sandbox?api=1075)
- [Condition.Read (Care Plan Problem) (R4)](https://fhir.epic.com//Sandbox?api=10047)
- [Condition.Search (Care Plan Problem) (R4)](https://fhir.epic.com//Sandbox?api=10048)
- [Condition.Read (Dental Finding) (R4)](https://fhir.epic.com//Sandbox?api=10066)
- [Condition.Search (Dental Finding) (R4)](https://fhir.epic.com//Sandbox?api=10067)
- [Condition.Read (Infection) (R4)](https://fhir.epic.com//Sandbox?api=10140)
- [Condition.Search (Infection) (R4)](https://fhir.epic.com//Sandbox?api=10141)
- [Condition.Read (Reason for Visit) (R4)](https://fhir.epic.com//Sandbox?api=10187)
- [Condition.Search (Reason for Visit) (R4)](https://fhir.epic.com//Sandbox?api=10208)
- [Condition.Read (Medical History) (R4)](https://fhir.epic.com//Sandbox?api=10302)
- [Condition.Search (Medical History) (R4)](https://fhir.epic.com//Sandbox?api=10314)
- [Condition.Read (Outside Record Health Concern) (R4)](https://fhir.epic.com//Sandbox?api=11371)
- [Condition.Read (Outside Record Problems) (R4)](https://fhir.epic.com//Sandbox?api=11374)
- [Condition.Search (Outside Record Health Concern) (R4)](https://fhir.epic.com//Sandbox?api=11376)
- [Condition.Search (Outside Record Problems) (R4)](https://fhir.epic.com//Sandbox?api=11377)
- [Condition.Read (Outside Record Encounter Diagnosis) (R4)](https://fhir.epic.com//Sandbox?api=11387)
- [Condition.Search (Outside Record Encounter Diagnosis) (R4)](https://fhir.epic.com//Sandbox?api=11389)

 

 

### 
 Consent

 

 

 

The FHIR Consent resource defines a concept around collected consent for some action. Consent resources correspond to Documents in Epic. The Consent.Search interaction returns only metadata about the patient consent document(s) on file, such as the type of consent and the effective period. This resource does not return the consent document itself. Typically this resource is used to check whether a consent document is on file for a particular patient. The Consent resource is intended only for provider-facing applications. Patient-facing applications cannot use this resource.

Technical Specifications:

- [Consent.Read (Document) (R4)](https://fhir.epic.com//Sandbox?api=986)
- [Consent.Search (Document) (R4)](https://fhir.epic.com//Sandbox?api=987)
- [Consent.Read (Code Status) (STU3)](https://fhir.epic.com//Sandbox?api=10255)
- [Consent.Search (Code Status) (STU3)](https://fhir.epic.com//Sandbox?api=10256)
- [Consent.Read (Code Status) (R4)](https://fhir.epic.com//Sandbox?api=10258)
- [Consent.Search (Code Status) (R4)](https://fhir.epic.com//Sandbox?api=10259)
- [Consent.Read (Document) (STU3)](https://fhir.epic.com//Sandbox?api=10260)
- [Consent.Search (Document) (STU3)](https://fhir.epic.com//Sandbox?api=10261)

 

 

### 
 Contract

 

 

 

The Contract resource is primarily used for read interactions and can be used as a reference when calling the DocumentReference.Create interaction.

Technical Specifications:

- [Contract.Read (Healthcare Services Reimbursement) (R4)](https://fhir.epic.com//Sandbox?api=10994)
- [Contract.Search (Healthcare Services Reimbursement) (R4)](https://fhir.epic.com//Sandbox?api=10995)

 

 

### 
 Coverage

 

 

 

Coverage resources represent an insurance coverage associated with the patient. A patient might have a long list of possible coverages, some of which are applicable only for specific services. Examples include third party liability, worker's comp, black lung insurance, Medicaid for ESRD, Medicare, commercial, etc.

Technical Specifications:

- [Coverage.Read (Patient Insurance Information) (R4)](https://fhir.epic.com//Sandbox?api=1076)
- [Coverage.Read (Patient Insurance Information) (STU3)](https://fhir.epic.com//Sandbox?api=1077)
- [Coverage.Search (Patient Insurance Information) (R4)](https://fhir.epic.com//Sandbox?api=1078)
- [Coverage.Search (Patient Insurance Information) (STU3)](https://fhir.epic.com//Sandbox?api=1079)
- [Coverage.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11455)
- [Coverage.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11456)

 

 

### 
 Coverage Requirements Discovery (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11288)

 

 

 

This web service is available as part of Epic's utilization management module for clients to integrate with Epic health plans and payers.

This web service is based on the [implementation guide published by the HL7® FHIR® Da Vinci Project for Coverage Requirements Discovery (STU 2.1)](https://hl7.org/fhir/us/davinci-crd/STU2.1/index.html), acting as a payer-side CRD server. The purpose of CRD is to communicate coverage information about a requested service for a covered member, including whether the service is a covered benefit, whether the service requires a prior authorization, and whether additional documentation is needed through the Documentation Templates and Rules web service (DTR).

Epic's CRD payer web service supports responding to requests by two mechanisms: directly by using authorization requirements created inside Epic's utilization management module; and by forwarding the CRD request to another system. This guide describes the requirements and invariants of Epic's implementation of CRD for its utilization management module. Coordinate with each payer you integrate with to understand any additional features or limitations of other CRD systems that might be involved in final responses over this web service. 

At the time of writing, CRD is a constantly evolving specification and is still receiving corrections and enhancements, as is our server implementation, so this content will change over time.

 

 

### 
 Coverage Requirements Discovery Endpoint Discovery (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11279)

 

 

 

This web service is only for use alongside the Coverage Requirements Discovery (CRD) service available with Epic's utilization management module for health plans and payers.

The Coverage Requirements Discovery Endpoint Discovery API allows a client to discover endpoints and prefetch queries to be used for the CRD service with a health plan or payer using Epic's utilization management module.

CRD is based on [the CDS Hooks standard](https://cds-hooks.hl7.org/STU2). Refer to the documentation for that standard for more information about the [CDS Hooks Discovery](https://cds-hooks.hl7.org/STU2#discovery) endpoint this web service implements. For more information about CRD, refer to the [implementation guide published by the HL7® FHIR® Da Vinci Project for Coverage Requirements Discovery (STU 2.1)](https://hl7.org/fhir/us/davinci-crd/STU2.1/index.html).

 

 

### 
 COVID SMART Scheduling Links

 

 

 

Provides an Epic implementation of the [SMART Scheduling Links standard](https://github.com/smart-on-fhir/smart-scheduling-links), a lightweight appointment availability publishing API designed to make it easy for organizations to publish COVID vaccine appointment slot availability in cooperation with outside websites, vendors, or government programs.

Technical Specifications:

- [COVID SMART Scheduling Links](https://fhir.epic.com//Sandbox?api=10061)

 

 

### 
 Da Vinci Plan Net Provider Directory
 [read the spec](/Tech/TechSpec?spec=9465)

 

 

 The Da Vinci Plan Net Provider Directory API enables public access to provider directory information, including health insurer's insurance plans, their associated networks, and the organizations and providers that participate in these networks. 
 

 

### 
 Device, DeviceRequest, DeviceUseStatement

 

 

 

The Device, DeviceRequest, and DeviceUseStatement resources define data about a patient's implanted and external devices, requests for devices, and information about how those devices are used.

Technical Specifications:

- [Device.Read (Implants) (DSTU2)](https://fhir.epic.com//Sandbox?api=8)
- [Device.Search (Implants) (DSTU2)](https://fhir.epic.com//Sandbox?api=9)
- [Device.Read (Implants and External Devices) (STU3)](https://fhir.epic.com//Sandbox?api=892)
- [Device.Search (Implants and External Devices) (STU3)](https://fhir.epic.com//Sandbox?api=893)
- [Device.Read (Implants) (R4)](https://fhir.epic.com//Sandbox?api=1012)
- [Device.Search (Implants) (R4)](https://fhir.epic.com//Sandbox?api=1013)
- [DeviceRequest.Read (STU3)](https://fhir.epic.com//Sandbox?api=10236)
- [DeviceRequest.Search (STU3)](https://fhir.epic.com//Sandbox?api=10240)
- [DeviceRequest.Search (R4)](https://fhir.epic.com//Sandbox?api=10243)
- [DeviceUseStatement.Read (Implants and External Devices) (STU3)](https://fhir.epic.com//Sandbox?api=10245)
- [DeviceUseStatement.Search (Implants and External Devices) (STU3) ](https://fhir.epic.com//Sandbox?api=10246)
- [DeviceUseStatement.Read (Implants) (R4)](https://fhir.epic.com//Sandbox?api=10247)
- [DeviceUseStatement.Search (Implants) (R4)](https://fhir.epic.com//Sandbox?api=10248)
- [Device.Read (External Devices) (R4)](https://fhir.epic.com//Sandbox?api=10254)
- [Device.Search (External Devices) (R4)](https://fhir.epic.com//Sandbox?api=10257)
- [DeviceUseStatement.Read (External Devices) (R4)](https://fhir.epic.com//Sandbox?api=10265)
- [DeviceUseStatement.Search (External Devices) (R4)](https://fhir.epic.com//Sandbox?api=10266)
- [DeviceUseStatement.Search (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=10449)
- [DeviceUseStatement.Search (LDAs) (STU3)](https://fhir.epic.com//Sandbox?api=10450)
- [DeviceUseStatement.Read (LDAs) (STU3)](https://fhir.epic.com//Sandbox?api=10451)
- [DeviceUseStatement.Read (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=10452)
- [Device.Search (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=10454)
- [Device.Search (LDA) (STU3)](https://fhir.epic.com//Sandbox?api=10460)
- [Device.Read (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=10461)
- [Device.Read (LDA) (STU3)](https://fhir.epic.com//Sandbox?api=10462)
- [Device.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11459)
- [Device.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11460)

 

 

### 
 Device.$auxiliary-function (Auxiliary Function Notification) (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11352)

 

 

 

This web service generates a push notification that represents a task triggered from an auxiliary function.

This is currently exclusive to staff duress push notifications, which are created when a user presses a panic button on a Real-Time Location System (RTLS) device and are sent to configured groups of users. The notification tracks who has received or responded to the notification.

Staff duress push notifications require third-party RTLS Badges integration with Epic. 

 

 

### 
 DiagnosticReport

 

 

 

DiagnosticReport describes the findings associated with a diagnostic laboratory procedure.

Technical Specifications:

- [DiagnosticReport.Read (Results) (DSTU2)](https://fhir.epic.com//Sandbox?api=10)
- [DiagnosticReport.Search (Results) (DSTU2)](https://fhir.epic.com//Sandbox?api=11)
- [DiagnosticReport.Read (Results) (STU3)](https://fhir.epic.com//Sandbox?api=842)
- [DiagnosticReport.Search (Results) (STU3)](https://fhir.epic.com//Sandbox?api=843)
- [DiagnosticReport.Read (Results) (R4)](https://fhir.epic.com//Sandbox?api=988)
- [DiagnosticReport.Search (Results) (R4)](https://fhir.epic.com//Sandbox?api=989)
- [DiagnosticReport.Read (Care Plan Goal) (R4)](https://fhir.epic.com//Sandbox?api=10439)
- [DiagnosticReport.Search (Care Plan Goal) (R4)](https://fhir.epic.com//Sandbox?api=10440)
- [DiagnosticReport.Read (Care Plan Goal) (STU3)](https://fhir.epic.com//Sandbox?api=10441)
- [DiagnosticReport.Search (Care Plan Goal) (STU3)](https://fhir.epic.com//Sandbox?api=10442)
- [DiagnosticReport.Read (Outside Record Results) (R4)](https://fhir.epic.com//Sandbox?api=11372)
- [DiagnosticReport.Search (Outside Record Results) (R4)](https://fhir.epic.com//Sandbox?api=11378)

 

 

### 
 Document & Image Management
 [read the spec](/Tech/TechSpec?spec=5154)

 

 

 Manage the ability to retrieve and view images and documents that are stored in a third-party Document Management System (DMS). Through these integrations, users can more easily view documents from Epic without separately opening the DMS.
 

 

### 
 DocumentReference

 

 

 

DocumentReference provides a list of available documents for a patient. CDA documents and clinical notes are examples of documents that this resource may return.

Technical Specifications:

- [DocumentReference.Read (Generated CCDA) (DSTU2)](https://fhir.epic.com//Sandbox?api=12)
- [DocumentReference.Search (Generated CCDA) (DSTU2)](https://fhir.epic.com//Sandbox?api=13)
- [DocumentReference.Read (Clinical Notes) (STU3)](https://fhir.epic.com//Sandbox?api=844)
- [DocumentReference.Create (Clinical Notes) (STU3)](https://fhir.epic.com//Sandbox?api=845)
- [DocumentReference.Search (Clinical Notes) (STU3)](https://fhir.epic.com//Sandbox?api=865)
- [DocumentReference.Create (Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=1046)
- [DocumentReference.Read (Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=1047)
- [DocumentReference.Search (Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=1048)
- [DocumentReference.Read (Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10049)
- [DocumentReference.Create (Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10050)
- [DocumentReference.Update (Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10051)
- [DocumentReference.Read (OASIS) (R4)](https://fhir.epic.com//Sandbox?api=10126)
- [DocumentReference.Search (OASIS) (R4)](https://fhir.epic.com//Sandbox?api=10127)
- [DocumentReference.Read (HIS) (R4)](https://fhir.epic.com//Sandbox?api=10128)
- [DocumentReference.Search (HIS) (R4)](https://fhir.epic.com//Sandbox?api=10129)
- [DocumentReference.Read (Handoff) (R4)](https://fhir.epic.com//Sandbox?api=10130)
- [DocumentReference.Search (Handoff) (R4)](https://fhir.epic.com//Sandbox?api=10131)
- [DocumentReference.Read (Labs) (R4)](https://fhir.epic.com//Sandbox?api=10132)
- [DocumentReference.Search (Labs) (R4)](https://fhir.epic.com//Sandbox?api=10133)
- [DocumentReference.Read (External CCDA) (R4)](https://fhir.epic.com//Sandbox?api=10134)
- [DocumentReference.Search (External CCDA) (R4)](https://fhir.epic.com//Sandbox?api=10135)
- [DocumentReference.Read (Radiology Results) (R4)](https://fhir.epic.com//Sandbox?api=10234)
- [DocumentReference.Search (Radiology Results) (R4)](https://fhir.epic.com//Sandbox?api=10235)
- [DeviceRequest.Read (R4)](https://fhir.epic.com//Sandbox?api=10237)
- [DocumentReference.Read (Radiology Results) (STU3)](https://fhir.epic.com//Sandbox?api=10238)
- [DocumentReference.Read (Correspondences) (R4)](https://fhir.epic.com//Sandbox?api=10239)
- [DocumentReference.Read (Correspondences) (STU3)](https://fhir.epic.com//Sandbox?api=10241)
- [DocumentReference.Search (Correspondences) (STU3)](https://fhir.epic.com//Sandbox?api=10242)
- [DocumentReference.Search (Correspondences) (R4)](https://fhir.epic.com//Sandbox?api=10244)
- [DocumentReference.Search (Radiology Results) (STU3)](https://fhir.epic.com//Sandbox?api=10253)
- [DocumentReference.Read (Minimum Data Set) (R4)](https://fhir.epic.com//Sandbox?api=10274)
- [DocumentReference.Search (Minimum Data Set) (R4)](https://fhir.epic.com//Sandbox?api=10284)
- [DocumentReference.Read (IRF-PAI) (R4)](https://fhir.epic.com//Sandbox?api=10286)
- [DocumentReference.Search (IRF-PAI) (R4)](https://fhir.epic.com//Sandbox?api=10287)
- [DocumentReference.Read (Non-Patient Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10299)
- [DocumentReference.Create (Non-Patient Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10303)
- [DocumentReference.Search (Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10310)
- [DocumentReference.Read (Clinical References) (R4)](https://fhir.epic.com//Sandbox?api=10317)
- [DocumentReference.Search (Clinical References) (R4)](https://fhir.epic.com//Sandbox?api=10318)
- [DocumentReference.Read (Patient-Entered Questionnaires) (STU3)](https://fhir.epic.com//Sandbox?api=10433)
- [DocumentReference.Search (Patient-Entered Questionnaires) (STU3)](https://fhir.epic.com//Sandbox?api=10434)
- [DocumentReference.Read (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10435)
- [DocumentReference.Search (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10436)
- [DocumentReference.Read (Generated CDAs) (R4)](https://fhir.epic.com//Sandbox?api=10502)
- [DocumentReference.Search (Non-Patient Document Information) (R4)](https://fhir.epic.com//Sandbox?api=10503)
- [DocumentReference.Search (Generated CDAs) (R4)](https://fhir.epic.com//Sandbox?api=10506)
- [Communication.Search (Non-Patient Customer Relationship Management) (R4)](https://fhir.epic.com//Sandbox?api=10536)
- [Communication.Search (Customer Relationship Management) (R4)](https://fhir.epic.com//Sandbox?api=10537)
- [DocumentReference.Search (Outside Record - Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=10999)
- [DocumentReference.Read (Outside Record - Clinical Notes) (R4)](https://fhir.epic.com//Sandbox?api=11009)
- [DocumentReference.Read (Prior Auth Supporting Info) (R4)](https://fhir.epic.com//Sandbox?api=11399)

 

 

### 
 Encoder Interface API
 [read the spec](/Tech/TechSpec?spec=5458)

 

 

 

The GetEncoderMessage and SetEncoderMessage APIs are used to integrate with encoders and computer-assisted coding systems to exchange information for Hospital Coding workflows. Epic offers front-end integrations through web services as well as back-end integration methods. To see the HL7 payload, check out the [HL7v2 - Coding-Bidirectional spec](../Interface/HL7v2#Coding-Bidirectional).

 

 

### 
 Encounter

 

 

 

The Encounter resource defines the setting where patient care takes place. This includes ambulatory, inpatient, emergency, home health, and virtual encounters. If you want to store upcoming appointment information, use the Appointment resource instead of Encounter.

Technical Specifications:

- [Encounter.Read (Patient Chart) (STU3)](https://fhir.epic.com//Sandbox?api=471)
- [Encounter.Search (Patient Chart) (STU3)](https://fhir.epic.com//Sandbox?api=472)
- [Encounter.Read (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=908)
- [Encounter.Search (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=909)
- [Encounter.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11000)
- [Encounter.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11006)

 

 

### 
 Endpoint

 

 

 

The FHIR Endpoint resource describes the technical details of a location that can be connected for the delivery or retrieval of information. The resource contains information on how to connect and for what purposes. This endpoint does not need to be the current system, it can describe locally hosted services, regional services, or national services. Talk to the target organization for their supported protocols when using this resource.

Technical Specifications:

- [Endpoint.Read (STU3)](https://fhir.epic.com//Sandbox?api=866)
- [Endpoint.Read (R4)](https://fhir.epic.com//Sandbox?api=910)

 

 

### 
 EpisodeOfCare

 

 

 

The EpisodeOfCare resource returns information about a patient's episode of care, including the episode type, care team members, diagnoses, and start and end dates.

Technical Specifications:

- [EpisodeOfCare.Read (R4)](https://fhir.epic.com//Sandbox?api=10156)
- [EpisodeOfCare.Search (R4)](https://fhir.epic.com//Sandbox?api=10157)

 

 

### 
 ExplanationOfBenefit

 

 

 

ExplanationOfBenefit resources represent claims data received and processed by health plans, including services rendered to a patient and the cost information associated with those services.

Technical Specifications:

- [ExplanationOfBenefit.Read (Claim) (R4)](https://fhir.epic.com//Sandbox?api=1072)
- [ExplanationOfBenefit.Search (Claim) (R4)](https://fhir.epic.com//Sandbox?api=1073)

 

 

### 
 ExplanationOfBenefit.Read (Prior Auth) (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11039)

 

 

 

Use this API to retrieve a specific ExplanationOfBenefit (Prior Auth) resource. This resource represents medical benefit prior authorization information, including requests for services or bed day authorizations submitted for a patient.

The data returned includes prior authorization requests processed directly by the organization as well as prior authorizations received from external payers through payer data exchange workflows. Data loaded from other FHIR servers is returned in the format the organization received it. Because of this, the documentation below does not apply to these loaded resources. These resources can include any elements from the FHIR specification and can be distinguished from other resources by the presence of meta.tag set to external-bulk-data. 

When used as part of the CMS Payer-to-Payer API, only approved prior authorizations are returned. In other interoperability scenarios, both approved and denied prior authorizations can be returned.

 

 

### 
 ExplanationOfBenefit.Search (Prior Auth) (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11054)

 

 

 

Use this API to search for ExplanationOfBenefit (Prior Auth) resources for a patient. This resource represents medical benefit prior authorization requests and determinations, including both service-based and bed day authorizations.

The API can retrieve prior authorizations processed directly by the organization as well as prior authorizations received from external payers through payer data exchange workflows. Data loaded from other FHIR servers is returned in the format the organization received it. Because of this, the documentation below does not apply to these loaded resources. These resources can include any elements from the FHIR specification and can be distinguished from other resources by the presence of meta.tag set to external-bulk-data. 

When used as part of the CMS Payer-to-Payer API, only approved prior authorizations are returned. In other interoperability scenarios, both approved and denied prior authorizations can be returned.

 

 

### 
 FamilyMemberHistory

 

 

 

FamilyMemberHistory describes the conditions, history, and relationship information of a patient's family members.

Technical Specifications:

- [FamilyMemberHistory.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=337)
- [FamilyMemberHistory.Read (R4)](https://fhir.epic.com//Sandbox?api=10158)
- [FamilyMemberHistory.Search (R4)](https://fhir.epic.com//Sandbox?api=10159)

 

 

### 
 Flag

 

 

 

The Flag resource retrieves patient FYI flags from the patient chart. Patient FYIs are short, free-text notes associated with a patient or with a specific encounter for that patient.

Technical Specifications:

- [Flag.Read (Patient FYI) (R4)](https://fhir.epic.com//Sandbox?api=10165)
- [Flag.Search (Patient FYI) (R4)](https://fhir.epic.com//Sandbox?api=10166)
- [Flag.Read (Patient FYI) (STU3)](https://fhir.epic.com//Sandbox?api=10167)
- [Flag.Search (Patient FYI) (STU3)](https://fhir.epic.com//Sandbox?api=10168)
- [Flag.Search (Isolation) (R4)](https://fhir.epic.com//Sandbox?api=10195)
- [Flag.Read (Isolation) (R4)](https://fhir.epic.com//Sandbox?api=10196)
- [Flag.Read (Health Concerns) (R4)](https://fhir.epic.com//Sandbox?api=10197)
- [Flag.Search (Health Concerns) (R4)](https://fhir.epic.com//Sandbox?api=10198)
- [Flag.Read (Infection) (R4)](https://fhir.epic.com//Sandbox?api=10201)
- [Flag.Search (Infection) (R4)](https://fhir.epic.com//Sandbox?api=10202)
- [Flag.Read (Infection) (STU3) ](https://fhir.epic.com//Sandbox?api=10203)
- [Flag.Search (Infection) (STU3)](https://fhir.epic.com//Sandbox?api=10204)
- [Flag.Read (Health Concern) (STU3)](https://fhir.epic.com//Sandbox?api=10205)
- [Flag.Search (Health Concern) (STU3)](https://fhir.epic.com//Sandbox?api=10206)

 

 

### 
 GetDepartmentWaitTimes
 [read the spec](https://fhir.epic.com//Sandbox?api=204)

 

 

 

 

 

### 
 GetProviderWaitTimes
 [read the spec](https://fhir.epic.com//Sandbox?api=363)

 

 

 

 

 

### 
 GetScanSignatureContext
 [read the spec](https://fhir.epic.com//Sandbox?api=10529)

 

 

 

See [Scan Signature Deficiencies](https://open.epic.com/Interface/WebServices/Other#ScanSignatureDeficiencies) on open.epic for further documentation on this resource.

This web service returns the complete list of patient encounters that are related to the given encounter for scan signature purposes. This service can also be used to find all the documents a provider has to sign in each encounter so the provider can work on them all at once.

Vendors should call this service to get the full list of patient CSNs for which to display documents and signature requirements. This service will search for patient encounters linked to the episode of the CSN and documents with outstanding signature requirements. Outstanding in this case means a provider hasn't completed the document’s signature requirement.

 

 

### 
 GetWaitTimes
 [read the spec](https://fhir.epic.com//Sandbox?api=220)

 

 

 

 

 

### 
 Group

 

 

 

The Group resource represents information about a collection of people or other entities. In Epic workflows, for example, this resource is used to represent an employer group that is part of a health plan.

Technical Specifications:

- [Group.Read (Employer Group) (R4)](https://fhir.epic.com//Sandbox?api=10315)
- [Group.Search (Employer Group) (R4)](https://fhir.epic.com//Sandbox?api=10476)

 

 

### 
 Group.$bulk-member-match File Request
 [read the spec](https://fhir.epic.com//Sandbox?api=11426)

 

 

 

 

 

### 
 Group.$bulk-member-match Kickoff
 [read the spec](https://fhir.epic.com//Sandbox?api=11424)

 

 

 

 

 

### 
 Group.$bulk-member-match Status Request
 [read the spec](https://fhir.epic.com//Sandbox?api=11425)

 

 

 

 

 

### 
 ImagingStudy

 

 

 

The ImagingStudy resource returns information related to a DICOM imaging study.

Technical Specifications:

- [Media.Read (Study) (R4)](https://fhir.epic.com//Sandbox?api=10989)
- [Binary.Search (Study) (R4)](https://fhir.epic.com//Sandbox?api=10992)
- [Media.Search (Study) (R4)](https://fhir.epic.com//Sandbox?api=11001)

 

 

### 
 Immunization, ImmunizationRecommendation

 

 

 

Immunization describes the details of a vaccine administered to a patient. ImmunizationRecommendation is available only to organizations in the Netherlands, and describes which immunizations are recommended for a patient.

Technical Specifications:

- [Immunization.Read (DSTU2)](https://fhir.epic.com//Sandbox?api=21)
- [Immunization.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=22)
- [Immunization.Read (STU3)](https://fhir.epic.com//Sandbox?api=926)
- [Immunization.Search (STU3)](https://fhir.epic.com//Sandbox?api=927)
- [Immunization.Read (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=1070)
- [Immunization.Search (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=1071)
- [ImmunizationRecommendation.Read (R4)](https://fhir.epic.com//Sandbox?api=10249)
- [ImmunizationRecommendation.Search (R4)](https://fhir.epic.com//Sandbox?api=10250)
- [ImmunizationRecommendation.Read (STU3)](https://fhir.epic.com//Sandbox?api=10251)
- [ImmunizationRecommendation.Search (STU3)](https://fhir.epic.com//Sandbox?api=10252)
- [Immunization.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11415)
- [Immunization.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11416)

 

 

### 
 Incoming FHIR Message Acknowledgement - Denmark

 

 

 Receives asynchronous acknowledgement messages in response to any MedCom FHIR messages sent from Epic.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 InitializeDeviceResponse
 [read the spec](https://fhir.epic.com//Sandbox?api=708)

 

 

 

 

 

### 
 International Patient Summary (IPS)

 

 

 

The International Patient Summary (IPS) is a FHIR document that contains an essential set of healthcare information for a single patient, making it easy for healthcare organizations to exchange clinical data for patient care across borders and jurisdictions. For more information, refer to Epic's [International Patient Summary](https://fhir.epic.com/Documentation?docId=internationalpatientsummary) overview and the [HL7 specification](https://build.fhir.org/ig/HL7/fhir-ips/). 

Technical Specifications:

- [Patient.$summary (International Patient Summary) (R4)](https://fhir.epic.com//Sandbox?api=11219)

 

 

### 
 Introspect

 

 

 

The Introspect web service allows an application using OAuth2 secured services to get data associated with an OAuth2 token. One useful function of this service is to allow the client application to determine the user associated with the OAuth2 token.

Technical Specifications:

- [Introspect](https://fhir.epic.com//Sandbox?api=488)

 

 

### 
 List

 

 

 

The FHIR List resource defines a collection of records that can be used within many places. We support direct reading of the List resource to give access to Patient Lists. Reading is supported for those types of lists and system lists.

Technical Specifications:

- [List.Read (Patient List) (STU3)](https://fhir.epic.com//Sandbox?api=879)
- [List.Search (Patient List) (STU3)](https://fhir.epic.com//Sandbox?api=880)
- [List.Search (Medication List) (R4)](https://fhir.epic.com//Sandbox?api=10104)
- [List.Read (Medication List) (R4)](https://fhir.epic.com//Sandbox?api=10105)
- [List.Read (Problems) (R4)](https://fhir.epic.com//Sandbox?api=10144)
- [List.Search (Problems) (R4)](https://fhir.epic.com//Sandbox?api=10145)
- [List.Read (Allergies) (R4)](https://fhir.epic.com//Sandbox?api=10146)
- [List.Search (Allergies) (R4)](https://fhir.epic.com//Sandbox?api=10147)
- [List.Read (Hospital Problems) (R4)](https://fhir.epic.com//Sandbox?api=10148)
- [List.Search (Hospital Problems) (R4)](https://fhir.epic.com//Sandbox?api=10149)
- [List.Read (Family History) (R4)](https://fhir.epic.com//Sandbox?api=10150)
- [List.Search (Family History) (R4)](https://fhir.epic.com//Sandbox?api=10151)
- [List.Read (Immunizations) (R4)](https://fhir.epic.com//Sandbox?api=10152)
- [List.Search (Immunizations) (R4)](https://fhir.epic.com//Sandbox?api=10153)
- [List.Search (Patient List) (R4)](https://fhir.epic.com//Sandbox?api=10519)
- [List.Read (Patient List) (R4)](https://fhir.epic.com//Sandbox?api=10520)

 

 

### 
 Location

 

 

 

The FHIR Location resource defines details and position information for a physical place where resources and participants can be found. 

Technical Specifications:

- [Location.Read (STU3)](https://fhir.epic.com//Sandbox?api=823)
- [Location.Read (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=928)
- [Location.Search (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=10084)
- [Location.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11461)
- [Location.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11462)

 

 

### 
 Medication, MedicationOrder, MedicationRequest, MedicationStatement, MedicationDispense

 

 

 

The Medication, MedicationOrder, MedicationRequest and MedicationStatement data models combine to model a patient's reported and prescribed medication orders and instructions. Medication provides information about each medication, independent of a patient. The MedicationOrder and MedicationRequest resources give a summary of the medication orders placed for the patient along with their status. The MedicationStatement resource gives a full-picture summary of all medications a patient may be taking, whether they are prescriptions or patient-reported medications. The MedicationDispense resource is available only to organizations in the Netherlands, and indicates how a medication product is to be or has been dispensed for a patient.

Technical Specifications:

- [Medication.Read (DSTU2)](https://fhir.epic.com//Sandbox?api=23)
- [MedicationOrder.Read (DSTU2)](https://fhir.epic.com//Sandbox?api=25)
- [MedicationOrder.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=26)
- [MedicationStatement.Read (DSTU2)](https://fhir.epic.com//Sandbox?api=338)
- [MedicationStatement.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=339)
- [Medication.Read (STU3)](https://fhir.epic.com//Sandbox?api=489)
- [MedicationRequest.Read (Signed Medication Order) (STU3)](https://fhir.epic.com//Sandbox?api=490)
- [MedicationRequest.Search (Signed Medication Order) (STU3)](https://fhir.epic.com//Sandbox?api=491)
- [MedicationStatement.Read (STU3)](https://fhir.epic.com//Sandbox?api=492)
- [MedicationStatement.Search (STU3)](https://fhir.epic.com//Sandbox?api=493)
- [Medication.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=692)
- [Medication.Read (Organization Med List) (R4)](https://fhir.epic.com//Sandbox?api=995)
- [MedicationRequest.Read (Signed Medication Order) (R4)](https://fhir.epic.com//Sandbox?api=996)
- [MedicationRequest.Search (Signed Medication Order) (R4)](https://fhir.epic.com//Sandbox?api=997)
- [CDS Hooks MedicationRequest.Create (Unsigned Order) (R4)](https://fhir.epic.com//Sandbox?api=1060)
- [CDS Hooks MedicationRequest.Create (Unsigned Order) (STU3)](https://fhir.epic.com//Sandbox?api=1061)
- [CDS Hooks MedicationRequest.Read (Unsigned Order) (R4)](https://fhir.epic.com//Sandbox?api=10031)
- [Medication.Search (Organization Med List) (R4)](https://fhir.epic.com//Sandbox?api=10079)
- [MedicationRequest.Read (Order Template Medication) (R4)](https://fhir.epic.com//Sandbox?api=10095)
- [MedicationRequest.Search (Order Template Medication) (R4)](https://fhir.epic.com//Sandbox?api=10096)
- [CDS Hooks MedicationRequest.Delete (Unsigned Order) (R4)](https://fhir.epic.com//Sandbox?api=10160)
- [CDS Hooks MedicationRequest.Delete (Unsigned Order) (STU3)](https://fhir.epic.com//Sandbox?api=10161)
- [MedicationDispense.Read (Verified Orders) (R4)](https://fhir.epic.com//Sandbox?api=10212)
- [MedicationDispense.Read (Verified Orders) (STU3)](https://fhir.epic.com//Sandbox?api=10213)
- [MedicationDispense.Search (Verified Orders) (STU3)](https://fhir.epic.com//Sandbox?api=10214)
- [MedicationDispense.Search (Verified Orders) (R4)](https://fhir.epic.com//Sandbox?api=10217)
- [MedicationAdministration.Search (LDAs) (R4)](https://fhir.epic.com//Sandbox?api=10463)
- [MedicationAdministration.Search (LDAs) (STU3)](https://fhir.epic.com//Sandbox?api=10464)
- [MedicationAdministration.Read (LDAs) (R4)](https://fhir.epic.com//Sandbox?api=10466)
- [MedicationAdministration.Read (LDAs) (STU3)](https://fhir.epic.com//Sandbox?api=10467)
- [MedicationDispense.Search (Fill Status) (R4)](https://fhir.epic.com//Sandbox?api=10646)
- [MedicationDispense.Read (Fill Status) (R4)](https://fhir.epic.com//Sandbox?api=10647)
- [MedicationRequest.Update (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11268)
- [MedicationRequest.Read (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11271)
- [MedicationRequest.Search (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11272)
- [MedicationDispense.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11417)
- [MedicationDispense.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11418)
- [MedicationRequest.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11419)
- [MedicationRequest.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11420)
- [Medication.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11463)
- [Medication.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11464)

 

 

### 
 NutritionOrder

 

 

 

NutritionOrder describes diet order data including oral diets, oral nutrition supplements, enteral nutrition (tube feedings), and infant formula. It can also include details about a patient's food allergies, intolerances, and personal/cultural requirements or preferences.

Technical Specifications:

- [NutritionOrder.Read (R4)](https://fhir.epic.com//Sandbox?api=10224)
- [NutritionOrder.Search (R4)](https://fhir.epic.com//Sandbox?api=10227)
- [NutritionOrder.Read (STU3)](https://fhir.epic.com//Sandbox?api=10228)
- [NutritionOrder.Search (STU3)](https://fhir.epic.com//Sandbox?api=10229)

 

 

### 
 Observation

 

 

 

This implementation of the Observation resource supports querying for vital signs, lab results, lines drains and airways (LDA-W), obstetric details, core characteristics, and smoking history. 

Technical Specifications:

- [Observation.Read (Labs) (DSTU2)](https://fhir.epic.com//Sandbox?api=27)
- [Observation.Search (Labs) (DSTU2)](https://fhir.epic.com//Sandbox?api=28)
- [Observation.Read (Social History) (DSTU2)](https://fhir.epic.com//Sandbox?api=447)
- [Observation.Search (Social History) (DSTU2)](https://fhir.epic.com//Sandbox?api=448)
- [Observation.Read (Vitals) (DSTU2)](https://fhir.epic.com//Sandbox?api=449)
- [Observation.Search (Vitals) (DSTU2)](https://fhir.epic.com//Sandbox?api=450)
- [Observation.Read (Labs) (STU3)](https://fhir.epic.com//Sandbox?api=494)
- [Observation.Search (Labs) (STU3)](https://fhir.epic.com//Sandbox?api=495)
- [Observation.Create (Vitals) (STU3)](https://fhir.epic.com//Sandbox?api=496)
- [Observation.Read (Vitals) (STU3)](https://fhir.epic.com//Sandbox?api=497)
- [Observation.Search (Vitals) (STU3)](https://fhir.epic.com//Sandbox?api=498)
- [Observation.Read (Core Characteristics) (STU3)](https://fhir.epic.com//Sandbox?api=853)
- [Observation.Search (Core Characteristics) (STU3)](https://fhir.epic.com//Sandbox?api=854)
- [Observation.Read (Social History) (STU3)](https://fhir.epic.com//Sandbox?api=855)
- [Observation.Search (Social History) (STU3)](https://fhir.epic.com//Sandbox?api=856)
- [Observation.Create (LDA-W) (STU3)](https://fhir.epic.com//Sandbox?api=897)
- [Observation.Read (LDA-W) (STU3)](https://fhir.epic.com//Sandbox?api=898)
- [Observation.Search (LDA-W) (STU3)](https://fhir.epic.com//Sandbox?api=899)
- [Observation.Update (LDA-W) (STU3)](https://fhir.epic.com//Sandbox?api=900)
- [Observation.Create (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=962)
- [Observation.Create (Vital Signs) (R4)](https://fhir.epic.com//Sandbox?api=963)
- [Observation.Read (Core Characteristics) (R4)](https://fhir.epic.com//Sandbox?api=964)
- [Observation.Read (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=965)
- [Observation.Read (Social History) (R4)](https://fhir.epic.com//Sandbox?api=967)
- [Observation.Read (Vital Signs) (R4)](https://fhir.epic.com//Sandbox?api=968)
- [Observation.Search (Core Characteristics) (R4)](https://fhir.epic.com//Sandbox?api=969)
- [Observation.Search (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=970)
- [Observation.Search (Social History) (R4)](https://fhir.epic.com//Sandbox?api=972)
- [Observation.Search (Vital Signs) (R4)](https://fhir.epic.com//Sandbox?api=973)
- [Observation.Update (Lines, Drains, Airways) (R4)](https://fhir.epic.com//Sandbox?api=974)
- [Observation.Read (Labs) (R4)](https://fhir.epic.com//Sandbox?api=998)
- [Observation.Search (Labs) (R4)](https://fhir.epic.com//Sandbox?api=999)
- [Observation.Read (Periodontal) (R4)](https://fhir.epic.com//Sandbox?api=10070)
- [Observation.Search (Periodontal) (R4)](https://fhir.epic.com//Sandbox?api=10071)
- [Observation.Read (SmartData Elements) (R4)](https://fhir.epic.com//Sandbox?api=10120)
- [Observation.Search (SmartData Elements) (R4)](https://fhir.epic.com//Sandbox?api=10121)
- [Observation.Read (Activities of Daily Living) (R4)](https://fhir.epic.com//Sandbox?api=10122)
- [Observation.Search (Activities of Daily Living) (R4)](https://fhir.epic.com//Sandbox?api=10123)
- [Observation.Read (Activities of Daily Living) (STU3)](https://fhir.epic.com//Sandbox?api=10124)
- [Observation.Search (Activities of Daily Living) (STU3)](https://fhir.epic.com//Sandbox?api=10125)
- [Observation.$lastn (Labs) (STU3)](https://fhir.epic.com//Sandbox?api=10188)
- [Observation.$lastn (Social History) (STU3)](https://fhir.epic.com//Sandbox?api=10223)
- [Observation.$lastn (Activities of Daily Living) (STU3)](https://fhir.epic.com//Sandbox?api=10282)
- [Observation.Read (Study Finding) (R4)](https://fhir.epic.com//Sandbox?api=10289)
- [Observation.Read (Obstetrics and Gynecology) (R4)](https://fhir.epic.com//Sandbox?api=10293)
- [Observation.Search (Obstetrics and Gynecology) (R4)](https://fhir.epic.com//Sandbox?api=10294)
- [Observation.Search (Study Finding) (R4)](https://fhir.epic.com//Sandbox?api=10297)
- [Observation.Search (Genomics) (R4)](https://fhir.epic.com//Sandbox?api=10298)
- [Observation.Read (Labor and Delivery) (R4)](https://fhir.epic.com//Sandbox?api=10300)
- [Observation.Search (Labor and Delivery) (R4)](https://fhir.epic.com//Sandbox?api=10301)
- [Observation.Read (Genomics) (R4)](https://fhir.epic.com//Sandbox?api=10304)
- [Observation.Read (Newborn Delivery) (R4)](https://fhir.epic.com//Sandbox?api=10306)
- [Observation.Search (Newborn Delivery) (R4)](https://fhir.epic.com//Sandbox?api=10307)
- [Observation.Read (Family Situation) (STU3)](https://fhir.epic.com//Sandbox?api=10444)
- [Observation.Read (Family Situation) (R4)](https://fhir.epic.com//Sandbox?api=10455)
- [Observation.Search (Family Situation) (R4)](https://fhir.epic.com//Sandbox?api=10456)
- [Observation.Search (Family Situation) (STU3)](https://fhir.epic.com//Sandbox?api=10457)
- [Observation.$lastn (Vitals) (STU3)](https://fhir.epic.com//Sandbox?api=10484)
- [Observation.Search (Assessments) (R4)](https://fhir.epic.com//Sandbox?api=11052)
- [Observation.Read (Assessments) (R4)](https://fhir.epic.com//Sandbox?api=11053)
- [Observation.Search (SDOH Assessments) (R4)](https://fhir.epic.com//Sandbox?api=11104)
- [Observation.Read (SDOH Assessments) (R4)](https://fhir.epic.com//Sandbox?api=11105)
- [Observation.Create (DICOM Image Characteristics) (R4)](https://fhir.epic.com//Sandbox?api=11224)
- [Observation.Update (DICOM Image Characteristics) (R4)](https://fhir.epic.com//Sandbox?api=11225)
- [Observation.Search (DICOM Image Characteristics) (R4)](https://fhir.epic.com//Sandbox?api=11226)
- [Observation.Read (DICOM Image Characteristics) (R4)](https://fhir.epic.com//Sandbox?api=11227)
- [Observation.Search (Phenotype) (R4)](https://fhir.epic.com//Sandbox?api=11328)
- [Observation.Read (Phenotype) (R4)](https://fhir.epic.com//Sandbox?api=11330)
- [Observation.Read (Outside Record Sexual Orientation) (R4)](https://fhir.epic.com//Sandbox?api=11375)
- [Observation.Read (Outside Record Smoking Status) (R4)](https://fhir.epic.com//Sandbox?api=11379)
- [Observation.Search (Outside Record Results) (R4)](https://fhir.epic.com//Sandbox?api=11381)
- [Observation.Search (Outside Record Smoking Status) (R4)](https://fhir.epic.com//Sandbox?api=11383)
- [Observation.Search (Outside Record Sexual Orientation) (R4)](https://fhir.epic.com//Sandbox?api=11384)
- [Observation.Read (Outside Record Screening Assessment) (R4)](https://fhir.epic.com//Sandbox?api=11386)
- [Observation.Search (Outside Record Screening Assessment) (R4)](https://fhir.epic.com//Sandbox?api=11388)
- [Observation.Read (Outside Record Pregnancy Status) (R4)](https://fhir.epic.com//Sandbox?api=11391)
- [Observation.Search (Outside Record Pregnancy Status) (R4)](https://fhir.epic.com//Sandbox?api=11392)
- [Observation.Read (Outside Record Vital Signs) (R4)](https://fhir.epic.com//Sandbox?api=11421)
- [Observation.Search (Outside Record Vital Signs) (R4)](https://fhir.epic.com//Sandbox?api=11422)
- [Observation.Read (Outside Record Activities of Daily Living) (R4)](https://fhir.epic.com//Sandbox?api=11465)
- [Observation.Search (Outside Record Activities of Daily Living) (R4)](https://fhir.epic.com//Sandbox?api=11466)
- [Observation.Read (Outside Record Occupation) (R4)](https://fhir.epic.com//Sandbox?api=11467)
- [Observation.Search (Outside Record Occupation) (R4)](https://fhir.epic.com//Sandbox?api=11468)
- [Observation.Read (Outside Record SDOH Assessment) (R4)](https://fhir.epic.com//Sandbox?api=11469)
- [Observation.Search (Outside Record SDOH Assessment) (R4)](https://fhir.epic.com//Sandbox?api=11470)

 

 

### 
 Organization

 

 

 

The read interaction of the Organization resource allows you to look up an organization using a constant server ID. The read interaction allows clients to store only the server ID, and with a single request, retrieve the most up-to-date information about an organization. Read interactions typically begin with a client having previously established a relationship, often through querying for Organization or PractitionerRoles through the search interaction.

Technical Specifications:

- [Organization.Read (STU3)](https://fhir.epic.com//Sandbox?api=857)
- [Organization.Read (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=929)
- [Organization.Search (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=10083)
- [Organization.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11439)
- [Organization.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11441)

 

 

### 
 Outgoing Hospital Notification

 

 

 Sends hospital notification messages to Danish municipalities. This interface can send ED arrival, admission, discharge, leave of absence, and death notifications. The messages follow the MedComHospitalNotificationMessage profile specifications.
 

 

 [Current integrations include ](#)
 

 - MEDCOM Information Systems

 

 

 

### 
 Outgoing Vital Records Death Reporting
 [read the spec](/Tech/TechSpec?spec=9450)

 

 

 Automates the death certification process by sending the required medical certifier information for a patient death to state or jurisdictional Vital Records Reporting systems. The interface follows the HL7 Vital Records Death Reporting (VRDR) FHIR Implementation Guide, VRDR 3.0.0, FHIR STU3.
 

 

### 
 PAS Incoming Claim Response Notification
 [read the spec](https://fhir.epic.com//Sandbox?api=11277)

 

 

 

The HL7 FHIR Da Vinci Prior Authorization Support (PAS) STU 2.1 ([https://hl7.org/fhir/us/davinci-pas/STU2.1/](https://hl7.org/fhir/us/davinci-pas/STU2.1/)) functionality is intended to streamline the prior authorization process using a FHIR-based data exchange rather than the previous ANSI X12-based electronic messaging specification as well as to encourage automation throughout the process.

Complex prior authorization requests can take some time to adjudicate. When a health plan finishes their adjudication or modifies the request, they shall use the $notify operation to inform the health system. This operation is essentially an asynchronous response to an authorization request using a bundled ClaimResponse resource ([https://hl7.org/fhir/us/davinci-pas/STU2.1/StructureDefinition-profile-pas-response-bundle.html](https://hl7.org/fhir/us/davinci-pas/STU2.1/StructureDefinition-profile-pas-response-bundle.html)).

While the HL7 specification suggests that a subscription ([https://hl7.org/fhir/us/davinci-pas/STU2.1/specification.html#subscription](https://hl7.org/fhir/us/davinci-pas/STU2.1/specification.html#subscription)) request should first be submitted to initiate this notification process, Epic recommends that health plans should always assume that a subscription is desired when an authorization request has been submitted to improve automation.

 

 

### 
 Patient

 

 

 

This basic FHIR service covers data about persons receiving care or other health-related services. It focuses on the demographic information necessary to support administrative, financial, or logistic purposes.

Technical Specifications:

- [Patient.Read (DSTU2)](https://fhir.epic.com//Sandbox?api=29)
- [Patient.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=30)
- [Patient.Create (STU3)](https://fhir.epic.com//Sandbox?api=824)
- [Patient.Read (STU3)](https://fhir.epic.com//Sandbox?api=825)
- [Patient.Search (STU3)](https://fhir.epic.com//Sandbox?api=883)
- [Patient.Create (Demographics) (R4)](https://fhir.epic.com//Sandbox?api=930)
- [Patient.Read (Demographics) (R4)](https://fhir.epic.com//Sandbox?api=931)
- [Patient.Search (Demographics) (R4)](https://fhir.epic.com//Sandbox?api=932)
- [Patient.$match (Patient Match) (R4)](https://fhir.epic.com//Sandbox?api=10423)

 

 

### 
 Patient Lookup and Identifiers
 [read the spec](/Tech/TechSpec?spec=5454)

 

 

 

Search for patients and obtain or assign identifiers. If no patient can be found for the given criteria, a patient record can be created.

 

 

### 
 Personnel Management
 [read the spec](/Tech/TechSpec?spec=5453)

 

 

 

Create, update, and delete user records in Epic. With this suite of services, you can also view and update user groups, pager IDs, user login departments, and departments the user has access to.

 

 

### 
 Practitioner, PractitionerRole

 

 

 

The Practicioner service covers data about providers of care or other health-related services. 

Technical Specifications:

- [Practitioner.Read (DSTU2)](https://fhir.epic.com//Sandbox?api=31)
- [Practitioner.Read (STU3)](https://fhir.epic.com//Sandbox?api=499)
- [Practitioner.Search (DSTU2)](https://fhir.epic.com//Sandbox?api=826)
- [Practitioner.Search (STU3)](https://fhir.epic.com//Sandbox?api=858)
- [PractitionerRole.Read (STU3)](https://fhir.epic.com//Sandbox?api=859)
- [PractitionerRole.Search (STU3)](https://fhir.epic.com//Sandbox?api=885)
- [Practitioner.Read (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=935)
- [Practitioner.Search (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=936)
- [PractitionerRole.Read (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=937)
- [PractitionerRole.Search (Organizational Directory) (R4)](https://fhir.epic.com//Sandbox?api=938)
- [PractitionerRole.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11373)
- [PractitionerRole.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11385)
- [Practitioner.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11471)
- [Practitioner.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11472)

 

 

### 
 Print Job Status
 [read the spec](/Tech/TechSpec?spec=5451)

 

 

 

Use the UpdatePrintJobStatus API to send back information about the status of the print job that you received from Epic through Epic Print Service (EPS).

 

 

### 
 PrintTestPage
 [read the spec](https://fhir.epic.com//Sandbox?api=380)

 

 

 

 

 

### 
 PrintTestPageToTray
 [read the spec](https://fhir.epic.com//Sandbox?api=10040)

 

 

 

 

 

### 
 Procedure, ProcedureRequest, ServiceRequest

 

 

 

Procedure describes performed surgical, dental, and diagnostic procedures on a patient. ProcedureRequest and ServiceRequest define a request for a procedure to be planned, proposed, or performed. The results of ProcedureRequest and ServiceRequest are available in the Procedure resource or the DiagnosticReport resource.

Technical Specifications:

- [Procedure.Read (Orders) (DSTU2)](https://fhir.epic.com//Sandbox?api=33)
- [Procedure.Search (Orders) (DSTU2)](https://fhir.epic.com//Sandbox?api=34)
- [ProcedureRequest.Read (Orders) (STU3)](https://fhir.epic.com//Sandbox?api=886)
- [ProcedureRequest.Search (Orders) (STU3)](https://fhir.epic.com//Sandbox?api=887)
- [Procedure.Read (Orders, Surgeries) (STU3)](https://fhir.epic.com//Sandbox?api=939)
- [Procedure.Search (Orders, Surgeries) (STU3)](https://fhir.epic.com//Sandbox?api=940)
- [Procedure.Read (Orders) (R4)](https://fhir.epic.com//Sandbox?api=975)
- [Procedure.Search (Orders) (R4)](https://fhir.epic.com//Sandbox?api=976)
- [ServiceRequest.Read (Orders) (R4)](https://fhir.epic.com//Sandbox?api=1053)
- [ServiceRequest.Search (Orders) (R4)](https://fhir.epic.com//Sandbox?api=1054)
- [CDS Hooks ServiceRequest.Create (Unsigned Order) (R4)](https://fhir.epic.com//Sandbox?api=1062)
- [CDS Hooks ProcedureRequest.Create (Unsigned Order) (STU3)](https://fhir.epic.com//Sandbox?api=1063)
- [ServiceRequest.Read (Dental Procedure) (R4)](https://fhir.epic.com//Sandbox?api=10018)
- [ServiceRequest.Search (Dental Procedure) (R4)](https://fhir.epic.com//Sandbox?api=10019)
- [Procedure.Read (Patient-Reported Surgical History) (R4)](https://fhir.epic.com//Sandbox?api=10029)
- [Procedure.Search (Patient-Reported Surgical History) (R4)](https://fhir.epic.com//Sandbox?api=10030)
- [CDS Hooks ServiceRequest.Read (Unsigned Order) (R4)](https://fhir.epic.com//Sandbox?api=10032)
- [Procedure.Read (Surgeries) (R4)](https://fhir.epic.com//Sandbox?api=10041)
- [Procedure.Search (Surgeries) (R4)](https://fhir.epic.com//Sandbox?api=10042)
- [ServiceRequest.Read (Community Resource ServiceRequest) (R4)](https://fhir.epic.com//Sandbox?api=10091)
- [ServiceRequest.Search (Community Resource ServiceRequest) (R4)](https://fhir.epic.com//Sandbox?api=10092)
- [ServiceRequest.Read (Order Template Procedure) (R4)](https://fhir.epic.com//Sandbox?api=10093)
- [ServiceRequest.Search (Order Template Procedure) (R4)](https://fhir.epic.com//Sandbox?api=10094)
- [CDS Hooks ServiceRequest.Delete (Unsigned Order) (R4)](https://fhir.epic.com//Sandbox?api=10162)
- [CDS Hooks ProcedureRequest.Delete (Unsigned Order) (STU3)](https://fhir.epic.com//Sandbox?api=10163)
- [ServiceRequest.Read (Referral) (R4)](https://fhir.epic.com//Sandbox?api=10164)
- [ServiceRequest.Read (Pregnancy Plans) (R4)](https://fhir.epic.com//Sandbox?api=10276)
- [ServiceRequest.Search (Pregnancy Plans) (R4)](https://fhir.epic.com//Sandbox?api=10277)
- [Procedure.Read (Surgical History) (STU3)](https://fhir.epic.com//Sandbox?api=10398)
- [Procedure.Search (Surgical History) (STU3)](https://fhir.epic.com//Sandbox?api=10399)
- [Procedure.Read (Nursing Intervention) (R4)](https://fhir.epic.com//Sandbox?api=10470)
- [Procedure.Search (Restricting Intervention) (R4)](https://fhir.epic.com//Sandbox?api=10472)
- [Procedure.Search (Restricting Intervention) (STU3)](https://fhir.epic.com//Sandbox?api=10473)
- [Procedure.Read (Restricting Intervention) (R4)](https://fhir.epic.com//Sandbox?api=10474)
- [Procedure.Read (Restricting Intervention) (STU3)](https://fhir.epic.com//Sandbox?api=10475)
- [Procedure.Read (Nursing Intervention) (STU3)](https://fhir.epic.com//Sandbox?api=10477)
- [Procedure.Search (Nursing Intervention) (R4)](https://fhir.epic.com//Sandbox?api=10479)
- [Procedure.Search (Nursing Intervention) (STU3)](https://fhir.epic.com//Sandbox?api=10480)
- [CDS Hooks ServiceRequest.Update (Unsigned Order) (R4)](https://fhir.epic.com//Sandbox?api=10643)
- [CDS Hooks ProcedureRequest.Update (Unsigned Order) (STU3)](https://fhir.epic.com//Sandbox?api=10644)
- [Procedure.Search (SDOH Intervention) (R4)](https://fhir.epic.com//Sandbox?api=11038)
- [ServiceRequest.Create (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11044)
- [ServiceRequest.Read (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11045)
- [ServiceRequest.Search (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11046)
- [ServiceRequest.Update (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11047)
- [Procedure.Create (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11048)
- [Procedure.Read (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11049)
- [Procedure.Search (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11050)
- [Procedure.Update (External Radiotherapy Summary) (R4)](https://fhir.epic.com//Sandbox?api=11051)
- [Procedure.Read (SDOH Intervention) (R4)](https://fhir.epic.com//Sandbox?api=11055)
- [ServiceRequest.Read (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11265)
- [ServiceRequest.Search (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11266)
- [ServiceRequest.Update (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11267)
- [Procedure.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11368)
- [Procedure.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11370)
- [ServiceRequest.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11475)
- [ServiceRequest.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11476)

 

 

### 
 ProcessTransactionResponse
 [read the spec](https://fhir.epic.com//Sandbox?api=710)

 

 

 

 

 

### 
 Provenance

 

 

 

Provenance returns contextual metadata about the origin of a different resource, such as who authored the data for the target resource, who transmitted it, or which organization such actions were performed on behalf of.

Technical Specifications:

- [Provenance.Read (R4)](https://fhir.epic.com//Sandbox?api=10180)

 

 

### 
 Questionnaire, QuestionnaireResponse

 

 

 

The Questionnaire resource is an organized collection of questions intended to solicit information from patients, providers or other individuals involved in the healthcare domain. The QuestionnaireResponse resource provides a complete or partial list of answers to a set of questions filled when responding to a questionnaire.

Technical Specifications:

- [QuestionnaireResponse.Create (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10023)
- [QuestionnaireResponse.Read (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10024)
- [Questionnaire.Read (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10025)
- [Questionnaire.Search (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10081)
- [QuestionnaireResponse.Read (Code Status Questionnaire) (R4)](https://fhir.epic.com//Sandbox?api=10226)
- [QuestionnaireResponse.Read (Prior Auth) (R4)](https://fhir.epic.com//Sandbox?api=11394)
- [QuestionnaireResponse.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11473)
- [QuestionnaireResponse.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11474)

 

 

### 
 Questionnaire.$log-questionnaire-errors (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11414)

 

 

 

The Questionnaire.$log-questionnaire-errors operation allows a client to report errors encountered while rendering or processing a DTR questionnaire.
The request identifies the questionnaire using its canonical URL. The server validates the canonical, resolves the appropriate downstream endpoint based on that canonical, and forwards the request to that endpoint for processing.
This implementation does not interpret or process the reported error details locally. Any additional parameters (such as an operationOutcome describing the errors) are forwarded to the resolved downstream endpoint without modification.
If the questionnaire canonical cannot be validated or resolved to a downstream endpoint, the operation returns an OperationOutcome describing the failure.
On successful resolution, the downstream endpoint’s response is returned unchanged.
Refer to [Operation Definition of $log-questionnaire-errors v2.1.0](https://www.hl7.org/fhir/us/davinci-dtr/STU2.1/OperationDefinition-log-questionnaire-errors.html) and [Structure Definition of dtr-log-errors-input-parameters v2.1.0](https://www.hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-log-errors-input-parameters.html) for more information.

 

 

### 
 Questionnaire.$next-question (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11400)

 

 

 

The Questionnaire.$next-question operation supports adaptive (dynamic) questionnaires by enabling a client to request the next set of questions based on the answers collected so far.

The client sends a FHIR Parameters resource containing a single input parameter named "in", whose value is a QuestionnaireResponse representing the current questionnaire state. The QuestionnaireResponse includes the Questionnaire definition as a contained resource and any answers gathered up to that point.

The server evaluates the adaptive logic and returns a FHIR Parameters resource containing a single output parameter named "out", whose value is an updated QuestionnaireResponse. The returned QuestionnaireResponse preserves previously provided answers and updates the contained Questionnaire to include the next question(s) the client should present.

This operation is typically called repeatedly in a loop:

- 

The client submits the current QuestionnaireResponse.

- 

The server returns the next question(s).

- 

The client collects answers and resubmits.

This cycle repeats until the server returns a QuestionnaireResponse with status = complete.

If the input is invalid or incomplete, the server returns an OperationOutcome describing the issue.

Refer to [Operation Definition of DTR Questionnaire $next-question v2.1.0](https://hl7.org/fhir/us/davinci-dtr/STU2.1/OperationDefinition-DTR-Questionnaire-next-question.html), [Structure Definition of dtr-next-question-input-parameters v2.1.0](https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-next-question-input-parameters.html), and [Structure Definition of dtr-next-question-output-parameters v2.1.0](https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-next-question-output-parameters.html) for more information.

 

 

### 
 Questionnaire.$questionnaire-package (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11287)

 

 

 

The HL7 FHIR Da Vinci Documentation Templates and Rules (DTR) STU 2.1 ([https://hl7.org/fhir/us/davinci-dtr/STU2.1/](https://hl7.org/fhir/us/davinci-dtr/STU2.1/)) enables health plans to express their documentation requirements for prior authorizations and to allow health systems to gather and submit that information in a streamlined manner. 

When a health plan responds to a CRD ([https://hl7.org/fhir/us/davinci-crd/STU2.1/](https://hl7.org/fhir/us/davinci-crd/STU2.1/)) or PAS ([https://hl7.org/fhir/us/davinci-pas/STU2.1/](https://hl7.org/fhir/us/davinci-pas/STU2.1/)) message indicating that clinical or administrative data is required, and optionally includes a canonical questionnaire, the health system performs a $questionnaire-package operation ([https://hl7.org/fhir/us/davinci-dtr/STU2.1/OperationDefinition-questionnaire-package.html](https://hl7.org/fhir/us/davinci-dtr/STU2.1/OperationDefinition-questionnaire-package.html)). 

Health systems use the $questionnaire-package operation ([https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-qpackage-input-parameters.html](https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-qpackage-input-parameters.html)) to retrieve a DTR Standard Questionnaire resource ([https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-std-questionnaire.html](https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-std-questionnaire.html)) from the output ([https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-qpackage-output-parameters.html](https://hl7.org/fhir/us/davinci-dtr/STU2.1/StructureDefinition-dtr-qpackage-output-parameters.html)), which is shown to an appropriate user. 

The health system then builds a QuestionnaireResponse resource from the answered questionnaire and sends it to the health plan as part of the PAS request process. 

 

 

### 
 RelatedPerson

 

 

 

The FHIR RelatedPerson resource is typically an entity with a personal or professional relationship to the patient. RelatedPersons are often a source of information about the patient. For integrations with Epic, the RelatedPerson is represented by a MyChart account record ID and their link to a Patient record ID. Typically the RelatedPerson represents a MyChart proxy for the patient.

Technical Specifications:

- [RelatedPerson.Read (Proxy) (R4)](https://fhir.epic.com//Sandbox?api=977)
- [RelatedPerson.Read (Friends and Family) (R4)](https://fhir.epic.com//Sandbox?api=11003)
- [RelatedPerson.Search (Proxy) (R4)](https://fhir.epic.com//Sandbox?api=11007)
- [RelatedPerson.Search (Friends and Family) (R4)](https://fhir.epic.com//Sandbox?api=11008)
- [RelatedPerson.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11438)
- [RelatedPerson.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11440)

 

 

### 
 Release of Information
 [read the spec](/Tech/TechSpec?spec=5450)

 

 

 

Create and update release of information (ROI) requests.

 

 

### 
 RequestGroup

 

 

 

A RequestGroup represents a group of related requests, such as MedicationRequest or ServiceRequest resources, that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".

Technical Specifications:

- [RequestGroup.Read (Dental Visit) (R4)](https://fhir.epic.com//Sandbox?api=10020)
- [RequestGroup.Read (Oncology Plan Day) (R4)](https://fhir.epic.com//Sandbox?api=10077)
- [RequestGroup.Search (Oncology Plan Day) (R4)](https://fhir.epic.com//Sandbox?api=10078)
- [RequestGroup.Search (Dental Visit) (R4)](https://fhir.epic.com//Sandbox?api=10080)
- [QuestionnaireResponse.Search (Patient-Entered Questionnaires) (R4)](https://fhir.epic.com//Sandbox?api=10082)

 

 

### 
 ResearchStudy

 

 

 

The ResearchStudy resource includes general information about the research studies tracked in Epic, including the title, status, identifier, and principal investigator. These studies focus on the safety, efficacy, comparative effectiveness, and other information about medications, devices, therapies, and other intervention and investigative techniques intended to increase the field of healthcare-related knowledge.

Technical Specifications:

- [ResearchStudy.Read (R4)](https://fhir.epic.com//Sandbox?api=1002)
- [ResearchStudy.Search (R4)](https://fhir.epic.com//Sandbox?api=1003)

 

 

### 
 ResearchSubject

 

 

 

The ResearchSubject resource includes general information about a research subject tracked in Epic, including the study, study arm, consent status, and other key items. Epic tracks human beings only for research associations.

Technical Specifications:

- [ResearchSubject.Read (R4)](https://fhir.epic.com//Sandbox?api=10142)
- [ResearchSubject.Search (R4)](https://fhir.epic.com//Sandbox?api=10143)

 

 

### 
 Scan Signature Deficiencies
 [read the spec](/Tech/TechSpec?spec=5449)

 

 

 

When using a document management system (DMS) to manage scans on a patient's chart, it's also possible to track signature requirements for those scans in Epic. DMS applications can use these web services to create and update signature deficiencies in Epic. These signature deficiencies will notify the signing users and let them launch directly into the DMS's signing application.

 

 

### 
 Security Information and Event Management (SIEM)

 

 

 

Receive event and access information from Epic to detect security incidents.

 

 

### 
 Specimen

 

 

 

The specimen resource covers substances used for diagnostic and environmental testing. The specimen resource focuses on the process for gathering, maintaining and processing the specimen as well as where the specimen originated.

Technical Specifications:

- [Specimen.Read (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=10014)
- [Specimen.Search (Patient Chart) (R4)](https://fhir.epic.com//Sandbox?api=10015)
- [Specimen.Read (STU3)](https://fhir.epic.com//Sandbox?api=10207)
- [Specimen.Search (STU3)](https://fhir.epic.com//Sandbox?api=10210)
- [Specimen.Read (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11364)
- [Specimen.Search (Outside Record) (R4)](https://fhir.epic.com//Sandbox?api=11366)

 

 

### 
 Substance

 

 

 

Substance returns basic information about a substance, such as the code or set of codes that identify the substance. For example, this resource can describe an electrolyte ion component of a total parenteral nutrition (TPN) medication.

Technical Specifications:

- [Substance.Read (R4)](https://fhir.epic.com//Sandbox?api=10075)
- [Substance.Search (R4)](https://fhir.epic.com//Sandbox?api=10076)

 

 

### 
 Task

 

 

 

The Task resource describes activities and tracks the completion state of those activities. It includes details such as the description of the task, the patient to whom it applies, who is expected to perform the task, and the task’s status. This resource can be used to track tasks associated with referral requests made through continued care and services workflows in Epic, such as a post-discharge service request for durable medical equipment (DME) or social services.

Technical Specifications:

- [Task.Read (Community Resource) (R4)](https://fhir.epic.com//Sandbox?api=10085)
- [Task.Search (Community Resource) (R4)](https://fhir.epic.com//Sandbox?api=10086)
- [Task.Update (Community Resource) (R4)](https://fhir.epic.com//Sandbox?api=10087)
- [Task.Read (Episode Checklist) (R4)](https://fhir.epic.com//Sandbox?api=10292)
- [Task.Search (Episode Checklist) (R4)](https://fhir.epic.com//Sandbox?api=10296)
- [Task.Search (Auxiliary Function Notification) (R4)](https://fhir.epic.com//Sandbox?api=11403)
- [Task.Read (Auxiliary Function Notification) (R4)](https://fhir.epic.com//Sandbox?api=11404)

 

 

### 
 UpdateUserDemographics
 [read the spec](https://fhir.epic.com//Sandbox?api=126)

 

 

 

 

 

### 
 Utilization Management
 [read the spec](/Tech/TechSpec?spec=5448)

 

 

 

The CriteriaReview web service retrieves data from a criteria review record. A ReviewCollection groups together CriteriaReview resources that have been created for a patient previously.

 

 

### 
 ValueSet

 

 

 

The ValueSet resource represents a subset of the codes in a code system that is supported by a given server. The $expand operation of the ValueSet resource can be used by a FHIR API consumer to determine what values to expect back from the server as a result of a Read or Search operation and what values they can pass in to the server when performing a Create or Update operation.

Technical Specifications:

- [ValueSet.$expand (Supported Codes) (R4)](https://fhir.epic.com//Sandbox?api=1038)

 

 

### 
 ValueSet.$expand (DTR Payer Guidelines) (R4)
 [read the spec](https://fhir.epic.com//Sandbox?api=11412)

 

 

 

The ValueSet resource represents a subset of the codes in a code system that is supported by a given server. The DTR (Documentation Templates and Rules) $expand operation of the ValueSet resource can be used to dynamically expand value sets referenced in DTR questionnaires, providing a simple collection of codes suitable for use for data entry or validation within documentation requirement workflows. It is important that this is the endpoint used to fetch ValueSets from references that come through during CRD/DTR/PAS related workflows.

The DTR $expand operation response represents a single ValueSet resource, or an OperationOutcome with an error message.

DTR value set expansion only supports querying the ValueSet.$expand operation at the resource type level.