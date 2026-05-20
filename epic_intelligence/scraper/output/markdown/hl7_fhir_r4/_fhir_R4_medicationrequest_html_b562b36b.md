# MedicationRequest - FHIR v4.0.1Identifiers associated with this medication request that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to serverA code specifying the current state of the order.  Generally, this will be active or completed state (this element modifies the meaning of other elements)A coded concept specifying the state of the prescribing event. Describes the lifecycle of the prescription. (Strength=Required)Captures the reason for the current state of the MedicationRequestIdentifies the reasons for a given status. (Strength=Example)Whether the request is a proposal, plan, or an original order (this element modifies the meaning of other elements)The kind of medication order. (Strength=Required)Indicates the type of medication request (for example, where the medication is expected to be consumed or administered (i.e. inpatient or outpatient))A coded concept identifying the category of medication request.  For example, where the medication is to be consumed or administered, or the type of medication treatment. (Strength=Example)Indicates how quickly the Medication Request should be addressed with respect to other requestsIdentifies the level of importance to be assigned to actioning the request. (Strength=Required)If true indicates that the provider is asking for the medication request not to occur (this element modifies the meaning of other elements)Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record.  It may also indicate the source of the reportIdentifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medicationsA coded concept identifying substance or product that can be ordered. (Strength=Example)A link to a resource representing the person or set of individuals to whom the medication will be givenThe Encounter during which this [x] was created or to which the creation of this record is tightly associatedInclude additional information (for example, patient height and weight) that supports the ordering of the medicationThe date (and perhaps time) when the prescription was initially written or authored onThe individual, organization, or device that initiated the request and has responsibility for its activationThe specified desired performer of the medication treatment (e.g. the performer of the medication administration)Indicates the type of performer of the administration of the medicationIdentifies the type of individual that is desired to administer the medication. (Strength=Example)The person who entered the order on behalf of another individual for example in the case of a verbal or a telephone orderThe reason or the indication for ordering or not ordering the medicationA coded concept indicating why the medication was ordered. (Strength=Example)Condition or observation that supports why the medication was orderedThe URL pointing to a protocol, guideline, orderset, or other definition that is adhered to in whole or in part by this MedicationRequestThe URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this MedicationRequestA plan or request that is fulfilled in whole or in part by this medication requestA shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition or prescriptionThe description of the overall patte3rn of the administration of the medication to the patientIdentifies the overall pattern of medication administratio. (Strength=Example)Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be required for delivering the requested serviceExtra information about the prescription that could not be conveyed by the other attributesIndicates how the medication is to be used by the patientA link to a resource representing an earlier order related order or prescriptionIndicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, duplicate therapy, dosage alert etcLinks to Provenance records for past versions of this resource or fulfilling request or event resources that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the resourceThe minimum period of time that must occur between dispenses of the medicationThis indicates the validity period of a prescription (stale dating the Prescription)An integer indicating the number of times, in addition to the original dispense, (aka refills or repeats) that the patient can receive the prescribed medication. Usage Notes: This integer does not include the original order dispense. This means that if an order indicates dispense 30 tablets plus "3 repeats", then the order can be dispensed a total of 4 times and the patient can receive a total of 120 tablets.  A prescriber may explicitly say that zero refills are permitted after the initial dispenseThe amount that is to be dispensed for one fillIdentifies the period time over which the supplied product is expected to be used, or the length of time the dispense is expected to lastIndicates the intended dispensing Organization specified by the prescriberThe amount or quantity to provide as part of the first dispenseThe length of time that the first dispense is expected to lastTrue if the prescriber allows a different drug to be dispensed from what was prescribedIdentifies the type of substitution allowed. (Strength=Example)Indicates the reason for the substitution, or why substitution must or must not be performedA coded concept describing the reason that a different medication should (or should not) be substituted from what was prescribed. (Strength=Example)Indicates the quantity or duration for the first dispense of the medicationIndicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order).  Note that this information is not always sent with the order.  There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy departmentIndicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be doneIdentifiers associated with this medication request that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to serverA code specifying the current state of the order.  Generally, this will be active or completed state (this element modifies the meaning of other elements)A coded concept specifying the state of the prescribing event. Describes the lifecycle of the prescription. (Strength=Required)Captures the reason for the current state of the MedicationRequestIdentifies the reasons for a given status. (Strength=Example)Whether the request is a proposal, plan, or an original order (this element modifies the meaning of other elements)The kind of medication order. (Strength=Required)Indicates the type of medication request (for example, where the medication is expected to be consumed or administered (i.e. inpatient or outpatient))A coded concept identifying the category of medication request.  For example, where the medication is to be consumed or administered, or the type of medication treatment. (Strength=Example)Indicates how quickly the Medication Request should be addressed with respect to other requestsIdentifies the level of importance to be assigned to actioning the request. (Strength=Required)If true indicates that the provider is asking for the medication request not to occur (this element modifies the meaning of other elements)Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record.  It may also indicate the source of the reportIdentifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medicationsA coded concept identifying substance or product that can be ordered. (Strength=Example)A link to a resource representing the person or set of individuals to whom the medication will be givenThe Encounter during which this [x] was created or to which the creation of this record is tightly associatedInclude additional information (for example, patient height and weight) that supports the ordering of the medicationThe date (and perhaps time) when the prescription was initially written or authored onThe individual, organization, or device that initiated the request and has responsibility for its activationThe specified desired performer of the medication treatment (e.g. the performer of the medication administration)Indicates the type of performer of the administration of the medicationIdentifies the type of individual that is desired to administer the medication. (Strength=Example)The person who entered the order on behalf of another individual for example in the case of a verbal or a telephone orderThe reason or the indication for ordering or not ordering the medicationA coded concept indicating why the medication was ordered. (Strength=Example)Condition or observation that supports why the medication was orderedThe URL pointing to a protocol, guideline, orderset, or other definition that is adhered to in whole or in part by this MedicationRequestThe URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this MedicationRequestA plan or request that is fulfilled in whole or in part by this medication requestA shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition or prescriptionThe description of the overall patte3rn of the administration of the medication to the patientIdentifies the overall pattern of medication administratio. (Strength=Example)Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be required for delivering the requested serviceExtra information about the prescription that could not be conveyed by the other attributesIndicates how the medication is to be used by the patientA link to a resource representing an earlier order related order or prescriptionIndicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, duplicate therapy, dosage alert etcLinks to Provenance records for past versions of this resource or fulfilling request or event resources that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the resourceThe minimum period of time that must occur between dispenses of the medicationThis indicates the validity period of a prescription (stale dating the Prescription)An integer indicating the number of times, in addition to the original dispense, (aka refills or repeats) that the patient can receive the prescribed medication. Usage Notes: This integer does not include the original order dispense. This means that if an order indicates dispense 30 tablets plus "3 repeats", then the order can be dispensed a total of 4 times and the patient can receive a total of 120 tablets.  A prescriber may explicitly say that zero refills are permitted after the initial dispenseThe amount that is to be dispensed for one fillIdentifies the period time over which the supplied product is expected to be used, or the length of time the dispense is expected to lastIndicates the intended dispensing Organization specified by the prescriberThe amount or quantity to provide as part of the first dispenseThe length of time that the first dispense is expected to lastTrue if the prescriber allows a different drug to be dispensed from what was prescribedIdentifies the type of substitution allowed. (Strength=Example)Indicates the reason for the substitution, or why substitution must or must not be performedA coded concept describing the reason that a different medication should (or should not) be substituted from what was prescribed. (Strength=Example)Indicates the quantity or duration for the first dispense of the medicationIndicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order).  Note that this information is not always sent with the order.  There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy departmentIndicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be done

> Source: https://hl7.org/fhir/R4/medicationrequest.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/medicationrequest.html) [R4B](http://hl7.org/fhir/R4B/medicationrequest.html) **R4** [R3](http://hl7.org/fhir/STU3/medicationrequest.html)
 

# 11.1 Resource MedicationRequest - Content [
](medicationrequest.html#11.1)

| [Pharmacy ](http://www.hl7.org/Special/committees/medication/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html) | |

An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.

## 11.1.1 Scope and Usage [
](medicationrequest.html#scope)

 This resource covers all type of orders for medications for a patient. This includes inpatient medication orders as well as community orders (whether filled by the prescriber or by a pharmacy). It also includes orders for over-the-counter medications (e.g. Aspirin), total parenteral nutrition and diet/ vitamin supplements. It may be used to support the order of medication-related devices. It is not intended for use in prescribing particular diets, or for ordering non-medication-related items (eyeglasses, supplies, etc.). In addition, the MedicationRequest may be used to report orders/request from external systems that have been reported for informational purposes and are not authoritative and are not expected to be acted upon (e.g. dispensed or administered).

 
The MedicationRequest resource is a "request" resource from a FHIR workflow perspective - see [Workflow Request.](workflow.html#request)

The MedicationRequest resource allows requesting only a single medication.
If a workflow requires requesting multiple items simultaneously, this is done using multiple instances of this resource.
These instances can be linked in different ways, depending on the needs of the workflow. For guidance, refer to [the Request pattern](request.html#compound)

## 11.1.2 Boundaries and Relationships [
](medicationrequest.html#bnr)

 The MedicationRequest resource is used to request or order medication for a subject. It may also be used to report a medication request or order from one organization or source to another. When requesting supplies or devices when there is a patient focus or instructions regarding their use, [SupplyRequest](supplyrequest.html) or [DeviceRequest](devicerequest.html) should be used instead. When reporting on the usage of a medication by a patient, the [MedicationStatement](medicationStatement.html)t resource should be used.

**The Medication domain includes a number of related resources**

 | 
 MedicationRequest | 
 An order for both supply of the medication and the instructions for administration of the medicine to a patient. | 
 |

 | 
 [MedicationDispense](medicationdispense.html) | 
 Provision of a supply of a medication with the intention that it is subsequently consumed by a patient (usually in response to a prescription). | 
 |

 | 
 [MedicationAdministration](medicationadministration.html) | 
 When a patient actually consumes a medicine, or it is otherwise administered to them | 
 |

 | 
 [MedicationStatement](medicationstatement.html) | 
 This is a record of medication being taken by a patient, or that the medication has been given to a patient where the record is the result of a report from the patient, or another clinician.
 A medication statement is not a part of the prescribe->dispense->administer sequence but is a report that such a sequence (or at least a part of it) did take place resulting in a belief that the patient has received a particular medication.
 | 
 |

This resource is referenced by [CarePlan](careplan.html#CarePlan), [Claim](claim.html#Claim), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), itself, [MedicationStatement](medicationstatement.html#MedicationStatement), [Observation](observation.html#Observation) and [ServiceRequest](servicerequest.html#ServiceRequest)

## 11.1.3 
Resource Content
 [
](medicationrequest.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [MedicationRequest](medicationrequest-definitions.html#MedicationRequest) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Ordering of medication for patient or group**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](medicationrequest-definitions.html#MedicationRequest.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | External ids for this request
 | |

| [status](medicationrequest-definitions.html#MedicationRequest.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown
[Medicationrequest status](valueset-medicationrequest-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](medicationrequest-definitions.html#MedicationRequest.statusReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status
[Medication request status reason codes](valueset-medicationrequest-status-reason.html) ([Example](terminologies.html#example)) | |

| [intent](medicationrequest-definitions.html#MedicationRequest.intent) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
[Medication request intent](valueset-medicationrequest-intent.html) ([Required](terminologies.html#required)) | |

| [category](medicationrequest-definitions.html#MedicationRequest.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of medication usage
[Medication request category codes](valueset-medicationrequest-category.html) ([Example](terminologies.html#example))
 | |

| [priority](medicationrequest-definitions.html#MedicationRequest.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | True if request is prohibiting action | |

| [reported[x]](medicationrequest-definitions.html#MedicationRequest.reported_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Reported rather than primary record | |

| reportedBoolean | | | [boolean](datatypes.html#boolean) | | |

| reportedReference | | | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | | |

| [medication[x]](medicationrequest-definitions.html#MedicationRequest.medication_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | | Medication to be taken
[SNOMED CT Medication Codes](valueset-medication-codes.html) ([Example](terminologies.html#example)) | |

| medicationCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| medicationReference | | | [Reference](references.html#Reference)([Medication](medication.html)) | | |

| [subject](medicationrequest-definitions.html#MedicationRequest.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who or group medication request is for | |

| [encounter](medicationrequest-definitions.html#MedicationRequest.encounter) | | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of encounter/admission/stay | |

| [supportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Information to support ordering of the medication
 | |

| [authoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When request was initially authored | |

| [requester](medicationrequest-definitions.html#MedicationRequest.requester) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Device](device.html)) | Who/What requested the Request | |

| [performer](medicationrequest-definitions.html#MedicationRequest.performer) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html) | [CareTeam](careteam.html)) | Intended performer of administration | |

| [performerType](medicationrequest-definitions.html#MedicationRequest.performerType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Desired kind of performer of the medication administration
[Procedure Performer Role Codes](valueset-performer-role.html) ([Example](terminologies.html#example)) | |

| [recorder](medicationrequest-definitions.html#MedicationRequest.recorder) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Person who entered the request | |

| [reasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Reason or indication for ordering or not ordering the medication
[Condition/Problem/Diagnosis Codes](valueset-condition-code.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference) | | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html)) | Condition or observation that supports why the prescription is being written
 | |

| [instantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [canonical](datatypes.html#canonical)() | Instantiates FHIR protocol or definition
 | |

| [instantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [uri](datatypes.html#uri) | Instantiates external protocol or definition
 | |

| [basedOn](medicationrequest-definitions.html#MedicationRequest.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CarePlan](careplan.html) | [MedicationRequest](medicationrequest.html) | [ServiceRequest](servicerequest.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | What request fulfills
 | |

| [groupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Composite request this is part of | |

| [courseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Overall pattern of medication administration
[Medication request course of therapy codes](valueset-medicationrequest-course-of-therapy.html) ([Example](terminologies.html#example)) | |

| [insurance](medicationrequest-definitions.html#MedicationRequest.insurance) | | 0..* | [Reference](references.html#Reference)([Coverage](coverage.html) | [ClaimResponse](claimresponse.html)) | Associated insurance coverage
 | |

| [note](medicationrequest-definitions.html#MedicationRequest.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Information about the prescription
 | |

| [dosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction) | | 0..* | [Dosage](dosage.html#Dosage) | How the medication should be taken
 | |

| [dispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest) | | 0..1 | [BackboneElement](backboneelement.html) | Medication supply authorization | |

| [initialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill) | | 0..1 | [BackboneElement](backboneelement.html) | First fill details | |

| [quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | First fill quantity | |

| [duration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration) | | 0..1 | [Duration](datatypes.html#Duration) | First fill duration | |

| [dispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval) | | 0..1 | [Duration](datatypes.html#Duration) | Minimum period of time between dispenses | |

| [validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod) | | 0..1 | [Period](datatypes.html#Period) | Time period supply is authorized for | |

| [numberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) | | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Number of refills authorized | |

| [quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Amount of medication to supply per dispense | |

| [expectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration) | | 0..1 | [Duration](datatypes.html#Duration) | Number of days supply per dispense | |

| [performer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Intended dispenser | |

| [substitution](medicationrequest-definitions.html#MedicationRequest.substitution) | | 0..1 | [BackboneElement](backboneelement.html) | Any restrictions on medication substitution | |

| [allowed[x]](medicationrequest-definitions.html#MedicationRequest.substitution.allowed_x_) | | 1..1 | | Whether substitution is allowed or not
[V3 Value SetActSubstanceAdminSubstitutionCode](v3/ActSubstanceAdminSubstitutionCode/vs.html) ([Example](terminologies.html#example)) | |

| allowedBoolean | | | [boolean](datatypes.html#boolean) | | |

| allowedCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| [reason](medicationrequest-definitions.html#MedicationRequest.substitution.reason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why should (not) substitution be made
[V3 Value SetSubstanceAdminSubstitutionReason](v3/SubstanceAdminSubstitutionReason/vs.html) ([Example](terminologies.html#example)) | |

| [priorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription) | | 0..1 | [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html)) | An order/prescription that is being replaced | |

| [detectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue) | | 0..* | [Reference](references.html#Reference)([DetectedIssue](detectedissue.html)) | Clinical Issue with action
 | |

| [eventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory) | | 0..* | [Reference](references.html#Reference)([Provenance](provenance.html)) | A list of events of interest in the lifecycle
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - MedicationRequest ([DomainResource](domainresource.html))[Identifiers associated with this medication request that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to serveridentifier](medicationrequest-definitions.html#MedicationRequest.identifier) : [Identifier](datatypes.html#Identifier) [0..*][A code specifying the current state of the order. Generally, this will be active or completed state (this element modifies the meaning of other elements)status](medicationrequest-definitions.html#MedicationRequest.status) : [code](datatypes.html#code) [1..1] « [A coded concept specifying the state of the prescribing event. Describes the lifecycle of the prescription. (Strength=Required)medicationrequest Status](valueset-medicationrequest-status.html)! »[Captures the reason for the current state of the MedicationRequeststatusReason](medicationrequest-definitions.html#MedicationRequest.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identifies the reasons for a given status. (Strength=Example)medicationRequest Status](valueset-medicationrequest-status-reason.html) [ Reas...](valueset-medicationrequest-status-reason.html)?? »[Whether the request is a proposal, plan, or an original order (this element modifies the meaning of other elements)intent](medicationrequest-definitions.html#MedicationRequest.intent) : [code](datatypes.html#code) [1..1] « [The kind of medication order. (Strength=Required)medicationRequest Intent](valueset-medicationrequest-intent.html)! »[Indicates the type of medication request (for example, where the medication is expected to be consumed or administered (i.e. inpatient or outpatient))category](medicationrequest-definitions.html#MedicationRequest.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [A coded concept identifying the category of medication request. For example, where the medication is to be consumed or administered, or the type of medication treatment. (Strength=Example)medicationRequest Category ](valueset-medicationrequest-category.html)?? »[Indicates how quickly the Medication Request should be addressed with respect to other requestspriority](medicationrequest-definitions.html#MedicationRequest.priority) : [code](datatypes.html#code) [0..1] « [Identifies the level of importance to be assigned to actioning the request. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[If true indicates that the provider is asking for the medication request not to occur (this element modifies the meaning of other elements)doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform) : [boolean](datatypes.html#boolean) [0..1][Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record. It may also indicate the source of the reportreported[x]](medicationrequest-definitions.html#MedicationRequest.reported_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) »[Identifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medicationsmedication[x]](medicationrequest-definitions.html#MedicationRequest.medication_x_) : [Type](formats.html#umlchoice) [1..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Medication](medication.html#Medication)); [A coded concept identifying substance or product that can be ordered. (Strength=Example)](valueset-medication-codes.html) [SNOMEDCTMedicationCodes](valueset-medication-codes.html)?? »[A link to a resource representing the person or set of individuals to whom the medication will be givensubject](medicationrequest-definitions.html#MedicationRequest.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this [x] was created or to which the creation of this record is tightly associatedencounter](medicationrequest-definitions.html#MedicationRequest.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Include additional information (for example, patient height and weight) that supports the ordering of the medicationsupportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[The date (and perhaps time) when the prescription was initially written or authored onauthoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn) : [dateTime](datatypes.html#dateTime) [0..1][The individual, organization, or device that initiated the request and has responsibility for its activationrequester](medicationrequest-definitions.html#MedicationRequest.requester) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device) »[The specified desired performer of the medication treatment (e.g. the performer of the medication administration)performer](medicationrequest-definitions.html#MedicationRequest.performer) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam) »[Indicates the type of performer of the administration of the medicationperformerType](medicationrequest-definitions.html#MedicationRequest.performerType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identifies the type of individual that is desired to administer the medication. (Strength=Example)ProcedurePerformerRoleCodes](valueset-performer-role.html)?? »[The person who entered the order on behalf of another individual for example in the case of a verbal or a telephone orderrecorder](medicationrequest-definitions.html#MedicationRequest.recorder) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[The reason or the indication for ordering or not ordering the medicationreasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [A coded concept indicating why the medication was ordered. (Strength=Example)](valueset-condition-code.html) [Condition/Problem/DiagnosisCo...](valueset-condition-code.html)?? »[Condition or observation that supports why the medication was orderedreasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation) »[The URL pointing to a protocol, guideline, orderset, or other definition that is adhered to in whole or in part by this MedicationRequestinstantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..*] « »[The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this MedicationRequestinstantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) : [uri](datatypes.html#uri) [0..*][A plan or request that is fulfilled in whole or in part by this medication requestbasedOn](medicationrequest-definitions.html#MedicationRequest.basedOn) : [Reference](references.html#Reference) [0..*] « [CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)| [ServiceRequest](servicerequest.html#ServiceRequest)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation) »[A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition or prescriptiongroupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][The description of the overall patte3rn of the administration of the medication to the patientcourseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identifies the overall pattern of medication administratio. (Strength=Example)medicationRequest](valueset-medicationrequest-course-of-therapy.html) [ Course of T...](valueset-medicationrequest-course-of-therapy.html)?? »[Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be required for delivering the requested serviceinsurance](medicationrequest-definitions.html#MedicationRequest.insurance) : [Reference](references.html#Reference) [0..*] « [Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse) »[Extra information about the prescription that could not be conveyed by the other attributesnote](medicationrequest-definitions.html#MedicationRequest.note) : [Annotation](datatypes.html#Annotation) [0..*][Indicates how the medication is to be used by the patientdosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction) : [Dosage](dosage.html#Dosage) [0..*][A link to a resource representing an earlier order related order or prescriptionpriorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription) : [Reference](references.html#Reference) [0..1] « [MedicationRequest](medicationrequest.html#MedicationRequest) »[Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, duplicate therapy, dosage alert etcdetectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue) : [Reference](references.html#Reference) [0..*] « [DetectedIssue](detectedissue.html#DetectedIssue) »[Links to Provenance records for past versions of this resource or fulfilling request or event resources that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the resourceeventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory) : [Reference](references.html#Reference) [0..*] « [Provenance](provenance.html#Provenance) »DispenseRequest[The minimum period of time that must occur between dispenses of the medicationdispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval) : [Duration](datatypes.html#Duration) [0..1][This indicates the validity period of a prescription (stale dating the Prescription)validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod) : [Period](datatypes.html#Period) [0..1][An integer indicating the number of times, in addition to the original dispense, (aka refills or repeats) that the patient can receive the prescribed medication. Usage Notes: This integer does not include the original order dispense. This means that if an order indicates dispense 30 tablets plus "3 repeats", then the order can be dispensed a total of 4 times and the patient can receive a total of 120 tablets. A prescriber may explicitly say that zero refills are permitted after the initial dispensenumberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) : [unsignedInt](datatypes.html#unsignedInt) [0..1][The amount that is to be dispensed for one fillquantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][Identifies the period time over which the supplied product is expected to be used, or the length of time the dispense is expected to lastexpectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration) : [Duration](datatypes.html#Duration) [0..1][Indicates the intended dispensing Organization specified by the prescriberperformer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »InitialFill[The amount or quantity to provide as part of the first dispensequantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][The length of time that the first dispense is expected to lastduration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration) : [Duration](datatypes.html#Duration) [0..1]Substitution[True if the prescriber allows a different drug to be dispensed from what was prescribedallowed[x]](medicationrequest-definitions.html#MedicationRequest.substitution.allowed_x_) : [Type](formats.html#umlchoice) [1..1] « [boolean](datatypes.html#boolean)|[CodeableConcept](datatypes.html#CodeableConcept); [Identifies the type of substitution allowed. (Strength=Example)](v3/ActSubstanceAdminSubstitutionCode/vs.html) [v3.ActSubstanceAdminSubstitut...](v3/ActSubstanceAdminSubstitutionCode/vs.html)?? »[Indicates the reason for the substitution, or why substitution must or must not be performedreason](medicationrequest-definitions.html#MedicationRequest.substitution.reason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A coded concept describing the reason that a different medication should (or should not) be substituted from what was prescribed. (Strength=Example)v3.SubstanceAdminSubstitution...](v3/SubstanceAdminSubstitutionReason/vs.html)?? »
[Indicates the quantity or duration for the first dispense of the medicationinitialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill)[0..1][Indicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order). Note that this information is not always sent with the order. There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy departmentdispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest)[0..1][Indicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be donesubstitution](medicationrequest-definitions.html#MedicationRequest.substitution)[0..1]
 

 

 

**XML Template**

 

 
```
<[**MedicationRequest**](medicationrequest-definitions.html#MedicationRequest) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](medicationrequest-definitions.html#MedicationRequest.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External ids for this request](terminologies.html#unbound) --></identifier>
 <[**status**](medicationrequest-definitions.html#MedicationRequest.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown](valueset-medicationrequest-status.html) -->
 <[**statusReason**](medicationrequest-definitions.html#MedicationRequest.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](valueset-medicationrequest-status-reason.html) --></statusReason>
 <[**intent**](medicationrequest-definitions.html#MedicationRequest.intent) value="[[code](datatypes.html#code)]"/><!-- **1..1** [proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-medicationrequest-intent.html) -->
 <[**category**](medicationrequest-definitions.html#MedicationRequest.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Type of medication usage](valueset-medicationrequest-category.html) --></category>
 <[**priority**](medicationrequest-definitions.html#MedicationRequest.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**doNotPerform**](medicationrequest-definitions.html#MedicationRequest.doNotPerform) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [True if request is prohibiting action](terminologies.html#unbound) -->
 <[**reported[x]**](medicationrequest-definitions.html#MedicationRequest.reported[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Reported rather than primary record](terminologies.html#unbound) --></reported[x]>
 <[**medication[x]**](medicationrequest-definitions.html#MedicationRequest.medication[x])><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Medication](medication.html#Medication)) [Medication to be taken](valueset-medication-codes.html) --></medication[x]>
 <[**subject**](medicationrequest-definitions.html#MedicationRequest.subject)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Who or group medication request is for](terminologies.html#unbound) --></subject>
 <[**encounter**](medicationrequest-definitions.html#MedicationRequest.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of encounter/admission/stay](terminologies.html#unbound) --></encounter>
 <[**supportingInformation**](medicationrequest-definitions.html#MedicationRequest.supportingInformation)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Information to support ordering of the medication](terminologies.html#unbound) --></supportingInformation>
 <[**authoredOn**](medicationrequest-definitions.html#MedicationRequest.authoredOn) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When request was initially authored](terminologies.html#unbound) -->
 <[**requester**](medicationrequest-definitions.html#MedicationRequest.requester)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) [Who/What requested the Request](terminologies.html#unbound) --></requester>
 <[**performer**](medicationrequest-definitions.html#MedicationRequest.performer)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam)) [Intended performer of administration](terminologies.html#unbound) --></performer>
 <[**performerType**](medicationrequest-definitions.html#MedicationRequest.performerType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Desired kind of performer of the medication administration](valueset-performer-role.html) --></performerType>
 <[**recorder**](medicationrequest-definitions.html#MedicationRequest.recorder)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [Person who entered the request](terminologies.html#unbound) --></recorder>
 <[**reasonCode**](medicationrequest-definitions.html#MedicationRequest.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Reason or indication for ordering or not ordering the medication](valueset-condition-code.html) --></reasonCode>
 <[**reasonReference**](medicationrequest-definitions.html#MedicationRequest.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)) [Condition or observation that supports why the prescription is being written](terminologies.html#unbound) --></reasonReference>
 <[**instantiatesCanonical**](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) value="[[canonical](datatypes.html#canonical)]"/><!-- **0..*** [Instantiates FHIR protocol or definition](terminologies.html#unbound) -->
 <[**instantiatesUri**](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Instantiates external protocol or definition](terminologies.html#unbound) -->
 <[**basedOn**](medicationrequest-definitions.html#MedicationRequest.basedOn)><!-- **0..*** [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[ServiceRequest](servicerequest.html#ServiceRequest)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) [What request fulfills](terminologies.html#unbound) --></basedOn>
 <[**groupIdentifier**](medicationrequest-definitions.html#MedicationRequest.groupIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Composite request this is part of](terminologies.html#unbound) --></groupIdentifier>
 <[**courseOfTherapyType**](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Overall pattern of medication administration](valueset-medicationrequest-course-of-therapy.html) --></courseOfTherapyType>
 <[**insurance**](medicationrequest-definitions.html#MedicationRequest.insurance)><!-- **0..*** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) [Associated insurance coverage](terminologies.html#unbound) --></insurance>
 <[**note**](medicationrequest-definitions.html#MedicationRequest.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Information about the prescription](terminologies.html#unbound) --></note>
 <[**dosageInstruction**](medicationrequest-definitions.html#MedicationRequest.dosageInstruction)><!-- **0..*** [Dosage](dosage.html#Dosage) [How the medication should be taken](terminologies.html#unbound) --></dosageInstruction>
 <[**dispenseRequest**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest)> <!-- **0..1** Medication supply authorization -->
 <[**initialFill**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill)> <!-- **0..1** First fill details -->
 <[**quantity**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [First fill quantity](terminologies.html#unbound) --></quantity>
 <[**duration**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration)><!-- **0..1** [Duration](datatypes.html#Duration) [First fill duration](terminologies.html#unbound) --></duration>
 </initialFill>
 <[**dispenseInterval**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval)><!-- **0..1** [Duration](datatypes.html#Duration) [Minimum period of time between dispenses](terminologies.html#unbound) --></dispenseInterval>
 <[**validityPeriod**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod)><!-- **0..1** [Period](datatypes.html#Period) [Time period supply is authorized for](terminologies.html#unbound) --></validityPeriod>
 <[**numberOfRepeatsAllowed**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) value="[[unsignedInt](datatypes.html#unsignedInt)]"/><!-- **0..1** [Number of refills authorized](terminologies.html#unbound) -->
 <[**quantity**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Amount of medication to supply per dispense](terminologies.html#unbound) --></quantity>
 <[**expectedSupplyDuration**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration)><!-- **0..1** [Duration](datatypes.html#Duration) [Number of days supply per dispense](terminologies.html#unbound) --></expectedSupplyDuration>
 <[**performer**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Intended dispenser](terminologies.html#unbound) --></performer>
 </dispenseRequest>
 <[**substitution**](medicationrequest-definitions.html#MedicationRequest.substitution)> <!-- **0..1** Any restrictions on medication substitution -->
 <[**allowed[x]**](medicationrequest-definitions.html#MedicationRequest.substitution.allowed[x])><!-- **1..1** [boolean](datatypes.html#boolean)|[CodeableConcept](datatypes.html#CodeableConcept) [Whether substitution is allowed or not](v3/ActSubstanceAdminSubstitutionCode/vs.html) --></allowed[x]>
 <[**reason**](medicationrequest-definitions.html#MedicationRequest.substitution.reason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Why should (not) substitution be made](v3/SubstanceAdminSubstitutionReason/vs.html) --></reason>
 </substitution>
 <[**priorPrescription**](medicationrequest-definitions.html#MedicationRequest.priorPrescription)><!-- **0..1** [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html#MedicationRequest)) [An order/prescription that is being replaced](terminologies.html#unbound) --></priorPrescription>
 <[**detectedIssue**](medicationrequest-definitions.html#MedicationRequest.detectedIssue)><!-- **0..*** [Reference](references.html#Reference)([DetectedIssue](detectedissue.html#DetectedIssue)) [Clinical Issue with action](terminologies.html#unbound) --></detectedIssue>
 <[**eventHistory**](medicationrequest-definitions.html#MedicationRequest.eventHistory)><!-- **0..*** [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) [A list of events of interest in the lifecycle](terminologies.html#unbound) --></eventHistory>
</MedicationRequest>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**MedicationRequest**](medicationrequest-definitions.html#MedicationRequest)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](medicationrequest-definitions.html#MedicationRequest.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External ids for this request](terminologies.html#unbound)
 "[status](medicationrequest-definitions.html#MedicationRequest.status)" : "<[code](datatypes.html#code)>", // **R!** [active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown](valueset-medicationrequest-status.html)
 "[statusReason](medicationrequest-definitions.html#MedicationRequest.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](valueset-medicationrequest-status-reason.html)
 "[intent](medicationrequest-definitions.html#MedicationRequest.intent)" : "<[code](datatypes.html#code)>", // **R!** [proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-medicationrequest-intent.html)
 "[category](medicationrequest-definitions.html#MedicationRequest.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Type of medication usage](valueset-medicationrequest-category.html)
 "[priority](medicationrequest-definitions.html#MedicationRequest.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform)" : <[boolean](datatypes.html#boolean)>, // [True if request is prohibiting action](terminologies.html#unbound)
 // reported[x]: Reported rather than primary record. One of these 2:
 "[reportedBoolean](medicationrequest-definitions.html#MedicationRequest.reportedBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[reportedReference](medicationrequest-definitions.html#MedicationRequest.reportedReference)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) },
 // medication[x]: Medication to be taken. One of these 2:
 "[medicationCodeableConcept](medicationrequest-definitions.html#MedicationRequest.medicationCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[medicationReference](medicationrequest-definitions.html#MedicationRequest.medicationReference)" : { [Reference](references.html#Reference)([Medication](medication.html#Medication)) },
 "[subject](medicationrequest-definitions.html#MedicationRequest.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Who or group medication request is for](terminologies.html#unbound)
 "[encounter](medicationrequest-definitions.html#MedicationRequest.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of encounter/admission/stay](terminologies.html#unbound)
 "[supportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Information to support ordering of the medication](terminologies.html#unbound)
 "[authoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn)" : "<[dateTime](datatypes.html#dateTime)>", // [When request was initially authored](terminologies.html#unbound)
 "[requester](medicationrequest-definitions.html#MedicationRequest.requester)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) }, // [Who/What requested the Request](terminologies.html#unbound)
 "[performer](medicationrequest-definitions.html#MedicationRequest.performer)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam)) }, // [Intended performer of administration](terminologies.html#unbound)
 "[performerType](medicationrequest-definitions.html#MedicationRequest.performerType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Desired kind of performer of the medication administration](valueset-performer-role.html)
 "[recorder](medicationrequest-definitions.html#MedicationRequest.recorder)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [Person who entered the request](terminologies.html#unbound)
 "[reasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Reason or indication for ordering or not ordering the medication](valueset-condition-code.html)
 "[reasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)) }], // [Condition or observation that supports why the prescription is being written](terminologies.html#unbound)
 "[instantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical)" : ["<[canonical](datatypes.html#canonical)>"], // [Instantiates FHIR protocol or definition](terminologies.html#unbound)
 "[instantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri)" : ["<[uri](datatypes.html#uri)>"], // [Instantiates external protocol or definition](terminologies.html#unbound)
 "[basedOn](medicationrequest-definitions.html#MedicationRequest.basedOn)" : [{ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[ServiceRequest](servicerequest.html#ServiceRequest)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) }], // [What request fulfills](terminologies.html#unbound)
 "[groupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Composite request this is part of](terminologies.html#unbound)
 "[courseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Overall pattern of medication administration](valueset-medicationrequest-course-of-therapy.html)
 "[insurance](medicationrequest-definitions.html#MedicationRequest.insurance)" : [{ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) }], // [Associated insurance coverage](terminologies.html#unbound)
 "[note](medicationrequest-definitions.html#MedicationRequest.note)" : [{ [Annotation](datatypes.html#Annotation) }], // [Information about the prescription](terminologies.html#unbound)
 "[dosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction)" : [{ [Dosage](dosage.html#Dosage) }], // [How the medication should be taken](terminologies.html#unbound)
 "[dispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest)" : { // [Medication supply authorization](terminologies.html#unbound)
 "[initialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill)" : { // [First fill details](terminologies.html#unbound)
 "[quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [First fill quantity](terminologies.html#unbound)
 "[duration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration)" : { [Duration](datatypes.html#Duration) } // [First fill duration](terminologies.html#unbound)
 },
 "[dispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval)" : { [Duration](datatypes.html#Duration) }, // [Minimum period of time between dispenses](terminologies.html#unbound)
 "[validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod)" : { [Period](datatypes.html#Period) }, // [Time period supply is authorized for](terminologies.html#unbound)
 "[numberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed)" : "<[unsignedInt](datatypes.html#unsignedInt)>", // [Number of refills authorized](terminologies.html#unbound)
 "[quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Amount of medication to supply per dispense](terminologies.html#unbound)
 "[expectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration)" : { [Duration](datatypes.html#Duration) }, // [Number of days supply per dispense](terminologies.html#unbound)
 "[performer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) } // [Intended dispenser](terminologies.html#unbound)
 },
 "[substitution](medicationrequest-definitions.html#MedicationRequest.substitution)" : { // [Any restrictions on medication substitution](terminologies.html#unbound)
 // allowed[x]: Whether substitution is allowed or not. One of these 2:
 "[allowedBoolean](medicationrequest-definitions.html#MedicationRequest.substitution.allowedBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[allowedCodeableConcept](medicationrequest-definitions.html#MedicationRequest.substitution.allowedCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[reason](medicationrequest-definitions.html#MedicationRequest.substitution.reason)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Why should (not) substitution be made](v3/SubstanceAdminSubstitutionReason/vs.html)
 },
 "[priorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription)" : { [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html#MedicationRequest)) }, // [An order/prescription that is being replaced](terminologies.html#unbound)
 "[detectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue)" : [{ [Reference](references.html#Reference)([DetectedIssue](detectedissue.html#DetectedIssue)) }], // [Clinical Issue with action](terminologies.html#unbound)
 "[eventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory)" : [{ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) }] // [A list of events of interest in the lifecycle](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**MedicationRequest**](medicationrequest-definitions.html#MedicationRequest);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[MedicationRequest.identifier](medicationrequest-definitions.html#MedicationRequest.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External ids for this request
 fhir:[MedicationRequest.status](medicationrequest-definitions.html#MedicationRequest.status) [ [code](datatypes.html#code) ]; # 1..1 active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown
 fhir:[MedicationRequest.statusReason](medicationrequest-definitions.html#MedicationRequest.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[MedicationRequest.intent](medicationrequest-definitions.html#MedicationRequest.intent) [ [code](datatypes.html#code) ]; # 1..1 proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
 fhir:[MedicationRequest.category](medicationrequest-definitions.html#MedicationRequest.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Type of medication usage
 fhir:[MedicationRequest.priority](medicationrequest-definitions.html#MedicationRequest.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[MedicationRequest.doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform) [ [boolean](datatypes.html#boolean) ]; # 0..1 True if request is prohibiting action
 # [MedicationRequest.reported[x]](medicationrequest-definitions.html#MedicationRequest.reported[x]) : 0..1 Reported rather than primary record. One of these 2
 fhir:[MedicationRequest.reportedBoolean](medicationrequest-definitions.html#MedicationRequest.reportedBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[MedicationRequest.reportedReference](medicationrequest-definitions.html#MedicationRequest.reportedReference) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]
 # [MedicationRequest.medication[x]](medicationrequest-definitions.html#MedicationRequest.medication[x]) : 1..1 Medication to be taken. One of these 2
 fhir:[MedicationRequest.medicationCodeableConcept](medicationrequest-definitions.html#MedicationRequest.medicationCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[MedicationRequest.medicationReference](medicationrequest-definitions.html#MedicationRequest.medicationReference) [ [Reference](references.html#Reference)([Medication](medication.html#Medication)) ]
 fhir:[MedicationRequest.subject](medicationrequest-definitions.html#MedicationRequest.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Who or group medication request is for
 fhir:[MedicationRequest.encounter](medicationrequest-definitions.html#MedicationRequest.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of encounter/admission/stay
 fhir:[MedicationRequest.supportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Information to support ordering of the medication
 fhir:[MedicationRequest.authoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When request was initially authored
 fhir:[MedicationRequest.requester](medicationrequest-definitions.html#MedicationRequest.requester) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) ]; # 0..1 Who/What requested the Request
 fhir:[MedicationRequest.performer](medicationrequest-definitions.html#MedicationRequest.performer) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam)) ]; # 0..1 Intended performer of administration
 fhir:[MedicationRequest.performerType](medicationrequest-definitions.html#MedicationRequest.performerType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Desired kind of performer of the medication administration
 fhir:[MedicationRequest.recorder](medicationrequest-definitions.html#MedicationRequest.recorder) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 Person who entered the request
 fhir:[MedicationRequest.reasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Reason or indication for ordering or not ordering the medication
 fhir:[MedicationRequest.reasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)) ], ... ; # 0..* Condition or observation that supports why the prescription is being written
 fhir:[MedicationRequest.instantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) [ [canonical](datatypes.html#canonical) ], ... ; # 0..* Instantiates FHIR protocol or definition
 fhir:[MedicationRequest.instantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Instantiates external protocol or definition
 fhir:[MedicationRequest.basedOn](medicationrequest-definitions.html#MedicationRequest.basedOn) [ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[ServiceRequest](servicerequest.html#ServiceRequest)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) ], ... ; # 0..* What request fulfills
 fhir:[MedicationRequest.groupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Composite request this is part of
 fhir:[MedicationRequest.courseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Overall pattern of medication administration
 fhir:[MedicationRequest.insurance](medicationrequest-definitions.html#MedicationRequest.insurance) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) ], ... ; # 0..* Associated insurance coverage
 fhir:[MedicationRequest.note](medicationrequest-definitions.html#MedicationRequest.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Information about the prescription
 fhir:[MedicationRequest.dosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction) [ [Dosage](dosage.html#Dosage) ], ... ; # 0..* How the medication should be taken
 fhir:[MedicationRequest.dispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest) [ # 0..1 Medication supply authorization
 fhir:[MedicationRequest.dispenseRequest.initialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill) [ # 0..1 First fill details
 fhir:[MedicationRequest.dispenseRequest.initialFill.quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 First fill quantity
 fhir:[MedicationRequest.dispenseRequest.initialFill.duration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration) [ [Duration](datatypes.html#Duration) ]; # 0..1 First fill duration
 ];
 fhir:[MedicationRequest.dispenseRequest.dispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval) [ [Duration](datatypes.html#Duration) ]; # 0..1 Minimum period of time between dispenses
 fhir:[MedicationRequest.dispenseRequest.validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Time period supply is authorized for
 fhir:[MedicationRequest.dispenseRequest.numberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) [ [unsignedInt](datatypes.html#unsignedInt) ]; # 0..1 Number of refills authorized
 fhir:[MedicationRequest.dispenseRequest.quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Amount of medication to supply per dispense
 fhir:[MedicationRequest.dispenseRequest.expectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration) [ [Duration](datatypes.html#Duration) ]; # 0..1 Number of days supply per dispense
 fhir:[MedicationRequest.dispenseRequest.performer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Intended dispenser
 ];
 fhir:[MedicationRequest.substitution](medicationrequest-definitions.html#MedicationRequest.substitution) [ # 0..1 Any restrictions on medication substitution
 # [MedicationRequest.substitution.allowed[x]](medicationrequest-definitions.html#MedicationRequest.substitution.allowed[x]) : 1..1 Whether substitution is allowed or not. One of these 2
 fhir:[MedicationRequest.substitution.allowedBoolean](medicationrequest-definitions.html#MedicationRequest.substitution.allowedBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[MedicationRequest.substitution.allowedCodeableConcept](medicationrequest-definitions.html#MedicationRequest.substitution.allowedCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[MedicationRequest.substitution.reason](medicationrequest-definitions.html#MedicationRequest.substitution.reason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Why should (not) substitution be made
 ];
 fhir:[MedicationRequest.priorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription) [ [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html#MedicationRequest)) ]; # 0..1 An order/prescription that is being replaced
 fhir:[MedicationRequest.detectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue) [ [Reference](references.html#Reference)([DetectedIssue](detectedissue.html#DetectedIssue)) ], ... ; # 0..* Clinical Issue with action
 fhir:[MedicationRequest.eventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory) [ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) ], ... ; # 0..* A list of events of interest in the lifecycle
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [MedicationRequest](medicationrequest.html#MedicationRequest)
 | 
 | 
 |

 | 
 MedicationRequest.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/medication-request-status to http://hl7.org/fhir/ValueSet/medicationrequest-status|4.0.1

 

 | 
 |

 | 
 MedicationRequest.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.intent | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/medication-request-intent to http://hl7.org/fhir/ValueSet/medicationrequest-intent|4.0.1

 

 | 
 |

 | 
 MedicationRequest.category | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 MedicationRequest.priority | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/medication-request-priority to http://hl7.org/fhir/ValueSet/request-priority|4.0.1

 

 | 
 |

 | 
 MedicationRequest.doNotPerform | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.reported[x] | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.requester | 
 
 

 - Type changed from BackboneElement to Reference(Practitioner | PractitionerRole | Organization | Patient | RelatedPerson | Device)

 

 | 
 |

 | 
 MedicationRequest.performer | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.performerType | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.recorder | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 MedicationRequest.instantiatesCanonical | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.basedOn | 
 
 

 - Type Reference: Added Target Types ServiceRequest, ImmunizationRecommendation

 - Type Reference: Removed Target Types ProcedureRequest, ReferralRequest

 

 | 
 |

 | 
 MedicationRequest.courseOfTherapyType | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.insurance | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.initialFill | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.initialFill.quantity | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.initialFill.duration | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.dispenseInterval | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.numberOfRepeatsAllowed | 
 
 

 - Type changed from positiveInt to unsignedInt

 

 | 
 |

 | 
 MedicationRequest.substitution.allowed[x] | 
 
 

 - Renamed from allowed to allowed[x]

 - Add Type CodeableConcept

 - No longer marked as Modifier

 

 | 
 |

 | 
 MedicationRequest.definition | 
 
 

 - deleted

 

 | 
 |

 | 
 MedicationRequest.context | 
 
 

 - deleted

 

 | 
 |

 | 
 MedicationRequest.requester.agent | 
 
 

 - deleted

 

 | 
 |

 | 
 MedicationRequest.requester.onBehalfOf | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](medicationrequest.diff.xml) or [JSON](medicationrequest.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](medicationrequest-version-maps.html) (status = 36 tests that all execute ok. 8 fail round-trip testing and 36 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [MedicationRequest](medicationrequest-definitions.html#MedicationRequest) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Ordering of medication for patient or group**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](medicationrequest-definitions.html#MedicationRequest.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | External ids for this request
 | |

| [status](medicationrequest-definitions.html#MedicationRequest.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown
[Medicationrequest status](valueset-medicationrequest-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](medicationrequest-definitions.html#MedicationRequest.statusReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status
[Medication request status reason codes](valueset-medicationrequest-status-reason.html) ([Example](terminologies.html#example)) | |

| [intent](medicationrequest-definitions.html#MedicationRequest.intent) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
[Medication request intent](valueset-medicationrequest-intent.html) ([Required](terminologies.html#required)) | |

| [category](medicationrequest-definitions.html#MedicationRequest.category) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of medication usage
[Medication request category codes](valueset-medicationrequest-category.html) ([Example](terminologies.html#example))
 | |

| [priority](medicationrequest-definitions.html#MedicationRequest.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | True if request is prohibiting action | |

| [reported[x]](medicationrequest-definitions.html#MedicationRequest.reported_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | Reported rather than primary record | |

| reportedBoolean | | | [boolean](datatypes.html#boolean) | | |

| reportedReference | | | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | | |

| [medication[x]](medicationrequest-definitions.html#MedicationRequest.medication_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | | Medication to be taken
[SNOMED CT Medication Codes](valueset-medication-codes.html) ([Example](terminologies.html#example)) | |

| medicationCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| medicationReference | | | [Reference](references.html#Reference)([Medication](medication.html)) | | |

| [subject](medicationrequest-definitions.html#MedicationRequest.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who or group medication request is for | |

| [encounter](medicationrequest-definitions.html#MedicationRequest.encounter) | | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of encounter/admission/stay | |

| [supportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Information to support ordering of the medication
 | |

| [authoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | When request was initially authored | |

| [requester](medicationrequest-definitions.html#MedicationRequest.requester) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Device](device.html)) | Who/What requested the Request | |

| [performer](medicationrequest-definitions.html#MedicationRequest.performer) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html) | [CareTeam](careteam.html)) | Intended performer of administration | |

| [performerType](medicationrequest-definitions.html#MedicationRequest.performerType) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Desired kind of performer of the medication administration
[Procedure Performer Role Codes](valueset-performer-role.html) ([Example](terminologies.html#example)) | |

| [recorder](medicationrequest-definitions.html#MedicationRequest.recorder) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Person who entered the request | |

| [reasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Reason or indication for ordering or not ordering the medication
[Condition/Problem/Diagnosis Codes](valueset-condition-code.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference) | | 0..* | [Reference](references.html#Reference)([Condition](condition.html) | [Observation](observation.html)) | Condition or observation that supports why the prescription is being written
 | |

| [instantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [canonical](datatypes.html#canonical)() | Instantiates FHIR protocol or definition
 | |

| [instantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [uri](datatypes.html#uri) | Instantiates external protocol or definition
 | |

| [basedOn](medicationrequest-definitions.html#MedicationRequest.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([CarePlan](careplan.html) | [MedicationRequest](medicationrequest.html) | [ServiceRequest](servicerequest.html) | [ImmunizationRecommendation](immunizationrecommendation.html)) | What request fulfills
 | |

| [groupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Composite request this is part of | |

| [courseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Overall pattern of medication administration
[Medication request course of therapy codes](valueset-medicationrequest-course-of-therapy.html) ([Example](terminologies.html#example)) | |

| [insurance](medicationrequest-definitions.html#MedicationRequest.insurance) | | 0..* | [Reference](references.html#Reference)([Coverage](coverage.html) | [ClaimResponse](claimresponse.html)) | Associated insurance coverage
 | |

| [note](medicationrequest-definitions.html#MedicationRequest.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Information about the prescription
 | |

| [dosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction) | | 0..* | [Dosage](dosage.html#Dosage) | How the medication should be taken
 | |

| [dispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest) | | 0..1 | [BackboneElement](backboneelement.html) | Medication supply authorization | |

| [initialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill) | | 0..1 | [BackboneElement](backboneelement.html) | First fill details | |

| [quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | First fill quantity | |

| [duration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration) | | 0..1 | [Duration](datatypes.html#Duration) | First fill duration | |

| [dispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval) | | 0..1 | [Duration](datatypes.html#Duration) | Minimum period of time between dispenses | |

| [validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod) | | 0..1 | [Period](datatypes.html#Period) | Time period supply is authorized for | |

| [numberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) | | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Number of refills authorized | |

| [quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Amount of medication to supply per dispense | |

| [expectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration) | | 0..1 | [Duration](datatypes.html#Duration) | Number of days supply per dispense | |

| [performer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Intended dispenser | |

| [substitution](medicationrequest-definitions.html#MedicationRequest.substitution) | | 0..1 | [BackboneElement](backboneelement.html) | Any restrictions on medication substitution | |

| [allowed[x]](medicationrequest-definitions.html#MedicationRequest.substitution.allowed_x_) | | 1..1 | | Whether substitution is allowed or not
[V3 Value SetActSubstanceAdminSubstitutionCode](v3/ActSubstanceAdminSubstitutionCode/vs.html) ([Example](terminologies.html#example)) | |

| allowedBoolean | | | [boolean](datatypes.html#boolean) | | |

| allowedCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| [reason](medicationrequest-definitions.html#MedicationRequest.substitution.reason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why should (not) substitution be made
[V3 Value SetSubstanceAdminSubstitutionReason](v3/SubstanceAdminSubstitutionReason/vs.html) ([Example](terminologies.html#example)) | |

| [priorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription) | | 0..1 | [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html)) | An order/prescription that is being replaced | |

| [detectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue) | | 0..* | [Reference](references.html#Reference)([DetectedIssue](detectedissue.html)) | Clinical Issue with action
 | |

| [eventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory) | | 0..* | [Reference](references.html#Reference)([Provenance](provenance.html)) | A list of events of interest in the lifecycle
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - MedicationRequest ([DomainResource](domainresource.html))[Identifiers associated with this medication request that are defined by business processes and/or used to refer to it when a direct URL reference to the resource itself is not appropriate. They are business identifiers assigned to this resource by the performer or other systems and remain constant as the resource is updated and propagates from server to serveridentifier](medicationrequest-definitions.html#MedicationRequest.identifier) : [Identifier](datatypes.html#Identifier) [0..*][A code specifying the current state of the order. Generally, this will be active or completed state (this element modifies the meaning of other elements)status](medicationrequest-definitions.html#MedicationRequest.status) : [code](datatypes.html#code) [1..1] « [A coded concept specifying the state of the prescribing event. Describes the lifecycle of the prescription. (Strength=Required)medicationrequest Status](valueset-medicationrequest-status.html)! »[Captures the reason for the current state of the MedicationRequeststatusReason](medicationrequest-definitions.html#MedicationRequest.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identifies the reasons for a given status. (Strength=Example)medicationRequest Status](valueset-medicationrequest-status-reason.html) [ Reas...](valueset-medicationrequest-status-reason.html)?? »[Whether the request is a proposal, plan, or an original order (this element modifies the meaning of other elements)intent](medicationrequest-definitions.html#MedicationRequest.intent) : [code](datatypes.html#code) [1..1] « [The kind of medication order. (Strength=Required)medicationRequest Intent](valueset-medicationrequest-intent.html)! »[Indicates the type of medication request (for example, where the medication is expected to be consumed or administered (i.e. inpatient or outpatient))category](medicationrequest-definitions.html#MedicationRequest.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [A coded concept identifying the category of medication request. For example, where the medication is to be consumed or administered, or the type of medication treatment. (Strength=Example)medicationRequest Category ](valueset-medicationrequest-category.html)?? »[Indicates how quickly the Medication Request should be addressed with respect to other requestspriority](medicationrequest-definitions.html#MedicationRequest.priority) : [code](datatypes.html#code) [0..1] « [Identifies the level of importance to be assigned to actioning the request. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[If true indicates that the provider is asking for the medication request not to occur (this element modifies the meaning of other elements)doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform) : [boolean](datatypes.html#boolean) [0..1][Indicates if this record was captured as a secondary 'reported' record rather than as an original primary source-of-truth record. It may also indicate the source of the reportreported[x]](medicationrequest-definitions.html#MedicationRequest.reported_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) »[Identifies the medication being requested. This is a link to a resource that represents the medication which may be the details of the medication or simply an attribute carrying a code that identifies the medication from a known list of medicationsmedication[x]](medicationrequest-definitions.html#MedicationRequest.medication_x_) : [Type](formats.html#umlchoice) [1..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Medication](medication.html#Medication)); [A coded concept identifying substance or product that can be ordered. (Strength=Example)](valueset-medication-codes.html) [SNOMEDCTMedicationCodes](valueset-medication-codes.html)?? »[A link to a resource representing the person or set of individuals to whom the medication will be givensubject](medicationrequest-definitions.html#MedicationRequest.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this [x] was created or to which the creation of this record is tightly associatedencounter](medicationrequest-definitions.html#MedicationRequest.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Include additional information (for example, patient height and weight) that supports the ordering of the medicationsupportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[The date (and perhaps time) when the prescription was initially written or authored onauthoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn) : [dateTime](datatypes.html#dateTime) [0..1][The individual, organization, or device that initiated the request and has responsibility for its activationrequester](medicationrequest-definitions.html#MedicationRequest.requester) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device) »[The specified desired performer of the medication treatment (e.g. the performer of the medication administration)performer](medicationrequest-definitions.html#MedicationRequest.performer) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam) »[Indicates the type of performer of the administration of the medicationperformerType](medicationrequest-definitions.html#MedicationRequest.performerType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identifies the type of individual that is desired to administer the medication. (Strength=Example)ProcedurePerformerRoleCodes](valueset-performer-role.html)?? »[The person who entered the order on behalf of another individual for example in the case of a verbal or a telephone orderrecorder](medicationrequest-definitions.html#MedicationRequest.recorder) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[The reason or the indication for ordering or not ordering the medicationreasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [A coded concept indicating why the medication was ordered. (Strength=Example)](valueset-condition-code.html) [Condition/Problem/DiagnosisCo...](valueset-condition-code.html)?? »[Condition or observation that supports why the medication was orderedreasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition)|[Observation](observation.html#Observation) »[The URL pointing to a protocol, guideline, orderset, or other definition that is adhered to in whole or in part by this MedicationRequestinstantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..*] « »[The URL pointing to an externally maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this MedicationRequestinstantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) : [uri](datatypes.html#uri) [0..*][A plan or request that is fulfilled in whole or in part by this medication requestbasedOn](medicationrequest-definitions.html#MedicationRequest.basedOn) : [Reference](references.html#Reference) [0..*] « [CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)| [ServiceRequest](servicerequest.html#ServiceRequest)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation) »[A shared identifier common to all requests that were authorized more or less simultaneously by a single author, representing the identifier of the requisition or prescriptiongroupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][The description of the overall patte3rn of the administration of the medication to the patientcourseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Identifies the overall pattern of medication administratio. (Strength=Example)medicationRequest](valueset-medicationrequest-course-of-therapy.html) [ Course of T...](valueset-medicationrequest-course-of-therapy.html)?? »[Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be required for delivering the requested serviceinsurance](medicationrequest-definitions.html#MedicationRequest.insurance) : [Reference](references.html#Reference) [0..*] « [Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse) »[Extra information about the prescription that could not be conveyed by the other attributesnote](medicationrequest-definitions.html#MedicationRequest.note) : [Annotation](datatypes.html#Annotation) [0..*][Indicates how the medication is to be used by the patientdosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction) : [Dosage](dosage.html#Dosage) [0..*][A link to a resource representing an earlier order related order or prescriptionpriorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription) : [Reference](references.html#Reference) [0..1] « [MedicationRequest](medicationrequest.html#MedicationRequest) »[Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, duplicate therapy, dosage alert etcdetectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue) : [Reference](references.html#Reference) [0..*] « [DetectedIssue](detectedissue.html#DetectedIssue) »[Links to Provenance records for past versions of this resource or fulfilling request or event resources that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the resourceeventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory) : [Reference](references.html#Reference) [0..*] « [Provenance](provenance.html#Provenance) »DispenseRequest[The minimum period of time that must occur between dispenses of the medicationdispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval) : [Duration](datatypes.html#Duration) [0..1][This indicates the validity period of a prescription (stale dating the Prescription)validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod) : [Period](datatypes.html#Period) [0..1][An integer indicating the number of times, in addition to the original dispense, (aka refills or repeats) that the patient can receive the prescribed medication. Usage Notes: This integer does not include the original order dispense. This means that if an order indicates dispense 30 tablets plus "3 repeats", then the order can be dispensed a total of 4 times and the patient can receive a total of 120 tablets. A prescriber may explicitly say that zero refills are permitted after the initial dispensenumberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) : [unsignedInt](datatypes.html#unsignedInt) [0..1][The amount that is to be dispensed for one fillquantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][Identifies the period time over which the supplied product is expected to be used, or the length of time the dispense is expected to lastexpectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration) : [Duration](datatypes.html#Duration) [0..1][Indicates the intended dispensing Organization specified by the prescriberperformer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »InitialFill[The amount or quantity to provide as part of the first dispensequantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][The length of time that the first dispense is expected to lastduration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration) : [Duration](datatypes.html#Duration) [0..1]Substitution[True if the prescriber allows a different drug to be dispensed from what was prescribedallowed[x]](medicationrequest-definitions.html#MedicationRequest.substitution.allowed_x_) : [Type](formats.html#umlchoice) [1..1] « [boolean](datatypes.html#boolean)|[CodeableConcept](datatypes.html#CodeableConcept); [Identifies the type of substitution allowed. (Strength=Example)](v3/ActSubstanceAdminSubstitutionCode/vs.html) [v3.ActSubstanceAdminSubstitut...](v3/ActSubstanceAdminSubstitutionCode/vs.html)?? »[Indicates the reason for the substitution, or why substitution must or must not be performedreason](medicationrequest-definitions.html#MedicationRequest.substitution.reason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A coded concept describing the reason that a different medication should (or should not) be substituted from what was prescribed. (Strength=Example)v3.SubstanceAdminSubstitution...](v3/SubstanceAdminSubstitutionReason/vs.html)?? »
[Indicates the quantity or duration for the first dispense of the medicationinitialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill)[0..1][Indicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order). Note that this information is not always sent with the order. There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy departmentdispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest)[0..1][Indicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be donesubstitution](medicationrequest-definitions.html#MedicationRequest.substitution)[0..1]
 

**XML Template**

 

 
```
<[**MedicationRequest**](medicationrequest-definitions.html#MedicationRequest) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](medicationrequest-definitions.html#MedicationRequest.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External ids for this request](terminologies.html#unbound) --></identifier>
 <[**status**](medicationrequest-definitions.html#MedicationRequest.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown](valueset-medicationrequest-status.html) -->
 <[**statusReason**](medicationrequest-definitions.html#MedicationRequest.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](valueset-medicationrequest-status-reason.html) --></statusReason>
 <[**intent**](medicationrequest-definitions.html#MedicationRequest.intent) value="[[code](datatypes.html#code)]"/><!-- **1..1** [proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-medicationrequest-intent.html) -->
 <[**category**](medicationrequest-definitions.html#MedicationRequest.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Type of medication usage](valueset-medicationrequest-category.html) --></category>
 <[**priority**](medicationrequest-definitions.html#MedicationRequest.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**doNotPerform**](medicationrequest-definitions.html#MedicationRequest.doNotPerform) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [True if request is prohibiting action](terminologies.html#unbound) -->
 <[**reported[x]**](medicationrequest-definitions.html#MedicationRequest.reported[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Reported rather than primary record](terminologies.html#unbound) --></reported[x]>
 <[**medication[x]**](medicationrequest-definitions.html#MedicationRequest.medication[x])><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Medication](medication.html#Medication)) [Medication to be taken](valueset-medication-codes.html) --></medication[x]>
 <[**subject**](medicationrequest-definitions.html#MedicationRequest.subject)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Who or group medication request is for](terminologies.html#unbound) --></subject>
 <[**encounter**](medicationrequest-definitions.html#MedicationRequest.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of encounter/admission/stay](terminologies.html#unbound) --></encounter>
 <[**supportingInformation**](medicationrequest-definitions.html#MedicationRequest.supportingInformation)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Information to support ordering of the medication](terminologies.html#unbound) --></supportingInformation>
 <[**authoredOn**](medicationrequest-definitions.html#MedicationRequest.authoredOn) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When request was initially authored](terminologies.html#unbound) -->
 <[**requester**](medicationrequest-definitions.html#MedicationRequest.requester)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) [Who/What requested the Request](terminologies.html#unbound) --></requester>
 <[**performer**](medicationrequest-definitions.html#MedicationRequest.performer)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam)) [Intended performer of administration](terminologies.html#unbound) --></performer>
 <[**performerType**](medicationrequest-definitions.html#MedicationRequest.performerType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Desired kind of performer of the medication administration](valueset-performer-role.html) --></performerType>
 <[**recorder**](medicationrequest-definitions.html#MedicationRequest.recorder)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [Person who entered the request](terminologies.html#unbound) --></recorder>
 <[**reasonCode**](medicationrequest-definitions.html#MedicationRequest.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Reason or indication for ordering or not ordering the medication](valueset-condition-code.html) --></reasonCode>
 <[**reasonReference**](medicationrequest-definitions.html#MedicationRequest.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)) [Condition or observation that supports why the prescription is being written](terminologies.html#unbound) --></reasonReference>
 <[**instantiatesCanonical**](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) value="[[canonical](datatypes.html#canonical)]"/><!-- **0..*** [Instantiates FHIR protocol or definition](terminologies.html#unbound) -->
 <[**instantiatesUri**](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Instantiates external protocol or definition](terminologies.html#unbound) -->
 <[**basedOn**](medicationrequest-definitions.html#MedicationRequest.basedOn)><!-- **0..*** [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[ServiceRequest](servicerequest.html#ServiceRequest)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) [What request fulfills](terminologies.html#unbound) --></basedOn>
 <[**groupIdentifier**](medicationrequest-definitions.html#MedicationRequest.groupIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Composite request this is part of](terminologies.html#unbound) --></groupIdentifier>
 <[**courseOfTherapyType**](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Overall pattern of medication administration](valueset-medicationrequest-course-of-therapy.html) --></courseOfTherapyType>
 <[**insurance**](medicationrequest-definitions.html#MedicationRequest.insurance)><!-- **0..*** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) [Associated insurance coverage](terminologies.html#unbound) --></insurance>
 <[**note**](medicationrequest-definitions.html#MedicationRequest.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Information about the prescription](terminologies.html#unbound) --></note>
 <[**dosageInstruction**](medicationrequest-definitions.html#MedicationRequest.dosageInstruction)><!-- **0..*** [Dosage](dosage.html#Dosage) [How the medication should be taken](terminologies.html#unbound) --></dosageInstruction>
 <[**dispenseRequest**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest)> <!-- **0..1** Medication supply authorization -->
 <[**initialFill**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill)> <!-- **0..1** First fill details -->
 <[**quantity**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [First fill quantity](terminologies.html#unbound) --></quantity>
 <[**duration**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration)><!-- **0..1** [Duration](datatypes.html#Duration) [First fill duration](terminologies.html#unbound) --></duration>
 </initialFill>
 <[**dispenseInterval**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval)><!-- **0..1** [Duration](datatypes.html#Duration) [Minimum period of time between dispenses](terminologies.html#unbound) --></dispenseInterval>
 <[**validityPeriod**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod)><!-- **0..1** [Period](datatypes.html#Period) [Time period supply is authorized for](terminologies.html#unbound) --></validityPeriod>
 <[**numberOfRepeatsAllowed**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) value="[[unsignedInt](datatypes.html#unsignedInt)]"/><!-- **0..1** [Number of refills authorized](terminologies.html#unbound) -->
 <[**quantity**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Amount of medication to supply per dispense](terminologies.html#unbound) --></quantity>
 <[**expectedSupplyDuration**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration)><!-- **0..1** [Duration](datatypes.html#Duration) [Number of days supply per dispense](terminologies.html#unbound) --></expectedSupplyDuration>
 <[**performer**](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Intended dispenser](terminologies.html#unbound) --></performer>
 </dispenseRequest>
 <[**substitution**](medicationrequest-definitions.html#MedicationRequest.substitution)> <!-- **0..1** Any restrictions on medication substitution -->
 <[**allowed[x]**](medicationrequest-definitions.html#MedicationRequest.substitution.allowed[x])><!-- **1..1** [boolean](datatypes.html#boolean)|[CodeableConcept](datatypes.html#CodeableConcept) [Whether substitution is allowed or not](v3/ActSubstanceAdminSubstitutionCode/vs.html) --></allowed[x]>
 <[**reason**](medicationrequest-definitions.html#MedicationRequest.substitution.reason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Why should (not) substitution be made](v3/SubstanceAdminSubstitutionReason/vs.html) --></reason>
 </substitution>
 <[**priorPrescription**](medicationrequest-definitions.html#MedicationRequest.priorPrescription)><!-- **0..1** [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html#MedicationRequest)) [An order/prescription that is being replaced](terminologies.html#unbound) --></priorPrescription>
 <[**detectedIssue**](medicationrequest-definitions.html#MedicationRequest.detectedIssue)><!-- **0..*** [Reference](references.html#Reference)([DetectedIssue](detectedissue.html#DetectedIssue)) [Clinical Issue with action](terminologies.html#unbound) --></detectedIssue>
 <[**eventHistory**](medicationrequest-definitions.html#MedicationRequest.eventHistory)><!-- **0..*** [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) [A list of events of interest in the lifecycle](terminologies.html#unbound) --></eventHistory>
</MedicationRequest>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**MedicationRequest**](medicationrequest-definitions.html#MedicationRequest)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](medicationrequest-definitions.html#MedicationRequest.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External ids for this request](terminologies.html#unbound)
 "[status](medicationrequest-definitions.html#MedicationRequest.status)" : "<[code](datatypes.html#code)>", // **R!** [active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown](valueset-medicationrequest-status.html)
 "[statusReason](medicationrequest-definitions.html#MedicationRequest.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](valueset-medicationrequest-status-reason.html)
 "[intent](medicationrequest-definitions.html#MedicationRequest.intent)" : "<[code](datatypes.html#code)>", // **R!** [proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-medicationrequest-intent.html)
 "[category](medicationrequest-definitions.html#MedicationRequest.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Type of medication usage](valueset-medicationrequest-category.html)
 "[priority](medicationrequest-definitions.html#MedicationRequest.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform)" : <[boolean](datatypes.html#boolean)>, // [True if request is prohibiting action](terminologies.html#unbound)
 // reported[x]: Reported rather than primary record. One of these 2:
 "[reportedBoolean](medicationrequest-definitions.html#MedicationRequest.reportedBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[reportedReference](medicationrequest-definitions.html#MedicationRequest.reportedReference)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) },
 // medication[x]: Medication to be taken. One of these 2:
 "[medicationCodeableConcept](medicationrequest-definitions.html#MedicationRequest.medicationCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[medicationReference](medicationrequest-definitions.html#MedicationRequest.medicationReference)" : { [Reference](references.html#Reference)([Medication](medication.html#Medication)) },
 "[subject](medicationrequest-definitions.html#MedicationRequest.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Who or group medication request is for](terminologies.html#unbound)
 "[encounter](medicationrequest-definitions.html#MedicationRequest.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of encounter/admission/stay](terminologies.html#unbound)
 "[supportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Information to support ordering of the medication](terminologies.html#unbound)
 "[authoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn)" : "<[dateTime](datatypes.html#dateTime)>", // [When request was initially authored](terminologies.html#unbound)
 "[requester](medicationrequest-definitions.html#MedicationRequest.requester)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) }, // [Who/What requested the Request](terminologies.html#unbound)
 "[performer](medicationrequest-definitions.html#MedicationRequest.performer)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam)) }, // [Intended performer of administration](terminologies.html#unbound)
 "[performerType](medicationrequest-definitions.html#MedicationRequest.performerType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Desired kind of performer of the medication administration](valueset-performer-role.html)
 "[recorder](medicationrequest-definitions.html#MedicationRequest.recorder)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [Person who entered the request](terminologies.html#unbound)
 "[reasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Reason or indication for ordering or not ordering the medication](valueset-condition-code.html)
 "[reasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)) }], // [Condition or observation that supports why the prescription is being written](terminologies.html#unbound)
 "[instantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical)" : ["<[canonical](datatypes.html#canonical)>"], // [Instantiates FHIR protocol or definition](terminologies.html#unbound)
 "[instantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri)" : ["<[uri](datatypes.html#uri)>"], // [Instantiates external protocol or definition](terminologies.html#unbound)
 "[basedOn](medicationrequest-definitions.html#MedicationRequest.basedOn)" : [{ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[ServiceRequest](servicerequest.html#ServiceRequest)|
 [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) }], // [What request fulfills](terminologies.html#unbound)
 "[groupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Composite request this is part of](terminologies.html#unbound)
 "[courseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Overall pattern of medication administration](valueset-medicationrequest-course-of-therapy.html)
 "[insurance](medicationrequest-definitions.html#MedicationRequest.insurance)" : [{ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) }], // [Associated insurance coverage](terminologies.html#unbound)
 "[note](medicationrequest-definitions.html#MedicationRequest.note)" : [{ [Annotation](datatypes.html#Annotation) }], // [Information about the prescription](terminologies.html#unbound)
 "[dosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction)" : [{ [Dosage](dosage.html#Dosage) }], // [How the medication should be taken](terminologies.html#unbound)
 "[dispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest)" : { // [Medication supply authorization](terminologies.html#unbound)
 "[initialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill)" : { // [First fill details](terminologies.html#unbound)
 "[quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [First fill quantity](terminologies.html#unbound)
 "[duration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration)" : { [Duration](datatypes.html#Duration) } // [First fill duration](terminologies.html#unbound)
 },
 "[dispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval)" : { [Duration](datatypes.html#Duration) }, // [Minimum period of time between dispenses](terminologies.html#unbound)
 "[validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod)" : { [Period](datatypes.html#Period) }, // [Time period supply is authorized for](terminologies.html#unbound)
 "[numberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed)" : "<[unsignedInt](datatypes.html#unsignedInt)>", // [Number of refills authorized](terminologies.html#unbound)
 "[quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Amount of medication to supply per dispense](terminologies.html#unbound)
 "[expectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration)" : { [Duration](datatypes.html#Duration) }, // [Number of days supply per dispense](terminologies.html#unbound)
 "[performer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) } // [Intended dispenser](terminologies.html#unbound)
 },
 "[substitution](medicationrequest-definitions.html#MedicationRequest.substitution)" : { // [Any restrictions on medication substitution](terminologies.html#unbound)
 // allowed[x]: Whether substitution is allowed or not. One of these 2:
 "[allowedBoolean](medicationrequest-definitions.html#MedicationRequest.substitution.allowedBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[allowedCodeableConcept](medicationrequest-definitions.html#MedicationRequest.substitution.allowedCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[reason](medicationrequest-definitions.html#MedicationRequest.substitution.reason)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Why should (not) substitution be made](v3/SubstanceAdminSubstitutionReason/vs.html)
 },
 "[priorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription)" : { [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html#MedicationRequest)) }, // [An order/prescription that is being replaced](terminologies.html#unbound)
 "[detectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue)" : [{ [Reference](references.html#Reference)([DetectedIssue](detectedissue.html#DetectedIssue)) }], // [Clinical Issue with action](terminologies.html#unbound)
 "[eventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory)" : [{ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) }] // [A list of events of interest in the lifecycle](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**MedicationRequest**](medicationrequest-definitions.html#MedicationRequest);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[MedicationRequest.identifier](medicationrequest-definitions.html#MedicationRequest.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External ids for this request
 fhir:[MedicationRequest.status](medicationrequest-definitions.html#MedicationRequest.status) [ [code](datatypes.html#code) ]; # 1..1 active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown
 fhir:[MedicationRequest.statusReason](medicationrequest-definitions.html#MedicationRequest.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[MedicationRequest.intent](medicationrequest-definitions.html#MedicationRequest.intent) [ [code](datatypes.html#code) ]; # 1..1 proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
 fhir:[MedicationRequest.category](medicationrequest-definitions.html#MedicationRequest.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Type of medication usage
 fhir:[MedicationRequest.priority](medicationrequest-definitions.html#MedicationRequest.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[MedicationRequest.doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform) [ [boolean](datatypes.html#boolean) ]; # 0..1 True if request is prohibiting action
 # [MedicationRequest.reported[x]](medicationrequest-definitions.html#MedicationRequest.reported[x]) : 0..1 Reported rather than primary record. One of these 2
 fhir:[MedicationRequest.reportedBoolean](medicationrequest-definitions.html#MedicationRequest.reportedBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[MedicationRequest.reportedReference](medicationrequest-definitions.html#MedicationRequest.reportedReference) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]
 # [MedicationRequest.medication[x]](medicationrequest-definitions.html#MedicationRequest.medication[x]) : 1..1 Medication to be taken. One of these 2
 fhir:[MedicationRequest.medicationCodeableConcept](medicationrequest-definitions.html#MedicationRequest.medicationCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[MedicationRequest.medicationReference](medicationrequest-definitions.html#MedicationRequest.medicationReference) [ [Reference](references.html#Reference)([Medication](medication.html#Medication)) ]
 fhir:[MedicationRequest.subject](medicationrequest-definitions.html#MedicationRequest.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Who or group medication request is for
 fhir:[MedicationRequest.encounter](medicationrequest-definitions.html#MedicationRequest.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of encounter/admission/stay
 fhir:[MedicationRequest.supportingInformation](medicationrequest-definitions.html#MedicationRequest.supportingInformation) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Information to support ordering of the medication
 fhir:[MedicationRequest.authoredOn](medicationrequest-definitions.html#MedicationRequest.authoredOn) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When request was initially authored
 fhir:[MedicationRequest.requester](medicationrequest-definitions.html#MedicationRequest.requester) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Device](device.html#Device)) ]; # 0..1 Who/What requested the Request
 fhir:[MedicationRequest.performer](medicationrequest-definitions.html#MedicationRequest.performer) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)|[CareTeam](careteam.html#CareTeam)) ]; # 0..1 Intended performer of administration
 fhir:[MedicationRequest.performerType](medicationrequest-definitions.html#MedicationRequest.performerType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Desired kind of performer of the medication administration
 fhir:[MedicationRequest.recorder](medicationrequest-definitions.html#MedicationRequest.recorder) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 Person who entered the request
 fhir:[MedicationRequest.reasonCode](medicationrequest-definitions.html#MedicationRequest.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Reason or indication for ordering or not ordering the medication
 fhir:[MedicationRequest.reasonReference](medicationrequest-definitions.html#MedicationRequest.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)|[Observation](observation.html#Observation)) ], ... ; # 0..* Condition or observation that supports why the prescription is being written
 fhir:[MedicationRequest.instantiatesCanonical](medicationrequest-definitions.html#MedicationRequest.instantiatesCanonical) [ [canonical](datatypes.html#canonical) ], ... ; # 0..* Instantiates FHIR protocol or definition
 fhir:[MedicationRequest.instantiatesUri](medicationrequest-definitions.html#MedicationRequest.instantiatesUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Instantiates external protocol or definition
 fhir:[MedicationRequest.basedOn](medicationrequest-definitions.html#MedicationRequest.basedOn) [ [Reference](references.html#Reference)([CarePlan](careplan.html#CarePlan)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[ServiceRequest](servicerequest.html#ServiceRequest)|[ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation)) ], ... ; # 0..* What request fulfills
 fhir:[MedicationRequest.groupIdentifier](medicationrequest-definitions.html#MedicationRequest.groupIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Composite request this is part of
 fhir:[MedicationRequest.courseOfTherapyType](medicationrequest-definitions.html#MedicationRequest.courseOfTherapyType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Overall pattern of medication administration
 fhir:[MedicationRequest.insurance](medicationrequest-definitions.html#MedicationRequest.insurance) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) ], ... ; # 0..* Associated insurance coverage
 fhir:[MedicationRequest.note](medicationrequest-definitions.html#MedicationRequest.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Information about the prescription
 fhir:[MedicationRequest.dosageInstruction](medicationrequest-definitions.html#MedicationRequest.dosageInstruction) [ [Dosage](dosage.html#Dosage) ], ... ; # 0..* How the medication should be taken
 fhir:[MedicationRequest.dispenseRequest](medicationrequest-definitions.html#MedicationRequest.dispenseRequest) [ # 0..1 Medication supply authorization
 fhir:[MedicationRequest.dispenseRequest.initialFill](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill) [ # 0..1 First fill details
 fhir:[MedicationRequest.dispenseRequest.initialFill.quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 First fill quantity
 fhir:[MedicationRequest.dispenseRequest.initialFill.duration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.initialFill.duration) [ [Duration](datatypes.html#Duration) ]; # 0..1 First fill duration
 ];
 fhir:[MedicationRequest.dispenseRequest.dispenseInterval](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.dispenseInterval) [ [Duration](datatypes.html#Duration) ]; # 0..1 Minimum period of time between dispenses
 fhir:[MedicationRequest.dispenseRequest.validityPeriod](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.validityPeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Time period supply is authorized for
 fhir:[MedicationRequest.dispenseRequest.numberOfRepeatsAllowed](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.numberOfRepeatsAllowed) [ [unsignedInt](datatypes.html#unsignedInt) ]; # 0..1 Number of refills authorized
 fhir:[MedicationRequest.dispenseRequest.quantity](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Amount of medication to supply per dispense
 fhir:[MedicationRequest.dispenseRequest.expectedSupplyDuration](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.expectedSupplyDuration) [ [Duration](datatypes.html#Duration) ]; # 0..1 Number of days supply per dispense
 fhir:[MedicationRequest.dispenseRequest.performer](medicationrequest-definitions.html#MedicationRequest.dispenseRequest.performer) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Intended dispenser
 ];
 fhir:[MedicationRequest.substitution](medicationrequest-definitions.html#MedicationRequest.substitution) [ # 0..1 Any restrictions on medication substitution
 # [MedicationRequest.substitution.allowed[x]](medicationrequest-definitions.html#MedicationRequest.substitution.allowed[x]) : 1..1 Whether substitution is allowed or not. One of these 2
 fhir:[MedicationRequest.substitution.allowedBoolean](medicationrequest-definitions.html#MedicationRequest.substitution.allowedBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[MedicationRequest.substitution.allowedCodeableConcept](medicationrequest-definitions.html#MedicationRequest.substitution.allowedCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[MedicationRequest.substitution.reason](medicationrequest-definitions.html#MedicationRequest.substitution.reason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Why should (not) substitution be made
 ];
 fhir:[MedicationRequest.priorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription) [ [Reference](references.html#Reference)([MedicationRequest](medicationrequest.html#MedicationRequest)) ]; # 0..1 An order/prescription that is being replaced
 fhir:[MedicationRequest.detectedIssue](medicationrequest-definitions.html#MedicationRequest.detectedIssue) [ [Reference](references.html#Reference)([DetectedIssue](detectedissue.html#DetectedIssue)) ], ... ; # 0..* Clinical Issue with action
 fhir:[MedicationRequest.eventHistory](medicationrequest-definitions.html#MedicationRequest.eventHistory) [ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) ], ... ; # 0..* A list of events of interest in the lifecycle
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [MedicationRequest](medicationrequest.html#MedicationRequest)
 | 
 | 
 |

 | 
 MedicationRequest.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/medication-request-status to http://hl7.org/fhir/ValueSet/medicationrequest-status|4.0.1

 

 | 
 |

 | 
 MedicationRequest.statusReason | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.intent | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/medication-request-intent to http://hl7.org/fhir/ValueSet/medicationrequest-intent|4.0.1

 

 | 
 |

 | 
 MedicationRequest.category | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 MedicationRequest.priority | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/medication-request-priority to http://hl7.org/fhir/ValueSet/request-priority|4.0.1

 

 | 
 |

 | 
 MedicationRequest.doNotPerform | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.reported[x] | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.requester | 
 
 

 - Type changed from BackboneElement to Reference(Practitioner | PractitionerRole | Organization | Patient | RelatedPerson | Device)

 

 | 
 |

 | 
 MedicationRequest.performer | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.performerType | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.recorder | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 MedicationRequest.instantiatesCanonical | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.basedOn | 
 
 

 - Type Reference: Added Target Types ServiceRequest, ImmunizationRecommendation

 - Type Reference: Removed Target Types ProcedureRequest, ReferralRequest

 

 | 
 |

 | 
 MedicationRequest.courseOfTherapyType | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.insurance | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.initialFill | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.initialFill.quantity | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.initialFill.duration | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.dispenseInterval | 
 
 

 - Added Element

 

 | 
 |

 | 
 MedicationRequest.dispenseRequest.numberOfRepeatsAllowed | 
 
 

 - Type changed from positiveInt to unsignedInt

 

 | 
 |

 | 
 MedicationRequest.substitution.allowed[x] | 
 
 

 - Renamed from allowed to allowed[x]

 - Add Type CodeableConcept

 - No longer marked as Modifier

 

 | 
 |

 | 
 MedicationRequest.definition | 
 
 

 - deleted

 

 | 
 |

 | 
 MedicationRequest.context | 
 
 

 - deleted

 

 | 
 |

 | 
 MedicationRequest.requester.agent | 
 
 

 - deleted

 

 | 
 |

 | 
 MedicationRequest.requester.onBehalfOf | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](medicationrequest.diff.xml) or [JSON](medicationrequest.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](medicationrequest-version-maps.html) (status = 36 tests that all execute ok. 8 fail round-trip testing and 36 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](medicationrequest-profiles.html) and the alternate definitions:
Master Definition [XML](medicationrequest.profile.xml.html) + [JSON](medicationrequest.profile.json.html),
[XML](xml.html) [Schema](medicationrequest.xsd)/[Schematron](medicationrequest.sch) + [JSON](json.html) 
[Schema](medicationrequest.schema.json.html), [ShEx](medicationrequest.shex.html) (for [Turtle](rdf.html)) + [see the extensions](medicationrequest-profiles.html) & the [dependency analysis](medicationrequest-dependencies.html)

### 11.1.3.1 
Terminology Bindings
 [
](medicationrequest.html#tx)

 | Path | Definition | Type | Reference | |

 | MedicationRequest.status | A coded concept specifying the state of the prescribing event. Describes the lifecycle of the prescription. | [Required](terminologies.html#required) | [medicationrequest Status](valueset-medicationrequest-status.html) | |

 | MedicationRequest.statusReason | Identifies the reasons for a given status. | [Example](terminologies.html#example) | [medicationRequest Status Reason Codes](valueset-medicationrequest-status-reason.html) | |

 | MedicationRequest.intent | The kind of medication order. | [Required](terminologies.html#required) | [medicationRequest Intent](valueset-medicationrequest-intent.html) | |

 | MedicationRequest.category | A coded concept identifying the category of medication request. For example, where the medication is to be consumed or administered, or the type of medication treatment. | [Example](terminologies.html#example) | [medicationRequest Category Codes](valueset-medicationrequest-category.html) | |

 | MedicationRequest.priority | Identifies the level of importance to be assigned to actioning the request. | [Required](terminologies.html#required) | [RequestPriority](valueset-request-priority.html) | |

 | MedicationRequest.medication[x] | A coded concept identifying substance or product that can be ordered. | [Example](terminologies.html#example) | [SNOMEDCTMedicationCodes](valueset-medication-codes.html) | |

 | MedicationRequest.performerType | Identifies the type of individual that is desired to administer the medication. | [Example](terminologies.html#example) | [ProcedurePerformerRoleCodes](valueset-performer-role.html) | |

 | MedicationRequest.reasonCode | A coded concept indicating why the medication was ordered. | [Example](terminologies.html#example) | [Condition/Problem/DiagnosisCodes](valueset-condition-code.html) | |

 | MedicationRequest.courseOfTherapyType | Identifies the overall pattern of medication administratio. | [Example](terminologies.html#example) | [medicationRequest Course of Therapy Codes](valueset-medicationrequest-course-of-therapy.html) | |

 | MedicationRequest.substitution.allowed[x] | Identifies the type of substitution allowed. | [Example](terminologies.html#example) | [v3.ActSubstanceAdminSubstitutionCode](v3/ActSubstanceAdminSubstitutionCode/vs.html) | |

 | MedicationRequest.substitution.reason | A coded concept describing the reason that a different medication should (or should not) be substituted from what was prescribed. | [Example](terminologies.html#example) | [v3.SubstanceAdminSubstitutionReason](v3/SubstanceAdminSubstitutionReason/vs.html) | |

 

### 11.1.3.2 Dosage Instructions [
](medicationrequest.html#11.1.3.2)

 Free text dosage instructions can be used for cases where the instructions are too complex to code. The content of this attribute does not include the name or description of the medication. When coded instructions are present, the free text instructions may still be present for display to humans taking or administering the medication. It is expected that the text instructions will always be populated. If the dosage.timing attribute is also populated, then the dosage.text should reflect the same information as the timing.

## 11.1.4 Search Parameters [
](medicationrequest.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| authoredon | [date](search.html#date) | Return prescriptions written on this date | MedicationRequest.authoredOn | | |

| category | [token](search.html#token) | Returns prescriptions with different categories | MedicationRequest.category | | |

| code | [token](search.html#token) | Return prescriptions of this medication code | (MedicationRequest.medication as CodeableConcept) | [13 Resources](searchparameter-registry.html#clinical-code) | |

| date | [date](search.html#date) | Returns medication request to be administered on a specific date | MedicationRequest.dosageInstruction.timing.event | [3 Resources](searchparameter-registry.html#medications-date) | |

| encounter | [reference](search.html#reference) | Return prescriptions with this encounter identifier | MedicationRequest.encounter
([Encounter](encounter.html)) | [1 Resources](searchparameter-registry.html#medications-encounter) | |

| identifier | [token](search.html#token) | Return prescriptions with this external identifier | MedicationRequest.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| intended-dispenser | [reference](search.html#reference) | Returns prescriptions intended to be dispensed by this Organization | MedicationRequest.dispenseRequest.performer
([Organization](organization.html)) | | |

| intended-performer | [reference](search.html#reference) | Returns the intended performer of the administration of the medication request | MedicationRequest.performer
([Practitioner](practitioner.html), [Organization](organization.html), [CareTeam](careteam.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| intended-performertype | [token](search.html#token) | Returns requests for a specific type of performer | MedicationRequest.performerType | | |

| intent | [token](search.html#token) | Returns prescriptions with different intents | MedicationRequest.intent | | |

| medication | [reference](search.html#reference) | Return prescriptions for this medication reference | (MedicationRequest.medication as Reference)
([Medication](medication.html)) | [3 Resources](searchparameter-registry.html#medications-medication) | |

| patient | [reference](search.html#reference) | Returns prescriptions for a specific patient | MedicationRequest.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| priority | [token](search.html#token) | Returns prescriptions with different priorities | MedicationRequest.priority | | |

| requester | [reference](search.html#reference) | Returns prescriptions prescribed by this prescriber | MedicationRequest.requester
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| status | [token](search.html#token) | Status of the prescription | MedicationRequest.status | [3 Resources](searchparameter-registry.html#medications-status) | |

| subject | [reference](search.html#reference) | The identity of a patient to list orders for | MedicationRequest.subject
([Group](group.html), [Patient](patient.html)) | | |