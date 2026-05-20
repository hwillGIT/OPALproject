# Compartmentdefinition-relatedperson - FHIR v4.0.1

> Source: https://hl7.org/fhir/R4/compartmentdefinition-relatedperson.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/compartmentdefinition-relatedperson.html) [R4B](http://hl7.org/fhir/R4B/compartmentdefinition-relatedperson.html) **R4** [R3](http://hl7.org/fhir/STU3/compartmentdefinition-relatedperson.html)

- 

# Compartment RelatedPerson

| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): N/A | [Standards Status](versions.html#std-process):[Trial Use](versions.html#std-process) | |

 | Formal URI | http://hl7.org/fhir/compartment/RelatedPerson | |

 | Description | The set of resources associated with a particular 'related person' | |

 | Identity | There is an instance of the relatedPerson compartment for each relatedPerson resource, and the identity of the compartment is the same as the relatedPerson | |

 | Membership | The relatedPerson compartment includes any resources where the resource is explicitly linked to relatedPerson (usually as author) | |

 | Formal Definition | [CompartmentDefinition](compartmentdefinition.html)resource: [XML](compartmentdefinition-relatedperson.xml.html) or [JSON](compartmentdefinition-relatedperson.json.html) | |

Resource based membership rules:

The following resources may be in this compartment:

 | **Resource** | **Inclusion Criteria** | |

 | [AdverseEvent](adverseevent.html) | recorder | |

 | [AllergyIntolerance](allergyintolerance.html) | asserter | |

 | [Appointment](appointment.html) | actor | |

 | [AppointmentResponse](appointmentresponse.html) | actor | |

 | [Basic](basic.html) | author | |

 | [CarePlan](careplan.html) | performer | |

 | [CareTeam](careteam.html) | participant | |

 | [ChargeItem](chargeitem.html) | enterer or performer-actor | |

 | [Claim](claim.html) | payee | |

 | [Communication](communication.html) | sender or recipient | |

 | [CommunicationRequest](communicationrequest.html) | sender or recipient or requester | |

 | [Composition](composition.html) | author | |

 | [Condition](condition.html) | asserter | |

 | [Coverage](coverage.html) | policy-holder or subscriber orpayor | |

 | [DocumentManifest](documentmanifest.html) | author or recipient | |

 | [DocumentReference](documentreference.html) | author | |

 | [Encounter](encounter.html) | participant | |

 | [ExplanationOfBenefit](explanationofbenefit.html) | payee | |

 | [Invoice](invoice.html) | recipient | |

 | [MedicationAdministration](medicationadministration.html) | performer | |

 | [MedicationStatement](medicationstatement.html) | source | |

 | [Observation](observation.html) | performer | |

 | [Patient](patient.html) | link | |

 | [Person](person.html) | link | |

 | [Procedure](procedure.html) | performer | |

 | [Provenance](provenance.html) | agent | |

 | [QuestionnaireResponse](questionnaireresponse.html) | author or source | |

 | [RequestGroup](requestgroup.html) | participant | |

 | [Schedule](schedule.html) | actor | |

 | [ServiceRequest](servicerequest.html) | performer | |

 | [SupplyRequest](supplyrequest.html) | requester | |

A resource is in this compartment if the nominated search parameter (or chain) refers to the patient resource that defines the compartment.

The following resources are never in this compartment:

 - [Account](account.html)

 - [ActivityDefinition](activitydefinition.html)

 - [AuditEvent](auditevent.html)

 - [Binary](binary.html)

 - [BiologicallyDerivedProduct](biologicallyderivedproduct.html)

 - [BodyStructure](bodystructure.html)

 - [Bundle](bundle.html)

 - [CapabilityStatement](capabilitystatement.html)

 - [CatalogEntry](catalogentry.html)

 - [ChargeItemDefinition](chargeitemdefinition.html)

 - [ClaimResponse](claimresponse.html)

 - [ClinicalImpression](clinicalimpression.html)

 - [CodeSystem](codesystem.html)

 - [CompartmentDefinition](compartmentdefinition.html)

 - [ConceptMap](conceptmap.html)

 - [Consent](consent.html)

 - [Contract](contract.html)

 - [CoverageEligibilityRequest](coverageeligibilityrequest.html)

 - [CoverageEligibilityResponse](coverageeligibilityresponse.html)

 - [DetectedIssue](detectedissue.html)

 - [Device](device.html)

 - [DeviceDefinition](devicedefinition.html)

 - [DeviceMetric](devicemetric.html)

 - [DeviceRequest](devicerequest.html)

 - [DeviceUseStatement](deviceusestatement.html)

 - [DiagnosticReport](diagnosticreport.html)

 - [EffectEvidenceSynthesis](effectevidencesynthesis.html)

 - [Endpoint](endpoint.html)

 - [EnrollmentRequest](enrollmentrequest.html)

 - [EnrollmentResponse](enrollmentresponse.html)

 - [EpisodeOfCare](episodeofcare.html)

 - [EventDefinition](eventdefinition.html)

 - [Evidence](evidence.html)

 - [EvidenceVariable](evidencevariable.html)

 - [ExampleScenario](examplescenario.html)

 - [FamilyMemberHistory](familymemberhistory.html)

 - [Flag](flag.html)

 - [Goal](goal.html)

 - [GraphDefinition](graphdefinition.html)

 - [Group](group.html)

 - [GuidanceResponse](guidanceresponse.html)

 - [HealthcareService](healthcareservice.html)

 - [ImagingStudy](imagingstudy.html)

 - [Immunization](immunization.html)

 - [ImmunizationEvaluation](immunizationevaluation.html)

 - [ImmunizationRecommendation](immunizationrecommendation.html)

 - [ImplementationGuide](implementationguide.html)

 - [InsurancePlan](insuranceplan.html)

 - [Library](library.html)

 - [Linkage](linkage.html)

 - [List](list.html)

 - [Location](location.html)

 - [Measure](measure.html)

 - [MeasureReport](measurereport.html)

 - [Media](media.html)

 - [Medication](medication.html)

 - [MedicationDispense](medicationdispense.html)

 - [MedicationKnowledge](medicationknowledge.html)

 - [MedicationRequest](medicationrequest.html)

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

 - [MolecularSequence](molecularsequence.html)

 - [NamingSystem](namingsystem.html)

 - [NutritionOrder](nutritionorder.html)

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

 - [ResearchSubject](researchsubject.html)

 - [RiskAssessment](riskassessment.html)

 - [RiskEvidenceSynthesis](riskevidencesynthesis.html)

 - [SearchParameter](searchparameter.html)

 - [Slot](slot.html)

 - [Specimen](specimen.html)

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

 - [SupplyDelivery](supplydelivery.html)

 - [Task](task.html)

 - [TerminologyCapabilities](terminologycapabilities.html)

 - [TestReport](testreport.html)

 - [TestScript](testscript.html)

 - [ValueSet](valueset.html)

 - [VerificationResult](verificationresult.html)

 - [VisionPrescription](visionprescription.html)

See [ information about compartments](compartmentdefinition.html).