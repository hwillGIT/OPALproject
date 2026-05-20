# User Access Brands Bundle Profile - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/StructureDefinition-user-access-brands-bundle.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 

 
 
## Resource Profile:

 User Access Brands Bundle Profile

 

 

 | 
 *Official URL*: http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-brands-bundle**
 | 
 *Version*:
 2.2.0
 | 
 |

 | 

 
 
 Active
 
 as of 2023-03-19
 
 
 | 

 *Computable Name*: UserAccessBrandsBundle | 
 |

 

JSON FHIR Bundle (type: `collection`) of Organizations and Endpoints that is hosted at a stable, publicly available, publicly disclosed location.

For background and context, see **[User Access Brands Overview](brands.html#brand-bundle-profile)**.

Bundle Entries include:

 - [User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html) resources.

 - [User Access Brand (Organization)](StructureDefinition-user-access-brand.html) resources. Vendors SHALL publish at least a “primary brand” for each endpoint and SHOULD support the publication of a more detailed Brand hierarchy.

Brand Bundles SHALL populate `Bundle.timestamp` to advertise the timestamp of the last change to the contents. In addition, Brand Bundles SHOULD populate `Bundle.entry.resource.meta.lastUpdated` with a more detailed timestamp if the system tracks updates per Resource.

Usage:**

 - This Resource Profile is not used by any profiles in this Implementation Guide

 
 
 
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
 

 

 
 

 

 
This structure is derived from [Bundle](http://hl7.org/fhir/R4/bundle.html)
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Bundle](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle) | 
 | 
0..* | 
[Bundle](http://hl7.org/fhir/R4/bundle.html) | 
User Access Brands Bundle | |

| [meta](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.meta) | 
S | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [lastUpdated](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.meta.lastUpdated) | 
S | 
1..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the resource version last changed | |

| [type](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.type) | 
S | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection**Fixed Value: collection | |

| [Slices for entry](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry) | 
S | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or informationSlice: Unordered, Open by type:resource | |

| [entry:UserAccessEndpoint](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessEndpoint) | 
S | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessEndpoint.resource) | 
S | 
0..1 | 
[UserAccessEndpoint](StructureDefinition-user-access-endpoint.html) | 
User Access Endpoint | |

| [entry:UserAccessBrand](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessBrand) | 
S | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessBrand.resource) | 
S | 
0..1 | 
[UserAccessBrand](StructureDefinition-user-access-brand.html) | 
User Access Brand | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
 
 
 
 
 
 

 

 

 
 

 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Bundle](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Bundle](http://hl7.org/fhir/R4/bundle.html) | 
User Access Brands Bundle
bdl-1: total only when a search or history
bdl-2: entry.search only when a search
bdl-3: entry.request mandatory for batch/transaction/history, otherwise prohibited
bdl-4: entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
bdl-7: FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
bdl-9: A document must have an identifier with a system and a value
bdl-10: A document must have a date
bdl-11: A document must have a Composition as the first resource
bdl-12: A message must have a MessageHeader as the first resource
 | |

| [meta](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.meta) | 
SΣ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [lastUpdated](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.meta.lastUpdated) | 
SΣ | 
1..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the resource version last changed | |

| [implicitRules](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [type](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.type) | 
SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection
Binding: [BundleType](http://hl7.org/fhir/R4/valueset-bundle-type.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Indicates the purpose of a bundle - how it is intended to be used.

Fixed Value: collection | |

| [Slices for entry](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or informationSlice: Unordered, Open by type:resourcebdl-5: must be a resource unless there's a request or responsebdl-8: fullUrl cannot be a version specific referenceThis repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| entry:All Slices | 
 | 
 | 
 | 
Content/Rules for all slices | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [entry:UserAccessEndpoint](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessEndpoint) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessEndpoint.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessEndpoint.resource) | 
S | 
0..1 | 
[UserAccessEndpoint](StructureDefinition-user-access-endpoint.html) | 
User Access Endpoint | |

| [entry:UserAccessBrand](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessBrand) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessBrand.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessBrand.resource) | 
S | 
0..1 | 
[UserAccessBrand](StructureDefinition-user-access-brand.html) | 
User Access Brand | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Bundle.type | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: collection
`http://hl7.org/fhir/ValueSet/bundle-type|4.0.1`**

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| bdl-1 | error | Bundle | total only when a search or history**: total.empty() or (type = 'searchset') or (type = 'history') | | |

| bdl-2 | error | Bundle | entry.search only when a search
: entry.search.empty() or (type = 'searchset') | | |

| bdl-3 | error | Bundle | entry.request mandatory for batch/transaction/history, otherwise prohibited
: entry.all(request.exists() = (%resource.type = 'batch' or %resource.type = 'transaction' or %resource.type = 'history')) | | |

| bdl-4 | error | Bundle | entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
: entry.all(response.exists() = (%resource.type = 'batch-response' or %resource.type = 'transaction-response' or %resource.type = 'history')) | | |

| bdl-5 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | must be a resource unless there's a request or response
: resource.exists() or request.exists() or response.exists() | | |

| bdl-7 | error | Bundle | FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
: (type = 'history') or entry.where(fullUrl.exists()).select(fullUrl&resource.meta.versionId).isDistinct() | | |

| bdl-8 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | fullUrl cannot be a version specific reference
: fullUrl.contains('/_history/').not() | | |

| bdl-9 | error | Bundle | A document must have an identifier with a system and a value
: type = 'document' implies (identifier.system.exists() and identifier.value.exists()) | | |

| bdl-10 | error | Bundle | A document must have a date
: type = 'document' implies (timestamp.hasValue()) | | |

| bdl-11 | error | Bundle | A document must have a Composition as the first resource
: type = 'document' implies entry.first().resource.is(Composition) | | |

| bdl-12 | error | Bundle | A message must have a MessageHeader as the first resource
: type = 'message' implies entry.first().resource.is(MessageHeader) | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 
 

 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Bundle](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Bundle](http://hl7.org/fhir/R4/bundle.html) | 
User Access Brands Bundle
bdl-1: total only when a search or history
bdl-2: entry.search only when a search
bdl-3: entry.request mandatory for batch/transaction/history, otherwise prohibited
bdl-4: entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
bdl-7: FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
bdl-9: A document must have an identifier with a system and a value
bdl-10: A document must have a date
bdl-11: A document must have a Composition as the first resource
bdl-12: A message must have a MessageHeader as the first resource
 | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.id) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Logical id of this artifact | |

| [meta](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta) | 
SΣ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
Slice: Unordered, Open by value:url
 | |

| [versionId](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.versionId) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Version specific identifier | |

| [lastUpdated](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.lastUpdated) | 
SΣ | 
1..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the resource version last changed | |

| [source](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.source) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identifies where the resource comes from | |

| [profile](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.profile) | 
Σ | 
0..* | 
[canonical](http://hl7.org/fhir/R4/references.html)([StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)) | 
Profiles this resource claims to conform to
 | |

| [security](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.security) | 
Σ | 
0..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Security Labels applied to this resource
Binding: [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)): Security Labels from the Healthcare Privacy and Security Classification System.

 | |

| [tag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.tag) | 
Σ | 
0..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Tags applied to this resource
Binding: [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example)): Codes that represent various types of tags, commonly workflow-related; e.g. "Needs review by Dr. Jones".

 | |

| [implicitRules](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [language](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.language) | 
 | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Language of the resource content
Binding: [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) ([preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)): A human language.

| Additional Bindings** | Purpose | |

| [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html) | 
[Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html) | |

|

| [identifier](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.identifier) | 
Σ | 
0..1 | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Persistent identifier for the bundle | |

| [type](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.type) | 
SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection**Binding: [BundleType](http://hl7.org/fhir/R4/valueset-bundle-type.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Indicates the purpose of a bundle - how it is intended to be used.

Fixed Value: collection | |

| [timestamp](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.timestamp) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the bundle was assembled | |

| [total](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.total) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[unsignedInt](http://hl7.org/fhir/R4/datatypes.html#unsignedInt) | 
If search, the total number of matches | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link) | 
Σ | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Links related to this Bundle
 | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [relation](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.relation) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Reference details for the link | |

| [Slices for entry](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or informationSlice: Unordered, Open by type:resourcebdl-5: must be a resource unless there's a request or responsebdl-8: fullUrl cannot be a version specific referenceThis repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| entry:All Slices | 
 | 
 | 
 | 
Content/Rules for all slices | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.link) | 
Σ | 
0..* | 
See [link (Bundle)](http://hl7.org/fhir/R4/bundle.html#Bundle.link) | 
Links related to this entry
 | |

| [fullUrl](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.fullUrl) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URI for resource (Absolute URL server address or URI for UUID/OID) | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.resource) | 
Σ | 
0..1 | 
Resource | 
A resource in the bundle | |

| [search](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Search related information | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [mode](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.mode) | 
Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
match | include | outcome - why this is in the result set
Binding: [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.

 | |

| [score](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.score) | 
Σ | 
0..1 | 
[decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) | 
Search ranking (between 0 and 1) | |

| [request](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Additional execution information (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [method](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.method) | 
Σ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
GET | HEAD | POST | PUT | DELETE | PATCH
Binding: [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.

 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URL for HTTP equivalent of this entry | |

| [ifNoneMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifNoneMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing cache currency | |

| [ifModifiedSince](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifModifiedSince) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
For managing cache currency | |

| [ifMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing update contention | |

| [ifNoneExist](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifNoneExist) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For conditional creates | |

| [response](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Results of execution (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [status](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.status) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Status response code (text optional) | |

| [location](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.location) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
The location (if the operation returns a location) | |

| [etag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.etag) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
The Etag for the resource (if relevant) | |

| [lastModified](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.lastModified) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
Server's date time modified | |

| [outcome](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.outcome) | 
Σ | 
0..1 | 
Resource | 
OperationOutcome with hints and warnings (for batch/transaction) | |

| [entry:UserAccessEndpoint](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.link) | 
Σ | 
0..* | 
See [link (Bundle)](http://hl7.org/fhir/R4/bundle.html#Bundle.link) | 
Links related to this entry
 | |

| [fullUrl](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.fullUrl) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URI for resource (Absolute URL server address or URI for UUID/OID) | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.resource) | 
S | 
0..1 | 
[UserAccessEndpoint](StructureDefinition-user-access-endpoint.html) | 
User Access Endpoint | |

| [search](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Search related information | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [mode](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.mode) | 
Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
match | include | outcome - why this is in the result set
Binding: [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.

 | |

| [score](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.score) | 
Σ | 
0..1 | 
[decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) | 
Search ranking (between 0 and 1) | |

| [request](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Additional execution information (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [method](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.method) | 
Σ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
GET | HEAD | POST | PUT | DELETE | PATCH
Binding: [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.

 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URL for HTTP equivalent of this entry | |

| [ifNoneMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifNoneMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing cache currency | |

| [ifModifiedSince](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifModifiedSince) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
For managing cache currency | |

| [ifMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing update contention | |

| [ifNoneExist](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifNoneExist) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For conditional creates | |

| [response](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Results of execution (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [status](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.status) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Status response code (text optional) | |

| [location](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.location) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
The location (if the operation returns a location) | |

| [etag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.etag) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
The Etag for the resource (if relevant) | |

| [lastModified](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.lastModified) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
Server's date time modified | |

| [outcome](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.outcome) | 
Σ | 
0..1 | 
Resource | 
OperationOutcome with hints and warnings (for batch/transaction) | |

| [entry:UserAccessBrand](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.link) | 
Σ | 
0..* | 
See [link (Bundle)](http://hl7.org/fhir/R4/bundle.html#Bundle.link) | 
Links related to this entry
 | |

| [fullUrl](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.fullUrl) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URI for resource (Absolute URL server address or URI for UUID/OID) | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.resource) | 
S | 
0..1 | 
[UserAccessBrand](StructureDefinition-user-access-brand.html) | 
User Access Brand | |

| [search](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Search related information | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [mode](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.mode) | 
Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
match | include | outcome - why this is in the result set
Binding: [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.

 | |

| [score](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.score) | 
Σ | 
0..1 | 
[decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) | 
Search ranking (between 0 and 1) | |

| [request](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Additional execution information (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [method](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.method) | 
Σ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
GET | HEAD | POST | PUT | DELETE | PATCH
Binding: [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.

 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URL for HTTP equivalent of this entry | |

| [ifNoneMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifNoneMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing cache currency | |

| [ifModifiedSince](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifModifiedSince) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
For managing cache currency | |

| [ifMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing update contention | |

| [ifNoneExist](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifNoneExist) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For conditional creates | |

| [response](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Results of execution (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [status](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.status) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Status response code (text optional) | |

| [location](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.location) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
The location (if the operation returns a location) | |

| [etag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.etag) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
The Etag for the resource (if relevant) | |

| [lastModified](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.lastModified) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
Server's date time modified | |

| [outcome](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.outcome) | 
Σ | 
0..1 | 
Resource | 
OperationOutcome with hints and warnings (for batch/transaction) | |

| [signature](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.signature) | 
Σ | 
0..1 | 
[Signature](http://hl7.org/fhir/R4/datatypes.html#Signature) | 
Digital Signature | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Bundle.meta.security | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html)
`http://hl7.org/fhir/ValueSet/security-labels`**

from the FHIR Standard
 | |

| Bundle.meta.tag | [example](http://hl7.org/fhir/R4/terminologies.html#example) | [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html)
`http://hl7.org/fhir/ValueSet/common-tags`

from the FHIR Standard
 | |

| Bundle.language | [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred) | [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html)

 | 
 
 Additional Bindings**
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

| Bundle.type | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: collection
`http://hl7.org/fhir/ValueSet/bundle-type|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry.search.mode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html)
`http://hl7.org/fhir/ValueSet/search-entry-mode|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry.request.method | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html)
`http://hl7.org/fhir/ValueSet/http-verb|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessEndpoint.search.mode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html)
`http://hl7.org/fhir/ValueSet/search-entry-mode|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessEndpoint.request.method | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html)
`http://hl7.org/fhir/ValueSet/http-verb|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessBrand.search.mode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html)
`http://hl7.org/fhir/ValueSet/search-entry-mode|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessBrand.request.method | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html)
`http://hl7.org/fhir/ValueSet/http-verb|4.0.1`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| bdl-1 | error | Bundle | total only when a search or history**: total.empty() or (type = 'searchset') or (type = 'history') | | |

| bdl-2 | error | Bundle | entry.search only when a search
: entry.search.empty() or (type = 'searchset') | | |

| bdl-3 | error | Bundle | entry.request mandatory for batch/transaction/history, otherwise prohibited
: entry.all(request.exists() = (%resource.type = 'batch' or %resource.type = 'transaction' or %resource.type = 'history')) | | |

| bdl-4 | error | Bundle | entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
: entry.all(response.exists() = (%resource.type = 'batch-response' or %resource.type = 'transaction-response' or %resource.type = 'history')) | | |

| bdl-5 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | must be a resource unless there's a request or response
: resource.exists() or request.exists() or response.exists() | | |

| bdl-7 | error | Bundle | FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
: (type = 'history') or entry.where(fullUrl.exists()).select(fullUrl&resource.meta.versionId).isDistinct() | | |

| bdl-8 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | fullUrl cannot be a version specific reference
: fullUrl.contains('/_history/').not() | | |

| bdl-9 | error | Bundle | A document must have an identifier with a system and a value
: type = 'document' implies (identifier.system.exists() and identifier.value.exists()) | | |

| bdl-10 | error | Bundle | A document must have a date
: type = 'document' implies (timestamp.hasValue()) | | |

| bdl-11 | error | Bundle | A document must have a Composition as the first resource
: type = 'document' implies entry.first().resource.is(Composition) | | |

| bdl-12 | error | Bundle | A message must have a MessageHeader as the first resource
: type = 'message' implies entry.first().resource.is(MessageHeader) | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 

 
 

 

 
This structure is derived from [Bundle](http://hl7.org/fhir/R4/bundle.html)
 

 

 
 

Summary
**

Mandatory: 0 element(1 nested mandatory element)** Must-Support: 8 elements
 Fixed: 1 element

Structures**

This structure refers to these other structures:

- [User Access Endpoint Profile (http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-endpoint)](StructureDefinition-user-access-endpoint.html)

- [User Access Brand (Organization) Profile (http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-brand)](StructureDefinition-user-access-brand.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

- The element 1 is sliced based on the value of Bundle.entry

 

 

 

 
 

 

 

 **Differential View**
 

 
This structure is derived from [Bundle](http://hl7.org/fhir/R4/bundle.html)
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Bundle](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle) | 
 | 
0..* | 
[Bundle](http://hl7.org/fhir/R4/bundle.html) | 
User Access Brands Bundle | |

| [meta](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.meta) | 
S | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [lastUpdated](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.meta.lastUpdated) | 
S | 
1..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the resource version last changed | |

| [type](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.type) | 
S | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection**Fixed Value: collection | |

| [Slices for entry](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry) | 
S | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or informationSlice: Unordered, Open by type:resource | |

| [entry:UserAccessEndpoint](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessEndpoint) | 
S | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessEndpoint.resource) | 
S | 
0..1 | 
[UserAccessEndpoint](StructureDefinition-user-access-endpoint.html) | 
User Access Endpoint | |

| [entry:UserAccessBrand](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessBrand) | 
S | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#diff_Bundle.entry:UserAccessBrand.resource) | 
S | 
0..1 | 
[UserAccessBrand](StructureDefinition-user-access-brand.html) | 
User Access Brand | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
 
 
 
 
 

 

 

 

 Key Elements View**
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Bundle](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Bundle](http://hl7.org/fhir/R4/bundle.html) | 
User Access Brands Bundle**bdl-1: total only when a search or history
bdl-2: entry.search only when a search
bdl-3: entry.request mandatory for batch/transaction/history, otherwise prohibited
bdl-4: entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
bdl-7: FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
bdl-9: A document must have an identifier with a system and a value
bdl-10: A document must have a date
bdl-11: A document must have a Composition as the first resource
bdl-12: A message must have a MessageHeader as the first resource
 | |

| [meta](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.meta) | 
SΣ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [lastUpdated](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.meta.lastUpdated) | 
SΣ | 
1..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the resource version last changed | |

| [implicitRules](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [type](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.type) | 
SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection
Binding: [BundleType](http://hl7.org/fhir/R4/valueset-bundle-type.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Indicates the purpose of a bundle - how it is intended to be used.

Fixed Value: collection | |

| [Slices for entry](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or informationSlice: Unordered, Open by type:resourcebdl-5: must be a resource unless there's a request or responsebdl-8: fullUrl cannot be a version specific referenceThis repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| entry:All Slices | 
 | 
 | 
 | 
Content/Rules for all slices | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [entry:UserAccessEndpoint](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessEndpoint) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessEndpoint.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessEndpoint.resource) | 
S | 
0..1 | 
[UserAccessEndpoint](StructureDefinition-user-access-endpoint.html) | 
User Access Endpoint | |

| [entry:UserAccessBrand](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessBrand) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessBrand.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#key_Bundle.entry:UserAccessBrand.resource) | 
S | 
0..1 | 
[UserAccessBrand](StructureDefinition-user-access-brand.html) | 
User Access Brand | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Bundle.type | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: collection
`http://hl7.org/fhir/ValueSet/bundle-type|4.0.1`**

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| bdl-1 | error | Bundle | total only when a search or history**: total.empty() or (type = 'searchset') or (type = 'history') | | |

| bdl-2 | error | Bundle | entry.search only when a search
: entry.search.empty() or (type = 'searchset') | | |

| bdl-3 | error | Bundle | entry.request mandatory for batch/transaction/history, otherwise prohibited
: entry.all(request.exists() = (%resource.type = 'batch' or %resource.type = 'transaction' or %resource.type = 'history')) | | |

| bdl-4 | error | Bundle | entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
: entry.all(response.exists() = (%resource.type = 'batch-response' or %resource.type = 'transaction-response' or %resource.type = 'history')) | | |

| bdl-5 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | must be a resource unless there's a request or response
: resource.exists() or request.exists() or response.exists() | | |

| bdl-7 | error | Bundle | FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
: (type = 'history') or entry.where(fullUrl.exists()).select(fullUrl&resource.meta.versionId).isDistinct() | | |

| bdl-8 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | fullUrl cannot be a version specific reference
: fullUrl.contains('/_history/').not() | | |

| bdl-9 | error | Bundle | A document must have an identifier with a system and a value
: type = 'document' implies (identifier.system.exists() and identifier.value.exists()) | | |

| bdl-10 | error | Bundle | A document must have a date
: type = 'document' implies (timestamp.hasValue()) | | |

| bdl-11 | error | Bundle | A document must have a Composition as the first resource
: type = 'document' implies entry.first().resource.is(Composition) | | |

| bdl-12 | error | Bundle | A message must have a MessageHeader as the first resource
: type = 'message' implies entry.first().resource.is(MessageHeader) | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 

 Snapshot View**
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Bundle](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Bundle](http://hl7.org/fhir/R4/bundle.html) | 
User Access Brands Bundle**bdl-1: total only when a search or history
bdl-2: entry.search only when a search
bdl-3: entry.request mandatory for batch/transaction/history, otherwise prohibited
bdl-4: entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
bdl-7: FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
bdl-9: A document must have an identifier with a system and a value
bdl-10: A document must have a date
bdl-11: A document must have a Composition as the first resource
bdl-12: A message must have a MessageHeader as the first resource
 | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.id) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Logical id of this artifact | |

| [meta](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta) | 
SΣ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
Slice: Unordered, Open by value:url
 | |

| [versionId](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.versionId) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Version specific identifier | |

| [lastUpdated](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.lastUpdated) | 
SΣ | 
1..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the resource version last changed | |

| [source](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.source) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Identifies where the resource comes from | |

| [profile](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.profile) | 
Σ | 
0..* | 
[canonical](http://hl7.org/fhir/R4/references.html)([StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)) | 
Profiles this resource claims to conform to
 | |

| [security](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.security) | 
Σ | 
0..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Security Labels applied to this resource
Binding: [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)): Security Labels from the Healthcare Privacy and Security Classification System.

 | |

| [tag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.meta.tag) | 
Σ | 
0..* | 
[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) | 
Tags applied to this resource
Binding: [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example)): Codes that represent various types of tags, commonly workflow-related; e.g. "Needs review by Dr. Jones".

 | |

| [implicitRules](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [language](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.language) | 
 | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Language of the resource content
Binding: [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) ([preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)): A human language.

| Additional Bindings** | Purpose | |

| [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html) | 
[Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html) | |

|

| [identifier](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.identifier) | 
Σ | 
0..1 | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Persistent identifier for the bundle | |

| [type](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.type) | 
SΣ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection**Binding: [BundleType](http://hl7.org/fhir/R4/valueset-bundle-type.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Indicates the purpose of a bundle - how it is intended to be used.

Fixed Value: collection | |

| [timestamp](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.timestamp) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
When the bundle was assembled | |

| [total](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.total) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[unsignedInt](http://hl7.org/fhir/R4/datatypes.html#unsignedInt) | 
If search, the total number of matches | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link) | 
Σ | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Links related to this Bundle
 | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [relation](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.relation) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.link.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Reference details for the link | |

| [Slices for entry](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or informationSlice: Unordered, Open by type:resourcebdl-5: must be a resource unless there's a request or responsebdl-8: fullUrl cannot be a version specific referenceThis repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| entry:All Slices | 
 | 
 | 
 | 
Content/Rules for all slices | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.link) | 
Σ | 
0..* | 
See [link (Bundle)](http://hl7.org/fhir/R4/bundle.html#Bundle.link) | 
Links related to this entry
 | |

| [fullUrl](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.fullUrl) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URI for resource (Absolute URL server address or URI for UUID/OID) | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.resource) | 
Σ | 
0..1 | 
Resource | 
A resource in the bundle | |

| [search](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Search related information | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [mode](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.mode) | 
Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
match | include | outcome - why this is in the result set
Binding: [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.

 | |

| [score](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.search.score) | 
Σ | 
0..1 | 
[decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) | 
Search ranking (between 0 and 1) | |

| [request](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Additional execution information (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [method](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.method) | 
Σ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
GET | HEAD | POST | PUT | DELETE | PATCH
Binding: [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.

 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URL for HTTP equivalent of this entry | |

| [ifNoneMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifNoneMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing cache currency | |

| [ifModifiedSince](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifModifiedSince) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
For managing cache currency | |

| [ifMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing update contention | |

| [ifNoneExist](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.request.ifNoneExist) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For conditional creates | |

| [response](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Results of execution (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [status](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.status) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Status response code (text optional) | |

| [location](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.location) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
The location (if the operation returns a location) | |

| [etag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.etag) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
The Etag for the resource (if relevant) | |

| [lastModified](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.lastModified) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
Server's date time modified | |

| [outcome](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry.response.outcome) | 
Σ | 
0..1 | 
Resource | 
OperationOutcome with hints and warnings (for batch/transaction) | |

| [entry:UserAccessEndpoint](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.link) | 
Σ | 
0..* | 
See [link (Bundle)](http://hl7.org/fhir/R4/bundle.html#Bundle.link) | 
Links related to this entry
 | |

| [fullUrl](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.fullUrl) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URI for resource (Absolute URL server address or URI for UUID/OID) | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.resource) | 
S | 
0..1 | 
[UserAccessEndpoint](StructureDefinition-user-access-endpoint.html) | 
User Access Endpoint | |

| [search](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Search related information | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [mode](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.mode) | 
Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
match | include | outcome - why this is in the result set
Binding: [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.

 | |

| [score](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.search.score) | 
Σ | 
0..1 | 
[decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) | 
Search ranking (between 0 and 1) | |

| [request](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Additional execution information (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [method](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.method) | 
Σ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
GET | HEAD | POST | PUT | DELETE | PATCH
Binding: [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.

 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URL for HTTP equivalent of this entry | |

| [ifNoneMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifNoneMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing cache currency | |

| [ifModifiedSince](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifModifiedSince) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
For managing cache currency | |

| [ifMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing update contention | |

| [ifNoneExist](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.request.ifNoneExist) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For conditional creates | |

| [response](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Results of execution (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [status](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.status) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Status response code (text optional) | |

| [location](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.location) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
The location (if the operation returns a location) | |

| [etag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.etag) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
The Etag for the resource (if relevant) | |

| [lastModified](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.lastModified) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
Server's date time modified | |

| [outcome](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessEndpoint.response.outcome) | 
Σ | 
0..1 | 
Resource | 
OperationOutcome with hints and warnings (for batch/transaction) | |

| [entry:UserAccessBrand](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Entry in the bundle - will have a resource or information
bdl-5: must be a resource unless there's a request or response
bdl-8: fullUrl cannot be a version specific reference
This repeating element order: For bundles of type 'document' and 'message', the first resource is special (must be Composition or MessageHeader respectively). For all bundles, the meaning of the order of entries depends on the bundle type | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [link](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.link) | 
Σ | 
0..* | 
See [link (Bundle)](http://hl7.org/fhir/R4/bundle.html#Bundle.link) | 
Links related to this entry
 | |

| [fullUrl](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.fullUrl) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URI for resource (Absolute URL server address or URI for UUID/OID) | |

| [resource](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.resource) | 
S | 
0..1 | 
[UserAccessBrand](StructureDefinition-user-access-brand.html) | 
User Access Brand | |

| [search](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Search related information | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [mode](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.mode) | 
Σ | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
match | include | outcome - why this is in the result set
Binding: [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.

 | |

| [score](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.search.score) | 
Σ | 
0..1 | 
[decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) | 
Search ranking (between 0 and 1) | |

| [request](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Additional execution information (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [method](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.method) | 
Σ | 
1..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
GET | HEAD | POST | PUT | DELETE | PATCH
Binding: [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)): HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.

 | |

| [url](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.url) | 
Σ | 
1..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
URL for HTTP equivalent of this entry | |

| [ifNoneMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifNoneMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing cache currency | |

| [ifModifiedSince](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifModifiedSince) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
For managing cache currency | |

| [ifMatch](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifMatch) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For managing update contention | |

| [ifNoneExist](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.request.ifNoneExist) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
For conditional creates | |

| [response](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response) | 
Σ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Results of execution (transaction/batch/history) | |

| [id](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [status](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.status) | 
Σ | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Status response code (text optional) | |

| [location](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.location) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
The location (if the operation returns a location) | |

| [etag](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.etag) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
The Etag for the resource (if relevant) | |

| [lastModified](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.lastModified) | 
Σ | 
0..1 | 
[instant](http://hl7.org/fhir/R4/datatypes.html#instant) | 
Server's date time modified | |

| [outcome](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.entry:UserAccessBrand.response.outcome) | 
Σ | 
0..1 | 
Resource | 
OperationOutcome with hints and warnings (for batch/transaction) | |

| [signature](StructureDefinition-user-access-brands-bundle-definitions.html#Bundle.signature) | 
Σ | 
0..1 | 
[Signature](http://hl7.org/fhir/R4/datatypes.html#Signature) | 
Digital Signature | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet / Code** | **URI** | |

| Bundle.meta.security | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html)
`http://hl7.org/fhir/ValueSet/security-labels`**

from the FHIR Standard
 | |

| Bundle.meta.tag | [example](http://hl7.org/fhir/R4/terminologies.html#example) | [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html)
`http://hl7.org/fhir/ValueSet/common-tags`

from the FHIR Standard
 | |

| Bundle.language | [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred) | [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html)

 | 
 
 Additional Bindings**
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

| Bundle.type | [required](http://hl7.org/fhir/R4/terminologies.html#required) | Fixed Value: collection
`http://hl7.org/fhir/ValueSet/bundle-type|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry.search.mode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html)
`http://hl7.org/fhir/ValueSet/search-entry-mode|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry.request.method | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html)
`http://hl7.org/fhir/ValueSet/http-verb|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessEndpoint.search.mode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html)
`http://hl7.org/fhir/ValueSet/search-entry-mode|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessEndpoint.request.method | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html)
`http://hl7.org/fhir/ValueSet/http-verb|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessBrand.search.mode | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [SearchEntryMode](http://hl7.org/fhir/R4/valueset-search-entry-mode.html)
`http://hl7.org/fhir/ValueSet/search-entry-mode|4.0.1`

from the FHIR Standard
 | |

| Bundle.entry:UserAccessBrand.request.method | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [HTTPVerb](http://hl7.org/fhir/R4/valueset-http-verb.html)
`http://hl7.org/fhir/ValueSet/http-verb|4.0.1`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| bdl-1 | error | Bundle | total only when a search or history**: total.empty() or (type = 'searchset') or (type = 'history') | | |

| bdl-2 | error | Bundle | entry.search only when a search
: entry.search.empty() or (type = 'searchset') | | |

| bdl-3 | error | Bundle | entry.request mandatory for batch/transaction/history, otherwise prohibited
: entry.all(request.exists() = (%resource.type = 'batch' or %resource.type = 'transaction' or %resource.type = 'history')) | | |

| bdl-4 | error | Bundle | entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
: entry.all(response.exists() = (%resource.type = 'batch-response' or %resource.type = 'transaction-response' or %resource.type = 'history')) | | |

| bdl-5 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | must be a resource unless there's a request or response
: resource.exists() or request.exists() or response.exists() | | |

| bdl-7 | error | Bundle | FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
: (type = 'history') or entry.where(fullUrl.exists()).select(fullUrl&resource.meta.versionId).isDistinct() | | |

| bdl-8 | error | Bundle.entry, Bundle.entry:UserAccessEndpoint, Bundle.entry:UserAccessBrand | fullUrl cannot be a version specific reference
: fullUrl.contains('/_history/').not() | | |

| bdl-9 | error | Bundle | A document must have an identifier with a system and a value
: type = 'document' implies (identifier.system.exists() and identifier.value.exists()) | | |

| bdl-10 | error | Bundle | A document must have a date
: type = 'document' implies (timestamp.hasValue()) | | |

| bdl-11 | error | Bundle | A document must have a Composition as the first resource
: type = 'document' implies entry.first().resource.is(Composition) | | |

| bdl-12 | error | Bundle | A message must have a MessageHeader as the first resource
: type = 'message' implies entry.first().resource.is(MessageHeader) | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

 
 

 

 

 

 

 

 
This structure is derived from [Bundle](http://hl7.org/fhir/R4/bundle.html)
 

 

 

Summary
**

Mandatory: 0 element(1 nested mandatory element)** Must-Support: 8 elements
 Fixed: 1 element

Structures**

This structure refers to these other structures:

- [User Access Endpoint Profile (http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-endpoint)](StructureDefinition-user-access-endpoint.html)

- [User Access Brand (Organization) Profile (http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-brand)](StructureDefinition-user-access-brand.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

- The element 1 is sliced based on the value of Bundle.entry

 

 

 

 

 
 

 
Other representations of profile: [CSV](StructureDefinition-user-access-brands-bundle.csv), [Excel](StructureDefinition-user-access-brands-bundle.xlsx), [Schematron](StructureDefinition-user-access-brands-bundle.sch)