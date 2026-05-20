# Administration-module - FHIR v4.0.1

> Source: https://hl7.org/fhir/R4/administration-module.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions *](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/administration-module.html) [R4B](http://hl7.org/fhir/R4B/administration-module.html) **R4** [R3](http://hl7.org/fhir/STU3/administration-module.html)
 
 
| Work Group [Patient Administration ](http://www.hl7.org/Special/committees/pafm/index.cfm) | [Standards Status](versions.html#std-process): [Informative](versions.html#std-process) | |

 
 
## 8.0 Administration Module [
](administration-module.html#8.0)

 
 
### 8.0.1 Introduction [](administration-module.html#intro)

 
 The Administrative module covers the base data that is then linked into
 the other modules for clinical content, finance/billing, workflow, etc.**
 It is built on the FHIR technology platform modules.
 

 

 Before any clinical data can be recorded, the basic information of the patient
 must be recorded, and then often the basis of the interaction (such as an encounter).
 

 
 
### 8.0.2 Index [
](administration-module.html#index)

 

 | 
 
 

 - [Patient](patient.html)

 - [RelatedPerson](relatedperson.html)

 - [Person](person.html)

 - [Group](group.html)

 - [Practitioner](practitioner.html)

 - [PractitionerRole](practitionerrole.html)

 

 | 
 
 

 - [Organization](organization.html)

 - [Location](location.html)

 - [HealthcareService](healthcareservice.html)

 - [Endpoint](endpoint.html)

 - [Schedule](schedule.html)

 - [Slot](slot.html)

 

 | 
 
 

 - [EpisodeOfCare](episodeofcare.html)

 - [Encounter](encounter.html)

 - [Appointment](appointment.html)

 - [AppointmentResponse](appointmentresponse.html)

 - [Account](account.html)

 - [Flag](flag.html)

 

 | 
 
 

 - [Device](device.html)

 - [DeviceDefinition](devicedefinition.html)

 - [DeviceMetric](devicemetric.html)

 - [Substance](substance.html)

 

 | 
 |

 

 
 
#### 8.0.2.1 Patient Registers [](administration-module.html#patient-reg)

 
 Track people involved in receiving healthcare, the basics nearly everything else references back to
 

 

 | Name** | **Aliases** | **Description** | |

 | [Patient](patient.html) | SubjectOfCare Client Resident | Demographics and other administrative information about an individual or animal receiving care or other health-related services. | |

 | [RelatedPerson](relatedperson.html) | | Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process. | |

 | [Person](person.html) | | Demographics and administrative information about a person independent of a specific health-related context. | |

 | [Group](group.html) | | Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization. | |

 

 

 
 

**
 Implementation Note:** 
 [Patient linking](patient.html#links) should also be considered when evaluating
 searches with references to other resources. e.g. searching for a patients' conditions for a patient.**
 At present the specification does not define if the links should be also followed to include
 conditions that reference the linked patients too. We are currently seeking feedback on this.

> 
 Implementation Note:** 
 The Person resource may be used as a centralized register of people that may
 eventually be involved in healthcare, and could be used as the central core demographics register.**
 However, the fields/values in Person are duplicated in the other resources, and in many cases the
 Person resource will be hosted on external systems.

 
 
#### 8.0.2.2 Clinical Categorization Resources [
](administration-module.html#clinical-reg)

 
 Most clinical activities occur grouped in some way. Long term care is typically covered by an EpisodeOfCare, whereas short term care is covered by encounters. Account associates the tracking of transactions back to a Patient (or other resource). Flag is just used to highlight a warning or other notification about a patient (or other resource)
 

 

 | Name** | **Aliases** | **Description** | |

 | [EpisodeOfCare](episodeofcare.html) | Case Program Problem | An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time. | |

 | [Encounter](encounter.html) | Visit | An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient. | |

 | [Account](account.html) | Cost center | A financial tool for tracking value accrued for a particular purpose. In the healthcare field, used to track charges for a patient, cost centers, etc. | |

 | [Flag](flag.html) | Barriers to Care, Alert | Prospective warnings of potential issues when providing care to the patient. | |

 

 

 
 

**
 Implementation Note:** 
 Resources shown with a dotted box are described in other sections of the specification:
 `Coverage` and `Claim` are from the [section on Finance](financial-module.html).

 
 
#### 8.0.2.3 Service Provider Directory Resources [
](administration-module.html#dir-reg)

 
 Service Provider Directory resources are usually stored in the administration section of applications, and may even be synchronized from external systems.
 

 

 | **Name** | **Aliases** | **Description** | |

 | [Organization](organization.html) | | A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc. | |

 | [Location](location.html) | | Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated. | |

 | [Practitioner](practitioner.html) | | A person who is directly or indirectly involved in the provisioning of healthcare. | |

 | [PractitionerRole](practitionerrole.html) | | A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time. | |

 | [HealthcareService](healthcareservice.html) | | The details of a healthcare service available at a location. | |

 | [Endpoint](endpoint.html) | | The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information. | |

 

 

 
 

 

 
 
#### 8.0.2.4 Scheduling and Appointments [
](administration-module.html#sched)

 
 The Scheduling/Appointment resources permit the planning of encounters to occur and follow on with other clinical activities.
 

 

 | **Name** | **Aliases** | **Description** | |

 | [Schedule](schedule.html) | Availability | A container for slots of time that may be available for booking appointments. | |

 | [Slot](slot.html) | | A slot of time on a schedule that may be available for booking appointments. | |

 | [Appointment](appointment.html) | | A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s). | |

 | [AppointmentResponse](appointmentresponse.html) | | A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection. | |

 

 

 
 

 

 
 
#### 8.0.2.5 Devices and Substances [
](administration-module.html#dev-sub)

 
 Other assets are often registered in the administration system, and maintained as master files.
 

 

 | **Name** | **Aliases** | **Description** | |

 | [Device](device.html) | | A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device. | |

 | [DeviceDefinition](devicedefinition.html) | | The characteristics, operational status and capabilities of a medical-related component of a medical device. | |

 | [DeviceMetric](devicemetric.html) | | Describes a measurement, calculation or setting capability of a medical device. | |

 | [Substance](substance.html) | | A homogeneous material with a definite composition. | |

 

 
 
### 8.0.3 Security and Privacy [
](administration-module.html#secpriv)

 
 Patient privacy is handled with security labels and tags in the Resource [Meta](resource.html#Meta) property.
 This is the standard way in which that the FHIR specification provides this supporting information
 to a sub-system that implements it (which is not defined by FHIR).
 

 

 One of the more common use cases is for marking a patient as being a [celebrity](security-labels.html).
 

 

 Note that privacy considerations apply to Person, Practitioner and RelatedPerson records in addition to Patient's.
 

 

 While Organization, Location, Device and other non-person-identifying records are generally subject to less stringent
 security precautions, such data must still be protected to avoid safety issues
 (e.g. someone maliciously changing the ingredients associated with a drug to cause/fail to cause alerts)
 

 

 Devices can be linked to Patients. If this occurs, they must be protected as any other patient-linked element
 

 

 For more general considerations, see [the Security and Privacy module](secpriv-module.html).
 

 
 
### 8.0.4 Common Use Cases [
](administration-module.html#uses)

 
 Administration Resources are cornerstone resources that are used by clinical and other domains of the FHIR Standard.
 

 

 - 
 **Managing a Master Record of a Patient and a Person** (e.g. MPI)**
 A [Patient](patient.html) resource is used to describe patient demographic information and any updates to it.
 It can be used to communicate [Patient](patient.html) information to other systems
 (e.g. other registries, clinical, ancillary and financial systems).
 Some systems distinguish the Patient Registry (or Client Registry) from the Person Registry.
 A [Person](person.html) resource is a base for the Person Registry system.
 The Patient/Person Management use case includes creation, update, as well as merge/unmerge and link/unlink scenarios.
 

 - 
 Managing a Master Record of a Provider and Service Catalogue** (e.g. Provider Registry, Service Directory)**
 A [Practitioner](practitioner.html) resource is a base resource for enabling the registry of individuals, related to providing health care services.
 Other resources, such as [Organization](organization.html), [Location](location.html), [HealthcareService](healthcareservice.html), are creating a complete picture of where, how and by whom
 the care services are offered to a patient. The resources can be used for managing the master record or as a reference in
 clinical resources to inform about participants and places for various clinical resources.
 

 - 
 Managing Other Administrative Records****
 The Administration domain of the FHIR standard includes creation and update of [Device](device.html) and [Substance](substance.html) records.
 Resources can be used for managing a master record or communicating its information to other systems.
 

 - 
 Enabling Patient Profiles, Clinical Reporting and Connecting Clinical Records****
 Administration Resources are referred to by almost all clinical resources.
 Querying systems, using the references to Administration Resources enables the creation of profiles and reports of various complexities.
 

 - 
 Enabling Clinical Grouping and Financial Reporting**

 Other use cases are included in the roadmap of resources, developed by the Patient Administration group.
 The roadmap section lists plans and updates of the current work.
 

 

 
 
### 8.0.5 Developmental Roadmap [
](administration-module.html#roadmap)

 
 The Patient Administration is currently working through resources that support:
 

 

 - Encounters and Scheduling (enhance maturity of encounters and further develop in/outpatient scheduling)*

 - Service Provider Directory *(in co-ordination with the Argonaut Provider Directory group)*

 - Financial Management interactions *(account/coverage, then charge item, which links administration to billing)*

 

 

 Many of the administrative resources are part of the core resources that most systems
 use first and have formed the basis for most people's first experiences with FHIR.

 However this limited exposure has still to be proven in all contexts, such as veterinary, public health and clinical research.