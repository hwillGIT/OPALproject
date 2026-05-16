# User Access Endpoint Profile - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/StructureDefinition-user-access-endpoint.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 

 
 
## Resource Profile:

 User Access Endpoint Profile

 

 

 | 
 *Official URL*: http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-endpoint**
 | 
 *Version*:
 2.2.0
 | 
 |

 | 

 
 
 Active
 
 as of 2023-08-31
 
 
 | 

 *Computable Name*: UserAccessEndpoint | 
 |

 

Profile on Endpoint associated with a User Access Brand.

For background and context, see **[User Access Brands Overview](brands.html#endpoint-profile)**.

In addition to the core data elements on Endpoint, one key extension is used in this profile:

 - [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version) conveys is a denormalization to help clients focus on supported endpoints. The `valueCode` is any version from http://hl7.org/fhir/valueset-FHIR-version.html (e.g., `4.0.1` is expected for FHIR R4 endpoints).

Notes:

 - `0..1` `name` Conveys a fallback or default name describing the endpoint and the organization offering User API access at this endpoint. This value MAY contain technical details like FHIR API Version designations and apps SHOULD preferentially use names from an associated `UserAccessBrand` rather than displaying this value to users.

 - `1..* MS` `contact` website where developers can configure access to this endpoint, providing at least one `"system": "url"` contact point where the `value` is an `https://` URL intended for app developers

 - `1..1 MS` `address` FHIR base URL for server supporting user access

Usage:**

 - Use this Resource Profile: [User Access Brands Bundle Profile](StructureDefinition-user-access-brands-bundle.html)

 - Refer to this Resource Profile: [User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html)

 
 
 
### Formal Views of Profile Content

 

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions).
 

 

 

 - 
 [Differential Table](#tabs-diff)
 

 - 
 [Key Elements Table](#tabs-key)
 

 - 
 [Snapshot Table](#tabs-snap)
 

 

 - 
 [Statistics/References](#tabs-summ)
 

 - 
 [All](#tabs-all)
 

 

 
 

 

 
This structure is derived from [Endpoint](http://hl7.org/fhir/R4/endpoint.html)
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Endpoint](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint) | 
 | 
0..* | 
[Endpoint](http://hl7.org/fhir/R4/endpoint.html) | 
User Access Endpoint | |

| [Slices for extension](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.extension) | 
 | 
1..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension**Slice: Unordered, Open by value:url | |

| [fhir-version](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.extension:fhir-version) | 
S | 
1..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Endpoint FHIR Version
URL: [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)
Binding: [FHIRVersion](http://hl7.org/fhir/R4/valueset-FHIR-version.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [status](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.status) | 
S | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
active | suspended | error | off | entered-in-error | test | |

| [connectionType](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.connectionType) | 
S | 
1..1 | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Protocol/Profile/Standard to be used with this endpoint connection
Required Pattern: At least the following | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-connection-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: hl7-fhir-rest | |

| [name](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.name) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
A name that this endpoint can be identified by | |

| [Slices for contact](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact information for the endpoint.Slice: Unordered, Open by value:system | |

| [contact:configuration-url](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact:configuration-url) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Website where developers can configure access to this endpoint
 | |

| [system](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact:configuration-url.system) | 
S | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
phone | fax | email | pager | url | sms | other
Fixed Value: url | |

| [value](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact:configuration-url.value) | 
S | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
an https:// URL for app developers | |

| [payloadType](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.payloadType) | 
S | 
1..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
Required Pattern: At least the following | |

| [coding](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.coding) | 
 | 
1..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Code defined by a terminology system
Fixed Value: (complex) | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-payload-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: none | |

| [address](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.address) | 
S | 
1..1 | 
[url](http://hl7.org/fhir/R4/datatypes.html#url) | 
FHIR base URL for servers supporting user access | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
 
 
 
 
 
 

 

 

 
 

 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Endpoint](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint) | 
 | 
0..* | 
[Endpoint](http://hl7.org/fhir/R4/endpoint.html) | 
User Access Endpoint
 | |

| [implicitRules](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [Slices for extension](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.extension) | 
 | 
1..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [fhir-version](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.extension:fhir-version) | 
S | 
1..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Endpoint FHIR Version
URL: [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)
Binding: [FHIRVersion](http://hl7.org/fhir/R4/valueset-FHIR-version.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [modifierExtension](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [status](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.status) | 
?!SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
active | suspended | error | off | entered-in-error | test
Binding: [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): The status of the endpoint.

 | |

| [connectionType](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.connectionType) | 
SΣ | 
1..1 | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Protocol/Profile/Standard to be used with this endpoint connection
Binding: [EndpointConnectionType](http://hl7.org/fhir/R4/valueset-endpoint-connection-type.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible))
Required Pattern: At least the following | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-connection-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: hl7-fhir-rest | |

| [name](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.name) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
A name that this endpoint can be identified by | |

| [Slices for contact](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact information for the endpoint.Slice: Unordered, Open by value:system | |

| [contact:configuration-url](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Website where developers can configure access to this endpoint
 | |

| [system](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url.system) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
phone | fax | email | pager | url | sms | other
Binding: [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Telecommunications form for contact point.

Fixed Value: url | |

| [value](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url.value) | 
SΣ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
an https:// URL for app developers | |

| [use](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url.use) | 
?!Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
home | work | temp | old | mobile - purpose of this contact point
Binding: [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Use of contact point.

 | |

| [payloadType](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.payloadType) | 
SΣ | 
1..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
Binding: [EndpointPayloadType](http://hl7.org/fhir/R4/valueset-endpoint-payload-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example))

Required Pattern: At least the following | |

| [coding](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.coding) | 
 | 
1..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Code defined by a terminology system
Fixed Value: (complex) | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-payload-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: none | |

| [address](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.address) | 
SΣ | 
1..1 | 
[url](http://hl7.org/fhir/R4/datatypes.html#url) | 
FHIR base URL for servers supporting user access | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Endpoint.status | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html)
`http://hl7.org/fhir/ValueSet/endpoint-status|4.0.1`**

from the FHIR Standard
 | |

| Endpoint.connectionType | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | Pattern: [hl7-fhir-rest](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-rest)
`http://hl7.org/fhir/ValueSet/endpoint-connection-type`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.system | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: url
`http://hl7.org/fhir/ValueSet/contact-point-system|4.0.1`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.use | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html)
`http://hl7.org/fhir/ValueSet/contact-point-use|4.0.1`

from the FHIR Standard
 | |

| Endpoint.payloadType | [example](http://hl7.org/fhir/R4/terminologies.html#example) | Pattern: [none](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-payload-type.html#endpoint-payload-type-none)
`http://hl7.org/fhir/ValueSet/endpoint-payload-type`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Endpoint | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Endpoint | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Endpoint | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 
 

 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Endpoint](StructureDefinition-user-access-endpoint-definitions.html#Endpoint) | 
 | 
0..* | 
[Endpoint](http://hl7.org/fhir/R4/endpoint.html) | 
User Access Endpoint
 | |

| [id](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.id) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Logical id of this artifact | |

| [meta](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.meta) | 
Σ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [implicitRules](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [language](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.language) | 
 | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Language of the resource content
Binding: [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) ([preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)): A human language.

| Additional Bindings** | Purpose | |

| [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html) | 
[Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html) | |

|

| [text](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.text) | 
 | 
0..1 | 
[Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) | 
Text summary of the resource, for human interpretation | |

| [contained](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contained) | 
 | 
0..* | 
Resource | 
Contained, inline Resources** | |

| [Slices for extension](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.extension) | 
 | 
1..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [fhir-version](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.extension:fhir-version) | 
S | 
1..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Endpoint FHIR Version
URL: [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)
Binding: [FHIRVersion](http://hl7.org/fhir/R4/valueset-FHIR-version.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [modifierExtension](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [identifier](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.identifier) | 
Σ | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Identifies this endpoint across multiple systems
 | |

| [status](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.status) | 
?!SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
active | suspended | error | off | entered-in-error | test
Binding: [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): The status of the endpoint.

 | |

| [connectionType](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.connectionType) | 
SΣ | 
1..1 | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Protocol/Profile/Standard to be used with this endpoint connection
Binding: [EndpointConnectionType](http://hl7.org/fhir/R4/valueset-endpoint-connection-type.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible))
Required Pattern: At least the following | |

| [id](http://hl7.org/fhir/R4/element-definitions.html#Element.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](http://hl7.org/fhir/R4/element-definitions.html#Element.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-connection-type | |

| [version](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.version) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Version of the system - if relevant | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: hl7-fhir-rest | |

| [display](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.display) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Representation defined by the system | |

| [userSelected](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.userSelected) | 
 | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
If this coding was chosen directly by the user | |

| [name](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.name) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
A name that this endpoint can be identified by | |

| [managingOrganization](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.managingOrganization) | 
Σ | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Organization that manages this endpoint (might not be the organization that exposes the endpoint) | |

| [Slices for contact](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact information for the endpoint.Slice: Unordered, Open by value:system | |

| [contact:configuration-url](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Website where developers can configure access to this endpoint
 | |

| [id](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
Slice: Unordered, Open by value:url
 | |

| [system](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.system) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
phone | fax | email | pager | url | sms | other
Binding: [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Telecommunications form for contact point.

Fixed Value: url | |

| [value](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.value) | 
SΣ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
an https:// URL for app developers | |

| [use](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.use) | 
?!Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
home | work | temp | old | mobile - purpose of this contact point
Binding: [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Use of contact point.

 | |

| [rank](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.rank) | 
Σ | 
0..1 | 
[positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) | 
Specify preferred order of use (1 = highest) | |

| [period](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.period) | 
Σ | 
0..1 | 
[Period](http://hl7.org/fhir/R4/datatypes.html#Period) | 
Time period when the contact point was/is in use | |

| [period](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.period) | 
Σ | 
0..1 | 
[Period](http://hl7.org/fhir/R4/datatypes.html#Period) | 
Interval the endpoint is expected to be operational | |

| [payloadType](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.payloadType) | 
SΣ | 
1..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
Binding: [EndpointPayloadType](http://hl7.org/fhir/R4/valueset-endpoint-payload-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example))

Required Pattern: At least the following | |

| [id](http://hl7.org/fhir/R4/element-definitions.html#Element.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](http://hl7.org/fhir/R4/element-definitions.html#Element.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations | |

| [coding](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.coding) | 
 | 
1..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Code defined by a terminology system
Fixed Value: (complex) | |

| [id](http://hl7.org/fhir/R4/element-definitions.html#Element.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](http://hl7.org/fhir/R4/element-definitions.html#Element.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-payload-type | |

| [version](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.version) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Version of the system - if relevant | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: none | |

| [display](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.display) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Representation defined by the system | |

| [userSelected](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.userSelected) | 
 | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
If this coding was chosen directly by the user | |

| [text](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.text) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Plain text representation of the concept | |

| [payloadMimeType](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.payloadMimeType) | 
Σ | 
0..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Mimetype to send. If not specified, the content could be anything (including no payload, if the connectionType defined this)
Binding: [Mime Types](http://hl7.org/fhir/R4/valueset-mimetypes.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): The mime type of an attachment. Any valid mime type is allowed.

 | |

| [address](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.address) | 
SΣ | 
1..1 | 
[url](http://hl7.org/fhir/R4/datatypes.html#url) | 
FHIR base URL for servers supporting user access | |

| [header](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.header) | 
 | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Usage depends on the channel type
 | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Endpoint.language | [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred) | [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html)

 | 
 
 **Additional Bindings**
 | 
 Purpose | 
 |

 | 
 
 [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html)
 | 
 
 [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html)
 | 
 |

`http://hl7.org/fhir/ValueSet/languages`**

from the FHIR Standard
|

| Endpoint.status | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html)
`http://hl7.org/fhir/ValueSet/endpoint-status|4.0.1`

from the FHIR Standard
 | |

| Endpoint.connectionType | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | Pattern: [hl7-fhir-rest](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-rest)
`http://hl7.org/fhir/ValueSet/endpoint-connection-type`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.system | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: url
`http://hl7.org/fhir/ValueSet/contact-point-system|4.0.1`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.use | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html)
`http://hl7.org/fhir/ValueSet/contact-point-use|4.0.1`

from the FHIR Standard
 | |

| Endpoint.payloadType | [example](http://hl7.org/fhir/R4/terminologies.html#example) | Pattern: [none](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-payload-type.html#endpoint-payload-type-none)
`http://hl7.org/fhir/ValueSet/endpoint-payload-type`

from the FHIR Standard
 | |

| Endpoint.payloadMimeType | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [Mime Types](http://hl7.org/fhir/R4/valueset-mimetypes.html) (a valid code from `urn:ietf:bcp:13`)
`http://hl7.org/fhir/ValueSet/mimetypes|4.0.1`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Endpoint | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Endpoint | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Endpoint | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 

 
 

 

 
This structure is derived from [Endpoint](http://hl7.org/fhir/R4/endpoint.html)
 

 

 
 

Summary
**

Mandatory: 6 elements** Must-Support: 9 elements
 Fixed: 1 element

Extensions**

This structure refers to these extensions:

- [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

- The element 1 is sliced based on the value of Endpoint.contact

 

 

 

 
 

 

 

 **Differential View**
 

 
This structure is derived from [Endpoint](http://hl7.org/fhir/R4/endpoint.html)
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Endpoint](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint) | 
 | 
0..* | 
[Endpoint](http://hl7.org/fhir/R4/endpoint.html) | 
User Access Endpoint | |

| [Slices for extension](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.extension) | 
 | 
1..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension**Slice: Unordered, Open by value:url | |

| [fhir-version](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.extension:fhir-version) | 
S | 
1..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Endpoint FHIR Version
URL: [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)
Binding: [FHIRVersion](http://hl7.org/fhir/R4/valueset-FHIR-version.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [status](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.status) | 
S | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
active | suspended | error | off | entered-in-error | test | |

| [connectionType](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.connectionType) | 
S | 
1..1 | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Protocol/Profile/Standard to be used with this endpoint connection
Required Pattern: At least the following | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-connection-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: hl7-fhir-rest | |

| [name](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.name) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
A name that this endpoint can be identified by | |

| [Slices for contact](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact information for the endpoint.Slice: Unordered, Open by value:system | |

| [contact:configuration-url](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact:configuration-url) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Website where developers can configure access to this endpoint
 | |

| [system](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact:configuration-url.system) | 
S | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
phone | fax | email | pager | url | sms | other
Fixed Value: url | |

| [value](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.contact:configuration-url.value) | 
S | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
an https:// URL for app developers | |

| [payloadType](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.payloadType) | 
S | 
1..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
Required Pattern: At least the following | |

| [coding](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.coding) | 
 | 
1..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Code defined by a terminology system
Fixed Value: (complex) | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-payload-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: none | |

| [address](StructureDefinition-user-access-endpoint-definitions.html#diff_Endpoint.address) | 
S | 
1..1 | 
[url](http://hl7.org/fhir/R4/datatypes.html#url) | 
FHIR base URL for servers supporting user access | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
 
 
 
 
 

 

 

 

 Key Elements View**
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Endpoint](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint) | 
 | 
0..* | 
[Endpoint](http://hl7.org/fhir/R4/endpoint.html) | 
User Access Endpoint** | |

| [implicitRules](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [Slices for extension](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.extension) | 
 | 
1..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [fhir-version](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.extension:fhir-version) | 
S | 
1..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Endpoint FHIR Version
URL: [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)
Binding: [FHIRVersion](http://hl7.org/fhir/R4/valueset-FHIR-version.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [modifierExtension](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [status](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.status) | 
?!SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
active | suspended | error | off | entered-in-error | test
Binding: [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): The status of the endpoint.

 | |

| [connectionType](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.connectionType) | 
SΣ | 
1..1 | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Protocol/Profile/Standard to be used with this endpoint connection
Binding: [EndpointConnectionType](http://hl7.org/fhir/R4/valueset-endpoint-connection-type.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible))
Required Pattern: At least the following | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-connection-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: hl7-fhir-rest | |

| [name](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.name) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
A name that this endpoint can be identified by | |

| [Slices for contact](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact information for the endpoint.Slice: Unordered, Open by value:system | |

| [contact:configuration-url](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Website where developers can configure access to this endpoint
 | |

| [system](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url.system) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
phone | fax | email | pager | url | sms | other
Binding: [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Telecommunications form for contact point.

Fixed Value: url | |

| [value](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url.value) | 
SΣ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
an https:// URL for app developers | |

| [use](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.contact:configuration-url.use) | 
?!Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
home | work | temp | old | mobile - purpose of this contact point
Binding: [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Use of contact point.

 | |

| [payloadType](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.payloadType) | 
SΣ | 
1..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
Binding: [EndpointPayloadType](http://hl7.org/fhir/R4/valueset-endpoint-payload-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example))

Required Pattern: At least the following | |

| [coding](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.coding) | 
 | 
1..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Code defined by a terminology system
Fixed Value: (complex) | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-payload-type | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: none | |

| [address](StructureDefinition-user-access-endpoint-definitions.html#key_Endpoint.address) | 
SΣ | 
1..1 | 
[url](http://hl7.org/fhir/R4/datatypes.html#url) | 
FHIR base URL for servers supporting user access | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Endpoint.status | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html)
`http://hl7.org/fhir/ValueSet/endpoint-status|4.0.1`**

from the FHIR Standard
 | |

| Endpoint.connectionType | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | Pattern: [hl7-fhir-rest](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-rest)
`http://hl7.org/fhir/ValueSet/endpoint-connection-type`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.system | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: url
`http://hl7.org/fhir/ValueSet/contact-point-system|4.0.1`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.use | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html)
`http://hl7.org/fhir/ValueSet/contact-point-use|4.0.1`

from the FHIR Standard
 | |

| Endpoint.payloadType | [example](http://hl7.org/fhir/R4/terminologies.html#example) | Pattern: [none](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-payload-type.html#endpoint-payload-type-none)
`http://hl7.org/fhir/ValueSet/endpoint-payload-type`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Endpoint | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Endpoint | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Endpoint | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 

 Snapshot View**
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Endpoint](StructureDefinition-user-access-endpoint-definitions.html#Endpoint) | 
 | 
0..* | 
[Endpoint](http://hl7.org/fhir/R4/endpoint.html) | 
User Access Endpoint** | |

| [id](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.id) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Logical id of this artifact | |

| [meta](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.meta) | 
Σ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [implicitRules](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [language](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.language) | 
 | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Language of the resource content
Binding: [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) ([preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)): A human language.

| Additional Bindings** | Purpose | |

| [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html) | 
[Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html) | |

|

| [text](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.text) | 
 | 
0..1 | 
[Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) | 
Text summary of the resource, for human interpretation | |

| [contained](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contained) | 
 | 
0..* | 
Resource | 
Contained, inline Resources** | |

| [Slices for extension](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.extension) | 
 | 
1..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [fhir-version](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.extension:fhir-version) | 
S | 
1..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Endpoint FHIR Version
URL: [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)
Binding: [FHIRVersion](http://hl7.org/fhir/R4/valueset-FHIR-version.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [modifierExtension](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [identifier](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.identifier) | 
Σ | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Identifies this endpoint across multiple systems
 | |

| [status](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.status) | 
?!SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
active | suspended | error | off | entered-in-error | test
Binding: [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): The status of the endpoint.

 | |

| [connectionType](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.connectionType) | 
SΣ | 
1..1 | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Protocol/Profile/Standard to be used with this endpoint connection
Binding: [EndpointConnectionType](http://hl7.org/fhir/R4/valueset-endpoint-connection-type.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible))
Required Pattern: At least the following | |

| [id](http://hl7.org/fhir/R4/element-definitions.html#Element.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](http://hl7.org/fhir/R4/element-definitions.html#Element.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-connection-type | |

| [version](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.version) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Version of the system - if relevant | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: hl7-fhir-rest | |

| [display](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.display) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Representation defined by the system | |

| [userSelected](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.userSelected) | 
 | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
If this coding was chosen directly by the user | |

| [name](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.name) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
A name that this endpoint can be identified by | |

| [managingOrganization](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.managingOrganization) | 
Σ | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Organization that manages this endpoint (might not be the organization that exposes the endpoint) | |

| [Slices for contact](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact information for the endpoint.Slice: Unordered, Open by value:system | |

| [contact:configuration-url](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url) | 
S | 
1..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Website where developers can configure access to this endpoint
 | |

| [id](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
Slice: Unordered, Open by value:url
 | |

| [system](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.system) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
phone | fax | email | pager | url | sms | other
Binding: [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Telecommunications form for contact point.

Fixed Value: url | |

| [value](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.value) | 
SΣ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
an https:// URL for app developers | |

| [use](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.use) | 
?!Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
home | work | temp | old | mobile - purpose of this contact point
Binding: [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Use of contact point.

 | |

| [rank](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.rank) | 
Σ | 
0..1 | 
[positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) | 
Specify preferred order of use (1 = highest) | |

| [period](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.contact:configuration-url.period) | 
Σ | 
0..1 | 
[Period](http://hl7.org/fhir/R4/datatypes.html#Period) | 
Time period when the contact point was/is in use | |

| [period](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.period) | 
Σ | 
0..1 | 
[Period](http://hl7.org/fhir/R4/datatypes.html#Period) | 
Interval the endpoint is expected to be operational | |

| [payloadType](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.payloadType) | 
SΣ | 
1..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
Binding: [EndpointPayloadType](http://hl7.org/fhir/R4/valueset-endpoint-payload-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example))

Required Pattern: At least the following | |

| [id](http://hl7.org/fhir/R4/element-definitions.html#Element.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](http://hl7.org/fhir/R4/element-definitions.html#Element.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations | |

| [coding](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.coding) | 
 | 
1..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Code defined by a terminology system
Fixed Value: (complex) | |

| [id](http://hl7.org/fhir/R4/element-definitions.html#Element.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](http://hl7.org/fhir/R4/element-definitions.html#Element.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations | |

| [system](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.system) | 
 | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identity of the terminology system
Fixed Value: http://terminology.hl7.org/CodeSystem/endpoint-payload-type | |

| [version](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.version) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Version of the system - if relevant | |

| [code](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.code) | 
 | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Symbol in syntax defined by the system
Fixed Value: none | |

| [display](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.display) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Representation defined by the system | |

| [userSelected](http://hl7.org/fhir/R4/datatypes-definitions.html#Coding.userSelected) | 
 | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
If this coding was chosen directly by the user | |

| [text](http://hl7.org/fhir/R4/datatypes-definitions.html#CodeableConcept.text) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Plain text representation of the concept | |

| [payloadMimeType](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.payloadMimeType) | 
Σ | 
0..* | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Mimetype to send. If not specified, the content could be anything (including no payload, if the connectionType defined this)
Binding: [Mime Types](http://hl7.org/fhir/R4/valueset-mimetypes.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): The mime type of an attachment. Any valid mime type is allowed.

 | |

| [address](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.address) | 
SΣ | 
1..1 | 
[url](http://hl7.org/fhir/R4/datatypes.html#url) | 
FHIR base URL for servers supporting user access | |

| [header](StructureDefinition-user-access-endpoint-definitions.html#Endpoint.header) | 
 | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Usage depends on the channel type
 | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Endpoint.language | [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred) | [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html)

 | 
 
 **Additional Bindings**
 | 
 Purpose | 
 |

 | 
 
 [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html)
 | 
 
 [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html)
 | 
 |

`http://hl7.org/fhir/ValueSet/languages`**

from the FHIR Standard
|

| Endpoint.status | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html)
`http://hl7.org/fhir/ValueSet/endpoint-status|4.0.1`

from the FHIR Standard
 | |

| Endpoint.connectionType | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | Pattern: [hl7-fhir-rest](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-connection-type.html#endpoint-connection-type-hl7-fhir-rest)
`http://hl7.org/fhir/ValueSet/endpoint-connection-type`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.system | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: url
`http://hl7.org/fhir/ValueSet/contact-point-system|4.0.1`

from the FHIR Standard
 | |

| Endpoint.contact:configuration-url.use | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html)
`http://hl7.org/fhir/ValueSet/contact-point-use|4.0.1`

from the FHIR Standard
 | |

| Endpoint.payloadType | [example](http://hl7.org/fhir/R4/terminologies.html#example) | Pattern: [none](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-payload-type.html#endpoint-payload-type-none)
`http://hl7.org/fhir/ValueSet/endpoint-payload-type`

from the FHIR Standard
 | |

| Endpoint.payloadMimeType | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [Mime Types](http://hl7.org/fhir/R4/valueset-mimetypes.html) (a valid code from `urn:ietf:bcp:13`)
`http://hl7.org/fhir/ValueSet/mimetypes|4.0.1`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Endpoint | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Endpoint | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Endpoint | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Endpoint | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 

 

 

 
This structure is derived from [Endpoint](http://hl7.org/fhir/R4/endpoint.html)
 

 

 

Summary
**

Mandatory: 6 elements** Must-Support: 9 elements
 Fixed: 1 element

Extensions**

This structure refers to these extensions:

- [http://hl7.org/fhir/StructureDefinition/endpoint-fhir-version](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-endpoint-fhir-version.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

- The element 1 is sliced based on the value of Endpoint.contact

 

 

 

 

 
 

 
Other representations of profile: [CSV](StructureDefinition-user-access-endpoint.csv), [Excel](StructureDefinition-user-access-endpoint.xlsx), [Schematron](StructureDefinition-user-access-endpoint.sch)