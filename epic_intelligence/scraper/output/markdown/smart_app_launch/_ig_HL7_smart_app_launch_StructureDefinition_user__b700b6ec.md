# User Access Brand (Organization) Profile - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/StructureDefinition-user-access-brand.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 

 
 
## Resource Profile:

 User Access Brand (Organization) Profile

 

 

 | 
 *Official URL*: http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-brand**
 | 
 *Version*:
 2.2.0
 | 
 |

 | 

 
 
 Active
 
 as of 2023-03-05
 
 
 | 

 *Computable Name*: UserAccessBrand | 
 |

 

Profile on Organization to convey a User Access Brand.

For background and context, see **[User Access Brands Overview](brands.html#brand-profile-organization)**.

In addition to the core data elements on Organization, two key extensions are used in this profile:

 - [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/StructureDefinition/organization-brand) conveys the organization’s logo(s) and other top-level branding details. See definitions for details.

 - [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/StructureDefinition/organization-portal) conveys the details of a user portal and its associated FHIR endpoints. See definitions for details.

Notes:

 - 
 
`0..1 MS` `partOf` Conveys that an affiliate Brand response for providing this Brand’s user access. The hierarchy of “access provided by” links SHALL NOT exceed a depth of two (i.e., a Brand either includes portal details or links directly to a Brand that provides them).

 

 - 
 
`0..* MS` `identifier` Conveys identifiers that apps can use to link this Brand across publishers or with external data sets. EHRs SHALL support customer-supplied identifiers (`system` and `value`).

 

 It is RECOMMENDED that each Brand include an identifier where `system` is `urn:ietf:rfc: 3986` (meaning the identifier is a URL) and `value` is the HTTPS URL for the Brand’s primary web presence, omitting any “www.” prefix from the domain and omitting any path component. For example, since the main web presence of Boston Children’s Hospital is https://www.childrenshospital.org/, a recommended identifier would be: `{"system": "urn:ietf:rfc:3986","value": "https://childrenshospital.org"}`

 

 

Usage:**

 - Use this Resource Profile: [User Access Brands Bundle Profile](StructureDefinition-user-access-brands-bundle.html)

 
 
 
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
 

 

 
 

 

 
This structure is derived from [Organization](http://hl7.org/fhir/R4/organization.html)
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Organization](StructureDefinition-user-access-brand-definitions.html#diff_Organization) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Organization](http://hl7.org/fhir/R4/organization.html) | 
User Access Brand**uab-1: Portal endpoints must also appear at Organization.endpoint | |

| [Slices for extension](StructureDefinition-user-access-brand-definitions.html#diff_Organization.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url | |

| [brand](StructureDefinition-user-access-brand-definitions.html#diff_Organization.extension:brand) | 
S | 
0..* | 
(Complex) | 
Brand Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)
 | |

| [portal](StructureDefinition-user-access-brand-definitions.html#diff_Organization.extension:portal) | 
S | 
0..* | 
(Complex) | 
Portal Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)
 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#diff_Organization.identifier) | 
S | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Unique identifier for the brand | |

| [Slices for type](StructureDefinition-user-access-brand-definitions.html#diff_Organization.type) | 
S | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Kind of organizationSlice: Unordered, Open by value:$this | |

| [type:pab](StructureDefinition-user-access-brand-definitions.html#diff_Organization.type:pab) | 
S | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Categories of user access offered
Binding: [User Access Category Value Set](ValueSet-user-access-category.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)) | |

| [name](StructureDefinition-user-access-brand-definitions.html#diff_Organization.name) | 
S | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Primary brand name to display on a card | |

| [alias](StructureDefinition-user-access-brand-definitions.html#diff_Organization.alias) | 
S | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Aliases (e.g., former names like "Partners Healthcare") for filtering/search | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#diff_Organization.telecom) | 
S | 
1..1 | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
The primary public website for the Brand. | |

| [address](StructureDefinition-user-access-brand-definitions.html#diff_Organization.address) | 
S | 
0..* | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Locations (e.g., zip codes and/or street addresses) associated with the Brand. | |

| [partOf](StructureDefinition-user-access-brand-definitions.html#diff_Organization.partOf) | 
S | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Affiliated "parent brand", if this Brand is part of a larger health system | |

| [endpoint](StructureDefinition-user-access-brand-definitions.html#diff_Organization.endpoint) | 
S | 
0..* | 
[Reference](http://hl7.org/fhir/R4/references.html)([User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html))[ {](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[b](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[}](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html) | 
Endpoint associated with this brand | |

| [reference](StructureDefinition-user-access-brand-definitions.html#diff_Organization.endpoint.reference) | 
S | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Relative URL to an Endpoint within the User Access Brands Bundle | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
 
#### Terminology Bindings (Differential)

| Path** | **Conformance** | **ValueSet** | **URI** | |

| Organization.type:pab | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UserAccessCategoryValueSet](ValueSet-user-access-category.html)
`http://hl7.org/fhir/smart-app-launch/ValueSet/user-access-category`**

from this IG
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| uab-1 | error | Organization | Portal endpoints must also appear at Organization.endpoint**: Organization.extension('http://hl7.org/fhir/StructureDefinition/organization-portal').extension('portalEndpoint').value.ofType(Reference).reference.subsetOf(%resource.endpoint.reference) | | |

 
 

 

 

 
 

 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Organization](StructureDefinition-user-access-brand-definitions.html#key_Organization) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Organization](http://hl7.org/fhir/R4/organization.html) | 
User Access Brand
org-1: The organization SHALL at least have a name or an identifier, and possibly more than one
uab-1: Portal endpoints must also appear at Organization.endpoint
 | |

| [implicitRules](StructureDefinition-user-access-brand-definitions.html#key_Organization.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [Slices for extension](StructureDefinition-user-access-brand-definitions.html#key_Organization.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [brand](StructureDefinition-user-access-brand-definitions.html#key_Organization.extension:brand) | 
S | 
0..* | 
(Complex) | 
Brand Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)
 | |

| [portal](StructureDefinition-user-access-brand-definitions.html#key_Organization.extension:portal) | 
S | 
0..* | 
(Complex) | 
Portal Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)
 | |

| [modifierExtension](StructureDefinition-user-access-brand-definitions.html#key_Organization.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#key_Organization.identifier) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Unique identifier for the brand
 | |

| [active](StructureDefinition-user-access-brand-definitions.html#key_Organization.active) | 
?!Σ | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
Whether the organization's record is still in active use | |

| [Slices for type](StructureDefinition-user-access-brand-definitions.html#key_Organization.type) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Kind of organizationSlice: Unordered, Open by value:$thisBinding: [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example)): Used to categorize the organization. | |

| [type:pab](StructureDefinition-user-access-brand-definitions.html#key_Organization.type:pab) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Categories of user access offered
Binding: [User Access Category Value Set](ValueSet-user-access-category.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [name](StructureDefinition-user-access-brand-definitions.html#key_Organization.name) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Primary brand name to display on a card | |

| [alias](StructureDefinition-user-access-brand-definitions.html#key_Organization.alias) | 
S | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Aliases (e.g., former names like "Partners Healthcare") for filtering/search
 | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#key_Organization.telecom) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
The primary public website for the Brand.
org-3: The telecom of an organization can never be of use 'home'
 | |

| [address](StructureDefinition-user-access-brand-definitions.html#key_Organization.address) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Locations (e.g., zip codes and/or street addresses) associated with the Brand.
org-2: An address of an organization can never be of use 'home'
 | |

| [partOf](StructureDefinition-user-access-brand-definitions.html#key_Organization.partOf) | 
SΣ | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Affiliated "parent brand", if this Brand is part of a larger health system | |

| [endpoint](StructureDefinition-user-access-brand-definitions.html#key_Organization.endpoint) | 
S | 
0..* | 
[Reference](http://hl7.org/fhir/R4/references.html)([User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html))[ {](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[b](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[}](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html) | 
Endpoint associated with this brand
 | |

| [reference](StructureDefinition-user-access-brand-definitions.html#key_Organization.endpoint.reference) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Relative URL to an Endpoint within the User Access Brands Bundle | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet** | **URI** | |

| Organization.type | [example](http://hl7.org/fhir/R4/terminologies.html#example) | [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html)
`http://hl7.org/fhir/ValueSet/organization-type`**

from the FHIR Standard
 | |

| Organization.type:pab | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UserAccessCategoryValueSet](ValueSet-user-access-category.html)
`http://hl7.org/fhir/smart-app-launch/ValueSet/user-access-category`

from this IG
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Organization | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Organization | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Organization | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

| org-1 | error | Organization | The organization SHALL at least have a name or an identifier, and possibly more than one
: (identifier.count() + name.count()) > 0 | | |

| org-2 | error | Organization.address | An address of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| org-3 | error | Organization.telecom | The telecom of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| uab-1 | error | Organization | Portal endpoints must also appear at Organization.endpoint
: Organization.extension('http://hl7.org/fhir/StructureDefinition/organization-portal').extension('portalEndpoint').value.ofType(Reference).reference.subsetOf(%resource.endpoint.reference) | | |

 
 

 

 

 
 

 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Organization](StructureDefinition-user-access-brand-definitions.html#Organization) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Organization](http://hl7.org/fhir/R4/organization.html) | 
User Access Brand
org-1: The organization SHALL at least have a name or an identifier, and possibly more than one
uab-1: Portal endpoints must also appear at Organization.endpoint
 | |

| [id](StructureDefinition-user-access-brand-definitions.html#Organization.id) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Logical id of this artifact | |

| [meta](StructureDefinition-user-access-brand-definitions.html#Organization.meta) | 
Σ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [implicitRules](StructureDefinition-user-access-brand-definitions.html#Organization.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [language](StructureDefinition-user-access-brand-definitions.html#Organization.language) | 
 | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Language of the resource content
Binding: [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) ([preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)): A human language.

| Additional Bindings** | Purpose | |

| [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html) | 
[Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html) | |

|

| [text](StructureDefinition-user-access-brand-definitions.html#Organization.text) | 
 | 
0..1 | 
[Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) | 
Text summary of the resource, for human interpretation | |

| [contained](StructureDefinition-user-access-brand-definitions.html#Organization.contained) | 
 | 
0..* | 
Resource | 
Contained, inline Resources** | |

| [Slices for extension](StructureDefinition-user-access-brand-definitions.html#Organization.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [brand](StructureDefinition-user-access-brand-definitions.html#Organization.extension:brand) | 
S | 
0..* | 
(Complex) | 
Brand Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)
 | |

| [portal](StructureDefinition-user-access-brand-definitions.html#Organization.extension:portal) | 
S | 
0..* | 
(Complex) | 
Portal Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)
 | |

| [modifierExtension](StructureDefinition-user-access-brand-definitions.html#Organization.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#Organization.identifier) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Unique identifier for the brand
 | |

| [active](StructureDefinition-user-access-brand-definitions.html#Organization.active) | 
?!Σ | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
Whether the organization's record is still in active use | |

| [Slices for type](StructureDefinition-user-access-brand-definitions.html#Organization.type) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Kind of organizationSlice: Unordered, Open by value:$thisBinding: [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example)): Used to categorize the organization. | |

| [type:pab](StructureDefinition-user-access-brand-definitions.html#Organization.type:pab) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Categories of user access offered
Binding: [User Access Category Value Set](ValueSet-user-access-category.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [name](StructureDefinition-user-access-brand-definitions.html#Organization.name) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Primary brand name to display on a card | |

| [alias](StructureDefinition-user-access-brand-definitions.html#Organization.alias) | 
S | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Aliases (e.g., former names like "Partners Healthcare") for filtering/search
 | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#Organization.telecom) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
The primary public website for the Brand.
org-3: The telecom of an organization can never be of use 'home'
 | |

| [address](StructureDefinition-user-access-brand-definitions.html#Organization.address) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Locations (e.g., zip codes and/or street addresses) associated with the Brand.
org-2: An address of an organization can never be of use 'home'
 | |

| [partOf](StructureDefinition-user-access-brand-definitions.html#Organization.partOf) | 
SΣ | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Affiliated "parent brand", if this Brand is part of a larger health system | |

| [contact](StructureDefinition-user-access-brand-definitions.html#Organization.contact) | 
 | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Contact for the organization for a certain purpose
 | |

| [id](StructureDefinition-user-access-brand-definitions.html#Organization.contact.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brand-definitions.html#Organization.contact.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brand-definitions.html#Organization.contact.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [purpose](StructureDefinition-user-access-brand-definitions.html#Organization.contact.purpose) | 
 | 
0..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of contact
Binding: [ContactEntityType](http://hl7.org/fhir/R4/valueset-contactentity-type.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)): The purpose for which you would contact a contact party.

 | |

| [name](StructureDefinition-user-access-brand-definitions.html#Organization.contact.name) | 
 | 
0..1 | 
[HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName) | 
A name associated with the contact | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#Organization.contact.telecom) | 
 | 
0..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact details (telephone, email, etc.) for a contact
 | |

| [address](StructureDefinition-user-access-brand-definitions.html#Organization.contact.address) | 
 | 
0..1 | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Visiting or postal addresses for the contact | |

| [endpoint](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint) | 
S | 
0..* | 
[Reference](http://hl7.org/fhir/R4/references.html)([User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html))[ {](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[b](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[}](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html) | 
Endpoint associated with this brand
 | |

| [id](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
Slice: Unordered, Open by value:url
 | |

| [reference](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.reference) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Relative URL to an Endpoint within the User Access Brands Bundle | |

| [type](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.type) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Type the reference refers to (e.g. "Patient")
Binding: [ResourceType](http://hl7.org/fhir/R4/valueset-resource-types.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)): Aa resource (or, for logical models, the URI of the logical model).

 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.identifier) | 
Σ | 
0..1 | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Logical reference, when literal reference is not known | |

| [display](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.display) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Text alternative for the resource | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet** | **URI** | |

| Organization.language | [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred) | [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html)

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

| Organization.type | [example](http://hl7.org/fhir/R4/terminologies.html#example) | [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html)
`http://hl7.org/fhir/ValueSet/organization-type`

from the FHIR Standard
 | |

| Organization.type:pab | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UserAccessCategoryValueSet](ValueSet-user-access-category.html)
`http://hl7.org/fhir/smart-app-launch/ValueSet/user-access-category`

from this IG
 | |

| Organization.contact.purpose | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [ContactEntityType](http://hl7.org/fhir/R4/valueset-contactentity-type.html)
`http://hl7.org/fhir/ValueSet/contactentity-type`

from the FHIR Standard
 | |

| Organization.endpoint.type | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [ResourceType](http://hl7.org/fhir/R4/valueset-resource-types.html)
`http://hl7.org/fhir/ValueSet/resource-types`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Organization | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Organization | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Organization | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

| org-1 | error | Organization | The organization SHALL at least have a name or an identifier, and possibly more than one
: (identifier.count() + name.count()) > 0 | | |

| org-2 | error | Organization.address | An address of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| org-3 | error | Organization.telecom | The telecom of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| uab-1 | error | Organization | Portal endpoints must also appear at Organization.endpoint
: Organization.extension('http://hl7.org/fhir/StructureDefinition/organization-portal').extension('portalEndpoint').value.ofType(Reference).reference.subsetOf(%resource.endpoint.reference) | | |

 
 

 

 

 

 
 

 

 
This structure is derived from [Organization](http://hl7.org/fhir/R4/organization.html)
 

 

 
 

Summary
**

Mandatory: 2 elements** Must-Support: 12 elements

Structures**

This structure refers to these other structures:

- [User Access Endpoint Profile (http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-endpoint)](StructureDefinition-user-access-endpoint.html)

**Extensions**

This structure refers to these extensions:

- [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)

- [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

- The element 1 is sliced based on the value of Organization.type

 

 

 

 
 

 

 

 **Differential View**
 

 
This structure is derived from [Organization](http://hl7.org/fhir/R4/organization.html)
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Organization](StructureDefinition-user-access-brand-definitions.html#diff_Organization) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Organization](http://hl7.org/fhir/R4/organization.html) | 
User Access Brand**uab-1: Portal endpoints must also appear at Organization.endpoint | |

| [Slices for extension](StructureDefinition-user-access-brand-definitions.html#diff_Organization.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url | |

| [brand](StructureDefinition-user-access-brand-definitions.html#diff_Organization.extension:brand) | 
S | 
0..* | 
(Complex) | 
Brand Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)
 | |

| [portal](StructureDefinition-user-access-brand-definitions.html#diff_Organization.extension:portal) | 
S | 
0..* | 
(Complex) | 
Portal Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)
 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#diff_Organization.identifier) | 
S | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Unique identifier for the brand | |

| [Slices for type](StructureDefinition-user-access-brand-definitions.html#diff_Organization.type) | 
S | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Kind of organizationSlice: Unordered, Open by value:$this | |

| [type:pab](StructureDefinition-user-access-brand-definitions.html#diff_Organization.type:pab) | 
S | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Categories of user access offered
Binding: [User Access Category Value Set](ValueSet-user-access-category.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required)) | |

| [name](StructureDefinition-user-access-brand-definitions.html#diff_Organization.name) | 
S | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Primary brand name to display on a card | |

| [alias](StructureDefinition-user-access-brand-definitions.html#diff_Organization.alias) | 
S | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Aliases (e.g., former names like "Partners Healthcare") for filtering/search | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#diff_Organization.telecom) | 
S | 
1..1 | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
The primary public website for the Brand. | |

| [address](StructureDefinition-user-access-brand-definitions.html#diff_Organization.address) | 
S | 
0..* | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Locations (e.g., zip codes and/or street addresses) associated with the Brand. | |

| [partOf](StructureDefinition-user-access-brand-definitions.html#diff_Organization.partOf) | 
S | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Affiliated "parent brand", if this Brand is part of a larger health system | |

| [endpoint](StructureDefinition-user-access-brand-definitions.html#diff_Organization.endpoint) | 
S | 
0..* | 
[Reference](http://hl7.org/fhir/R4/references.html)([User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html))[ {](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[b](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[}](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html) | 
Endpoint associated with this brand | |

| [reference](StructureDefinition-user-access-brand-definitions.html#diff_Organization.endpoint.reference) | 
S | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Relative URL to an Endpoint within the User Access Brands Bundle | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings (Differential)

| Path** | **Conformance** | **ValueSet** | **URI** | |

| Organization.type:pab | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UserAccessCategoryValueSet](ValueSet-user-access-category.html)
`http://hl7.org/fhir/smart-app-launch/ValueSet/user-access-category`**

from this IG
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| uab-1 | error | Organization | Portal endpoints must also appear at Organization.endpoint**: Organization.extension('http://hl7.org/fhir/StructureDefinition/organization-portal').extension('portalEndpoint').value.ofType(Reference).reference.subsetOf(%resource.endpoint.reference) | | |

 
 

 

 

 

 Key Elements View**
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Organization](StructureDefinition-user-access-brand-definitions.html#key_Organization) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Organization](http://hl7.org/fhir/R4/organization.html) | 
User Access Brand**org-1: The organization SHALL at least have a name or an identifier, and possibly more than one
uab-1: Portal endpoints must also appear at Organization.endpoint
 | |

| [implicitRules](StructureDefinition-user-access-brand-definitions.html#key_Organization.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [Slices for extension](StructureDefinition-user-access-brand-definitions.html#key_Organization.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [brand](StructureDefinition-user-access-brand-definitions.html#key_Organization.extension:brand) | 
S | 
0..* | 
(Complex) | 
Brand Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)
 | |

| [portal](StructureDefinition-user-access-brand-definitions.html#key_Organization.extension:portal) | 
S | 
0..* | 
(Complex) | 
Portal Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)
 | |

| [modifierExtension](StructureDefinition-user-access-brand-definitions.html#key_Organization.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#key_Organization.identifier) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Unique identifier for the brand
 | |

| [active](StructureDefinition-user-access-brand-definitions.html#key_Organization.active) | 
?!Σ | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
Whether the organization's record is still in active use | |

| [Slices for type](StructureDefinition-user-access-brand-definitions.html#key_Organization.type) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Kind of organizationSlice: Unordered, Open by value:$thisBinding: [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example)): Used to categorize the organization. | |

| [type:pab](StructureDefinition-user-access-brand-definitions.html#key_Organization.type:pab) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Categories of user access offered
Binding: [User Access Category Value Set](ValueSet-user-access-category.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [name](StructureDefinition-user-access-brand-definitions.html#key_Organization.name) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Primary brand name to display on a card | |

| [alias](StructureDefinition-user-access-brand-definitions.html#key_Organization.alias) | 
S | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Aliases (e.g., former names like "Partners Healthcare") for filtering/search
 | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#key_Organization.telecom) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
The primary public website for the Brand.
org-3: The telecom of an organization can never be of use 'home'
 | |

| [address](StructureDefinition-user-access-brand-definitions.html#key_Organization.address) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Locations (e.g., zip codes and/or street addresses) associated with the Brand.
org-2: An address of an organization can never be of use 'home'
 | |

| [partOf](StructureDefinition-user-access-brand-definitions.html#key_Organization.partOf) | 
SΣ | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Affiliated "parent brand", if this Brand is part of a larger health system | |

| [endpoint](StructureDefinition-user-access-brand-definitions.html#key_Organization.endpoint) | 
S | 
0..* | 
[Reference](http://hl7.org/fhir/R4/references.html)([User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html))[ {](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[b](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[}](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html) | 
Endpoint associated with this brand
 | |

| [reference](StructureDefinition-user-access-brand-definitions.html#key_Organization.endpoint.reference) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Relative URL to an Endpoint within the User Access Brands Bundle | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet** | **URI** | |

| Organization.type | [example](http://hl7.org/fhir/R4/terminologies.html#example) | [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html)
`http://hl7.org/fhir/ValueSet/organization-type`**

from the FHIR Standard
 | |

| Organization.type:pab | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UserAccessCategoryValueSet](ValueSet-user-access-category.html)
`http://hl7.org/fhir/smart-app-launch/ValueSet/user-access-category`

from this IG
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Organization | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Organization | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Organization | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

| org-1 | error | Organization | The organization SHALL at least have a name or an identifier, and possibly more than one
: (identifier.count() + name.count()) > 0 | | |

| org-2 | error | Organization.address | An address of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| org-3 | error | Organization.telecom | The telecom of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| uab-1 | error | Organization | Portal endpoints must also appear at Organization.endpoint
: Organization.extension('http://hl7.org/fhir/StructureDefinition/organization-portal').extension('portalEndpoint').value.ofType(Reference).reference.subsetOf(%resource.endpoint.reference) | | |

 
 

 

 

 

 Snapshot View**
 

 

 
| [Name](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Flags](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Card.](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Type](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | [Description & Constraints](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views)[](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

| [Organization](StructureDefinition-user-access-brand-definitions.html#Organization) | 
[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Organization](http://hl7.org/fhir/R4/organization.html) | 
User Access Brand**org-1: The organization SHALL at least have a name or an identifier, and possibly more than one
uab-1: Portal endpoints must also appear at Organization.endpoint
 | |

| [id](StructureDefinition-user-access-brand-definitions.html#Organization.id) | 
Σ | 
0..1 | 
[id](http://hl7.org/fhir/R4/datatypes.html#id) | 
Logical id of this artifact | |

| [meta](StructureDefinition-user-access-brand-definitions.html#Organization.meta) | 
Σ | 
0..1 | 
[Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) | 
Metadata about the resource | |

| [implicitRules](StructureDefinition-user-access-brand-definitions.html#Organization.implicitRules) | 
?!Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
A set of rules under which this content was created | |

| [language](StructureDefinition-user-access-brand-definitions.html#Organization.language) | 
 | 
0..1 | 
[code](http://hl7.org/fhir/R4/datatypes.html#code) | 
Language of the resource content
Binding: [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) ([preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)): A human language.

| Additional Bindings** | Purpose | |

| [AllLanguages](http://hl7.org/fhir/R5/valueset-all-languages.html) | 
[Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html) | |

|

| [text](StructureDefinition-user-access-brand-definitions.html#Organization.text) | 
 | 
0..1 | 
[Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) | 
Text summary of the resource, for human interpretation | |

| [contained](StructureDefinition-user-access-brand-definitions.html#Organization.contained) | 
 | 
0..* | 
Resource | 
Contained, inline Resources** | |

| [Slices for extension](StructureDefinition-user-access-brand-definitions.html#Organization.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extension
Slice: Unordered, Open by value:url
 | |

| [brand](StructureDefinition-user-access-brand-definitions.html#Organization.extension:brand) | 
S | 
0..* | 
(Complex) | 
Brand Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)
 | |

| [portal](StructureDefinition-user-access-brand-definitions.html#Organization.extension:portal) | 
S | 
0..* | 
(Complex) | 
Portal Details
URL: [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)
 | |

| [modifierExtension](StructureDefinition-user-access-brand-definitions.html#Organization.modifierExtension) | 
?! | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored
 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#Organization.identifier) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Unique identifier for the brand
 | |

| [active](StructureDefinition-user-access-brand-definitions.html#Organization.active) | 
?!Σ | 
0..1 | 
[boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) | 
Whether the organization's record is still in active use | |

| [Slices for type](StructureDefinition-user-access-brand-definitions.html#Organization.type) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Kind of organizationSlice: Unordered, Open by value:$thisBinding: [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html) ([example](http://hl7.org/fhir/R4/terminologies.html#example)): Used to categorize the organization. | |

| [type:pab](StructureDefinition-user-access-brand-definitions.html#Organization.type:pab) | 
SΣ | 
0..* | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
Categories of user access offered
Binding: [User Access Category Value Set](ValueSet-user-access-category.html) ([required](http://hl7.org/fhir/R4/terminologies.html#required))
 | |

| [name](StructureDefinition-user-access-brand-definitions.html#Organization.name) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Primary brand name to display on a card | |

| [alias](StructureDefinition-user-access-brand-definitions.html#Organization.alias) | 
S | 
0..* | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Aliases (e.g., former names like "Partners Healthcare") for filtering/search
 | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#Organization.telecom) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
1..1 | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
The primary public website for the Brand.
org-3: The telecom of an organization can never be of use 'home'
 | |

| [address](StructureDefinition-user-access-brand-definitions.html#Organization.address) | 
S[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..* | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Locations (e.g., zip codes and/or street addresses) associated with the Brand.
org-2: An address of an organization can never be of use 'home'
 | |

| [partOf](StructureDefinition-user-access-brand-definitions.html#Organization.partOf) | 
SΣ | 
0..1 | 
[Reference](http://hl7.org/fhir/R4/references.html)([Organization](http://hl7.org/fhir/R4/organization.html)) | 
Affiliated "parent brand", if this Brand is part of a larger health system | |

| [contact](StructureDefinition-user-access-brand-definitions.html#Organization.contact) | 
 | 
0..* | 
[BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) | 
Contact for the organization for a certain purpose
 | |

| [id](StructureDefinition-user-access-brand-definitions.html#Organization.contact.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brand-definitions.html#Organization.contact.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
 | |

| [modifierExtension](StructureDefinition-user-access-brand-definitions.html#Organization.contact.modifierExtension) | 
?!Σ | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Extensions that cannot be ignored even if unrecognized
 | |

| [purpose](StructureDefinition-user-access-brand-definitions.html#Organization.contact.purpose) | 
 | 
0..1 | 
[CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) | 
The type of contact
Binding: [ContactEntityType](http://hl7.org/fhir/R4/valueset-contactentity-type.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)): The purpose for which you would contact a contact party.

 | |

| [name](StructureDefinition-user-access-brand-definitions.html#Organization.contact.name) | 
 | 
0..1 | 
[HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName) | 
A name associated with the contact | |

| [telecom](StructureDefinition-user-access-brand-definitions.html#Organization.contact.telecom) | 
 | 
0..* | 
[ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) | 
Contact details (telephone, email, etc.) for a contact
 | |

| [address](StructureDefinition-user-access-brand-definitions.html#Organization.contact.address) | 
 | 
0..1 | 
[Address](http://hl7.org/fhir/R4/datatypes.html#Address) | 
Visiting or postal addresses for the contact | |

| [endpoint](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint) | 
S | 
0..* | 
[Reference](http://hl7.org/fhir/R4/references.html)([User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html))[ {](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[b](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html)[}](http://hl7.org/fhir/R4/valueset-resource-aggregation-mode.html) | 
Endpoint associated with this brand
 | |

| [id](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.id) | 
 | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Unique id for inter-element referencing | |

| [extension](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.extension) | 
 | 
0..* | 
[Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) | 
Additional content defined by implementations
Slice: Unordered, Open by value:url
 | |

| [reference](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.reference) | 
SΣ[C](http://hl7.org/fhir/R4/conformance-rules.html#constraints) | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Relative URL to an Endpoint within the User Access Brands Bundle | |

| [type](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.type) | 
Σ | 
0..1 | 
[uri](http://hl7.org/fhir/R4/datatypes.html#uri) | 
Type the reference refers to (e.g. "Patient")
Binding: [ResourceType](http://hl7.org/fhir/R4/valueset-resource-types.html) ([extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)): Aa resource (or, for logical models, the URI of the logical model).

 | |

| [identifier](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.identifier) | 
Σ | 
0..1 | 
[Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) | 
Logical reference, when literal reference is not known | |

| [display](StructureDefinition-user-access-brand-definitions.html#Organization.endpoint.display) | 
Σ | 
0..1 | 
[string](http://hl7.org/fhir/R4/datatypes.html#string) | 
Text alternative for the resource | |

| 
[ Documentation for this format](https://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#table-views) | |

 
 
#### Terminology Bindings

| Path** | **Conformance** | **ValueSet** | **URI** | |

| Organization.language | [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred) | [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html)

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

| Organization.type | [example](http://hl7.org/fhir/R4/terminologies.html#example) | [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html)
`http://hl7.org/fhir/ValueSet/organization-type`

from the FHIR Standard
 | |

| Organization.type:pab | [required](http://hl7.org/fhir/R4/terminologies.html#required) | [UserAccessCategoryValueSet](ValueSet-user-access-category.html)
`http://hl7.org/fhir/smart-app-launch/ValueSet/user-access-category`

from this IG
 | |

| Organization.contact.purpose | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [ContactEntityType](http://hl7.org/fhir/R4/valueset-contactentity-type.html)
`http://hl7.org/fhir/ValueSet/contactentity-type`

from the FHIR Standard
 | |

| Organization.endpoint.type | [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible) | [ResourceType](http://hl7.org/fhir/R4/valueset-resource-types.html)
`http://hl7.org/fhir/ValueSet/resource-types`

from the FHIR Standard
 | |

 
 
 
 
 
 
 
#### Constraints

| Id** | **Grade** | **Path(s)** | **Details** | **Requirements** | |

| dom-2 | error | Organization | If the resource is contained in another resource, it SHALL NOT contain nested Resources**: contained.contained.empty() | | |

| dom-3 | error | Organization | If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource
: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty() | | |

| dom-4 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated
: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty() | | |

| dom-5 | error | Organization | If a resource is contained in another resource, it SHALL NOT have a security label
: contained.meta.security.empty() | | |

| dom-6 | best practice | Organization | A resource should have narrative for robust management
: text.`div`.exists() | | |

| ele-1 | error | **ALL** elements | All FHIR elements must have a @value or children
: hasValue() or (children().count() > id.count()) | | |

| ext-1 | error | **ALL** extensions | Must have either extensions or value[x], not both
: extension.exists() != value.exists() | | |

| org-1 | error | Organization | The organization SHALL at least have a name or an identifier, and possibly more than one
: (identifier.count() + name.count()) > 0 | | |

| org-2 | error | Organization.address | An address of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| org-3 | error | Organization.telecom | The telecom of an organization can never be of use 'home'
: where(use = 'home').empty() | | |

| uab-1 | error | Organization | Portal endpoints must also appear at Organization.endpoint
: Organization.extension('http://hl7.org/fhir/StructureDefinition/organization-portal').extension('portalEndpoint').value.ofType(Reference).reference.subsetOf(%resource.endpoint.reference) | | |

 
 

 

 

 

 

 

 
This structure is derived from [Organization](http://hl7.org/fhir/R4/organization.html)
 

 

 

Summary
**

Mandatory: 2 elements** Must-Support: 12 elements

Structures**

This structure refers to these other structures:

- [User Access Endpoint Profile (http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-endpoint)](StructureDefinition-user-access-endpoint.html)

**Extensions**

This structure refers to these extensions:

- [http://hl7.org/fhir/StructureDefinition/organization-brand](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-brand.html)

- [http://hl7.org/fhir/StructureDefinition/organization-portal](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-organization-portal.html)

**Slices**

This structure defines the following [Slices](http://hl7.org/fhir/R4/profiling.html#slices):

- The element 1 is sliced based on the value of Organization.type

 

 

 

 

 
 

 
Other representations of profile: [CSV](StructureDefinition-user-access-brand.csv), [Excel](StructureDefinition-user-access-brand.xlsx), [Schematron](StructureDefinition-user-access-brand.sch)