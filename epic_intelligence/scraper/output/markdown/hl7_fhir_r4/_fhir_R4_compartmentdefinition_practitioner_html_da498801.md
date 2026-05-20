# Compartmentdefinition-practitioner - FHIR v4.0.1

> Source: https://hl7.org/fhir/R4/compartmentdefinition-practitioner.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/compartmentdefinition-practitioner.html) [R4B](http://hl7.org/fhir/R4B/compartmentdefinition-practitioner.html) **R4** [R3](http://hl7.org/fhir/STU3/compartmentdefinition-practitioner.html)

- 

# Compartment Practitioner

| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): N/A | [Standards Status](versions.html#std-process):[Trial Use](versions.html#std-process) | |

 | Formal URI | http://hl7.org/fhir/compartment/Practitioner | |

 | Description | The set of resources associated with a particular practitioner | |

 | Identity | There is an instance of the practitioner compartment for each Practitioner resource, and the identity of the compartment is the same as the Practitioner | |

 | Membership | The practitioner compartment includes any resources where the resource is explicitly linked to a Practitioner (usually as author, but other kinds of linkage exist) | |

 | Formal Definition | [CompartmentDefinition](compartmentdefinition.html)resource: [XML](compartmentdefinition-practitioner.xml.html) or [JSON](compartmentdefinition-practitioner.json.html) | |

Resource based membership rules:

The following resources may be in this compartment:

 | **Resource** | **Inclusion Criteria** | |

 | [Account](account.html) | subject | |

 | [AdverseEvent](adverseevent.html) | recorder | |

 | [AllergyIntolerance](allergyintolerance.html) | recorder or asserter | |

 | [Appointment](appointment.html) | actor | |

 | [AppointmentResponse](appointmentresponse.html) | actor | |

 | [AuditEvent](auditevent.html) | agent | |

 | [Basic](basic.html) | author | |

 | [CarePlan](careplan.html) | performer | |

 | [CareTeam](careteam.html) | participant | |

 | [ChargeItem](chargeitem.html) | enterer or performer-actor | |

 | [Claim](claim.html) | enterer or provider or payee or care-team | |

 | [ClaimResponse](claimresponse.html) | requestor | |

 | [ClinicalImpression](clinicalimpression.html) | assessor | |

 | [Communication](communication.html) | sender or recipient | |

 | [CommunicationRequest](communicationrequest.html) | sender or recipient or requester | |

 | [Composition](composition.html) | subject or author or attester | |

 | [Condition](condition.html) | asserter | |

 | [CoverageEligibilityRequest](coverageeligibilityrequest.html) | enterer or provider | |

 | [CoverageEligibilityResponse](coverageeligibilityresponse.html) | requestor | |

 | [DetectedIssue](detectedissue.html) | author | |

 | [DeviceRequest](devicerequest.html) | requester or performer | |

 | [DiagnosticReport](diagnosticreport.html) | performer | |

 | [DocumentManifest](documentmanifest.html) | subject or author or recipient | |

 | [DocumentReference](documentreference.html) | subject or author or authenticator | |

 | [Encounter](encounter.html) | practitioner or participant | |

 | [EpisodeOfCare](episodeofcare.html) | care-manager | |

 | [ExplanationOfBenefit](explanationofbenefit.html) | enterer or provider or payee or care-team | |

 | [Flag](flag.html) | author | |

 | [Group](group.html) | member | |

 | [Immunization](immunization.html) | performer | |

 | [Invoice](invoice.html) | participant | |

 | [Linkage](linkage.html) | author | |

 | [List](list.html) | source | |

 | [Media](media.html) | subject or operator | |

 | [MedicationAdministration](medicationadministration.html) | performer | |

 | [MedicationDispense](medicationdispense.html) | performer or receiver | |

 | [MedicationRequest](medicationrequest.html) | requester | |

 | [MedicationStatement](medicationstatement.html) | source | |

 | [MessageHeader](messageheader.html) | receiver or author or responsible or enterer | |

 | [NutritionOrder](nutritionorder.html) | provider | |

 | [Observation](observation.html) | performer | |

 | [Patient](patient.html) | general-practitioner | |

 | [PaymentNotice](paymentnotice.html) | provider | |

 | [PaymentReconciliation](paymentreconciliation.html) | requestor | |

 | [Person](person.html) | practitioner | |

 | [PractitionerRole](practitionerrole.html) | practitioner | |

 | [Procedure](procedure.html) | performer | |

 | [Provenance](provenance.html) | agent | |

 | [QuestionnaireResponse](questionnaireresponse.html) | author or source | |

 | [RequestGroup](requestgroup.html) | participant or author | |

 | [ResearchStudy](researchstudy.html) | principalinvestigator | |

 | [RiskAssessment](riskassessment.html) | performer | |

 | [Schedule](schedule.html) | actor | |

 | [ServiceRequest](servicerequest.html) | performer or requester | |

 | [Specimen](specimen.html) | collector | |

 | [SupplyDelivery](supplydelivery.html) | supplier or receiver | |

 | [SupplyRequest](supplyrequest.html) | requester | |

 | [VisionPrescription](visionprescription.html) | prescriber | |

A resource is in this compartment if the nominated search parameter (or chain) refers to the patient resource that defines the compartment.

The following resources are never in this compartment:

 - [ActivityDefinition](activitydefinition.html)

 - [Binary](binary.html)

 - [BiologicallyDerivedProduct](biologicallyderivedproduct.html)

 - [BodyStructure](bodystructure.html)

 - [Bundle](bundle.html)

 - [CapabilityStatement](capabilitystatement.html)

 - [CatalogEntry](catalogentry.html)

 - [ChargeItemDefinition](chargeitemdefinition.html)

 - [CodeSystem](codesystem.html)

 - [CompartmentDefinition](compartmentdefinition.html)

 - [ConceptMap](conceptmap.html)

 - [Consent](consent.html)

 - [Contract](contract.html)

 - [Coverage](coverage.html)

 - [Device](device.html)

 - [DeviceDefinition](devicedefinition.html)

 - [DeviceMetric](devicemetric.html)

 - [DeviceUseStatement](deviceusestatement.html)

 - [EffectEvidenceSynthesis](effectevidencesynthesis.html)

 - [Endpoint](endpoint.html)

 - [EnrollmentRequest](enrollmentrequest.html)

 - [EnrollmentResponse](enrollmentresponse.html)

 - [EventDefinition](eventdefinition.html)

 - [Evidence](evidence.html)

 - [EvidenceVariable](evidencevariable.html)

 - [ExampleScenario](examplescenario.html)

 - [FamilyMemberHistory](familymemberhistory.html)

 - [Goal](goal.html)

 - [GraphDefinition](graphdefinition.html)

 - [GuidanceResponse](guidanceresponse.html)

 - [HealthcareService](healthcareservice.html)

 - [ImagingStudy](imagingstudy.html)

 - [ImmunizationEvaluation](immunizationevaluation.html)

 - [ImmunizationRecommendation](immunizationrecommendation.html)

 - [ImplementationGuide](implementationguide.html)

 - [InsurancePlan](insuranceplan.html)

 - [Library](library.html)

 - [Location](location.html)

 - [Measure](measure.html)

 - [MeasureReport](measurereport.html)

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

 - [MolecularSequence](molecularsequence.html)

 - [NamingSystem](namingsystem.html)

 - [ObservationDefinition](observationdefinition.html)

 - [OperationDefinition](operationdefinition.html)

 - [OperationOutcome](operationoutcome.html)

 - [Organization](organization.html)

 - [OrganizationAffiliation](organizationaffiliation.html)

 - [PlanDefinition](plandefinition.html)

 - [Questionnaire](questionnaire.html)

 - [RelatedPerson](relatedperson.html)

 - [ResearchDefinition](researchdefinition.html)

 - [ResearchElementDefinition](researchelementdefinition.html)

 - [ResearchSubject](researchsubject.html)

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