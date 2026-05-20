# Coverage - FHIR v4.0.1A unique identifier assigned to this coverageThe status of the resource instance (this element modifies the meaning of other elements)A code specifying the state of the resource instance. (Strength=Required)The type of coverage: social program, medical plan, accident coverage (workers compensation, auto), group health or payment by an individual or organizationThe type of insurance: public health, worker compensation; private accident, auto, private health, etc.) or a direct payment by an individual or organization. (Strength=Preferred)The party who 'owns' the insurance policyThe party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is dueThe insurer assigned ID for the SubscriberThe party who benefits from the insurance coverage; the patient when products and/or services are providedA unique identifier for a dependent under the coverageThe relationship of beneficiary (patient) to the subscriberThe relationship between the Subscriber and the Beneficiary (insured/covered party/patient). (Strength=Extensible)Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in forceThe program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreementsThe order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of careThe insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions applyWhen 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costsThe policy(s) which constitute this insurance coverageThe type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, PlanThe policy classifications, eg. Group, Plan, Class, etc. (Strength=Extensible)The alphanumeric string value associated with the insurer issued labelA short description for the classThe category of patient centric costs associated with treatmentThe types of services to which patient copayments are specified. (Strength=Extensible)The amount due from the patient for the cost categoryThe code for the specific exceptionThe types of exceptions from the part or full value of financial obligations such as copays. (Strength=Example)The timeframe during when the exception is in forceA suite of underwriter specific classifiersA suite of codes indicating exceptions or reductions to patient costs and their effective periodsA suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health cardA unique identifier assigned to this coverageThe status of the resource instance (this element modifies the meaning of other elements)A code specifying the state of the resource instance. (Strength=Required)The type of coverage: social program, medical plan, accident coverage (workers compensation, auto), group health or payment by an individual or organizationThe type of insurance: public health, worker compensation; private accident, auto, private health, etc.) or a direct payment by an individual or organization. (Strength=Preferred)The party who 'owns' the insurance policyThe party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is dueThe insurer assigned ID for the SubscriberThe party who benefits from the insurance coverage; the patient when products and/or services are providedA unique identifier for a dependent under the coverageThe relationship of beneficiary (patient) to the subscriberThe relationship between the Subscriber and the Beneficiary (insured/covered party/patient). (Strength=Extensible)Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in forceThe program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreementsThe order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of careThe insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions applyWhen 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costsThe policy(s) which constitute this insurance coverageThe type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, PlanThe policy classifications, eg. Group, Plan, Class, etc. (Strength=Extensible)The alphanumeric string value associated with the insurer issued labelA short description for the classThe category of patient centric costs associated with treatmentThe types of services to which patient copayments are specified. (Strength=Extensible)The amount due from the patient for the cost categoryThe code for the specific exceptionThe types of exceptions from the part or full value of financial obligations such as copays. (Strength=Example)The timeframe during when the exception is in forceA suite of underwriter specific classifiersA suite of codes indicating exceptions or reductions to patient costs and their effective periodsA suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card

> Source: https://hl7.org/fhir/R4/coverage.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/coverage.html) [R4B](http://hl7.org/fhir/R4B/coverage.html) **R4** [R3](http://hl7.org/fhir/STU3/coverage.html) [R2](http://hl7.org/fhir/DSTU2/coverage.html)
 

# 13.1 Resource Coverage - Content [
](coverage.html#13.1)

| [Financial Management ](http://www.hl7.org/Special/committees/fm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.

## 13.1.1 Scope and Usage [
](coverage.html#scope)

The Coverage resource is intended to provide the high-level identifiers and descriptors of an insurance plan, typically the information which would 
appear on an insurance card, which may be used to pay, in part or in whole, for the provision of health care products and services. 

This resource may also be used to register 'SelfPay' where an individual or organization other than an insurer is taking responsibility for payment for a
 portion of the health care costs. Selfpay should not be confused with being a guarantor of the patient's account.

The Coverage resource is a "event" resource from a FHIR workflow perspective - see [Workflow Request.](workflow.html#event)

 

 
 
## 13.1.2 Boundaries and Relationships [
](coverage.html#bnr)

 **The eClaim domain includes a number of related insurance resources**
 

 

 | 
 Coverage | 
 The Coverage resource is intended to provide the high-level identifiers and descriptors of a specific insurance plan for
a specific individual - essentially the insurance card information. This may alternately provide the individual or organization, selfpay,
 which will pay for products and services rendered. | 
 |

 | 
 [Contract](contract.html) | 
 A Contract resource holds the references to parties who have entered into an agreement of some type, the parties who may sign or witness
 such an agreement, descriptors of the type of agreement and even the actual text or executable copy of the agreement. The agreement may be of 
 a variety of types including service contracts, insurance contracts, directives, etc. The contract may be either definitional or actual instances.
 | 
 |

 | 
 [InsurancePlan](insuranceplan.html) | 
 The InsurancePlan resource holds the definition of an insurance plan which an insurer may offer to potential clients through
 insurance brokers or an online insurance marketplace. This is only the plan definition and does not contain or reference 
 a list of individuals who have purchased the plan. 
 | 
 |

 

 

This resource is referenced by [Account](account.html#Account), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [DeviceRequest](devicerequest.html#DeviceRequest), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [MedicationRequest](medicationrequest.html#MedicationRequest), [ServiceRequest](servicerequest.html#ServiceRequest) and [Task](task.html#Task)

## 13.1.3 
Resource Content
 [
](coverage.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Coverage](coverage-definitions.html#Coverage) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Insurance or medical plan or a payment agreement**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](coverage-definitions.html#Coverage.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for the coverage
 | |

| [status](coverage-definitions.html#Coverage.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | cancelled | draft | entered-in-error
[Financial Resource Status Codes](valueset-fm-status.html) ([Required](terminologies.html#required)) | |

| [type](coverage-definitions.html#Coverage.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Coverage category such as medical or accident
[Coverage Type and Self-Pay Codes](valueset-coverage-type.html) ([Preferred](terminologies.html#preferred)) | |

| [policyHolder](coverage-definitions.html#Coverage.policyHolder) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Owner of the policy | |

| [subscriber](coverage-definitions.html#Coverage.subscriber) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Subscriber to the policy | |

| [subscriberId](coverage-definitions.html#Coverage.subscriberId) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | ID assigned to the subscriber | |

| [beneficiary](coverage-definitions.html#Coverage.beneficiary) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | Plan beneficiary | |

| [dependent](coverage-definitions.html#Coverage.dependent) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Dependent number | |

| [relationship](coverage-definitions.html#Coverage.relationship) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Beneficiary relationship to the subscriber
[SubscriberPolicyholder Relationship Codes](valueset-subscriber-relationship.html) ([Extensible](terminologies.html#extensible)) | |

| [period](coverage-definitions.html#Coverage.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Coverage start and end dates | |

| [payor](coverage-definitions.html#Coverage.payor) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [Reference](references.html#Reference)([Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Issuer of the policy
 | |

| [class](coverage-definitions.html#Coverage.class) | | 0..* | [BackboneElement](backboneelement.html) | Additional coverage classifications
 | |

| [type](coverage-definitions.html#Coverage.class.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of class such as 'group' or 'plan'
[Coverage Class Codes](valueset-coverage-class.html) ([Extensible](terminologies.html#extensible)) | |

| [value](coverage-definitions.html#Coverage.class.value) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [string](datatypes.html#string) | Value associated with the type | |

| [name](coverage-definitions.html#Coverage.class.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human readable description of the type and value | |

| [order](coverage-definitions.html#Coverage.order) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [positiveInt](datatypes.html#positiveInt) | Relative order of the coverage | |

| [network](coverage-definitions.html#Coverage.network) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Insurer network | |

| [costToBeneficiary](coverage-definitions.html#Coverage.costToBeneficiary) | | 0..* | [BackboneElement](backboneelement.html) | Patient payments for services/products
 | |

| [type](coverage-definitions.html#Coverage.costToBeneficiary.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Cost category
[Coverage Copay Type Codes](valueset-coverage-copay-type.html) ([Extensible](terminologies.html#extensible)) | |

| [value[x]](coverage-definitions.html#Coverage.costToBeneficiary.value_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | | The amount or percentage due from the beneficiary | |

| valueQuantity | | | [SimpleQuantity](datatypes.html#SimpleQuantity) | | |

| valueMoney | | | [Money](datatypes.html#Money) | | |

| [exception](coverage-definitions.html#Coverage.costToBeneficiary.exception) | | 0..* | [BackboneElement](backboneelement.html) | Exceptions for patient payments
 | |

| [type](coverage-definitions.html#Coverage.costToBeneficiary.exception.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Exception category
[Example Coverage Financial Exception Codes](valueset-coverage-financial-exception.html) ([Example](terminologies.html#example)) | |

| [period](coverage-definitions.html#Coverage.costToBeneficiary.exception.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | The effective period of the exception | |

| [subrogation](coverage-definitions.html#Coverage.subrogation) | | 0..1 | [boolean](datatypes.html#boolean) | Reimbursement to insurer | |

| [contract](coverage-definitions.html#Coverage.contract) | | 0..* | [Reference](references.html#Reference)([Contract](contract.html)) | Contract details
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Coverage ([DomainResource](domainresource.html))[A unique identifier assigned to this coverageidentifier](coverage-definitions.html#Coverage.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The status of the resource instance (this element modifies the meaning of other elements)status](coverage-definitions.html#Coverage.status) : [code](datatypes.html#code) [1..1] « [A code specifying the state of the resource instance. (Strength=Required)FinancialResourceStatusCodes](valueset-fm-status.html)! »[The type of coverage: social program, medical plan, accident coverage (workers compensation, auto), group health or payment by an individual or organizationtype](coverage-definitions.html#Coverage.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The type of insurance: public health, worker compensation; private accident, auto, private health, etc.) or a direct payment by an individual or organization. (Strength=Preferred)CoverageTypeAndSelf-PayCodes](valueset-coverage-type.html)? »[The party who 'owns' the insurance policypolicyHolder](coverage-definitions.html#Coverage.policyHolder) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »[The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is duesubscriber](coverage-definitions.html#Coverage.subscriber) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »[The insurer assigned ID for the SubscribersubscriberId](coverage-definitions.html#Coverage.subscriberId) : [string](datatypes.html#string) [0..1][The party who benefits from the insurance coverage; the patient when products and/or services are providedbeneficiary](coverage-definitions.html#Coverage.beneficiary) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient) »[A unique identifier for a dependent under the coveragedependent](coverage-definitions.html#Coverage.dependent) : [string](datatypes.html#string) [0..1][The relationship of beneficiary (patient) to the subscriberrelationship](coverage-definitions.html#Coverage.relationship) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The relationship between the Subscriber and the Beneficiary (insured/covered party/patient). (Strength=Extensible)SubscriberRelationshipCodes](valueset-subscriber-relationship.html)+ »[Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in forceperiod](coverage-definitions.html#Coverage.period) : [Period](datatypes.html#Period) [0..1][The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreementspayor](coverage-definitions.html#Coverage.payor) : [Reference](references.html#Reference) [1..*] « [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »[The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of careorder](coverage-definitions.html#Coverage.order) : [positiveInt](datatypes.html#positiveInt) [0..1][The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions applynetwork](coverage-definitions.html#Coverage.network) : [string](datatypes.html#string) [0..1][When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costssubrogation](coverage-definitions.html#Coverage.subrogation) : [boolean](datatypes.html#boolean) [0..1][The policy(s) which constitute this insurance coveragecontract](coverage-definitions.html#Coverage.contract) : [Reference](references.html#Reference) [0..*] « [Contract](contract.html#Contract) »Class[The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plantype](coverage-definitions.html#Coverage.class.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The policy classifications, eg. Group, Plan, Class, etc. (Strength=Extensible)CoverageClassCodes](valueset-coverage-class.html)+ »[The alphanumeric string value associated with the insurer issued labelvalue](coverage-definitions.html#Coverage.class.value) : [string](datatypes.html#string) [1..1][A short description for the classname](coverage-definitions.html#Coverage.class.name) : [string](datatypes.html#string) [0..1]CostToBeneficiary[The category of patient centric costs associated with treatmenttype](coverage-definitions.html#Coverage.costToBeneficiary.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The types of services to which patient copayments are specified. (Strength=Extensible)CoverageCopayTypeCodes](valueset-coverage-copay-type.html)+ »[The amount due from the patient for the cost categoryvalue[x]](coverage-definitions.html#Coverage.costToBeneficiary.value_x_) : [Type](formats.html#umlchoice) [1..1] « [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity))|[Money](datatypes.html#Money) »Exemption[The code for the specific exceptiontype](coverage-definitions.html#Coverage.costToBeneficiary.exception.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The types of exceptions from the part or full value of financial obligations such as copays. (Strength=Example)ExampleCoverageFinancialExcep...](valueset-coverage-financial-exception.html)?? »[The timeframe during when the exception is in forceperiod](coverage-definitions.html#Coverage.costToBeneficiary.exception.period) : [Period](datatypes.html#Period) [0..1]
[A suite of underwriter specific classifiersclass](coverage-definitions.html#Coverage.class)[0..*][A suite of codes indicating exceptions or reductions to patient costs and their effective periodsexception](coverage-definitions.html#Coverage.costToBeneficiary.exception)[0..*][A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been included on the health cardcostToBeneficiary](coverage-definitions.html#Coverage.costToBeneficiary)[0..*]
 

 

 

**XML Template**

 

 
```
http://hl7.org/fhir/ValueSet/subscriber-relationship
```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Coverage**](coverage-definitions.html#Coverage)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](coverage-definitions.html#Coverage.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business Identifier for the coverage](terminologies.html#unbound)
 "[status](coverage-definitions.html#Coverage.status)" : "<[code](datatypes.html#code)>", // **R!** [active | cancelled | draft | entered-in-error](valueset-fm-status.html)
 "[type](coverage-definitions.html#Coverage.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Coverage category such as medical or accident](valueset-coverage-type.html)
 "[policyHolder](coverage-definitions.html#Coverage.policyHolder)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) }, // [Owner of the policy](terminologies.html#unbound)
 "[subscriber](coverage-definitions.html#Coverage.subscriber)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Subscriber to the policy](terminologies.html#unbound)
 "[subscriberId](coverage-definitions.html#Coverage.subscriberId)" : "<[string](datatypes.html#string)>", // [ID assigned to the subscriber](terminologies.html#unbound)
 "[beneficiary](coverage-definitions.html#Coverage.beneficiary)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) }, // **R!** [Plan beneficiary](terminologies.html#unbound)
 "[dependent](coverage-definitions.html#Coverage.dependent)" : "<[string](datatypes.html#string)>", // [Dependent number](terminologies.html#unbound)
 "[relationship](coverage-definitions.html#Coverage.relationship)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Beneficiary relationship to the subscriber](valueset-subscriber-relationship.html)
 "[period](coverage-definitions.html#Coverage.period)" : { [Period](datatypes.html#Period) }, // [Coverage start and end dates](terminologies.html#unbound)
 "[payor](coverage-definitions.html#Coverage.payor)" : [{ [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) }], // **R!** [Issuer of the policy](terminologies.html#unbound)
 "[class](coverage-definitions.html#Coverage.class)" : [{ // [Additional coverage classifications](terminologies.html#unbound)
 "[type](coverage-definitions.html#Coverage.class.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Type of class such as 'group' or 'plan'](valueset-coverage-class.html)
 "[value](coverage-definitions.html#Coverage.class.value)" : "<[string](datatypes.html#string)>", // **R!** [Value associated with the type](terminologies.html#unbound)
 "[name](coverage-definitions.html#Coverage.class.name)" : "<[string](datatypes.html#string)>" // [Human readable description of the type and value](terminologies.html#unbound)
 }],
 "[order](coverage-definitions.html#Coverage.order)" : "<[positiveInt](datatypes.html#positiveInt)>", // [Relative order of the coverage](terminologies.html#unbound)
 "[network](coverage-definitions.html#Coverage.network)" : "<[string](datatypes.html#string)>", // [Insurer network](terminologies.html#unbound)
 "[costToBeneficiary](coverage-definitions.html#Coverage.costToBeneficiary)" : [{ // [Patient payments for services/products](terminologies.html#unbound)
 "[type](coverage-definitions.html#Coverage.costToBeneficiary.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Cost category](valueset-coverage-copay-type.html)
 // value[x]: The amount or percentage due from the beneficiary. One of these 2:
 "[valueQuantity](coverage-definitions.html#Coverage.costToBeneficiary.valueQuantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) },
 "[valueMoney](coverage-definitions.html#Coverage.costToBeneficiary.valueMoney)" : { [Money](datatypes.html#Money) },
 "[exception](coverage-definitions.html#Coverage.costToBeneficiary.exception)" : [{ // [Exceptions for patient payments](terminologies.html#unbound)
 "[type](coverage-definitions.html#Coverage.costToBeneficiary.exception.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Exception category](valueset-coverage-financial-exception.html)
 "[period](coverage-definitions.html#Coverage.costToBeneficiary.exception.period)" : { [Period](datatypes.html#Period) } // [The effective period of the exception](terminologies.html#unbound)
 }]
 }],
 "[subrogation](coverage-definitions.html#Coverage.subrogation)" : <[boolean](datatypes.html#boolean)>, // [Reimbursement to insurer](terminologies.html#unbound)
 "[contract](coverage-definitions.html#Coverage.contract)" : [{ [Reference](references.html#Reference)([Contract](contract.html#Contract)) }] // [Contract details](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Coverage**](coverage-definitions.html#Coverage);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Coverage.identifier](coverage-definitions.html#Coverage.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for the coverage
 fhir:[Coverage.status](coverage-definitions.html#Coverage.status) [ [code](datatypes.html#code) ]; # 1..1 active | cancelled | draft | entered-in-error
 fhir:[Coverage.type](coverage-definitions.html#Coverage.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Coverage category such as medical or accident
 fhir:[Coverage.policyHolder](coverage-definitions.html#Coverage.policyHolder) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]; # 0..1 Owner of the policy
 fhir:[Coverage.subscriber](coverage-definitions.html#Coverage.subscriber) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Subscriber to the policy
 fhir:[Coverage.subscriberId](coverage-definitions.html#Coverage.subscriberId) [ [string](datatypes.html#string) ]; # 0..1 ID assigned to the subscriber
 fhir:[Coverage.beneficiary](coverage-definitions.html#Coverage.beneficiary) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 1..1 Plan beneficiary
 fhir:[Coverage.dependent](coverage-definitions.html#Coverage.dependent) [ [string](datatypes.html#string) ]; # 0..1 Dependent number
 fhir:[Coverage.relationship](coverage-definitions.html#Coverage.relationship) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Beneficiary relationship to the subscriber
 fhir:[Coverage.period](coverage-definitions.html#Coverage.period) [ [Period](datatypes.html#Period) ]; # 0..1 Coverage start and end dates
 fhir:[Coverage.payor](coverage-definitions.html#Coverage.payor) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ], ... ; # 1..* Issuer of the policy
 fhir:[Coverage.class](coverage-definitions.html#Coverage.class) [ # 0..* Additional coverage classifications
 fhir:[Coverage.class.type](coverage-definitions.html#Coverage.class.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Type of class such as 'group' or 'plan'
 fhir:[Coverage.class.value](coverage-definitions.html#Coverage.class.value) [ [string](datatypes.html#string) ]; # 1..1 Value associated with the type
 fhir:[Coverage.class.name](coverage-definitions.html#Coverage.class.name) [ [string](datatypes.html#string) ]; # 0..1 Human readable description of the type and value
 ], ...;
 fhir:[Coverage.order](coverage-definitions.html#Coverage.order) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Relative order of the coverage
 fhir:[Coverage.network](coverage-definitions.html#Coverage.network) [ [string](datatypes.html#string) ]; # 0..1 Insurer network
 fhir:[Coverage.costToBeneficiary](coverage-definitions.html#Coverage.costToBeneficiary) [ # 0..* Patient payments for services/products
 fhir:[Coverage.costToBeneficiary.type](coverage-definitions.html#Coverage.costToBeneficiary.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Cost category
 # [Coverage.costToBeneficiary.value[x]](coverage-definitions.html#Coverage.costToBeneficiary.value[x]) : 1..1 The amount or percentage due from the beneficiary. One of these 2
 fhir:[Coverage.costToBeneficiary.valueSimpleQuantity](coverage-definitions.html#Coverage.costToBeneficiary.valueSimpleQuantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]
 fhir:[Coverage.costToBeneficiary.valueMoney](coverage-definitions.html#Coverage.costToBeneficiary.valueMoney) [ [Money](datatypes.html#Money) ]
 fhir:[Coverage.costToBeneficiary.exception](coverage-definitions.html#Coverage.costToBeneficiary.exception) [ # 0..* Exceptions for patient payments
 fhir:[Coverage.costToBeneficiary.exception.type](coverage-definitions.html#Coverage.costToBeneficiary.exception.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Exception category
 fhir:[Coverage.costToBeneficiary.exception.period](coverage-definitions.html#Coverage.costToBeneficiary.exception.period) [ [Period](datatypes.html#Period) ]; # 0..1 The effective period of the exception
 ], ...;
 ], ...;
 fhir:[Coverage.subrogation](coverage-definitions.html#Coverage.subrogation) [ [boolean](datatypes.html#boolean) ]; # 0..1 Reimbursement to insurer
 fhir:[Coverage.contract](coverage-definitions.html#Coverage.contract) [ [Reference](references.html#Reference)([Contract](contract.html#Contract)) ], ... ; # 0..* Contract details
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Coverage](coverage.html#Coverage)
 | 
 | 
 |

 | 
 Coverage.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/fm-status to http://hl7.org/fhir/ValueSet/fm-status|4.0.1

 

 | 
 |

 | 
 Coverage.beneficiary | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Coverage.relationship | 
 
 

 - 
Add Binding `http://hl7.org/fhir/ValueSet/subscriber-relationship` (extensible)
 

 

 | 
 |

 | 
 Coverage.payor | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Coverage.class | 
 
 

 - Renamed from grouping to class

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Coverage.class.type | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 Coverage.class.value | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 Coverage.class.name | 
 
 

 - Added Element

 

 | 
 |

 | 
 Coverage.costToBeneficiary | 
 
 

 - Added Element

 

 | 
 |

 | 
 Coverage.costToBeneficiary.type | 
 
 

 - Added Element

 

 | 
 |

 | 
 Coverage.costToBeneficiary.value[x] | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 Coverage.costToBeneficiary.exception | 
 
 

 - Added Element

 

 | 
 |

 | 
 Coverage.costToBeneficiary.exception.type | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 Coverage.costToBeneficiary.exception.period | 
 
 

 - Added Element

 

 | 
 |

 | 
 Coverage.subrogation | 
 
 

 - Added Element

 

 | 
 |

 | 
 Coverage.grouping.group | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.groupDisplay | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.subGroup | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.subGroupDisplay | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.plan | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.planDisplay | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.subPlan | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.subPlanDisplay | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.class | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.classDisplay | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.subClass | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.grouping.subClassDisplay | 
 
 

 - deleted

 

 | 
 |

 | 
 Coverage.sequence | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](coverage.diff.xml) or [JSON](coverage.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](coverage-version-maps.html) (status = 4 tests that all execute ok. 1 fail round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](coverage-profiles.html) and the alternate definitions:
Master Definition [XML](coverage.profile.xml.html) + [JSON](coverage.profile.json.html),
[XML](xml.html) [Schema](coverage.xsd)/[Schematron](coverage.sch) + [JSON](json.html) 
[Schema](coverage.schema.json.html), [ShEx](coverage.shex.html) (for [Turtle](rdf.html)) + [see the extensions](coverage-profiles.html) & the [dependency analysis](coverage-dependencies.html)

### 13.1.3.1 
Terminology Bindings
 [
](coverage.html#tx)

 | Path | Definition | Type | Reference | |

 | Coverage.status | A code specifying the state of the resource instance. | [Required](terminologies.html#required) | [FinancialResourceStatusCodes](valueset-fm-status.html) | |

 | Coverage.type | The type of insurance: public health, worker compensation; private accident, auto, private health, etc.) or a direct payment by an individual or organization. | [Preferred](terminologies.html#preferred) | [CoverageTypeAndSelf-PayCodes](valueset-coverage-type.html) | |

 | Coverage.relationship | The relationship between the Subscriber and the Beneficiary (insured/covered party/patient). | [Extensible](terminologies.html#extensible) | [SubscriberRelationshipCodes](valueset-subscriber-relationship.html) | |

 | Coverage.class.type | The policy classifications, eg. Group, Plan, Class, etc. | [Extensible](terminologies.html#extensible) | [CoverageClassCodes](valueset-coverage-class.html) | |

 | Coverage.costToBeneficiary.type | The types of services to which patient copayments are specified. | [Extensible](terminologies.html#extensible) | [CoverageCopayTypeCodes](valueset-coverage-copay-type.html) | |

 | Coverage.costToBeneficiary.exception.type | The types of exceptions from the part or full value of financial obligations such as copays. | [Example](terminologies.html#example) | [ExampleCoverageFinancialExceptionCodes](valueset-coverage-financial-exception.html) | |

 

 

## 13.1.4 Search Parameters [
](coverage.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| beneficiary | [reference](search.html#reference) | Covered party | Coverage.beneficiary
([Patient](patient.html)) | | |

| class-type | [token](search.html#token) | Coverage class (eg. plan, group) | Coverage.class.type | | |

| class-value | [string](search.html#string) | Value of the class (eg. Plan number, group number) | Coverage.class.value | | |

| dependent | [string](search.html#string) | Dependent number | Coverage.dependent | | |

| identifier | [token](search.html#token) | The primary identifier of the insured and the coverage | Coverage.identifier | | |

| patient | [reference](search.html#reference) | Retrieve coverages for a patient | Coverage.beneficiary
([Patient](patient.html)) | | |

| payor | [reference](search.html#reference) | The identity of the insurer or party paying for services | Coverage.payor
([Organization](organization.html), [Patient](patient.html), [RelatedPerson](relatedperson.html)) | | |

| policy-holder | [reference](search.html#reference) | Reference to the policyholder | Coverage.policyHolder
([Organization](organization.html), [Patient](patient.html), [RelatedPerson](relatedperson.html)) | | |

| status | [token](search.html#token) | The status of the Coverage | Coverage.status | | |

| subscriber | [reference](search.html#reference) | Reference to the subscriber | Coverage.subscriber
([Patient](patient.html), [RelatedPerson](relatedperson.html)) | | |

| type | [token](search.html#token) | The kind of coverage (health plan, auto, Workers Compensation) | Coverage.type | | |