# SmartAppLaunch : Validation Results

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/qa.html

---

# Validation Results for SmartAppLaunch

 
Generated Tue May 14 20:31:24 UTC 2024, FHIR version 4.0.1 for hl7.fhir.uv.smart-app-launch#2.2.0 (canonical = [http://hl7.org/fhir/smart-app-launch](http://hl7.org/fhir/smart-app-launch) ([history](http://hl7.org/fhir/smart-app-launch/history.html))). See [Errors Only](qa.min.html)

 | **Quality Checks** | |

 | Publisher Version: | IG Publisher Version: v1.6.7 | |

 | Publication Code: | smart-app-launch . PackageId = hl7.fhir.uv.smart-app-launch, Canonical = http://hl7.org/fhir/smart-app-launch | |

 | Realm Check for UV: | Error: realms in canonical and package id are different: uv vs fhir
- n/a

 | |

 | Publication Request: | 
- Version 2.2.0 has already been published *

- Publication Request is for version v2.2.0 which is already published 

 | |

 | Supressed Messages: | [41 Suppressed Issues](#suppressed)
 | |

 | Dependency Checks: | 

| Package | Version | FHIR | Canonical | Web Base | Comment | |
| hl7.fhir.uv.smart-app-launch | 2.2.0 | [R4](http://hl7.org/fhir/R4) | http://hl7.org/fhir/smart-app-launch | | | |

| hl7.fhir.uv.extensions | 5.1.0 M | [R5](http://hl7.org/fhir/R5) | http://hl7.org/fhir/extensions | http://hl7.org/fhir/extensions/5.1.0 | FHIR Version Mismatch | |

| hl7.terminology.r5 | 5.5.0 M | [R5](http://hl7.org/fhir/R5) | http://terminology.hl7.org | http://terminology.hl7.org/5.5.0 | FHIR Version Mismatch | |

| hl7.terminology | 5.5.0 M | [R4](http://hl7.org/fhir/R4) | http://terminology.hl7.org | http://terminology.hl7.org/5.5.0 | | |

| hl7.fhir.uv.extensions.r4 | 1.0.0 O | [R4](http://hl7.org/fhir/R4) | http://hl7.org/fhir/extensions | http://hl7.org/fhir/extensions/1.0.0 | Latest Release is 5.1.0 | |

Templates: hl7.smart.template#0.0.1 -> hl7.fhir.template#current -> hl7.base.template#current -> fhir.base.template#current. Tools: 0.1.0
|

 | Dependent IGs: | [10 guides](qa-dep.html) | |

 | Global Profiles: | (none declared) | |

 | Terminology Server(s): | [http://tx.fhir.org/r4](http://tx.fhir.org/r4) ([details](qa-txservers.html)) | |

 | HTA Analysis: | no Non-HL7 references found* | |

 | R5 Dependencies: | (none) | |

 | Draft Dependencies: | 

 - 
hl7.fhir.r4.core#4.0.1: [GuideParameterCode](http://hl7.org/fhir/R4/codesystem-guide-parameter-code.html)
 (15 uses), [Organization](http://hl7.org/fhir/R4/organization.html)
 (13 uses), [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html)
 (6 uses), [OrganizationType](http://hl7.org/fhir/R4/valueset-organization-type.html)
 (1 uses), [ContactEntityType](http://hl7.org/fhir/R4/valueset-contactentity-type.html)
 (1 uses), [Basic](http://hl7.org/fhir/R4/basic.html)
 (1 uses), [BasicResourceTypes](http://hl7.org/fhir/R4/valueset-basic-resource-type.html)
 (1 uses), [Practitioner](http://hl7.org/fhir/R4/practitioner.html)
 (7 uses), [PractitionerRole](http://hl7.org/fhir/R4/practitionerrole.html)
 (7 uses), [RelatedPerson](http://hl7.org/fhir/R4/relatedperson.html)
 (7 uses), [Task](http://hl7.org/fhir/R4/task.html)
 (6 uses), [ActivityDefinition](http://hl7.org/fhir/R4/activitydefinition.html)
 (2 uses), [TaskStatus](http://hl7.org/fhir/R4/valueset-task-status.html)
 (2 uses), [TaskIntent](http://hl7.org/fhir/R4/valueset-task-intent.html)
 (2 uses), [RequestPriority](http://hl7.org/fhir/R4/valueset-request-priority.html)
 (2 uses), [Encounter](http://hl7.org/fhir/R4/encounter.html)
 (2 uses), [Device](http://hl7.org/fhir/R4/device.html)
 (4 uses), [ProcedurePerformerRoleCodes](http://hl7.org/fhir/R4/valueset-performer-role.html)
 (2 uses), [CareTeam](http://hl7.org/fhir/R4/careteam.html)
 (2 uses), [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html)
 (2 uses), [Location](http://hl7.org/fhir/R4/location.html)
 (2 uses), [Coverage](http://hl7.org/fhir/R4/coverage.html)
 (2 uses), [ClaimResponse](http://hl7.org/fhir/R4/claimresponse.html)
 (2 uses), [Provenance](http://hl7.org/fhir/R4/provenance.html)
 (2 uses), [Group](http://hl7.org/fhir/R4/group.html)
 (2 uses), [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html)
 (1 uses), [Endpoint](http://hl7.org/fhir/R4/endpoint.html)
 (1 uses), [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html)
 (1 uses), [EndpointConnectionType](http://hl7.org/fhir/R4/valueset-endpoint-connection-type.html)
 (1 uses), [EndpointPayloadType](http://hl7.org/fhir/R4/valueset-endpoint-payload-type.html)
 (1 uses)
 

 - 
hl7.fhir.uv.tools#0.2.0: [ResourceSortExt](http://hl7.org/fhir/tools/0.2.0/StructureDefinition-resource-sort.html)
 (18 uses)
 

 - 
hl7.terminology#5.5.0: [OrganizationType](http://terminology.hl7.org/5.5.0/CodeSystem-organization-type.html)
 (8 uses), [EndpointConnectionType](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-connection-type.html)
 (8 uses), [EndpointPayloadType](http://terminology.hl7.org/5.5.0/CodeSystem-endpoint-payload-type.html)
 (8 uses)
 

 | |

 | Modifier Extensions: | (none) | |

 | Previous Version Comparison: | | |

 | IPA Comparison: | n/a | |

 | IPS Comparison: | n/a | |

| Narratives Suppressed | [Basic/app-state](Basic-app-state.html), [Bundle/example1](Bundle-example1.html), [Bundle/example2](Bundle-example2.html), [Bundle/example3](Bundle-example3.html), [Bundle/example4](Bundle-example4.html), [Task/task-for-ehr-launch](Task-task-for-ehr-launch.html), [Task/task-for-standalone-launch](Task-task-for-standalone-launch.html) | |
| Summary: | errors = 0, warn = 0, info = 0, broken links = 0 | |

 

 | 
 **Filename** | **Errors** | **Warnings** | **Hints** | 
 |

 | 
 [**Build Errors**](#internal) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/Basic-app-state**](#_scratch_repo_input_resources_Basic-app-state) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/Bundle-example1**](#_scratch_repo_input_resources_Bundle-example1) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/Bundle-example2**](#_scratch_repo_input_resources_Bundle-example2) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/Bundle-example3**](#_scratch_repo_input_resources_Bundle-example3) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/Bundle-example4**](#_scratch_repo_input_resources_Bundle-example4) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/CapabilityStatement-smart-app-state-server**](#_scratch_repo_input_resources_CapabilityStatement-smart-app-state-server) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/CodeSystem-smart-codes**](#_scratch_repo_input_resources_CodeSystem-smart-codes) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/ImplementationGuide-hl7.fhir.uv.smart-app-launch**](#_scratch_repo_input_resources_ImplementationGuide-hl7.fhir.uv.smart-app-launch) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/StructureDefinition-patient-access-brand**](#_scratch_repo_input_resources_StructureDefinition-patient-access-brand) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/StructureDefinition-smart-app-state-basic**](#_scratch_repo_input_resources_StructureDefinition-smart-app-state-basic) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/StructureDefinition-task-ehr-launch**](#_scratch_repo_input_resources_StructureDefinition-task-ehr-launch) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/StructureDefinition-task-standalone-launch**](#_scratch_repo_input_resources_StructureDefinition-task-standalone-launch) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/StructureDefinition-user-access-brands-bundle**](#_scratch_repo_input_resources_StructureDefinition-user-access-brands-bundle) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/StructureDefinition-user-access-endpoint**](#_scratch_repo_input_resources_StructureDefinition-user-access-endpoint) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/Task-task-for-ehr-launch**](#_scratch_repo_input_resources_Task-task-for-ehr-launch) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/Task-task-for-standalone-launch**](#_scratch_repo_input_resources_Task-task-for-standalone-launch) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/ValueSet-smart-launch-info**](#_scratch_repo_input_resources_ValueSet-smart-launch-info) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/ValueSet-smart-launch-types**](#_scratch_repo_input_resources_ValueSet-smart-launch-types) | **0** | **0** | **0** | 
 |

 | 
 [**/scratch/repo/input/resources/ValueSet-user-access-category**](#_scratch_repo_input_resources_ValueSet-user-access-category) | **0** | **0** | **0** | 
 |

---

 

## [n/a]() Show Validation Information 

 

 

---

 

## [input/resources/Basic-app-state.json](Basic-app-state.html) Show Validation Information (1)

 

- Basic: Validated against *this.*[SMART App State](StructureDefinition-smart-app-state-basic.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/Bundle-example1.json](Bundle-example1.html) Show Validation Information (5)

 

- Bundle: Validated against *this.*[User Access Brands Bundle Profile](StructureDefinition-user-access-brands-bundle.html)
- Bundle.entry[0].resource: Validated against *this.*[User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html) and [fhir](http://hl7.org/fhir).[Organization](http://hl7.org/fhir/R4/organization.html)
- Bundle.entry[1].resource: Validated against *this.*[User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html) and [fhir](http://hl7.org/fhir).[Endpoint](http://hl7.org/fhir/R4/endpoint.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/Bundle-example2.json](Bundle-example2.html) Show Validation Information (11)

 

- Bundle: Validated against *this.*[User Access Brands Bundle Profile](StructureDefinition-user-access-brands-bundle.html)
- Bundle.entry[0].resource: Validated against *this.*[User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html) and [fhir](http://hl7.org/fhir).[Organization](http://hl7.org/fhir/R4/organization.html)
- Bundle.entry[1].resource: Validated against *this.*[User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html) and [fhir](http://hl7.org/fhir).[Organization](http://hl7.org/fhir/R4/organization.html)
- Bundle.entry[2].resource: Validated against *this.*[User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html) and [fhir](http://hl7.org/fhir).[Organization](http://hl7.org/fhir/R4/organization.html)
- Bundle.entry[3].resource: Validated against *this.*[User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html) and [fhir](http://hl7.org/fhir).[Endpoint](http://hl7.org/fhir/R4/endpoint.html)
- Bundle.entry[4].resource: Validated against *this.*[User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html) and [fhir](http://hl7.org/fhir).[Endpoint](http://hl7.org/fhir/R4/endpoint.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/Bundle-example3.json](Bundle-example3.html) Show Validation Information (7)

 

- Bundle: Validated against *this.*[User Access Brands Bundle Profile](StructureDefinition-user-access-brands-bundle.html)
- Bundle.entry[0].resource: Validated against *this.*[User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html) and [fhir](http://hl7.org/fhir).[Organization](http://hl7.org/fhir/R4/organization.html)
- Bundle.entry[1].resource: Validated against *this.*[User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html) and [fhir](http://hl7.org/fhir).[Endpoint](http://hl7.org/fhir/R4/endpoint.html)
- Bundle.entry[2].resource: Validated against *this.*[User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html) and [fhir](http://hl7.org/fhir).[Endpoint](http://hl7.org/fhir/R4/endpoint.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/Bundle-example4.json](Bundle-example4.html) Show Validation Information (7)

 

- Bundle: Validated against *this.*[User Access Brands Bundle Profile](StructureDefinition-user-access-brands-bundle.html)
- Bundle.entry[0].resource: Validated against *this.*[User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html) and [fhir](http://hl7.org/fhir).[Organization](http://hl7.org/fhir/R4/organization.html)
- Bundle.entry[1].resource: Validated against *this.*[User Access Brand (Organization) Profile](StructureDefinition-user-access-brand.html) and [fhir](http://hl7.org/fhir).[Organization](http://hl7.org/fhir/R4/organization.html)
- Bundle.entry[2].resource: Validated against *this.*[User Access Endpoint Profile](StructureDefinition-user-access-endpoint.html) and [fhir](http://hl7.org/fhir).[Endpoint](http://hl7.org/fhir/R4/endpoint.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/CapabilityStatement-smart-app-state-server.json](CapabilityStatement-smart-app-state-server.html) Show Validation Information (1)

 

- CapabilityStatement: Validated against [fhir](http://hl7.org/fhir).[CapabilityStatement](http://hl7.org/fhir/R4/capabilitystatement.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/CodeSystem-smart-codes.json](CodeSystem-smart-codes.html) Show Validation Information (1)

 

- CodeSystem: Validated against [fhir](http://hl7.org/fhir).[CodeSystem](http://hl7.org/fhir/R4/codesystem.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/ImplementationGuide-hl7.fhir.uv.smart-app-launch.json](index.html) Show Validation Information (1)

 

- ImplementationGuide/hl7.fhir.uv.smart-app-launch: ImplementationGuide: Validated against [fhir](http://hl7.org/fhir).[ImplementationGuide](http://hl7.org/fhir/R4/implementationguide.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/StructureDefinition-patient-access-brand.json](StructureDefinition-user-access-brand.html) Show Validation Information (1)

 

- StructureDefinition: Validated against [fhir](http://hl7.org/fhir).[StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/StructureDefinition-smart-app-state-basic.json](StructureDefinition-smart-app-state-basic.html) Show Validation Information (1)

 

- StructureDefinition: Validated against [fhir](http://hl7.org/fhir).[StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/StructureDefinition-task-ehr-launch.json](StructureDefinition-task-ehr-launch.html) Show Validation Information (1)

 

- StructureDefinition: Validated against [fhir](http://hl7.org/fhir).[StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/StructureDefinition-task-standalone-launch.json](StructureDefinition-task-standalone-launch.html) Show Validation Information (1)

 

- StructureDefinition: Validated against [fhir](http://hl7.org/fhir).[StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/StructureDefinition-user-access-brands-bundle.json](StructureDefinition-user-access-brands-bundle.html) Show Validation Information (1)

 

- StructureDefinition: Validated against [fhir](http://hl7.org/fhir).[StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/StructureDefinition-user-access-endpoint.json](StructureDefinition-user-access-endpoint.html) Show Validation Information (1)

 

- StructureDefinition: Validated against [fhir](http://hl7.org/fhir).[StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/Task-task-for-ehr-launch.json](Task-task-for-ehr-launch.html) Show Validation Information (1)

 

- Task: Validated against *this.*[TaskEhrLaunch](StructureDefinition-task-ehr-launch.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/Task-task-for-standalone-launch.json](Task-task-for-standalone-launch.html) Show Validation Information (1)

 

- Task: Validated against *this.*[TaskStandaloneLaunch](StructureDefinition-task-standalone-launch.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/ValueSet-smart-launch-info.json](ValueSet-smart-launch-info.html) Show Validation Information (1)

 

- ValueSet: Validated against [fhir](http://hl7.org/fhir).[ValueSet](http://hl7.org/fhir/R4/valueset.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/ValueSet-smart-launch-types.json](ValueSet-smart-launch-types.html) Show Validation Information (1)

 

- ValueSet: Validated against [fhir](http://hl7.org/fhir).[ValueSet](http://hl7.org/fhir/R4/valueset.html)

 

 | 
 ✓ | 
 |

---

 

## [input/resources/ValueSet-user-access-category.json](ValueSet-user-access-category.html) Show Validation Information (1)

 

- ValueSet: Validated against [fhir](http://hl7.org/fhir).[ValueSet](http://hl7.org/fhir/R4/valueset.html)

 

 | 
 ✓ | 
 |

 
**Suppressed Messages (Warnings, hints, broken links)**

**Example URI in example.org domain does not need to be validated**

 - INFORMATION: Basic/app-state: Basic.code.coding[0].system: A definition for CodeSystem 'https://myapp.example.org' could not be found, so the code cannot be validated (1 uses)

**Examples are validated in the context of their Brand Bundles**

 - INFORMATION: StructureDefinition.where(url = 'http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-brand'): The Implementation Guide contains no explicitly linked examples for this profile (1 uses)

 - INFORMATION: StructureDefinition.where(url = 'http://hl7.org/fhir/smart-app-launch/StructureDefinition/user-access-endpoint'): The Implementation Guide contains no explicitly linked examples for this profile (1 uses)

**Ignoring info about references to draft code system for Organization type, since we've beek asked to use this draft code system**

 - INFORMATION: Bundle/example1: Bundle.entry[0].resource/*Organization/examplelabs*/.type[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/organization-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example1: Bundle.entry[1].resource/*Endpoint/examplelabs*/.payloadType[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example2: Bundle.entry[0].resource/*Organization/examplehealth*/.type[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/organization-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example2: Bundle.entry[1].resource/*Organization/ehchospital*/.type[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/organization-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example2: Bundle.entry[2].resource/*Organization/ehpmadison*/.type[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/organization-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example2: Bundle.entry[3].resource/*Endpoint/examplehealth-r2*/.payloadType[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example2: Bundle.entry[4].resource/*Endpoint/examplehealth-r4*/.payloadType[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example3: Bundle.entry[0].resource/*Organization/examplehospital*/.type[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/organization-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example3: Bundle.entry[1].resource/*Endpoint/examplehospital-ehr1*/.payloadType[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example3: Bundle.entry[2].resource/*Endpoint/examplehospital-ehr2*/.payloadType[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example4: Bundle.entry[0].resource/*Organization/brand1*/.type[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/organization-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example4: Bundle.entry[1].resource/*Organization/brand2*/.type[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/organization-type|2.0.0 (1 uses)

 - INFORMATION: Bundle/example4: Bundle.entry[2].resource/*Endpoint/coequal-example*/.payloadType[0]: Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

 - INFORMATION: StructureDefinition/user-access-endpoint: StructureDefinition.differential.element[10].pattern.ofType(CodeableConcept): Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

 - INFORMATION: StructureDefinition/user-access-endpoint: StructureDefinition.differential.element[4].pattern.ofType(Coding): Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-connection-type|2.1.0 (1 uses)

 - INFORMATION: StructureDefinition/user-access-endpoint: StructureDefinition.snapshot.element[12].pattern.ofType(Coding): Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-connection-type|2.1.0 (1 uses)

 - INFORMATION: StructureDefinition/user-access-endpoint: StructureDefinition.snapshot.element[25].pattern.ofType(CodeableConcept): Reference to draft CodeSystem http://terminology.hl7.org/CodeSystem/endpoint-payload-type|2.0.0 (1 uses)

**The 'no narrative' parameter is used for these resources instances because they are infrastructural in nature and used in strictly managed trading systems where all systems share a common data model and additional text is unnecessary.**

 - WARNING: Basic/app-state: Basic: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example1: Bundle.entry[0].resource/*Organization/examplelabs*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example1: Bundle.entry[1].resource/*Endpoint/examplelabs*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example2: Bundle.entry[0].resource/*Organization/examplehealth*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example2: Bundle.entry[1].resource/*Organization/ehchospital*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example2: Bundle.entry[2].resource/*Organization/ehpmadison*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example2: Bundle.entry[3].resource/*Endpoint/examplehealth-r2*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example2: Bundle.entry[4].resource/*Endpoint/examplehealth-r4*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example3: Bundle.entry[0].resource/*Organization/examplehospital*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example3: Bundle.entry[1].resource/*Endpoint/examplehospital-ehr1*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example3: Bundle.entry[2].resource/*Endpoint/examplehospital-ehr2*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example4: Bundle.entry[0].resource/*Organization/brand1*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example4: Bundle.entry[1].resource/*Organization/brand2*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Bundle/example4: Bundle.entry[2].resource/*Endpoint/coequal-example*/: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Task/task-for-ehr-launch: Task: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

 - WARNING: Task/task-for-standalone-launch: Task: Constraint failed: dom-6: 'A resource should have narrative for robust management' (defined in http://hl7.org/fhir/StructureDefinition/DomainResource) (Best Practice Recommendation) (1 uses)

**These example resources have content that can be inferred, and a standalone examples page providing more detail**

 - WARNING: Unable to find ImplementationGuide.definition.resource.description for the resource Bundle/example1. Descriptions are strongly encouraged if they cannot be inferred from the resource to allow proper population of the artifact list. (1 uses)

 - WARNING: Unable to find ImplementationGuide.definition.resource.description for the resource Bundle/example2. Descriptions are strongly encouraged if they cannot be inferred from the resource to allow proper population of the artifact list. (1 uses)

 - WARNING: Unable to find ImplementationGuide.definition.resource.description for the resource Bundle/example3. Descriptions are strongly encouraged if they cannot be inferred from the resource to allow proper population of the artifact list. (1 uses)

 - WARNING: Unable to find ImplementationGuide.definition.resource.description for the resource Bundle/example4. Descriptions are strongly encouraged if they cannot be inferred from the resource to allow proper population of the artifact list. (1 uses)

**smart-codes is granted an exemption, details at https://confluence.hl7.org/display/TSMG/2024-03-18+TSMG+Agenda+and+Minutes**

 - INFORMATION: CodeSystem/smart-codes: CodeSystem: Most code systems defined in HL7 IGs will need to move to THO later during the process. Consider giving this code system a THO URL now (See https://confluence.hl7.org/display/TSMG/Terminology+Play+Book, and/or talk to TSMG) (1 uses)

 

**Errors sorted by type**