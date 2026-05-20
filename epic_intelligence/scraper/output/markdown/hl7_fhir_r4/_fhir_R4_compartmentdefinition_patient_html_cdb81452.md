# Compartmentdefinition-patient - FHIR v4.0.1

> Source: https://hl7.org/fhir/R4/compartmentdefinition-patient.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/compartmentdefinition-patient.html) [R4B](http://hl7.org/fhir/R4B/compartmentdefinition-patient.html) **R4** [R3](http://hl7.org/fhir/STU3/compartmentdefinition-patient.html)

- 

# Compartment Patient

| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): N/A | [Standards Status](versions.html#std-process):[Trial Use](versions.html#std-process) | |

 | Formal URI | http://hl7.org/fhir/compartment/Patient | |

 | Description | The set of resources associated with a particular patient | |

 | Identity | There is an instance of the patient compartment for each patient resource, and the identity of the compartment is the same as the patient. When a patient is linked to another patient, all the records associated with the linked patient are in the compartment associated with the target of the link. | |

 | Membership | The patient compartment includes any resources where the subject of the resource is the patient, and some other resources that are directly linked to resources in the patient compartment | |

 | Formal Definition | [CompartmentDefinition](compartmentdefinition.html)resource: [XML](compartmentdefinition-patient.xml.html) or [JSON](compartmentdefinition-patient.json.html) | |

Resource based membership rules:

The following resources may be in this compartment:

 | **Resource** | **Inclusion Criteria** | |

 | [Account](account.html) | subject | |

 | [AdverseEvent](adverseevent.html) | subject | |

 | [AllergyIntolerance](allergyintolerance.html) | patient or recorder or asserter | |

 | [Appointment](appointment.html) | actor | |

 | [AppointmentResponse](appointmentresponse.html) | actor | |

 | [AuditEvent](auditevent.html) | patient | |

 | [Basic](basic.html) | patient or author | |

 | [BodyStructure](bodystructure.html) | patient | |

 | [CarePlan](careplan.html) | patient or performer | |

 | [CareTeam](careteam.html) | patient or participant | |

 | [ChargeItem](chargeitem.html) | subject | |

 | [Claim](claim.html) | patient or payee | |

 | [ClaimResponse](claimresponse.html) | patient | |

 | [ClinicalImpression](clinicalimpression.html) | subject | |

 | [Communication](communication.html) | subject or sender or recipient | |

 | [CommunicationRequest](communicationrequest.html) | subject or sender or recipient or requester | |

 | [Composition](composition.html) | subject or author or attester | |

 | [Condition](condition.html) | patient or asserter | |

 | [Consent](consent.html) | patient | |

 | [Coverage](coverage.html) | policy-holder or subscriber or beneficiary orpayor | |

 | [CoverageEligibilityRequest](coverageeligibilityrequest.html) | patient | |

 | [CoverageEligibilityResponse](coverageeligibilityresponse.html) | patient | |

 | [DetectedIssue](detectedissue.html) | patient | |

 | [DeviceRequest](devicerequest.html) | subject or performer | |

 | [DeviceUseStatement](deviceusestatement.html) | subject | |

 | [DiagnosticReport](diagnosticreport.html) | subject | |

 | [DocumentManifest](documentmanifest.html) | subject or author or recipient | |

 | [DocumentReference](documentreference.html) | subject or author | |

 | [Encounter](encounter.html) | patient | |

 | [EnrollmentRequest](enrollmentrequest.html) | subject | |

 | [EpisodeOfCare](episodeofcare.html) | patient | |

 | [ExplanationOfBenefit](explanationofbenefit.html) | patient or payee | |

 | [FamilyMemberHistory](familymemberhistory.html) | patient | |

 | [Flag](flag.html) | patient | |

 | [Goal](goal.html) | patient | |

 | [Group](group.html) | member | |

 | [ImagingStudy](imagingstudy.html) | patient | |

 | [Immunization](immunization.html) | patient | |

 | [ImmunizationEvaluation](immunizationevaluation.html) | patient | |

 | [ImmunizationRecommendation](immunizationrecommendation.html) | patient | |

 | [Invoice](invoice.html) | subject or patient or recipient | |

 | [List](list.html) | subject or source | |

 | [MeasureReport](measurereport.html) | patient | |

 | [Media](media.html) | subject | |

 | [MedicationAdministration](medicationadministration.html) | patient or performer or subject | |

 | [MedicationDispense](medicationdispense.html) | subject or patient or receiver | |

 | [MedicationRequest](medicationrequest.html) | subject | |

 | [MedicationStatement](medicationstatement.html) | subject | |

 | [MolecularSequence](molecularsequence.html) | patient | |

 | [NutritionOrder](nutritionorder.html) | patient | |

 | [Observation](observation.html) | subject or performer | |

 | [Patient](patient.html) | link | |

 | [Person](person.html) | patient | |

 | [Procedure](procedure.html) | patient or performer | |

 | [Provenance](provenance.html) | patient | |

 | [QuestionnaireResponse](questionnaireresponse.html) | subject or author | |

 | [RelatedPerson](relatedperson.html) | patient | |

 | [RequestGroup](requestgroup.html) | subject or participant | |

 | [ResearchSubject](researchsubject.html) | individual | |

 | [RiskAssessment](riskassessment.html) | subject | |

 | [Schedule](schedule.html) | actor | |

 | [ServiceRequest](servicerequest.html) | subject or performer | |

 | [Specimen](specimen.html) | subject | |

 | [SupplyDelivery](supplydelivery.html) | patient | |

 | [SupplyRequest](supplyrequest.html) | subject | |

 | [VisionPrescription](visionprescription.html) | patient | |

A resource is in this compartment if the nominated search parameter (or chain) refers to the patient resource that defines the compartment.

The following resources are never in this compartment:

 - [ActivityDefinition](activitydefinition.html)

 - [Binary](binary.html)

 - [BiologicallyDerivedProduct](biologicallyderivedproduct.html)

 - [Bundle](bundle.html)

 - [CapabilityStatement](capabilitystatement.html)

 - [CatalogEntry](catalogentry.html)

 - [ChargeItemDefinition](chargeitemdefinition.html)

 - [CodeSystem](codesystem.html)

 - [CompartmentDefinition](compartmentdefinition.html)

 - [ConceptMap](conceptmap.html)

 - [Contract](contract.html)

 - [Device](device.html)

 - [DeviceDefinition](devicedefinition.html)

 - [DeviceMetric](devicemetric.html)

 - [EffectEvidenceSynthesis](effectevidencesynthesis.html)

 - [Endpoint](endpoint.html)

 - [EnrollmentResponse](enrollmentresponse.html)

 - [EventDefinition](eventdefinition.html)

 - [Evidence](evidence.html)

 - [EvidenceVariable](evidencevariable.html)

 - [ExampleScenario](examplescenario.html)

 - [GraphDefinition](graphdefinition.html)

 - [GuidanceResponse](guidanceresponse.html)

 - [HealthcareService](healthcareservice.html)

 - [ImplementationGuide](implementationguide.html)

 - [InsurancePlan](insuranceplan.html)

 - [Library](library.html)

 - [Linkage](linkage.html)

 - [Location](location.html)

 - [Measure](measure.html)

 - [Medication](medication.html)

 - [MedicationKnowledge](medicationknowledge.html)

 - [MedicinalProduct](medicinalproduct.html)

 - [MedicinalProductAuthorization](medicinalproductauthorization.html)

 - [MedicinalProductContraindication](medicinalproductcontraindication.html)

 - [MedicinalProductIndication](medicinalproductindication.html)

 - [MedicinalProductIngredient](medicinalproductingredient.html)

 - [MedicinalProductInteraction](medicinalproductinteraction.html)

 - [MedicinalProductManufactured](medicinalproductmanufactured.html)

 - [MedicinalProductPackaged](medicinalproductpackaged.html)

 - [MedicinalProductPharmaceutical](medicinalproductpharmaceutical.html)

 - [MedicinalProductUndesirableEffect](medicinalproductundesirableeffect.html)

 - [MessageDefinition](messagedefinition.html)

 - [MessageHeader](messageheader.html)

 - [NamingSystem](namingsystem.html)

 - [ObservationDefinition](observationdefinition.html)

 - [OperationDefinition](operationdefinition.html)

 - [OperationOutcome](operationoutcome.html)

 - [Organization](organization.html)

 - [OrganizationAffiliation](organizationaffiliation.html)

 - [PaymentNotice](paymentnotice.html)

 - [PaymentReconciliation](paymentreconciliation.html)

 - [PlanDefinition](plandefinition.html)

 - [Practitioner](practitioner.html)

 - [PractitionerRole](practitionerrole.html)

 - [Questionnaire](questionnaire.html)

 - [ResearchDefinition](researchdefinition.html)

 - [ResearchElementDefinition](researchelementdefinition.html)

 - [ResearchStudy](researchstudy.html)

 - [RiskEvidenceSynthesis](riskevidencesynthesis.html)

 - [SearchParameter](searchparameter.html)

 - [Slot](slot.html)

 - [SpecimenDefinition](specimendefinition.html)

 - [StructureDefinition](structuredefinition.html)

 - [StructureMap](structuremap.html)

 - [Subscription](subscription.html)

 - [Substance](substance.html)

 - [SubstanceNucleicAcid](substancenucleicacid.html)

 - [SubstancePolymer](substancepolymer.html)

 - [SubstanceProtein](substanceprotein.html)

 - [SubstanceReferenceInformation](substancereferenceinformation.html)

 - [SubstanceSourceMaterial](substancesourcematerial.html)

 - [SubstanceSpecification](substancespecification.html)

 - [Task](task.html)

 - [TerminologyCapabilities](terminologycapabilities.html)

 - [TestReport](testreport.html)

 - [TestScript](testscript.html)

 - [ValueSet](valueset.html)

 - [VerificationResult](verificationresult.html)

See [ information about compartments](compartmentdefinition.html).