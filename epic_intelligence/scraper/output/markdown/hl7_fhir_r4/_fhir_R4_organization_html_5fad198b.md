# Organization - FHIR v4.0.1Identifier for the organization that is used to identify the organization across multiple disparate systemsWhether the organization's record is still in active use (this element modifies the meaning of other elements)The kind(s) of organization that this isUsed to categorize the organization. (Strength=Example)A name associated with the organizationA list of alternate names that the organization is known as, or was known as in the pastA contact detail for the organizationAn address for the organizationThe organization of which this organization forms a partTechnical endpoints providing access to services operated for the organizationIndicates a purpose for which the contact can be reachedThe purpose for which you would contact a contact party. (Strength=Extensible)A name associated with the contactA contact detail (e.g. a telephone number or an email address) by which the party may be contactedVisiting or postal addresses for the contactContact for the organization for a certain purposeIdentifier for the organization that is used to identify the organization across multiple disparate systemsWhether the organization's record is still in active use (this element modifies the meaning of other elements)The kind(s) of organization that this isUsed to categorize the organization. (Strength=Example)A name associated with the organizationA list of alternate names that the organization is known as, or was known as in the pastA contact detail for the organizationAn address for the organizationThe organization of which this organization forms a partTechnical endpoints providing access to services operated for the organizationIndicates a purpose for which the contact can be reachedThe purpose for which you would contact a contact party. (Strength=Extensible)A name associated with the contactA contact detail (e.g. a telephone number or an email address) by which the party may be contactedVisiting or postal addresses for the contactContact for the organization for a certain purpose

> Source: https://hl7.org/fhir/R4/organization.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/organization.html) [R4B](http://hl7.org/fhir/R4B/organization.html) **R4** [R3](http://hl7.org/fhir/STU3/organization.html) [R2](http://hl7.org/fhir/DSTU2/organization.html)
 

# 8.6 Resource Organization - Content [
](organization.html#8.6)

| [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Business | [Compartments](compartmentdefinition.html): Not linked to any defined compartments | |

A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.

## 8.6.1 Scope and Usage [
](organization.html#scope)

This resource may be used in a shared registry of contact and other information for various organizations or it can be used merely as a support
for other resources that need to reference organizations, perhaps as a [document](documents.html), [message](messaging.html) or 
as a [contained](references.html#contained) resource. If using a registry approach, it's entirely possible for multiple registries to exist, each dealing
with different types or levels of organization.

## 8.6.2 Boundaries and Relationships [
](organization.html#bnr)

The Organization resource is used for collections of people that have come together to achieve an objective. 
The [Group](group.html) resource is used to identify a collection of people (or animals, devices, etc.) 
that are gathered for the purpose of analysis or acting upon, but are not expected to act themselves.

 

 The Organization resource often exists as a hierarchy of organization resources, using the part-of* property to provide
 the association of the child to its parent organization.**
 This organizational hierarchy helps communicate the conceptual structure, whereas the Location resource provides the physical
 representation of the hierarchy.

 The linkage between Organization and Location is from each point in the location hierarchy to the appropriate level in the 
 Organization hierarchy. These links don't all have to be to the top level Organization.

 When populating the organization and location hierarchies there is often not a clear distinction between these 2, however
 to assist in making the decision, Locations are always used for recording where a service occurs, and hence where encounters
 and observations are associated. The Organization property on these resources might not be the location where the service took place.
 

This resource is referenced by [Annotation](datatypes.html#Annotation), [Identifier](datatypes.html#Identifier), [Signature](datatypes.html#Signature), [UsageContext](metadatatypes.html#UsageContext), [Account](account.html#Account), [AuditEvent](auditevent.html#AuditEvent), [Basic](basic.html#Basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct), [CapabilityStatement](capabilitystatement.html#CapabilityStatement), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [CatalogEntry](catalogentry.html#CatalogEntry), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [Coverage](coverage.html#Coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [Device](device.html#Device), [DeviceDefinition](devicedefinition.html#DeviceDefinition), [DeviceRequest](devicerequest.html#DeviceRequest), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [Encounter](encounter.html#Encounter), [Endpoint](endpoint.html#Endpoint), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [EnrollmentResponse](enrollmentresponse.html#EnrollmentResponse), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [Goal](goal.html#Goal), [Group](group.html#Group), [HealthcareService](healthcareservice.html#HealthcareService), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [ImmunizationEvaluation](immunizationevaluation.html#ImmunizationEvaluation), [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation), [InsurancePlan](insuranceplan.html#InsurancePlan), [Invoice](invoice.html#Invoice), [Linkage](linkage.html#Linkage), [Location](location.html#Location), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [Medication](medication.html#Medication), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationKnowledge](medicationknowledge.html#MedicationKnowledge), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MedicinalProduct](medicinalproduct.html#MedicinalProduct), [MedicinalProductAuthorization](medicinalproductauthorization.html#MedicinalProductAuthorization), [MedicinalProductIngredient](medicinalproductingredient.html#MedicinalProductIngredient), [MedicinalProductManufactured](medicinalproductmanufactured.html#MedicinalProductManufactured), [MedicinalProductPackaged](medicinalproductpackaged.html#MedicinalProductPackaged), [MessageHeader](messageheader.html#MessageHeader), [MolecularSequence](molecularsequence.html#MolecularSequence), [Observation](observation.html#Observation), itself, [OrganizationAffiliation](organizationaffiliation.html#OrganizationAffiliation), [Patient](patient.html#Patient), [PaymentNotice](paymentnotice.html#PaymentNotice), [PaymentReconciliation](paymentreconciliation.html#PaymentReconciliation), [Person](person.html#Person), [Practitioner](practitioner.html#Practitioner), [PractitionerRole](practitionerrole.html#PractitionerRole), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [ResearchStudy](researchstudy.html#ResearchStudy), [ServiceRequest](servicerequest.html#ServiceRequest), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest), [Task](task.html#Task) and [VerificationResult](verificationresult.html#VerificationResult)

## 8.6.3 
Resource Content
 [
](organization.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[*](formats.html#table) | |
| [Organization](organization-definitions.html#Organization) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A grouping of people or organizations with a common purpose**+ Rule: The organization SHALL at least have a name or an identifier, and possibly more than one
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](organization-definitions.html#Organization.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..* | [Identifier](datatypes.html#Identifier) | Identifies this organization across multiple systems
 | |

| [active](organization-definitions.html#Organization.active) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether the organization's record is still in active use | |

| [type](organization-definitions.html#Organization.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of organization
[Organization type](valueset-organization-type.html) ([Example](terminologies.html#example))
 | |

| [name](organization-definitions.html#Organization.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..1 | [string](datatypes.html#string) | Name used for the organization | |

| [alias](organization-definitions.html#Organization.alias) | | 0..* | [string](datatypes.html#string) | A list of alternate names that the organization is known as, or was known as in the past
 | |

| [telecom](organization-definitions.html#Organization.telecom) | [I](conformance-rules.html#constraints) | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the organization
+ Rule: The telecom of an organization can never be of use 'home'
 | |

| [address](organization-definitions.html#Organization.address) | [I](conformance-rules.html#constraints) | 0..* | [Address](datatypes.html#Address) | An address for the organization
+ Rule: An address of an organization can never be of use 'home'
 | |

| [partOf](organization-definitions.html#Organization.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization of which this organization forms a part | |

| [contact](organization-definitions.html#Organization.contact) | | 0..* | [BackboneElement](backboneelement.html) | Contact for the organization for a certain purpose
 | |

| [purpose](organization-definitions.html#Organization.contact.purpose) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of contact
[Contact entity type](valueset-contactentity-type.html) ([Extensible](terminologies.html#extensible)) | |

| [name](organization-definitions.html#Organization.contact.name) | | 0..1 | [HumanName](datatypes.html#HumanName) | A name associated with the contact | |

| [telecom](organization-definitions.html#Organization.contact.telecom) | | 0..* | [ContactPoint](datatypes.html#ContactPoint) | Contact details (telephone, email, etc.) for a contact
 | |

| [address](organization-definitions.html#Organization.contact.address) | | 0..1 | [Address](datatypes.html#Address) | Visiting or postal addresses for the contact | |

| [endpoint](organization-definitions.html#Organization.endpoint) | | 0..* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the organization
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Organization ([DomainResource](domainresource.html))[Identifier for the organization that is used to identify the organization across multiple disparate systemsidentifier](organization-definitions.html#Organization.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether the organization's record is still in active use (this element modifies the meaning of other elements)active](organization-definitions.html#Organization.active) : [boolean](datatypes.html#boolean) [0..1][The kind(s) of organization that this istype](organization-definitions.html#Organization.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Used to categorize the organization. (Strength=Example)OrganizationType](valueset-organization-type.html)?? »[A name associated with the organizationname](organization-definitions.html#Organization.name) : [string](datatypes.html#string) [0..1][A list of alternate names that the organization is known as, or was known as in the pastalias](organization-definitions.html#Organization.alias) : [string](datatypes.html#string) [0..*][A contact detail for the organizationtelecom](organization-definitions.html#Organization.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][An address for the organizationaddress](organization-definitions.html#Organization.address) : [Address](datatypes.html#Address) [0..*][The organization of which this organization forms a partpartOf](organization-definitions.html#Organization.partOf) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Technical endpoints providing access to services operated for the organizationendpoint](organization-definitions.html#Organization.endpoint) : [Reference](references.html#Reference) [0..*] « [Endpoint](endpoint.html#Endpoint) »Contact[Indicates a purpose for which the contact can be reachedpurpose](organization-definitions.html#Organization.contact.purpose) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The purpose for which you would contact a contact party. (Strength=Extensible)ContactEntityType](valueset-contactentity-type.html)+ »[A name associated with the contactname](organization-definitions.html#Organization.contact.name) : [HumanName](datatypes.html#HumanName) [0..1][A contact detail (e.g. a telephone number or an email address) by which the party may be contactedtelecom](organization-definitions.html#Organization.contact.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Visiting or postal addresses for the contactaddress](organization-definitions.html#Organization.contact.address) : [Address](datatypes.html#Address) [0..1]
[Contact for the organization for a certain purposecontact](organization-definitions.html#Organization.contact)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Organization**](organization-definitions.html#Organization) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](organization-definitions.html#Organization.identifier)><!-- ** 0..*** [Identifier](datatypes.html#Identifier) [Identifies this organization across multiple systems](terminologies.html#unbound) --></identifier>
 <[**active**](organization-definitions.html#Organization.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether the organization's record is still in active use](terminologies.html#unbound) -->
 <[**type**](organization-definitions.html#Organization.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of organization](valueset-organization-type.html) --></type>
 <[**name**](organization-definitions.html#Organization.name) value="[[string](datatypes.html#string)]"/><!-- ** 0..1** [Name used for the organization](terminologies.html#unbound) -->
 <[**alias**](organization-definitions.html#Organization.alias) value="[[string](datatypes.html#string)]"/><!-- **0..*** [A list of alternate names that the organization is known as, or was known as in the past](terminologies.html#unbound) -->
 <[**telecom**](organization-definitions.html#Organization.telecom)><!-- ** 0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the organization](terminologies.html#unbound) --></telecom>
 <[**address**](organization-definitions.html#Organization.address)><!-- ** 0..*** [Address](datatypes.html#Address) [An address for the organization](terminologies.html#unbound) --></address>
 <[**partOf**](organization-definitions.html#Organization.partOf)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [The organization of which this organization forms a part](terminologies.html#unbound) --></partOf>
 <[**contact**](organization-definitions.html#Organization.contact)> <!-- **0..*** Contact for the organization for a certain purpose -->
 <[**purpose**](organization-definitions.html#Organization.contact.purpose)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The type of contact](valueset-contactentity-type.html) --></purpose>
 <[**name**](organization-definitions.html#Organization.contact.name)><!-- **0..1** [HumanName](datatypes.html#HumanName) [A name associated with the contact](terminologies.html#unbound) --></name>
 <[**telecom**](organization-definitions.html#Organization.contact.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [Contact details (telephone, email, etc.) for a contact](terminologies.html#unbound) --></telecom>
 <[**address**](organization-definitions.html#Organization.contact.address)><!-- **0..1** [Address](datatypes.html#Address) [Visiting or postal addresses for the contact](terminologies.html#unbound) --></address>
 </contact>
 <[**endpoint**](organization-definitions.html#Organization.endpoint)><!-- **0..*** [Reference](references.html#Reference)([Endpoint](endpoint.html#Endpoint)) [Technical endpoints providing access to services operated for the organization](terminologies.html#unbound) --></endpoint>
</Organization>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Organization**](organization-definitions.html#Organization)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](organization-definitions.html#Organization.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // **C?** [Identifies this organization across multiple systems](terminologies.html#unbound)
 "[active](organization-definitions.html#Organization.active)" : <[boolean](datatypes.html#boolean)>, // [Whether the organization's record is still in active use](terminologies.html#unbound)
 "[type](organization-definitions.html#Organization.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Kind of organization](valueset-organization-type.html)
 "[name](organization-definitions.html#Organization.name)" : "<[string](datatypes.html#string)>", // **C?** [Name used for the organization](terminologies.html#unbound)
 "[alias](organization-definitions.html#Organization.alias)" : ["<[string](datatypes.html#string)>"], // [A list of alternate names that the organization is known as, or was known as in the past](terminologies.html#unbound)
 "[telecom](organization-definitions.html#Organization.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // **C?** [A contact detail for the organization](terminologies.html#unbound)
 "[address](organization-definitions.html#Organization.address)" : [{ [Address](datatypes.html#Address) }], // **C?** [An address for the organization](terminologies.html#unbound)
 "[partOf](organization-definitions.html#Organization.partOf)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [The organization of which this organization forms a part](terminologies.html#unbound)
 "[contact](organization-definitions.html#Organization.contact)" : [{ // [Contact for the organization for a certain purpose](terminologies.html#unbound)
 "[purpose](organization-definitions.html#Organization.contact.purpose)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The type of contact](valueset-contactentity-type.html)
 "[name](organization-definitions.html#Organization.contact.name)" : { [HumanName](datatypes.html#HumanName) }, // [A name associated with the contact](terminologies.html#unbound)
 "[telecom](organization-definitions.html#Organization.contact.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [Contact details (telephone, email, etc.) for a contact](terminologies.html#unbound)
 "[address](organization-definitions.html#Organization.contact.address)" : { [Address](datatypes.html#Address) } // [Visiting or postal addresses for the contact](terminologies.html#unbound)
 }],
 "[endpoint](organization-definitions.html#Organization.endpoint)" : [{ [Reference](references.html#Reference)([Endpoint](endpoint.html#Endpoint)) }] // [Technical endpoints providing access to services operated for the organization](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Organization**](organization-definitions.html#Organization);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Organization.identifier](organization-definitions.html#Organization.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Identifies this organization across multiple systems
 fhir:[Organization.active](organization-definitions.html#Organization.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether the organization's record is still in active use
 fhir:[Organization.type](organization-definitions.html#Organization.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Kind of organization
 fhir:[Organization.name](organization-definitions.html#Organization.name) [ [string](datatypes.html#string) ]; # 0..1 Name used for the organization
 fhir:[Organization.alias](organization-definitions.html#Organization.alias) [ [string](datatypes.html#string) ], ... ; # 0..* A list of alternate names that the organization is known as, or was known as in the past
 fhir:[Organization.telecom](organization-definitions.html#Organization.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the organization
 fhir:[Organization.address](organization-definitions.html#Organization.address) [ [Address](datatypes.html#Address) ], ... ; # 0..* An address for the organization
 fhir:[Organization.partOf](organization-definitions.html#Organization.partOf) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 The organization of which this organization forms a part
 fhir:[Organization.contact](organization-definitions.html#Organization.contact) [ # 0..* Contact for the organization for a certain purpose
 fhir:[Organization.contact.purpose](organization-definitions.html#Organization.contact.purpose) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The type of contact
 fhir:[Organization.contact.name](organization-definitions.html#Organization.contact.name) [ [HumanName](datatypes.html#HumanName) ]; # 0..1 A name associated with the contact
 fhir:[Organization.contact.telecom](organization-definitions.html#Organization.contact.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* Contact details (telephone, email, etc.) for a contact
 fhir:[Organization.contact.address](organization-definitions.html#Organization.contact.address) [ [Address](datatypes.html#Address) ]; # 0..1 Visiting or postal addresses for the contact
 ], ...;
 fhir:[Organization.endpoint](organization-definitions.html#Organization.endpoint) [ [Reference](references.html#Reference)([Endpoint](endpoint.html#Endpoint)) ], ... ; # 0..* Technical endpoints providing access to services operated for the organization
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Organization](organization.html#Organization)
 | 
 | 
 |

 | 
 Organization.active | 
 
 

 Default Value "true" removed

 

 | 
 |

 | 
 Organization.contact.purpose | 
 
 

 - Change code system for extensibly bound codes from "http://hl7.org/fhir/contactentity-type" to "http://terminology.hl7.org/CodeSystem/contactentity-type"

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](organization.diff.xml) or [JSON](organization.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](organization-version-maps.html) (status = 11 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Organization](organization-definitions.html#Organization) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A grouping of people or organizations with a common purpose**+ Rule: The organization SHALL at least have a name or an identifier, and possibly more than one
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](organization-definitions.html#Organization.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..* | [Identifier](datatypes.html#Identifier) | Identifies this organization across multiple systems
 | |

| [active](organization-definitions.html#Organization.active) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether the organization's record is still in active use | |

| [type](organization-definitions.html#Organization.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of organization
[Organization type](valueset-organization-type.html) ([Example](terminologies.html#example))
 | |

| [name](organization-definitions.html#Organization.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..1 | [string](datatypes.html#string) | Name used for the organization | |

| [alias](organization-definitions.html#Organization.alias) | | 0..* | [string](datatypes.html#string) | A list of alternate names that the organization is known as, or was known as in the past
 | |

| [telecom](organization-definitions.html#Organization.telecom) | [I](conformance-rules.html#constraints) | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the organization
+ Rule: The telecom of an organization can never be of use 'home'
 | |

| [address](organization-definitions.html#Organization.address) | [I](conformance-rules.html#constraints) | 0..* | [Address](datatypes.html#Address) | An address for the organization
+ Rule: An address of an organization can never be of use 'home'
 | |

| [partOf](organization-definitions.html#Organization.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization of which this organization forms a part | |

| [contact](organization-definitions.html#Organization.contact) | | 0..* | [BackboneElement](backboneelement.html) | Contact for the organization for a certain purpose
 | |

| [purpose](organization-definitions.html#Organization.contact.purpose) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of contact
[Contact entity type](valueset-contactentity-type.html) ([Extensible](terminologies.html#extensible)) | |

| [name](organization-definitions.html#Organization.contact.name) | | 0..1 | [HumanName](datatypes.html#HumanName) | A name associated with the contact | |

| [telecom](organization-definitions.html#Organization.contact.telecom) | | 0..* | [ContactPoint](datatypes.html#ContactPoint) | Contact details (telephone, email, etc.) for a contact
 | |

| [address](organization-definitions.html#Organization.contact.address) | | 0..1 | [Address](datatypes.html#Address) | Visiting or postal addresses for the contact | |

| [endpoint](organization-definitions.html#Organization.endpoint) | | 0..* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the organization
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Organization ([DomainResource](domainresource.html))[Identifier for the organization that is used to identify the organization across multiple disparate systemsidentifier](organization-definitions.html#Organization.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether the organization's record is still in active use (this element modifies the meaning of other elements)active](organization-definitions.html#Organization.active) : [boolean](datatypes.html#boolean) [0..1][The kind(s) of organization that this istype](organization-definitions.html#Organization.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Used to categorize the organization. (Strength=Example)OrganizationType](valueset-organization-type.html)?? »[A name associated with the organizationname](organization-definitions.html#Organization.name) : [string](datatypes.html#string) [0..1][A list of alternate names that the organization is known as, or was known as in the pastalias](organization-definitions.html#Organization.alias) : [string](datatypes.html#string) [0..*][A contact detail for the organizationtelecom](organization-definitions.html#Organization.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][An address for the organizationaddress](organization-definitions.html#Organization.address) : [Address](datatypes.html#Address) [0..*][The organization of which this organization forms a partpartOf](organization-definitions.html#Organization.partOf) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Technical endpoints providing access to services operated for the organizationendpoint](organization-definitions.html#Organization.endpoint) : [Reference](references.html#Reference) [0..*] « [Endpoint](endpoint.html#Endpoint) »Contact[Indicates a purpose for which the contact can be reachedpurpose](organization-definitions.html#Organization.contact.purpose) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The purpose for which you would contact a contact party. (Strength=Extensible)ContactEntityType](valueset-contactentity-type.html)+ »[A name associated with the contactname](organization-definitions.html#Organization.contact.name) : [HumanName](datatypes.html#HumanName) [0..1][A contact detail (e.g. a telephone number or an email address) by which the party may be contactedtelecom](organization-definitions.html#Organization.contact.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Visiting or postal addresses for the contactaddress](organization-definitions.html#Organization.contact.address) : [Address](datatypes.html#Address) [0..1]
[Contact for the organization for a certain purposecontact](organization-definitions.html#Organization.contact)[0..*]
 

**XML Template**

 

 
```
<[**Organization**](organization-definitions.html#Organization) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](organization-definitions.html#Organization.identifier)><!-- ** 0..*** [Identifier](datatypes.html#Identifier) [Identifies this organization across multiple systems](terminologies.html#unbound) --></identifier>
 <[**active**](organization-definitions.html#Organization.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether the organization's record is still in active use](terminologies.html#unbound) -->
 <[**type**](organization-definitions.html#Organization.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of organization](valueset-organization-type.html) --></type>
 <[**name**](organization-definitions.html#Organization.name) value="[[string](datatypes.html#string)]"/><!-- ** 0..1** [Name used for the organization](terminologies.html#unbound) -->
 <[**alias**](organization-definitions.html#Organization.alias) value="[[string](datatypes.html#string)]"/><!-- **0..*** [A list of alternate names that the organization is known as, or was known as in the past](terminologies.html#unbound) -->
 <[**telecom**](organization-definitions.html#Organization.telecom)><!-- ** 0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the organization](terminologies.html#unbound) --></telecom>
 <[**address**](organization-definitions.html#Organization.address)><!-- ** 0..*** [Address](datatypes.html#Address) [An address for the organization](terminologies.html#unbound) --></address>
 <[**partOf**](organization-definitions.html#Organization.partOf)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [The organization of which this organization forms a part](terminologies.html#unbound) --></partOf>
 <[**contact**](organization-definitions.html#Organization.contact)> <!-- **0..*** Contact for the organization for a certain purpose -->
 <[**purpose**](organization-definitions.html#Organization.contact.purpose)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The type of contact](valueset-contactentity-type.html) --></purpose>
 <[**name**](organization-definitions.html#Organization.contact.name)><!-- **0..1** [HumanName](datatypes.html#HumanName) [A name associated with the contact](terminologies.html#unbound) --></name>
 <[**telecom**](organization-definitions.html#Organization.contact.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [Contact details (telephone, email, etc.) for a contact](terminologies.html#unbound) --></telecom>
 <[**address**](organization-definitions.html#Organization.contact.address)><!-- **0..1** [Address](datatypes.html#Address) [Visiting or postal addresses for the contact](terminologies.html#unbound) --></address>
 </contact>
 <[**endpoint**](organization-definitions.html#Organization.endpoint)><!-- **0..*** [Reference](references.html#Reference)([Endpoint](endpoint.html#Endpoint)) [Technical endpoints providing access to services operated for the organization](terminologies.html#unbound) --></endpoint>
</Organization>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Organization**](organization-definitions.html#Organization)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](organization-definitions.html#Organization.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // **C?** [Identifies this organization across multiple systems](terminologies.html#unbound)
 "[active](organization-definitions.html#Organization.active)" : <[boolean](datatypes.html#boolean)>, // [Whether the organization's record is still in active use](terminologies.html#unbound)
 "[type](organization-definitions.html#Organization.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Kind of organization](valueset-organization-type.html)
 "[name](organization-definitions.html#Organization.name)" : "<[string](datatypes.html#string)>", // **C?** [Name used for the organization](terminologies.html#unbound)
 "[alias](organization-definitions.html#Organization.alias)" : ["<[string](datatypes.html#string)>"], // [A list of alternate names that the organization is known as, or was known as in the past](terminologies.html#unbound)
 "[telecom](organization-definitions.html#Organization.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // **C?** [A contact detail for the organization](terminologies.html#unbound)
 "[address](organization-definitions.html#Organization.address)" : [{ [Address](datatypes.html#Address) }], // **C?** [An address for the organization](terminologies.html#unbound)
 "[partOf](organization-definitions.html#Organization.partOf)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [The organization of which this organization forms a part](terminologies.html#unbound)
 "[contact](organization-definitions.html#Organization.contact)" : [{ // [Contact for the organization for a certain purpose](terminologies.html#unbound)
 "[purpose](organization-definitions.html#Organization.contact.purpose)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The type of contact](valueset-contactentity-type.html)
 "[name](organization-definitions.html#Organization.contact.name)" : { [HumanName](datatypes.html#HumanName) }, // [A name associated with the contact](terminologies.html#unbound)
 "[telecom](organization-definitions.html#Organization.contact.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [Contact details (telephone, email, etc.) for a contact](terminologies.html#unbound)
 "[address](organization-definitions.html#Organization.contact.address)" : { [Address](datatypes.html#Address) } // [Visiting or postal addresses for the contact](terminologies.html#unbound)
 }],
 "[endpoint](organization-definitions.html#Organization.endpoint)" : [{ [Reference](references.html#Reference)([Endpoint](endpoint.html#Endpoint)) }] // [Technical endpoints providing access to services operated for the organization](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Organization**](organization-definitions.html#Organization);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Organization.identifier](organization-definitions.html#Organization.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Identifies this organization across multiple systems
 fhir:[Organization.active](organization-definitions.html#Organization.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether the organization's record is still in active use
 fhir:[Organization.type](organization-definitions.html#Organization.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Kind of organization
 fhir:[Organization.name](organization-definitions.html#Organization.name) [ [string](datatypes.html#string) ]; # 0..1 Name used for the organization
 fhir:[Organization.alias](organization-definitions.html#Organization.alias) [ [string](datatypes.html#string) ], ... ; # 0..* A list of alternate names that the organization is known as, or was known as in the past
 fhir:[Organization.telecom](organization-definitions.html#Organization.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the organization
 fhir:[Organization.address](organization-definitions.html#Organization.address) [ [Address](datatypes.html#Address) ], ... ; # 0..* An address for the organization
 fhir:[Organization.partOf](organization-definitions.html#Organization.partOf) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 The organization of which this organization forms a part
 fhir:[Organization.contact](organization-definitions.html#Organization.contact) [ # 0..* Contact for the organization for a certain purpose
 fhir:[Organization.contact.purpose](organization-definitions.html#Organization.contact.purpose) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The type of contact
 fhir:[Organization.contact.name](organization-definitions.html#Organization.contact.name) [ [HumanName](datatypes.html#HumanName) ]; # 0..1 A name associated with the contact
 fhir:[Organization.contact.telecom](organization-definitions.html#Organization.contact.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* Contact details (telephone, email, etc.) for a contact
 fhir:[Organization.contact.address](organization-definitions.html#Organization.contact.address) [ [Address](datatypes.html#Address) ]; # 0..1 Visiting or postal addresses for the contact
 ], ...;
 fhir:[Organization.endpoint](organization-definitions.html#Organization.endpoint) [ [Reference](references.html#Reference)([Endpoint](endpoint.html#Endpoint)) ], ... ; # 0..* Technical endpoints providing access to services operated for the organization
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Organization](organization.html#Organization)
 | 
 | 
 |

 | 
 Organization.active | 
 
 

 Default Value "true" removed

 

 | 
 |

 | 
 Organization.contact.purpose | 
 
 

 - Change code system for extensibly bound codes from "http://hl7.org/fhir/contactentity-type" to "http://terminology.hl7.org/CodeSystem/contactentity-type"

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](organization.diff.xml) or [JSON](organization.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](organization-version-maps.html) (status = 11 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](organization-profiles.html) and the alternate definitions:
Master Definition [XML](organization.profile.xml.html) + [JSON](organization.profile.json.html),
[XML](xml.html) [Schema](organization.xsd)/[Schematron](organization.sch) + [JSON](json.html) 
[Schema](organization.schema.json.html), [ShEx](organization.shex.html) (for [Turtle](rdf.html)) + [see the extensions](organization-profiles.html) & the [dependency analysis](organization-dependencies.html)

### 8.6.3.1 
Terminology Bindings
 [
](organization.html#tx)

 | Path | Definition | Type | Reference | |

 | Organization.type | Used to categorize the organization. | [Example](terminologies.html#example) | [OrganizationType](valueset-organization-type.html) | |

 | Organization.contact.purpose | The purpose for which you would contact a contact party. | [Extensible](terminologies.html#extensible) | [ContactEntityType](valueset-contactentity-type.html) | |

 

 

### 8.6.3.2 Constraints [
](organization.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **org-1** | [Rule](conformance-rules.html#rule) | (base) | The organization SHALL at least have a name or an identifier, and possibly more than one | (identifier.count() + name.count()) > 0 | |
| **org-2** | [Rule](conformance-rules.html#rule) | Organization.address | An address of an organization can never be of use 'home' | where(use = 'home').empty() | |
| **org-3** | [Rule](conformance-rules.html#rule) | Organization.telecom | The telecom of an organization can never be of use 'home' | where(use = 'home').empty() | |

 
## 8.6.4 
 Notes:
 [](organization.html#notes)

 

 - 
 There are two places for contact information: one on Organization itself and zero or more using the ContactEntity construct.
 The first one is to be used for the generic, public organization point of contact. The ContactEntity is to be used for
 reaching a person or party that has been designated by the organization to be contacted for a specific purpose or goal.
 

 

 

 
## 8.6.5 
 Example Organization Hierarchy:
 [](organization.html#example)

 
 An example organization hierarchy should help give some guidance as to one example
 of how a location hierarchy could look within a fictitious Medical Organization.**
 (The nesting here would be the "part-of" structure of the Organization resource)*
 

 
```
Burgers University Medical Center
 Eastern Services (prov)
 Emergency Dept
 Oncology Dept
 Nuclear Medicine Research Trials (edu)
 Maternity Ward
 Childrens Ward
 Day Procedures Unit
 Mobile Services (Ambulance)
 Research Center (edu)
 Nuclear Medicine (edu)
 Burgers University (edu)
 Nuclear Medicine Faculty (edu)
 Undergraduate Medicine (edu)
 ...
 
```

 

 *Note that physical structures of this hierarchy are not present - these are defined by a Location hierarchy.*
 

 

## 8.6.6 Search Parameters [
](organization.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| Name** | **Type** | **Description** | **Expression** | **In Common** | |

| active | [token](search.html#token) | Is the Organization record active | Organization.active | | |

| address | [string](search.html#string) | A server defined search that may match any of the string fields in the Address, including line, city, district, state, country, postalCode, and/or text | Organization.address | | |

| address-city | [string](search.html#string) | A city specified in an address | Organization.address.city | | |

| address-country | [string](search.html#string) | A country specified in an address | Organization.address.country | | |

| address-postalcode | [string](search.html#string) | A postal code specified in an address | Organization.address.postalCode | | |

| address-state | [string](search.html#string) | A state specified in an address | Organization.address.state | | |

| address-use | [token](search.html#token) | A use code specified in an address | Organization.address.use | | |

| endpoint | [reference](search.html#reference) | Technical endpoints providing access to services operated for the organization | Organization.endpoint
([Endpoint](endpoint.html)) | | |

| identifier | [token](search.html#token) | Any identifier for the organization (not the accreditation issuer's identifier) | Organization.identifier | | |

| name | [string](search.html#string) | A portion of the organization's name or alias | Organization.name | Organization.alias | | |

| partof | [reference](search.html#reference) | An organization of which this organization forms a part | Organization.partOf
([Organization](organization.html)) | | |

| phonetic | [string](search.html#string) | A portion of the organization's name using some kind of phonetic matching algorithm | Organization.name | | |

| type | [token](search.html#token) | A code for the type of organization | Organization.type | | |