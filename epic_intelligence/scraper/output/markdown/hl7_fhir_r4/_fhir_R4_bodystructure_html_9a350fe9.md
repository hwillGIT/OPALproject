# BodyStructure - FHIR v4.0.1Identifier for this instance of the anatomical structureWhether this body site is in active use (this element modifies the meaning of other elements)The kind of structure being represented by the body structure at `BodyStructure.location`.  This can define both normal and abnormal morphologiesCodes describing anatomic morphology. (Strength=Example)The anatomical location or region of the specimen, lesion, or body structureCodes describing anatomical locations. May include laterality. (Strength=Example)Qualifier to refine the anatomical location.  These include qualifiers for laterality, relative location, directionality, number, and planeConcepts modifying the anatomic location. (Strength=Example)A summary, characterization or explanation of the body structureImage or images used to identify a locationThe person to which the body site belongsIdentifier for this instance of the anatomical structureWhether this body site is in active use (this element modifies the meaning of other elements)The kind of structure being represented by the body structure at `BodyStructure.location`.  This can define both normal and abnormal morphologiesCodes describing anatomic morphology. (Strength=Example)The anatomical location or region of the specimen, lesion, or body structureCodes describing anatomical locations. May include laterality. (Strength=Example)Qualifier to refine the anatomical location.  These include qualifiers for laterality, relative location, directionality, number, and planeConcepts modifying the anatomic location. (Strength=Example)A summary, characterization or explanation of the body structureImage or images used to identify a locationThe person to which the body site belongs

> Source: https://hl7.org/fhir/R4/bodystructure.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/bodystructure.html) [R4B](http://hl7.org/fhir/R4B/bodystructure.html) **R4**
 

# 10.9 Resource BodyStructure - Content [
](bodystructure.html#10.9)

| [Orders and Observations ](http://www.hl7.org/Special/committees/orders/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 1 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html) | |

Record details about an anatomical structure. This resource may be used when a coded concept does not provide the necessary detail needed for the use case.

## 10.9.1 Scope and Usage [
](bodystructure.html#scope)

 The BodyStructure resource contains details about the anatomical location of a specimen or body part, including patient information, identifiers, as well as text descriptions and images. It provides for the addition of qualifiers such as laterality and directionality to the anatomic location for those use cases where precoordination of codes is not possible. The BodyStructure resource supports recording and tracking of an anatomic location or structure on a patient outside the context of another resource. For example it can be the target of a [Procedure](procedure.html) resource or [Observation](observation.html) resource.

## 10.9.2 Boundaries and Relationships [
](bodystructure.html#bnr)

The BodyStructure resource is not intended to substitute for precoordination of codes. If precoordination of codes is supported by an implementation the codeableConcept should be used. This resource is not intended for describing the type of anatomical location but rather a specific body site on a specific patient.

## 10.9.3 
Resource Content
 [
](bodystructure.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [BodyStructure](bodystructure-definitions.html#BodyStructure) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Specific and identified anatomical structure**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](bodystructure-definitions.html#BodyStructure.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Bodystructure identifier
 | |

| [active](bodystructure-definitions.html#BodyStructure.active) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether this record is in active use | |

| [morphology](bodystructure-definitions.html#BodyStructure.morphology) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of Structure
[SNOMED CT Morphologic Abnormalities](valueset-bodystructure-code.html) ([Example](terminologies.html#example)) | |

| [location](bodystructure-definitions.html#BodyStructure.location) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Body site
[SNOMED CT Body Structures](valueset-body-site.html) ([Example](terminologies.html#example)) | |

| [locationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Body site modifier
[Bodystructure Location Qualifier](valueset-bodystructure-relative-location.html) ([Example](terminologies.html#example))
 | |

| [description](bodystructure-definitions.html#BodyStructure.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Text description | |

| [image](bodystructure-definitions.html#BodyStructure.image) | | 0..* | [Attachment](datatypes.html#Attachment) | Attached images
 | |

| [patient](bodystructure-definitions.html#BodyStructure.patient) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | Who this is about | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 BodyStructure ([DomainResource](domainresource.html))[Identifier for this instance of the anatomical structureidentifier](bodystructure-definitions.html#BodyStructure.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether this body site is in active use (this element modifies the meaning of other elements)active](bodystructure-definitions.html#BodyStructure.active) : [boolean](datatypes.html#boolean) [0..1][The kind of structure being represented by the body structure at `BodyStructure.location`. This can define both normal and abnormal morphologiesmorphology](bodystructure-definitions.html#BodyStructure.morphology) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing anatomic morphology. (Strength=Example)](valueset-bodystructure-code.html) [SNOMEDCTMorphologicAbnormalit...](valueset-bodystructure-code.html)?? »[The anatomical location or region of the specimen, lesion, or body structurelocation](bodystructure-definitions.html#BodyStructure.location) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing anatomical locations. May include laterality. (Strength=Example)SNOMEDCTBodyStructures](valueset-body-site.html)?? »[Qualifier to refine the anatomical location. These include qualifiers for laterality, relative location, directionality, number, and planelocationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Concepts modifying the anatomic location. (Strength=Example)](valueset-bodystructure-relative-location.html) [BodystructureLocationQualifier](valueset-bodystructure-relative-location.html)?? »[A summary, characterization or explanation of the body structuredescription](bodystructure-definitions.html#BodyStructure.description) : [string](datatypes.html#string) [0..1][Image or images used to identify a locationimage](bodystructure-definitions.html#BodyStructure.image) : [Attachment](datatypes.html#Attachment) [0..*][The person to which the body site belongspatient](bodystructure-definitions.html#BodyStructure.patient) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient) »
 

 

 

**XML Template**

 

 
```
<[**BodyStructure**](bodystructure-definitions.html#BodyStructure) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](bodystructure-definitions.html#BodyStructure.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Bodystructure identifier](terminologies.html#unbound) --></identifier>
 <[**active**](bodystructure-definitions.html#BodyStructure.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether this record is in active use](terminologies.html#unbound) -->
 <[**morphology**](bodystructure-definitions.html#BodyStructure.morphology)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of Structure](valueset-bodystructure-code.html) --></morphology>
 <[**location**](bodystructure-definitions.html#BodyStructure.location)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Body site](valueset-body-site.html) --></location>
 <[**locationQualifier**](bodystructure-definitions.html#BodyStructure.locationQualifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Body site modifier](valueset-bodystructure-relative-location.html) --></locationQualifier>
 <[**description**](bodystructure-definitions.html#BodyStructure.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Text description](terminologies.html#unbound) -->
 <[**image**](bodystructure-definitions.html#BodyStructure.image)><!-- **0..*** [Attachment](datatypes.html#Attachment) [Attached images](terminologies.html#unbound) --></image>
 <[**patient**](bodystructure-definitions.html#BodyStructure.patient)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)) [Who this is about](terminologies.html#unbound) --></patient>
</BodyStructure>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**BodyStructure**](bodystructure-definitions.html#BodyStructure)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](bodystructure-definitions.html#BodyStructure.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Bodystructure identifier](terminologies.html#unbound)
 "[active](bodystructure-definitions.html#BodyStructure.active)" : <[boolean](datatypes.html#boolean)>, // [Whether this record is in active use](terminologies.html#unbound)
 "[morphology](bodystructure-definitions.html#BodyStructure.morphology)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of Structure](valueset-bodystructure-code.html)
 "[location](bodystructure-definitions.html#BodyStructure.location)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Body site](valueset-body-site.html)
 "[locationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Body site modifier](valueset-bodystructure-relative-location.html)
 "[description](bodystructure-definitions.html#BodyStructure.description)" : "<[string](datatypes.html#string)>", // [Text description](terminologies.html#unbound)
 "[image](bodystructure-definitions.html#BodyStructure.image)" : [{ [Attachment](datatypes.html#Attachment) }], // [Attached images](terminologies.html#unbound)
 "[patient](bodystructure-definitions.html#BodyStructure.patient)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) } // **R!** [Who this is about](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**BodyStructure**](bodystructure-definitions.html#BodyStructure);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[BodyStructure.identifier](bodystructure-definitions.html#BodyStructure.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Bodystructure identifier
 fhir:[BodyStructure.active](bodystructure-definitions.html#BodyStructure.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether this record is in active use
 fhir:[BodyStructure.morphology](bodystructure-definitions.html#BodyStructure.morphology) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of Structure
 fhir:[BodyStructure.location](bodystructure-definitions.html#BodyStructure.location) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Body site
 fhir:[BodyStructure.locationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Body site modifier
 fhir:[BodyStructure.description](bodystructure-definitions.html#BodyStructure.description) [ [string](datatypes.html#string) ]; # 0..1 Text description
 fhir:[BodyStructure.image](bodystructure-definitions.html#BodyStructure.image) [ [Attachment](datatypes.html#Attachment) ], ... ; # 0..* Attached images
 fhir:[BodyStructure.patient](bodystructure-definitions.html#BodyStructure.patient) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 1..1 Who this is about
]

```

 

 

 

**Changes since R3**

 

 
This resource did not exist in Release 2

 

 This analysis is available as [XML](bodystructure.diff.xml) or [JSON](bodystructure.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](bodystructure-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [BodyStructure](bodystructure-definitions.html#BodyStructure) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Specific and identified anatomical structure**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](bodystructure-definitions.html#BodyStructure.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Bodystructure identifier
 | |

| [active](bodystructure-definitions.html#BodyStructure.active) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | Whether this record is in active use | |

| [morphology](bodystructure-definitions.html#BodyStructure.morphology) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of Structure
[SNOMED CT Morphologic Abnormalities](valueset-bodystructure-code.html) ([Example](terminologies.html#example)) | |

| [location](bodystructure-definitions.html#BodyStructure.location) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Body site
[SNOMED CT Body Structures](valueset-body-site.html) ([Example](terminologies.html#example)) | |

| [locationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Body site modifier
[Bodystructure Location Qualifier](valueset-bodystructure-relative-location.html) ([Example](terminologies.html#example))
 | |

| [description](bodystructure-definitions.html#BodyStructure.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Text description | |

| [image](bodystructure-definitions.html#BodyStructure.image) | | 0..* | [Attachment](datatypes.html#Attachment) | Attached images
 | |

| [patient](bodystructure-definitions.html#BodyStructure.patient) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | Who this is about | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 BodyStructure ([DomainResource](domainresource.html))[Identifier for this instance of the anatomical structureidentifier](bodystructure-definitions.html#BodyStructure.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Whether this body site is in active use (this element modifies the meaning of other elements)active](bodystructure-definitions.html#BodyStructure.active) : [boolean](datatypes.html#boolean) [0..1][The kind of structure being represented by the body structure at `BodyStructure.location`. This can define both normal and abnormal morphologiesmorphology](bodystructure-definitions.html#BodyStructure.morphology) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing anatomic morphology. (Strength=Example)](valueset-bodystructure-code.html) [SNOMEDCTMorphologicAbnormalit...](valueset-bodystructure-code.html)?? »[The anatomical location or region of the specimen, lesion, or body structurelocation](bodystructure-definitions.html#BodyStructure.location) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes describing anatomical locations. May include laterality. (Strength=Example)SNOMEDCTBodyStructures](valueset-body-site.html)?? »[Qualifier to refine the anatomical location. These include qualifiers for laterality, relative location, directionality, number, and planelocationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Concepts modifying the anatomic location. (Strength=Example)](valueset-bodystructure-relative-location.html) [BodystructureLocationQualifier](valueset-bodystructure-relative-location.html)?? »[A summary, characterization or explanation of the body structuredescription](bodystructure-definitions.html#BodyStructure.description) : [string](datatypes.html#string) [0..1][Image or images used to identify a locationimage](bodystructure-definitions.html#BodyStructure.image) : [Attachment](datatypes.html#Attachment) [0..*][The person to which the body site belongspatient](bodystructure-definitions.html#BodyStructure.patient) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient) »
 

**XML Template**

 

 
```
<[**BodyStructure**](bodystructure-definitions.html#BodyStructure) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](bodystructure-definitions.html#BodyStructure.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Bodystructure identifier](terminologies.html#unbound) --></identifier>
 <[**active**](bodystructure-definitions.html#BodyStructure.active) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Whether this record is in active use](terminologies.html#unbound) -->
 <[**morphology**](bodystructure-definitions.html#BodyStructure.morphology)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of Structure](valueset-bodystructure-code.html) --></morphology>
 <[**location**](bodystructure-definitions.html#BodyStructure.location)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Body site](valueset-body-site.html) --></location>
 <[**locationQualifier**](bodystructure-definitions.html#BodyStructure.locationQualifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Body site modifier](valueset-bodystructure-relative-location.html) --></locationQualifier>
 <[**description**](bodystructure-definitions.html#BodyStructure.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Text description](terminologies.html#unbound) -->
 <[**image**](bodystructure-definitions.html#BodyStructure.image)><!-- **0..*** [Attachment](datatypes.html#Attachment) [Attached images](terminologies.html#unbound) --></image>
 <[**patient**](bodystructure-definitions.html#BodyStructure.patient)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)) [Who this is about](terminologies.html#unbound) --></patient>
</BodyStructure>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**BodyStructure**](bodystructure-definitions.html#BodyStructure)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](bodystructure-definitions.html#BodyStructure.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Bodystructure identifier](terminologies.html#unbound)
 "[active](bodystructure-definitions.html#BodyStructure.active)" : <[boolean](datatypes.html#boolean)>, // [Whether this record is in active use](terminologies.html#unbound)
 "[morphology](bodystructure-definitions.html#BodyStructure.morphology)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of Structure](valueset-bodystructure-code.html)
 "[location](bodystructure-definitions.html#BodyStructure.location)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Body site](valueset-body-site.html)
 "[locationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Body site modifier](valueset-bodystructure-relative-location.html)
 "[description](bodystructure-definitions.html#BodyStructure.description)" : "<[string](datatypes.html#string)>", // [Text description](terminologies.html#unbound)
 "[image](bodystructure-definitions.html#BodyStructure.image)" : [{ [Attachment](datatypes.html#Attachment) }], // [Attached images](terminologies.html#unbound)
 "[patient](bodystructure-definitions.html#BodyStructure.patient)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) } // **R!** [Who this is about](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**BodyStructure**](bodystructure-definitions.html#BodyStructure);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[BodyStructure.identifier](bodystructure-definitions.html#BodyStructure.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Bodystructure identifier
 fhir:[BodyStructure.active](bodystructure-definitions.html#BodyStructure.active) [ [boolean](datatypes.html#boolean) ]; # 0..1 Whether this record is in active use
 fhir:[BodyStructure.morphology](bodystructure-definitions.html#BodyStructure.morphology) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of Structure
 fhir:[BodyStructure.location](bodystructure-definitions.html#BodyStructure.location) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Body site
 fhir:[BodyStructure.locationQualifier](bodystructure-definitions.html#BodyStructure.locationQualifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Body site modifier
 fhir:[BodyStructure.description](bodystructure-definitions.html#BodyStructure.description) [ [string](datatypes.html#string) ]; # 0..1 Text description
 fhir:[BodyStructure.image](bodystructure-definitions.html#BodyStructure.image) [ [Attachment](datatypes.html#Attachment) ], ... ; # 0..* Attached images
 fhir:[BodyStructure.patient](bodystructure-definitions.html#BodyStructure.patient) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 1..1 Who this is about
]

```

 

**Changes since Release 3**

 

 
This resource did not exist in Release 2

 

 This analysis is available as [XML](bodystructure.diff.xml) or [JSON](bodystructure.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](bodystructure-version-maps.html) (status = 3 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](bodystructure-profiles.html) and the alternate definitions:
Master Definition [XML](bodystructure.profile.xml.html) + [JSON](bodystructure.profile.json.html),
[XML](xml.html) [Schema](bodystructure.xsd)/[Schematron](bodystructure.sch) + [JSON](json.html) 
[Schema](bodystructure.schema.json.html), [ShEx](bodystructure.shex.html) (for [Turtle](rdf.html)) + [see the extensions](bodystructure-profiles.html) & the [dependency analysis](bodystructure-dependencies.html)

### 10.9.3.1 
Terminology Bindings
 [
](bodystructure.html#tx)

 | Path | Definition | Type | Reference | |

 | BodyStructure.morphology | Codes describing anatomic morphology. | [Example](terminologies.html#example) | [SNOMEDCTMorphologicAbnormalities](valueset-bodystructure-code.html) | |

 | BodyStructure.location | Codes describing anatomical locations. May include laterality. | [Example](terminologies.html#example) | [SNOMEDCTBodyStructures](valueset-body-site.html) | |

 | BodyStructure.locationQualifier | Concepts modifying the anatomic location. | [Example](terminologies.html#example) | [BodystructureLocationQualifier](valueset-bodystructure-relative-location.html) | |

 

 

## 10.9.4 Search Parameters [
](bodystructure.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| identifier | [token](search.html#token) | Bodystructure identifier | BodyStructure.identifier | | |

| location | [token](search.html#token) | Body site | BodyStructure.location | | |

| morphology | [token](search.html#token) | Kind of Structure | BodyStructure.morphology | | |

| patient | [reference](search.html#reference) | Who this is about | BodyStructure.patient
([Patient](patient.html)) | | |