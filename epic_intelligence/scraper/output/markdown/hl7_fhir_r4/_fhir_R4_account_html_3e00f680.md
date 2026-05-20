# Account - FHIR v4.0.1Unique identifier used to reference the account.  Might or might not be intended for human use (e.g. credit card number)Indicates whether the account is presently used/usable or not (this element modifies the meaning of other elements)Indicates whether the account is available to be used. (Strength=Required)Categorizes the account for reporting and searching purposesThe usage type of this account, permits categorization of accounts. (Strength=Example)Name used for the account when displaying it to humans in reports, etcIdentifies the entity which incurs the expenses. While the immediate recipients of services or goods might be entities related to the subject, the expenses were ultimately incurred by the subject of the AccountThe date range of services associated with this accountIndicates the service area, hospital, department, etc. with responsibility for managing the AccountProvides additional information about what the account tracks and how it is usedReference to a parent AccountThe party(s) that contribute to payment (or part of) of the charges applied to this account (including self-pay).

A coverage may only be responsible for specific types of charges, and the sequence of the coverages in the account could be important when processing billingThe priority of the coverage in the context of this accountThe entity who is responsibleA guarantor may be placed on credit hold or otherwise have their role temporarily suspendedThe timeframe during which the guarantor accepts responsibility for the accountThe party(s) that are responsible for covering the payment of this account, and what order should they be applied to the accountThe parties responsible for balancing the account if other payment options fall shortUnique identifier used to reference the account.  Might or might not be intended for human use (e.g. credit card number)Indicates whether the account is presently used/usable or not (this element modifies the meaning of other elements)Indicates whether the account is available to be used. (Strength=Required)Categorizes the account for reporting and searching purposesThe usage type of this account, permits categorization of accounts. (Strength=Example)Name used for the account when displaying it to humans in reports, etcIdentifies the entity which incurs the expenses. While the immediate recipients of services or goods might be entities related to the subject, the expenses were ultimately incurred by the subject of the AccountThe date range of services associated with this accountIndicates the service area, hospital, department, etc. with responsibility for managing the AccountProvides additional information about what the account tracks and how it is usedReference to a parent AccountThe party(s) that contribute to payment (or part of) of the charges applied to this account (including self-pay).

A coverage may only be responsible for specific types of charges, and the sequence of the coverages in the account could be important when processing billingThe priority of the coverage in the context of this accountThe entity who is responsibleA guarantor may be placed on credit hold or otherwise have their role temporarily suspendedThe timeframe during which the guarantor accepts responsibility for the accountThe party(s) that are responsible for covering the payment of this account, and what order should they be applied to the accountThe parties responsible for balancing the account if other payment options fall short

> Source: https://hl7.org/fhir/R4/account.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/account.html) [R4B](http://hl7.org/fhir/R4B/account.html) **R4** [R3](http://hl7.org/fhir/STU3/account.html) [R2](http://hl7.org/fhir/DSTU2/account.html)
 

# 8.12 Resource Account - Content [
](account.html#8.12)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html) | |

A financial tool for tracking value accrued for a particular purpose. In the healthcare field, used to track charges for a patient, cost centers, etc.

## 8.12.1 Scope and Usage [
](account.html#scope)

The Account resource acts as a central record against which charges, payments, and adjustments are applied. It contains information about which parties are responsible for payment of the account.

While the Account does conceptually have a balance, expressing that balance directly as a resource property is challenging due to the complexity of pricing contracts. An operation to retrieve the current balance of an account is in consideration as future work.

## 8.12.2 Boundaries and Relationships [
](account.html#8.12.2)

The Account itself does not include information about the charges, payments or adjustments, but rather those resources, such as ChargeItem point to the account to which they apply. Payment and adjustment resources have not yet been developed.

## 8.12.3 Background and Context [
](account.html#8.12.3)

The Account resource can be considered a "bucket" to which ChargeItem resources are linked. These charges are processed by a billing system, which determines the responsible parties for the balance of the account. The billing system then submits claims or sends statements to the appropriate parties. Once payment is received, an adjustment is applied to the Account. The internal calculation of balances and allocation of responsibility is expected to be internal to the billing systems. Only the inputs and outputs of the billing process is communicated in the relevant financial FHIR resources.

This resource is referenced by itself, [ChargeItem](chargeitem.html#ChargeItem), [Encounter](encounter.html#Encounter), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare) and [Invoice](invoice.html#Invoice)

## 8.12.4 
Resource Content
 [
](account.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Account](account-definitions.html#Account) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Tracks balance, charges, for patient or cost center**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](account-definitions.html#Account.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Account number
 | |

| [status](account-definitions.html#Account.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | inactive | entered-in-error | on-hold | unknown
[AccountStatus](valueset-account-status.html) ([Required](terminologies.html#required)) | |

| [type](account-definitions.html#Account.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | E.g. patient, expense, depreciation
[Account Types](valueset-account-type.html) ([Example](terminologies.html#example)) | |

| [name](account-definitions.html#Account.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human-readable label | |

| [subject](account-definitions.html#Account.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Patient](patient.html) | [Device](device.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Location](location.html) | [HealthcareService](healthcareservice.html) | [Organization](organization.html)) | The entity that caused the expenses
 | |

| [servicePeriod](account-definitions.html#Account.servicePeriod) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Transaction window | |

| [coverage](account-definitions.html#Account.coverage) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
 | |

| [coverage](account-definitions.html#Account.coverage.coverage) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Coverage](coverage.html)) | The party(s), such as insurances, that may contribute to the payment of this account | |

| [priority](account-definitions.html#Account.coverage.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [positiveInt](datatypes.html#positiveInt) | The priority of the coverage in the context of this account | |

| [owner](account-definitions.html#Account.owner) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Entity managing the Account | |

| [description](account-definitions.html#Account.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Explanation of purpose/use | |

| [guarantor](account-definitions.html#Account.guarantor) | | 0..* | [BackboneElement](backboneelement.html) | The parties ultimately responsible for balancing the Account
 | |

| [party](account-definitions.html#Account.guarantor.party) | | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Responsible entity | |

| [onHold](account-definitions.html#Account.guarantor.onHold) | | 0..1 | [boolean](datatypes.html#boolean) | Credit or other hold applied | |

| [period](account-definitions.html#Account.guarantor.period) | | 0..1 | [Period](datatypes.html#Period) | Guarantee account during | |

| [partOf](account-definitions.html#Account.partOf) | | 0..1 | [Reference](references.html#Reference)([Account](account.html)) | Reference to a parent Account | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Account ([DomainResource](domainresource.html))[Unique identifier used to reference the account. Might or might not be intended for human use (e.g. credit card number)identifier](account-definitions.html#Account.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Indicates whether the account is presently used/usable or not (this element modifies the meaning of other elements)status](account-definitions.html#Account.status) : [code](datatypes.html#code) [1..1] « [Indicates whether the account is available to be used. (Strength=Required)AccountStatus](valueset-account-status.html)! »[Categorizes the account for reporting and searching purposestype](account-definitions.html#Account.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The usage type of this account, permits categorization of accounts. (Strength=Example)AccountTypes](valueset-account-type.html)?? »[Name used for the account when displaying it to humans in reports, etcname](account-definitions.html#Account.name) : [string](datatypes.html#string) [0..1][Identifies the entity which incurs the expenses. While the immediate recipients of services or goods might be entities related to the subject, the expenses were ultimately incurred by the subject of the Accountsubject](account-definitions.html#Account.subject) : [Reference](references.html#Reference) [0..*] « [Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|[Organization](organization.html#Organization) »[The date range of services associated with this accountservicePeriod](account-definitions.html#Account.servicePeriod) : [Period](datatypes.html#Period) [0..1][Indicates the service area, hospital, department, etc. with responsibility for managing the Accountowner](account-definitions.html#Account.owner) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Provides additional information about what the account tracks and how it is useddescription](account-definitions.html#Account.description) : [string](datatypes.html#string) [0..1][Reference to a parent AccountpartOf](account-definitions.html#Account.partOf) : [Reference](references.html#Reference) [0..1] « [Account](account.html#Account) »Coverage[The party(s) that contribute to payment (or part of) of the charges applied to this account (including self-pay).

A coverage may only be responsible for specific types of charges, and the sequence of the coverages in the account could be important when processing billingcoverage](account-definitions.html#Account.coverage.coverage) : [Reference](references.html#Reference) [1..1] « [Coverage](coverage.html#Coverage) »[The priority of the coverage in the context of this accountpriority](account-definitions.html#Account.coverage.priority) : [positiveInt](datatypes.html#positiveInt) [0..1]Guarantor[The entity who is responsibleparty](account-definitions.html#Account.guarantor.party) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »[A guarantor may be placed on credit hold or otherwise have their role temporarily suspendedonHold](account-definitions.html#Account.guarantor.onHold) : [boolean](datatypes.html#boolean) [0..1][The timeframe during which the guarantor accepts responsibility for the accountperiod](account-definitions.html#Account.guarantor.period) : [Period](datatypes.html#Period) [0..1]
[The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the accountcoverage](account-definitions.html#Account.coverage)[0..*][The parties responsible for balancing the account if other payment options fall shortguarantor](account-definitions.html#Account.guarantor)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Account**](account-definitions.html#Account) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](account-definitions.html#Account.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Account number](terminologies.html#unbound) --></identifier>
 <[**status**](account-definitions.html#Account.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [active | inactive | entered-in-error | on-hold | unknown](valueset-account-status.html) -->
 <[**type**](account-definitions.html#Account.type)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [E.g. patient, expense, depreciation](valueset-account-type.html) --></type>
 <[**name**](account-definitions.html#Account.name) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Human-readable label](terminologies.html#unbound) -->
 <[**subject**](account-definitions.html#Account.subject)><!-- **0..*** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|[Organization](organization.html#Organization)) [The entity that caused the expenses](terminologies.html#unbound) --></subject>
 <[**servicePeriod**](account-definitions.html#Account.servicePeriod)><!-- **0..1** [Period](datatypes.html#Period) [Transaction window](terminologies.html#unbound) --></servicePeriod>
 <[**coverage**](account-definitions.html#Account.coverage)> <!-- **0..*** The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account -->
 <[**coverage**](account-definitions.html#Account.coverage.coverage)><!-- **1..1** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) [The party(s), such as insurances, that may contribute to the payment of this account](terminologies.html#unbound) --></coverage>
 <[**priority**](account-definitions.html#Account.coverage.priority) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [The priority of the coverage in the context of this account](terminologies.html#unbound) -->
 </coverage>
 <[**owner**](account-definitions.html#Account.owner)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Entity managing the Account](terminologies.html#unbound) --></owner>
 <[**description**](account-definitions.html#Account.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Explanation of purpose/use](terminologies.html#unbound) -->
 <[**guarantor**](account-definitions.html#Account.guarantor)> <!-- **0..*** The parties ultimately responsible for balancing the Account -->
 <[**party**](account-definitions.html#Account.guarantor.party)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Responsible entity](terminologies.html#unbound) --></party>
 <[**onHold**](account-definitions.html#Account.guarantor.onHold) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Credit or other hold applied](terminologies.html#unbound) -->
 <[**period**](account-definitions.html#Account.guarantor.period)><!-- **0..1** [Period](datatypes.html#Period) [Guarantee account during](terminologies.html#unbound) --></period>
 </guarantor>
 <[**partOf**](account-definitions.html#Account.partOf)><!-- **0..1** [Reference](references.html#Reference)([Account](account.html#Account)) [Reference to a parent Account](terminologies.html#unbound) --></partOf>
</Account>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Account**](account-definitions.html#Account)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](account-definitions.html#Account.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Account number](terminologies.html#unbound)
 "[status](account-definitions.html#Account.status)" : "<[code](datatypes.html#code)>", // **R!** [active | inactive | entered-in-error | on-hold | unknown](valueset-account-status.html)
 "[type](account-definitions.html#Account.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [E.g. patient, expense, depreciation](valueset-account-type.html)
 "[name](account-definitions.html#Account.name)" : "<[string](datatypes.html#string)>", // [Human-readable label](terminologies.html#unbound)
 "[subject](account-definitions.html#Account.subject)" : [{ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|[Organization](organization.html#Organization)) }], // [The entity that caused the expenses](terminologies.html#unbound)
 "[servicePeriod](account-definitions.html#Account.servicePeriod)" : { [Period](datatypes.html#Period) }, // [Transaction window](terminologies.html#unbound)
 "[coverage](account-definitions.html#Account.coverage)" : [{ // [The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account](terminologies.html#unbound)
 "[coverage](account-definitions.html#Account.coverage.coverage)" : { [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) }, // **R!** [The party(s), such as insurances, that may contribute to the payment of this account](terminologies.html#unbound)
 "[priority](account-definitions.html#Account.coverage.priority)" : "<[positiveInt](datatypes.html#positiveInt)>" // [The priority of the coverage in the context of this account](terminologies.html#unbound)
 }],
 "[owner](account-definitions.html#Account.owner)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Entity managing the Account](terminologies.html#unbound)
 "[description](account-definitions.html#Account.description)" : "<[string](datatypes.html#string)>", // [Explanation of purpose/use](terminologies.html#unbound)
 "[guarantor](account-definitions.html#Account.guarantor)" : [{ // [The parties ultimately responsible for balancing the Account](terminologies.html#unbound)
 "[party](account-definitions.html#Account.guarantor.party)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) }, // **R!** [Responsible entity](terminologies.html#unbound)
 "[onHold](account-definitions.html#Account.guarantor.onHold)" : <[boolean](datatypes.html#boolean)>, // [Credit or other hold applied](terminologies.html#unbound)
 "[period](account-definitions.html#Account.guarantor.period)" : { [Period](datatypes.html#Period) } // [Guarantee account during](terminologies.html#unbound)
 }],
 "[partOf](account-definitions.html#Account.partOf)" : { [Reference](references.html#Reference)([Account](account.html#Account)) } // [Reference to a parent Account](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Account**](account-definitions.html#Account);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Account.identifier](account-definitions.html#Account.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Account number
 fhir:[Account.status](account-definitions.html#Account.status) [ [code](datatypes.html#code) ]; # 1..1 active | inactive | entered-in-error | on-hold | unknown
 fhir:[Account.type](account-definitions.html#Account.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 E.g. patient, expense, depreciation
 fhir:[Account.name](account-definitions.html#Account.name) [ [string](datatypes.html#string) ]; # 0..1 Human-readable label
 fhir:[Account.subject](account-definitions.html#Account.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|
 [Organization](organization.html#Organization)) ], ... ; # 0..* The entity that caused the expenses
 fhir:[Account.servicePeriod](account-definitions.html#Account.servicePeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Transaction window
 fhir:[Account.coverage](account-definitions.html#Account.coverage) [ # 0..* The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
 fhir:[Account.coverage.coverage](account-definitions.html#Account.coverage.coverage) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) ]; # 1..1 The party(s), such as insurances, that may contribute to the payment of this account
 fhir:[Account.coverage.priority](account-definitions.html#Account.coverage.priority) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 The priority of the coverage in the context of this account
 ], ...;
 fhir:[Account.owner](account-definitions.html#Account.owner) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Entity managing the Account
 fhir:[Account.description](account-definitions.html#Account.description) [ [string](datatypes.html#string) ]; # 0..1 Explanation of purpose/use
 fhir:[Account.guarantor](account-definitions.html#Account.guarantor) [ # 0..* The parties ultimately responsible for balancing the Account
 fhir:[Account.guarantor.party](account-definitions.html#Account.guarantor.party) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]; # 1..1 Responsible entity
 fhir:[Account.guarantor.onHold](account-definitions.html#Account.guarantor.onHold) [ [boolean](datatypes.html#boolean) ]; # 0..1 Credit or other hold applied
 fhir:[Account.guarantor.period](account-definitions.html#Account.guarantor.period) [ [Period](datatypes.html#Period) ]; # 0..1 Guarantee account during
 ], ...;
 fhir:[Account.partOf](account-definitions.html#Account.partOf) [ [Reference](references.html#Reference)([Account](account.html#Account)) ]; # 0..1 Reference to a parent Account
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Account](account.html#Account)
 | 
 | 
 |

 | 
 Account.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/account-status to http://hl7.org/fhir/ValueSet/account-status|4.0.1

 

 | 
 |

 | 
 Account.subject | 
 
 

 - Max Cardinality changed from 1 to *

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Account.servicePeriod | 
 
 

 - Renamed from period to servicePeriod

 

 | 
 |

 | 
 Account.partOf | 
 
 

 - Added Element

 

 | 
 |

 | 
 Account.active | 
 
 

 - deleted

 

 | 
 |

 | 
 Account.balance | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](account.diff.xml) or [JSON](account.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](account-version-maps.html) (status = 2 tests that all execute ok. 2 fail round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Account](account-definitions.html#Account) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Tracks balance, charges, for patient or cost center**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](account-definitions.html#Account.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Account number
 | |

| [status](account-definitions.html#Account.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | inactive | entered-in-error | on-hold | unknown
[AccountStatus](valueset-account-status.html) ([Required](terminologies.html#required)) | |

| [type](account-definitions.html#Account.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | E.g. patient, expense, depreciation
[Account Types](valueset-account-type.html) ([Example](terminologies.html#example)) | |

| [name](account-definitions.html#Account.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human-readable label | |

| [subject](account-definitions.html#Account.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Patient](patient.html) | [Device](device.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Location](location.html) | [HealthcareService](healthcareservice.html) | [Organization](organization.html)) | The entity that caused the expenses
 | |

| [servicePeriod](account-definitions.html#Account.servicePeriod) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Transaction window | |

| [coverage](account-definitions.html#Account.coverage) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
 | |

| [coverage](account-definitions.html#Account.coverage.coverage) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Coverage](coverage.html)) | The party(s), such as insurances, that may contribute to the payment of this account | |

| [priority](account-definitions.html#Account.coverage.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [positiveInt](datatypes.html#positiveInt) | The priority of the coverage in the context of this account | |

| [owner](account-definitions.html#Account.owner) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Entity managing the Account | |

| [description](account-definitions.html#Account.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Explanation of purpose/use | |

| [guarantor](account-definitions.html#Account.guarantor) | | 0..* | [BackboneElement](backboneelement.html) | The parties ultimately responsible for balancing the Account
 | |

| [party](account-definitions.html#Account.guarantor.party) | | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Responsible entity | |

| [onHold](account-definitions.html#Account.guarantor.onHold) | | 0..1 | [boolean](datatypes.html#boolean) | Credit or other hold applied | |

| [period](account-definitions.html#Account.guarantor.period) | | 0..1 | [Period](datatypes.html#Period) | Guarantee account during | |

| [partOf](account-definitions.html#Account.partOf) | | 0..1 | [Reference](references.html#Reference)([Account](account.html)) | Reference to a parent Account | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Account ([DomainResource](domainresource.html))[Unique identifier used to reference the account. Might or might not be intended for human use (e.g. credit card number)identifier](account-definitions.html#Account.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Indicates whether the account is presently used/usable or not (this element modifies the meaning of other elements)status](account-definitions.html#Account.status) : [code](datatypes.html#code) [1..1] « [Indicates whether the account is available to be used. (Strength=Required)AccountStatus](valueset-account-status.html)! »[Categorizes the account for reporting and searching purposestype](account-definitions.html#Account.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The usage type of this account, permits categorization of accounts. (Strength=Example)AccountTypes](valueset-account-type.html)?? »[Name used for the account when displaying it to humans in reports, etcname](account-definitions.html#Account.name) : [string](datatypes.html#string) [0..1][Identifies the entity which incurs the expenses. While the immediate recipients of services or goods might be entities related to the subject, the expenses were ultimately incurred by the subject of the Accountsubject](account-definitions.html#Account.subject) : [Reference](references.html#Reference) [0..*] « [Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|[Organization](organization.html#Organization) »[The date range of services associated with this accountservicePeriod](account-definitions.html#Account.servicePeriod) : [Period](datatypes.html#Period) [0..1][Indicates the service area, hospital, department, etc. with responsibility for managing the Accountowner](account-definitions.html#Account.owner) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Provides additional information about what the account tracks and how it is useddescription](account-definitions.html#Account.description) : [string](datatypes.html#string) [0..1][Reference to a parent AccountpartOf](account-definitions.html#Account.partOf) : [Reference](references.html#Reference) [0..1] « [Account](account.html#Account) »Coverage[The party(s) that contribute to payment (or part of) of the charges applied to this account (including self-pay).

A coverage may only be responsible for specific types of charges, and the sequence of the coverages in the account could be important when processing billingcoverage](account-definitions.html#Account.coverage.coverage) : [Reference](references.html#Reference) [1..1] « [Coverage](coverage.html#Coverage) »[The priority of the coverage in the context of this accountpriority](account-definitions.html#Account.coverage.priority) : [positiveInt](datatypes.html#positiveInt) [0..1]Guarantor[The entity who is responsibleparty](account-definitions.html#Account.guarantor.party) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »[A guarantor may be placed on credit hold or otherwise have their role temporarily suspendedonHold](account-definitions.html#Account.guarantor.onHold) : [boolean](datatypes.html#boolean) [0..1][The timeframe during which the guarantor accepts responsibility for the accountperiod](account-definitions.html#Account.guarantor.period) : [Period](datatypes.html#Period) [0..1]
[The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the accountcoverage](account-definitions.html#Account.coverage)[0..*][The parties responsible for balancing the account if other payment options fall shortguarantor](account-definitions.html#Account.guarantor)[0..*]
 

**XML Template**

 

 
```
<[**Account**](account-definitions.html#Account) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](account-definitions.html#Account.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Account number](terminologies.html#unbound) --></identifier>
 <[**status**](account-definitions.html#Account.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [active | inactive | entered-in-error | on-hold | unknown](valueset-account-status.html) -->
 <[**type**](account-definitions.html#Account.type)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [E.g. patient, expense, depreciation](valueset-account-type.html) --></type>
 <[**name**](account-definitions.html#Account.name) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Human-readable label](terminologies.html#unbound) -->
 <[**subject**](account-definitions.html#Account.subject)><!-- **0..*** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|[Organization](organization.html#Organization)) [The entity that caused the expenses](terminologies.html#unbound) --></subject>
 <[**servicePeriod**](account-definitions.html#Account.servicePeriod)><!-- **0..1** [Period](datatypes.html#Period) [Transaction window](terminologies.html#unbound) --></servicePeriod>
 <[**coverage**](account-definitions.html#Account.coverage)> <!-- **0..*** The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account -->
 <[**coverage**](account-definitions.html#Account.coverage.coverage)><!-- **1..1** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) [The party(s), such as insurances, that may contribute to the payment of this account](terminologies.html#unbound) --></coverage>
 <[**priority**](account-definitions.html#Account.coverage.priority) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [The priority of the coverage in the context of this account](terminologies.html#unbound) -->
 </coverage>
 <[**owner**](account-definitions.html#Account.owner)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Entity managing the Account](terminologies.html#unbound) --></owner>
 <[**description**](account-definitions.html#Account.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Explanation of purpose/use](terminologies.html#unbound) -->
 <[**guarantor**](account-definitions.html#Account.guarantor)> <!-- **0..*** The parties ultimately responsible for balancing the Account -->
 <[**party**](account-definitions.html#Account.guarantor.party)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Responsible entity](terminologies.html#unbound) --></party>
 <[**onHold**](account-definitions.html#Account.guarantor.onHold) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Credit or other hold applied](terminologies.html#unbound) -->
 <[**period**](account-definitions.html#Account.guarantor.period)><!-- **0..1** [Period](datatypes.html#Period) [Guarantee account during](terminologies.html#unbound) --></period>
 </guarantor>
 <[**partOf**](account-definitions.html#Account.partOf)><!-- **0..1** [Reference](references.html#Reference)([Account](account.html#Account)) [Reference to a parent Account](terminologies.html#unbound) --></partOf>
</Account>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Account**](account-definitions.html#Account)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](account-definitions.html#Account.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Account number](terminologies.html#unbound)
 "[status](account-definitions.html#Account.status)" : "<[code](datatypes.html#code)>", // **R!** [active | inactive | entered-in-error | on-hold | unknown](valueset-account-status.html)
 "[type](account-definitions.html#Account.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [E.g. patient, expense, depreciation](valueset-account-type.html)
 "[name](account-definitions.html#Account.name)" : "<[string](datatypes.html#string)>", // [Human-readable label](terminologies.html#unbound)
 "[subject](account-definitions.html#Account.subject)" : [{ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|[Organization](organization.html#Organization)) }], // [The entity that caused the expenses](terminologies.html#unbound)
 "[servicePeriod](account-definitions.html#Account.servicePeriod)" : { [Period](datatypes.html#Period) }, // [Transaction window](terminologies.html#unbound)
 "[coverage](account-definitions.html#Account.coverage)" : [{ // [The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account](terminologies.html#unbound)
 "[coverage](account-definitions.html#Account.coverage.coverage)" : { [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) }, // **R!** [The party(s), such as insurances, that may contribute to the payment of this account](terminologies.html#unbound)
 "[priority](account-definitions.html#Account.coverage.priority)" : "<[positiveInt](datatypes.html#positiveInt)>" // [The priority of the coverage in the context of this account](terminologies.html#unbound)
 }],
 "[owner](account-definitions.html#Account.owner)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Entity managing the Account](terminologies.html#unbound)
 "[description](account-definitions.html#Account.description)" : "<[string](datatypes.html#string)>", // [Explanation of purpose/use](terminologies.html#unbound)
 "[guarantor](account-definitions.html#Account.guarantor)" : [{ // [The parties ultimately responsible for balancing the Account](terminologies.html#unbound)
 "[party](account-definitions.html#Account.guarantor.party)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) }, // **R!** [Responsible entity](terminologies.html#unbound)
 "[onHold](account-definitions.html#Account.guarantor.onHold)" : <[boolean](datatypes.html#boolean)>, // [Credit or other hold applied](terminologies.html#unbound)
 "[period](account-definitions.html#Account.guarantor.period)" : { [Period](datatypes.html#Period) } // [Guarantee account during](terminologies.html#unbound)
 }],
 "[partOf](account-definitions.html#Account.partOf)" : { [Reference](references.html#Reference)([Account](account.html#Account)) } // [Reference to a parent Account](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Account**](account-definitions.html#Account);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Account.identifier](account-definitions.html#Account.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Account number
 fhir:[Account.status](account-definitions.html#Account.status) [ [code](datatypes.html#code) ]; # 1..1 active | inactive | entered-in-error | on-hold | unknown
 fhir:[Account.type](account-definitions.html#Account.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 E.g. patient, expense, depreciation
 fhir:[Account.name](account-definitions.html#Account.name) [ [string](datatypes.html#string) ]; # 0..1 Human-readable label
 fhir:[Account.subject](account-definitions.html#Account.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Device](device.html#Device)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Location](location.html#Location)|[HealthcareService](healthcareservice.html#HealthcareService)|
 [Organization](organization.html#Organization)) ], ... ; # 0..* The entity that caused the expenses
 fhir:[Account.servicePeriod](account-definitions.html#Account.servicePeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Transaction window
 fhir:[Account.coverage](account-definitions.html#Account.coverage) [ # 0..* The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
 fhir:[Account.coverage.coverage](account-definitions.html#Account.coverage.coverage) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) ]; # 1..1 The party(s), such as insurances, that may contribute to the payment of this account
 fhir:[Account.coverage.priority](account-definitions.html#Account.coverage.priority) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 The priority of the coverage in the context of this account
 ], ...;
 fhir:[Account.owner](account-definitions.html#Account.owner) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Entity managing the Account
 fhir:[Account.description](account-definitions.html#Account.description) [ [string](datatypes.html#string) ]; # 0..1 Explanation of purpose/use
 fhir:[Account.guarantor](account-definitions.html#Account.guarantor) [ # 0..* The parties ultimately responsible for balancing the Account
 fhir:[Account.guarantor.party](account-definitions.html#Account.guarantor.party) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]; # 1..1 Responsible entity
 fhir:[Account.guarantor.onHold](account-definitions.html#Account.guarantor.onHold) [ [boolean](datatypes.html#boolean) ]; # 0..1 Credit or other hold applied
 fhir:[Account.guarantor.period](account-definitions.html#Account.guarantor.period) [ [Period](datatypes.html#Period) ]; # 0..1 Guarantee account during
 ], ...;
 fhir:[Account.partOf](account-definitions.html#Account.partOf) [ [Reference](references.html#Reference)([Account](account.html#Account)) ]; # 0..1 Reference to a parent Account
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Account](account.html#Account)
 | 
 | 
 |

 | 
 Account.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/account-status to http://hl7.org/fhir/ValueSet/account-status|4.0.1

 

 | 
 |

 | 
 Account.subject | 
 
 

 - Max Cardinality changed from 1 to *

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Account.servicePeriod | 
 
 

 - Renamed from period to servicePeriod

 

 | 
 |

 | 
 Account.partOf | 
 
 

 - Added Element

 

 | 
 |

 | 
 Account.active | 
 
 

 - deleted

 

 | 
 |

 | 
 Account.balance | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](account.diff.xml) or [JSON](account.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](account-version-maps.html) (status = 2 tests that all execute ok. 2 fail round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](account-profiles.html) and the alternate definitions:
Master Definition [XML](account.profile.xml.html) + [JSON](account.profile.json.html),
[XML](xml.html) [Schema](account.xsd)/[Schematron](account.sch) + [JSON](json.html) 
[Schema](account.schema.json.html), [ShEx](account.shex.html) (for [Turtle](rdf.html)) + [see the extensions](account-profiles.html) & the [dependency analysis](account-dependencies.html)

### 8.12.4.1 
Terminology Bindings
 [
](account.html#tx)

 | Path | Definition | Type | Reference | |

 | Account.status | Indicates whether the account is available to be used. | [Required](terminologies.html#required) | [AccountStatus](valueset-account-status.html) | |

 | Account.type | The usage type of this account, permits categorization of accounts. | [Example](terminologies.html#example) | [AccountTypes](valueset-account-type.html) | |

 

 

## 8.12.5 Search Parameters [
](account.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| identifier | [token](search.html#token) | Account number | Account.identifier | | |

| name | [string](search.html#string) | Human-readable label | Account.name | | |

| owner | [reference](search.html#reference) | Entity managing the Account | Account.owner
([Organization](organization.html)) | | |

| patient | [reference](search.html#reference) | The entity that caused the expenses | Account.subject.where(resolve() is Patient)
([Patient](patient.html)) | | |

| period | [date](search.html#date) | Transaction window | Account.servicePeriod | | |

| status | [token](search.html#token) | active | inactive | entered-in-error | on-hold | unknown | Account.status | | |

| subject | [reference](search.html#reference) | The entity that caused the expenses | Account.subject
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [Location](location.html)) | | |

| type | [token](search.html#token) | E.g. patient, expense, depreciation | Account.type | | |