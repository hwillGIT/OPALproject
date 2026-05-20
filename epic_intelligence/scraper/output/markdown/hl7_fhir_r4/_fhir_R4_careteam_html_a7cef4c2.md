# CareTeam - FHIR v4.0.1Business identifiers assigned to this care team by the performer or other systems which remain constant as the resource is updated and propagates from server to serverIndicates the current state of the care team (this element modifies the meaning of other elements)Indicates the status of the care team. (Strength=Required)Identifies what kind of team.  This is to support differentiation between multiple co-existing teams, such as care plan team, episode of care team, longitudinal care teamIndicates the type of care team. (Strength=Example)A label for human use intended to distinguish like teams.  E.g. the "red" vs. "green" trauma teamsIdentifies the patient or group whose intended care is handled by the teamThe Encounter during which this CareTeam was created or to which the creation of this record is tightly associatedIndicates when the team did (or is intended to) come into effect and endDescribes why the care team existsIndicates the reason for the care team. (Strength=Example)Condition(s) that this care team addressesThe organization responsible for the care teamA central contact detail for the care team (that applies to all members)Comments made about the CareTeamIndicates specific responsibility of an individual within the care team, such as "Primary care physician", "Trained social worker counselor", "Caregiver", etcIndicates specific responsibility of an individual within the care team, such as "Primary physician", "Team coordinator", "Caregiver", etc. (Strength=Example)The specific person or organization who is participating/expected to participate in the care teamThe organization of the practitionerIndicates when the specific member or organization did (or is intended to) come into effect and endIdentifies all people and organizations who are expected to be involved in the care teamBusiness identifiers assigned to this care team by the performer or other systems which remain constant as the resource is updated and propagates from server to serverIndicates the current state of the care team (this element modifies the meaning of other elements)Indicates the status of the care team. (Strength=Required)Identifies what kind of team.  This is to support differentiation between multiple co-existing teams, such as care plan team, episode of care team, longitudinal care teamIndicates the type of care team. (Strength=Example)A label for human use intended to distinguish like teams.  E.g. the "red" vs. "green" trauma teamsIdentifies the patient or group whose intended care is handled by the teamThe Encounter during which this CareTeam was created or to which the creation of this record is tightly associatedIndicates when the team did (or is intended to) come into effect and endDescribes why the care team existsIndicates the reason for the care team. (Strength=Example)Condition(s) that this care team addressesThe organization responsible for the care teamA central contact detail for the care team (that applies to all members)Comments made about the CareTeamIndicates specific responsibility of an individual within the care team, such as "Primary care physician", "Trained social worker counselor", "Caregiver", etcIndicates specific responsibility of an individual within the care team, such as "Primary physician", "Team coordinator", "Caregiver", etc. (Strength=Example)The specific person or organization who is participating/expected to participate in the care teamThe organization of the practitionerIndicates when the specific member or organization did (or is intended to) come into effect and endIdentifies all people and organizations who are expected to be involved in the care team

> Source: https://hl7.org/fhir/R4/careteam.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/careteam.html) [R4B](http://hl7.org/fhir/R4B/careteam.html) **R4** [R3](http://hl7.org/fhir/STU3/careteam.html)
 

# 9.7 Resource CareTeam - Content [
](careteam.html#9.7)

| [Patient Care ](http://www.hl7.org/Special/committees/patientcare/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.

## 9.7.1 Scope and Usage [
](careteam.html#bnc)

The CareTeam includes all the people, teams, and organizations who plan to participate in the coordination and delivery of care for a single patient or a group (such as a married couple in therapy or a support group). CareTeam can also be organizationally assigned without a subject in context, such as a code blue team or emergency response team. This is not limited to practitioners, but may include other caregivers such as family members, guardians, the patient themself, or others. 

The Care Team, depending on where used, may include care team members specific to a particular care plan, an episode, an encounter, or may reflect all known team members across these perspectives. An individual's CareTeam can be dynamic over time, such that there can be transience of team members, such as a rehabilitation team.

## 9.7.2 Boundaries and Relationships [
](careteam.html#9.7.2)

Care Team is distinct from Group. Group is patient-independent and identifies an undifferentiated set of individuals who are intended to be the target of one or more clinical activities (e.g. set of clinical trial participants, set of individuals impacted by or at risk of a public health event, a herd or flock, etc.) The CareTeam resource establishes a set of relationships and roles and is specific to a particular Patient. The actors are the individual members or organized group of individuals. 

CareTeam can be referenced by EpisodeOfCare, Encounter, or CarePlan to identify the set of individuals (and their respective roles) who are intended to be involved in providing the care defined by those resources. 

 

This resource is referenced by [CarePlan](careplan.html#CarePlan), itself, [ChargeItem](chargeitem.html#ChargeItem), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [DeviceRequest](devicerequest.html#DeviceRequest), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ImagingStudy](imagingstudy.html#ImagingStudy), [Media](media.html#Media), [MedicationRequest](medicationrequest.html#MedicationRequest), [Observation](observation.html#Observation), [ServiceRequest](servicerequest.html#ServiceRequest) and [Task](task.html#Task)

## 9.7.3 
Resource Content
 [
](careteam.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [CareTeam](careteam-definitions.html#CareTeam) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Planned participants in the coordination and delivery of care for a patient or group**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](careteam-definitions.html#CareTeam.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this team
 | |

| [status](careteam-definitions.html#CareTeam.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | proposed | active | suspended | inactive | entered-in-error
[CareTeamStatus](valueset-care-team-status.html) ([Required](terminologies.html#required)) | |

| [category](careteam-definitions.html#CareTeam.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of team
[Care Team category](valueset-care-team-category.html) ([Example](terminologies.html#example))
 | |

| [name](careteam-definitions.html#CareTeam.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Name of the team, such as crisis assessment team | |

| [subject](careteam-definitions.html#CareTeam.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who care team is for | |

| [encounter](careteam-definitions.html#CareTeam.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [period](careteam-definitions.html#CareTeam.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Time period team covers | |

| [participant](careteam-definitions.html#CareTeam.participant) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Members of the team
+ Rule: CareTeam.participant.onBehalfOf can only be populated when CareTeam.participant.member is a Practitioner
 | |

| [role](careteam-definitions.html#CareTeam.participant.role) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of involvement
[Participant Roles](valueset-participant-role.html) ([Example](terminologies.html#example))
 | |

| [member](careteam-definitions.html#CareTeam.participant.member) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Organization](organization.html) | [CareTeam](careteam.html)) | Who is involved | |

| [onBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization of the practitioner | |

| [period](careteam-definitions.html#CareTeam.participant.period) | | 0..1 | [Period](datatypes.html#Period) | Time period of participant | |

| [reasonCode](careteam-definitions.html#CareTeam.reasonCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Why the care team exists
[SNOMED CT Clinical Findings](valueset-clinical-findings.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](careteam-definitions.html#CareTeam.reasonReference) | | 0..* | [Reference](references.html#Reference)([Condition](condition.html)) | Why the care team exists
 | |

| [managingOrganization](careteam-definitions.html#CareTeam.managingOrganization) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for the care team
 | |

| [telecom](careteam-definitions.html#CareTeam.telecom) | | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the care team (that applies to all members)
 | |

| [note](careteam-definitions.html#CareTeam.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the CareTeam
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - CareTeam ([DomainResource](domainresource.html))[Business identifiers assigned to this care team by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](careteam-definitions.html#CareTeam.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Indicates the current state of the care team (this element modifies the meaning of other elements)status](careteam-definitions.html#CareTeam.status) : [code](datatypes.html#code) [0..1] « [Indicates the status of the care team. (Strength=Required)CareTeamStatus](valueset-care-team-status.html)! »[Identifies what kind of team. This is to support differentiation between multiple co-existing teams, such as care plan team, episode of care team, longitudinal care teamcategory](careteam-definitions.html#CareTeam.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Indicates the type of care team. (Strength=Example)CareTeamCategory](valueset-care-team-category.html)?? »[A label for human use intended to distinguish like teams. E.g. the "red" vs. "green" trauma teamsname](careteam-definitions.html#CareTeam.name) : [string](datatypes.html#string) [0..1][Identifies the patient or group whose intended care is handled by the teamsubject](careteam-definitions.html#CareTeam.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this CareTeam was created or to which the creation of this record is tightly associatedencounter](careteam-definitions.html#CareTeam.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Indicates when the team did (or is intended to) come into effect and endperiod](careteam-definitions.html#CareTeam.period) : [Period](datatypes.html#Period) [0..1][Describes why the care team existsreasonCode](careteam-definitions.html#CareTeam.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Indicates the reason for the care team. (Strength=Example)SNOMEDCTClinicalFindings](valueset-clinical-findings.html)?? »[Condition(s) that this care team addressesreasonReference](careteam-definitions.html#CareTeam.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition) »[The organization responsible for the care teammanagingOrganization](careteam-definitions.html#CareTeam.managingOrganization) : [Reference](references.html#Reference) [0..*] « [Organization](organization.html#Organization) »[A central contact detail for the care team (that applies to all members)telecom](careteam-definitions.html#CareTeam.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Comments made about the CareTeamnote](careteam-definitions.html#CareTeam.note) : [Annotation](datatypes.html#Annotation) [0..*]Participant[Indicates specific responsibility of an individual within the care team, such as "Primary care physician", "Trained social worker counselor", "Caregiver", etcrole](careteam-definitions.html#CareTeam.participant.role) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Indicates specific responsibility of an individual within the care team, such as "Primary physician", "Team coordinator", "Caregiver", etc. (Strength=Example)ParticipantRoles](valueset-participant-role.html)?? »[The specific person or organization who is participating/expected to participate in the care teammember](careteam-definitions.html#CareTeam.participant.member) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam) »[The organization of the practitioneronBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Indicates when the specific member or organization did (or is intended to) come into effect and endperiod](careteam-definitions.html#CareTeam.participant.period) : [Period](datatypes.html#Period) [0..1]
[Identifies all people and organizations who are expected to be involved in the care teamparticipant](careteam-definitions.html#CareTeam.participant)[0..*]
 

 

 

**XML Template**

 

 
```
<[**CareTeam**](careteam-definitions.html#CareTeam) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](careteam-definitions.html#CareTeam.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External Ids for this team](terminologies.html#unbound) --></identifier>
 <[**status**](careteam-definitions.html#CareTeam.status) value="[[code](datatypes.html#code)]"/><!-- **0..1** [proposed | active | suspended | inactive | entered-in-error](valueset-care-team-status.html) -->
 <[**category**](careteam-definitions.html#CareTeam.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Type of team](valueset-care-team-category.html) --></category>
 <[**name**](careteam-definitions.html#CareTeam.name) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Name of the team, such as crisis assessment team](terminologies.html#unbound) -->
 <[**subject**](careteam-definitions.html#CareTeam.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Who care team is for](terminologies.html#unbound) --></subject>
 <[**encounter**](careteam-definitions.html#CareTeam.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**period**](careteam-definitions.html#CareTeam.period)><!-- **0..1** [Period](datatypes.html#Period) [Time period team covers](terminologies.html#unbound) --></period>
 <[**participant**](careteam-definitions.html#CareTeam.participant)> <!-- ** 0..*** Members of the team -->
 <[**role**](careteam-definitions.html#CareTeam.participant.role)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Type of involvement](valueset-participant-role.html) --></role>
 <[**member**](careteam-definitions.html#CareTeam.participant.member)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|
 [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) [Who is involved](terminologies.html#unbound) --></member>
 <[**onBehalfOf**](careteam-definitions.html#CareTeam.participant.onBehalfOf)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization of the practitioner](terminologies.html#unbound) --></onBehalfOf>
 <[**period**](careteam-definitions.html#CareTeam.participant.period)><!-- **0..1** [Period](datatypes.html#Period) [Time period of participant](terminologies.html#unbound) --></period>
 </participant>
 <[**reasonCode**](careteam-definitions.html#CareTeam.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Why the care team exists](valueset-clinical-findings.html) --></reasonCode>
 <[**reasonReference**](careteam-definitions.html#CareTeam.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)) [Why the care team exists](terminologies.html#unbound) --></reasonReference>
 <[**managingOrganization**](careteam-definitions.html#CareTeam.managingOrganization)><!-- **0..*** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization responsible for the care team](terminologies.html#unbound) --></managingOrganization>
 <[**telecom**](careteam-definitions.html#CareTeam.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the care team (that applies to all members)](terminologies.html#unbound) --></telecom>
 <[**note**](careteam-definitions.html#CareTeam.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the CareTeam](terminologies.html#unbound) --></note>
</CareTeam>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**CareTeam**](careteam-definitions.html#CareTeam)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](careteam-definitions.html#CareTeam.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this team](terminologies.html#unbound)
 "[status](careteam-definitions.html#CareTeam.status)" : "<[code](datatypes.html#code)>", // [proposed | active | suspended | inactive | entered-in-error](valueset-care-team-status.html)
 "[category](careteam-definitions.html#CareTeam.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Type of team](valueset-care-team-category.html)
 "[name](careteam-definitions.html#CareTeam.name)" : "<[string](datatypes.html#string)>", // [Name of the team, such as crisis assessment team](terminologies.html#unbound)
 "[subject](careteam-definitions.html#CareTeam.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [Who care team is for](terminologies.html#unbound)
 "[encounter](careteam-definitions.html#CareTeam.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[period](careteam-definitions.html#CareTeam.period)" : { [Period](datatypes.html#Period) }, // [Time period team covers](terminologies.html#unbound)
 "[participant](careteam-definitions.html#CareTeam.participant)" : [{ // **C?** [Members of the team](terminologies.html#unbound)
 "[role](careteam-definitions.html#CareTeam.participant.role)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Type of involvement](valueset-participant-role.html)
 "[member](careteam-definitions.html#CareTeam.participant.member)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|
 [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) }, // [Who is involved](terminologies.html#unbound)
 "[onBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization of the practitioner](terminologies.html#unbound)
 "[period](careteam-definitions.html#CareTeam.participant.period)" : { [Period](datatypes.html#Period) } // [Time period of participant](terminologies.html#unbound)
 }],
 "[reasonCode](careteam-definitions.html#CareTeam.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Why the care team exists](valueset-clinical-findings.html)
 "[reasonReference](careteam-definitions.html#CareTeam.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)) }], // [Why the care team exists](terminologies.html#unbound)
 "[managingOrganization](careteam-definitions.html#CareTeam.managingOrganization)" : [{ [Reference](references.html#Reference)([Organization](organization.html#Organization)) }], // [Organization responsible for the care team](terminologies.html#unbound)
 "[telecom](careteam-definitions.html#CareTeam.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the care team (that applies to all members)](terminologies.html#unbound)
 "[note](careteam-definitions.html#CareTeam.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about the CareTeam](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**CareTeam**](careteam-definitions.html#CareTeam);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[CareTeam.identifier](careteam-definitions.html#CareTeam.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this team
 fhir:[CareTeam.status](careteam-definitions.html#CareTeam.status) [ [code](datatypes.html#code) ]; # 0..1 proposed | active | suspended | inactive | entered-in-error
 fhir:[CareTeam.category](careteam-definitions.html#CareTeam.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Type of team
 fhir:[CareTeam.name](careteam-definitions.html#CareTeam.name) [ [string](datatypes.html#string) ]; # 0..1 Name of the team, such as crisis assessment team
 fhir:[CareTeam.subject](careteam-definitions.html#CareTeam.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 Who care team is for
 fhir:[CareTeam.encounter](careteam-definitions.html#CareTeam.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[CareTeam.period](careteam-definitions.html#CareTeam.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time period team covers
 fhir:[CareTeam.participant](careteam-definitions.html#CareTeam.participant) [ # 0..* Members of the team
 fhir:[CareTeam.participant.role](careteam-definitions.html#CareTeam.participant.role) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Type of involvement
 fhir:[CareTeam.participant.member](careteam-definitions.html#CareTeam.participant.member) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) ]; # 0..1 Who is involved
 fhir:[CareTeam.participant.onBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization of the practitioner
 fhir:[CareTeam.participant.period](careteam-definitions.html#CareTeam.participant.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time period of participant
 ], ...;
 fhir:[CareTeam.reasonCode](careteam-definitions.html#CareTeam.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Why the care team exists
 fhir:[CareTeam.reasonReference](careteam-definitions.html#CareTeam.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)) ], ... ; # 0..* Why the care team exists
 fhir:[CareTeam.managingOrganization](careteam-definitions.html#CareTeam.managingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ], ... ; # 0..* Organization responsible for the care team
 fhir:[CareTeam.telecom](careteam-definitions.html#CareTeam.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the care team (that applies to all members)
 fhir:[CareTeam.note](careteam-definitions.html#CareTeam.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the CareTeam
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [CareTeam](careteam.html#CareTeam)
 | 
 | 
 |

 | 
 CareTeam.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/care-team-status to http://hl7.org/fhir/ValueSet/care-team-status|4.0.1

 

 | 
 |

 | 
 CareTeam.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 CareTeam.participant.role | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 CareTeam.participant.member | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 CareTeam.telecom | 
 
 

 - Added Element

 

 | 
 |

 | 
 CareTeam.context | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](careteam.diff.xml) or [JSON](careteam.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](careteam-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [CareTeam](careteam-definitions.html#CareTeam) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Planned participants in the coordination and delivery of care for a patient or group**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](careteam-definitions.html#CareTeam.identifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Identifier](datatypes.html#Identifier) | External Ids for this team
 | |

| [status](careteam-definitions.html#CareTeam.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [code](datatypes.html#code) | proposed | active | suspended | inactive | entered-in-error
[CareTeamStatus](valueset-care-team-status.html) ([Required](terminologies.html#required)) | |

| [category](careteam-definitions.html#CareTeam.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of team
[Care Team category](valueset-care-team-category.html) ([Example](terminologies.html#example))
 | |

| [name](careteam-definitions.html#CareTeam.name) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Name of the team, such as crisis assessment team | |

| [subject](careteam-definitions.html#CareTeam.subject) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Group](group.html)) | Who care team is for | |

| [encounter](careteam-definitions.html#CareTeam.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounter created as part of | |

| [period](careteam-definitions.html#CareTeam.period) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Time period team covers | |

| [participant](careteam-definitions.html#CareTeam.participant) | [I](conformance-rules.html#constraints) | 0..* | [BackboneElement](backboneelement.html) | Members of the team
+ Rule: CareTeam.participant.onBehalfOf can only be populated when CareTeam.participant.member is a Practitioner
 | |

| [role](careteam-definitions.html#CareTeam.participant.role) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of involvement
[Participant Roles](valueset-participant-role.html) ([Example](terminologies.html#example))
 | |

| [member](careteam-definitions.html#CareTeam.participant.member) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Patient](patient.html) | [Organization](organization.html) | [CareTeam](careteam.html)) | Who is involved | |

| [onBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization of the practitioner | |

| [period](careteam-definitions.html#CareTeam.participant.period) | | 0..1 | [Period](datatypes.html#Period) | Time period of participant | |

| [reasonCode](careteam-definitions.html#CareTeam.reasonCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Why the care team exists
[SNOMED CT Clinical Findings](valueset-clinical-findings.html) ([Example](terminologies.html#example))
 | |

| [reasonReference](careteam-definitions.html#CareTeam.reasonReference) | | 0..* | [Reference](references.html#Reference)([Condition](condition.html)) | Why the care team exists
 | |

| [managingOrganization](careteam-definitions.html#CareTeam.managingOrganization) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for the care team
 | |

| [telecom](careteam-definitions.html#CareTeam.telecom) | | 0..* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the care team (that applies to all members)
 | |

| [note](careteam-definitions.html#CareTeam.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the CareTeam
 | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - CareTeam ([DomainResource](domainresource.html))[Business identifiers assigned to this care team by the performer or other systems which remain constant as the resource is updated and propagates from server to serveridentifier](careteam-definitions.html#CareTeam.identifier) : [Identifier](datatypes.html#Identifier) [0..*][Indicates the current state of the care team (this element modifies the meaning of other elements)status](careteam-definitions.html#CareTeam.status) : [code](datatypes.html#code) [0..1] « [Indicates the status of the care team. (Strength=Required)CareTeamStatus](valueset-care-team-status.html)! »[Identifies what kind of team. This is to support differentiation between multiple co-existing teams, such as care plan team, episode of care team, longitudinal care teamcategory](careteam-definitions.html#CareTeam.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Indicates the type of care team. (Strength=Example)CareTeamCategory](valueset-care-team-category.html)?? »[A label for human use intended to distinguish like teams. E.g. the "red" vs. "green" trauma teamsname](careteam-definitions.html#CareTeam.name) : [string](datatypes.html#string) [0..1][Identifies the patient or group whose intended care is handled by the teamsubject](careteam-definitions.html#CareTeam.subject) : [Reference](references.html#Reference) [0..1] « [Patient](patient.html#Patient)|[Group](group.html#Group) »[The Encounter during which this CareTeam was created or to which the creation of this record is tightly associatedencounter](careteam-definitions.html#CareTeam.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Indicates when the team did (or is intended to) come into effect and endperiod](careteam-definitions.html#CareTeam.period) : [Period](datatypes.html#Period) [0..1][Describes why the care team existsreasonCode](careteam-definitions.html#CareTeam.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Indicates the reason for the care team. (Strength=Example)SNOMEDCTClinicalFindings](valueset-clinical-findings.html)?? »[Condition(s) that this care team addressesreasonReference](careteam-definitions.html#CareTeam.reasonReference) : [Reference](references.html#Reference) [0..*] « [Condition](condition.html#Condition) »[The organization responsible for the care teammanagingOrganization](careteam-definitions.html#CareTeam.managingOrganization) : [Reference](references.html#Reference) [0..*] « [Organization](organization.html#Organization) »[A central contact detail for the care team (that applies to all members)telecom](careteam-definitions.html#CareTeam.telecom) : [ContactPoint](datatypes.html#ContactPoint) [0..*][Comments made about the CareTeamnote](careteam-definitions.html#CareTeam.note) : [Annotation](datatypes.html#Annotation) [0..*]Participant[Indicates specific responsibility of an individual within the care team, such as "Primary care physician", "Trained social worker counselor", "Caregiver", etcrole](careteam-definitions.html#CareTeam.participant.role) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Indicates specific responsibility of an individual within the care team, such as "Primary physician", "Team coordinator", "Caregiver", etc. (Strength=Example)ParticipantRoles](valueset-participant-role.html)?? »[The specific person or organization who is participating/expected to participate in the care teammember](careteam-definitions.html#CareTeam.participant.member) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam) »[The organization of the practitioneronBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[Indicates when the specific member or organization did (or is intended to) come into effect and endperiod](careteam-definitions.html#CareTeam.participant.period) : [Period](datatypes.html#Period) [0..1]
[Identifies all people and organizations who are expected to be involved in the care teamparticipant](careteam-definitions.html#CareTeam.participant)[0..*]
 

**XML Template**

 

 
```
<[**CareTeam**](careteam-definitions.html#CareTeam) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](careteam-definitions.html#CareTeam.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [External Ids for this team](terminologies.html#unbound) --></identifier>
 <[**status**](careteam-definitions.html#CareTeam.status) value="[[code](datatypes.html#code)]"/><!-- **0..1** [proposed | active | suspended | inactive | entered-in-error](valueset-care-team-status.html) -->
 <[**category**](careteam-definitions.html#CareTeam.category)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Type of team](valueset-care-team-category.html) --></category>
 <[**name**](careteam-definitions.html#CareTeam.name) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Name of the team, such as crisis assessment team](terminologies.html#unbound) -->
 <[**subject**](careteam-definitions.html#CareTeam.subject)><!-- **0..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) [Who care team is for](terminologies.html#unbound) --></subject>
 <[**encounter**](careteam-definitions.html#CareTeam.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounter created as part of](terminologies.html#unbound) --></encounter>
 <[**period**](careteam-definitions.html#CareTeam.period)><!-- **0..1** [Period](datatypes.html#Period) [Time period team covers](terminologies.html#unbound) --></period>
 <[**participant**](careteam-definitions.html#CareTeam.participant)> <!-- ** 0..*** Members of the team -->
 <[**role**](careteam-definitions.html#CareTeam.participant.role)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Type of involvement](valueset-participant-role.html) --></role>
 <[**member**](careteam-definitions.html#CareTeam.participant.member)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|
 [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) [Who is involved](terminologies.html#unbound) --></member>
 <[**onBehalfOf**](careteam-definitions.html#CareTeam.participant.onBehalfOf)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization of the practitioner](terminologies.html#unbound) --></onBehalfOf>
 <[**period**](careteam-definitions.html#CareTeam.participant.period)><!-- **0..1** [Period](datatypes.html#Period) [Time period of participant](terminologies.html#unbound) --></period>
 </participant>
 <[**reasonCode**](careteam-definitions.html#CareTeam.reasonCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Why the care team exists](valueset-clinical-findings.html) --></reasonCode>
 <[**reasonReference**](careteam-definitions.html#CareTeam.reasonReference)><!-- **0..*** [Reference](references.html#Reference)([Condition](condition.html#Condition)) [Why the care team exists](terminologies.html#unbound) --></reasonReference>
 <[**managingOrganization**](careteam-definitions.html#CareTeam.managingOrganization)><!-- **0..*** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Organization responsible for the care team](terminologies.html#unbound) --></managingOrganization>
 <[**telecom**](careteam-definitions.html#CareTeam.telecom)><!-- **0..*** [ContactPoint](datatypes.html#ContactPoint) [A contact detail for the care team (that applies to all members)](terminologies.html#unbound) --></telecom>
 <[**note**](careteam-definitions.html#CareTeam.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the CareTeam](terminologies.html#unbound) --></note>
</CareTeam>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**CareTeam**](careteam-definitions.html#CareTeam)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](careteam-definitions.html#CareTeam.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [External Ids for this team](terminologies.html#unbound)
 "[status](careteam-definitions.html#CareTeam.status)" : "<[code](datatypes.html#code)>", // [proposed | active | suspended | inactive | entered-in-error](valueset-care-team-status.html)
 "[category](careteam-definitions.html#CareTeam.category)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Type of team](valueset-care-team-category.html)
 "[name](careteam-definitions.html#CareTeam.name)" : "<[string](datatypes.html#string)>", // [Name of the team, such as crisis assessment team](terminologies.html#unbound)
 "[subject](careteam-definitions.html#CareTeam.subject)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) }, // [Who care team is for](terminologies.html#unbound)
 "[encounter](careteam-definitions.html#CareTeam.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Encounter created as part of](terminologies.html#unbound)
 "[period](careteam-definitions.html#CareTeam.period)" : { [Period](datatypes.html#Period) }, // [Time period team covers](terminologies.html#unbound)
 "[participant](careteam-definitions.html#CareTeam.participant)" : [{ // **C?** [Members of the team](terminologies.html#unbound)
 "[role](careteam-definitions.html#CareTeam.participant.role)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Type of involvement](valueset-participant-role.html)
 "[member](careteam-definitions.html#CareTeam.participant.member)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|
 [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) }, // [Who is involved](terminologies.html#unbound)
 "[onBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Organization of the practitioner](terminologies.html#unbound)
 "[period](careteam-definitions.html#CareTeam.participant.period)" : { [Period](datatypes.html#Period) } // [Time period of participant](terminologies.html#unbound)
 }],
 "[reasonCode](careteam-definitions.html#CareTeam.reasonCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Why the care team exists](valueset-clinical-findings.html)
 "[reasonReference](careteam-definitions.html#CareTeam.reasonReference)" : [{ [Reference](references.html#Reference)([Condition](condition.html#Condition)) }], // [Why the care team exists](terminologies.html#unbound)
 "[managingOrganization](careteam-definitions.html#CareTeam.managingOrganization)" : [{ [Reference](references.html#Reference)([Organization](organization.html#Organization)) }], // [Organization responsible for the care team](terminologies.html#unbound)
 "[telecom](careteam-definitions.html#CareTeam.telecom)" : [{ [ContactPoint](datatypes.html#ContactPoint) }], // [A contact detail for the care team (that applies to all members)](terminologies.html#unbound)
 "[note](careteam-definitions.html#CareTeam.note)" : [{ [Annotation](datatypes.html#Annotation) }] // [Comments made about the CareTeam](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**CareTeam**](careteam-definitions.html#CareTeam);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[CareTeam.identifier](careteam-definitions.html#CareTeam.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* External Ids for this team
 fhir:[CareTeam.status](careteam-definitions.html#CareTeam.status) [ [code](datatypes.html#code) ]; # 0..1 proposed | active | suspended | inactive | entered-in-error
 fhir:[CareTeam.category](careteam-definitions.html#CareTeam.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Type of team
 fhir:[CareTeam.name](careteam-definitions.html#CareTeam.name) [ [string](datatypes.html#string) ]; # 0..1 Name of the team, such as crisis assessment team
 fhir:[CareTeam.subject](careteam-definitions.html#CareTeam.subject) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Group](group.html#Group)) ]; # 0..1 Who care team is for
 fhir:[CareTeam.encounter](careteam-definitions.html#CareTeam.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Encounter created as part of
 fhir:[CareTeam.period](careteam-definitions.html#CareTeam.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time period team covers
 fhir:[CareTeam.participant](careteam-definitions.html#CareTeam.participant) [ # 0..* Members of the team
 fhir:[CareTeam.participant.role](careteam-definitions.html#CareTeam.participant.role) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Type of involvement
 fhir:[CareTeam.participant.member](careteam-definitions.html#CareTeam.participant.member) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Patient](patient.html#Patient)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)) ]; # 0..1 Who is involved
 fhir:[CareTeam.participant.onBehalfOf](careteam-definitions.html#CareTeam.participant.onBehalfOf) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Organization of the practitioner
 fhir:[CareTeam.participant.period](careteam-definitions.html#CareTeam.participant.period) [ [Period](datatypes.html#Period) ]; # 0..1 Time period of participant
 ], ...;
 fhir:[CareTeam.reasonCode](careteam-definitions.html#CareTeam.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Why the care team exists
 fhir:[CareTeam.reasonReference](careteam-definitions.html#CareTeam.reasonReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)) ], ... ; # 0..* Why the care team exists
 fhir:[CareTeam.managingOrganization](careteam-definitions.html#CareTeam.managingOrganization) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ], ... ; # 0..* Organization responsible for the care team
 fhir:[CareTeam.telecom](careteam-definitions.html#CareTeam.telecom) [ [ContactPoint](datatypes.html#ContactPoint) ], ... ; # 0..* A contact detail for the care team (that applies to all members)
 fhir:[CareTeam.note](careteam-definitions.html#CareTeam.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the CareTeam
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [CareTeam](careteam.html#CareTeam)
 | 
 | 
 |

 | 
 CareTeam.status | 
 
 

 Change value set from http://hl7.org/fhir/ValueSet/care-team-status to http://hl7.org/fhir/ValueSet/care-team-status|4.0.1

 

 | 
 |

 | 
 CareTeam.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 CareTeam.participant.role | 
 
 

 - Max Cardinality changed from 1 to *

 

 | 
 |

 | 
 CareTeam.participant.member | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 CareTeam.telecom | 
 
 

 - Added Element

 

 | 
 |

 | 
 CareTeam.context | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](careteam.diff.xml) or [JSON](careteam.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](careteam-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](careteam-profiles.html) and the alternate definitions:
Master Definition [XML](careteam.profile.xml.html) + [JSON](careteam.profile.json.html),
[XML](xml.html) [Schema](careteam.xsd)/[Schematron](careteam.sch) + [JSON](json.html) 
[Schema](careteam.schema.json.html), [ShEx](careteam.shex.html) (for [Turtle](rdf.html)) + [see the extensions](careteam-profiles.html) & the [dependency analysis](careteam-dependencies.html)

### 9.7.3.1 
Terminology Bindings
 [
](careteam.html#tx)

 | Path | Definition | Type | Reference | |

 | CareTeam.status | Indicates the status of the care team. | [Required](terminologies.html#required) | [CareTeamStatus](valueset-care-team-status.html) | |

 | CareTeam.category | Indicates the type of care team. | [Example](terminologies.html#example) | [CareTeamCategory](valueset-care-team-category.html) | |

 | CareTeam.participant.role | Indicates specific responsibility of an individual within the care team, such as "Primary physician", "Team coordinator", "Caregiver", etc. | [Example](terminologies.html#example) | [ParticipantRoles](valueset-participant-role.html) | |

 | CareTeam.reasonCode | Indicates the reason for the care team. | [Example](terminologies.html#example) | [SNOMEDCTClinicalFindings](valueset-clinical-findings.html) | |

 

 

### 9.7.3.2 Constraints [
](careteam.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **ctm-1** | [Rule](conformance-rules.html#rule) | CareTeam.participant | CareTeam.participant.onBehalfOf can only be populated when CareTeam.participant.member is a Practitioner | onBehalfOf.exists() implies (member.resolve().iif(empty(), true, ofType(Practitioner).exists())) | |

### 9.7.3.3 Notes [](careteam.html#9.7.3.3)

The [Provenance](provenance.html) resource can be used for detailed review information, such as when the care team was last reviewed and by whom. 

## 9.7.4 Search Parameters [
](careteam.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| category | [token](search.html#token) | Type of team | CareTeam.category | | |

| date | [date](search.html#date) | Time period team covers | CareTeam.period | [17 Resources](searchparameter-registry.html#clinical-date) | |

| encounter | [reference](search.html#reference) | Encounter created as part of | CareTeam.encounter
([Encounter](encounter.html)) | | |

| identifier | [token](search.html#token) | External Ids for this team | CareTeam.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier) | |

| participant | [reference](search.html#reference) | Who is involved | CareTeam.participant.member
([Practitioner](practitioner.html), [Organization](organization.html), [CareTeam](careteam.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| patient | [reference](search.html#reference) | Who care team is for | CareTeam.subject.where(resolve() is Patient)
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient) | |

| status | [token](search.html#token) | proposed | active | suspended | inactive | entered-in-error | CareTeam.status | | |

| subject | [reference](search.html#reference) | Who care team is for | CareTeam.subject
([Group](group.html), [Patient](patient.html)) | | |