# Basic - FHIR v4.0.1Identifier assigned to the resource for business purposes, outside the context of FHIRIdentifies the 'type' of resource - equivalent to the resource name for other resources (this element modifies the meaning of other elements)Codes for identifying types of resources not yet defined by FHIR. (Strength=Example)Identifies the patient, practitioner, device or any other resource that is the "focus" of this resourceIdentifies when the resource was first createdIndicates who was responsible for creating the resource instanceIdentifier assigned to the resource for business purposes, outside the context of FHIRIdentifies the 'type' of resource - equivalent to the resource name for other resources (this element modifies the meaning of other elements)Codes for identifying types of resources not yet defined by FHIR. (Strength=Example)Identifies the patient, practitioner, device or any other resource that is the "focus" of this resourceIdentifies when the resource was first createdIndicates who was responsible for creating the resource instance

> Source: https://hl7.org/fhir/R4/basic.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/basic.html) [R4B](http://hl7.org/fhir/R4B/basic.html) **R4** [R3](http://hl7.org/fhir/STU3/basic.html) [R2](http://hl7.org/fhir/DSTU2/basic.html)
 

# 2.34 Resource Basic - Content [
](basic.html#2.34)

| [FHIR Infrastructure ](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 1 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Not Classified | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

Basic is used for handling concepts not yet defined in FHIR, narrative-only resources that don't map to an existing resource, and custom resources not appropriate for inclusion in the FHIR specification.

## 2.34.1 Scope and Usage [
](basic.html#scope)

**Basic** is a special type of resource. Unlike all other resources, it doesn't correspond to a specific pre-defined HL7 concept. Instead, it's a placeholder for any resource-like concept that isn't already defined in the HL7 specification.

The Basic resource is intended for use in three circumstances:

- When an implementer needs a resource concept that is likely to be defined by HL7 in the future but they have not yet done so (due to bandwidth issues, lack of sufficient requirements, lower prioritization, etc.)

- When there's a need to convey a narrative-only construct that doesn't neatly correspond to one of the other resources, either because it combines aspects of several resources (e.g. Assessment + Plan) or because the allowed content is flexible such that the system can't be totally sure what sort of content might have been included in the narrative text.

- Other than the circumstances above, this resource will see minimal use. To keep the FHIR specification manageable, it cannot incorporate every site-specific requirement that might be needed in some implementation somewhere. This set of resources likely won't ever be officially defined in HL7.

There's also a fourth circumstance: An implementer wishes to convey information that could/should be conveyed
using a standard resource, however they want to represent the information in a custom format that isn't
aligned with the official resource's elements. While this resource would be the preferred way of meeting that
use-case because it will at least be wire-format compatible, such a use would not be conformant because
making use of the Basic resource would prevent the healthcare-related information from being safely processed,
queried and analyzed by other conformant systems.

Implementers don't need to be concerned with which of the three categories their desired resource fits within. If they need a resource and it clearly doesn't fit one of the ones currently defined, they should use Basic.

## 2.34.2 Background and Context [
](basic.html#bnc)

Basic defines only a minimal set of data elements - those necessary to identify what kind of resource it
represents and those necessary to support resource [compartmenting](compartmentdefinition.html). All other data elements
are represented using the [extension](extensibility.html) mechanism. It's entirely possible to have a
Basic resource instance with nothing other than narrative, a subject and code. And, in practice, that's all many systems will understand.

## 2.34.3 
Resource Content
 [
](basic.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Basic](basic-definitions.html#Basic) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Resource for non-supported content**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](basic-definitions.html#Basic.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business identifier
 | |

| [code](basic-definitions.html#Basic.code) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of Resource
[Basic Resource Types](valueset-basic-resource-type.html) ([Example](terminologies.html#example)) | |

| [subject](basic-definitions.html#Basic.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Identifies the focus of this resource | |

| [created](basic-definitions.html#Basic.created) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [date](datatypes.html#date) | When created | |

| [author](basic-definitions.html#Basic.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Who created | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Basic ([DomainResource](domainresource.html))[Identifier assigned to the resource for business purposes, outside the context of FHIRidentifier](basic-definitions.html#Basic.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Identifies the 'type' of resource - equivalent to the resource name for other resources (this element modifies the meaning of other elements)code](basic-definitions.html#Basic.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Codes for identifying types of resources not yet defined by FHIR. (Strength=Example)BasicResourceTypes](valueset-basic-resource-type.html)?? »[Identifies the patient, practitioner, device or any other resource that is the "focus" of this resourcesubject](basic-definitions.html#Basic.subject) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[Identifies when the resource was first createdcreated](basic-definitions.html#Basic.created) : [date](datatypes.html#date) [0..1][Indicates who was responsible for creating the resource instanceauthor](basic-definitions.html#Basic.author) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »
 

 

 

**XML Template**

 

 
```
<[**Basic**](basic-definitions.html#Basic) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](basic-definitions.html#Basic.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business identifier](terminologies.html#unbound) --></identifier>
 <[**code**](basic-definitions.html#Basic.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of Resource](valueset-basic-resource-type.html) --></code>
 <[**subject**](basic-definitions.html#Basic.subject)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Identifies the focus of this resource](terminologies.html#unbound) --></subject>
 <[**created**](basic-definitions.html#Basic.created) value="[[date](datatypes.html#date)]"/><!-- **0..1** [When created](terminologies.html#unbound) -->
 <[**author**](basic-definitions.html#Basic.author)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Organization](organization.html#Organization)) [Who created](terminologies.html#unbound) --></author>
</Basic>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Basic**](basic-definitions.html#Basic)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](basic-definitions.html#Basic.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business identifier](terminologies.html#unbound)
 "[code](basic-definitions.html#Basic.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Kind of Resource](valueset-basic-resource-type.html)
 "[subject](basic-definitions.html#Basic.subject)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Identifies the focus of this resource](terminologies.html#unbound)
 "[created](basic-definitions.html#Basic.created)" : "<[date](datatypes.html#date)>", // [When created](terminologies.html#unbound)
 "[author](basic-definitions.html#Basic.author)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Organization](organization.html#Organization)) } // [Who created](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Basic**](basic-definitions.html#Basic);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Basic.identifier](basic-definitions.html#Basic.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business identifier
 fhir:[Basic.code](basic-definitions.html#Basic.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Kind of Resource
 fhir:[Basic.subject](basic-definitions.html#Basic.subject) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Identifies the focus of this resource
 fhir:[Basic.created](basic-definitions.html#Basic.created) [ [date](datatypes.html#date) ]; # 0..1 When created
 fhir:[Basic.author](basic-definitions.html#Basic.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]; # 0..1 Who created
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Basic](basic.html#Basic)
 | 
 | 
 |

 | 
 Basic.author | 
 
 

 Type Reference: Added Target Types PractitionerRole, Organization

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](basic.diff.xml) or [JSON](basic.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](basic-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Basic](basic-definitions.html#Basic) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Resource for non-supported content**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](basic-definitions.html#Basic.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Business identifier
 | |

| [code](basic-definitions.html#Basic.code) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of Resource
[Basic Resource Types](valueset-basic-resource-type.html) ([Example](terminologies.html#example)) | |

| [subject](basic-definitions.html#Basic.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Identifies the focus of this resource | |

| [created](basic-definitions.html#Basic.created) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [date](datatypes.html#date) | When created | |

| [author](basic-definitions.html#Basic.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Who created | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Basic ([DomainResource](domainresource.html))[Identifier assigned to the resource for business purposes, outside the context of FHIRidentifier](basic-definitions.html#Basic.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Identifies the 'type' of resource - equivalent to the resource name for other resources (this element modifies the meaning of other elements)code](basic-definitions.html#Basic.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Codes for identifying types of resources not yet defined by FHIR. (Strength=Example)BasicResourceTypes](valueset-basic-resource-type.html)?? »[Identifies the patient, practitioner, device or any other resource that is the "focus" of this resourcesubject](basic-definitions.html#Basic.subject) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[Identifies when the resource was first createdcreated](basic-definitions.html#Basic.created) : [date](datatypes.html#date) [0..1][Indicates who was responsible for creating the resource instanceauthor](basic-definitions.html#Basic.author) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »
 

**XML Template**

 

 
```
<[**Basic**](basic-definitions.html#Basic) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](basic-definitions.html#Basic.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business identifier](terminologies.html#unbound) --></identifier>
 <[**code**](basic-definitions.html#Basic.code)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of Resource](valueset-basic-resource-type.html) --></code>
 <[**subject**](basic-definitions.html#Basic.subject)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Identifies the focus of this resource](terminologies.html#unbound) --></subject>
 <[**created**](basic-definitions.html#Basic.created) value="[[date](datatypes.html#date)]"/><!-- **0..1** [When created](terminologies.html#unbound) -->
 <[**author**](basic-definitions.html#Basic.author)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Organization](organization.html#Organization)) [Who created](terminologies.html#unbound) --></author>
</Basic>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Basic**](basic-definitions.html#Basic)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](basic-definitions.html#Basic.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business identifier](terminologies.html#unbound)
 "[code](basic-definitions.html#Basic.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Kind of Resource](valueset-basic-resource-type.html)
 "[subject](basic-definitions.html#Basic.subject)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Identifies the focus of this resource](terminologies.html#unbound)
 "[created](basic-definitions.html#Basic.created)" : "<[date](datatypes.html#date)>", // [When created](terminologies.html#unbound)
 "[author](basic-definitions.html#Basic.author)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|
 [Organization](organization.html#Organization)) } // [Who created](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Basic**](basic-definitions.html#Basic);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Basic.identifier](basic-definitions.html#Basic.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business identifier
 fhir:[Basic.code](basic-definitions.html#Basic.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Kind of Resource
 fhir:[Basic.subject](basic-definitions.html#Basic.subject) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Identifies the focus of this resource
 fhir:[Basic.created](basic-definitions.html#Basic.created) [ [date](datatypes.html#date) ]; # 0..1 When created
 fhir:[Basic.author](basic-definitions.html#Basic.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ]; # 0..1 Who created
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Basic](basic.html#Basic)
 | 
 | 
 |

 | 
 Basic.author | 
 
 

 Type Reference: Added Target Types PractitionerRole, Organization

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](basic.diff.xml) or [JSON](basic.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](basic-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](basic-profiles.html) and the alternate definitions:
Master Definition [XML](basic.profile.xml.html) + [JSON](basic.profile.json.html),
[XML](xml.html) [Schema](basic.xsd)/[Schematron](basic.sch) + [JSON](json.html) 
[Schema](basic.schema.json.html), [ShEx](basic.shex.html) (for [Turtle](rdf.html)) + [see the extensions](basic-profiles.html) & the [dependency analysis](basic-dependencies.html)

### 2.34.3.1 
Terminology Bindings
 [
](basic.html#tx)

 | Path | Definition | Type | Reference | |

 | Basic.code | Codes for identifying types of resources not yet defined by FHIR. | [Example](terminologies.html#example) | [BasicResourceTypes](valueset-basic-resource-type.html) | |

 

## 2.34.4 Why not custom resources? [
](basic.html#why)

Technically, nothing prevents implementers from going off and defining their own resources containing
whatever data elements they wish. However, doing so causes several issues:

 - Custom resources don't have a discoverability mechanism in the same way custom codes and extensions
 do using the [ValueSet](valueset.html) and [StructureDefinition](structuredefinition.html) resources. As a 
 result, any implementer that receives a custom resource would have no way of looking up what the meaning 
 of the resource or its elements were. While they could get some sense of meaning from XML or JSON tag names, this often 
 isn't sufficient for safe healthcare interoperability.

 - Custom resource names would not be present in the FHIR schemas as allowed elements within the FHIR
 Bundle schema, would not be present in the enumeration of resources in the Reference type, and would not be supported by any of the autogenerated reference implementations and software interfaces.
 This would cause issues for any receiving system making use of the schemas directly or via code-generation.

 - There is no means of preventing two implementers from independently coming up with the same name for
 a resource but defining it differently in terms of meaning as well as allowed elements. This would also cause
 interoperability issues.

All of these concerns are mitigated when there's an assumption that the custom resource will only be used
within a narrow constrained environment where all participants will be aware of the semantics, will be using
the same custom schemas and there's no chance of collisions. However, HL7's experience is that closed
implementation environments rarely remain that way over the long term. Eventually data will need to be
shared with others outside the closed environment and all of the above issues will again come into play.

Therefore, use of 'custom' resources is **NOT** considered to be conformant with FHIR. While the use of
extensions may make the Basic resource slightly more complex and less visually appealing, it is the only safe
and approved mechanism for sharing resource concepts not representable using standard HL7-defined resources.

It is expected that future versions of the interface tooling will be able to generate object interfaces on the
basis of profiles. Where this occurs, the complexity of custom resource elements being expressed as extensions
should be transparent to the internal code of systems that support that particular variant of the Basic resource.
This should further reduce the cost of using 'Basic' as opposed to custom resources.

NOTE: This position is subject to change based on implementation experience. Alternative mechanisms for
handling custom resource requirements in a safe manner may be explored. Ideas around alternative technical 
strategies for managing this issue are welcome.

## 2.34.5 Documents and narrative-only resources [
](basic.html#docs)

Documents are constructed of sections, where a key part of each section is the narrative. The narratives
are stitched together to form the overall text of the document. Many document sections will correspond neatly to
resources that are already defined - [List](list.html), [DiagnosticReport](diagnosticreport.html),
[FamilyMemberHistory](familymemberhistory.html), etc. However, oddly enough, alignment with FHIR resources isn't
always in mind when clinicians and others design documents, and some sections won't neatly align with the
boundaries of resources. Sometimes there's simply a need for a place where a document author can say "stuff"
without any particular constraints on what they may choose to talk about. Basic is intended to provide a
mechanism to handle those circumstances.

Wherever possible, the "standard" FHIR resources should be used, even for narrative-only content. That's because
subsequent revisions of the narrative-only content might choose to encode pieces or even all of the narrative content.
Encoding can occur with "Basic" as well. Extensions can point to other resources (contained or stand-alone) that
fully encode pieces of the free-form narrative found in the Basic resource. If no appropriate other resource exists
for the meaning of the content, extensions can also be used.

## 2.34.6 Best practices for using 'Basic' [
](basic.html#bp)

There are several good practices to follow when making use of the Basic resource:

 - Before using Basic, post a description of the desired resource type on HL7's FHIR list-server or on
 [Stack Overflow ](http://stackoverflow.com/questions/tagged/hl7_fhir) to see whether the
 use-case can be met by an existing resource. (Sometimes the intended scope of an existing resource won't 
 be clear, even if the intent is to cover your space.) Using an existing resource is usually preferable
 to using Basic as it significantly increases the likelihood of interoperability.

 
 - If an existing resource would normally be a good fit for your use-case but can't be used due to
 overly prescriptive constraints your implementation is unable to meet, again raise the problem on
 [Stack Overflow ](http://stackoverflow.com/questions/tagged/hl7_fhir) so the problem with the
 specification can be addressed.

 
 - If it is necessary to make use of the Basic resource, try to use one of the HL7-defined codes for
 resource type or submit your requirement for a new type for inclusion in the HL7 vocabulary (using the [Propose a change ](http://hl7.org/fhir-issues) link), as this will
 increase the likelihood of interoperability. Alternate code systems are conformant, but are less likely to
 be recognized or re-used across the healthcare implementation space.

 
 - Architect your interface in a way that will make it less painful to swap your use of Basic with an
 'official' resource in the event that a future release of FHIR formally defines a resource that encompasses
 your use-case.

 
 - Use a [StructureDefinition](structuredefinition.html) to define the extensions relevant to each type of other resource used.
 Profiles can also be used to define additional search criteria appropriate for the resource.

 
 - When defining a profile on Basic, include mappings to the w5 categories to allow systems to easily manage 
 [AuditEvent](auditevent.html) and [Provenance](provenance.html) uses as well as other potential
 higher-level abstractions of the data.

 
 - As well, profiles should consider how best to handle common notions such as "entered in error" status and alignment
 with common practices within similar resource families (other request resources, medication-related resources), etc.
 

## 2.34.7 Referencing Basic resources [
](basic.html#ref)

None of the standard resources will have direct references to Basic, aside from those that allow linking to
"Any" resource. As a result, most references to "Basic" will need to be performed using extensions.

## 2.34.8 Search Parameters [
](basic.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| author | [reference](search.html#reference) | Who created | Basic.author
([Practitioner](practitioner.html), [Organization](organization.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| code | [token](search.html#token) | Kind of Resource | Basic.code | | |

| created | [date](search.html#date) | When created | Basic.created | | |

| identifier | [token](search.html#token) | Business identifier | Basic.identifier | | |

| patient | [reference](search.html#reference) | Identifies the focus of this resource | Basic.subject.where(resolve() is Patient)
([Patient](patient.html)) | | |

| subject | [reference](search.html#reference) | Identifies the focus of this resource | Basic.subject
(Any) | | |