# Composition - FHIR v4.0.1A version-independent identifier for the Composition. This identifier stays constant as the composition is changed over timeThe workflow/clinical status of this composition. The status is a marker for the clinical standing of the document (this element modifies the meaning of other elements)The workflow/clinical status of the composition. (Strength=Required)Specifies the particular kind of composition (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the compositionType of a composition. (Strength=Preferred)A categorization for the type of the composition - helps for indexing and searching. This may be implied by or derived from the code specified in the Composition TypeHigh-level kind of a clinical document at a macro level. (Strength=Example)Who or what the composition is about. The composition can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of livestock, or a set of patients that share a common exposure)Describes the clinical encounter or type of care this documentation is associated withThe composition editing time, when the composition was last logically changed by the authorIdentifies who is responsible for the information in the composition, not necessarily who typed it inOfficial human-readable label for the compositionThe code specifying the level of confidentiality of the CompositionCodes specifying the level of confidentiality of the composition. (Strength=Required)Identifies the organization or group who is responsible for ongoing maintenance of and access to the composition/document informationThe type of attestation the authenticator offersThe way in which a person authenticated a composition. (Strength=Required)When the composition was attested by the partyWho attested the composition in the specified wayThe type of relationship that this composition has with anther composition or documentThe type of relationship between documents. (Strength=Required)The target composition/document of this relationshipThis list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the typeCode, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actThis list of codes represents the main clinical acts being documented. (Strength=Example)The period of time covered by the documentation. There is no assertion that the documentation is a complete representation for this period, only that it documents events during this timeThe description and/or reference of the event(s) being documented. For example, this could be used to document such a colonoscopy or an appendectomyThe label for this particular section.  This will be part of the rendered content for the document, and is often used to build a table of contentsA code identifying the kind of content contained within the section. This must be consistent with the section titleClassification of a section of a composition/document. (Strength=Example)Identifies who is responsible for the information in this section, not necessarily who typed it inThe actual focus of the section when it is not the subject of the composition, but instead represents something or someone associated with the subject such as (for a patient subject) a spouse, parent, fetus, or donor. If not focus is specified, the focus is assumed to be focus of the parent section, or, for a section in the Composition itself, the subject of the composition. Sections with a focus SHALL only include resources where the logical subject (patient, subject, focus, etc.) matches the section focus, or the resources have no logical subject (few resources)A human-readable narrative that contains the attested content of the section, used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrativeHow the entry list was prepared - whether it is a working list that is suitable for being maintained on an ongoing basis, or if it represents a snapshot of a list of items from another source, or whether it is a prepared list where items may be marked as added, modified or deletedThe processing mode that applies to this section. (Strength=Required)Specifies the order applied to the items in the section entriesWhat order applies to the items in the entry. (Strength=Preferred)A reference to the actual resource from which the narrative in the section is derivedIf the section is empty, why the list is empty. An empty section typically has some text explaining the empty reasonIf a section is empty, why it is empty. (Strength=Preferred)A participant who has attested to the accuracy of the composition/documentRelationships that this composition has with other compositions or documents that already existThe clinical service, such as a colonoscopy or an appendectomy, being documentedA nested sub-section within this sectionThe root of the sections that make up the compositionA version-independent identifier for the Composition. This identifier stays constant as the composition is changed over timeThe workflow/clinical status of this composition. The status is a marker for the clinical standing of the document (this element modifies the meaning of other elements)The workflow/clinical status of the composition. (Strength=Required)Specifies the particular kind of composition (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the compositionType of a composition. (Strength=Preferred)A categorization for the type of the composition - helps for indexing and searching. This may be implied by or derived from the code specified in the Composition TypeHigh-level kind of a clinical document at a macro level. (Strength=Example)Who or what the composition is about. The composition can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of livestock, or a set of patients that share a common exposure)Describes the clinical encounter or type of care this documentation is associated withThe composition editing time, when the composition was last logically changed by the authorIdentifies who is responsible for the information in the composition, not necessarily who typed it inOfficial human-readable label for the compositionThe code specifying the level of confidentiality of the CompositionCodes specifying the level of confidentiality of the composition. (Strength=Required)Identifies the organization or group who is responsible for ongoing maintenance of and access to the composition/document informationThe type of attestation the authenticator offersThe way in which a person authenticated a composition. (Strength=Required)When the composition was attested by the partyWho attested the composition in the specified wayThe type of relationship that this composition has with anther composition or documentThe type of relationship between documents. (Strength=Required)The target composition/document of this relationshipThis list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the typeCode, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actThis list of codes represents the main clinical acts being documented. (Strength=Example)The period of time covered by the documentation. There is no assertion that the documentation is a complete representation for this period, only that it documents events during this timeThe description and/or reference of the event(s) being documented. For example, this could be used to document such a colonoscopy or an appendectomyThe label for this particular section.  This will be part of the rendered content for the document, and is often used to build a table of contentsA code identifying the kind of content contained within the section. This must be consistent with the section titleClassification of a section of a composition/document. (Strength=Example)Identifies who is responsible for the information in this section, not necessarily who typed it inThe actual focus of the section when it is not the subject of the composition, but instead represents something or someone associated with the subject such as (for a patient subject) a spouse, parent, fetus, or donor. If not focus is specified, the focus is assumed to be focus of the parent section, or, for a section in the Composition itself, the subject of the composition. Sections with a focus SHALL only include resources where the logical subject (patient, subject, focus, etc.) matches the section focus, or the resources have no logical subject (few resources)A human-readable narrative that contains the attested content of the section, used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrativeHow the entry list was prepared - whether it is a working list that is suitable for being maintained on an ongoing basis, or if it represents a snapshot of a list of items from another source, or whether it is a prepared list where items may be marked as added, modified or deletedThe processing mode that applies to this section. (Strength=Required)Specifies the order applied to the items in the section entriesWhat order applies to the items in the entry. (Strength=Preferred)A reference to the actual resource from which the narrative in the section is derivedIf the section is empty, why the list is empty. An empty section typically has some text explaining the empty reasonIf a section is empty, why it is empty. (Strength=Preferred)A participant who has attested to the accuracy of the composition/documentRelationships that this composition has with other compositions or documents that already existThe clinical service, such as a colonoscopy or an appendectomy, being documentedA nested sub-section within this sectionThe root of the sections that make up the composition

> Source: https://hl7.org/fhir/R4/composition.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/composition.html) [R4B](http://hl7.org/fhir/R4B/composition.html) **R4** [R3](http://hl7.org/fhir/STU3/composition.html) [R2](http://hl7.org/fhir/DSTU2/composition.html)
 

# 2.41 Resource Composition - Content [
](composition.html#2.41)

| [Structured Documents ](http://www.hl7.org/Special/committees/structure/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Not Classified | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).

## 2.41.1 Scope and Usage [
](composition.html#scope)

 
A Composition is the basic structure from which [FHIR Documents](documents.html) - 
immutable bundles with attested narrative - are built. A single logical composition may be 
associated with a series of derived documents, each of which is a frozen copy of the 
composition.

Note: [EN 13606 ](http://en.wikipedia.org/wiki/EN_13606) uses the term "Composition" 
to refer to a single commit to an EHR system, and offers some common examples: a composition 
containing a consultation note, a progress note, a report or a letter, an investigation report, 
a prescription form or a set of bedside nursing observations. Using Composition for an attested
EHR commit is a valid use of the Composition resource, but for FHIR purposes, it would be usual
to make more granular updates with individual provenance statements.

The [Clinical Document profile](composition-clinicaldocument.html) constrains Composition to specify a clinical document
(matching [CDA ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7)). 
See also the [comparison with CDA](comparison-cda.html).

## 2.41.2 Boundaries and Relationships [
](composition.html#bnr)

Composition is a structure for grouping information for purposes of persistence and attestability. There
are several other grouping structures in FHIR with distinct purposes:

- 
The [List](list.html) resource - enumerates a flat collection of resources and provides features for managing the collection. 
While a particular List instance may represent a "snapshot", from a business process perspective, the notion of "list" 
is dynamic – items are added and removed over time. The List resource references other resources. Lists may be 
curated and have specific business meaning.

- 
The [Group](group.html) resource - defines a group of specific people, animals, devices, etc. by enumerating them, 
or by describing qualities that group members have. The Group resource refers to other resources, possibly implicitly. 
Groups are intended to be acted upon or observed as a whole (e.g., performing therapy on a group, calculating risk for a group, 
etc.). This resource will commonly be used for public health (e.g., describing an at-risk population), clinical trials (e.g., 
defining a test subject pool) and similar purposes.

- 
The [Bundle](bundle.html) resource - is an infrastructure container for a group of resources. It does not have narrative 
and is used to group collections of resources for transmission, persistence or processing (e.g., messages, documents, transactions, 
query responses, etc.). The content of bundles is typically algorithmically determined for a particular exchange or persistence purpose.

- 
The [Composition](composition.html) resource - defines a set of healthcare-related information that is assembled 
together into a single logical document that provides a single coherent statement of meaning, establishes its own context and 
that has clinical attestation with regard to who is making the statement. The Composition resource provides the basic structure 
of a FHIR [document](documents.html). The full content of the document is expressed using a [Bundle](bundle.html) 
containing the Composition and its entries. 

The Composition resource organizes clinical and administrative content into sections, each of which contains a narrative, 
and references other resources for supporting data. The narrative content of the various sections in a Composition are 
supported by the resources referenced in the section entries. The complete set of content to make up a document includes 
the Composition resource together with various resources pointed to or indirectly
connected to the Composition, all gathered together into a [Bundle](bundle.html) for transport and persistence.
Resources associated with the following list of Composition references SHALL be included in the [Bundle](bundle.html):

 - [Composition.subject](composition-definitions.html#Composition.subject)

 - [Composition.encounter](composition-definitions.html#Composition.encounter)

 - [Composition.author](composition-definitions.html#Composition.author)

 - [Composition.attester.party](composition-definitions.html#Composition.attester.party)

 - [Composition.custodian](composition-definitions.html#Composition.custodian)

 - [Composition.event.detail](composition-definitions.html#Composition.event.detail)

 - [Composition.section.author](composition-definitions.html#Composition.section.author)

 - [Composition.section.focus](composition-definitions.html#Composition.section.focus)

 - [Composition.section.entry](composition-definitions.html#Composition.section.entry)

Other resources referred to by those resources MAY be included in the [Bundle](bundle.html) at the discretion of the authoring 
system as documented in the system's operation definition (such as [$document](composition-operation-document.html) operation), 
or as specified by any applicable profiles. 

## 2.41.3 Background and Context [
](composition.html#bnc)

### 2.41.3.1 Composition Status Codes [](composition.html#status)

Every composition has a status element, which describes the status of the content of the composition, taken from this list of codes:

### 2.41.3.2 The workflow/clinical status of the composition. [
](composition.html#2.41.3.2)

 | preliminary | This is a preliminary composition or document (also known as initial or interim). The content may be incomplete or unverified. | |

 | final | This version of the composition is complete and verified by an appropriate person and no further work is planned. Any subsequent updates would be on a new version of the composition. | |

 | amended | The composition content or the referenced resources have been modified (edited or added to) subsequent to being released as "final" and the composition is complete and verified by an authorized person. | |

 | entered-in-error | The composition or document was originally created/issued in error, and this is an amendment that marks that the entire series should not be considered as valid. | |

Composition status generally only moves down through this list - it moves from `preliminary` to `final` and then it may progress to `amended`. 
Note that in many workflows, only `final` compositions are made available and the `preliminary` status is not used. 

A very few compositions are created entirely in error in the workflow - usually the composition concerns the wrong patient or is written by the wrong author,
and the error is only detected after the composition has been used or documents have been derived from it. To support resolution of this case, 
the composition is updated to be marked as `entered-in-error` and a new derived document can be created. This means that the entire series of derived 
documents is now considered to be created in error and systems receiving derived documents based on retracted compositions
SHOULD remove data taken from earlier documents from routine use and/or take other appropriate actions. Systems are not required to 
provide this workflow or support documents derived from retracted compositions, but they SHALL NOT ignore a status of `entered-in-error`. 
Note that systems that handle compositions or derived documents and don't support the error status need to define 
some other way of handling compositions that are created in error; while this is not a common occurrence, some clinical systems 
have no provision for removing erroneous information from a patient's record, and there is no way for a user to know that it is not fit for use -
this is not safe. 

### 2.41.3.3 Note for CDA aware readers [
](composition.html#cda)

Many users of this specification are familiar with the [Clinical Document Architecture ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) (CDA) and related specifications.
CDA is a primary design input to the Composition resource (other principal inputs are other HL7 document specifications and EN13606). There are three important structural 
differences between CDA and the Composition resource:

 - A composition is a logical construct- its identifier matches to the CDA ClinicalDocument.setId. 
 Composition resources are wrapped into [Document](documents.html) structures, for exchange
 of the whole package (the composition and its parts), and this wrapped, sealed entity is equivalent to a CDA document, 
 where the Bundle.id is equivalent in function to ClinicalDocument.id (but it is not identical when interconverting, since it's a transform between them).

 - The composition section defines a section (or sub-section) of the document, but unlike CDA, the section entries are 
 actually references to other [resources](resourcelist.html) that hold the supporting data content for the section. 
 This design means that the data can be reused in many other ways. 
 

 - Unlike CDA, the context defined in the `Composition` (the confidentiality, subject, author, event, event period and encounter) apply to the composition and do not specifically apply to the resources referenced from 
 the `section.entry`. There is no context flow model in FHIR, so each resource referenced from 
 within a `Composition` expresses its own individual context. In this way, clinical content can 
 safely be extracted from the composition.

In addition, note that both the code lists (e.g., [Composition.status](valueset-composition-status.html)) and the Composition resource are [mapped](composition-mappings.html) to [HL7 v3 ](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) and/or CDA.

This resource is referenced by itself, [Contract](contract.html#Contract) and [Procedure](procedure.html#Procedure)

## 2.41.4 
Resource Content
 [
](composition.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Composition](composition-definitions.html#Composition) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A set of resources composed into a single coherent clinical statement with clinical attestation**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](composition-definitions.html#Composition.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Version-independent identifier for the Composition | |

| [status](composition-definitions.html#Composition.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | preliminary | final | amended | entered-in-error
[CompositionStatus](valueset-composition-status.html) ([Required](terminologies.html#required)) | |

| [type](composition-definitions.html#Composition.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of composition (LOINC if possible)
[FHIR Document Type Codes](valueset-doc-typecodes.html) ([Preferred](terminologies.html#preferred)) | |

| [category](composition-definitions.html#Composition.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Categorization of Composition
[Document Class Value Set](valueset-document-classcodes.html) ([Example](terminologies.html#example))
 | |

| [subject](composition-definitions.html#Composition.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Who and/or what the composition is about | |

| [encounter](composition-definitions.html#Composition.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Context of the Composition | |

| [date](composition-definitions.html#Composition.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [dateTime](datatypes.html#dateTime) | Composition editing time | |

| [author](composition-definitions.html#Composition.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Who and/or what authored the composition
 | |

| [title](composition-definitions.html#Composition.title) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [string](datatypes.html#string) | Human Readable name/title | |

| [confidentiality](composition-definitions.html#Composition.confidentiality) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | As defined by affinity domain
[V3 Value SetConfidentialityClassification](v3/ConfidentialityClassification/vs.html) ([Required](terminologies.html#required)) | |

| [attester](composition-definitions.html#Composition.attester) | | 0..* | [BackboneElement](backboneelement.html) | Attests to accuracy of composition
 | |

| [mode](composition-definitions.html#Composition.attester.mode) | | 1..1 | [code](datatypes.html#code) | personal | professional | legal | official
[CompositionAttestationMode](valueset-composition-attestation-mode.html) ([Required](terminologies.html#required)) | |

| [time](composition-definitions.html#Composition.attester.time) | | 0..1 | [dateTime](datatypes.html#dateTime) | When the composition was attested | |

| [party](composition-definitions.html#Composition.attester.party) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Who attested the composition | |

| [custodian](composition-definitions.html#Composition.custodian) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization which maintains the composition | |

| [relatesTo](composition-definitions.html#Composition.relatesTo) | | 0..* | [BackboneElement](backboneelement.html) | Relationships to other compositions/documents
 | |

| [code](composition-definitions.html#Composition.relatesTo.code) | | 1..1 | [code](datatypes.html#code) | replaces | transforms | signs | appends
[DocumentRelationshipType](valueset-document-relationship-type.html) ([Required](terminologies.html#required)) | |

| [target[x]](composition-definitions.html#Composition.relatesTo.target_x_) | | 1..1 | | Target of the relationship | |

| targetIdentifier | | | [Identifier](datatypes.html#Identifier) | | |

| targetReference | | | [Reference](references.html#Reference)([Composition](composition.html)) | | |

| [event](composition-definitions.html#Composition.event) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | The clinical service(s) being documented
 | |

| [code](composition-definitions.html#Composition.event.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Code(s) that apply to the event being documented
[v3 Code System ActCode](v3/ActCode/vs.html) ([Example](terminologies.html#example))
 | |

| [period](composition-definitions.html#Composition.event.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | The period covered by the documentation | |

| [detail](composition-definitions.html#Composition.event.detail) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | The event(s) being documented
 | |

| [section](composition-definitions.html#Composition.section) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Composition is broken into sections
+ Rule: A section must contain at least one of text, entries, or sub-sections
+ Rule: A section can only have an emptyReason if it is empty
 | |

| [title](composition-definitions.html#Composition.section.title) | | 0..1 | [string](datatypes.html#string) | Label for section (e.g. for ToC) | |

| [code](composition-definitions.html#Composition.section.code) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of section (recommended)
[Document Section Codes](valueset-doc-section-codes.html) ([Example](terminologies.html#example)) | |

| [author](composition-definitions.html#Composition.section.author) | | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Who and/or what authored the section
 | |

| [focus](composition-definitions.html#Composition.section.focus) | | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Who/what the section is about, when it is not about the subject of composition | |

| [text](composition-definitions.html#Composition.section.text) | [I](conformance-rules.html#constraints) | 0..1 | [Narrative](narrative.html#Narrative) | Text summary of the section, for human interpretation | |

| [mode](composition-definitions.html#Composition.section.mode) | | 0..1 | [code](datatypes.html#code) | working | snapshot | changes
[ListMode](valueset-list-mode.html) ([Required](terminologies.html#required)) | |

| [orderedBy](composition-definitions.html#Composition.section.orderedBy) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Order of section entries
[List Order Codes](valueset-list-order.html) ([Preferred](terminologies.html#preferred)) | |

| [entry](composition-definitions.html#Composition.section.entry) | [I](conformance-rules.html#constraints) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | A reference to data that supports this section
 | |

| [emptyReason](composition-definitions.html#Composition.section.emptyReason) | [I](conformance-rules.html#constraints) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the section is empty
[List Empty Reasons](valueset-list-empty-reason.html) ([Preferred](terminologies.html#preferred)) | |

| [section](composition-definitions.html#Composition.section.section) | [I](conformance-rules.html#constraints) | 0..* | see [section](#Composition.section) | Nested Section
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Composition ([DomainResource](domainresource.html))[A version-independent identifier for the Composition. This identifier stays constant as the composition is changed over timeidentifier](composition-definitions.html#Composition.identifier) : [Identifier](datatypes.html#Identifier) [0..1][The workflow/clinical status of this composition. The status is a marker for the clinical standing of the document (this element modifies the meaning of other elements)status](composition-definitions.html#Composition.status) : [code](datatypes.html#code) [1..1] « [The workflow/clinical status of the composition. (Strength=Required)CompositionStatus](valueset-composition-status.html)! »[Specifies the particular kind of composition (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the compositiontype](composition-definitions.html#Composition.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Type of a composition. (Strength=Preferred)FHIRDocumentTypeCodes](valueset-doc-typecodes.html)? »[A categorization for the type of the composition - helps for indexing and searching. This may be implied by or derived from the code specified in the Composition Typecategory](composition-definitions.html#Composition.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [High-level kind of a clinical document at a macro level. (Strength=Example)DocumentClassValueSet](valueset-document-classcodes.html)?? »[Who or what the composition is about. The composition can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of livestock, or a set of patients that share a common exposure)subject](composition-definitions.html#Composition.subject) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[Describes the clinical encounter or type of care this documentation is associated withencounter](composition-definitions.html#Composition.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The composition editing time, when the composition was last logically changed by the authordate](composition-definitions.html#Composition.date) : [dateTime](datatypes.html#dateTime) [1..1][Identifies who is responsible for the information in the composition, not necessarily who typed it inauthor](composition-definitions.html#Composition.author) : [Reference](references.html#Reference) [1..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)| [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »[Official human-readable label for the compositiontitle](composition-definitions.html#Composition.title) : [string](datatypes.html#string) [1..1][The code specifying the level of confidentiality of the Compositionconfidentiality](composition-definitions.html#Composition.confidentiality) : [code](datatypes.html#code) [0..1] « [Codes specifying the level of confidentiality of the composition. (Strength=Required)v3.ConfidentialityClassificat...](v3/ConfidentialityClassification/vs.html)! »[Identifies the organization or group who is responsible for ongoing maintenance of and access to the composition/document informationcustodian](composition-definitions.html#Composition.custodian) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »Attester[The type of attestation the authenticator offersmode](composition-definitions.html#Composition.attester.mode) : [code](datatypes.html#code) [1..1] « [The way in which a person authenticated a composition. (Strength=Required)CompositionAttestationMode](valueset-composition-attestation-mode.html)! »[When the composition was attested by the partytime](composition-definitions.html#Composition.attester.time) : [dateTime](datatypes.html#dateTime) [0..1][Who attested the composition in the specified wayparty](composition-definitions.html#Composition.attester.party) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization) »RelatesTo[The type of relationship that this composition has with anther composition or documentcode](composition-definitions.html#Composition.relatesTo.code) : [code](datatypes.html#code) [1..1] « [The type of relationship between documents. (Strength=Required)DocumentRelationshipType](valueset-document-relationship-type.html)! »[The target composition/document of this relationshiptarget[x]](composition-definitions.html#Composition.relatesTo.target_x_) : [Type](formats.html#umlchoice) [1..1] « [Identifier](datatypes.html#Identifier)|[Reference](references.html#Reference)([Composition](composition.html#Composition)) »Event[This list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the typeCode, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actcode](composition-definitions.html#Composition.event.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [This list of codes represents the main clinical acts being documented. (Strength=Example)v3.ActCode](v3/ActCode/vs.html)?? »[The period of time covered by the documentation. There is no assertion that the documentation is a complete representation for this period, only that it documents events during this timeperiod](composition-definitions.html#Composition.event.period) : [Period](datatypes.html#Period) [0..1][The description and/or reference of the event(s) being documented. For example, this could be used to document such a colonoscopy or an appendectomydetail](composition-definitions.html#Composition.event.detail) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »Section[The label for this particular section. This will be part of the rendered content for the document, and is often used to build a table of contentstitle](composition-definitions.html#Composition.section.title) : [string](datatypes.html#string) [0..1][A code identifying the kind of content contained within the section. This must be consistent with the section titlecode](composition-definitions.html#Composition.section.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Classification of a section of a composition/document. (Strength=Example)DocumentSectionCodes](valueset-doc-section-codes.html)?? »[Identifies who is responsible for the information in this section, not necessarily who typed it inauthor](composition-definitions.html#Composition.section.author) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)| [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »[The actual focus of the section when it is not the subject of the composition, but instead represents something or someone associated with the subject such as (for a patient subject) a spouse, parent, fetus, or donor. If not focus is specified, the focus is assumed to be focus of the parent section, or, for a section in the Composition itself, the subject of the composition. Sections with a focus SHALL only include resources where the logical subject (patient, subject, focus, etc.) matches the section focus, or the resources have no logical subject (few resources)focus](composition-definitions.html#Composition.section.focus) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[A human-readable narrative that contains the attested content of the section, used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrativetext](composition-definitions.html#Composition.section.text) : [Narrative](narrative.html#Narrative) [0..1][How the entry list was prepared - whether it is a working list that is suitable for being maintained on an ongoing basis, or if it represents a snapshot of a list of items from another source, or whether it is a prepared list where items may be marked as added, modified or deletedmode](composition-definitions.html#Composition.section.mode) : [code](datatypes.html#code) [0..1] « [The processing mode that applies to this section. (Strength=Required)ListMode](valueset-list-mode.html)! »[Specifies the order applied to the items in the section entriesorderedBy](composition-definitions.html#Composition.section.orderedBy) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [What order applies to the items in the entry. (Strength=Preferred)ListOrderCodes](valueset-list-order.html)? »[A reference to the actual resource from which the narrative in the section is derivedentry](composition-definitions.html#Composition.section.entry) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[If the section is empty, why the list is empty. An empty section typically has some text explaining the empty reasonemptyReason](composition-definitions.html#Composition.section.emptyReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [If a section is empty, why it is empty. (Strength=Preferred)ListEmptyReasons](valueset-list-empty-reason.html)? »
[A participant who has attested to the accuracy of the composition/documentattester](composition-definitions.html#Composition.attester)[0..*][Relationships that this composition has with other compositions or documents that already existrelatesTo](composition-definitions.html#Composition.relatesTo)[0..*][The clinical service, such as a colonoscopy or an appendectomy, being documentedevent](composition-definitions.html#Composition.event)[0..*][A nested sub-section within this sectionsection](composition-definitions.html#Composition.section.section)[0..*][The root of the sections that make up the compositionsection](composition-definitions.html#Composition.section)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Composition**](composition-definitions.html#Composition) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](composition-definitions.html#Composition.identifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Version-independent identifier for the Composition](terminologies.html#unbound) --></identifier>
 <[**status**](composition-definitions.html#Composition.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [preliminary | final | amended | entered-in-error](valueset-composition-status.html) -->
 <[**type**](composition-definitions.html#Composition.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of composition (LOINC if possible)](valueset-doc-typecodes.html) --></type>
 <[**category**](composition-definitions.html#Composition.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Categorization of Composition](valueset-document-classcodes.html) --></category>
 <[**subject**](composition-definitions.html#Composition.subject)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Who and/or what the composition is about](terminologies.html#unbound) --></subject>
 <[**encounter**](composition-definitions.html#Composition.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Context of the Composition](terminologies.html#unbound) --></encounter>
 <[**date**](composition-definitions.html#Composition.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **1..1** [Composition editing time](terminologies.html#unbound) -->
 <[**author**](composition-definitions.html#Composition.author)><!-- **1..*** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Who and/or what authored the composition](terminologies.html#unbound) --></author>
 <[**title**](composition-definitions.html#Composition.title) value="[[string](datatypes.html#string)]"/><!-- **1..1** [Human Readable name/title](terminologies.html#unbound) -->
 <[**confidentiality**](composition-definitions.html#Composition.confidentiality) value="[[code](datatypes.html#code)]"/><!-- **0..1** [As defined by affinity domain](v3/ConfidentialityClassification/vs.html) -->
 <[**attester**](composition-definitions.html#Composition.attester)> <!-- **0..*** Attests to accuracy of composition -->
 <[**mode**](composition-definitions.html#Composition.attester.mode) value="[[code](datatypes.html#code)]"/><!-- **1..1** [personal | professional | legal | official](valueset-composition-attestation-mode.html) -->
 <[**time**](composition-definitions.html#Composition.attester.time) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When the composition was attested](terminologies.html#unbound) -->
 <[**party**](composition-definitions.html#Composition.attester.party)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Organization](organization.html#Organization)) [Who attested the composition](terminologies.html#unbound) --></party>
 </attester>
 <[**custodian**](composition-definitions.html#Composition.custodian)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization which maintains the composition](terminologies.html#unbound) --></custodian>
 <[**relatesTo**](composition-definitions.html#Composition.relatesTo)> <!-- **0..*** Relationships to other compositions/documents -->
 <[**code**](composition-definitions.html#Composition.relatesTo.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [replaces | transforms | signs | appends](valueset-document-relationship-type.html) -->
 <[**target[x]**](composition-definitions.html#Composition.relatesTo.target[x])><!-- **1..1** [Identifier](datatypes.html#Identifier)|[Reference](references.html#Reference)([Composition](composition.html#Composition)) [Target of the relationship](terminologies.html#unbound) --></target[x]>
 </relatesTo>
 <[**event**](composition-definitions.html#Composition.event)> <!-- **0..*** The clinical service(s) being documented -->
 <[**code**](composition-definitions.html#Composition.event.code)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Code(s) that apply to the event being documented](v3/ActCode/vs.html) --></code>
 <[**period**](composition-definitions.html#Composition.event.period)><!-- **0..1** [Period](datatypes.html#Period) [The period covered by the documentation](terminologies.html#unbound) --></period>
 <[**detail**](composition-definitions.html#Composition.event.detail)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [The event(s) being documented](terminologies.html#unbound) --></detail>
 </event>
 <[**section**](composition-definitions.html#Composition.section)> <!-- **0..*** Composition is broken into sections -->
 <[**title**](composition-definitions.html#Composition.section.title) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Label for section (e.g. for ToC)](terminologies.html#unbound) -->
 <[**code**](composition-definitions.html#Composition.section.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Classification of section (recommended)](valueset-doc-section-codes.html) --></code>
 <[**author**](composition-definitions.html#Composition.section.author)><!-- **0..*** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Who and/or what authored the section](terminologies.html#unbound) --></author>
 <[**focus**](composition-definitions.html#Composition.section.focus)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Who/what the section is about, when it is not about the subject of composition](terminologies.html#unbound) --></focus>
 <[**text**](composition-definitions.html#Composition.section.text)><!-- ** 0..1** [Narrative](narrative.html#Narrative) [Text summary of the section, for human interpretation](terminologies.html#unbound) --></text>
 <[**mode**](composition-definitions.html#Composition.section.mode) value="[[code](datatypes.html#code)]"/><!-- **0..1** [working | snapshot | changes](valueset-list-mode.html) -->
 <[**orderedBy**](composition-definitions.html#Composition.section.orderedBy)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Order of section entries](valueset-list-order.html) --></orderedBy>
 <[**entry**](composition-definitions.html#Composition.section.entry)><!-- ** 0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [A reference to data that supports this section](terminologies.html#unbound) --></entry>
 <[**emptyReason**](composition-definitions.html#Composition.section.emptyReason)><!-- ** 0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Why the section is empty](valueset-list-empty-reason.html) --></emptyReason>
 <[**section**](composition-definitions.html#Composition.section.section)><!-- ** 0..*** Content as for Composition.section [Nested Section](terminologies.html#unbound) --></section>
 </section>
</Composition>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Composition**](composition-definitions.html#Composition)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](composition-definitions.html#Composition.identifier)" : { [Identifier](datatypes.html#Identifier) }, // [Version-independent identifier for the Composition](terminologies.html#unbound)
 "[status](composition-definitions.html#Composition.status)" : "<[code](datatypes.html#code)>", // **R!** [preliminary | final | amended | entered-in-error](valueset-composition-status.html)
 "[type](composition-definitions.html#Composition.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Kind of composition (LOINC if possible)](valueset-doc-typecodes.html)
 "[category](composition-definitions.html#Composition.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Categorization of Composition](valueset-document-classcodes.html)
 "[subject](composition-definitions.html#Composition.subject)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Who and/or what the composition is about](terminologies.html#unbound)
 "[encounter](composition-definitions.html#Composition.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Context of the Composition](terminologies.html#unbound)
 "[date](composition-definitions.html#Composition.date)" : "<[dateTime](datatypes.html#dateTime)>", // **R!** [Composition editing time](terminologies.html#unbound)
 "[author](composition-definitions.html#Composition.author)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) }], // **R!** [Who and/or what authored the composition](terminologies.html#unbound)
 "[title](composition-definitions.html#Composition.title)" : "<[string](datatypes.html#string)>", // **R!** [Human Readable name/title](terminologies.html#unbound)
 "[confidentiality](composition-definitions.html#Composition.confidentiality)" : "<[code](datatypes.html#code)>", // [As defined by affinity domain](v3/ConfidentialityClassification/vs.html)
 "[attester](composition-definitions.html#Composition.attester)" : [{ // [Attests to accuracy of composition](terminologies.html#unbound)
 "[mode](composition-definitions.html#Composition.attester.mode)" : "<[code](datatypes.html#code)>", // **R!** [personal | professional | legal | official](valueset-composition-attestation-mode.html)
 "[time](composition-definitions.html#Composition.attester.time)" : "<[dateTime](datatypes.html#dateTime)>", // [When the composition was attested](terminologies.html#unbound)
 "[party](composition-definitions.html#Composition.attester.party)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Organization](organization.html#Organization)) } // [Who attested the composition](terminologies.html#unbound)
 }],
 "[custodian](composition-definitions.html#Composition.custodian)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization which maintains the composition](terminologies.html#unbound)
 "[relatesTo](composition-definitions.html#Composition.relatesTo)" : [{ // [Relationships to other compositions/documents](terminologies.html#unbound)
 "[code](composition-definitions.html#Composition.relatesTo.code)" : "<[code](datatypes.html#code)>", // **R!** [replaces | transforms | signs | appends](valueset-document-relationship-type.html)
 // target[x]: Target of the relationship. One of these 2:
 "[targetIdentifier](composition-definitions.html#Composition.relatesTo.targetIdentifier)" : { [Identifier](datatypes.html#Identifier) }
 "[targetReference](composition-definitions.html#Composition.relatesTo.targetReference)" : { [Reference](references.html#Reference)([Composition](composition.html#Composition)) }
 }],
 "[event](composition-definitions.html#Composition.event)" : [{ // [The clinical service(s) being documented](terminologies.html#unbound)
 "[code](composition-definitions.html#Composition.event.code)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Code(s) that apply to the event being documented](v3/ActCode/vs.html)
 "[period](composition-definitions.html#Composition.event.period)" : { [Period](datatypes.html#Period) }, // [The period covered by the documentation](terminologies.html#unbound)
 "[detail](composition-definitions.html#Composition.event.detail)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }] // [The event(s) being documented](terminologies.html#unbound)
 }],
 "[section](composition-definitions.html#Composition.section)" : [{ // [Composition is broken into sections](terminologies.html#unbound)
 "[title](composition-definitions.html#Composition.section.title)" : "<[string](datatypes.html#string)>", // [Label for section (e.g. for ToC)](terminologies.html#unbound)
 "[code](composition-definitions.html#Composition.section.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Classification of section (recommended)](valueset-doc-section-codes.html)
 "[author](composition-definitions.html#Composition.section.author)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) }], // [Who and/or what authored the section](terminologies.html#unbound)
 "[focus](composition-definitions.html#Composition.section.focus)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Who/what the section is about, when it is not about the subject of composition](terminologies.html#unbound)
 "[text](composition-definitions.html#Composition.section.text)" : { [Narrative](narrative.html#Narrative) }, // **C?** [Text summary of the section, for human interpretation](terminologies.html#unbound)
 "[mode](composition-definitions.html#Composition.section.mode)" : "<[code](datatypes.html#code)>", // [working | snapshot | changes](valueset-list-mode.html)
 "[orderedBy](composition-definitions.html#Composition.section.orderedBy)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Order of section entries](valueset-list-order.html)
 "[entry](composition-definitions.html#Composition.section.entry)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // **C?** [A reference to data that supports this section](terminologies.html#unbound)
 "[emptyReason](composition-definitions.html#Composition.section.emptyReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **C?** [Why the section is empty](valueset-list-empty-reason.html)
 "[section](composition-definitions.html#Composition.section.section)" : [{ Content as for Composition.section }] // **C?** [Nested Section](terminologies.html#unbound)
 }]
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Composition**](composition-definitions.html#Composition);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Composition.identifier](composition-definitions.html#Composition.identifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Version-independent identifier for the Composition
 fhir:[Composition.status](composition-definitions.html#Composition.status) [ [code](datatypes.html#code) ]; # 1..1 preliminary | final | amended | entered-in-error
 fhir:[Composition.type](composition-definitions.html#Composition.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Kind of composition (LOINC if possible)
 fhir:[Composition.category](composition-definitions.html#Composition.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Categorization of Composition
 fhir:[Composition.subject](composition-definitions.html#Composition.subject) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Who and/or what the composition is about
 fhir:[Composition.encounter](composition-definitions.html#Composition.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Context of the Composition
 fhir:[Composition.date](composition-definitions.html#Composition.date) [ [dateTime](datatypes.html#dateTime) ]; # 1..1 Composition editing time
 fhir:[Composition.author](composition-definitions.html#Composition.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ], ... ; # 1..* Who and/or what authored the composition
 fhir:[Composition.title](composition-definitions.html#Composition.title) [ [string](datatypes.html#string) ]; # 1..1 Human Readable name/title
 fhir:[Composition.confidentiality](composition-definitions.html#Composition.confidentiality) [ [code](datatypes.html#code) ]; # 0..1 As defined by affinity domain
 fhir:[Composition.attester](composition-definitions.html#Composition.attester) [ # 0..* Attests to accuracy of composition
 fhir:[Composition.attester.mode](composition-definitions.html#Composition.attester.mode) [ [code](datatypes.html#code) ]; # 1..1 personal | professional | legal | official
 fhir:[Composition.attester.time](composition-definitions.html#Composition.attester.time) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the composition was attested
 fhir:[Composition.attester.party](composition-definitions.html#Composition.attester.party) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 0..1 Who attested the composition
 ], ...;
 fhir:[Composition.custodian](composition-definitions.html#Composition.custodian) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization which maintains the composition
 fhir:[Composition.relatesTo](composition-definitions.html#Composition.relatesTo) [ # 0..* Relationships to other compositions/documents
 fhir:[Composition.relatesTo.code](composition-definitions.html#Composition.relatesTo.code) [ [code](datatypes.html#code) ]; # 1..1 replaces | transforms | signs | appends
 # [Composition.relatesTo.target[x]](composition-definitions.html#Composition.relatesTo.target[x]) : 1..1 Target of the relationship. One of these 2
 fhir:[Composition.relatesTo.targetIdentifier](composition-definitions.html#Composition.relatesTo.targetIdentifier) [ [Identifier](datatypes.html#Identifier) ]
 fhir:[Composition.relatesTo.targetReference](composition-definitions.html#Composition.relatesTo.targetReference) [ [Reference](references.html#Reference)([Composition](composition.html#Composition)) ]
 ], ...;
 fhir:[Composition.event](composition-definitions.html#Composition.event) [ # 0..* The clinical service(s) being documented
 fhir:[Composition.event.code](composition-definitions.html#Composition.event.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Code(s) that apply to the event being documented
 fhir:[Composition.event.period](composition-definitions.html#Composition.event.period) [ [Period](datatypes.html#Period) ]; # 0..1 The period covered by the documentation
 fhir:[Composition.event.detail](composition-definitions.html#Composition.event.detail) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* The event(s) being documented
 ], ...;
 fhir:[Composition.section](composition-definitions.html#Composition.section) [ # 0..* Composition is broken into sections
 fhir:[Composition.section.title](composition-definitions.html#Composition.section.title) [ [string](datatypes.html#string) ]; # 0..1 Label for section (e.g. for ToC)
 fhir:[Composition.section.code](composition-definitions.html#Composition.section.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Classification of section (recommended)
 fhir:[Composition.section.author](composition-definitions.html#Composition.section.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ], ... ; # 0..* Who and/or what authored the section
 fhir:[Composition.section.focus](composition-definitions.html#Composition.section.focus) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Who/what the section is about, when it is not about the subject of composition
 fhir:[Composition.section.text](composition-definitions.html#Composition.section.text) [ [Narrative](narrative.html#Narrative) ]; # 0..1 Text summary of the section, for human interpretation
 fhir:[Composition.section.mode](composition-definitions.html#Composition.section.mode) [ [code](datatypes.html#code) ]; # 0..1 working | snapshot | changes
 fhir:[Composition.section.orderedBy](composition-definitions.html#Composition.section.orderedBy) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Order of section entries
 fhir:[Composition.section.entry](composition-definitions.html#Composition.section.entry) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* A reference to data that supports this section
 fhir:[Composition.section.emptyReason](composition-definitions.html#Composition.section.emptyReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Why the section is empty
 fhir:[Composition.section.section](composition-definitions.html#Composition.section.section) [ [See Composition.section](#ttl-Composition.section) ], ... ; # 0..* Nested Section
 ], ...;
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Composition](composition.html#Composition)
 | 
 | 
 |

 | 
 Composition.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/composition-status to http://hl7.org/fhir/ValueSet/composition-status|4.0.1

 

 | 
 |

 | 
 Composition.category | 
 
 

 - Renamed from class to category

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Composition.subject | 
 
 

 - Min Cardinality changed from 1 to 0

 

 | 
 |

 | 
 Composition.author | 
 
 

 - Type Reference: Added Target Types PractitionerRole, Organization

 

 | 
 |

 | 
 Composition.confidentiality | 
 
 

 - Change value set from http://terminology.hl7.org/ValueSet/v3-ConfidentialityClassification to http://terminology.hl7.org/ValueSet/v3-ConfidentialityClassification|2014-03-26

 - No longer marked as Modifier

 

 | 
 |

 | 
 Composition.attester.mode | 
 
 

 - Max Cardinality changed from * to 1

 - Change value set from http://hl7.org/fhir/ValueSet/composition-attestation-mode to http://hl7.org/fhir/ValueSet/composition-attestation-mode|4.0.1

 

 | 
 |

 | 
 Composition.attester.party | 
 
 

 - Type Reference: Added Target Types RelatedPerson, PractitionerRole

 

 | 
 |

 | 
 Composition.relatesTo.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/document-relationship-type to http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.1

 

 | 
 |

 | 
 Composition.section.author | 
 
 

 - Added Element

 

 | 
 |

 | 
 Composition.section.focus | 
 
 

 - Added Element

 

 | 
 |

 | 
 Composition.section.mode | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/list-mode to http://hl7.org/fhir/ValueSet/list-mode|4.0.1

 - No longer marked as Modifier

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](composition.diff.xml) or [JSON](composition.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](composition-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Composition](composition-definitions.html#Composition) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A set of resources composed into a single coherent clinical statement with clinical attestation**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](composition-definitions.html#Composition.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Version-independent identifier for the Composition | |

| [status](composition-definitions.html#Composition.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | preliminary | final | amended | entered-in-error
[CompositionStatus](valueset-composition-status.html) ([Required](terminologies.html#required)) | |

| [type](composition-definitions.html#Composition.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of composition (LOINC if possible)
[FHIR Document Type Codes](valueset-doc-typecodes.html) ([Preferred](terminologies.html#preferred)) | |

| [category](composition-definitions.html#Composition.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Categorization of Composition
[Document Class Value Set](valueset-document-classcodes.html) ([Example](terminologies.html#example))
 | |

| [subject](composition-definitions.html#Composition.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Who and/or what the composition is about | |

| [encounter](composition-definitions.html#Composition.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Context of the Composition | |

| [date](composition-definitions.html#Composition.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [dateTime](datatypes.html#dateTime) | Composition editing time | |

| [author](composition-definitions.html#Composition.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Who and/or what authored the composition
 | |

| [title](composition-definitions.html#Composition.title) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [string](datatypes.html#string) | Human Readable name/title | |

| [confidentiality](composition-definitions.html#Composition.confidentiality) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | As defined by affinity domain
[V3 Value SetConfidentialityClassification](v3/ConfidentialityClassification/vs.html) ([Required](terminologies.html#required)) | |

| [attester](composition-definitions.html#Composition.attester) | | 0..* | [BackboneElement](backboneelement.html) | Attests to accuracy of composition
 | |

| [mode](composition-definitions.html#Composition.attester.mode) | | 1..1 | [code](datatypes.html#code) | personal | professional | legal | official
[CompositionAttestationMode](valueset-composition-attestation-mode.html) ([Required](terminologies.html#required)) | |

| [time](composition-definitions.html#Composition.attester.time) | | 0..1 | [dateTime](datatypes.html#dateTime) | When the composition was attested | |

| [party](composition-definitions.html#Composition.attester.party) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Who attested the composition | |

| [custodian](composition-definitions.html#Composition.custodian) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization which maintains the composition | |

| [relatesTo](composition-definitions.html#Composition.relatesTo) | | 0..* | [BackboneElement](backboneelement.html) | Relationships to other compositions/documents
 | |

| [code](composition-definitions.html#Composition.relatesTo.code) | | 1..1 | [code](datatypes.html#code) | replaces | transforms | signs | appends
[DocumentRelationshipType](valueset-document-relationship-type.html) ([Required](terminologies.html#required)) | |

| [target[x]](composition-definitions.html#Composition.relatesTo.target_x_) | | 1..1 | | Target of the relationship | |

| targetIdentifier | | | [Identifier](datatypes.html#Identifier) | | |

| targetReference | | | [Reference](references.html#Reference)([Composition](composition.html)) | | |

| [event](composition-definitions.html#Composition.event) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | The clinical service(s) being documented
 | |

| [code](composition-definitions.html#Composition.event.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Code(s) that apply to the event being documented
[v3 Code System ActCode](v3/ActCode/vs.html) ([Example](terminologies.html#example))
 | |

| [period](composition-definitions.html#Composition.event.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | The period covered by the documentation | |

| [detail](composition-definitions.html#Composition.event.detail) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | The event(s) being documented
 | |

| [section](composition-definitions.html#Composition.section) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Composition is broken into sections
+ Rule: A section must contain at least one of text, entries, or sub-sections
+ Rule: A section can only have an emptyReason if it is empty
 | |

| [title](composition-definitions.html#Composition.section.title) | | 0..1 | [string](datatypes.html#string) | Label for section (e.g. for ToC) | |

| [code](composition-definitions.html#Composition.section.code) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of section (recommended)
[Document Section Codes](valueset-doc-section-codes.html) ([Example](terminologies.html#example)) | |

| [author](composition-definitions.html#Composition.section.author) | | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Who and/or what authored the section
 | |

| [focus](composition-definitions.html#Composition.section.focus) | | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Who/what the section is about, when it is not about the subject of composition | |

| [text](composition-definitions.html#Composition.section.text) | [I](conformance-rules.html#constraints) | 0..1 | [Narrative](narrative.html#Narrative) | Text summary of the section, for human interpretation | |

| [mode](composition-definitions.html#Composition.section.mode) | | 0..1 | [code](datatypes.html#code) | working | snapshot | changes
[ListMode](valueset-list-mode.html) ([Required](terminologies.html#required)) | |

| [orderedBy](composition-definitions.html#Composition.section.orderedBy) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Order of section entries
[List Order Codes](valueset-list-order.html) ([Preferred](terminologies.html#preferred)) | |

| [entry](composition-definitions.html#Composition.section.entry) | [I](conformance-rules.html#constraints) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | A reference to data that supports this section
 | |

| [emptyReason](composition-definitions.html#Composition.section.emptyReason) | [I](conformance-rules.html#constraints) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why the section is empty
[List Empty Reasons](valueset-list-empty-reason.html) ([Preferred](terminologies.html#preferred)) | |

| [section](composition-definitions.html#Composition.section.section) | [I](conformance-rules.html#constraints) | 0..* | see [section](#Composition.section) | Nested Section
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Composition ([DomainResource](domainresource.html))[A version-independent identifier for the Composition. This identifier stays constant as the composition is changed over timeidentifier](composition-definitions.html#Composition.identifier) : [Identifier](datatypes.html#Identifier) [0..1][The workflow/clinical status of this composition. The status is a marker for the clinical standing of the document (this element modifies the meaning of other elements)status](composition-definitions.html#Composition.status) : [code](datatypes.html#code) [1..1] « [The workflow/clinical status of the composition. (Strength=Required)CompositionStatus](valueset-composition-status.html)! »[Specifies the particular kind of composition (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the compositiontype](composition-definitions.html#Composition.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Type of a composition. (Strength=Preferred)FHIRDocumentTypeCodes](valueset-doc-typecodes.html)? »[A categorization for the type of the composition - helps for indexing and searching. This may be implied by or derived from the code specified in the Composition Typecategory](composition-definitions.html#Composition.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [High-level kind of a clinical document at a macro level. (Strength=Example)DocumentClassValueSet](valueset-document-classcodes.html)?? »[Who or what the composition is about. The composition can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of livestock, or a set of patients that share a common exposure)subject](composition-definitions.html#Composition.subject) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[Describes the clinical encounter or type of care this documentation is associated withencounter](composition-definitions.html#Composition.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[The composition editing time, when the composition was last logically changed by the authordate](composition-definitions.html#Composition.date) : [dateTime](datatypes.html#dateTime) [1..1][Identifies who is responsible for the information in the composition, not necessarily who typed it inauthor](composition-definitions.html#Composition.author) : [Reference](references.html#Reference) [1..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)| [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »[Official human-readable label for the compositiontitle](composition-definitions.html#Composition.title) : [string](datatypes.html#string) [1..1][The code specifying the level of confidentiality of the Compositionconfidentiality](composition-definitions.html#Composition.confidentiality) : [code](datatypes.html#code) [0..1] « [Codes specifying the level of confidentiality of the composition. (Strength=Required)v3.ConfidentialityClassificat...](v3/ConfidentialityClassification/vs.html)! »[Identifies the organization or group who is responsible for ongoing maintenance of and access to the composition/document informationcustodian](composition-definitions.html#Composition.custodian) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »Attester[The type of attestation the authenticator offersmode](composition-definitions.html#Composition.attester.mode) : [code](datatypes.html#code) [1..1] « [The way in which a person authenticated a composition. (Strength=Required)CompositionAttestationMode](valueset-composition-attestation-mode.html)! »[When the composition was attested by the partytime](composition-definitions.html#Composition.attester.time) : [dateTime](datatypes.html#dateTime) [0..1][Who attested the composition in the specified wayparty](composition-definitions.html#Composition.attester.party) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)| [PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization) »RelatesTo[The type of relationship that this composition has with anther composition or documentcode](composition-definitions.html#Composition.relatesTo.code) : [code](datatypes.html#code) [1..1] « [The type of relationship between documents. (Strength=Required)DocumentRelationshipType](valueset-document-relationship-type.html)! »[The target composition/document of this relationshiptarget[x]](composition-definitions.html#Composition.relatesTo.target_x_) : [Type](formats.html#umlchoice) [1..1] « [Identifier](datatypes.html#Identifier)|[Reference](references.html#Reference)([Composition](composition.html#Composition)) »Event[This list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the typeCode, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actcode](composition-definitions.html#Composition.event.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [This list of codes represents the main clinical acts being documented. (Strength=Example)v3.ActCode](v3/ActCode/vs.html)?? »[The period of time covered by the documentation. There is no assertion that the documentation is a complete representation for this period, only that it documents events during this timeperiod](composition-definitions.html#Composition.event.period) : [Period](datatypes.html#Period) [0..1][The description and/or reference of the event(s) being documented. For example, this could be used to document such a colonoscopy or an appendectomydetail](composition-definitions.html#Composition.event.detail) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »Section[The label for this particular section. This will be part of the rendered content for the document, and is often used to build a table of contentstitle](composition-definitions.html#Composition.section.title) : [string](datatypes.html#string) [0..1][A code identifying the kind of content contained within the section. This must be consistent with the section titlecode](composition-definitions.html#Composition.section.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Classification of a section of a composition/document. (Strength=Example)DocumentSectionCodes](valueset-doc-section-codes.html)?? »[Identifies who is responsible for the information in this section, not necessarily who typed it inauthor](composition-definitions.html#Composition.section.author) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)| [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization) »[The actual focus of the section when it is not the subject of the composition, but instead represents something or someone associated with the subject such as (for a patient subject) a spouse, parent, fetus, or donor. If not focus is specified, the focus is assumed to be focus of the parent section, or, for a section in the Composition itself, the subject of the composition. Sections with a focus SHALL only include resources where the logical subject (patient, subject, focus, etc.) matches the section focus, or the resources have no logical subject (few resources)focus](composition-definitions.html#Composition.section.focus) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[A human-readable narrative that contains the attested content of the section, used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrativetext](composition-definitions.html#Composition.section.text) : [Narrative](narrative.html#Narrative) [0..1][How the entry list was prepared - whether it is a working list that is suitable for being maintained on an ongoing basis, or if it represents a snapshot of a list of items from another source, or whether it is a prepared list where items may be marked as added, modified or deletedmode](composition-definitions.html#Composition.section.mode) : [code](datatypes.html#code) [0..1] « [The processing mode that applies to this section. (Strength=Required)ListMode](valueset-list-mode.html)! »[Specifies the order applied to the items in the section entriesorderedBy](composition-definitions.html#Composition.section.orderedBy) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [What order applies to the items in the entry. (Strength=Preferred)ListOrderCodes](valueset-list-order.html)? »[A reference to the actual resource from which the narrative in the section is derivedentry](composition-definitions.html#Composition.section.entry) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[If the section is empty, why the list is empty. An empty section typically has some text explaining the empty reasonemptyReason](composition-definitions.html#Composition.section.emptyReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [If a section is empty, why it is empty. (Strength=Preferred)ListEmptyReasons](valueset-list-empty-reason.html)? »
[A participant who has attested to the accuracy of the composition/documentattester](composition-definitions.html#Composition.attester)[0..*][Relationships that this composition has with other compositions or documents that already existrelatesTo](composition-definitions.html#Composition.relatesTo)[0..*][The clinical service, such as a colonoscopy or an appendectomy, being documentedevent](composition-definitions.html#Composition.event)[0..*][A nested sub-section within this sectionsection](composition-definitions.html#Composition.section.section)[0..*][The root of the sections that make up the compositionsection](composition-definitions.html#Composition.section)[0..*]
 

**XML Template**

 

 
```
<[**Composition**](composition-definitions.html#Composition) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](composition-definitions.html#Composition.identifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Version-independent identifier for the Composition](terminologies.html#unbound) --></identifier>
 <[**status**](composition-definitions.html#Composition.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [preliminary | final | amended | entered-in-error](valueset-composition-status.html) -->
 <[**type**](composition-definitions.html#Composition.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of composition (LOINC if possible)](valueset-doc-typecodes.html) --></type>
 <[**category**](composition-definitions.html#Composition.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Categorization of Composition](valueset-document-classcodes.html) --></category>
 <[**subject**](composition-definitions.html#Composition.subject)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Who and/or what the composition is about](terminologies.html#unbound) --></subject>
 <[**encounter**](composition-definitions.html#Composition.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Context of the Composition](terminologies.html#unbound) --></encounter>
 <[**date**](composition-definitions.html#Composition.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **1..1** [Composition editing time](terminologies.html#unbound) -->
 <[**author**](composition-definitions.html#Composition.author)><!-- **1..*** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Who and/or what authored the composition](terminologies.html#unbound) --></author>
 <[**title**](composition-definitions.html#Composition.title) value="[[string](datatypes.html#string)]"/><!-- **1..1** [Human Readable name/title](terminologies.html#unbound) -->
 <[**confidentiality**](composition-definitions.html#Composition.confidentiality) value="[[code](datatypes.html#code)]"/><!-- **0..1** [As defined by affinity domain](v3/ConfidentialityClassification/vs.html) -->
 <[**attester**](composition-definitions.html#Composition.attester)> <!-- **0..*** Attests to accuracy of composition -->
 <[**mode**](composition-definitions.html#Composition.attester.mode) value="[[code](datatypes.html#code)]"/><!-- **1..1** [personal | professional | legal | official](valueset-composition-attestation-mode.html) -->
 <[**time**](composition-definitions.html#Composition.attester.time) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When the composition was attested](terminologies.html#unbound) -->
 <[**party**](composition-definitions.html#Composition.attester.party)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Organization](organization.html#Organization)) [Who attested the composition](terminologies.html#unbound) --></party>
 </attester>
 <[**custodian**](composition-definitions.html#Composition.custodian)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization which maintains the composition](terminologies.html#unbound) --></custodian>
 <[**relatesTo**](composition-definitions.html#Composition.relatesTo)> <!-- **0..*** Relationships to other compositions/documents -->
 <[**code**](composition-definitions.html#Composition.relatesTo.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [replaces | transforms | signs | appends](valueset-document-relationship-type.html) -->
 <[**target[x]**](composition-definitions.html#Composition.relatesTo.target[x])><!-- **1..1** [Identifier](datatypes.html#Identifier)|[Reference](references.html#Reference)([Composition](composition.html#Composition)) [Target of the relationship](terminologies.html#unbound) --></target[x]>
 </relatesTo>
 <[**event**](composition-definitions.html#Composition.event)> <!-- **0..*** The clinical service(s) being documented -->
 <[**code**](composition-definitions.html#Composition.event.code)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Code(s) that apply to the event being documented](v3/ActCode/vs.html) --></code>
 <[**period**](composition-definitions.html#Composition.event.period)><!-- **0..1** [Period](datatypes.html#Period) [The period covered by the documentation](terminologies.html#unbound) --></period>
 <[**detail**](composition-definitions.html#Composition.event.detail)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [The event(s) being documented](terminologies.html#unbound) --></detail>
 </event>
 <[**section**](composition-definitions.html#Composition.section)> <!-- **0..*** Composition is broken into sections -->
 <[**title**](composition-definitions.html#Composition.section.title) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Label for section (e.g. for ToC)](terminologies.html#unbound) -->
 <[**code**](composition-definitions.html#Composition.section.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Classification of section (recommended)](valueset-doc-section-codes.html) --></code>
 <[**author**](composition-definitions.html#Composition.section.author)><!-- **0..*** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) [Who and/or what authored the section](terminologies.html#unbound) --></author>
 <[**focus**](composition-definitions.html#Composition.section.focus)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Who/what the section is about, when it is not about the subject of composition](terminologies.html#unbound) --></focus>
 <[**text**](composition-definitions.html#Composition.section.text)><!-- ** 0..1** [Narrative](narrative.html#Narrative) [Text summary of the section, for human interpretation](terminologies.html#unbound) --></text>
 <[**mode**](composition-definitions.html#Composition.section.mode) value="[[code](datatypes.html#code)]"/><!-- **0..1** [working | snapshot | changes](valueset-list-mode.html) -->
 <[**orderedBy**](composition-definitions.html#Composition.section.orderedBy)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Order of section entries](valueset-list-order.html) --></orderedBy>
 <[**entry**](composition-definitions.html#Composition.section.entry)><!-- ** 0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [A reference to data that supports this section](terminologies.html#unbound) --></entry>
 <[**emptyReason**](composition-definitions.html#Composition.section.emptyReason)><!-- ** 0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Why the section is empty](valueset-list-empty-reason.html) --></emptyReason>
 <[**section**](composition-definitions.html#Composition.section.section)><!-- ** 0..*** Content as for Composition.section [Nested Section](terminologies.html#unbound) --></section>
 </section>
</Composition>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Composition**](composition-definitions.html#Composition)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](composition-definitions.html#Composition.identifier)" : { [Identifier](datatypes.html#Identifier) }, // [Version-independent identifier for the Composition](terminologies.html#unbound)
 "[status](composition-definitions.html#Composition.status)" : "<[code](datatypes.html#code)>", // **R!** [preliminary | final | amended | entered-in-error](valueset-composition-status.html)
 "[type](composition-definitions.html#Composition.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Kind of composition (LOINC if possible)](valueset-doc-typecodes.html)
 "[category](composition-definitions.html#Composition.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Categorization of Composition](valueset-document-classcodes.html)
 "[subject](composition-definitions.html#Composition.subject)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Who and/or what the composition is about](terminologies.html#unbound)
 "[encounter](composition-definitions.html#Composition.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Context of the Composition](terminologies.html#unbound)
 "[date](composition-definitions.html#Composition.date)" : "<[dateTime](datatypes.html#dateTime)>", // **R!** [Composition editing time](terminologies.html#unbound)
 "[author](composition-definitions.html#Composition.author)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) }], // **R!** [Who and/or what authored the composition](terminologies.html#unbound)
 "[title](composition-definitions.html#Composition.title)" : "<[string](datatypes.html#string)>", // **R!** [Human Readable name/title](terminologies.html#unbound)
 "[confidentiality](composition-definitions.html#Composition.confidentiality)" : "<[code](datatypes.html#code)>", // [As defined by affinity domain](v3/ConfidentialityClassification/vs.html)
 "[attester](composition-definitions.html#Composition.attester)" : [{ // [Attests to accuracy of composition](terminologies.html#unbound)
 "[mode](composition-definitions.html#Composition.attester.mode)" : "<[code](datatypes.html#code)>", // **R!** [personal | professional | legal | official](valueset-composition-attestation-mode.html)
 "[time](composition-definitions.html#Composition.attester.time)" : "<[dateTime](datatypes.html#dateTime)>", // [When the composition was attested](terminologies.html#unbound)
 "[party](composition-definitions.html#Composition.attester.party)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [Organization](organization.html#Organization)) } // [Who attested the composition](terminologies.html#unbound)
 }],
 "[custodian](composition-definitions.html#Composition.custodian)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization which maintains the composition](terminologies.html#unbound)
 "[relatesTo](composition-definitions.html#Composition.relatesTo)" : [{ // [Relationships to other compositions/documents](terminologies.html#unbound)
 "[code](composition-definitions.html#Composition.relatesTo.code)" : "<[code](datatypes.html#code)>", // **R!** [replaces | transforms | signs | appends](valueset-document-relationship-type.html)
 // target[x]: Target of the relationship. One of these 2:
 "[targetIdentifier](composition-definitions.html#Composition.relatesTo.targetIdentifier)" : { [Identifier](datatypes.html#Identifier) }
 "[targetReference](composition-definitions.html#Composition.relatesTo.targetReference)" : { [Reference](references.html#Reference)([Composition](composition.html#Composition)) }
 }],
 "[event](composition-definitions.html#Composition.event)" : [{ // [The clinical service(s) being documented](terminologies.html#unbound)
 "[code](composition-definitions.html#Composition.event.code)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Code(s) that apply to the event being documented](v3/ActCode/vs.html)
 "[period](composition-definitions.html#Composition.event.period)" : { [Period](datatypes.html#Period) }, // [The period covered by the documentation](terminologies.html#unbound)
 "[detail](composition-definitions.html#Composition.event.detail)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }] // [The event(s) being documented](terminologies.html#unbound)
 }],
 "[section](composition-definitions.html#Composition.section)" : [{ // [Composition is broken into sections](terminologies.html#unbound)
 "[title](composition-definitions.html#Composition.section.title)" : "<[string](datatypes.html#string)>", // [Label for section (e.g. for ToC)](terminologies.html#unbound)
 "[code](composition-definitions.html#Composition.section.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Classification of section (recommended)](valueset-doc-section-codes.html)
 "[author](composition-definitions.html#Composition.section.author)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) }], // [Who and/or what authored the section](terminologies.html#unbound)
 "[focus](composition-definitions.html#Composition.section.focus)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Who/what the section is about, when it is not about the subject of composition](terminologies.html#unbound)
 "[text](composition-definitions.html#Composition.section.text)" : { [Narrative](narrative.html#Narrative) }, // **C?** [Text summary of the section, for human interpretation](terminologies.html#unbound)
 "[mode](composition-definitions.html#Composition.section.mode)" : "<[code](datatypes.html#code)>", // [working | snapshot | changes](valueset-list-mode.html)
 "[orderedBy](composition-definitions.html#Composition.section.orderedBy)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Order of section entries](valueset-list-order.html)
 "[entry](composition-definitions.html#Composition.section.entry)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // **C?** [A reference to data that supports this section](terminologies.html#unbound)
 "[emptyReason](composition-definitions.html#Composition.section.emptyReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **C?** [Why the section is empty](valueset-list-empty-reason.html)
 "[section](composition-definitions.html#Composition.section.section)" : [{ Content as for Composition.section }] // **C?** [Nested Section](terminologies.html#unbound)
 }]
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Composition**](composition-definitions.html#Composition);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Composition.identifier](composition-definitions.html#Composition.identifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Version-independent identifier for the Composition
 fhir:[Composition.status](composition-definitions.html#Composition.status) [ [code](datatypes.html#code) ]; # 1..1 preliminary | final | amended | entered-in-error
 fhir:[Composition.type](composition-definitions.html#Composition.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Kind of composition (LOINC if possible)
 fhir:[Composition.category](composition-definitions.html#Composition.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Categorization of Composition
 fhir:[Composition.subject](composition-definitions.html#Composition.subject) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Who and/or what the composition is about
 fhir:[Composition.encounter](composition-definitions.html#Composition.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Context of the Composition
 fhir:[Composition.date](composition-definitions.html#Composition.date) [ [dateTime](datatypes.html#dateTime) ]; # 1..1 Composition editing time
 fhir:[Composition.author](composition-definitions.html#Composition.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ], ... ; # 1..* Who and/or what authored the composition
 fhir:[Composition.title](composition-definitions.html#Composition.title) [ [string](datatypes.html#string) ]; # 1..1 Human Readable name/title
 fhir:[Composition.confidentiality](composition-definitions.html#Composition.confidentiality) [ [code](datatypes.html#code) ]; # 0..1 As defined by affinity domain
 fhir:[Composition.attester](composition-definitions.html#Composition.attester) [ # 0..* Attests to accuracy of composition
 fhir:[Composition.attester.mode](composition-definitions.html#Composition.attester.mode) [ [code](datatypes.html#code) ]; # 1..1 personal | professional | legal | official
 fhir:[Composition.attester.time](composition-definitions.html#Composition.attester.time) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the composition was attested
 fhir:[Composition.attester.party](composition-definitions.html#Composition.attester.party) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 0..1 Who attested the composition
 ], ...;
 fhir:[Composition.custodian](composition-definitions.html#Composition.custodian) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization which maintains the composition
 fhir:[Composition.relatesTo](composition-definitions.html#Composition.relatesTo) [ # 0..* Relationships to other compositions/documents
 fhir:[Composition.relatesTo.code](composition-definitions.html#Composition.relatesTo.code) [ [code](datatypes.html#code) ]; # 1..1 replaces | transforms | signs | appends
 # [Composition.relatesTo.target[x]](composition-definitions.html#Composition.relatesTo.target[x]) : 1..1 Target of the relationship. One of these 2
 fhir:[Composition.relatesTo.targetIdentifier](composition-definitions.html#Composition.relatesTo.targetIdentifier) [ [Identifier](datatypes.html#Identifier) ]
 fhir:[Composition.relatesTo.targetReference](composition-definitions.html#Composition.relatesTo.targetReference) [ [Reference](references.html#Reference)([Composition](composition.html#Composition)) ]
 ], ...;
 fhir:[Composition.event](composition-definitions.html#Composition.event) [ # 0..* The clinical service(s) being documented
 fhir:[Composition.event.code](composition-definitions.html#Composition.event.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Code(s) that apply to the event being documented
 fhir:[Composition.event.period](composition-definitions.html#Composition.event.period) [ [Period](datatypes.html#Period) ]; # 0..1 The period covered by the documentation
 fhir:[Composition.event.detail](composition-definitions.html#Composition.event.detail) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* The event(s) being documented
 ], ...;
 fhir:[Composition.section](composition-definitions.html#Composition.section) [ # 0..* Composition is broken into sections
 fhir:[Composition.section.title](composition-definitions.html#Composition.section.title) [ [string](datatypes.html#string) ]; # 0..1 Label for section (e.g. for ToC)
 fhir:[Composition.section.code](composition-definitions.html#Composition.section.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Classification of section (recommended)
 fhir:[Composition.section.author](composition-definitions.html#Composition.section.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Organization](organization.html#Organization)) ], ... ; # 0..* Who and/or what authored the section
 fhir:[Composition.section.focus](composition-definitions.html#Composition.section.focus) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Who/what the section is about, when it is not about the subject of composition
 fhir:[Composition.section.text](composition-definitions.html#Composition.section.text) [ [Narrative](narrative.html#Narrative) ]; # 0..1 Text summary of the section, for human interpretation
 fhir:[Composition.section.mode](composition-definitions.html#Composition.section.mode) [ [code](datatypes.html#code) ]; # 0..1 working | snapshot | changes
 fhir:[Composition.section.orderedBy](composition-definitions.html#Composition.section.orderedBy) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Order of section entries
 fhir:[Composition.section.entry](composition-definitions.html#Composition.section.entry) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* A reference to data that supports this section
 fhir:[Composition.section.emptyReason](composition-definitions.html#Composition.section.emptyReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Why the section is empty
 fhir:[Composition.section.section](composition-definitions.html#Composition.section.section) [ [See Composition.section](#ttl-Composition.section) ], ... ; # 0..* Nested Section
 ], ...;
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Composition](composition.html#Composition)
 | 
 | 
 |

 | 
 Composition.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/composition-status to http://hl7.org/fhir/ValueSet/composition-status|4.0.1

 

 | 
 |

 | 
 Composition.category | 
 
 

 - Renamed from class to category

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 Composition.subject | 
 
 

 - Min Cardinality changed from 1 to 0

 

 | 
 |

 | 
 Composition.author | 
 
 

 - Type Reference: Added Target Types PractitionerRole, Organization

 

 | 
 |

 | 
 Composition.confidentiality | 
 
 

 - Change value set from http://terminology.hl7.org/ValueSet/v3-ConfidentialityClassification to http://terminology.hl7.org/ValueSet/v3-ConfidentialityClassification|2014-03-26

 - No longer marked as Modifier

 

 | 
 |

 | 
 Composition.attester.mode | 
 
 

 - Max Cardinality changed from * to 1

 - Change value set from http://hl7.org/fhir/ValueSet/composition-attestation-mode to http://hl7.org/fhir/ValueSet/composition-attestation-mode|4.0.1

 

 | 
 |

 | 
 Composition.attester.party | 
 
 

 - Type Reference: Added Target Types RelatedPerson, PractitionerRole

 

 | 
 |

 | 
 Composition.relatesTo.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/document-relationship-type to http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.1

 

 | 
 |

 | 
 Composition.section.author | 
 
 

 - Added Element

 

 | 
 |

 | 
 Composition.section.focus | 
 
 

 - Added Element

 

 | 
 |

 | 
 Composition.section.mode | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/list-mode to http://hl7.org/fhir/ValueSet/list-mode|4.0.1

 - No longer marked as Modifier

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](composition.diff.xml) or [JSON](composition.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](composition-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

 

 

 

See the [Profiles & Extensions](composition-profiles.html) and the alternate definitions:
Master Definition [XML](composition.profile.xml.html) + [JSON](composition.profile.json.html),
[XML](xml.html) [Schema](composition.xsd)/[Schematron](composition.sch) + [JSON](json.html) 
[Schema](composition.schema.json.html), [ShEx](composition.shex.html) (for [Turtle](rdf.html)) + [see the extensions](composition-profiles.html) & the [dependency analysis](composition-dependencies.html)

### 2.41.4.1 
Terminology Bindings
 [
](composition.html#tx)

 | Path | Definition | Type | Reference | |

 | Composition.status | The workflow/clinical status of the composition. | [Required](terminologies.html#required) | [CompositionStatus](valueset-composition-status.html) | |

 | Composition.type | Type of a composition. | [Preferred](terminologies.html#preferred) | [FHIRDocumentTypeCodes](valueset-doc-typecodes.html) | |

 | Composition.category | High-level kind of a clinical document at a macro level. | [Example](terminologies.html#example) | [DocumentClassValueSet](valueset-document-classcodes.html) | |

 | Composition.confidentiality | Codes specifying the level of confidentiality of the composition. | [Required](terminologies.html#required) | [v3.ConfidentialityClassification](v3/ConfidentialityClassification/vs.html) | |

 | Composition.attester.mode | The way in which a person authenticated a composition. | [Required](terminologies.html#required) | [CompositionAttestationMode](valueset-composition-attestation-mode.html) | |

 | Composition.relatesTo.code | The type of relationship between documents. | [Required](terminologies.html#required) | [DocumentRelationshipType](valueset-document-relationship-type.html) | |

 | Composition.event.code | This list of codes represents the main clinical acts being documented. | [Example](terminologies.html#example) | [v3.ActCode](v3/ActCode/vs.html) | |

 | Composition.section.code | Classification of a section of a composition/document. | [Example](terminologies.html#example) | [DocumentSectionCodes](valueset-doc-section-codes.html) | |

 | Composition.section.mode | The processing mode that applies to this section. | [Required](terminologies.html#required) | [ListMode](valueset-list-mode.html) | |

 | Composition.section.orderedBy | What order applies to the items in the entry. | [Preferred](terminologies.html#preferred) | [ListOrderCodes](valueset-list-order.html) | |

 | Composition.section.emptyReason | If a section is empty, why it is empty. | [Preferred](terminologies.html#preferred) | [ListEmptyReasons](valueset-list-empty-reason.html) | |

 

 

### 2.41.4.2 Constraints [
](composition.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **cmp-1** | [Rule](conformance-rules.html#rule) | Composition.section | A section must contain at least one of text, entries, or sub-sections | text.exists() or entry.exists() or section.exists() | |
| **cmp-2** | [Rule](conformance-rules.html#rule) | Composition.section | A section can only have an emptyReason if it is empty | emptyReason.empty() or entry.empty() | |

## 2.41.5 
Notes:
 [](composition.html#notes)

 
 - The author and the attester are often the same person, but this might not be the case in some clinical workflows.

 - The attester attests contents of the document resource, the subject resource and the resources referred to 
 in the Composition.section.content references. Because documents are often derived Compositions and the attestation
 from the composition is held to apply to the document, the method for [presenting a document](documents.html#presentation)
 should be used when/if attesters review the content of the composition.
 

 - The custodian is responsible for the maintenance of the composition and any documents derived from it. With regard to the documents, they are 
 responsible for the policy regarding persistence of the documents. Although they need not actually retain a copy of the document, they SHOULD do so.
 

 - It is acceptable for a Composition to contain only narrative (`Composition.section.text`) and no entries (`Composition.section.entry`)

 

## 2.41.6 
Compositions about multiple entities
 [](composition.html#mixed)

Typically, a composition is made about the subject - e.g. a patient, or group of patients, location, or device - and the 
distinction between the subject and the composition describes the subject. Some kinds of documents contain data about other 
parties or entities that are relevant to the subject of the document. Some examples:

 - A neonatal discharge summary that contains information about the mother

 - A family history document that contains multiple sections for different family members

 - A social health evaluation document that contains information about the patient's family members

 - A procedure report that contains details about a device implanted in the patient

In all these cases, the subject of the document is a single patient, but some of the details are actually
related to other persons or entities. When this happens, these other entities are detailed in the `Composition.section.focus` element.
In the absence of a `focus`, it is assumed that the `subject` of the composition is the focus. 

If a `focus` is specified, then the resources referred to from the section SHALL 
either:

 - specify that their `subject` (however named e.g. `patient`) or `focus` element (if present) is the focus indicated

 - not have a `subject` element

A few compositions genuinely cover multiple subjects - different sections are about different subjects. In such
case, `Composition.subject` is omitted, and the extension [section-subject](extension-composition-section-subject.html)
is used on each section to indicate the subject.

**
Trial-Use Note:**
Feedback is welcome on two issues related to Composition:

 - For many compositions, the title is the same as the text or a display name of Composition.type (e.g., a "consultation" or "progress note"). Note that [CDA ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) does not make title mandatory, but there are no known cases where it is useful for title to be omitted, so it is mandatory here during the trial use period.

 - A client can ask a server to generate a fully bundled document from a Composition resource using the $snapshot operation. This operation definition does not resolve the question how document signatures are created. This is an open issue during the period of trial use, and feedback is requested regarding this question.

Feedback [here ](http://hl7.org/fhir-issues).

## 2.41.7 Search Parameters [
](composition.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| attester | [reference](search.html#reference) | Who attested the composition | Composition.attester.party
([Practitioner](practitioner.html), [Organization](organization.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| author | [reference](search.html#reference) | Who and/or what authored the composition | Composition.author
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| category | [token](search.html#token) | Categorization of Composition | Composition.category | | |

| confidentiality | [token](search.html#token) | As defined by affinity domain | Composition.confidentiality | | |

| context | [token](search.html#token) | Code(s) that apply to the event being documented | Composition.event.code | | |

| date | [date](search.html#date) | Composition editing time | Composition.date | [17 Resources](searchparameter-registry.html#clinical-date) | |

| encounter | [reference](search.html#reference) | Context of the Composition | Composition.encounter
([Encounter](encounter.html)) | [12 Resources](searchparameter-registry.html#clinical-encounter) | |

| entry | [reference](search.html#reference) | A reference to data that supports this section | Composition.section.entry
(Any) | | |

| identifier | [token](search.html#token) | Version-independent identifier for the Composition | Composition.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| patient | [reference](search.html#reference) | Who and/or what the composition is about | Composition.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| period | [date](search.html#date) | The period covered by the documentation | Composition.event.period | | |

| related-id | [token](search.html#token) | Target of the relationship | (Composition.relatesTo.target as Identifier) | | |

| related-ref | [reference](search.html#reference) | Target of the relationship | (Composition.relatesTo.target as Reference)
([Composition](composition.html)) | | |

| section | [token](search.html#token) | Classification of section (recommended) | Composition.section.code | | |

| status | [token](search.html#token) | preliminary | final | amended | entered-in-error | Composition.status | | |

| subject | [reference](search.html#reference) | Who and/or what the composition is about | Composition.subject
(Any) | | |

| title | [string](search.html#string) | Human Readable name/title | Composition.title | | |

| type | [token](search.html#token) | Kind of composition (LOINC if possible) | Composition.type | [5 Resources](searchparameter-registry.html#clinical-type) | |