# CompartmentDefinition - FHIR v4.0.1An absolute URI that is used to identify this compartment definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this compartment definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the compartment definition is stored on different serversThe identifier that is used to identify this version of the compartment definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the compartment definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequenceA natural language name identifying the compartment definition. This name should be usable as an identifier for the module by machine processing applications such as code generationThe status of this compartment definition. Enables tracking the life-cycle of the content (this element modifies the meaning of other elements)The lifecycle status of an artifact. (Strength=Required)A Boolean value to indicate that this compartment definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usageThe date  (and optionally time) when the compartment definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the compartment definition changesThe name of the organization or individual that published the compartment definitionContact details to assist a user in finding and communicating with the publisherA free text natural language description of the compartment definition from a consumer's perspectiveThe content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate compartment definition instancesExplanation of why this compartment definition is needed and why it has been designed as it hasWhich compartment this definition describesWhich type a compartment definition describes. (Strength=Required)Whether the search syntax is supported,The name of a resource supported by the serverOne of the resource types defined as part of this version of FHIR. (Strength=Required)The name of a search parameter that represents the link to the compartment. More than one may be listed because a resource may be linked to a compartment in more than one way,Additional documentation about the resource and compartmentInformation about how a resource is related to the compartmentAn absolute URI that is used to identify this compartment definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this compartment definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the compartment definition is stored on different serversThe identifier that is used to identify this version of the compartment definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the compartment definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequenceA natural language name identifying the compartment definition. This name should be usable as an identifier for the module by machine processing applications such as code generationThe status of this compartment definition. Enables tracking the life-cycle of the content (this element modifies the meaning of other elements)The lifecycle status of an artifact. (Strength=Required)A Boolean value to indicate that this compartment definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usageThe date  (and optionally time) when the compartment definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the compartment definition changesThe name of the organization or individual that published the compartment definitionContact details to assist a user in finding and communicating with the publisherA free text natural language description of the compartment definition from a consumer's perspectiveThe content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate compartment definition instancesExplanation of why this compartment definition is needed and why it has been designed as it hasWhich compartment this definition describesWhich type a compartment definition describes. (Strength=Required)Whether the search syntax is supported,The name of a resource supported by the serverOne of the resource types defined as part of this version of FHIR. (Strength=Required)The name of a search parameter that represents the link to the compartment. More than one may be listed because a resource may be linked to a compartment in more than one way,Additional documentation about the resource and compartmentInformation about how a resource is related to the compartment

> Source: https://hl7.org/fhir/R4/compartmentdefinition.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/compartmentdefinition.html) [R4B](http://hl7.org/fhir/R4B/compartmentdefinition.html) **R4** [R3](http://hl7.org/fhir/STU3/compartmentdefinition.html)
 

# 5.6 Resource CompartmentDefinition - Content [
](compartmentdefinition.html#5.6)

| [FHIR Infrastructure ](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 1 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Anonymous | [Compartments](compartmentdefinition.html): Not linked to any defined compartments | |

A compartment definition that defines how resources are accessed on a server.

## 5.6.1 Scope and Usage [
](compartmentdefinition.html#scope)

Each resource may belong to one or more logical compartments. A compartment is a logical 
grouping of resources which share a common property. Compartments have two principal roles:

 - Function as an access mechanism for finding a set of related resources quickly

 - Provide a definitional basis for applying access control to resources quickly

**Note:**

At present, compartment definitions can only* be defined by HL7 International. This is because
their existence creates significant impact on the behavior of servers.

 

 

## 5.6.2 Boundaries and Relationships [
](compartmentdefinition.html#bnr)
 

Compartment definitions describe how particular compartment instances are named and identified,
and how systems know which resources are in the compartment. The following compartments are 
defined by this specification:

 | **Title** | **Description** | **Identity** | **Membership** | |

 | [Patient](compartmentdefinition-patient.html) | The set of resources associated with a particular patient | There is an instance of the patient compartment for each patient resource, and the identity of the compartment is the same as the patient. When a patient is linked to another patient, all the records associated with the linked patient are in the compartment associated with the target of the link. | The patient compartment includes any resources where the subject of the resource is the patient, and some other resources that are directly linked to resources in the patient compartment | |

 | [Encounter](compartmentdefinition-encounter.html) | The set of resources associated with a particular encounter | There is an instance of the encounter compartment for each encounter resource, and the identity of the compartment is the same as the encounter | The encounter compartment includes any resources where the resource has an explicitly nominated encounter, and some other resources that themselves link to resources in the encounter compartment. Note that for many resources, the exact nature of the link to encounter can be ambiguous (e.g. for a DiagnosticReport, is it the encounter when it was initiated, or when it was reported?) | |

 | [RelatedPerson](compartmentdefinition-relatedperson.html) | The set of resources associated with a particular 'related person' | There is an instance of the relatedPerson compartment for each relatedPerson resource, and the identity of the compartment is the same as the relatedPerson | The relatedPerson compartment includes any resources where the resource is explicitly linked to relatedPerson (usually as author) | |

 | [Practitioner](compartmentdefinition-practitioner.html) | The set of resources associated with a particular practitioner | There is an instance of the practitioner compartment for each Practitioner resource, and the identity of the compartment is the same as the Practitioner | The practitioner compartment includes any resources where the resource is explicitly linked to a Practitioner (usually as author, but other kinds of linkage exist) | |

 | [Device](compartmentdefinition-device.html) | The set of resources associated with a particular device | There is an instance of the device compartment for each Device resource, and the identity of the compartment is the same as the Device | The device compartment includes any resources where the resource is explicitly linked to a Device (mostly subject or performer) | |

The full definitions of these compartments are published as `CompartmentDefinition`
resources. Servers typically do not support the full definition of a compartment, and are not 
required to. Systems may publish `CompartmentDefinition` resources so that
other systems may make use of compartments properly.

 - CompartmentDefinitions are used by [CapabilityStatement](capabilitystatement.html) instances for specifying how resources are accessed

This resource is referenced by [CapabilityStatement](capabilitystatement.html#CapabilityStatement)

## 5.6.3 
Resource Content
 [
](compartmentdefinition.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [CompartmentDefinition](compartmentdefinition-definitions.html#CompartmentDefinition) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Compartment Definition for a resource**+ Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [url](compartmentdefinition-definitions.html#CompartmentDefinition.url) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [uri](datatypes.html#uri) | Canonical identifier for this compartment definition, represented as a URI (globally unique) | |

| [version](compartmentdefinition-definitions.html#CompartmentDefinition.version) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Business version of the compartment definition | |

| [name](compartmentdefinition-definitions.html#CompartmentDefinition.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 1..1 | [string](datatypes.html#string) | Name for this compartment definition (computer friendly) | |

| [status](compartmentdefinition-definitions.html#CompartmentDefinition.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown
[PublicationStatus](valueset-publication-status.html) ([Required](terminologies.html#required)) | |

| [experimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage | |

| [date](compartmentdefinition-definitions.html#CompartmentDefinition.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed | |

| [publisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) | |

| [contact](compartmentdefinition-definitions.html#CompartmentDefinition.contact) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher
 | |

| [description](compartmentdefinition-definitions.html#CompartmentDefinition.description) | | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the compartment definition | |

| [useContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support
 | |

| [purpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) | | 0..1 | [markdown](datatypes.html#markdown) | Why this compartment definition is defined | |

| [code](compartmentdefinition-definitions.html#CompartmentDefinition.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | Patient | Encounter | RelatedPerson | Practitioner | Device
[CompartmentType](valueset-compartment-type.html) ([Required](terminologies.html#required)) | |

| [search](compartmentdefinition-definitions.html#CompartmentDefinition.search) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [boolean](datatypes.html#boolean) | Whether the search syntax is supported | |

| [resource](compartmentdefinition-definitions.html#CompartmentDefinition.resource) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | How a resource is related to the compartment
 | |

| [code](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | Name of resource type
[ResourceType](valueset-resource-types.html) ([Required](terminologies.html#required)) | |

| [param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [string](datatypes.html#string) | Search Parameter Name, or chained parameters
 | |

| [documentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) | | 0..1 | [string](datatypes.html#string) | Additional documentation about the resource and compartment | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - CompartmentDefinition ([DomainResource](domainresource.html))[An absolute URI that is used to identify this compartment definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this compartment definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the compartment definition is stored on different serversurl](compartmentdefinition-definitions.html#CompartmentDefinition.url) : [uri](datatypes.html#uri) [1..1][The identifier that is used to identify this version of the compartment definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the compartment definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequenceversion](compartmentdefinition-definitions.html#CompartmentDefinition.version) : [string](datatypes.html#string) [0..1][A natural language name identifying the compartment definition. This name should be usable as an identifier for the module by machine processing applications such as code generationname](compartmentdefinition-definitions.html#CompartmentDefinition.name) : [string](datatypes.html#string) [1..1][The status of this compartment definition. Enables tracking the life-cycle of the content (this element modifies the meaning of other elements)status](compartmentdefinition-definitions.html#CompartmentDefinition.status) : [code](datatypes.html#code) [1..1] « [The lifecycle status of an artifact. (Strength=Required)PublicationStatus](valueset-publication-status.html)! »[A Boolean value to indicate that this compartment definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usageexperimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) : [boolean](datatypes.html#boolean) [0..1][The date (and optionally time) when the compartment definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the compartment definition changesdate](compartmentdefinition-definitions.html#CompartmentDefinition.date) : [dateTime](datatypes.html#dateTime) [0..1][The name of the organization or individual that published the compartment definitionpublisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) : [string](datatypes.html#string) [0..1][Contact details to assist a user in finding and communicating with the publishercontact](compartmentdefinition-definitions.html#CompartmentDefinition.contact) : [ContactDetail](metadatatypes.html#ContactDetail) [0..*][A free text natural language description of the compartment definition from a consumer's perspectivedescription](compartmentdefinition-definitions.html#CompartmentDefinition.description) : [markdown](datatypes.html#markdown) [0..1][The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate compartment definition instancesuseContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext) : [UsageContext](metadatatypes.html#UsageContext) [0..*][Explanation of why this compartment definition is needed and why it has been designed as it haspurpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) : [markdown](datatypes.html#markdown) [0..1][Which compartment this definition describescode](compartmentdefinition-definitions.html#CompartmentDefinition.code) : [code](datatypes.html#code) [1..1] « [Which type a compartment definition describes. (Strength=Required)CompartmentType](valueset-compartment-type.html)! »[Whether the search syntax is supported,search](compartmentdefinition-definitions.html#CompartmentDefinition.search) : [boolean](datatypes.html#boolean) [1..1]Resource[The name of a resource supported by the servercode](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) : [code](datatypes.html#code) [1..1] « [One of the resource types defined as part of this version of FHIR. (Strength=Required)ResourceType](valueset-resource-types.html)! »[The name of a search parameter that represents the link to the compartment. More than one may be listed because a resource may be linked to a compartment in more than one way,param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) : [string](datatypes.html#string) [0..*][Additional documentation about the resource and compartmentdocumentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) : [string](datatypes.html#string) [0..1]
[Information about how a resource is related to the compartmentresource](compartmentdefinition-definitions.html#CompartmentDefinition.resource)[0..*]
 

 

 

**XML Template**

 

 
```
<[**CompartmentDefinition**](compartmentdefinition-definitions.html#CompartmentDefinition) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**url**](compartmentdefinition-definitions.html#CompartmentDefinition.url) value="[[uri](datatypes.html#uri)]"/><!-- **1..1** [Canonical identifier for this compartment definition, represented as a URI (globally unique)](terminologies.html#unbound) -->
 <[**version**](compartmentdefinition-definitions.html#CompartmentDefinition.version) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Business version of the compartment definition](terminologies.html#unbound) -->
 <[**name**](compartmentdefinition-definitions.html#CompartmentDefinition.name) value="[[string](datatypes.html#string)]"/><!-- ** 1..1** [Name for this compartment definition (computer friendly)](terminologies.html#unbound) -->
 <[**status**](compartmentdefinition-definitions.html#CompartmentDefinition.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [draft | active | retired | unknown](valueset-publication-status.html) -->
 <[**experimental**](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [For testing purposes, not real usage](terminologies.html#unbound) -->
 <[**date**](compartmentdefinition-definitions.html#CompartmentDefinition.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [Date last changed](terminologies.html#unbound) -->
 <[**publisher**](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Name of the publisher (organization or individual)](terminologies.html#unbound) -->
 <[**contact**](compartmentdefinition-definitions.html#CompartmentDefinition.contact)><!-- **0..*** [ContactDetail](metadatatypes.html#ContactDetail) [Contact details for the publisher](terminologies.html#unbound) --></contact>
 <[**description**](compartmentdefinition-definitions.html#CompartmentDefinition.description) value="[[markdown](datatypes.html#markdown)]"/><!-- **0..1** [Natural language description of the compartment definition](terminologies.html#unbound) -->
 <[**useContext**](compartmentdefinition-definitions.html#CompartmentDefinition.useContext)><!-- **0..*** [UsageContext](metadatatypes.html#UsageContext) [The context that the content is intended to support](terminologies.html#unbound) --></useContext>
 <[**purpose**](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) value="[[markdown](datatypes.html#markdown)]"/><!-- **0..1** [Why this compartment definition is defined](terminologies.html#unbound) -->
 <[**code**](compartmentdefinition-definitions.html#CompartmentDefinition.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [Patient | Encounter | RelatedPerson | Practitioner | Device](valueset-compartment-type.html) -->
 <[**search**](compartmentdefinition-definitions.html#CompartmentDefinition.search) value="[[boolean](datatypes.html#boolean)]"/><!-- **1..1** [Whether the search syntax is supported](terminologies.html#unbound) -->
 <[**resource**](compartmentdefinition-definitions.html#CompartmentDefinition.resource)> <!-- **0..*** How a resource is related to the compartment -->
 <[**code**](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [Name of resource type](valueset-resource-types.html) -->
 <[**param**](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) value="[[string](datatypes.html#string)]"/><!-- **0..*** [Search Parameter Name, or chained parameters](terminologies.html#unbound) -->
 <[**documentation**](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional documentation about the resource and compartment](terminologies.html#unbound) -->
 </resource>
</CompartmentDefinition>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**CompartmentDefinition**](compartmentdefinition-definitions.html#CompartmentDefinition)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[url](compartmentdefinition-definitions.html#CompartmentDefinition.url)" : "<[uri](datatypes.html#uri)>", // **R!** [Canonical identifier for this compartment definition, represented as a URI (globally unique)](terminologies.html#unbound)
 "[version](compartmentdefinition-definitions.html#CompartmentDefinition.version)" : "<[string](datatypes.html#string)>", // [Business version of the compartment definition](terminologies.html#unbound)
 "[name](compartmentdefinition-definitions.html#CompartmentDefinition.name)" : "<[string](datatypes.html#string)>", // **C?** **R!** [Name for this compartment definition (computer friendly)](terminologies.html#unbound)
 "[status](compartmentdefinition-definitions.html#CompartmentDefinition.status)" : "<[code](datatypes.html#code)>", // **R!** [draft | active | retired | unknown](valueset-publication-status.html)
 "[experimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental)" : <[boolean](datatypes.html#boolean)>, // [For testing purposes, not real usage](terminologies.html#unbound)
 "[date](compartmentdefinition-definitions.html#CompartmentDefinition.date)" : "<[dateTime](datatypes.html#dateTime)>", // [Date last changed](terminologies.html#unbound)
 "[publisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher)" : "<[string](datatypes.html#string)>", // [Name of the publisher (organization or individual)](terminologies.html#unbound)
 "[contact](compartmentdefinition-definitions.html#CompartmentDefinition.contact)" : [{ [ContactDetail](metadatatypes.html#ContactDetail) }], // [Contact details for the publisher](terminologies.html#unbound)
 "[description](compartmentdefinition-definitions.html#CompartmentDefinition.description)" : "<[markdown](datatypes.html#markdown)>", // [Natural language description of the compartment definition](terminologies.html#unbound)
 "[useContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext)" : [{ [UsageContext](metadatatypes.html#UsageContext) }], // [The context that the content is intended to support](terminologies.html#unbound)
 "[purpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose)" : "<[markdown](datatypes.html#markdown)>", // [Why this compartment definition is defined](terminologies.html#unbound)
 "[code](compartmentdefinition-definitions.html#CompartmentDefinition.code)" : "<[code](datatypes.html#code)>", // **R!** [Patient | Encounter | RelatedPerson | Practitioner | Device](valueset-compartment-type.html)
 "[search](compartmentdefinition-definitions.html#CompartmentDefinition.search)" : <[boolean](datatypes.html#boolean)>, // **R!** [Whether the search syntax is supported](terminologies.html#unbound)
 "[resource](compartmentdefinition-definitions.html#CompartmentDefinition.resource)" : [{ // [How a resource is related to the compartment](terminologies.html#unbound)
 "[code](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code)" : "<[code](datatypes.html#code)>", // **R!** [Name of resource type](valueset-resource-types.html)
 "[param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param)" : ["<[string](datatypes.html#string)>"], // [Search Parameter Name, or chained parameters](terminologies.html#unbound)
 "[documentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation)" : "<[string](datatypes.html#string)>" // [Additional documentation about the resource and compartment](terminologies.html#unbound)
 }]
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**CompartmentDefinition**](compartmentdefinition-definitions.html#CompartmentDefinition);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[CompartmentDefinition.url](compartmentdefinition-definitions.html#CompartmentDefinition.url) [ [uri](datatypes.html#uri) ]; # 1..1 Canonical identifier for this compartment definition, represented as a URI (globally unique)
 fhir:[CompartmentDefinition.version](compartmentdefinition-definitions.html#CompartmentDefinition.version) [ [string](datatypes.html#string) ]; # 0..1 Business version of the compartment definition
 fhir:[CompartmentDefinition.name](compartmentdefinition-definitions.html#CompartmentDefinition.name) [ [string](datatypes.html#string) ]; # 1..1 Name for this compartment definition (computer friendly)
 fhir:[CompartmentDefinition.status](compartmentdefinition-definitions.html#CompartmentDefinition.status) [ [code](datatypes.html#code) ]; # 1..1 draft | active | retired | unknown
 fhir:[CompartmentDefinition.experimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) [ [boolean](datatypes.html#boolean) ]; # 0..1 For testing purposes, not real usage
 fhir:[CompartmentDefinition.date](compartmentdefinition-definitions.html#CompartmentDefinition.date) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Date last changed
 fhir:[CompartmentDefinition.publisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) [ [string](datatypes.html#string) ]; # 0..1 Name of the publisher (organization or individual)
 fhir:[CompartmentDefinition.contact](compartmentdefinition-definitions.html#CompartmentDefinition.contact) [ [ContactDetail](metadatatypes.html#ContactDetail) ], ... ; # 0..* Contact details for the publisher
 fhir:[CompartmentDefinition.description](compartmentdefinition-definitions.html#CompartmentDefinition.description) [ [markdown](datatypes.html#markdown) ]; # 0..1 Natural language description of the compartment definition
 fhir:[CompartmentDefinition.useContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext) [ [UsageContext](metadatatypes.html#UsageContext) ], ... ; # 0..* The context that the content is intended to support
 fhir:[CompartmentDefinition.purpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) [ [markdown](datatypes.html#markdown) ]; # 0..1 Why this compartment definition is defined
 fhir:[CompartmentDefinition.code](compartmentdefinition-definitions.html#CompartmentDefinition.code) [ [code](datatypes.html#code) ]; # 1..1 Patient | Encounter | RelatedPerson | Practitioner | Device
 fhir:[CompartmentDefinition.search](compartmentdefinition-definitions.html#CompartmentDefinition.search) [ [boolean](datatypes.html#boolean) ]; # 1..1 Whether the search syntax is supported
 fhir:[CompartmentDefinition.resource](compartmentdefinition-definitions.html#CompartmentDefinition.resource) [ # 0..* How a resource is related to the compartment
 fhir:[CompartmentDefinition.resource.code](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) [ [code](datatypes.html#code) ]; # 1..1 Name of resource type
 fhir:[CompartmentDefinition.resource.param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) [ [string](datatypes.html#string) ], ... ; # 0..* Search Parameter Name, or chained parameters
 fhir:[CompartmentDefinition.resource.documentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) [ [string](datatypes.html#string) ]; # 0..1 Additional documentation about the resource and compartment
 ], ...;
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [CompartmentDefinition](compartmentdefinition.html#CompartmentDefinition)
 | 
 | 
 |

 | 
 CompartmentDefinition | 
 
 

 Min Cardinality changed from 1 to 0

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 CompartmentDefinition.version | 
 
 

 - Added Element

 

 | 
 |

 | 
 CompartmentDefinition.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1

 

 | 
 |

 | 
 CompartmentDefinition.experimental | 
 
 

 - No longer marked as Modifier

 

 | 
 |

 | 
 CompartmentDefinition.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/compartment-type to http://hl7.org/fhir/ValueSet/compartment-type|4.0.1

 

 | 
 |

 | 
 CompartmentDefinition.resource.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/resource-types to http://hl7.org/fhir/ValueSet/resource-types|4.0.1

 

 | 
 |

 | 
 CompartmentDefinition.title | 
 
 

 - deleted

 

 | 
 |

 | 
 CompartmentDefinition.jurisdiction | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](compartmentdefinition.diff.xml) or [JSON](compartmentdefinition.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](compartmentdefinition-version-maps.html) (status = 6 tests that all execute ok. 1 fail round-trip testing and 5 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [CompartmentDefinition](compartmentdefinition-definitions.html#CompartmentDefinition) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Compartment Definition for a resource**+ Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [url](compartmentdefinition-definitions.html#CompartmentDefinition.url) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [uri](datatypes.html#uri) | Canonical identifier for this compartment definition, represented as a URI (globally unique) | |

| [version](compartmentdefinition-definitions.html#CompartmentDefinition.version) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Business version of the compartment definition | |

| [name](compartmentdefinition-definitions.html#CompartmentDefinition.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 1..1 | [string](datatypes.html#string) | Name for this compartment definition (computer friendly) | |

| [status](compartmentdefinition-definitions.html#CompartmentDefinition.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown
[PublicationStatus](valueset-publication-status.html) ([Required](terminologies.html#required)) | |

| [experimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage | |

| [date](compartmentdefinition-definitions.html#CompartmentDefinition.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed | |

| [publisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) | |

| [contact](compartmentdefinition-definitions.html#CompartmentDefinition.contact) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher
 | |

| [description](compartmentdefinition-definitions.html#CompartmentDefinition.description) | | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the compartment definition | |

| [useContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support
 | |

| [purpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) | | 0..1 | [markdown](datatypes.html#markdown) | Why this compartment definition is defined | |

| [code](compartmentdefinition-definitions.html#CompartmentDefinition.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | Patient | Encounter | RelatedPerson | Practitioner | Device
[CompartmentType](valueset-compartment-type.html) ([Required](terminologies.html#required)) | |

| [search](compartmentdefinition-definitions.html#CompartmentDefinition.search) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [boolean](datatypes.html#boolean) | Whether the search syntax is supported | |

| [resource](compartmentdefinition-definitions.html#CompartmentDefinition.resource) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | How a resource is related to the compartment
 | |

| [code](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | Name of resource type
[ResourceType](valueset-resource-types.html) ([Required](terminologies.html#required)) | |

| [param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [string](datatypes.html#string) | Search Parameter Name, or chained parameters
 | |

| [documentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) | | 0..1 | [string](datatypes.html#string) | Additional documentation about the resource and compartment | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - CompartmentDefinition ([DomainResource](domainresource.html))[An absolute URI that is used to identify this compartment definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this compartment definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the compartment definition is stored on different serversurl](compartmentdefinition-definitions.html#CompartmentDefinition.url) : [uri](datatypes.html#uri) [1..1][The identifier that is used to identify this version of the compartment definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the compartment definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequenceversion](compartmentdefinition-definitions.html#CompartmentDefinition.version) : [string](datatypes.html#string) [0..1][A natural language name identifying the compartment definition. This name should be usable as an identifier for the module by machine processing applications such as code generationname](compartmentdefinition-definitions.html#CompartmentDefinition.name) : [string](datatypes.html#string) [1..1][The status of this compartment definition. Enables tracking the life-cycle of the content (this element modifies the meaning of other elements)status](compartmentdefinition-definitions.html#CompartmentDefinition.status) : [code](datatypes.html#code) [1..1] « [The lifecycle status of an artifact. (Strength=Required)PublicationStatus](valueset-publication-status.html)! »[A Boolean value to indicate that this compartment definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usageexperimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) : [boolean](datatypes.html#boolean) [0..1][The date (and optionally time) when the compartment definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the compartment definition changesdate](compartmentdefinition-definitions.html#CompartmentDefinition.date) : [dateTime](datatypes.html#dateTime) [0..1][The name of the organization or individual that published the compartment definitionpublisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) : [string](datatypes.html#string) [0..1][Contact details to assist a user in finding and communicating with the publishercontact](compartmentdefinition-definitions.html#CompartmentDefinition.contact) : [ContactDetail](metadatatypes.html#ContactDetail) [0..*][A free text natural language description of the compartment definition from a consumer's perspectivedescription](compartmentdefinition-definitions.html#CompartmentDefinition.description) : [markdown](datatypes.html#markdown) [0..1][The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate compartment definition instancesuseContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext) : [UsageContext](metadatatypes.html#UsageContext) [0..*][Explanation of why this compartment definition is needed and why it has been designed as it haspurpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) : [markdown](datatypes.html#markdown) [0..1][Which compartment this definition describescode](compartmentdefinition-definitions.html#CompartmentDefinition.code) : [code](datatypes.html#code) [1..1] « [Which type a compartment definition describes. (Strength=Required)CompartmentType](valueset-compartment-type.html)! »[Whether the search syntax is supported,search](compartmentdefinition-definitions.html#CompartmentDefinition.search) : [boolean](datatypes.html#boolean) [1..1]Resource[The name of a resource supported by the servercode](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) : [code](datatypes.html#code) [1..1] « [One of the resource types defined as part of this version of FHIR. (Strength=Required)ResourceType](valueset-resource-types.html)! »[The name of a search parameter that represents the link to the compartment. More than one may be listed because a resource may be linked to a compartment in more than one way,param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) : [string](datatypes.html#string) [0..*][Additional documentation about the resource and compartmentdocumentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) : [string](datatypes.html#string) [0..1]
[Information about how a resource is related to the compartmentresource](compartmentdefinition-definitions.html#CompartmentDefinition.resource)[0..*]
 

**XML Template**

 

 
```
<[**CompartmentDefinition**](compartmentdefinition-definitions.html#CompartmentDefinition) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**url**](compartmentdefinition-definitions.html#CompartmentDefinition.url) value="[[uri](datatypes.html#uri)]"/><!-- **1..1** [Canonical identifier for this compartment definition, represented as a URI (globally unique)](terminologies.html#unbound) -->
 <[**version**](compartmentdefinition-definitions.html#CompartmentDefinition.version) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Business version of the compartment definition](terminologies.html#unbound) -->
 <[**name**](compartmentdefinition-definitions.html#CompartmentDefinition.name) value="[[string](datatypes.html#string)]"/><!-- ** 1..1** [Name for this compartment definition (computer friendly)](terminologies.html#unbound) -->
 <[**status**](compartmentdefinition-definitions.html#CompartmentDefinition.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [draft | active | retired | unknown](valueset-publication-status.html) -->
 <[**experimental**](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [For testing purposes, not real usage](terminologies.html#unbound) -->
 <[**date**](compartmentdefinition-definitions.html#CompartmentDefinition.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [Date last changed](terminologies.html#unbound) -->
 <[**publisher**](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Name of the publisher (organization or individual)](terminologies.html#unbound) -->
 <[**contact**](compartmentdefinition-definitions.html#CompartmentDefinition.contact)><!-- **0..*** [ContactDetail](metadatatypes.html#ContactDetail) [Contact details for the publisher](terminologies.html#unbound) --></contact>
 <[**description**](compartmentdefinition-definitions.html#CompartmentDefinition.description) value="[[markdown](datatypes.html#markdown)]"/><!-- **0..1** [Natural language description of the compartment definition](terminologies.html#unbound) -->
 <[**useContext**](compartmentdefinition-definitions.html#CompartmentDefinition.useContext)><!-- **0..*** [UsageContext](metadatatypes.html#UsageContext) [The context that the content is intended to support](terminologies.html#unbound) --></useContext>
 <[**purpose**](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) value="[[markdown](datatypes.html#markdown)]"/><!-- **0..1** [Why this compartment definition is defined](terminologies.html#unbound) -->
 <[**code**](compartmentdefinition-definitions.html#CompartmentDefinition.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [Patient | Encounter | RelatedPerson | Practitioner | Device](valueset-compartment-type.html) -->
 <[**search**](compartmentdefinition-definitions.html#CompartmentDefinition.search) value="[[boolean](datatypes.html#boolean)]"/><!-- **1..1** [Whether the search syntax is supported](terminologies.html#unbound) -->
 <[**resource**](compartmentdefinition-definitions.html#CompartmentDefinition.resource)> <!-- **0..*** How a resource is related to the compartment -->
 <[**code**](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [Name of resource type](valueset-resource-types.html) -->
 <[**param**](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) value="[[string](datatypes.html#string)]"/><!-- **0..*** [Search Parameter Name, or chained parameters](terminologies.html#unbound) -->
 <[**documentation**](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional documentation about the resource and compartment](terminologies.html#unbound) -->
 </resource>
</CompartmentDefinition>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**CompartmentDefinition**](compartmentdefinition-definitions.html#CompartmentDefinition)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[url](compartmentdefinition-definitions.html#CompartmentDefinition.url)" : "<[uri](datatypes.html#uri)>", // **R!** [Canonical identifier for this compartment definition, represented as a URI (globally unique)](terminologies.html#unbound)
 "[version](compartmentdefinition-definitions.html#CompartmentDefinition.version)" : "<[string](datatypes.html#string)>", // [Business version of the compartment definition](terminologies.html#unbound)
 "[name](compartmentdefinition-definitions.html#CompartmentDefinition.name)" : "<[string](datatypes.html#string)>", // **C?** **R!** [Name for this compartment definition (computer friendly)](terminologies.html#unbound)
 "[status](compartmentdefinition-definitions.html#CompartmentDefinition.status)" : "<[code](datatypes.html#code)>", // **R!** [draft | active | retired | unknown](valueset-publication-status.html)
 "[experimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental)" : <[boolean](datatypes.html#boolean)>, // [For testing purposes, not real usage](terminologies.html#unbound)
 "[date](compartmentdefinition-definitions.html#CompartmentDefinition.date)" : "<[dateTime](datatypes.html#dateTime)>", // [Date last changed](terminologies.html#unbound)
 "[publisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher)" : "<[string](datatypes.html#string)>", // [Name of the publisher (organization or individual)](terminologies.html#unbound)
 "[contact](compartmentdefinition-definitions.html#CompartmentDefinition.contact)" : [{ [ContactDetail](metadatatypes.html#ContactDetail) }], // [Contact details for the publisher](terminologies.html#unbound)
 "[description](compartmentdefinition-definitions.html#CompartmentDefinition.description)" : "<[markdown](datatypes.html#markdown)>", // [Natural language description of the compartment definition](terminologies.html#unbound)
 "[useContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext)" : [{ [UsageContext](metadatatypes.html#UsageContext) }], // [The context that the content is intended to support](terminologies.html#unbound)
 "[purpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose)" : "<[markdown](datatypes.html#markdown)>", // [Why this compartment definition is defined](terminologies.html#unbound)
 "[code](compartmentdefinition-definitions.html#CompartmentDefinition.code)" : "<[code](datatypes.html#code)>", // **R!** [Patient | Encounter | RelatedPerson | Practitioner | Device](valueset-compartment-type.html)
 "[search](compartmentdefinition-definitions.html#CompartmentDefinition.search)" : <[boolean](datatypes.html#boolean)>, // **R!** [Whether the search syntax is supported](terminologies.html#unbound)
 "[resource](compartmentdefinition-definitions.html#CompartmentDefinition.resource)" : [{ // [How a resource is related to the compartment](terminologies.html#unbound)
 "[code](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code)" : "<[code](datatypes.html#code)>", // **R!** [Name of resource type](valueset-resource-types.html)
 "[param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param)" : ["<[string](datatypes.html#string)>"], // [Search Parameter Name, or chained parameters](terminologies.html#unbound)
 "[documentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation)" : "<[string](datatypes.html#string)>" // [Additional documentation about the resource and compartment](terminologies.html#unbound)
 }]
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**CompartmentDefinition**](compartmentdefinition-definitions.html#CompartmentDefinition);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[CompartmentDefinition.url](compartmentdefinition-definitions.html#CompartmentDefinition.url) [ [uri](datatypes.html#uri) ]; # 1..1 Canonical identifier for this compartment definition, represented as a URI (globally unique)
 fhir:[CompartmentDefinition.version](compartmentdefinition-definitions.html#CompartmentDefinition.version) [ [string](datatypes.html#string) ]; # 0..1 Business version of the compartment definition
 fhir:[CompartmentDefinition.name](compartmentdefinition-definitions.html#CompartmentDefinition.name) [ [string](datatypes.html#string) ]; # 1..1 Name for this compartment definition (computer friendly)
 fhir:[CompartmentDefinition.status](compartmentdefinition-definitions.html#CompartmentDefinition.status) [ [code](datatypes.html#code) ]; # 1..1 draft | active | retired | unknown
 fhir:[CompartmentDefinition.experimental](compartmentdefinition-definitions.html#CompartmentDefinition.experimental) [ [boolean](datatypes.html#boolean) ]; # 0..1 For testing purposes, not real usage
 fhir:[CompartmentDefinition.date](compartmentdefinition-definitions.html#CompartmentDefinition.date) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Date last changed
 fhir:[CompartmentDefinition.publisher](compartmentdefinition-definitions.html#CompartmentDefinition.publisher) [ [string](datatypes.html#string) ]; # 0..1 Name of the publisher (organization or individual)
 fhir:[CompartmentDefinition.contact](compartmentdefinition-definitions.html#CompartmentDefinition.contact) [ [ContactDetail](metadatatypes.html#ContactDetail) ], ... ; # 0..* Contact details for the publisher
 fhir:[CompartmentDefinition.description](compartmentdefinition-definitions.html#CompartmentDefinition.description) [ [markdown](datatypes.html#markdown) ]; # 0..1 Natural language description of the compartment definition
 fhir:[CompartmentDefinition.useContext](compartmentdefinition-definitions.html#CompartmentDefinition.useContext) [ [UsageContext](metadatatypes.html#UsageContext) ], ... ; # 0..* The context that the content is intended to support
 fhir:[CompartmentDefinition.purpose](compartmentdefinition-definitions.html#CompartmentDefinition.purpose) [ [markdown](datatypes.html#markdown) ]; # 0..1 Why this compartment definition is defined
 fhir:[CompartmentDefinition.code](compartmentdefinition-definitions.html#CompartmentDefinition.code) [ [code](datatypes.html#code) ]; # 1..1 Patient | Encounter | RelatedPerson | Practitioner | Device
 fhir:[CompartmentDefinition.search](compartmentdefinition-definitions.html#CompartmentDefinition.search) [ [boolean](datatypes.html#boolean) ]; # 1..1 Whether the search syntax is supported
 fhir:[CompartmentDefinition.resource](compartmentdefinition-definitions.html#CompartmentDefinition.resource) [ # 0..* How a resource is related to the compartment
 fhir:[CompartmentDefinition.resource.code](compartmentdefinition-definitions.html#CompartmentDefinition.resource.code) [ [code](datatypes.html#code) ]; # 1..1 Name of resource type
 fhir:[CompartmentDefinition.resource.param](compartmentdefinition-definitions.html#CompartmentDefinition.resource.param) [ [string](datatypes.html#string) ], ... ; # 0..* Search Parameter Name, or chained parameters
 fhir:[CompartmentDefinition.resource.documentation](compartmentdefinition-definitions.html#CompartmentDefinition.resource.documentation) [ [string](datatypes.html#string) ]; # 0..1 Additional documentation about the resource and compartment
 ], ...;
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [CompartmentDefinition](compartmentdefinition.html#CompartmentDefinition)
 | 
 | 
 |

 | 
 CompartmentDefinition | 
 
 

 Min Cardinality changed from 1 to 0

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 CompartmentDefinition.version | 
 
 

 - Added Element

 

 | 
 |

 | 
 CompartmentDefinition.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1

 

 | 
 |

 | 
 CompartmentDefinition.experimental | 
 
 

 - No longer marked as Modifier

 

 | 
 |

 | 
 CompartmentDefinition.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/compartment-type to http://hl7.org/fhir/ValueSet/compartment-type|4.0.1

 

 | 
 |

 | 
 CompartmentDefinition.resource.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/resource-types to http://hl7.org/fhir/ValueSet/resource-types|4.0.1

 

 | 
 |

 | 
 CompartmentDefinition.title | 
 
 

 - deleted

 

 | 
 |

 | 
 CompartmentDefinition.jurisdiction | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](compartmentdefinition.diff.xml) or [JSON](compartmentdefinition.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](compartmentdefinition-version-maps.html) (status = 6 tests that all execute ok. 1 fail round-trip testing and 5 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](compartmentdefinition-profiles.html) and the alternate definitions:
Master Definition [XML](compartmentdefinition.profile.xml.html) + [JSON](compartmentdefinition.profile.json.html),
[XML](xml.html) [Schema](compartmentdefinition.xsd)/[Schematron](compartmentdefinition.sch) + [JSON](json.html) 
[Schema](compartmentdefinition.schema.json.html), [ShEx](compartmentdefinition.shex.html) (for [Turtle](rdf.html)) + [see the extensions](compartmentdefinition-profiles.html) & the [dependency analysis](compartmentdefinition-dependencies.html)

### 5.6.3.1 
Terminology Bindings
 [
](compartmentdefinition.html#tx)

 | Path | Definition | Type | Reference | |

 | CompartmentDefinition.status | The lifecycle status of an artifact. | [Required](terminologies.html#required) | [PublicationStatus](valueset-publication-status.html) | |

 | CompartmentDefinition.code | Which type a compartment definition describes. | [Required](terminologies.html#required) | [CompartmentType](valueset-compartment-type.html) | |

 | CompartmentDefinition.resource.code | One of the resource types defined as part of this version of FHIR. | [Required](terminologies.html#required) | [Resource Types](valueset-resource-types.html) | |

 

 

### 5.6.3.2 Constraints [
](compartmentdefinition.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **cpd-0** | [Warning](conformance-rules.html#warning) | (base) | Name should be usable as an identifier for the module by machine processing applications such as code generation | name.matches('[A-Z]([A-Za-z0-9_]){0,254}') | |

### 5.6.3.3 Using Compartments [](compartmentdefinition.html#use)

As an example of compartment usage, to retrieve a list of a patient's conditions, use the URL:

```
 GET [base]/Patient/[id]/Condition

```

Additional search parameters can be defined, such as this hypothetical search for 
acute conditions:

```
 GET [base]/Patient/[id]/Condition?code:in=http://hspc.org/ValueSet/acute-concerns

```

Note that as searches, these are syntactic variations on these two search
URLs respectively:

```
 GET [base]/Condition?patient=[id]
 GET [base]/Condition?patient=[id]&code:in=http://hspc.org/ValueSet/acute-concerns

```

The outcome of a compartment search is the same as the equivalent normal search. 
For example, both these searches return the same outcome if there is no patient 333:

```
 GET [base]/Patient/333/Condition
 GET [base]/Condition?patient=333

```

Whether the patient doesn't exist, or the user has no access to the patient,
both these searches return an empty bundle with no matches. Some systems 
will include an operation outcome warning that there is no matching patient.

However, there is a key difference in functionality between compartment based searches 
and direct searches with parameters. Consider this search:

```
 GET [base]/Patient/[id]/Communication

```

Because the definition of the [patient compartment](compartmentdefinition-patient.html) for 
[Communication ](communication.html) says that a Communication resource is in the 
patient compartment if the subject, sender, or recipient is the patient, the compartment
search is actually the same as the union of these 3 searches:

```
 GET [base]/Communication?subject=[id]
 GET [base]/Communication?sender=[id]
 GET [base]/Communication?recipient=[id]

```

There is no way to do this as a single search, except by using the [_filter](search_filter.html):

```
 GET [base]/Communication?_filter=subject re [id] or sender re [id] or recipient re [id]

```

Further details of searching by compartment are [described under the search operation](http.html#vsearch).
As a search related operation, the assignment of resources to compartments is only based on 
the current version of any of the resources involved. Note that [contained](references.html#contained)
patient resources cannot create a patient compartment of their own. 

Note that while this specification describes how to use the compartment syntax to find resources 
that are logically associated with the compartment, the compartment is not part of the
identity of the resource. E.g. the response to the following is not defined by this specification:

```
 GET [base]/Patient/[patient-id]/Condition/[resource-id]

```

The response for write operations (PUT/DELETE/PATCH) are also not defined by this
specification. Nor is the response to a POST defined:

```
 POST [base]/Patient/[patient-id]/Condition

```

There is no expectation for servers to support either read or write 
to such URLs.

### 5.6.3.4 Logical Meaning of Compartments [
](compartmentdefinition.html#logical)

Compartments may be used explicitly, like this, but can also be used implicitly. For instance,
if a FHIR server is providing a patient view of a record, the authorized user associated
with use of the FHIR RESTful API may be limited to accessing records from the
compartment instance(s) logically associated with their identity. Irrespective of whether
compartments are being used explicitly or implicitly, servers will need to make arrangements
to make some resources with no direct link to a patient available to the client (medications, 
substances, etc.).

Note that resources may cross between compartments, or interlink them. Examples of 
this would be where a [Diagnostic Report](diagnosticreport.html) identifies 
a subject, but an [Observation](observation.html) it references identifies
a different subject, or where a [List](list.html) resource references
items that identify different subjects. Such cross-linking may arise for 
many valid reasons, including:

 - Cases where subject records are inter-linked - Transplants, Perinatal care, family therapy etc.

 - Workflow management where action lists link multiple patients and/or practitioners

Given the wide variety of use cases and contexts in which FHIR is used, compartments 
do not define how cross-linking is handled. Systems may reject resources, remove them 
from both compartments, or place them in both, or act in some other fashion.

The [graph definition](graphdefinition.html) resource provides a method
by which rules about cross-linking may be made and enforced.

It is at the discretion of the server whether to include resources in a compartment when
the reference to the resource that establishes the compartment is in an extension.

Some resources are not in any compartment, e.g. [Medication](medication.html), 
[Substance](substance.html), [Location](location.html). These resources are not linked directly to a patient 
or authored record, and are sometimes called 'master files'. Servers will need to make 
arrangements to make these resources available to the clients that are limited to 
particular compartments. For example, a Medication resource describes a medication itself 
and does not link to a patient; however, a resource such as MedicationAdministration 
connects the Medication (details of what was administered) to the patient (for whom was 
it administered), and so is required to interpret the administration.

## 5.6.4 Defining New Compartments [
](compartmentdefinition.html#5.6.4)

Compartments are defined and added to the list above when implementer 
communities identify them as common access points for data. As described 
below, compartments have both syntactical and logical consequences, and
both these aspects of their functionality are evaluated when deciding
whether to define compartments. 

## 5.6.5 Search Parameters [
](compartmentdefinition.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| code | [token](search.html#token) | Patient | Encounter | RelatedPerson | Practitioner | Device | CompartmentDefinition.code | | |

| context | [token](search.html#token) | A use context assigned to the compartment definition | (CompartmentDefinition.useContext.value as CodeableConcept) | | |

| context-quantity | [quantity](search.html#quantity) | A quantity- or range-valued use context assigned to the compartment definition | (CompartmentDefinition.useContext.value as Quantity) | (CompartmentDefinition.useContext.value as Range) | | |

| context-type | [token](search.html#token) | A type of use context assigned to the compartment definition | CompartmentDefinition.useContext.code | | |

| context-type-quantity | [composite](search.html#composite) | A use context type and quantity- or range-based value assigned to the compartment definition | On CompartmentDefinition.useContext:
 context-type: code
 context-quantity: value.as(Quantity) | value.as(Range) | | |

| context-type-value | [composite](search.html#composite) | A use context type and value assigned to the compartment definition | On CompartmentDefinition.useContext:
 context-type: code
 context: value.as(CodeableConcept) | | |

| date | [date](search.html#date) | The compartment definition publication date | CompartmentDefinition.date | | |

| description | [string](search.html#string) | The description of the compartment definition | CompartmentDefinition.description | | |

| name | [string](search.html#string) | Computationally friendly name of the compartment definition | CompartmentDefinition.name | | |

| publisher | [string](search.html#string) | Name of the publisher of the compartment definition | CompartmentDefinition.publisher | | |

| resource | [token](search.html#token) | Name of resource type | CompartmentDefinition.resource.code | | |

| status | [token](search.html#token) | The current status of the compartment definition | CompartmentDefinition.status | | |

| url | [uri](search.html#uri) | The uri that identifies the compartment definition | CompartmentDefinition.url | | |

| version | [token](search.html#token) | The business version of the compartment definition | CompartmentDefinition.version | | |