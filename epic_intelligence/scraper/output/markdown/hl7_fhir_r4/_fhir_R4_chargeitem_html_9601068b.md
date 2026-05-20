# ChargeItem - FHIR v4.0.1Identifiers assigned to this event performer or other systemsReferences the (external) source of pricing information, rules of application for the code this ChargeItem usesReferences the source of pricing information, rules of application for the code this ChargeItem usesThe current state of the ChargeItem (this element modifies the meaning of other elements)Codes identifying the lifecycle stage of a ChargeItem. (Strength=Required)ChargeItems can be grouped to larger ChargeItems covering the whole setA code that identifies the charge, like a billing codeExample set of codes that can be used for billing purposes. (Strength=Example)The individual or set of individuals the action is being or was performed onThe encounter or episode of care that establishes the context for this eventDate/time(s) or duration when the charged service was appliedThe organization requesting the serviceThe organization performing the serviceThe financial cost center permits the tracking of charge attributionQuantity of which the charge item has been servicedThe anatomical location where the related service has been appliedCodes describing anatomical locations. May include laterality. (Strength=Example)Factor overriding the factor determined by the rules associated with the codeTotal price of the charge overriding the list price associated with the codeIf the list price or the rule-based factor associated with the code is overridden, this attribute can capture a text to indicate the  reason for this actionThe device, practitioner, etc. who entered the charge itemDate the charge item was enteredDescribes why the event occurred in coded or textual formExample binding for reason. (Strength=Example)Indicated the rendered service that caused this chargeIdentifies the device, food, drug or other product being charged either by type code or reference to an instanceExample binding for product type. (Strength=Example)Account into which this ChargeItems belongsComments made about the event by the performer, subject or other participantsFurther information supporting this chargeDescribes the type of performance or participation(e.g. primary surgeon, anesthesiologiest, etc.)Codes describing the types of functional roles performers can take on when performing events. (Strength=Example)The device, practitioner, etc. who performed or participated in the serviceIndicates who or what performed or participated in the charged serviceIdentifiers assigned to this event performer or other systemsReferences the (external) source of pricing information, rules of application for the code this ChargeItem usesReferences the source of pricing information, rules of application for the code this ChargeItem usesThe current state of the ChargeItem (this element modifies the meaning of other elements)Codes identifying the lifecycle stage of a ChargeItem. (Strength=Required)ChargeItems can be grouped to larger ChargeItems covering the whole setA code that identifies the charge, like a billing codeExample set of codes that can be used for billing purposes. (Strength=Example)The individual or set of individuals the action is being or was performed onThe encounter or episode of care that establishes the context for this eventDate/time(s) or duration when the charged service was appliedThe organization requesting the serviceThe organization performing the serviceThe financial cost center permits the tracking of charge attributionQuantity of which the charge item has been servicedThe anatomical location where the related service has been appliedCodes describing anatomical locations. May include laterality. (Strength=Example)Factor overriding the factor determined by the rules associated with the codeTotal price of the charge overriding the list price associated with the codeIf the list price or the rule-based factor associated with the code is overridden, this attribute can capture a text to indicate the  reason for this actionThe device, practitioner, etc. who entered the charge itemDate the charge item was enteredDescribes why the event occurred in coded or textual formExample binding for reason. (Strength=Example)Indicated the rendered service that caused this chargeIdentifies the device, food, drug or other product being charged either by type code or reference to an instanceExample binding for product type. (Strength=Example)Account into which this ChargeItems belongsComments made about the event by the performer, subject or other participantsFurther information supporting this chargeDescribes the type of performance or participation(e.g. primary surgeon, anesthesiologiest, etc.)Codes describing the types of functional roles performers can take on when performing events. (Strength=Example)The device, practitioner, etc. who performed or participated in the serviceIndicates who or what performed or participated in the charged service

> Source: https://hl7.org/fhir/R4/chargeitem.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/chargeitem.html) [R4B](http://hl7.org/fhir/R4B/chargeitem.html) **R4** [R3](http://hl7.org/fhir/STU3/chargeitem.html)
 

# 8.24 Resource ChargeItem - Content [
](chargeitem.html#8.24)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 0 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.

 
 
## 8.24.1 Scope and Usage [
](chargeitem.html#scope)

 
Tracking Financial information is vital in Patient Administration and Finance systems in most Healthcare Organizations.
The resource ChargeItem describes the charge for provision of healthcare provider products for a certain patient, 
therefore referring not only to the product, but containing in addition details of the provision, 
like date, time, amounts and participating organizations and persons. 
Main Usage of the ChargeItem is to enable the billing process and internal cost allocation. 
They are created as soon as the products are planned or provisioned, references to Encounters and/or Accounts can be maintained in a later process step.
 

 

The target of ChargeItem.definition may provide information on the Charge code such as pricing and inclusion/exclusion rules as well as 
factors that apply under certain conditions.
In many cases however this information may have been drawn from sources outside of FHIR depending on the distribution format of the code catalogue.
The ChargeItem assumes that such information is either implicitly known by the communicating systems or explicitly shared through the ChargeItem.definition. 
Therefore explicit pricing information is not shared within the ChargeItem resource. 
Also, the systems posting the ChargeItems are not expected to apply the rules associated with the charge codes as they may
 not know the whole context of the patient/encounter to evaluate such rules.

It lies within the responsibility of a billing engine, to collect the ChargeItems in the context of an Account or Encounter at a certain point in time 
(e.g. discharge of the patient) and to evaluate the associated rules resulting in some of the ChargeItems to be set to the status "not billable" 
in case the rules exclude them from being billed, or to create financial transactions according to base price and factors. 
Additional references to Encounter/EpisodeOfCare, Patient/Group and
 Services provide further context to help billing systems determine the appropriate account and establish the clinical/financial context
 to evaluate the rules associated with the charge codes.
 

 

 

 
## 8.24.2 Boundaries and Relationships [
](chargeitem.html#8.24.2)

 
This resource is not an actual financial transaction (such as an item on an invoice or any concise monetary amount being transferred from one Account to another) 
but is the base administrative data that may be used by 
a billing engine to create the financial transactions based on rules, factors and base prices associated with the charge code.

Unlike the Financial Transaction the ChargeItem primarily describes the provision, whereas the Financial Transaction documents cash flow. 
Therefore, the Financial Transaction results from ChargeItems created via the subsequent billing- or cost allocation process. 

 

The actual financial transaction resulting from the evaluation of these rules against the clinical and financial context may be 
represented in formats appropriate to the financial realm.
These are considered out of scope for the FHIR Standard, as they are not specific to the healthcare domain.
The FHIR Claim resource does contain line items, and this ChargeItem resource provides the source material
 for the billing engine to create the items on the claim (which may be different due to business rules).

 

 

 

This resource is referenced by itself and [Invoice](invoice.html#Invoice)

## 8.24.3 
Resource Content
 [
](chargeitem.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [ChargeItem](chargeitem-definitions.html#ChargeItem) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Item containing charge code(s) associated with the provision of healthcare provider products**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](chargeitem-definitions.html#ChargeItem.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for item
 | |

| [definitionUri](chargeitem-definitions.html#ChargeItem.definitionUri) | | 0..* | [uri](datatypes.html#uri) | Defining information about the code of this charge item
 | |

| [definitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical) | | 0..* | [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html)) | Resource defining the code of this ChargeItem
 | |

| [status](chargeitem-definitions.html#ChargeItem.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | planned | billable | not-billable | aborted | billed | entered-in-error | unknown
[ChargeItemStatus](valueset-chargeitem-status.html) ([Required](terminologies.html#required)) | |

| [partOf](chargeitem-definitions.html#ChargeItem.partOf) | | 0..* | [Reference](references.html#Reference)([ChargeItem](chargeitem.html)) | Part of referenced ChargeItem
 | |

| [code](chargeitem-definitions.html#ChargeItem.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | A code that identifies the charge, like a billing code
[ChargeItemCode](valueset-chargeitem-billingcodes.html) ([Example](terminologies.html#example)) | |

| [subject](chargeitem-definitions.html#ChargeItem.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Individual service was done for/to | |

| [context](chargeitem-definitions.html#ChargeItem.context) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html) | [EpisodeOfCare](episodeofcare.html)) | Encounter / Episode associated with event | |

| [occurrence[x]](chargeitem-definitions.html#ChargeItem.occurrence_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | When the charged service was applied | |

| occurrenceDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| occurrencePeriod | | | [Period](datatypes.html#Period) | | |

| occurrenceTiming | | | [Timing](datatypes.html#Timing) | | |

| [performer](chargeitem-definitions.html#ChargeItem.performer) | | 0..* | [BackboneElement](backboneelement.html) | Who performed charged service
 | |

| [function](chargeitem-definitions.html#ChargeItem.performer.function) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What type of performance was done
[Procedure Performer Role Codes](valueset-performer-role.html) ([Example](terminologies.html#example)) | |

| [actor](chargeitem-definitions.html#ChargeItem.performer.actor) | | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [CareTeam](careteam.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html)) | Individual who was performing | |

| [performingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization providing the charged service | |

| [requestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization requesting the charged service | |

| [costCenter](chargeitem-definitions.html#ChargeItem.costCenter) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that has ownership of the (potential, future) revenue | |

| [quantity](chargeitem-definitions.html#ChargeItem.quantity) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Quantity](datatypes.html#Quantity) | Quantity of which the charge item has been serviced | |

| [bodysite](chargeitem-definitions.html#ChargeItem.bodysite) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location, if relevant
[SNOMED CT Body Structures](valueset-body-site.html) ([Example](terminologies.html#example))
 | |

| [factorOverride](chargeitem-definitions.html#ChargeItem.factorOverride) | | 0..1 | [decimal](datatypes.html#decimal) | Factor overriding the associated rules | |

| [priceOverride](chargeitem-definitions.html#ChargeItem.priceOverride) | | 0..1 | [Money](datatypes.html#Money) | Price overriding the associated rules | |

| [overrideReason](chargeitem-definitions.html#ChargeItem.overrideReason) | | 0..1 | [string](datatypes.html#string) | Reason for overriding the list price/factor | |

| [enterer](chargeitem-definitions.html#ChargeItem.enterer) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html)) | Individual who was entering | |

| [enteredDate](chargeitem-definitions.html#ChargeItem.enteredDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | Date the charge item was entered | |

| [reason](chargeitem-definitions.html#ChargeItem.reason) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Why was the charged service rendered?
[ICD-10 Codes](valueset-icd-10.html) ([Example](terminologies.html#example))
 | |

| [service](chargeitem-definitions.html#ChargeItem.service) | | 0..* | [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html) | [ImagingStudy](imagingstudy.html) | [Immunization](immunization.html) | [MedicationAdministration](medicationadministration.html) | [MedicationDispense](medicationdispense.html) | [Observation](observation.html) | [Procedure](procedure.html) | [SupplyDelivery](supplydelivery.html)) | Which rendered service is being charged?
 | |

| [product[x]](chargeitem-definitions.html#ChargeItem.product_x_) | | 0..1 | | Product charged
[FHIR Device Types](valueset-device-kind.html) ([Example](terminologies.html#example)) | |

| productReference | | | [Reference](references.html#Reference)([Device](device.html) | [Medication](medication.html) | [Substance](substance.html)) | | |

| productCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| [account](chargeitem-definitions.html#ChargeItem.account) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Account](account.html)) | Account to place this charge
 | |

| [note](chargeitem-definitions.html#ChargeItem.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the ChargeItem
 | |

| [supportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Further information supporting this charge
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - ChargeItem ([DomainResource](domainresource.html))[Identifiers assigned to this event performer or other systemsidentifier](chargeitem-definitions.html#ChargeItem.identifier) : [Identifier](datatypes.html#Identifier) [0..*][References the (external) source of pricing information, rules of application for the code this ChargeItem usesdefinitionUri](chargeitem-definitions.html#ChargeItem.definitionUri) : [uri](datatypes.html#uri) [0..*][References the source of pricing information, rules of application for the code this ChargeItem usesdefinitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical) : [canonical](datatypes.html#canonical) [0..*] « [ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition) »[The current state of the ChargeItem (this element modifies the meaning of other elements)status](chargeitem-definitions.html#ChargeItem.status) : [code](datatypes.html#code) [1..1] « [Codes identifying the lifecycle stage of a ChargeItem. (Strength=Required)ChargeItemStatus](valueset-chargeitem-status.html)! »[ChargeItems can be grouped to larger ChargeItems covering the whole setpartOf](chargeitem-definitions.html#ChargeItem.partOf) : [Reference](references.html#Reference) [0..*] « [ChargeItem](chargeitem.html#ChargeItem) »[A code that identifies the charge, like a billing codecode](chargeitem-definitions.html#ChargeItem.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Example set of codes that can be used for billing purposes. (Strength=Example)ChargeItemCode](valueset-chargeitem-billingcodes.html)?? »[The individual or set of individuals the action is being or was performed onsubject](chargeitem-definitions.html#ChargeItem.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The encounter or episode of care that establishes the context for this eventcontext](chargeitem-definitions.html#ChargeItem.context) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare) »[Date/time(s) or duration when the charged service was appliedoccurrence[x]](chargeitem-definitions.html#ChargeItem.occurrence_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period)|[Timing](datatypes.html#Timing) »[The organization requesting the serviceperformingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The organization performing the servicerequestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The financial cost center permits the tracking of charge attributioncostCenter](chargeitem-definitions.html#ChargeItem.costCenter) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Quantity of which the charge item has been servicedquantity](chargeitem-definitions.html#ChargeItem.quantity) : [Quantity](datatypes.html#Quantity) [0..1][The anatomical location where the related service has been appliedbodysite](chargeitem-definitions.html#ChargeItem.bodysite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes describing anatomical locations. May include laterality. (Strength=Example)SNOMEDCTBodyStructures](valueset-body-site.html)?? »[Factor overriding the factor determined by the rules associated with the codefactorOverride](chargeitem-definitions.html#ChargeItem.factorOverride) : [decimal](datatypes.html#decimal) [0..1][Total price of the charge overriding the list price associated with the codepriceOverride](chargeitem-definitions.html#ChargeItem.priceOverride) : [Money](datatypes.html#Money) [0..1][If the list price or the rule-based factor associated with the code is overridden, this attribute can capture a text to indicate the reason for this actionoverrideReason](chargeitem-definitions.html#ChargeItem.overrideReason) : [string](datatypes.html#string) [0..1][The device, practitioner, etc. who entered the charge itementerer](chargeitem-definitions.html#ChargeItem.enterer) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson) »[Date the charge item was enteredenteredDate](chargeitem-definitions.html#ChargeItem.enteredDate) : [dateTime](datatypes.html#dateTime) [0..1][Describes why the event occurred in coded or textual formreason](chargeitem-definitions.html#ChargeItem.reason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Example binding for reason. (Strength=Example)ICD-10Codes](valueset-icd-10.html)?? »[Indicated the rendered service that caused this chargeservice](chargeitem-definitions.html#ChargeItem.service) : [Reference](references.html#Reference) [0..*] « [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)| [Immunization](immunization.html#Immunization)|[MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationDispense](medicationdispense.html#MedicationDispense)| [Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|[SupplyDelivery](supplydelivery.html#SupplyDelivery) »[Identifies the device, food, drug or other product being charged either by type code or reference to an instanceproduct[x]](chargeitem-definitions.html#ChargeItem.product_x_) : [Type](formats.html#umlchoice) [0..1] « [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance))| [CodeableConcept](datatypes.html#CodeableConcept); [Example binding for product type. (Strength=Example)FHIRDeviceTypes](valueset-device-kind.html)?? »[Account into which this ChargeItems belongsaccount](chargeitem-definitions.html#ChargeItem.account) : [Reference](references.html#Reference) [0..*] « [Account](account.html#Account) »[Comments made about the event by the performer, subject or other participantsnote](chargeitem-definitions.html#ChargeItem.note) : [Annotation](datatypes.html#Annotation) [0..*][Further information supporting this chargesupportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »Performer[Describes the type of performance or participation(e.g. primary surgeon, anesthesiologiest, etc.)function](chargeitem-definitions.html#ChargeItem.performer.function) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing the types of functional roles performers can take on when performing events. (Strength=Example)ProcedurePerformerRoleCodes](valueset-performer-role.html)?? »[The device, practitioner, etc. who performed or participated in the serviceactor](chargeitem-definitions.html#ChargeItem.performer.actor) : [Reference](references.html#Reference) [1..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson) »
[Indicates who or what performed or participated in the charged serviceperformer](chargeitem-definitions.html#ChargeItem.performer)[0..*]
 

 

 

**XML Template**

 

 
```
<[**ChargeItem**](chargeitem-definitions.html#ChargeItem) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](chargeitem-definitions.html#ChargeItem.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business Identifier for item](terminologies.html#unbound) --></identifier>
 <[**definitionUri**](chargeitem-definitions.html#ChargeItem.definitionUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Defining information about the code of this charge item](terminologies.html#unbound) -->
 <[**definitionCanonical**](chargeitem-definitions.html#ChargeItem.definitionCanonical)><!-- **0..*** [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition)) [Resource defining the code of this ChargeItem](terminologies.html#unbound) --></definitionCanonical>
 <[**status**](chargeitem-definitions.html#ChargeItem.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [planned | billable | not-billable | aborted | billed | entered-in-error | unknown](valueset-chargeitem-status.html) -->
 <[**partOf**](chargeitem-definitions.html#ChargeItem.partOf)><!-- **0..*** [Reference](references.html#Reference)([ChargeItem](chargeitem.html#ChargeItem)) [Part of referenced ChargeItem](terminologies.html#unbound) --></partOf>
 <[**code**](chargeitem-definitions.html#ChargeItem.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [A code that identifies the charge, like a billing code](valueset-chargeitem-billingcodes.html) --></code>
 <[**subject**](chargeitem-definitions.html#ChargeItem.subject)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Individual service was done for/to](terminologies.html#unbound) --></subject>
 <[**context**](chargeitem-definitions.html#ChargeItem.context)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) [Encounter / Episode associated with event](terminologies.html#unbound) --></context>
 <[**occurrence[x]**](chargeitem-definitions.html#ChargeItem.occurrence[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period)|[Timing](datatypes.html#Timing) [When the charged service was applied](terminologies.html#unbound) --></occurrence[x]>
 <[**performer**](chargeitem-definitions.html#ChargeItem.performer)> <!-- **0..*** Who performed charged service -->
 <[**function**](chargeitem-definitions.html#ChargeItem.performer.function)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [What type of performance was done](valueset-performer-role.html) --></function>
 <[**actor**](chargeitem-definitions.html#ChargeItem.performer.actor)><!-- **1..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Individual who was performing](terminologies.html#unbound) --></actor>
 </performer>
 <[**performingOrganization**](chargeitem-definitions.html#ChargeItem.performingOrganization)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization providing the charged service](terminologies.html#unbound) --></performingOrganization>
 <[**requestingOrganization**](chargeitem-definitions.html#ChargeItem.requestingOrganization)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization requesting the charged service](terminologies.html#unbound) --></requestingOrganization>
 <[**costCenter**](chargeitem-definitions.html#ChargeItem.costCenter)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that has ownership of the (potential, future) revenue](terminologies.html#unbound) --></costCenter>
 <[**quantity**](chargeitem-definitions.html#ChargeItem.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity) [Quantity of which the charge item has been serviced](terminologies.html#unbound) --></quantity>
 <[**bodysite**](chargeitem-definitions.html#ChargeItem.bodysite)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Anatomical location, if relevant](valueset-body-site.html) --></bodysite>
 <[**factorOverride**](chargeitem-definitions.html#ChargeItem.factorOverride) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Factor overriding the associated rules](terminologies.html#unbound) -->
 <[**priceOverride**](chargeitem-definitions.html#ChargeItem.priceOverride)><!-- **0..1** [Money](datatypes.html#Money) [Price overriding the associated rules](terminologies.html#unbound) --></priceOverride>
 <[**overrideReason**](chargeitem-definitions.html#ChargeItem.overrideReason) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Reason for overriding the list price/factor](terminologies.html#unbound) -->
 <[**enterer**](chargeitem-definitions.html#ChargeItem.enterer)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Individual who was entering](terminologies.html#unbound) --></enterer>
 <[**enteredDate**](chargeitem-definitions.html#ChargeItem.enteredDate) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [Date the charge item was entered](terminologies.html#unbound) -->
 <[**reason**](chargeitem-definitions.html#ChargeItem.reason)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Why was the charged service rendered?](valueset-icd-10.html) --></reason>
 <[**service**](chargeitem-definitions.html#ChargeItem.service)><!-- **0..*** [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Immunization](immunization.html#Immunization)|
 [MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationDispense](medicationdispense.html#MedicationDispense)|[Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|
 [SupplyDelivery](supplydelivery.html#SupplyDelivery)) [Which rendered service is being charged?](terminologies.html#unbound) --></service>
 <[**product[x]**](chargeitem-definitions.html#ChargeItem.product[x])><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance))|[CodeableConcept](datatypes.html#CodeableConcept) [Product charged](valueset-device-kind.html) --></product[x]>
 <[**account**](chargeitem-definitions.html#ChargeItem.account)><!-- **0..*** [Reference](references.html#Reference)([Account](account.html#Account)) [Account to place this charge](terminologies.html#unbound) --></account>
 <[**note**](chargeitem-definitions.html#ChargeItem.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the ChargeItem](terminologies.html#unbound) --></note>
 <[**supportingInformation**](chargeitem-definitions.html#ChargeItem.supportingInformation)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Further information supporting this charge](terminologies.html#unbound) --></supportingInformation>
</ChargeItem>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**ChargeItem**](chargeitem-definitions.html#ChargeItem)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](chargeitem-definitions.html#ChargeItem.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business Identifier for item](terminologies.html#unbound)
 "[definitionUri](chargeitem-definitions.html#ChargeItem.definitionUri)" : ["<[uri](datatypes.html#uri)>"], // [Defining information about the code of this charge item](terminologies.html#unbound)
 "[definitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical)" : [{ [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition)) }], // [Resource defining the code of this ChargeItem](terminologies.html#unbound)
 "[status](chargeitem-definitions.html#ChargeItem.status)" : "<[code](datatypes.html#code)>", // **R!** [planned | billable | not-billable | aborted | billed | entered-in-error | unknown](valueset-chargeitem-status.html)
 "[partOf](chargeitem-definitions.html#ChargeItem.partOf)" : [{ [Reference](references.html#Reference)([ChargeItem](chargeitem.html#ChargeItem)) }], // [Part of referenced ChargeItem](terminologies.html#unbound)
 "[code](chargeitem-definitions.html#ChargeItem.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [A code that identifies the charge, like a billing code](valueset-chargeitem-billingcodes.html)
 "[subject](chargeitem-definitions.html#ChargeItem.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Individual service was done for/to](terminologies.html#unbound)
 "[context](chargeitem-definitions.html#ChargeItem.context)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) }, // [Encounter / Episode associated with event](terminologies.html#unbound)
 // occurrence[x]: When the charged service was applied. One of these 3:
 "[occurrenceDateTime](chargeitem-definitions.html#ChargeItem.occurrenceDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[occurrencePeriod](chargeitem-definitions.html#ChargeItem.occurrencePeriod)" : { [Period](datatypes.html#Period) },
 "[occurrenceTiming](chargeitem-definitions.html#ChargeItem.occurrenceTiming)" : { [Timing](datatypes.html#Timing) },
 "[performer](chargeitem-definitions.html#ChargeItem.performer)" : [{ // [Who performed charged service](terminologies.html#unbound)
 "[function](chargeitem-definitions.html#ChargeItem.performer.function)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [What type of performance was done](valueset-performer-role.html)
 "[actor](chargeitem-definitions.html#ChargeItem.performer.actor)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) } // **R!** [Individual who was performing](terminologies.html#unbound)
 }],
 "[performingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization providing the charged service](terminologies.html#unbound)
 "[requestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization requesting the charged service](terminologies.html#unbound)
 "[costCenter](chargeitem-definitions.html#ChargeItem.costCenter)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization that has ownership of the (potential, future) revenue](terminologies.html#unbound)
 "[quantity](chargeitem-definitions.html#ChargeItem.quantity)" : { [Quantity](datatypes.html#Quantity) }, // [Quantity of which the charge item has been serviced](terminologies.html#unbound)
 "[bodysite](chargeitem-definitions.html#ChargeItem.bodysite)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Anatomical location, if relevant](valueset-body-site.html)
 "[factorOverride](chargeitem-definitions.html#ChargeItem.factorOverride)" : <[decimal](datatypes.html#decimal)>, // [Factor overriding the associated rules](terminologies.html#unbound)
 "[priceOverride](chargeitem-definitions.html#ChargeItem.priceOverride)" : { [Money](datatypes.html#Money) }, // [Price overriding the associated rules](terminologies.html#unbound)
 "[overrideReason](chargeitem-definitions.html#ChargeItem.overrideReason)" : "<[string](datatypes.html#string)>", // [Reason for overriding the list price/factor](terminologies.html#unbound)
 "[enterer](chargeitem-definitions.html#ChargeItem.enterer)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Individual who was entering](terminologies.html#unbound)
 "[enteredDate](chargeitem-definitions.html#ChargeItem.enteredDate)" : "<[dateTime](datatypes.html#dateTime)>", // [Date the charge item was entered](terminologies.html#unbound)
 "[reason](chargeitem-definitions.html#ChargeItem.reason)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Why was the charged service rendered?](valueset-icd-10.html)
 "[service](chargeitem-definitions.html#ChargeItem.service)" : [{ [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Immunization](immunization.html#Immunization)|
 [MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationDispense](medicationdispense.html#MedicationDispense)|[Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|
 [SupplyDelivery](supplydelivery.html#SupplyDelivery)) }], // [Which rendered service is being charged?](terminologies.html#unbound)
 // product[x]: Product charged. One of these 2:
 "[productReference](chargeitem-definitions.html#ChargeItem.productReference)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance)) },
 "[productCodeableConcept](chargeitem-definitions.html#ChargeItem.productCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[account](chargeitem-definitions.html#ChargeItem.account)" : [{ [Reference](references.html#Reference)([Account](account.html#Account)) }], // [Account to place this charge](terminologies.html#unbound)
 "[note](chargeitem-definitions.html#ChargeItem.note)" : [{ [Annotation](datatypes.html#Annotation) }], // [Comments made about the ChargeItem](terminologies.html#unbound)
 "[supportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }] // [Further information supporting this charge](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**ChargeItem**](chargeitem-definitions.html#ChargeItem);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[ChargeItem.identifier](chargeitem-definitions.html#ChargeItem.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for item
 fhir:[ChargeItem.definitionUri](chargeitem-definitions.html#ChargeItem.definitionUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Defining information about the code of this charge item
 fhir:[ChargeItem.definitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical) [ [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition)) ], ... ; # 0..* Resource defining the code of this ChargeItem
 fhir:[ChargeItem.status](chargeitem-definitions.html#ChargeItem.status) [ [code](datatypes.html#code) ]; # 1..1 planned | billable | not-billable | aborted | billed | entered-in-error | unknown
 fhir:[ChargeItem.partOf](chargeitem-definitions.html#ChargeItem.partOf) [ [Reference](references.html#Reference)([ChargeItem](chargeitem.html#ChargeItem)) ], ... ; # 0..* Part of referenced ChargeItem
 fhir:[ChargeItem.code](chargeitem-definitions.html#ChargeItem.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 A code that identifies the charge, like a billing code
 fhir:[ChargeItem.subject](chargeitem-definitions.html#ChargeItem.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Individual service was done for/to
 fhir:[ChargeItem.context](chargeitem-definitions.html#ChargeItem.context) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) ]; # 0..1 Encounter / Episode associated with event
 # [ChargeItem.occurrence[x]](chargeitem-definitions.html#ChargeItem.occurrence[x]) : 0..1 When the charged service was applied. One of these 3
 fhir:[ChargeItem.occurrenceDateTime](chargeitem-definitions.html#ChargeItem.occurrenceDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[ChargeItem.occurrencePeriod](chargeitem-definitions.html#ChargeItem.occurrencePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[ChargeItem.occurrenceTiming](chargeitem-definitions.html#ChargeItem.occurrenceTiming) [ [Timing](datatypes.html#Timing) ]
 fhir:[ChargeItem.performer](chargeitem-definitions.html#ChargeItem.performer) [ # 0..* Who performed charged service
 fhir:[ChargeItem.performer.function](chargeitem-definitions.html#ChargeItem.performer.function) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 What type of performance was done
 fhir:[ChargeItem.performer.actor](chargeitem-definitions.html#ChargeItem.performer.actor) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 1..1 Individual who was performing
 ], ...;
 fhir:[ChargeItem.performingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization providing the charged service
 fhir:[ChargeItem.requestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization requesting the charged service
 fhir:[ChargeItem.costCenter](chargeitem-definitions.html#ChargeItem.costCenter) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that has ownership of the (potential, future) revenue
 fhir:[ChargeItem.quantity](chargeitem-definitions.html#ChargeItem.quantity) [ [Quantity](datatypes.html#Quantity) ]; # 0..1 Quantity of which the charge item has been serviced
 fhir:[ChargeItem.bodysite](chargeitem-definitions.html#ChargeItem.bodysite) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Anatomical location, if relevant
 fhir:[ChargeItem.factorOverride](chargeitem-definitions.html#ChargeItem.factorOverride) [ [decimal](datatypes.html#decimal) ]; # 0..1 Factor overriding the associated rules
 fhir:[ChargeItem.priceOverride](chargeitem-definitions.html#ChargeItem.priceOverride) [ [Money](datatypes.html#Money) ]; # 0..1 Price overriding the associated rules
 fhir:[ChargeItem.overrideReason](chargeitem-definitions.html#ChargeItem.overrideReason) [ [string](datatypes.html#string) ]; # 0..1 Reason for overriding the list price/factor
 fhir:[ChargeItem.enterer](chargeitem-definitions.html#ChargeItem.enterer) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Individual who was entering
 fhir:[ChargeItem.enteredDate](chargeitem-definitions.html#ChargeItem.enteredDate) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Date the charge item was entered
 fhir:[ChargeItem.reason](chargeitem-definitions.html#ChargeItem.reason) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Why was the charged service rendered?
 fhir:[ChargeItem.service](chargeitem-definitions.html#ChargeItem.service) [ [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Immunization](immunization.html#Immunization)|[MedicationAdministration](medicationadministration.html#MedicationAdministration)|
 [MedicationDispense](medicationdispense.html#MedicationDispense)|[Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|[SupplyDelivery](supplydelivery.html#SupplyDelivery)) ], ... ; # 0..* Which rendered service is being charged?
 # [ChargeItem.product[x]](chargeitem-definitions.html#ChargeItem.product[x]) : 0..1 Product charged. One of these 2
 fhir:[ChargeItem.productReference](chargeitem-definitions.html#ChargeItem.productReference) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance)) ]
 fhir:[ChargeItem.productCodeableConcept](chargeitem-definitions.html#ChargeItem.productCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[ChargeItem.account](chargeitem-definitions.html#ChargeItem.account) [ [Reference](references.html#Reference)([Account](account.html#Account)) ], ... ; # 0..* Account to place this charge
 fhir:[ChargeItem.note](chargeitem-definitions.html#ChargeItem.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the ChargeItem
 fhir:[ChargeItem.supportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Further information supporting this charge
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [ChargeItem](chargeitem.html#ChargeItem)
 | 
 | 
 |

 | 
 ChargeItem.identifier | 
 
 

 Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 ChargeItem.definitionUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.definitionCanonical | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/chargeitem-status to http://hl7.org/fhir/ValueSet/chargeitem-status|4.0.1

 

 | 
 |

 | 
 ChargeItem.performer | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.performer.function | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.performer.actor | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ChargeItem.costCenter | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.enterer | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 ChargeItem.product[x] | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.definition | 
 
 

 - deleted

 

 | 
 |

 | 
 ChargeItem.participant | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](chargeitem.diff.xml) or [JSON](chargeitem.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](chargeitem-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [ChargeItem](chargeitem-definitions.html#ChargeItem) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Item containing charge code(s) associated with the provision of healthcare provider products**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](chargeitem-definitions.html#ChargeItem.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for item
 | |

| [definitionUri](chargeitem-definitions.html#ChargeItem.definitionUri) | | 0..* | [uri](datatypes.html#uri) | Defining information about the code of this charge item
 | |

| [definitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical) | | 0..* | [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html)) | Resource defining the code of this ChargeItem
 | |

| [status](chargeitem-definitions.html#ChargeItem.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | planned | billable | not-billable | aborted | billed | entered-in-error | unknown
[ChargeItemStatus](valueset-chargeitem-status.html) ([Required](terminologies.html#required)) | |

| [partOf](chargeitem-definitions.html#ChargeItem.partOf) | | 0..* | [Reference](references.html#Reference)([ChargeItem](chargeitem.html)) | Part of referenced ChargeItem
 | |

| [code](chargeitem-definitions.html#ChargeItem.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | A code that identifies the charge, like a billing code
[ChargeItemCode](valueset-chargeitem-billingcodes.html) ([Example](terminologies.html#example)) | |

| [subject](chargeitem-definitions.html#ChargeItem.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Individual service was done for/to | |

| [context](chargeitem-definitions.html#ChargeItem.context) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html) | [EpisodeOfCare](episodeofcare.html)) | Encounter / Episode associated with event | |

| [occurrence[x]](chargeitem-definitions.html#ChargeItem.occurrence_x_) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | | When the charged service was applied | |

| occurrenceDateTime | | | [dateTime](datatypes.html#dateTime) | | |

| occurrencePeriod | | | [Period](datatypes.html#Period) | | |

| occurrenceTiming | | | [Timing](datatypes.html#Timing) | | |

| [performer](chargeitem-definitions.html#ChargeItem.performer) | | 0..* | [BackboneElement](backboneelement.html) | Who performed charged service
 | |

| [function](chargeitem-definitions.html#ChargeItem.performer.function) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | What type of performance was done
[Procedure Performer Role Codes](valueset-performer-role.html) ([Example](terminologies.html#example)) | |

| [actor](chargeitem-definitions.html#ChargeItem.performer.actor) | | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [CareTeam](careteam.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html)) | Individual who was performing | |

| [performingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization providing the charged service | |

| [requestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization requesting the charged service | |

| [costCenter](chargeitem-definitions.html#ChargeItem.costCenter) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that has ownership of the (potential, future) revenue | |

| [quantity](chargeitem-definitions.html#ChargeItem.quantity) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Quantity](datatypes.html#Quantity) | Quantity of which the charge item has been serviced | |

| [bodysite](chargeitem-definitions.html#ChargeItem.bodysite) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location, if relevant
[SNOMED CT Body Structures](valueset-body-site.html) ([Example](terminologies.html#example))
 | |

| [factorOverride](chargeitem-definitions.html#ChargeItem.factorOverride) | | 0..1 | [decimal](datatypes.html#decimal) | Factor overriding the associated rules | |

| [priceOverride](chargeitem-definitions.html#ChargeItem.priceOverride) | | 0..1 | [Money](datatypes.html#Money) | Price overriding the associated rules | |

| [overrideReason](chargeitem-definitions.html#ChargeItem.overrideReason) | | 0..1 | [string](datatypes.html#string) | Reason for overriding the list price/factor | |

| [enterer](chargeitem-definitions.html#ChargeItem.enterer) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html)) | Individual who was entering | |

| [enteredDate](chargeitem-definitions.html#ChargeItem.enteredDate) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | Date the charge item was entered | |

| [reason](chargeitem-definitions.html#ChargeItem.reason) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Why was the charged service rendered?
[ICD-10 Codes](valueset-icd-10.html) ([Example](terminologies.html#example))
 | |

| [service](chargeitem-definitions.html#ChargeItem.service) | | 0..* | [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html) | [ImagingStudy](imagingstudy.html) | [Immunization](immunization.html) | [MedicationAdministration](medicationadministration.html) | [MedicationDispense](medicationdispense.html) | [Observation](observation.html) | [Procedure](procedure.html) | [SupplyDelivery](supplydelivery.html)) | Which rendered service is being charged?
 | |

| [product[x]](chargeitem-definitions.html#ChargeItem.product_x_) | | 0..1 | | Product charged
[FHIR Device Types](valueset-device-kind.html) ([Example](terminologies.html#example)) | |

| productReference | | | [Reference](references.html#Reference)([Device](device.html) | [Medication](medication.html) | [Substance](substance.html)) | | |

| productCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| [account](chargeitem-definitions.html#ChargeItem.account) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Account](account.html)) | Account to place this charge
 | |

| [note](chargeitem-definitions.html#ChargeItem.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the ChargeItem
 | |

| [supportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Further information supporting this charge
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - ChargeItem ([DomainResource](domainresource.html))[Identifiers assigned to this event performer or other systemsidentifier](chargeitem-definitions.html#ChargeItem.identifier) : [Identifier](datatypes.html#Identifier) [0..*][References the (external) source of pricing information, rules of application for the code this ChargeItem usesdefinitionUri](chargeitem-definitions.html#ChargeItem.definitionUri) : [uri](datatypes.html#uri) [0..*][References the source of pricing information, rules of application for the code this ChargeItem usesdefinitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical) : [canonical](datatypes.html#canonical) [0..*] « [ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition) »[The current state of the ChargeItem (this element modifies the meaning of other elements)status](chargeitem-definitions.html#ChargeItem.status) : [code](datatypes.html#code) [1..1] « [Codes identifying the lifecycle stage of a ChargeItem. (Strength=Required)ChargeItemStatus](valueset-chargeitem-status.html)! »[ChargeItems can be grouped to larger ChargeItems covering the whole setpartOf](chargeitem-definitions.html#ChargeItem.partOf) : [Reference](references.html#Reference) [0..*] « [ChargeItem](chargeitem.html#ChargeItem) »[A code that identifies the charge, like a billing codecode](chargeitem-definitions.html#ChargeItem.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Example set of codes that can be used for billing purposes. (Strength=Example)ChargeItemCode](valueset-chargeitem-billingcodes.html)?? »[The individual or set of individuals the action is being or was performed onsubject](chargeitem-definitions.html#ChargeItem.subject) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The encounter or episode of care that establishes the context for this eventcontext](chargeitem-definitions.html#ChargeItem.context) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare) »[Date/time(s) or duration when the charged service was appliedoccurrence[x]](chargeitem-definitions.html#ChargeItem.occurrence_x_) : [Type](formats.html#umlchoice) [0..1] « [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period)|[Timing](datatypes.html#Timing) »[The organization requesting the serviceperformingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The organization performing the servicerequestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The financial cost center permits the tracking of charge attributioncostCenter](chargeitem-definitions.html#ChargeItem.costCenter) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Quantity of which the charge item has been servicedquantity](chargeitem-definitions.html#ChargeItem.quantity) : [Quantity](datatypes.html#Quantity) [0..1][The anatomical location where the related service has been appliedbodysite](chargeitem-definitions.html#ChargeItem.bodysite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Codes describing anatomical locations. May include laterality. (Strength=Example)SNOMEDCTBodyStructures](valueset-body-site.html)?? »[Factor overriding the factor determined by the rules associated with the codefactorOverride](chargeitem-definitions.html#ChargeItem.factorOverride) : [decimal](datatypes.html#decimal) [0..1][Total price of the charge overriding the list price associated with the codepriceOverride](chargeitem-definitions.html#ChargeItem.priceOverride) : [Money](datatypes.html#Money) [0..1][If the list price or the rule-based factor associated with the code is overridden, this attribute can capture a text to indicate the reason for this actionoverrideReason](chargeitem-definitions.html#ChargeItem.overrideReason) : [string](datatypes.html#string) [0..1][The device, practitioner, etc. who entered the charge itementerer](chargeitem-definitions.html#ChargeItem.enterer) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson) »[Date the charge item was enteredenteredDate](chargeitem-definitions.html#ChargeItem.enteredDate) : [dateTime](datatypes.html#dateTime) [0..1][Describes why the event occurred in coded or textual formreason](chargeitem-definitions.html#ChargeItem.reason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Example binding for reason. (Strength=Example)ICD-10Codes](valueset-icd-10.html)?? »[Indicated the rendered service that caused this chargeservice](chargeitem-definitions.html#ChargeItem.service) : [Reference](references.html#Reference) [0..*] « [DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)| [Immunization](immunization.html#Immunization)|[MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationDispense](medicationdispense.html#MedicationDispense)| [Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|[SupplyDelivery](supplydelivery.html#SupplyDelivery) »[Identifies the device, food, drug or other product being charged either by type code or reference to an instanceproduct[x]](chargeitem-definitions.html#ChargeItem.product_x_) : [Type](formats.html#umlchoice) [0..1] « [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance))| [CodeableConcept](datatypes.html#CodeableConcept); [Example binding for product type. (Strength=Example)FHIRDeviceTypes](valueset-device-kind.html)?? »[Account into which this ChargeItems belongsaccount](chargeitem-definitions.html#ChargeItem.account) : [Reference](references.html#Reference) [0..*] « [Account](account.html#Account) »[Comments made about the event by the performer, subject or other participantsnote](chargeitem-definitions.html#ChargeItem.note) : [Annotation](datatypes.html#Annotation) [0..*][Further information supporting this chargesupportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »Performer[Describes the type of performance or participation(e.g. primary surgeon, anesthesiologiest, etc.)function](chargeitem-definitions.html#ChargeItem.performer.function) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing the types of functional roles performers can take on when performing events. (Strength=Example)ProcedurePerformerRoleCodes](valueset-performer-role.html)?? »[The device, practitioner, etc. who performed or participated in the serviceactor](chargeitem-definitions.html#ChargeItem.performer.actor) : [Reference](references.html#Reference) [1..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson) »
[Indicates who or what performed or participated in the charged serviceperformer](chargeitem-definitions.html#ChargeItem.performer)[0..*]
 

**XML Template**

 

 
```
<[**ChargeItem**](chargeitem-definitions.html#ChargeItem) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](chargeitem-definitions.html#ChargeItem.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business Identifier for item](terminologies.html#unbound) --></identifier>
 <[**definitionUri**](chargeitem-definitions.html#ChargeItem.definitionUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..*** [Defining information about the code of this charge item](terminologies.html#unbound) -->
 <[**definitionCanonical**](chargeitem-definitions.html#ChargeItem.definitionCanonical)><!-- **0..*** [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition)) [Resource defining the code of this ChargeItem](terminologies.html#unbound) --></definitionCanonical>
 <[**status**](chargeitem-definitions.html#ChargeItem.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [planned | billable | not-billable | aborted | billed | entered-in-error | unknown](valueset-chargeitem-status.html) -->
 <[**partOf**](chargeitem-definitions.html#ChargeItem.partOf)><!-- **0..*** [Reference](references.html#Reference)([ChargeItem](chargeitem.html#ChargeItem)) [Part of referenced ChargeItem](terminologies.html#unbound) --></partOf>
 <[**code**](chargeitem-definitions.html#ChargeItem.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [A code that identifies the charge, like a billing code](valueset-chargeitem-billingcodes.html) --></code>
 <[**subject**](chargeitem-definitions.html#ChargeItem.subject)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Individual service was done for/to](terminologies.html#unbound) --></subject>
 <[**context**](chargeitem-definitions.html#ChargeItem.context)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) [Encounter / Episode associated with event](terminologies.html#unbound) --></context>
 <[**occurrence[x]**](chargeitem-definitions.html#ChargeItem.occurrence[x])><!-- **0..1** [dateTime](datatypes.html#dateTime)|[Period](datatypes.html#Period)|[Timing](datatypes.html#Timing) [When the charged service was applied](terminologies.html#unbound) --></occurrence[x]>
 <[**performer**](chargeitem-definitions.html#ChargeItem.performer)> <!-- **0..*** Who performed charged service -->
 <[**function**](chargeitem-definitions.html#ChargeItem.performer.function)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [What type of performance was done](valueset-performer-role.html) --></function>
 <[**actor**](chargeitem-definitions.html#ChargeItem.performer.actor)><!-- **1..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Individual who was performing](terminologies.html#unbound) --></actor>
 </performer>
 <[**performingOrganization**](chargeitem-definitions.html#ChargeItem.performingOrganization)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization providing the charged service](terminologies.html#unbound) --></performingOrganization>
 <[**requestingOrganization**](chargeitem-definitions.html#ChargeItem.requestingOrganization)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization requesting the charged service](terminologies.html#unbound) --></requestingOrganization>
 <[**costCenter**](chargeitem-definitions.html#ChargeItem.costCenter)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization that has ownership of the (potential, future) revenue](terminologies.html#unbound) --></costCenter>
 <[**quantity**](chargeitem-definitions.html#ChargeItem.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity) [Quantity of which the charge item has been serviced](terminologies.html#unbound) --></quantity>
 <[**bodysite**](chargeitem-definitions.html#ChargeItem.bodysite)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Anatomical location, if relevant](valueset-body-site.html) --></bodysite>
 <[**factorOverride**](chargeitem-definitions.html#ChargeItem.factorOverride) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Factor overriding the associated rules](terminologies.html#unbound) -->
 <[**priceOverride**](chargeitem-definitions.html#ChargeItem.priceOverride)><!-- **0..1** [Money](datatypes.html#Money) [Price overriding the associated rules](terminologies.html#unbound) --></priceOverride>
 <[**overrideReason**](chargeitem-definitions.html#ChargeItem.overrideReason) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Reason for overriding the list price/factor](terminologies.html#unbound) -->
 <[**enterer**](chargeitem-definitions.html#ChargeItem.enterer)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Individual who was entering](terminologies.html#unbound) --></enterer>
 <[**enteredDate**](chargeitem-definitions.html#ChargeItem.enteredDate) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [Date the charge item was entered](terminologies.html#unbound) -->
 <[**reason**](chargeitem-definitions.html#ChargeItem.reason)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Why was the charged service rendered?](valueset-icd-10.html) --></reason>
 <[**service**](chargeitem-definitions.html#ChargeItem.service)><!-- **0..*** [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Immunization](immunization.html#Immunization)|
 [MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationDispense](medicationdispense.html#MedicationDispense)|[Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|
 [SupplyDelivery](supplydelivery.html#SupplyDelivery)) [Which rendered service is being charged?](terminologies.html#unbound) --></service>
 <[**product[x]**](chargeitem-definitions.html#ChargeItem.product[x])><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance))|[CodeableConcept](datatypes.html#CodeableConcept) [Product charged](valueset-device-kind.html) --></product[x]>
 <[**account**](chargeitem-definitions.html#ChargeItem.account)><!-- **0..*** [Reference](references.html#Reference)([Account](account.html#Account)) [Account to place this charge](terminologies.html#unbound) --></account>
 <[**note**](chargeitem-definitions.html#ChargeItem.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the ChargeItem](terminologies.html#unbound) --></note>
 <[**supportingInformation**](chargeitem-definitions.html#ChargeItem.supportingInformation)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Further information supporting this charge](terminologies.html#unbound) --></supportingInformation>
</ChargeItem>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**ChargeItem**](chargeitem-definitions.html#ChargeItem)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](chargeitem-definitions.html#ChargeItem.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business Identifier for item](terminologies.html#unbound)
 "[definitionUri](chargeitem-definitions.html#ChargeItem.definitionUri)" : ["<[uri](datatypes.html#uri)>"], // [Defining information about the code of this charge item](terminologies.html#unbound)
 "[definitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical)" : [{ [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition)) }], // [Resource defining the code of this ChargeItem](terminologies.html#unbound)
 "[status](chargeitem-definitions.html#ChargeItem.status)" : "<[code](datatypes.html#code)>", // **R!** [planned | billable | not-billable | aborted | billed | entered-in-error | unknown](valueset-chargeitem-status.html)
 "[partOf](chargeitem-definitions.html#ChargeItem.partOf)" : [{ [Reference](references.html#Reference)([ChargeItem](chargeitem.html#ChargeItem)) }], // [Part of referenced ChargeItem](terminologies.html#unbound)
 "[code](chargeitem-definitions.html#ChargeItem.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [A code that identifies the charge, like a billing code](valueset-chargeitem-billingcodes.html)
 "[subject](chargeitem-definitions.html#ChargeItem.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // **R!** [Individual service was done for/to](terminologies.html#unbound)
 "[context](chargeitem-definitions.html#ChargeItem.context)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) }, // [Encounter / Episode associated with event](terminologies.html#unbound)
 // occurrence[x]: When the charged service was applied. One of these 3:
 "[occurrenceDateTime](chargeitem-definitions.html#ChargeItem.occurrenceDateTime)" : "<[dateTime](datatypes.html#dateTime)>",
 "[occurrencePeriod](chargeitem-definitions.html#ChargeItem.occurrencePeriod)" : { [Period](datatypes.html#Period) },
 "[occurrenceTiming](chargeitem-definitions.html#ChargeItem.occurrenceTiming)" : { [Timing](datatypes.html#Timing) },
 "[performer](chargeitem-definitions.html#ChargeItem.performer)" : [{ // [Who performed charged service](terminologies.html#unbound)
 "[function](chargeitem-definitions.html#ChargeItem.performer.function)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [What type of performance was done](valueset-performer-role.html)
 "[actor](chargeitem-definitions.html#ChargeItem.performer.actor)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) } // **R!** [Individual who was performing](terminologies.html#unbound)
 }],
 "[performingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization providing the charged service](terminologies.html#unbound)
 "[requestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization requesting the charged service](terminologies.html#unbound)
 "[costCenter](chargeitem-definitions.html#ChargeItem.costCenter)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization that has ownership of the (potential, future) revenue](terminologies.html#unbound)
 "[quantity](chargeitem-definitions.html#ChargeItem.quantity)" : { [Quantity](datatypes.html#Quantity) }, // [Quantity of which the charge item has been serviced](terminologies.html#unbound)
 "[bodysite](chargeitem-definitions.html#ChargeItem.bodysite)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Anatomical location, if relevant](valueset-body-site.html)
 "[factorOverride](chargeitem-definitions.html#ChargeItem.factorOverride)" : <[decimal](datatypes.html#decimal)>, // [Factor overriding the associated rules](terminologies.html#unbound)
 "[priceOverride](chargeitem-definitions.html#ChargeItem.priceOverride)" : { [Money](datatypes.html#Money) }, // [Price overriding the associated rules](terminologies.html#unbound)
 "[overrideReason](chargeitem-definitions.html#ChargeItem.overrideReason)" : "<[string](datatypes.html#string)>", // [Reason for overriding the list price/factor](terminologies.html#unbound)
 "[enterer](chargeitem-definitions.html#ChargeItem.enterer)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Individual who was entering](terminologies.html#unbound)
 "[enteredDate](chargeitem-definitions.html#ChargeItem.enteredDate)" : "<[dateTime](datatypes.html#dateTime)>", // [Date the charge item was entered](terminologies.html#unbound)
 "[reason](chargeitem-definitions.html#ChargeItem.reason)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Why was the charged service rendered?](valueset-icd-10.html)
 "[service](chargeitem-definitions.html#ChargeItem.service)" : [{ [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Immunization](immunization.html#Immunization)|
 [MedicationAdministration](medicationadministration.html#MedicationAdministration)|[MedicationDispense](medicationdispense.html#MedicationDispense)|[Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|
 [SupplyDelivery](supplydelivery.html#SupplyDelivery)) }], // [Which rendered service is being charged?](terminologies.html#unbound)
 // product[x]: Product charged. One of these 2:
 "[productReference](chargeitem-definitions.html#ChargeItem.productReference)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance)) },
 "[productCodeableConcept](chargeitem-definitions.html#ChargeItem.productCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[account](chargeitem-definitions.html#ChargeItem.account)" : [{ [Reference](references.html#Reference)([Account](account.html#Account)) }], // [Account to place this charge](terminologies.html#unbound)
 "[note](chargeitem-definitions.html#ChargeItem.note)" : [{ [Annotation](datatypes.html#Annotation) }], // [Comments made about the ChargeItem](terminologies.html#unbound)
 "[supportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }] // [Further information supporting this charge](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**ChargeItem**](chargeitem-definitions.html#ChargeItem);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[ChargeItem.identifier](chargeitem-definitions.html#ChargeItem.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for item
 fhir:[ChargeItem.definitionUri](chargeitem-definitions.html#ChargeItem.definitionUri) [ [uri](datatypes.html#uri) ], ... ; # 0..* Defining information about the code of this charge item
 fhir:[ChargeItem.definitionCanonical](chargeitem-definitions.html#ChargeItem.definitionCanonical) [ [canonical](datatypes.html#canonical)([ChargeItemDefinition](chargeitemdefinition.html#ChargeItemDefinition)) ], ... ; # 0..* Resource defining the code of this ChargeItem
 fhir:[ChargeItem.status](chargeitem-definitions.html#ChargeItem.status) [ [code](datatypes.html#code) ]; # 1..1 planned | billable | not-billable | aborted | billed | entered-in-error | unknown
 fhir:[ChargeItem.partOf](chargeitem-definitions.html#ChargeItem.partOf) [ [Reference](references.html#Reference)([ChargeItem](chargeitem.html#ChargeItem)) ], ... ; # 0..* Part of referenced ChargeItem
 fhir:[ChargeItem.code](chargeitem-definitions.html#ChargeItem.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 A code that identifies the charge, like a billing code
 fhir:[ChargeItem.subject](chargeitem-definitions.html#ChargeItem.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 1..1 Individual service was done for/to
 fhir:[ChargeItem.context](chargeitem-definitions.html#ChargeItem.context) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) ]; # 0..1 Encounter / Episode associated with event
 # [ChargeItem.occurrence[x]](chargeitem-definitions.html#ChargeItem.occurrence[x]) : 0..1 When the charged service was applied. One of these 3
 fhir:[ChargeItem.occurrenceDateTime](chargeitem-definitions.html#ChargeItem.occurrenceDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[ChargeItem.occurrencePeriod](chargeitem-definitions.html#ChargeItem.occurrencePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[ChargeItem.occurrenceTiming](chargeitem-definitions.html#ChargeItem.occurrenceTiming) [ [Timing](datatypes.html#Timing) ]
 fhir:[ChargeItem.performer](chargeitem-definitions.html#ChargeItem.performer) [ # 0..* Who performed charged service
 fhir:[ChargeItem.performer.function](chargeitem-definitions.html#ChargeItem.performer.function) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 What type of performance was done
 fhir:[ChargeItem.performer.actor](chargeitem-definitions.html#ChargeItem.performer.actor) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 1..1 Individual who was performing
 ], ...;
 fhir:[ChargeItem.performingOrganization](chargeitem-definitions.html#ChargeItem.performingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization providing the charged service
 fhir:[ChargeItem.requestingOrganization](chargeitem-definitions.html#ChargeItem.requestingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization requesting the charged service
 fhir:[ChargeItem.costCenter](chargeitem-definitions.html#ChargeItem.costCenter) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization that has ownership of the (potential, future) revenue
 fhir:[ChargeItem.quantity](chargeitem-definitions.html#ChargeItem.quantity) [ [Quantity](datatypes.html#Quantity) ]; # 0..1 Quantity of which the charge item has been serviced
 fhir:[ChargeItem.bodysite](chargeitem-definitions.html#ChargeItem.bodysite) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Anatomical location, if relevant
 fhir:[ChargeItem.factorOverride](chargeitem-definitions.html#ChargeItem.factorOverride) [ [decimal](datatypes.html#decimal) ]; # 0..1 Factor overriding the associated rules
 fhir:[ChargeItem.priceOverride](chargeitem-definitions.html#ChargeItem.priceOverride) [ [Money](datatypes.html#Money) ]; # 0..1 Price overriding the associated rules
 fhir:[ChargeItem.overrideReason](chargeitem-definitions.html#ChargeItem.overrideReason) [ [string](datatypes.html#string) ]; # 0..1 Reason for overriding the list price/factor
 fhir:[ChargeItem.enterer](chargeitem-definitions.html#ChargeItem.enterer) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Individual who was entering
 fhir:[ChargeItem.enteredDate](chargeitem-definitions.html#ChargeItem.enteredDate) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Date the charge item was entered
 fhir:[ChargeItem.reason](chargeitem-definitions.html#ChargeItem.reason) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Why was the charged service rendered?
 fhir:[ChargeItem.service](chargeitem-definitions.html#ChargeItem.service) [ [Reference](references.html#Reference)([DiagnosticReport](diagnosticreport.html#DiagnosticReport)|[ImagingStudy](imagingstudy.html#ImagingStudy)|[Immunization](immunization.html#Immunization)|[MedicationAdministration](medicationadministration.html#MedicationAdministration)|
 [MedicationDispense](medicationdispense.html#MedicationDispense)|[Observation](observation.html#Observation)|[Procedure](procedure.html#Procedure)|[SupplyDelivery](supplydelivery.html#SupplyDelivery)) ], ... ; # 0..* Which rendered service is being charged?
 # [ChargeItem.product[x]](chargeitem-definitions.html#ChargeItem.product[x]) : 0..1 Product charged. One of these 2
 fhir:[ChargeItem.productReference](chargeitem-definitions.html#ChargeItem.productReference) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Medication](medication.html#Medication)|[Substance](substance.html#Substance)) ]
 fhir:[ChargeItem.productCodeableConcept](chargeitem-definitions.html#ChargeItem.productCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[ChargeItem.account](chargeitem-definitions.html#ChargeItem.account) [ [Reference](references.html#Reference)([Account](account.html#Account)) ], ... ; # 0..* Account to place this charge
 fhir:[ChargeItem.note](chargeitem-definitions.html#ChargeItem.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the ChargeItem
 fhir:[ChargeItem.supportingInformation](chargeitem-definitions.html#ChargeItem.supportingInformation) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Further information supporting this charge
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [ChargeItem](chargeitem.html#ChargeItem)
 | 
 | 
 |

 | 
 ChargeItem.identifier | 
 
 

 Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 ChargeItem.definitionUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.definitionCanonical | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/chargeitem-status to http://hl7.org/fhir/ValueSet/chargeitem-status|4.0.1

 

 | 
 |

 | 
 ChargeItem.performer | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.performer.function | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.performer.actor | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ChargeItem.costCenter | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.enterer | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 ChargeItem.product[x] | 
 
 

 - Added Element

 

 | 
 |

 | 
 ChargeItem.definition | 
 
 

 - deleted

 

 | 
 |

 | 
 ChargeItem.participant | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](chargeitem.diff.xml) or [JSON](chargeitem.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](chargeitem-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](chargeitem-profiles.html) and the alternate definitions:
Master Definition [XML](chargeitem.profile.xml.html) + [JSON](chargeitem.profile.json.html),
[XML](xml.html) [Schema](chargeitem.xsd)/[Schematron](chargeitem.sch) + [JSON](json.html) 
[Schema](chargeitem.schema.json.html), [ShEx](chargeitem.shex.html) (for [Turtle](rdf.html)) + [see the extensions](chargeitem-profiles.html) & the [dependency analysis](chargeitem-dependencies.html)

### 8.24.3.1 
Terminology Bindings
 [
](chargeitem.html#tx)

 | Path | Definition | Type | Reference | |

 | ChargeItem.status | Codes identifying the lifecycle stage of a ChargeItem. | [Required](terminologies.html#required) | [ChargeItemStatus](valueset-chargeitem-status.html) | |

 | ChargeItem.code | Example set of codes that can be used for billing purposes. | [Example](terminologies.html#example) | [ChargeItemCode](valueset-chargeitem-billingcodes.html) | |

 | ChargeItem.performer.function | Codes describing the types of functional roles performers can take on when performing events. | [Example](terminologies.html#example) | [ProcedurePerformerRoleCodes](valueset-performer-role.html) | |

 | ChargeItem.bodysite | Codes describing anatomical locations. May include laterality. | [Example](terminologies.html#example) | [SNOMEDCTBodyStructures](valueset-body-site.html) | |

 | ChargeItem.reason | Example binding for reason. | [Example](terminologies.html#example) | [ICD-10Codes](valueset-icd-10.html) | |

 | ChargeItem.product[x] | Example binding for product type. | [Example](terminologies.html#example) | [FHIRDeviceTypes](valueset-device-kind.html) | |

 

 

## 8.24.4 Search Parameters [
](chargeitem.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| account | [reference](search.html#reference) | Account to place this charge | ChargeItem.account
([Account](account.html)) | | |

| code | [token](search.html#token) | A code that identifies the charge, like a billing code | ChargeItem.code | | |

| context | [reference](search.html#reference) | Encounter / Episode associated with event | ChargeItem.context
([EpisodeOfCare](episodeofcare.html), [Encounter](encounter.html)) | | |

| entered-date | [date](search.html#date) | Date the charge item was entered | ChargeItem.enteredDate | | |

| enterer | [reference](search.html#reference) | Individual who was entering | ChargeItem.enterer
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| factor-override | [number](search.html#number) | Factor overriding the associated rules | ChargeItem.factorOverride | | |

| identifier | [token](search.html#token) | Business Identifier for item | ChargeItem.identifier | | |

| occurrence | [date](search.html#date) | When the charged service was applied | ChargeItem.occurrence | | |

| patient | [reference](search.html#reference) | Individual service was done for/to | ChargeItem.subject.where(resolve() is Patient)
([Patient](patient.html)) | | |

| performer-actor | [reference](search.html#reference) | Individual who was performing | ChargeItem.performer.actor
([Practitioner](practitioner.html), [Organization](organization.html), [CareTeam](careteam.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| performer-function | [token](search.html#token) | What type of performance was done | ChargeItem.performer.function | | |

| performing-organization | [reference](search.html#reference) | Organization providing the charged service | ChargeItem.performingOrganization
([Organization](organization.html)) | | |

| price-override | [quantity](search.html#quantity) | Price overriding the associated rules | ChargeItem.priceOverride | | |

| quantity | [quantity](search.html#quantity) | Quantity of which the charge item has been serviced | ChargeItem.quantity | | |

| requesting-organization | [reference](search.html#reference) | Organization requesting the charged service | ChargeItem.requestingOrganization
([Organization](organization.html)) | | |

| service | [reference](search.html#reference) | Which rendered service is being charged? | ChargeItem.service
([Immunization](immunization.html), [MedicationDispense](medicationdispense.html), [SupplyDelivery](supplydelivery.html), [Observation](observation.html), [DiagnosticReport](diagnosticreport.html), [ImagingStudy](imagingstudy.html), [MedicationAdministration](medicationadministration.html), [Procedure](procedure.html)) | | |

| subject | [reference](search.html#reference) | Individual service was done for/to | ChargeItem.subject
([Group](group.html), [Patient](patient.html)) | | |