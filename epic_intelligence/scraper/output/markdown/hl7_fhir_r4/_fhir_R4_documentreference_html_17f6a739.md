# DocumentReference - FHIR v4.0.1Document identifier as assigned by the source of the document. This identifier is specific to this version of the document. This unique identifier may be used elsewhere to identify this version of the documentOther identifiers associated with the document, including version independent identifiersThe status of this document reference (this element modifies the meaning of other elements)The status of the document reference. (Strength=Required)The status of the underlying documentStatus of the underlying document. (Strength=Required)Specifies the particular kind of document referenced  (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the document referencedPrecise type of clinical document. (Strength=Preferred)A categorization for the type of document referenced - helps for indexing and searching. This may be implied by or derived from the code specified in the DocumentReference.typeHigh-level kind of a clinical document at a macro level. (Strength=Example)Who or what the document is about. The document can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of farm animals, or a set of patients that share a common exposure)When the document reference was createdIdentifies who is responsible for adding the information to the documentWhich person or organization authenticates that this document is validIdentifies the organization or group who is responsible for ongoing maintenance of and access to the documentHuman-readable description of the source documentA set of Security-Tag codes specifying the level of privacy/security of the Document. Note that DocumentReference.meta.security contains the security labels of the "reference" to the document, while DocumentReference.securityLabel contains a snapshot of the security labels on the document the reference refers toSecurity Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)The type of relationship that this document has with anther documentThe type of relationship between documents. (Strength=Required)The target document of this relationshipThe document or URL of the document along with critical metadata to prove content has integrityAn identifier of the document encoding, structure, and template that the document conforms to beyond the base format indicated in the mimeTypeDocument Format Codes. (Strength=Preferred)Describes the clinical encounter or type of care that the document content is associated withThis list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the type Code, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actThis list of codes represents the main clinical acts being documented. (Strength=Example)The time period over which the service that is described by the document was providedThe kind of facility where the patient was seenXDS Facility Type. (Strength=Example)This property may convey specifics about the practice setting where the content was created, often reflecting the clinical specialtyAdditional details about where the content was created (e.g. clinical specialty). (Strength=Example)The Patient Information as known when the document was published. May be a reference to a version specific, or containedRelated identifiers or resources associated with the DocumentReferenceRelationships that this document has with other document references that already existThe document and format referenced. There may be multiple content element repetitions, each with a different formatThe clinical context in which the document was preparedDocument identifier as assigned by the source of the document. This identifier is specific to this version of the document. This unique identifier may be used elsewhere to identify this version of the documentOther identifiers associated with the document, including version independent identifiersThe status of this document reference (this element modifies the meaning of other elements)The status of the document reference. (Strength=Required)The status of the underlying documentStatus of the underlying document. (Strength=Required)Specifies the particular kind of document referenced  (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the document referencedPrecise type of clinical document. (Strength=Preferred)A categorization for the type of document referenced - helps for indexing and searching. This may be implied by or derived from the code specified in the DocumentReference.typeHigh-level kind of a clinical document at a macro level. (Strength=Example)Who or what the document is about. The document can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of farm animals, or a set of patients that share a common exposure)When the document reference was createdIdentifies who is responsible for adding the information to the documentWhich person or organization authenticates that this document is validIdentifies the organization or group who is responsible for ongoing maintenance of and access to the documentHuman-readable description of the source documentA set of Security-Tag codes specifying the level of privacy/security of the Document. Note that DocumentReference.meta.security contains the security labels of the "reference" to the document, while DocumentReference.securityLabel contains a snapshot of the security labels on the document the reference refers toSecurity Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)The type of relationship that this document has with anther documentThe type of relationship between documents. (Strength=Required)The target document of this relationshipThe document or URL of the document along with critical metadata to prove content has integrityAn identifier of the document encoding, structure, and template that the document conforms to beyond the base format indicated in the mimeTypeDocument Format Codes. (Strength=Preferred)Describes the clinical encounter or type of care that the document content is associated withThis list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the type Code, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actThis list of codes represents the main clinical acts being documented. (Strength=Example)The time period over which the service that is described by the document was providedThe kind of facility where the patient was seenXDS Facility Type. (Strength=Example)This property may convey specifics about the practice setting where the content was created, often reflecting the clinical specialtyAdditional details about where the content was created (e.g. clinical specialty). (Strength=Example)The Patient Information as known when the document was published. May be a reference to a version specific, or containedRelated identifiers or resources associated with the DocumentReferenceRelationships that this document has with other document references that already existThe document and format referenced. There may be multiple content element repetitions, each with a different formatThe clinical context in which the document was prepared

> Source: https://hl7.org/fhir/R4/documentreference.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/documentreference.html) [R4B](http://hl7.org/fhir/R4B/documentreference.html) **R4** [R3](http://hl7.org/fhir/STU3/documentreference.html) [R2](http://hl7.org/fhir/DSTU2/documentreference.html)
 

# 2.42 Resource DocumentReference - Content [
](documentreference.html#2.42)

| [Structured Documents ](http://www.hl7.org/Special/committees/structure/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Not Classified | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.

## 2.42.1 Scope and Usage [
](documentreference.html#scope)

 
A DocumentReference resource is used to index a document, clinical note, and other binary objects 
to make them available to a healthcare system. 
A document is some sequence of bytes that is identifiable, establishes its own context (e.g., what subject, 
author, etc. can be displayed to the user), and has defined update management. The DocumentReference resource can be 
used with any document format that has a recognized mime type and that conforms to this definition.

Typically, DocumentReference resources are used in document indexing systems, such as [IHE XDS ](http://wiki.ihe.net/index.php?title=Cross-Enterprise_Document_Sharing),
such as profiled in [IHE Mobile access to Health Documents ](http://wiki.ihe.net/index.php/Mobile_access_to_Health_Documents_(MHD)).

DocumentReference is metadata describing a document such as:

 - [CDA ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) documents in FHIR systems

 - [FHIR documents](documents.html) stored elsewhere (i.e. registry/repository following the XDS model)

 - [PDF documents ](http://en.wikipedia.org/wiki/Portable_Document_Format), Scanned Paper, and digital records of faxes

 - Clinical Notes in various forms

 - Image files (e.g., JPEG, GIF, TIFF)

 - Non-Standard formats (e.g., WORD)

 - Other kinds of documents, such as records of prescriptions or immunizations
 

## 2.42.2 Boundaries and Relationships [
](documentreference.html#bnr)

FHIR defines both a [document format](documents.html) and this document reference. FHIR documents are for documents 
that are authored and assembled in FHIR. This resource is mainly intended for general references to assembled documents. 

The document that is a target of the reference can be a reference to a FHIR document served by another server, or 
the target can be stored in the special [FHIR Binary Resource](http.html#binary), or the target can be 
stored on some other server system. The document reference is also able to address documents that are retrieved 
by a service call such as an XDS.b RetrieveDocumentSet, or a DICOM exchange, or an [HL7 v2 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) message query - though 
the way each of these service calls works must be specified in some external standard or other documentation.

A `DocumentReference` describes some other document. This means that there are two sets of 
provenance information relevant here: the provenance of the document, and the provenance of the document
reference. Sometimes, the provenance information is closely related, as when the document producer also 
produces the document reference, but in other workflows, the document reference is generated later by
other actors. In the `DocumentReference` resource, the [meta](resource.html#Meta)
content refers to the provenance of the reference itself, while the content described below concerns
the document it references. Like all resources, there is overlap between the information in the 
resource directly, and in the general [Provenance](provenance.html) resource. This is 
discussed as [part of the description of the Provenance resource](provenance.html#overlap).

This resource is referenced by [AdverseEvent](adverseevent.html#AdverseEvent), [CarePlan](careplan.html#CarePlan), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), itself, [FamilyMemberHistory](familymemberhistory.html#FamilyMemberHistory), [GuidanceResponse](guidanceresponse.html#GuidanceResponse), [ImagingStudy](imagingstudy.html#ImagingStudy), [MedicationKnowledge](medicationknowledge.html#MedicationKnowledge), [MedicinalProduct](medicinalproduct.html#MedicinalProduct), [Observation](observation.html#Observation), [Procedure](procedure.html#Procedure), [RequestGroup](requestgroup.html#RequestGroup), [RiskAssessment](riskassessment.html#RiskAssessment), [ServiceRequest](servicerequest.html#ServiceRequest), [SubstanceReferenceInformation](substancereferenceinformation.html#SubstanceReferenceInformation), [SubstanceSpecification](substancespecification.html#SubstanceSpecification) and [SupplyRequest](supplyrequest.html#SupplyRequest)

## 2.42.3 
Resource Content
 [
](documentreference.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [DocumentReference](documentreference-definitions.html#DocumentReference) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A reference to a document**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [masterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Master Version Specific Identifier | |

| [identifier](documentreference-definitions.html#DocumentReference.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Other identifiers for the document
 | |

| [status](documentreference-definitions.html#DocumentReference.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | current | superseded | entered-in-error
[DocumentReferenceStatus](valueset-document-reference-status.html) ([Required](terminologies.html#required)) | |

| [docStatus](documentreference-definitions.html#DocumentReference.docStatus) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | preliminary | final | amended | entered-in-error
[CompositionStatus](valueset-composition-status.html) ([Required](terminologies.html#required)) | |

| [type](documentreference-definitions.html#DocumentReference.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of document (LOINC if possible)
[Document Type Value Set](valueset-c80-doc-typecodes.html) ([Preferred](terminologies.html#preferred)) | |

| [category](documentreference-definitions.html#DocumentReference.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Categorization of document
[Document Class Value Set](valueset-document-classcodes.html) ([Example](terminologies.html#example))
 | |

| [subject](documentreference-definitions.html#DocumentReference.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [Group](group.html) | [Device](device.html)) | Who/what is the subject of the document | |

| [date](documentreference-definitions.html#DocumentReference.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [instant](datatypes.html#instant) | When this document reference was created | |

| [author](documentreference-definitions.html#DocumentReference.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who and/or what authored the document
 | |

| [authenticator](documentreference-definitions.html#DocumentReference.authenticator) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Who/what authenticated the document | |

| [custodian](documentreference-definitions.html#DocumentReference.custodian) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization which maintains the document | |

| [relatesTo](documentreference-definitions.html#DocumentReference.relatesTo) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | Relationships to other documents
 | |

| [code](documentreference-definitions.html#DocumentReference.relatesTo.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | replaces | transforms | signs | appends
[DocumentRelationshipType](valueset-document-relationship-type.html) ([Required](terminologies.html#required)) | |

| [target](documentreference-definitions.html#DocumentReference.relatesTo.target) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([DocumentReference](documentreference.html)) | Target of the relationship | |

| [description](documentreference-definitions.html#DocumentReference.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human-readable description | |

| [securityLabel](documentreference-definitions.html#DocumentReference.securityLabel) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Document security-tags
[SecurityLabels](valueset-security-labels.html) ([Extensible](terminologies.html#extensible))
 | |

| [content](documentreference-definitions.html#DocumentReference.content) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [BackboneElement](backboneelement.html) | Document referenced
 | |

| [attachment](documentreference-definitions.html#DocumentReference.content.attachment) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Attachment](datatypes.html#Attachment) | Where to access the document | |

| [format](documentreference-definitions.html#DocumentReference.content.format) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Coding](datatypes.html#Coding) | Format/content rules for the document
[DocumentReference Format Code Set](valueset-formatcodes.html) ([Preferred](terminologies.html#preferred)) | |

| [context](documentreference-definitions.html#DocumentReference.context) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [BackboneElement](backboneelement.html) | Clinical context of document | |

| [encounter](documentreference-definitions.html#DocumentReference.context.encounter) | | 0..* | [Reference](references.html#Reference)([Encounter](encounter.html) | [EpisodeOfCare](episodeofcare.html)) | Context of the document content
 | |

| [event](documentreference-definitions.html#DocumentReference.context.event) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Main clinical acts documented
[v3 Code System ActCode](v3/ActCode/vs.html) ([Example](terminologies.html#example))
 | |

| [period](documentreference-definitions.html#DocumentReference.context.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Time of service that is being documented | |

| [facilityType](documentreference-definitions.html#DocumentReference.context.facilityType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of facility where patient was seen
[Facility Type Code Value Set](valueset-c80-facilitycodes.html) ([Example](terminologies.html#example)) | |

| [practiceSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Additional details about where the content was created (e.g. clinical specialty)
[Practice Setting Code Value Set](valueset-c80-practice-codes.html) ([Example](terminologies.html#example)) | |

| [sourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html)) | Patient demographics from source | |

| [related](documentreference-definitions.html#DocumentReference.context.related) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Related identifiers or resources
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - DocumentReference ([DomainResource](domainresource.html))[Document identifier as assigned by the source of the document. This identifier is specific to this version of the document. This unique identifier may be used elsewhere to identify this version of the documentmasterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][Other identifiers associated with the document, including version independent identifiersidentifier](documentreference-definitions.html#DocumentReference.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The status of this document reference (this element modifies the meaning of other elements)status](documentreference-definitions.html#DocumentReference.status) : [code](datatypes.html#code) [1..1] « [The status of the document reference. (Strength=Required)DocumentReferenceStatus](valueset-document-reference-status.html)! »[The status of the underlying documentdocStatus](documentreference-definitions.html#DocumentReference.docStatus) : [code](datatypes.html#code) [0..1] « [Status of the underlying document. (Strength=Required)CompositionStatus](valueset-composition-status.html)! »[Specifies the particular kind of document referenced (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the document referencedtype](documentreference-definitions.html#DocumentReference.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Precise type of clinical document. (Strength=Preferred)DocumentTypeValueSet](valueset-c80-doc-typecodes.html)? »[A categorization for the type of document referenced - helps for indexing and searching. This may be implied by or derived from the code specified in the DocumentReference.typecategory](documentreference-definitions.html#DocumentReference.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [High-level kind of a clinical document at a macro level. (Strength=Example)DocumentClassValueSet](valueset-document-classcodes.html)?? »[Who or what the document is about. The document can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of farm animals, or a set of patients that share a common exposure)subject](documentreference-definitions.html#DocumentReference.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device) »[When the document reference was createddate](documentreference-definitions.html#DocumentReference.date) : [instant](datatypes.html#instant) [0..1][Identifies who is responsible for adding the information to the documentauthor](documentreference-definitions.html#DocumentReference.author) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »[Which person or organization authenticates that this document is validauthenticator](documentreference-definitions.html#DocumentReference.authenticator) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[Identifies the organization or group who is responsible for ongoing maintenance of and access to the documentcustodian](documentreference-definitions.html#DocumentReference.custodian) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Human-readable description of the source documentdescription](documentreference-definitions.html#DocumentReference.description) : [string](datatypes.html#string) [0..1][A set of Security-Tag codes specifying the level of privacy/security of the Document. Note that DocumentReference.meta.security contains the security labels of the "reference" to the document, while DocumentReference.securityLabel contains a snapshot of the security labels on the document the reference refers tosecurityLabel](documentreference-definitions.html#DocumentReference.securityLabel) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Security Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)All Security Labels](valueset-security-labels.html)+ »RelatesTo[The type of relationship that this document has with anther documentcode](documentreference-definitions.html#DocumentReference.relatesTo.code) : [code](datatypes.html#code) [1..1] « [The type of relationship between documents. (Strength=Required)DocumentRelationshipType](valueset-document-relationship-type.html)! »[The target document of this relationshiptarget](documentreference-definitions.html#DocumentReference.relatesTo.target) : [Reference](references.html#Reference) [1..1] « [DocumentReference](documentreference.html#DocumentReference) »Content[The document or URL of the document along with critical metadata to prove content has integrityattachment](documentreference-definitions.html#DocumentReference.content.attachment) : [Attachment](datatypes.html#Attachment) [1..1][An identifier of the document encoding, structure, and template that the document conforms to beyond the base format indicated in the mimeTypeformat](documentreference-definitions.html#DocumentReference.content.format) : [Coding](datatypes.html#Coding) [0..1] « [Document Format Codes. (Strength=Preferred)DocumentReferenceFormatCodeSet](valueset-formatcodes.html)? »Context[Describes the clinical encounter or type of care that the document content is associated withencounter](documentreference-definitions.html#DocumentReference.context.encounter) : [Reference](references.html#Reference) [0..*] « [Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare) »[This list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the type Code, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actevent](documentreference-definitions.html#DocumentReference.context.event) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [This list of codes represents the main clinical acts being documented. (Strength=Example)v3.ActCode](v3/ActCode/vs.html)?? »[The time period over which the service that is described by the document was providedperiod](documentreference-definitions.html#DocumentReference.context.period) : [Period](datatypes.html#Period) [0..1][The kind of facility where the patient was seenfacilityType](documentreference-definitions.html#DocumentReference.context.facilityType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [XDS Facility Type. (Strength=Example)FacilityTypeCodeValueSet](valueset-c80-facilitycodes.html)?? »[This property may convey specifics about the practice setting where the content was created, often reflecting the clinical specialtypracticeSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Additional details about where the content was created (e.g. clinical specialty). (Strength=Example)](valueset-c80-practice-codes.html) [PracticeSettingCodeValueSet](valueset-c80-practice-codes.html)?? »[The Patient Information as known when the document was published. May be a reference to a version specific, or containedsourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient) »[Related identifiers or resources associated with the DocumentReferencerelated](documentreference-definitions.html#DocumentReference.context.related) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »
[Relationships that this document has with other document references that already existrelatesTo](documentreference-definitions.html#DocumentReference.relatesTo)[0..*][The document and format referenced. There may be multiple content element repetitions, each with a different formatcontent](documentreference-definitions.html#DocumentReference.content)[1..*][The clinical context in which the document was preparedcontext](documentreference-definitions.html#DocumentReference.context)[0..1]
 

 

 

**XML Template**

 

 
```
<[**DocumentReference**](documentreference-definitions.html#DocumentReference) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**masterIdentifier**](documentreference-definitions.html#DocumentReference.masterIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Master Version Specific Identifier](terminologies.html#unbound) --></masterIdentifier>
 <[**identifier**](documentreference-definitions.html#DocumentReference.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Other identifiers for the document](terminologies.html#unbound) --></identifier>
 <[**status**](documentreference-definitions.html#DocumentReference.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [current | superseded | entered-in-error](valueset-document-reference-status.html) -->
 <[**docStatus**](documentreference-definitions.html#DocumentReference.docStatus) value="[[code](datatypes.html#code)]"/><!-- **0..1** [preliminary | final | amended | entered-in-error](valueset-composition-status.html) -->
 <[**type**](documentreference-definitions.html#DocumentReference.type)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of document (LOINC if possible)](valueset-c80-doc-typecodes.html) --></type>
 <[**category**](documentreference-definitions.html#DocumentReference.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Categorization of document](valueset-document-classcodes.html) --></category>
 <[**subject**](documentreference-definitions.html#DocumentReference.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device)) [Who/what is the subject of the document](terminologies.html#unbound) --></subject>
 <[**date**](documentreference-definitions.html#DocumentReference.date) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [When this document reference was created](terminologies.html#unbound) -->
 <[**author**](documentreference-definitions.html#DocumentReference.author)><!-- **0..*** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Device](device.html#Device)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Who and/or what authored the document](terminologies.html#unbound) --></author>
 <[**authenticator**](documentreference-definitions.html#DocumentReference.authenticator)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) [Who/what authenticated the document](terminologies.html#unbound) --></authenticator>
 <[**custodian**](documentreference-definitions.html#DocumentReference.custodian)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization which maintains the document](terminologies.html#unbound) --></custodian>
 <[**relatesTo**](documentreference-definitions.html#DocumentReference.relatesTo)> <!-- **0..*** Relationships to other documents -->
 <[**code**](documentreference-definitions.html#DocumentReference.relatesTo.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [replaces | transforms | signs | appends](valueset-document-relationship-type.html) -->
 <[**target**](documentreference-definitions.html#DocumentReference.relatesTo.target)><!-- **1..1** [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) [Target of the relationship](terminologies.html#unbound) --></target>
 </relatesTo>
 <[**description**](documentreference-definitions.html#DocumentReference.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Human-readable description](terminologies.html#unbound) -->
 <[**securityLabel**](documentreference-definitions.html#DocumentReference.securityLabel)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Document security-tags](valueset-security-labels.html) --></securityLabel>
 <[**content**](documentreference-definitions.html#DocumentReference.content)> <!-- **1..*** Document referenced -->
 <[**attachment**](documentreference-definitions.html#DocumentReference.content.attachment)><!-- **1..1** [Attachment](datatypes.html#Attachment) [Where to access the document](terminologies.html#unbound) --></attachment>
 <[**format**](documentreference-definitions.html#DocumentReference.content.format)><!-- **0..1** [Coding](datatypes.html#Coding) [Format/content rules for the document](valueset-formatcodes.html) --></format>
 </content>
 <[**context**](documentreference-definitions.html#DocumentReference.context)> <!-- **0..1** Clinical context of document -->
 <[**encounter**](documentreference-definitions.html#DocumentReference.context.encounter)><!-- **0..*** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) [Context of the document content](terminologies.html#unbound) --></encounter>
 <[**event**](documentreference-definitions.html#DocumentReference.context.event)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Main clinical acts documented](v3/ActCode/vs.html) --></event>
 <[**period**](documentreference-definitions.html#DocumentReference.context.period)><!-- **0..1** [Period](datatypes.html#Period) [Time of service that is being documented](terminologies.html#unbound) --></period>
 <[**facilityType**](documentreference-definitions.html#DocumentReference.context.facilityType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of facility where patient was seen](valueset-c80-facilitycodes.html) --></facilityType>
 <[**practiceSetting**](documentreference-definitions.html#DocumentReference.context.practiceSetting)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Additional details about where the content was created (e.g. clinical specialty)](valueset-c80-practice-codes.html) --></practiceSetting>
 <[**sourcePatientInfo**](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)) [Patient demographics from source](terminologies.html#unbound) --></sourcePatientInfo>
 <[**related**](documentreference-definitions.html#DocumentReference.context.related)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Related identifiers or resources](terminologies.html#unbound) --></related>
 </context>
</DocumentReference>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**DocumentReference**](documentreference-definitions.html#DocumentReference)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[masterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Master Version Specific Identifier](terminologies.html#unbound)
 "[identifier](documentreference-definitions.html#DocumentReference.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Other identifiers for the document](terminologies.html#unbound)
 "[status](documentreference-definitions.html#DocumentReference.status)" : "<[code](datatypes.html#code)>", // **R!** [current | superseded | entered-in-error](valueset-document-reference-status.html)
 "[docStatus](documentreference-definitions.html#DocumentReference.docStatus)" : "<[code](datatypes.html#code)>", // [preliminary | final | amended | entered-in-error](valueset-composition-status.html)
 "[type](documentreference-definitions.html#DocumentReference.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of document (LOINC if possible)](valueset-c80-doc-typecodes.html)
 "[category](documentreference-definitions.html#DocumentReference.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Categorization of document](valueset-document-classcodes.html)
 "[subject](documentreference-definitions.html#DocumentReference.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device)) }, // [Who/what is the subject of the document](terminologies.html#unbound)
 "[date](documentreference-definitions.html#DocumentReference.date)" : "<[instant](datatypes.html#instant)>", // [When this document reference was created](terminologies.html#unbound)
 "[author](documentreference-definitions.html#DocumentReference.author)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Device](device.html#Device)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) }], // [Who and/or what authored the document](terminologies.html#unbound)
 "[authenticator](documentreference-definitions.html#DocumentReference.authenticator)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }, // [Who/what authenticated the document](terminologies.html#unbound)
 "[custodian](documentreference-definitions.html#DocumentReference.custodian)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization which maintains the document](terminologies.html#unbound)
 "[relatesTo](documentreference-definitions.html#DocumentReference.relatesTo)" : [{ // [Relationships to other documents](terminologies.html#unbound)
 "[code](documentreference-definitions.html#DocumentReference.relatesTo.code)" : "<[code](datatypes.html#code)>", // **R!** [replaces | transforms | signs | appends](valueset-document-relationship-type.html)
 "[target](documentreference-definitions.html#DocumentReference.relatesTo.target)" : { [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) } // **R!** [Target of the relationship](terminologies.html#unbound)
 }],
 "[description](documentreference-definitions.html#DocumentReference.description)" : "<[string](datatypes.html#string)>", // [Human-readable description](terminologies.html#unbound)
 "[securityLabel](documentreference-definitions.html#DocumentReference.securityLabel)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Document security-tags](valueset-security-labels.html)
 "[content](documentreference-definitions.html#DocumentReference.content)" : [{ // **R!** [Document referenced](terminologies.html#unbound)
 "[attachment](documentreference-definitions.html#DocumentReference.content.attachment)" : { [Attachment](datatypes.html#Attachment) }, // **R!** [Where to access the document](terminologies.html#unbound)
 "[format](documentreference-definitions.html#DocumentReference.content.format)" : { [Coding](datatypes.html#Coding) } // [Format/content rules for the document](valueset-formatcodes.html)
 }],
 "[context](documentreference-definitions.html#DocumentReference.context)" : { // [Clinical context of document](terminologies.html#unbound)
 "[encounter](documentreference-definitions.html#DocumentReference.context.encounter)" : [{ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) }], // [Context of the document content](terminologies.html#unbound)
 "[event](documentreference-definitions.html#DocumentReference.context.event)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Main clinical acts documented](v3/ActCode/vs.html)
 "[period](documentreference-definitions.html#DocumentReference.context.period)" : { [Period](datatypes.html#Period) }, // [Time of service that is being documented](terminologies.html#unbound)
 "[facilityType](documentreference-definitions.html#DocumentReference.context.facilityType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of facility where patient was seen](valueset-c80-facilitycodes.html)
 "[practiceSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Additional details about where the content was created (e.g. clinical specialty)](valueset-c80-practice-codes.html)
 "[sourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) }, // [Patient demographics from source](terminologies.html#unbound)
 "[related](documentreference-definitions.html#DocumentReference.context.related)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }] // [Related identifiers or resources](terminologies.html#unbound)
 }
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**DocumentReference**](documentreference-definitions.html#DocumentReference);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[DocumentReference.masterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Master Version Specific Identifier
 fhir:[DocumentReference.identifier](documentreference-definitions.html#DocumentReference.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Other identifiers for the document
 fhir:[DocumentReference.status](documentreference-definitions.html#DocumentReference.status) [ [code](datatypes.html#code) ]; # 1..1 current | superseded | entered-in-error
 fhir:[DocumentReference.docStatus](documentreference-definitions.html#DocumentReference.docStatus) [ [code](datatypes.html#code) ]; # 0..1 preliminary | final | amended | entered-in-error
 fhir:[DocumentReference.type](documentreference-definitions.html#DocumentReference.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of document (LOINC if possible)
 fhir:[DocumentReference.category](documentreference-definitions.html#DocumentReference.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Categorization of document
 fhir:[DocumentReference.subject](documentreference-definitions.html#DocumentReference.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device)) ]; # 0..1 Who/what is the subject of the document
 fhir:[DocumentReference.date](documentreference-definitions.html#DocumentReference.date) [ [instant](datatypes.html#instant) ]; # 0..1 When this document reference was created
 fhir:[DocumentReference.author](documentreference-definitions.html#DocumentReference.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ], ... ; # 0..* Who and/or what authored the document
 fhir:[DocumentReference.authenticator](documentreference-definitions.html#DocumentReference.authenticator) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 0..1 Who/what authenticated the document
 fhir:[DocumentReference.custodian](documentreference-definitions.html#DocumentReference.custodian) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization which maintains the document
 fhir:[DocumentReference.relatesTo](documentreference-definitions.html#DocumentReference.relatesTo) [ # 0..* Relationships to other documents
 fhir:[DocumentReference.relatesTo.code](documentreference-definitions.html#DocumentReference.relatesTo.code) [ [code](datatypes.html#code) ]; # 1..1 replaces | transforms | signs | appends
 fhir:[DocumentReference.relatesTo.target](documentreference-definitions.html#DocumentReference.relatesTo.target) [ [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) ]; # 1..1 Target of the relationship
 ], ...;
 fhir:[DocumentReference.description](documentreference-definitions.html#DocumentReference.description) [ [string](datatypes.html#string) ]; # 0..1 Human-readable description
 fhir:[DocumentReference.securityLabel](documentreference-definitions.html#DocumentReference.securityLabel) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Document security-tags
 fhir:[DocumentReference.content](documentreference-definitions.html#DocumentReference.content) [ # 1..* Document referenced
 fhir:[DocumentReference.content.attachment](documentreference-definitions.html#DocumentReference.content.attachment) [ [Attachment](datatypes.html#Attachment) ]; # 1..1 Where to access the document
 fhir:[DocumentReference.content.format](documentreference-definitions.html#DocumentReference.content.format) [ [Coding](datatypes.html#Coding) ]; # 0..1 Format/content rules for the document
 ], ...;
 fhir:[DocumentReference.context](documentreference-definitions.html#DocumentReference.context) [ # 0..1 Clinical context of document
 fhir:[DocumentReference.context.encounter](documentreference-definitions.html#DocumentReference.context.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) ], ... ; # 0..* Context of the document content
 fhir:[DocumentReference.context.event](documentreference-definitions.html#DocumentReference.context.event) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Main clinical acts documented
 fhir:[DocumentReference.context.period](documentreference-definitions.html#DocumentReference.context.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time of service that is being documented
 fhir:[DocumentReference.context.facilityType](documentreference-definitions.html#DocumentReference.context.facilityType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of facility where patient was seen
 fhir:[DocumentReference.context.practiceSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Additional details about where the content was created (e.g. clinical specialty)
 fhir:[DocumentReference.context.sourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 0..1 Patient demographics from source
 fhir:[DocumentReference.context.related](documentreference-definitions.html#DocumentReference.context.related) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Related identifiers or resources
 ];
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [DocumentReference](documentreference.html#DocumentReference)
 | 
 | 
 |

 | 
 DocumentReference.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/document-reference-status to http://hl7.org/fhir/ValueSet/document-reference-status|4.0.1

 

 | 
 |

 | 
 DocumentReference.docStatus | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/composition-status to http://hl7.org/fhir/ValueSet/composition-status|4.0.1

 

 | 
 |

 | 
 DocumentReference.type | 
 
 

 - Min Cardinality changed from 1 to 0

 

 | 
 |

 | 
 DocumentReference.category | 
 
 

 - Renamed from class to category

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 DocumentReference.date | 
 
 

 - Added Element

 

 | 
 |

 | 
 DocumentReference.author | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 DocumentReference.authenticator | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 DocumentReference.relatesTo | 
 
 

 - No longer marked as Modifier

 

 | 
 |

 | 
 DocumentReference.relatesTo.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/document-relationship-type to http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.1

 

 | 
 |

 | 
 DocumentReference.context.encounter | 
 
 

 - Max Cardinality changed from 1 to *

 - Type Reference: Added Target Type EpisodeOfCare

 

 | 
 |

 | 
 DocumentReference.context.related | 
 
 

 - Type changed from BackboneElement to Reference(Resource)

 

 | 
 |

 | 
 DocumentReference.created | 
 
 

 - deleted

 

 | 
 |

 | 
 DocumentReference.indexed | 
 
 

 - deleted

 

 | 
 |

 | 
 DocumentReference.context.related.identifier | 
 
 

 - deleted

 

 | 
 |

 | 
 DocumentReference.context.related.ref | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](documentreference.diff.xml) or [JSON](documentreference.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](documentreference-version-maps.html) (status = 1 test of which 1 fail to execute.)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [DocumentReference](documentreference-definitions.html#DocumentReference) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A reference to a document**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [masterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Master Version Specific Identifier | |

| [identifier](documentreference-definitions.html#DocumentReference.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | Other identifiers for the document
 | |

| [status](documentreference-definitions.html#DocumentReference.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | current | superseded | entered-in-error
[DocumentReferenceStatus](valueset-document-reference-status.html) ([Required](terminologies.html#required)) | |

| [docStatus](documentreference-definitions.html#DocumentReference.docStatus) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | preliminary | final | amended | entered-in-error
[CompositionStatus](valueset-composition-status.html) ([Required](terminologies.html#required)) | |

| [type](documentreference-definitions.html#DocumentReference.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of document (LOINC if possible)
[Document Type Value Set](valueset-c80-doc-typecodes.html) ([Preferred](terminologies.html#preferred)) | |

| [category](documentreference-definitions.html#DocumentReference.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Categorization of document
[Document Class Value Set](valueset-document-classcodes.html) ([Example](terminologies.html#example))
 | |

| [subject](documentreference-definitions.html#DocumentReference.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [Group](group.html) | [Device](device.html)) | Who/what is the subject of the document | |

| [date](documentreference-definitions.html#DocumentReference.date) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [instant](datatypes.html#instant) | When this document reference was created | |

| [author](documentreference-definitions.html#DocumentReference.author) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Who and/or what authored the document
 | |

| [authenticator](documentreference-definitions.html#DocumentReference.authenticator) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Who/what authenticated the document | |

| [custodian](documentreference-definitions.html#DocumentReference.custodian) | | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization which maintains the document | |

| [relatesTo](documentreference-definitions.html#DocumentReference.relatesTo) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | Relationships to other documents
 | |

| [code](documentreference-definitions.html#DocumentReference.relatesTo.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | replaces | transforms | signs | appends
[DocumentRelationshipType](valueset-document-relationship-type.html) ([Required](terminologies.html#required)) | |

| [target](documentreference-definitions.html#DocumentReference.relatesTo.target) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([DocumentReference](documentreference.html)) | Target of the relationship | |

| [description](documentreference-definitions.html#DocumentReference.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human-readable description | |

| [securityLabel](documentreference-definitions.html#DocumentReference.securityLabel) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Document security-tags
[SecurityLabels](valueset-security-labels.html) ([Extensible](terminologies.html#extensible))
 | |

| [content](documentreference-definitions.html#DocumentReference.content) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [BackboneElement](backboneelement.html) | Document referenced
 | |

| [attachment](documentreference-definitions.html#DocumentReference.content.attachment) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Attachment](datatypes.html#Attachment) | Where to access the document | |

| [format](documentreference-definitions.html#DocumentReference.content.format) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Coding](datatypes.html#Coding) | Format/content rules for the document
[DocumentReference Format Code Set](valueset-formatcodes.html) ([Preferred](terminologies.html#preferred)) | |

| [context](documentreference-definitions.html#DocumentReference.context) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [BackboneElement](backboneelement.html) | Clinical context of document | |

| [encounter](documentreference-definitions.html#DocumentReference.context.encounter) | | 0..* | [Reference](references.html#Reference)([Encounter](encounter.html) | [EpisodeOfCare](episodeofcare.html)) | Context of the document content
 | |

| [event](documentreference-definitions.html#DocumentReference.context.event) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Main clinical acts documented
[v3 Code System ActCode](v3/ActCode/vs.html) ([Example](terminologies.html#example))
 | |

| [period](documentreference-definitions.html#DocumentReference.context.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Time of service that is being documented | |

| [facilityType](documentreference-definitions.html#DocumentReference.context.facilityType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of facility where patient was seen
[Facility Type Code Value Set](valueset-c80-facilitycodes.html) ([Example](terminologies.html#example)) | |

| [practiceSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Additional details about where the content was created (e.g. clinical specialty)
[Practice Setting Code Value Set](valueset-c80-practice-codes.html) ([Example](terminologies.html#example)) | |

| [sourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo) | | 0..1 | [Reference](references.html#Reference)([Patient](patient.html)) | Patient demographics from source | |

| [related](documentreference-definitions.html#DocumentReference.context.related) | | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Related identifiers or resources
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - DocumentReference ([DomainResource](domainresource.html))[Document identifier as assigned by the source of the document. This identifier is specific to this version of the document. This unique identifier may be used elsewhere to identify this version of the documentmasterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][Other identifiers associated with the document, including version independent identifiersidentifier](documentreference-definitions.html#DocumentReference.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The status of this document reference (this element modifies the meaning of other elements)status](documentreference-definitions.html#DocumentReference.status) : [code](datatypes.html#code) [1..1] « [The status of the document reference. (Strength=Required)DocumentReferenceStatus](valueset-document-reference-status.html)! »[The status of the underlying documentdocStatus](documentreference-definitions.html#DocumentReference.docStatus) : [code](datatypes.html#code) [0..1] « [Status of the underlying document. (Strength=Required)CompositionStatus](valueset-composition-status.html)! »[Specifies the particular kind of document referenced (e.g. History and Physical, Discharge Summary, Progress Note). This usually equates to the purpose of making the document referencedtype](documentreference-definitions.html#DocumentReference.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Precise type of clinical document. (Strength=Preferred)DocumentTypeValueSet](valueset-c80-doc-typecodes.html)? »[A categorization for the type of document referenced - helps for indexing and searching. This may be implied by or derived from the code specified in the DocumentReference.typecategory](documentreference-definitions.html#DocumentReference.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [High-level kind of a clinical document at a macro level. (Strength=Example)DocumentClassValueSet](valueset-document-classcodes.html)?? »[Who or what the document is about. The document can be about a person, (patient or healthcare practitioner), a device (e.g. a machine) or even a group of subjects (such as a document about a herd of farm animals, or a set of patients that share a common exposure)subject](documentreference-definitions.html#DocumentReference.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device) »[When the document reference was createddate](documentreference-definitions.html#DocumentReference.date) : [instant](datatypes.html#instant) [0..1][Identifies who is responsible for adding the information to the documentauthor](documentreference-definitions.html#DocumentReference.author) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »[Which person or organization authenticates that this document is validauthenticator](documentreference-definitions.html#DocumentReference.authenticator) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[Identifies the organization or group who is responsible for ongoing maintenance of and access to the documentcustodian](documentreference-definitions.html#DocumentReference.custodian) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Human-readable description of the source documentdescription](documentreference-definitions.html#DocumentReference.description) : [string](datatypes.html#string) [0..1][A set of Security-Tag codes specifying the level of privacy/security of the Document. Note that DocumentReference.meta.security contains the security labels of the "reference" to the document, while DocumentReference.securityLabel contains a snapshot of the security labels on the document the reference refers tosecurityLabel](documentreference-definitions.html#DocumentReference.securityLabel) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Security Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)All Security Labels](valueset-security-labels.html)+ »RelatesTo[The type of relationship that this document has with anther documentcode](documentreference-definitions.html#DocumentReference.relatesTo.code) : [code](datatypes.html#code) [1..1] « [The type of relationship between documents. (Strength=Required)DocumentRelationshipType](valueset-document-relationship-type.html)! »[The target document of this relationshiptarget](documentreference-definitions.html#DocumentReference.relatesTo.target) : [Reference](references.html#Reference) [1..1] « [DocumentReference](documentreference.html#DocumentReference) »Content[The document or URL of the document along with critical metadata to prove content has integrityattachment](documentreference-definitions.html#DocumentReference.content.attachment) : [Attachment](datatypes.html#Attachment) [1..1][An identifier of the document encoding, structure, and template that the document conforms to beyond the base format indicated in the mimeTypeformat](documentreference-definitions.html#DocumentReference.content.format) : [Coding](datatypes.html#Coding) [0..1] « [Document Format Codes. (Strength=Preferred)DocumentReferenceFormatCodeSet](valueset-formatcodes.html)? »Context[Describes the clinical encounter or type of care that the document content is associated withencounter](documentreference-definitions.html#DocumentReference.context.encounter) : [Reference](references.html#Reference) [0..*] « [Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare) »[This list of codes represents the main clinical acts, such as a colonoscopy or an appendectomy, being documented. In some cases, the event is inherent in the type Code, such as a "History and Physical Report" in which the procedure being documented is necessarily a "History and Physical" actevent](documentreference-definitions.html#DocumentReference.context.event) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [This list of codes represents the main clinical acts being documented. (Strength=Example)v3.ActCode](v3/ActCode/vs.html)?? »[The time period over which the service that is described by the document was providedperiod](documentreference-definitions.html#DocumentReference.context.period) : [Period](datatypes.html#Period) [0..1][The kind of facility where the patient was seenfacilityType](documentreference-definitions.html#DocumentReference.context.facilityType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [XDS Facility Type. (Strength=Example)FacilityTypeCodeValueSet](valueset-c80-facilitycodes.html)?? »[This property may convey specifics about the practice setting where the content was created, often reflecting the clinical specialtypracticeSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Additional details about where the content was created (e.g. clinical specialty). (Strength=Example)](valueset-c80-practice-codes.html) [PracticeSettingCodeValueSet](valueset-c80-practice-codes.html)?? »[The Patient Information as known when the document was published. May be a reference to a version specific, or containedsourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient) »[Related identifiers or resources associated with the DocumentReferencerelated](documentreference-definitions.html#DocumentReference.context.related) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »
[Relationships that this document has with other document references that already existrelatesTo](documentreference-definitions.html#DocumentReference.relatesTo)[0..*][The document and format referenced. There may be multiple content element repetitions, each with a different formatcontent](documentreference-definitions.html#DocumentReference.content)[1..*][The clinical context in which the document was preparedcontext](documentreference-definitions.html#DocumentReference.context)[0..1]
 

**XML Template**

 

 
```
<[**DocumentReference**](documentreference-definitions.html#DocumentReference) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**masterIdentifier**](documentreference-definitions.html#DocumentReference.masterIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Master Version Specific Identifier](terminologies.html#unbound) --></masterIdentifier>
 <[**identifier**](documentreference-definitions.html#DocumentReference.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Other identifiers for the document](terminologies.html#unbound) --></identifier>
 <[**status**](documentreference-definitions.html#DocumentReference.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [current | superseded | entered-in-error](valueset-document-reference-status.html) -->
 <[**docStatus**](documentreference-definitions.html#DocumentReference.docStatus) value="[[code](datatypes.html#code)]"/><!-- **0..1** [preliminary | final | amended | entered-in-error](valueset-composition-status.html) -->
 <[**type**](documentreference-definitions.html#DocumentReference.type)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of document (LOINC if possible)](valueset-c80-doc-typecodes.html) --></type>
 <[**category**](documentreference-definitions.html#DocumentReference.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Categorization of document](valueset-document-classcodes.html) --></category>
 <[**subject**](documentreference-definitions.html#DocumentReference.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device)) [Who/what is the subject of the document](terminologies.html#unbound) --></subject>
 <[**date**](documentreference-definitions.html#DocumentReference.date) value="[[instant](datatypes.html#instant)]"/><!-- **0..1** [When this document reference was created](terminologies.html#unbound) -->
 <[**author**](documentreference-definitions.html#DocumentReference.author)><!-- **0..*** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Device](device.html#Device)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Who and/or what authored the document](terminologies.html#unbound) --></author>
 <[**authenticator**](documentreference-definitions.html#DocumentReference.authenticator)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) [Who/what authenticated the document](terminologies.html#unbound) --></authenticator>
 <[**custodian**](documentreference-definitions.html#DocumentReference.custodian)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization which maintains the document](terminologies.html#unbound) --></custodian>
 <[**relatesTo**](documentreference-definitions.html#DocumentReference.relatesTo)> <!-- **0..*** Relationships to other documents -->
 <[**code**](documentreference-definitions.html#DocumentReference.relatesTo.code) value="[[code](datatypes.html#code)]"/><!-- **1..1** [replaces | transforms | signs | appends](valueset-document-relationship-type.html) -->
 <[**target**](documentreference-definitions.html#DocumentReference.relatesTo.target)><!-- **1..1** [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) [Target of the relationship](terminologies.html#unbound) --></target>
 </relatesTo>
 <[**description**](documentreference-definitions.html#DocumentReference.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Human-readable description](terminologies.html#unbound) -->
 <[**securityLabel**](documentreference-definitions.html#DocumentReference.securityLabel)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Document security-tags](valueset-security-labels.html) --></securityLabel>
 <[**content**](documentreference-definitions.html#DocumentReference.content)> <!-- **1..*** Document referenced -->
 <[**attachment**](documentreference-definitions.html#DocumentReference.content.attachment)><!-- **1..1** [Attachment](datatypes.html#Attachment) [Where to access the document](terminologies.html#unbound) --></attachment>
 <[**format**](documentreference-definitions.html#DocumentReference.content.format)><!-- **0..1** [Coding](datatypes.html#Coding) [Format/content rules for the document](valueset-formatcodes.html) --></format>
 </content>
 <[**context**](documentreference-definitions.html#DocumentReference.context)> <!-- **0..1** Clinical context of document -->
 <[**encounter**](documentreference-definitions.html#DocumentReference.context.encounter)><!-- **0..*** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) [Context of the document content](terminologies.html#unbound) --></encounter>
 <[**event**](documentreference-definitions.html#DocumentReference.context.event)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Main clinical acts documented](v3/ActCode/vs.html) --></event>
 <[**period**](documentreference-definitions.html#DocumentReference.context.period)><!-- **0..1** [Period](datatypes.html#Period) [Time of service that is being documented](terminologies.html#unbound) --></period>
 <[**facilityType**](documentreference-definitions.html#DocumentReference.context.facilityType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Kind of facility where patient was seen](valueset-c80-facilitycodes.html) --></facilityType>
 <[**practiceSetting**](documentreference-definitions.html#DocumentReference.context.practiceSetting)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Additional details about where the content was created (e.g. clinical specialty)](valueset-c80-practice-codes.html) --></practiceSetting>
 <[**sourcePatientInfo**](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)) [Patient demographics from source](terminologies.html#unbound) --></sourcePatientInfo>
 <[**related**](documentreference-definitions.html#DocumentReference.context.related)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Related identifiers or resources](terminologies.html#unbound) --></related>
 </context>
</DocumentReference>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**DocumentReference**](documentreference-definitions.html#DocumentReference)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[masterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Master Version Specific Identifier](terminologies.html#unbound)
 "[identifier](documentreference-definitions.html#DocumentReference.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Other identifiers for the document](terminologies.html#unbound)
 "[status](documentreference-definitions.html#DocumentReference.status)" : "<[code](datatypes.html#code)>", // **R!** [current | superseded | entered-in-error](valueset-document-reference-status.html)
 "[docStatus](documentreference-definitions.html#DocumentReference.docStatus)" : "<[code](datatypes.html#code)>", // [preliminary | final | amended | entered-in-error](valueset-composition-status.html)
 "[type](documentreference-definitions.html#DocumentReference.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of document (LOINC if possible)](valueset-c80-doc-typecodes.html)
 "[category](documentreference-definitions.html#DocumentReference.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Categorization of document](valueset-document-classcodes.html)
 "[subject](documentreference-definitions.html#DocumentReference.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device)) }, // [Who/what is the subject of the document](terminologies.html#unbound)
 "[date](documentreference-definitions.html#DocumentReference.date)" : "<[instant](datatypes.html#instant)>", // [When this document reference was created](terminologies.html#unbound)
 "[author](documentreference-definitions.html#DocumentReference.author)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Device](device.html#Device)|
 [Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) }], // [Who and/or what authored the document](terminologies.html#unbound)
 "[authenticator](documentreference-definitions.html#DocumentReference.authenticator)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }, // [Who/what authenticated the document](terminologies.html#unbound)
 "[custodian](documentreference-definitions.html#DocumentReference.custodian)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization which maintains the document](terminologies.html#unbound)
 "[relatesTo](documentreference-definitions.html#DocumentReference.relatesTo)" : [{ // [Relationships to other documents](terminologies.html#unbound)
 "[code](documentreference-definitions.html#DocumentReference.relatesTo.code)" : "<[code](datatypes.html#code)>", // **R!** [replaces | transforms | signs | appends](valueset-document-relationship-type.html)
 "[target](documentreference-definitions.html#DocumentReference.relatesTo.target)" : { [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) } // **R!** [Target of the relationship](terminologies.html#unbound)
 }],
 "[description](documentreference-definitions.html#DocumentReference.description)" : "<[string](datatypes.html#string)>", // [Human-readable description](terminologies.html#unbound)
 "[securityLabel](documentreference-definitions.html#DocumentReference.securityLabel)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Document security-tags](valueset-security-labels.html)
 "[content](documentreference-definitions.html#DocumentReference.content)" : [{ // **R!** [Document referenced](terminologies.html#unbound)
 "[attachment](documentreference-definitions.html#DocumentReference.content.attachment)" : { [Attachment](datatypes.html#Attachment) }, // **R!** [Where to access the document](terminologies.html#unbound)
 "[format](documentreference-definitions.html#DocumentReference.content.format)" : { [Coding](datatypes.html#Coding) } // [Format/content rules for the document](valueset-formatcodes.html)
 }],
 "[context](documentreference-definitions.html#DocumentReference.context)" : { // [Clinical context of document](terminologies.html#unbound)
 "[encounter](documentreference-definitions.html#DocumentReference.context.encounter)" : [{ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) }], // [Context of the document content](terminologies.html#unbound)
 "[event](documentreference-definitions.html#DocumentReference.context.event)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Main clinical acts documented](v3/ActCode/vs.html)
 "[period](documentreference-definitions.html#DocumentReference.context.period)" : { [Period](datatypes.html#Period) }, // [Time of service that is being documented](terminologies.html#unbound)
 "[facilityType](documentreference-definitions.html#DocumentReference.context.facilityType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Kind of facility where patient was seen](valueset-c80-facilitycodes.html)
 "[practiceSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Additional details about where the content was created (e.g. clinical specialty)](valueset-c80-practice-codes.html)
 "[sourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) }, // [Patient demographics from source](terminologies.html#unbound)
 "[related](documentreference-definitions.html#DocumentReference.context.related)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }] // [Related identifiers or resources](terminologies.html#unbound)
 }
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**DocumentReference**](documentreference-definitions.html#DocumentReference);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[DocumentReference.masterIdentifier](documentreference-definitions.html#DocumentReference.masterIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Master Version Specific Identifier
 fhir:[DocumentReference.identifier](documentreference-definitions.html#DocumentReference.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Other identifiers for the document
 fhir:[DocumentReference.status](documentreference-definitions.html#DocumentReference.status) [ [code](datatypes.html#code) ]; # 1..1 current | superseded | entered-in-error
 fhir:[DocumentReference.docStatus](documentreference-definitions.html#DocumentReference.docStatus) [ [code](datatypes.html#code) ]; # 0..1 preliminary | final | amended | entered-in-error
 fhir:[DocumentReference.type](documentreference-definitions.html#DocumentReference.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of document (LOINC if possible)
 fhir:[DocumentReference.category](documentreference-definitions.html#DocumentReference.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Categorization of document
 fhir:[DocumentReference.subject](documentreference-definitions.html#DocumentReference.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[Group](group.html#Group)|[Device](device.html#Device)) ]; # 0..1 Who/what is the subject of the document
 fhir:[DocumentReference.date](documentreference-definitions.html#DocumentReference.date) [ [instant](datatypes.html#instant) ]; # 0..1 When this document reference was created
 fhir:[DocumentReference.author](documentreference-definitions.html#DocumentReference.author) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Device](device.html#Device)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ], ... ; # 0..* Who and/or what authored the document
 fhir:[DocumentReference.authenticator](documentreference-definitions.html#DocumentReference.authenticator) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 0..1 Who/what authenticated the document
 fhir:[DocumentReference.custodian](documentreference-definitions.html#DocumentReference.custodian) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization which maintains the document
 fhir:[DocumentReference.relatesTo](documentreference-definitions.html#DocumentReference.relatesTo) [ # 0..* Relationships to other documents
 fhir:[DocumentReference.relatesTo.code](documentreference-definitions.html#DocumentReference.relatesTo.code) [ [code](datatypes.html#code) ]; # 1..1 replaces | transforms | signs | appends
 fhir:[DocumentReference.relatesTo.target](documentreference-definitions.html#DocumentReference.relatesTo.target) [ [Reference](references.html#Reference)([DocumentReference](documentreference.html#DocumentReference)) ]; # 1..1 Target of the relationship
 ], ...;
 fhir:[DocumentReference.description](documentreference-definitions.html#DocumentReference.description) [ [string](datatypes.html#string) ]; # 0..1 Human-readable description
 fhir:[DocumentReference.securityLabel](documentreference-definitions.html#DocumentReference.securityLabel) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Document security-tags
 fhir:[DocumentReference.content](documentreference-definitions.html#DocumentReference.content) [ # 1..* Document referenced
 fhir:[DocumentReference.content.attachment](documentreference-definitions.html#DocumentReference.content.attachment) [ [Attachment](datatypes.html#Attachment) ]; # 1..1 Where to access the document
 fhir:[DocumentReference.content.format](documentreference-definitions.html#DocumentReference.content.format) [ [Coding](datatypes.html#Coding) ]; # 0..1 Format/content rules for the document
 ], ...;
 fhir:[DocumentReference.context](documentreference-definitions.html#DocumentReference.context) [ # 0..1 Clinical context of document
 fhir:[DocumentReference.context.encounter](documentreference-definitions.html#DocumentReference.context.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)|[EpisodeOfCare](episodeofcare.html#EpisodeOfCare)) ], ... ; # 0..* Context of the document content
 fhir:[DocumentReference.context.event](documentreference-definitions.html#DocumentReference.context.event) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Main clinical acts documented
 fhir:[DocumentReference.context.period](documentreference-definitions.html#DocumentReference.context.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time of service that is being documented
 fhir:[DocumentReference.context.facilityType](documentreference-definitions.html#DocumentReference.context.facilityType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Kind of facility where patient was seen
 fhir:[DocumentReference.context.practiceSetting](documentreference-definitions.html#DocumentReference.context.practiceSetting) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Additional details about where the content was created (e.g. clinical specialty)
 fhir:[DocumentReference.context.sourcePatientInfo](documentreference-definitions.html#DocumentReference.context.sourcePatientInfo) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 0..1 Patient demographics from source
 fhir:[DocumentReference.context.related](documentreference-definitions.html#DocumentReference.context.related) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Related identifiers or resources
 ];
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [DocumentReference](documentreference.html#DocumentReference)
 | 
 | 
 |

 | 
 DocumentReference.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/document-reference-status to http://hl7.org/fhir/ValueSet/document-reference-status|4.0.1

 

 | 
 |

 | 
 DocumentReference.docStatus | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/composition-status to http://hl7.org/fhir/ValueSet/composition-status|4.0.1

 

 | 
 |

 | 
 DocumentReference.type | 
 
 

 - Min Cardinality changed from 1 to 0

 

 | 
 |

 | 
 DocumentReference.category | 
 
 

 - Renamed from class to category

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 DocumentReference.date | 
 
 

 - Added Element

 

 | 
 |

 | 
 DocumentReference.author | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 DocumentReference.authenticator | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 DocumentReference.relatesTo | 
 
 

 - No longer marked as Modifier

 

 | 
 |

 | 
 DocumentReference.relatesTo.code | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/document-relationship-type to http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.1

 

 | 
 |

 | 
 DocumentReference.context.encounter | 
 
 

 - Max Cardinality changed from 1 to *

 - Type Reference: Added Target Type EpisodeOfCare

 

 | 
 |

 | 
 DocumentReference.context.related | 
 
 

 - Type changed from BackboneElement to Reference(Resource)

 

 | 
 |

 | 
 DocumentReference.created | 
 
 

 - deleted

 

 | 
 |

 | 
 DocumentReference.indexed | 
 
 

 - deleted

 

 | 
 |

 | 
 DocumentReference.context.related.identifier | 
 
 

 - deleted

 

 | 
 |

 | 
 DocumentReference.context.related.ref | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](documentreference.diff.xml) or [JSON](documentreference.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](documentreference-version-maps.html) (status = 1 test of which 1 fail to execute.)

 

 

 

See the [Profiles & Extensions](documentreference-profiles.html) and the alternate definitions:
Master Definition [XML](documentreference.profile.xml.html) + [JSON](documentreference.profile.json.html),
[XML](xml.html) [Schema](documentreference.xsd)/[Schematron](documentreference.sch) + [JSON](json.html) 
[Schema](documentreference.schema.json.html), [ShEx](documentreference.shex.html) (for [Turtle](rdf.html)) + [see the extensions](documentreference-profiles.html) & the [dependency analysis](documentreference-dependencies.html)

### 2.42.3.1 
Terminology Bindings
 [
](documentreference.html#tx)

 | Path | Definition | Type | Reference | |

 | DocumentReference.status | The status of the document reference. | [Required](terminologies.html#required) | [DocumentReferenceStatus](valueset-document-reference-status.html) | |

 | DocumentReference.docStatus | Status of the underlying document. | [Required](terminologies.html#required) | [CompositionStatus](valueset-composition-status.html) | |

 | DocumentReference.type | Precise type of clinical document. | [Preferred](terminologies.html#preferred) | [DocumentTypeValueSet](valueset-c80-doc-typecodes.html) | |

 | DocumentReference.category | High-level kind of a clinical document at a macro level. | [Example](terminologies.html#example) | [DocumentClassValueSet](valueset-document-classcodes.html) | |

 | DocumentReference.relatesTo.code | The type of relationship between documents. | [Required](terminologies.html#required) | [DocumentRelationshipType](valueset-document-relationship-type.html) | |

 | DocumentReference.securityLabel | Security Labels from the Healthcare Privacy and Security Classification System. | [Extensible](terminologies.html#extensible) | [All Security Labels](valueset-security-labels.html) | |

 | DocumentReference.content.format | Document Format Codes. | [Preferred](terminologies.html#preferred) | [DocumentReferenceFormatCodeSet](valueset-formatcodes.html) | |

 | DocumentReference.context.event | This list of codes represents the main clinical acts being documented. | [Example](terminologies.html#example) | [v3.ActCode](v3/ActCode/vs.html) | |

 | DocumentReference.context.facilityType | XDS Facility Type. | [Example](terminologies.html#example) | [FacilityTypeCodeValueSet](valueset-c80-facilitycodes.html) | |

 | DocumentReference.context.practiceSetting | Additional details about where the content was created (e.g. clinical specialty). | [Example](terminologies.html#example) | [PracticeSettingCodeValueSet](valueset-c80-practice-codes.html) | |

 

## 2.42.4 Implementation Notes [
](documentreference.html#impl)

 - The use of the .docStatus codes is discussed in the [Composition description](composition.html#status)

 - The resources maintain one way relationships that point backwards - e.g., the document that replaces one document points towards the document that it replaced. The reverse relationships can be followed by using 
 indexes built from the resources. Typically, this is done using the search parameters described below. Given that documents may have other documents that replace or append them, clients should always check these relationships when accessing documents

 

 

### 2.42.4.1 Generating a Document Reference [](documentreference.html#2.42.4.1)

A client can ask a server to generate a document reference from a document.
The server reads the existing document and generates a matching DocumentReference
resource, or returns one it has previously generated. Servers may be able to 
return or generate document references for the following types of content:

 | **Type** | **Comments** | |

 | [FHIR Documents](documents.html) | The uri refers to an existing Document | |

 | [CDA ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) Document | The uri is a reference to a [Binary](binary.html) end-point that returns either a CDA 
 document, or some kind of CDA Package that the server knows how to process (e.g., an IHE .zip) | |

 | Other | The server can be asked to generate a document reference for other kinds of 
 documents. For some of these documents (e.g., PDF documents) a server could only provide a 
 document reference if it already existed or the server had special knowledge of the document. | |

The server either returns a search result containing a single document reference, 
or it returns an error. 
If the URI refers to another server, it is at the discretion of the 
server whether to retrieve it or return an error. 

The operation is initiated by a named query, using _query=generate on the /DocumentReference
end-point:

```
 GET [service-url]/DocumentReference/?_query=generate&uri=:url&...

```

The "uri" parameter is a relative or absolute reference to one of the 
document types described above. Other parameters may be supplied:

 | **Name** | **Meaning** | |

 | persist | Whether to store the document at the document end-point (/Document) or not, once it is generated. Value = true or false (default is for the server to decide). | |

## 2.42.5 Search Parameters [
](documentreference.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| authenticator | [reference](search.html#reference) | Who/what authenticated the document | DocumentReference.authenticator
([Practitioner](practitioner.html), [Organization](organization.html), [PractitionerRole](practitionerrole.html)) | | |

| author | [reference](search.html#reference) | Who and/or what authored the document | DocumentReference.author
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| category | [token](search.html#token) | Categorization of document | DocumentReference.category | | |

| contenttype | [token](search.html#token) | Mime type of the content, with charset etc. | DocumentReference.content.attachment.contentType | | |

| custodian | [reference](search.html#reference) | Organization which maintains the document | DocumentReference.custodian
([Organization](organization.html)) | | |

| date | [date](search.html#date) | When this document reference was created | DocumentReference.date | | |

| description | [string](search.html#string) | Human-readable description | DocumentReference.description | | |

| encounter | [reference](search.html#reference) | Context of the document content | DocumentReference.context.encounter
([EpisodeOfCare](episodeofcare.html), [Encounter](encounter.html)) | [12 Resources](searchparameter-registry.html#clinical-encounter) | |

| event | [token](search.html#token) | Main clinical acts documented | DocumentReference.context.event | | |

| facility | [token](search.html#token) | Kind of facility where patient was seen | DocumentReference.context.facilityType | | |

| format | [token](search.html#token) | Format/content rules for the document | DocumentReference.content.format | | |

| identifier | [token](search.html#token) | Master Version Specific Identifier | DocumentReference.masterIdentifier | DocumentReference.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| language | [token](search.html#token) | Human language of the content (BCP-47) | DocumentReference.content.attachment.language | | |

| location | [uri](search.html#uri) | Uri where the data can be found | DocumentReference.content.attachment.url | | |

| patient | [reference](search.html#reference) | Who/what is the subject of the document | DocumentReference.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| period | [date](search.html#date) | Time of service that is being documented | DocumentReference.context.period | | |

| related | [reference](search.html#reference) | Related identifiers or resources | DocumentReference.context.related
(Any) | | |

| relatesto | [reference](search.html#reference) | Target of the relationship | DocumentReference.relatesTo.target
([DocumentReference](documentreference.html)) | | |

| relation | [token](search.html#token) | replaces | transforms | signs | appends | DocumentReference.relatesTo.code | | |

| relationship | [composite](search.html#composite) | Combination of relation and relatesTo | On DocumentReference.relatesTo:
 relatesto: code
 relation: target | | |

| security-label | [token](search.html#token) | Document security-tags | DocumentReference.securityLabel | | |

| setting | [token](search.html#token) | Additional details about where the content was created (e.g. clinical specialty) | DocumentReference.context.practiceSetting | | |

| status | [token](search.html#token) | current | superseded | entered-in-error | DocumentReference.status | | |

| subject | [reference](search.html#reference) | Who/what is the subject of the document | DocumentReference.subject
([Practitioner](practitioner.html), [Group](group.html), [Device](device.html), [Patient](patient.html)) | | |

| type | [token](search.html#token) | Kind of document (LOINC if possible) | DocumentReference.type | [5 Resources](searchparameter-registry.html#clinical-type) | |