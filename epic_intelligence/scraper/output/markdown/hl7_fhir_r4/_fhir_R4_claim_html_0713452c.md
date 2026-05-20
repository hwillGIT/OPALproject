# Claim - FHIR v4.0.1A unique identifier assigned to this claimThe status of the resource instance (this element modifies the meaning of other elements)A code specifying the state of the resource instance. (Strength=Required)The category of claim, e.g. oral, pharmacy, vision, institutional, professionalThe type or discipline-style of the claim. (Strength=Extensible)A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty serviceA more granular claim typecode. (Strength=Example)A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the futureThe purpose of the Claim: predetermination, preauthorization, claim. (Strength=Required)The party to whom the professional services and/or products have been supplied or are being considered and for whom actual or forecast reimbursement is soughtThe period for which charges are being submittedThe date this resource was createdIndividual who created the claim, predetermination or preauthorizationThe Insurer who is target of the requestThe provider which is responsible for the claim, predetermination or preauthorizationThe provider-required urgency of processing the request. Typical values include: stat, routine deferredThe timeliness with which processing is required: stat, normal, deferred. (Strength=Example)A code to indicate whether and for whom funds are to be reserved for future claimsFor whom funds are to be reserved: (Patient, Provider, None). (Strength=Example)Prescription to support the dispensing of pharmacy, device or vision productsOriginal prescription which has been superseded by this prescription to support the dispensing of pharmacy services, medications or productsA reference to a referral resourceFacility where the services were providedThe total value of the all the items in the claimReference to a related claimA code to convey how the claims are relatedRelationship of this claim to a related Claim. (Strength=Example)An alternate organizational reference to the case or file to which this particular claim pertainsType of Party to be reimbursed: subscriber, provider, otherA code for the party to be reimbursed. (Strength=Example)Reference to the individual or organization to whom any payment will be madeA number to uniquely identify care team entriesMember of the team who provided the product or serviceThe party who is billing and/or responsible for the claimed products or servicesThe lead, assisting or supervising practitioner and their discipline if a multidisciplinary teamThe role codes for the care team members. (Strength=Example)The qualification of the practitioner which is applicable for this serviceProvider professional qualifications. (Strength=Example)A number to uniquely identify supporting information entriesThe general class of the information supplied: information; exception; accident, employment; onset, etcThe valuset used for additional information category codes. (Strength=Example)System and code pertaining to the specific information regarding special conditions relating to the setting, treatment or patient  for which care is soughtThe valuset used for additional information codes. (Strength=Example)The date when or period to which this information refersAdditional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the dataProvides the reason in the situation where a reason code is required in addition to the contentReason codes for the missing teeth. (Strength=Example)A number to uniquely identify diagnosis entriesThe nature of illness or problem in a coded form or as a reference to an external defined ConditionExample ICD10 Diagnostic codes. (Strength=Example)When the condition was observed or the relative rankingThe type of the diagnosis: admitting, principal, discharge. (Strength=Example)Indication of whether the diagnosis was present on admission to a facilityPresent on admission. (Strength=Example)A package billing code or bundle code used to group products and services to a particular health condition (such as heart attack) which is based on a predetermined grouping code systemThe DRG codes associated with the diagnosis. (Strength=Example)A number to uniquely identify procedure entriesWhen the condition was observed or the relative rankingExample procedure type codes. (Strength=Example)Date and optionally time the procedure was performedThe code or reference to a Procedure resource which identifies the clinical intervention performedExample ICD10 Procedure codes. (Strength=Example)Unique Device Identifiers associated with this line itemA number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit orderA flag to indicate that this Coverage is to be used for adjudication of this claim when set to trueThe business identifier to be used when the claim is sent for adjudication against this insurance policyReference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information systemA business agreement number established between the provider and the insurer for special business processing purposesReference numbers previously provided by the insurer to the provider to be quoted on subsequent claims containing services or products related to the prior authorizationThe result of the adjudication of the line items for the Coverage specified in this insuranceDate of an accident event  related to the products and services contained in the claimThe type or context of the accident event for the purposes of selection of potential insurance coverages and determination of coordination between insurersType of accident: work place, auto, etc. (Strength=Extensible)The physical location of the accident eventA number to uniquely identify item entriesCareTeam members related to this service or productDiagnosis applicable for this service or productProcedures applicable for this service or productExceptions, special conditions and supporting information applicable for this service or productThe type of revenue or cost center providing the product and/or serviceCodes for the revenue or cost centers supplying the service and/or products. (Strength=Example)Code to identify the general type of benefits under which products and services are providedBenefit categories such as: oral-basic, major, glasses. (Strength=Example)When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The date or dates when the service or product was supplied, performed or completedWhere the product or service was providedPlace of service: pharmacy, school, prison, etc. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeUnique Device Identifiers associated with this line itemPhysical service site on the patient (limb, tooth, etc.)The code for the teeth, quadrant, sextant and arch. (Strength=Example)A region or surface of the bodySite, e.g. limb region or tooth surface(s)The code for the tooth surface and surface combinations. (Strength=Example)The Encounters during which this Claim was created or to which the creation of this record is tightly associatedA number to uniquely identify item entriesThe type of revenue or cost center providing the product and/or serviceCodes for the revenue or cost centers supplying the service and/or products. (Strength=Example)Code to identify the general type of benefits under which products and services are providedBenefit categories such as: oral-basic, major, glasses. (Strength=Example)When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeUnique Device Identifiers associated with this line itemA number to uniquely identify item entriesThe type of revenue or cost center providing the product and/or serviceCodes for the revenue or cost centers supplying the service and/or products. (Strength=Example)Code to identify the general type of benefits under which products and services are providedBenefit categories such as: oral-basic, major, glasses. (Strength=Example)When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeUnique Device Identifiers associated with this line itemOther claims which are related to this claim such as prior submissions or claims for related services or for the same eventThe party to be reimbursed for cost of the products and services according to the terms of the policyThe members of the team who provided the products and servicesAdditional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issuesInformation about diagnoses relevant to the claim itemsProcedures performed on the patient relevant to the billing items with the claimFinancial instruments for reimbursement for the health care products and services specified on the claimDetails of an accident which resulted in injuries which required the products and services listed in the claimA claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsA claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsA claim line. Either a simple  product or service or a 'group' of details which can each be a simple items or groups of sub-detailsA unique identifier assigned to this claimThe status of the resource instance (this element modifies the meaning of other elements)A code specifying the state of the resource instance. (Strength=Required)The category of claim, e.g. oral, pharmacy, vision, institutional, professionalThe type or discipline-style of the claim. (Strength=Extensible)A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty serviceA more granular claim typecode. (Strength=Example)A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the futureThe purpose of the Claim: predetermination, preauthorization, claim. (Strength=Required)The party to whom the professional services and/or products have been supplied or are being considered and for whom actual or forecast reimbursement is soughtThe period for which charges are being submittedThe date this resource was createdIndividual who created the claim, predetermination or preauthorizationThe Insurer who is target of the requestThe provider which is responsible for the claim, predetermination or preauthorizationThe provider-required urgency of processing the request. Typical values include: stat, routine deferredThe timeliness with which processing is required: stat, normal, deferred. (Strength=Example)A code to indicate whether and for whom funds are to be reserved for future claimsFor whom funds are to be reserved: (Patient, Provider, None). (Strength=Example)Prescription to support the dispensing of pharmacy, device or vision productsOriginal prescription which has been superseded by this prescription to support the dispensing of pharmacy services, medications or productsA reference to a referral resourceFacility where the services were providedThe total value of the all the items in the claimReference to a related claimA code to convey how the claims are relatedRelationship of this claim to a related Claim. (Strength=Example)An alternate organizational reference to the case or file to which this particular claim pertainsType of Party to be reimbursed: subscriber, provider, otherA code for the party to be reimbursed. (Strength=Example)Reference to the individual or organization to whom any payment will be madeA number to uniquely identify care team entriesMember of the team who provided the product or serviceThe party who is billing and/or responsible for the claimed products or servicesThe lead, assisting or supervising practitioner and their discipline if a multidisciplinary teamThe role codes for the care team members. (Strength=Example)The qualification of the practitioner which is applicable for this serviceProvider professional qualifications. (Strength=Example)A number to uniquely identify supporting information entriesThe general class of the information supplied: information; exception; accident, employment; onset, etcThe valuset used for additional information category codes. (Strength=Example)System and code pertaining to the specific information regarding special conditions relating to the setting, treatment or patient  for which care is soughtThe valuset used for additional information codes. (Strength=Example)The date when or period to which this information refersAdditional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the dataProvides the reason in the situation where a reason code is required in addition to the contentReason codes for the missing teeth. (Strength=Example)A number to uniquely identify diagnosis entriesThe nature of illness or problem in a coded form or as a reference to an external defined ConditionExample ICD10 Diagnostic codes. (Strength=Example)When the condition was observed or the relative rankingThe type of the diagnosis: admitting, principal, discharge. (Strength=Example)Indication of whether the diagnosis was present on admission to a facilityPresent on admission. (Strength=Example)A package billing code or bundle code used to group products and services to a particular health condition (such as heart attack) which is based on a predetermined grouping code systemThe DRG codes associated with the diagnosis. (Strength=Example)A number to uniquely identify procedure entriesWhen the condition was observed or the relative rankingExample procedure type codes. (Strength=Example)Date and optionally time the procedure was performedThe code or reference to a Procedure resource which identifies the clinical intervention performedExample ICD10 Procedure codes. (Strength=Example)Unique Device Identifiers associated with this line itemA number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit orderA flag to indicate that this Coverage is to be used for adjudication of this claim when set to trueThe business identifier to be used when the claim is sent for adjudication against this insurance policyReference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information systemA business agreement number established between the provider and the insurer for special business processing purposesReference numbers previously provided by the insurer to the provider to be quoted on subsequent claims containing services or products related to the prior authorizationThe result of the adjudication of the line items for the Coverage specified in this insuranceDate of an accident event  related to the products and services contained in the claimThe type or context of the accident event for the purposes of selection of potential insurance coverages and determination of coordination between insurersType of accident: work place, auto, etc. (Strength=Extensible)The physical location of the accident eventA number to uniquely identify item entriesCareTeam members related to this service or productDiagnosis applicable for this service or productProcedures applicable for this service or productExceptions, special conditions and supporting information applicable for this service or productThe type of revenue or cost center providing the product and/or serviceCodes for the revenue or cost centers supplying the service and/or products. (Strength=Example)Code to identify the general type of benefits under which products and services are providedBenefit categories such as: oral-basic, major, glasses. (Strength=Example)When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The date or dates when the service or product was supplied, performed or completedWhere the product or service was providedPlace of service: pharmacy, school, prison, etc. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeUnique Device Identifiers associated with this line itemPhysical service site on the patient (limb, tooth, etc.)The code for the teeth, quadrant, sextant and arch. (Strength=Example)A region or surface of the bodySite, e.g. limb region or tooth surface(s)The code for the tooth surface and surface combinations. (Strength=Example)The Encounters during which this Claim was created or to which the creation of this record is tightly associatedA number to uniquely identify item entriesThe type of revenue or cost center providing the product and/or serviceCodes for the revenue or cost centers supplying the service and/or products. (Strength=Example)Code to identify the general type of benefits under which products and services are providedBenefit categories such as: oral-basic, major, glasses. (Strength=Example)When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeUnique Device Identifiers associated with this line itemA number to uniquely identify item entriesThe type of revenue or cost center providing the product and/or serviceCodes for the revenue or cost centers supplying the service and/or products. (Strength=Example)Code to identify the general type of benefits under which products and services are providedBenefit categories such as: oral-basic, major, glasses. (Strength=Example)When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeUnique Device Identifiers associated with this line itemOther claims which are related to this claim such as prior submissions or claims for related services or for the same eventThe party to be reimbursed for cost of the products and services according to the terms of the policyThe members of the team who provided the products and servicesAdditional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issuesInformation about diagnoses relevant to the claim itemsProcedures performed on the patient relevant to the billing items with the claimFinancial instruments for reimbursement for the health care products and services specified on the claimDetails of an accident which resulted in injuries which required the products and services listed in the claimA claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsA claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsA claim line. Either a simple  product or service or a 'group' of details which can each be a simple items or groups of sub-details

> Source: https://hl7.org/fhir/R4/claim.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/claim.html) [R4B](http://hl7.org/fhir/R4B/claim.html) **R4** [R3](http://hl7.org/fhir/STU3/claim.html) [R2](http://hl7.org/fhir/DSTU2/claim.html)
 

# 13.6 Resource Claim - Content [
](claim.html#13.6)

| [Financial Management ](http://www.hl7.org/Special/committees/fm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Encounter](compartmentdefinition-encounter.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) | |

A provider issued list of professional services and products which have been provided, or are to be provided, to a patient which is sent to an insurer for reimbursement.

 
 
## 13.6.1 Scope and Usage [
](claim.html#scope)

 
The Claim is used by providers and payors, insurers, to exchange the financial information, and supporting clinical information, regarding the provision
 of health care services with payors and for reporting to regulatory bodies and firms which provide data analytics. The primary uses of this resource is to support eClaims, 
the exchange of information relating to the proposed or actual provision of healthcare-related goods and services for patients to their benefit payors, insurers and national health programs, for treatment payment planning and reimbursement.
 

 
The Claim resource is a "request" resource from a FHIR workflow perspective - see [Workflow Request.](workflow.html#request)

 

The Claim resource may be interpreted differently depending on its intended use (and the Claim.use element contains the code to indicate):
 

 - claim - where the provision of goods and services is **complete** and adjudication under a plan and payment is sought.

 - preauthorization - where the provision of goods and services is **proposed** and authorization and/or the reservation of funds is desired.

 - predetermination - where the provision of goods and services is **explored** to determine what services may be covered and to what amount. Essentially a 'what if' claim.

 
 
 

 

The Claim also supports:
 

 - Up to a 3-tier hierarchy of Goods, products, and Services, to support simple to complex billing.

 - Multiple insurance programs arranged in a Coordination of Benefit sequence to enable exchange with primary, secondary, tertiary etc. insurance coverages.

 - Assignment of benefit - the benefit may be requested to be directed to the subscriber, the provider or another party.

 

 

 

 **Mapping to other Claim specifications:** Mappings are currently maintained by the Financial Management Work Group to UB04 and CMS1500 and are available 
at [https://confluence.hl7.org/display/FM/FHIR+Resource+Development ](https://confluence.hl7.org/display/FM/FHIR+Resource+Development).
Mappings to other specifications may be made available where IP restrictions permit. 
 

### 13.6.1.1 Additional Information [
](claim.html#13.6.1.1)

Additional information regarding electronic claims content and usage may be found at:

 

- [Financial Resource Status Lifecycle](financial-module.html#resource-status): how .status is used in the financial resources.

- [Secondary Use of Resources](financial-module.html#secondary-use): how resources such as Claim and ExplanationOfBenefit may used for 
 reporting and data exchange for analytics, not just for eClaims exchange between providers and payors.

- [Subrogation](financial-module.html#subrogation): how eClaims may handle patient insurance coverages when another insurer rather than 
the provider will settle the claim and potentially recover costs against specified coverages.

- [Coordination of Benefit](financial-module.html#cob): how eClaims may handle multiple patient insurance coverages.

- [Batches](financial-module.html#batch): how eClaims may handle batches of eligibility, claims and responses.

- [Attachments and Supporting Information](financial-module.html#attachments): how eClaims may handle the provision of supporting
 information, whether provided by content or reference, within the eClaim resource when submitted to the payor or later in a resource which refers
 to the subject eClaim resource. This also includes how payors may request additional supporting information from providers.

 

 

 
 
## 13.6.2 Boundaries and Relationships [
](claim.html#bnr)

 The Claim resource is used to request the adjudication and/or authorization of a set of healthcare-related goods and services for a patient against the patient's insurance coverages, or
 to request what the adjudication would be for a supplied set of goods or services should they be actually supplied to the patient.

 
When requesting whether the patient's coverage is inforce, whether it is valid at this or a specified date, or requesting the benefit details or preauthorization requirements 
 associated with a coverage, then [CoverageEligibilityRequest](coverageeligibilityrequest.html) should be used instead.

 
When using the resources for reporting and transferring claims data, which may have originated in some standard other than FHIR, the Claim resource is useful if only the
 request side of the information exchange is of interest. If, however, both the request and the adjudication information is to be reported then the 
 [ExplanationOfBenefit](explanationofbenefit.html) should be used instead.

 
For reporting out to patients or transferring data to patient centered applications, such as patient health Record (PHR) application, the [ExplanationOfBenefit](explanationofbenefit.html) 
 should be used instead of the Claim and ClaimResponse resources as those resources may contain provider and payer specific information which is not appropriate for sharing with 
 the patient.

 

 **The eClaim domain includes a number of related resources**
 

 

 | 
 Claim | 
 A suite of goods and services and insurances coverages under which adjudication or authorization is requested. | 
 |

 | 
 [CoverageEligibilityRequest](coverageeligibilityrequest.html) | 
 A request to a payor to: ascertain whether a coverage is in-force at the current or at a specified time; list the table of benefits;
 determine whether coverage is provided for specified categories or specific services; and whether preauthorization is required, and if so
 what supporting information would be required. | 
 |

 | 
 [ClaimResponse](claimresponse.html) | 
 A payor's adjudication and/or authorization response to the suite of services provided in a Claim. Typically the ClaimResponse references the Claim but does not duplicate
 the clinical or financial information provided in the claim. | 
 |

 | 
 [ExplanationOfBenefit](explanationofbenefit.html) | 
 This resource combines the information from the Claim and the ClaimResponse, stripping out any provider or payor proprietary information, into a unified information model 
 suitable for use for: patient reporting; transferring information to a Patient Health Record system; and, supporting complete claim and adjudication information exchange
 with regulatory and analytics organizations and other parts of the provider's organization.
 | 
 |

 

 

This resource is referenced by itself, [ClaimResponse](claimresponse.html#ClaimResponse), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement) and [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit)

## 13.6.3 
Resource Content
 [
](claim.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Claim](claim-definitions.html#Claim) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Claim, Pre-determination or Pre-authorization**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](claim-definitions.html#Claim.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for claim
 | |

| [status](claim-definitions.html#Claim.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | cancelled | draft | entered-in-error
[Financial Resource Status Codes](valueset-fm-status.html) ([Required](terminologies.html#required)) | |

| [type](claim-definitions.html#Claim.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category or discipline
[Claim Type Codes](valueset-claim-type.html) ([Extensible](terminologies.html#extensible)) | |

| [subType](claim-definitions.html#Claim.subType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | More granular claim type
[Example Claim SubType Codes](valueset-claim-subtype.html) ([Example](terminologies.html#example)) | |

| [use](claim-definitions.html#Claim.use) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | claim | preauthorization | predetermination
[Use](valueset-claim-use.html) ([Required](terminologies.html#required)) | |

| [patient](claim-definitions.html#Claim.patient) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | The recipient of the products and services | |

| [billablePeriod](claim-definitions.html#Claim.billablePeriod) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Relevant time frame for the claim | |

| [created](claim-definitions.html#Claim.created) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [dateTime](datatypes.html#dateTime) | Resource creation date | |

| [enterer](claim-definitions.html#Claim.enterer) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Author of the claim | |

| [insurer](claim-definitions.html#Claim.insurer) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Target | |

| [provider](claim-definitions.html#Claim.provider) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Party responsible for the claim | |

| [priority](claim-definitions.html#Claim.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Desired processing ugency
[Process Priority Codes](valueset-process-priority.html) ([Example](terminologies.html#example)) | |

| [fundsReserve](claim-definitions.html#Claim.fundsReserve) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | For whom to reserve funds
[FundsReserve](valueset-fundsreserve.html) ([Example](terminologies.html#example)) | |

| [related](claim-definitions.html#Claim.related) | | 0..* | [BackboneElement](backboneelement.html) | Prior or corollary claims
 | |

| [claim](claim-definitions.html#Claim.related.claim) | | 0..1 | [Reference](references.html#Reference)([Claim](claim.html)) | Reference to the related claim | |

| [relationship](claim-definitions.html#Claim.related.relationship) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How the reference claim is related
[Example Related Claim Relationship Codes](valueset-related-claim-relationship.html) ([Example](terminologies.html#example)) | |

| [reference](claim-definitions.html#Claim.related.reference) | | 0..1 | [Identifier](datatypes.html#Identifier) | File or case reference | |

| [prescription](claim-definitions.html#Claim.prescription) | | 0..1 | [Reference](references.html#Reference)([DeviceRequest](devicerequest.html) | [MedicationRequest](medicationrequest.html) | [VisionPrescription](visionprescription.html)) | Prescription authorizing services and products | |

| [originalPrescription](claim-definitions.html#Claim.originalPrescription) | | 0..1 | [Reference](references.html#Reference)([DeviceRequest](devicerequest.html) | [MedicationRequest](medicationrequest.html) | [VisionPrescription](visionprescription.html)) | Original prescription if superseded by fulfiller | |

| [payee](claim-definitions.html#Claim.payee) | | 0..1 | [BackboneElement](backboneelement.html) | Recipient of benefits payable | |

| [type](claim-definitions.html#Claim.payee.type) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category of recipient
[PayeeType](valueset-payeetype.html) ([Example](terminologies.html#example)) | |

| [party](claim-definitions.html#Claim.payee.party) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Recipient reference | |

| [referral](claim-definitions.html#Claim.referral) | | 0..1 | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | Treatment referral | |

| [facility](claim-definitions.html#Claim.facility) | | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Servicing facility | |

| [careTeam](claim-definitions.html#Claim.careTeam) | | 0..* | [BackboneElement](backboneelement.html) | Members of the care team
 | |

| [sequence](claim-definitions.html#Claim.careTeam.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Order of care team | |

| [provider](claim-definitions.html#Claim.careTeam.provider) | | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Practitioner or organization | |

| [responsible](claim-definitions.html#Claim.careTeam.responsible) | | 0..1 | [boolean](datatypes.html#boolean) | Indicator of the lead practitioner | |

| [role](claim-definitions.html#Claim.careTeam.role) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Function within the team
[Claim Care Team Role Codes](valueset-claim-careteamrole.html) ([Example](terminologies.html#example)) | |

| [qualification](claim-definitions.html#Claim.careTeam.qualification) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Practitioner credential or specialization
[Example Provider Qualification Codes](valueset-provider-qualification.html) ([Example](terminologies.html#example)) | |

| [supportingInfo](claim-definitions.html#Claim.supportingInfo) | | 0..* | [BackboneElement](backboneelement.html) | Supporting information
 | |

| [sequence](claim-definitions.html#Claim.supportingInfo.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Information instance identifier | |

| [category](claim-definitions.html#Claim.supportingInfo.category) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of the supplied information
[Claim Information Category Codes](valueset-claim-informationcategory.html) ([Example](terminologies.html#example)) | |

| [code](claim-definitions.html#Claim.supportingInfo.code) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of information
[Exception Codes](valueset-claim-exception.html) ([Example](terminologies.html#example)) | |

| [timing[x]](claim-definitions.html#Claim.supportingInfo.timing_x_) | | 0..1 | | When it occurred | |

| timingDate | | | [date](datatypes.html#date) | | |

| timingPeriod | | | [Period](datatypes.html#Period) | | |

| [value[x]](claim-definitions.html#Claim.supportingInfo.value_x_) | | 0..1 | | Data to be provided | |

| valueBoolean | | | [boolean](datatypes.html#boolean) | | |

| valueString | | | [string](datatypes.html#string) | | |

| valueQuantity | | | [Quantity](datatypes.html#Quantity) | | |

| valueAttachment | | | [Attachment](datatypes.html#Attachment) | | |

| valueReference | | | [Reference](references.html#Reference)([Any](resourcelist.html)) | | |

| [reason](claim-definitions.html#Claim.supportingInfo.reason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Explanation for the information
[Missing Tooth Reason Codes](valueset-missing-tooth-reason.html) ([Example](terminologies.html#example)) | |

| [diagnosis](claim-definitions.html#Claim.diagnosis) | | 0..* | [BackboneElement](backboneelement.html) | Pertinent diagnosis information
 | |

| [sequence](claim-definitions.html#Claim.diagnosis.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Diagnosis instance identifier | |

| [diagnosis[x]](claim-definitions.html#Claim.diagnosis.diagnosis_x_) | | 1..1 | | Nature of illness or problem
[ICD-10 Codes](valueset-icd-10.html) ([Example](terminologies.html#example)) | |

| diagnosisCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| diagnosisReference | | | [Reference](references.html#Reference)([Condition](condition.html)) | | |

| [type](claim-definitions.html#Claim.diagnosis.type) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Timing or nature of the diagnosis
[Example Diagnosis Type Codes](valueset-ex-diagnosistype.html) ([Example](terminologies.html#example))
 | |

| [onAdmission](claim-definitions.html#Claim.diagnosis.onAdmission) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Present on admission
[Example Diagnosis on Admission Codes](valueset-ex-diagnosis-on-admission.html) ([Example](terminologies.html#example)) | |

| [packageCode](claim-definitions.html#Claim.diagnosis.packageCode) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Package billing code
[Example Diagnosis Related Group Codes](valueset-ex-diagnosisrelatedgroup.html) ([Example](terminologies.html#example)) | |

| [procedure](claim-definitions.html#Claim.procedure) | | 0..* | [BackboneElement](backboneelement.html) | Clinical procedures performed
 | |

| [sequence](claim-definitions.html#Claim.procedure.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Procedure instance identifier | |

| [type](claim-definitions.html#Claim.procedure.type) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Category of Procedure
[Example Procedure Type Codes](valueset-ex-procedure-type.html) ([Example](terminologies.html#example))
 | |

| [date](claim-definitions.html#Claim.procedure.date) | | 0..1 | [dateTime](datatypes.html#dateTime) | When the procedure was performed | |

| [procedure[x]](claim-definitions.html#Claim.procedure.procedure_x_) | | 1..1 | | Specific clinical procedure
[ICD-10 Procedure Codes](valueset-icd-10-procedures.html) ([Example](terminologies.html#example)) | |

| procedureCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| procedureReference | | | [Reference](references.html#Reference)([Procedure](procedure.html)) | | |

| [udi](claim-definitions.html#Claim.procedure.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [insurance](claim-definitions.html#Claim.insurance) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [BackboneElement](backboneelement.html) | Patient insurance information
 | |

| [sequence](claim-definitions.html#Claim.insurance.sequence) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [positiveInt](datatypes.html#positiveInt) | Insurance instance identifier | |

| [focal](claim-definitions.html#Claim.insurance.focal) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [boolean](datatypes.html#boolean) | Coverage to be used for adjudication | |

| [identifier](claim-definitions.html#Claim.insurance.identifier) | | 0..1 | [Identifier](datatypes.html#Identifier) | Pre-assigned Claim number | |

| [coverage](claim-definitions.html#Claim.insurance.coverage) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Coverage](coverage.html)) | Insurance information | |

| [businessArrangement](claim-definitions.html#Claim.insurance.businessArrangement) | | 0..1 | [string](datatypes.html#string) | Additional provider contract number | |

| [preAuthRef](claim-definitions.html#Claim.insurance.preAuthRef) | | 0..* | [string](datatypes.html#string) | Prior authorization reference number
 | |

| [claimResponse](claim-definitions.html#Claim.insurance.claimResponse) | | 0..1 | [Reference](references.html#Reference)([ClaimResponse](claimresponse.html)) | Adjudication results | |

| [accident](claim-definitions.html#Claim.accident) | | 0..1 | [BackboneElement](backboneelement.html) | Details of the event | |

| [date](claim-definitions.html#Claim.accident.date) | | 1..1 | [date](datatypes.html#date) | When the incident occurred | |

| [type](claim-definitions.html#Claim.accident.type) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The nature of the accident
[V3 Value SetActIncidentCode](v3/ActIncidentCode/vs.html) ([Extensible](terminologies.html#extensible)) | |

| [location[x]](claim-definitions.html#Claim.accident.location_x_) | | 0..1 | | Where the event occurred | |

| locationAddress | | | [Address](datatypes.html#Address) | | |

| locationReference | | | [Reference](references.html#Reference)([Location](location.html)) | | |

| [item](claim-definitions.html#Claim.item) | | 0..* | [BackboneElement](backboneelement.html) | Product or service provided
 | |

| [sequence](claim-definitions.html#Claim.item.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Item instance identifier | |

| [careTeamSequence](claim-definitions.html#Claim.item.careTeamSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable careTeam members
 | |

| [diagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable diagnoses
 | |

| [procedureSequence](claim-definitions.html#Claim.item.procedureSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable procedures
 | |

| [informationSequence](claim-definitions.html#Claim.item.informationSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable exception and supporting information
 | |

| [revenue](claim-definitions.html#Claim.item.revenue) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Revenue or cost center code
[Example Revenue Center Codes](valueset-ex-revenue-center.html) ([Example](terminologies.html#example)) | |

| [category](claim-definitions.html#Claim.item.category) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Benefit classification
[Benefit Category Codes](valueset-ex-benefitcategory.html) ([Example](terminologies.html#example)) | |

| [productOrService](claim-definitions.html#Claim.item.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claim-definitions.html#Claim.item.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Product or service billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [programCode](claim-definitions.html#Claim.item.programCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Program the product or service is provided under
[Example Program Reason Codes](valueset-ex-program-code.html) ([Example](terminologies.html#example))
 | |

| [serviced[x]](claim-definitions.html#Claim.item.serviced_x_) | | 0..1 | | Date or dates of service or product delivery | |

| servicedDate | | | [date](datatypes.html#date) | | |

| servicedPeriod | | | [Period](datatypes.html#Period) | | |

| [location[x]](claim-definitions.html#Claim.item.location_x_) | | 0..1 | | Place of service or where product was supplied
[Example Service Place Codes](valueset-service-place.html) ([Example](terminologies.html#example)) | |

| locationCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| locationAddress | | | [Address](datatypes.html#Address) | | |

| locationReference | | | [Reference](references.html#Reference)([Location](location.html)) | | |

| [quantity](claim-definitions.html#Claim.item.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claim-definitions.html#Claim.item.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claim-definitions.html#Claim.item.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claim-definitions.html#Claim.item.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [udi](claim-definitions.html#Claim.item.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [bodySite](claim-definitions.html#Claim.item.bodySite) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location
[Oral Site Codes](valueset-tooth.html) ([Example](terminologies.html#example)) | |

| [subSite](claim-definitions.html#Claim.item.subSite) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical sub-location
[Surface Codes](valueset-surface.html) ([Example](terminologies.html#example))
 | |

| [encounter](claim-definitions.html#Claim.item.encounter) | | 0..* | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounters related to this billed item
 | |

| [detail](claim-definitions.html#Claim.item.detail) | | 0..* | [BackboneElement](backboneelement.html) | Product or service provided
 | |

| [sequence](claim-definitions.html#Claim.item.detail.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Item instance identifier | |

| [revenue](claim-definitions.html#Claim.item.detail.revenue) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Revenue or cost center code
[Example Revenue Center Codes](valueset-ex-revenue-center.html) ([Example](terminologies.html#example)) | |

| [category](claim-definitions.html#Claim.item.detail.category) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Benefit classification
[Benefit Category Codes](valueset-ex-benefitcategory.html) ([Example](terminologies.html#example)) | |

| [productOrService](claim-definitions.html#Claim.item.detail.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claim-definitions.html#Claim.item.detail.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Service/Product billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [programCode](claim-definitions.html#Claim.item.detail.programCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Program the product or service is provided under
[Example Program Reason Codes](valueset-ex-program-code.html) ([Example](terminologies.html#example))
 | |

| [quantity](claim-definitions.html#Claim.item.detail.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claim-definitions.html#Claim.item.detail.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claim-definitions.html#Claim.item.detail.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claim-definitions.html#Claim.item.detail.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [udi](claim-definitions.html#Claim.item.detail.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [subDetail](claim-definitions.html#Claim.item.detail.subDetail) | | 0..* | [BackboneElement](backboneelement.html) | Product or service provided
 | |

| [sequence](claim-definitions.html#Claim.item.detail.subDetail.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Item instance identifier | |

| [revenue](claim-definitions.html#Claim.item.detail.subDetail.revenue) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Revenue or cost center code
[Example Revenue Center Codes](valueset-ex-revenue-center.html) ([Example](terminologies.html#example)) | |

| [category](claim-definitions.html#Claim.item.detail.subDetail.category) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Benefit classification
[Benefit Category Codes](valueset-ex-benefitcategory.html) ([Example](terminologies.html#example)) | |

| [productOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claim-definitions.html#Claim.item.detail.subDetail.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Service/Product billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [programCode](claim-definitions.html#Claim.item.detail.subDetail.programCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Program the product or service is provided under
[Example Program Reason Codes](valueset-ex-program-code.html) ([Example](terminologies.html#example))
 | |

| [quantity](claim-definitions.html#Claim.item.detail.subDetail.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claim-definitions.html#Claim.item.detail.subDetail.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claim-definitions.html#Claim.item.detail.subDetail.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [udi](claim-definitions.html#Claim.item.detail.subDetail.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [total](claim-definitions.html#Claim.total) | | 0..1 | [Money](datatypes.html#Money) | Total claim cost | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Claim ([DomainResource](domainresource.html))[A unique identifier assigned to this claimidentifier](claim-definitions.html#Claim.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The status of the resource instance (this element modifies the meaning of other elements)status](claim-definitions.html#Claim.status) : [code](datatypes.html#code) [1..1] « [A code specifying the state of the resource instance. (Strength=Required)FinancialResourceStatusCodes](valueset-fm-status.html)! »[The category of claim, e.g. oral, pharmacy, vision, institutional, professionaltype](claim-definitions.html#Claim.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The type or discipline-style of the claim. (Strength=Extensible)ClaimTypeCodes](valueset-claim-type.html)+ »[A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty servicesubType](claim-definitions.html#Claim.subType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A more granular claim typecode. (Strength=Example)ExampleClaimSubTypeCodes](valueset-claim-subtype.html)?? »[A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the futureuse](claim-definitions.html#Claim.use) : [code](datatypes.html#code) [1..1] « [The purpose of the Claim: predetermination, preauthorization, claim. (Strength=Required)Use](valueset-claim-use.html)! »[The party to whom the professional services and/or products have been supplied or are being considered and for whom actual or forecast reimbursement is soughtpatient](claim-definitions.html#Claim.patient) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient) »[The period for which charges are being submittedbillablePeriod](claim-definitions.html#Claim.billablePeriod) : [Period](datatypes.html#Period) [0..1][The date this resource was createdcreated](claim-definitions.html#Claim.created) : [dateTime](datatypes.html#dateTime) [1..1][Individual who created the claim, predetermination or preauthorizationenterer](claim-definitions.html#Claim.enterer) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[The Insurer who is target of the requestinsurer](claim-definitions.html#Claim.insurer) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The provider which is responsible for the claim, predetermination or preauthorizationprovider](claim-definitions.html#Claim.provider) : [Reference](references.html#Reference) [1..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[The provider-required urgency of processing the request. Typical values include: stat, routine deferredpriority](claim-definitions.html#Claim.priority) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The timeliness with which processing is required: stat, normal, deferred. (Strength=Example)ProcessPriorityCodes](valueset-process-priority.html)?? »[A code to indicate whether and for whom funds are to be reserved for future claimsfundsReserve](claim-definitions.html#Claim.fundsReserve) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [For whom funds are to be reserved: (Patient, Provider, None). (Strength=Example)Funds Reservation ](valueset-fundsreserve.html)?? »[Prescription to support the dispensing of pharmacy, device or vision productsprescription](claim-definitions.html#Claim.prescription) : [Reference](references.html#Reference) [0..1] « [DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)| [VisionPrescription](visionprescription.html#VisionPrescription) »[Original prescription which has been superseded by this prescription to support the dispensing of pharmacy services, medications or productsoriginalPrescription](claim-definitions.html#Claim.originalPrescription) : [Reference](references.html#Reference) [0..1] « [DeviceRequest](devicerequest.html#DeviceRequest)| [MedicationRequest](medicationrequest.html#MedicationRequest)|[VisionPrescription](visionprescription.html#VisionPrescription) »[A reference to a referral resourcereferral](claim-definitions.html#Claim.referral) : [Reference](references.html#Reference) [0..1] « [ServiceRequest](servicerequest.html#ServiceRequest) »[Facility where the services were providedfacility](claim-definitions.html#Claim.facility) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location) »[The total value of the all the items in the claimtotal](claim-definitions.html#Claim.total) : [Money](datatypes.html#Money) [0..1]RelatedClaim[Reference to a related claimclaim](claim-definitions.html#Claim.related.claim) : [Reference](references.html#Reference) [0..1] « [Claim](claim.html#Claim) »[A code to convey how the claims are relatedrelationship](claim-definitions.html#Claim.related.relationship) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Relationship of this claim to a related Claim. (Strength=Example)](valueset-related-claim-relationship.html) [ExampleRelatedClaimRelationsh...](valueset-related-claim-relationship.html)?? »[An alternate organizational reference to the case or file to which this particular claim pertainsreference](claim-definitions.html#Claim.related.reference) : [Identifier](datatypes.html#Identifier) [0..1]Payee[Type of Party to be reimbursed: subscriber, provider, othertype](claim-definitions.html#Claim.payee.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [A code for the party to be reimbursed. (Strength=Example)Claim Payee Type ](valueset-payeetype.html)?? »[Reference to the individual or organization to whom any payment will be madeparty](claim-definitions.html#Claim.payee.party) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »CareTeam[A number to uniquely identify care team entriessequence](claim-definitions.html#Claim.careTeam.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][Member of the team who provided the product or serviceprovider](claim-definitions.html#Claim.careTeam.provider) : [Reference](references.html#Reference) [1..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[The party who is billing and/or responsible for the claimed products or servicesresponsible](claim-definitions.html#Claim.careTeam.responsible) : [boolean](datatypes.html#boolean) [0..1][The lead, assisting or supervising practitioner and their discipline if a multidisciplinary teamrole](claim-definitions.html#Claim.careTeam.role) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The role codes for the care team members. (Strength=Example)ClaimCareTeamRoleCodes](valueset-claim-careteamrole.html)?? »[The qualification of the practitioner which is applicable for this servicequalification](claim-definitions.html#Claim.careTeam.qualification) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Provider professional qualifications. (Strength=Example)](valueset-provider-qualification.html) [ExampleProviderQualificationC...](valueset-provider-qualification.html)?? »SupportingInformation[A number to uniquely identify supporting information entriessequence](claim-definitions.html#Claim.supportingInfo.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The general class of the information supplied: information; exception; accident, employment; onset, etccategory](claim-definitions.html#Claim.supportingInfo.category) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The valuset used for additional information category codes. (Strength=Example)ClaimInformationCategoryCodes](valueset-claim-informationcategory.html)?? »[System and code pertaining to the specific information regarding special conditions relating to the setting, treatment or patient for which care is soughtcode](claim-definitions.html#Claim.supportingInfo.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The valuset used for additional information codes. (Strength=Example)ExceptionCodes](valueset-claim-exception.html)?? »[The date when or period to which this information referstiming[x]](claim-definitions.html#Claim.supportingInfo.timing_x_) : [Type](formats.html#umlchoice) [0..1] « [date](datatypes.html#date)|[Period](datatypes.html#Period) »[Additional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the datavalue[x]](claim-definitions.html#Claim.supportingInfo.value_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[string](datatypes.html#string)|[Quantity](datatypes.html#Quantity)|[Attachment](datatypes.html#Attachment)| [Reference](references.html#Reference)([Any](resourcelist.html#Any)) »[Provides the reason in the situation where a reason code is required in addition to the contentreason](claim-definitions.html#Claim.supportingInfo.reason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Reason codes for the missing teeth. (Strength=Example)MissingToothReasonCodes](valueset-missing-tooth-reason.html)?? »Diagnosis[A number to uniquely identify diagnosis entriessequence](claim-definitions.html#Claim.diagnosis.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The nature of illness or problem in a coded form or as a reference to an external defined Conditiondiagnosis[x]](claim-definitions.html#Claim.diagnosis.diagnosis_x_) : [Type](formats.html#umlchoice) [1..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Condition](condition.html#Condition)); [Example ICD10 Diagnostic codes. (Strength=Example)](valueset-icd-10.html) [ICD-10Codes](valueset-icd-10.html)?? »[When the condition was observed or the relative rankingtype](claim-definitions.html#Claim.diagnosis.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The type of the diagnosis: admitting, principal, discharge. (Strength=Example)ExampleDiagnosisTypeCodes](valueset-ex-diagnosistype.html)?? »[Indication of whether the diagnosis was present on admission to a facilityonAdmission](claim-definitions.html#Claim.diagnosis.onAdmission) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Present on admission. (Strength=Example)](valueset-ex-diagnosis-on-admission.html) [ExampleDiagnosisOnAdmissionCo...](valueset-ex-diagnosis-on-admission.html)?? »[A package billing code or bundle code used to group products and services to a particular health condition (such as heart attack) which is based on a predetermined grouping code systempackageCode](claim-definitions.html#Claim.diagnosis.packageCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The DRG codes associated with the diagnosis. (Strength=Example)](valueset-ex-diagnosisrelatedgroup.html) [ExampleDiagnosisRelatedGroupC...](valueset-ex-diagnosisrelatedgroup.html)?? »Procedure[A number to uniquely identify procedure entriessequence](claim-definitions.html#Claim.procedure.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][When the condition was observed or the relative rankingtype](claim-definitions.html#Claim.procedure.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Example procedure type codes. (Strength=Example)ExampleProcedureTypeCodes](valueset-ex-procedure-type.html)?? »[Date and optionally time the procedure was performeddate](claim-definitions.html#Claim.procedure.date) : [dateTime](datatypes.html#dateTime) [0..1][The code or reference to a Procedure resource which identifies the clinical intervention performedprocedure[x]](claim-definitions.html#Claim.procedure.procedure_x_) : [Type](formats.html#umlchoice) [1..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Procedure](procedure.html#Procedure)); [Example ICD10 Procedure codes. (Strength=Example)](valueset-icd-10-procedures.html) [ICD-10ProcedureCodes](valueset-icd-10-procedures.html)?? »[Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.procedure.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »Insurance[A number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit ordersequence](claim-definitions.html#Claim.insurance.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][A flag to indicate that this Coverage is to be used for adjudication of this claim when set to truefocal](claim-definitions.html#Claim.insurance.focal) : [boolean](datatypes.html#boolean) [1..1][The business identifier to be used when the claim is sent for adjudication against this insurance policyidentifier](claim-definitions.html#Claim.insurance.identifier) : [Identifier](datatypes.html#Identifier) [0..1][Reference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information systemcoverage](claim-definitions.html#Claim.insurance.coverage) : [Reference](references.html#Reference) [1..1] « [Coverage](coverage.html#Coverage) »[A business agreement number established between the provider and the insurer for special business processing purposesbusinessArrangement](claim-definitions.html#Claim.insurance.businessArrangement) : [string](datatypes.html#string) [0..1][Reference numbers previously provided by the insurer to the provider to be quoted on subsequent claims containing services or products related to the prior authorizationpreAuthRef](claim-definitions.html#Claim.insurance.preAuthRef) : [string](datatypes.html#string) [0..*][The result of the adjudication of the line items for the Coverage specified in this insuranceclaimResponse](claim-definitions.html#Claim.insurance.claimResponse) : [Reference](references.html#Reference) [0..1] « [ClaimResponse](claimresponse.html#ClaimResponse) »Accident[Date of an accident event related to the products and services contained in the claimdate](claim-definitions.html#Claim.accident.date) : [date](datatypes.html#date) [1..1][The type or context of the accident event for the purposes of selection of potential insurance coverages and determination of coordination between insurerstype](claim-definitions.html#Claim.accident.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Type of accident: work place, auto, etc. (Strength=Extensible)v3.ActIncidentCode](v3/ActIncidentCode/vs.html)+ »[The physical location of the accident eventlocation[x]](claim-definitions.html#Claim.accident.location_x_) : [Type](formats.html#umlchoice) [0..1] « [Address](datatypes.html#Address)|[Reference](references.html#Reference)([Location](location.html#Location)) »Item[A number to uniquely identify item entriessequence](claim-definitions.html#Claim.item.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][CareTeam members related to this service or productcareTeamSequence](claim-definitions.html#Claim.item.careTeamSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][Diagnosis applicable for this service or productdiagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][Procedures applicable for this service or productprocedureSequence](claim-definitions.html#Claim.item.procedureSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][Exceptions, special conditions and supporting information applicable for this service or productinformationSequence](claim-definitions.html#Claim.item.informationSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][The type of revenue or cost center providing the product and/or servicerevenue](claim-definitions.html#Claim.item.revenue) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the revenue or cost centers supplying the service and/or products. (Strength=Example)ExampleRevenueCenterCodes](valueset-ex-revenue-center.html)?? »[Code to identify the general type of benefits under which products and services are providedcategory](claim-definitions.html#Claim.item.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Benefit categories such as: oral-basic, major, glasses. (Strength=Example)BenefitCategoryCodes](valueset-ex-benefitcategory.html)?? »[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claim-definitions.html#Claim.item.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claim-definitions.html#Claim.item.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[Identifies the program under which this may be recoveredprogramCode](claim-definitions.html#Claim.item.programCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Program specific reason codes. (Strength=Example)ExampleProgramReasonCodes](valueset-ex-program-code.html)?? »[The date or dates when the service or product was supplied, performed or completedserviced[x]](claim-definitions.html#Claim.item.serviced_x_) : [Type](formats.html#umlchoice) [0..1] « [date](datatypes.html#date)|[Period](datatypes.html#Period) »[Where the product or service was providedlocation[x]](claim-definitions.html#Claim.item.location_x_) : [Type](formats.html#umlchoice) [0..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Address](datatypes.html#Address)|[Reference](references.html#Reference)( [Location](location.html#Location)); [Place of service: pharmacy, school, prison, etc. (Strength=Example)ExampleServicePlaceCodes](valueset-service-place.html)?? »[The number of repetitions of a service or productquantity](claim-definitions.html#Claim.item.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claim-definitions.html#Claim.item.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claim-definitions.html#Claim.item.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claim-definitions.html#Claim.item.net) : [Money](datatypes.html#Money) [0..1][Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.item.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »[Physical service site on the patient (limb, tooth, etc.)bodySite](claim-definitions.html#Claim.item.bodySite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The code for the teeth, quadrant, sextant and arch. (Strength=Example)OralSiteCodes](valueset-tooth.html)?? »[A region or surface of the bodySite, e.g. limb region or tooth surface(s)subSite](claim-definitions.html#Claim.item.subSite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The code for the tooth surface and surface combinations. (Strength=Example)SurfaceCodes](valueset-surface.html)?? »[The Encounters during which this Claim was created or to which the creation of this record is tightly associatedencounter](claim-definitions.html#Claim.item.encounter) : [Reference](references.html#Reference) [0..*] « [Encounter](encounter.html#Encounter) »Detail[A number to uniquely identify item entriessequence](claim-definitions.html#Claim.item.detail.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The type of revenue or cost center providing the product and/or servicerevenue](claim-definitions.html#Claim.item.detail.revenue) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the revenue or cost centers supplying the service and/or products. (Strength=Example)ExampleRevenueCenterCodes](valueset-ex-revenue-center.html)?? »[Code to identify the general type of benefits under which products and services are providedcategory](claim-definitions.html#Claim.item.detail.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Benefit categories such as: oral-basic, major, glasses. (Strength=Example)BenefitCategoryCodes](valueset-ex-benefitcategory.html)?? »[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claim-definitions.html#Claim.item.detail.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claim-definitions.html#Claim.item.detail.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[Identifies the program under which this may be recoveredprogramCode](claim-definitions.html#Claim.item.detail.programCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Program specific reason codes. (Strength=Example)ExampleProgramReasonCodes](valueset-ex-program-code.html)?? »[The number of repetitions of a service or productquantity](claim-definitions.html#Claim.item.detail.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claim-definitions.html#Claim.item.detail.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claim-definitions.html#Claim.item.detail.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claim-definitions.html#Claim.item.detail.net) : [Money](datatypes.html#Money) [0..1][Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.item.detail.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »SubDetail[A number to uniquely identify item entriessequence](claim-definitions.html#Claim.item.detail.subDetail.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The type of revenue or cost center providing the product and/or servicerevenue](claim-definitions.html#Claim.item.detail.subDetail.revenue) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the revenue or cost centers supplying the service and/or products. (Strength=Example)ExampleRevenueCenterCodes](valueset-ex-revenue-center.html)?? »[Code to identify the general type of benefits under which products and services are providedcategory](claim-definitions.html#Claim.item.detail.subDetail.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Benefit categories such as: oral-basic, major, glasses. (Strength=Example)BenefitCategoryCodes](valueset-ex-benefitcategory.html)?? »[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claim-definitions.html#Claim.item.detail.subDetail.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[Identifies the program under which this may be recoveredprogramCode](claim-definitions.html#Claim.item.detail.subDetail.programCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Program specific reason codes. (Strength=Example)ExampleProgramReasonCodes](valueset-ex-program-code.html)?? »[The number of repetitions of a service or productquantity](claim-definitions.html#Claim.item.detail.subDetail.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claim-definitions.html#Claim.item.detail.subDetail.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claim-definitions.html#Claim.item.detail.subDetail.net) : [Money](datatypes.html#Money) [0..1][Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.item.detail.subDetail.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »
[Other claims which are related to this claim such as prior submissions or claims for related services or for the same eventrelated](claim-definitions.html#Claim.related)[0..*][The party to be reimbursed for cost of the products and services according to the terms of the policypayee](claim-definitions.html#Claim.payee)[0..1][The members of the team who provided the products and servicescareTeam](claim-definitions.html#Claim.careTeam)[0..*][Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issuessupportingInfo](claim-definitions.html#Claim.supportingInfo)[0..*][Information about diagnoses relevant to the claim itemsdiagnosis](claim-definitions.html#Claim.diagnosis)[0..*][Procedures performed on the patient relevant to the billing items with the claimprocedure](claim-definitions.html#Claim.procedure)[0..*][Financial instruments for reimbursement for the health care products and services specified on the claiminsurance](claim-definitions.html#Claim.insurance)[1..*][Details of an accident which resulted in injuries which required the products and services listed in the claimaccident](claim-definitions.html#Claim.accident)[0..1][A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemssubDetail](claim-definitions.html#Claim.item.detail.subDetail)[0..*][A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsdetail](claim-definitions.html#Claim.item.detail)[0..*][A claim line. Either a simple product or service or a 'group' of details which can each be a simple items or groups of sub-detailsitem](claim-definitions.html#Claim.item)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Claim**](claim-definitions.html#Claim) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](claim-definitions.html#Claim.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business Identifier for claim](terminologies.html#unbound) --></identifier>
 <[**status**](claim-definitions.html#Claim.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [active | cancelled | draft | entered-in-error](valueset-fm-status.html) -->
 <[**type**](claim-definitions.html#Claim.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Category or discipline](valueset-claim-type.html) --></type>
 <[**subType**](claim-definitions.html#Claim.subType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [More granular claim type](valueset-claim-subtype.html) --></subType>
 <[**use**](claim-definitions.html#Claim.use) value="[[code](datatypes.html#code)]"/><!-- **1..1** [claim | preauthorization | predetermination](valueset-claim-use.html) -->
 <[**patient**](claim-definitions.html#Claim.patient)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)) [The recipient of the products and services](terminologies.html#unbound) --></patient>
 <[**billablePeriod**](claim-definitions.html#Claim.billablePeriod)><!-- **0..1** [Period](datatypes.html#Period) [Relevant time frame for the claim](terminologies.html#unbound) --></billablePeriod>
 <[**created**](claim-definitions.html#Claim.created) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **1..1** [Resource creation date](terminologies.html#unbound) -->
 <[**enterer**](claim-definitions.html#Claim.enterer)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [Author of the claim](terminologies.html#unbound) --></enterer>
 <[**insurer**](claim-definitions.html#Claim.insurer)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Target](terminologies.html#unbound) --></insurer>
 <[**provider**](claim-definitions.html#Claim.provider)><!-- **1..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) [Party responsible for the claim](terminologies.html#unbound) --></provider>
 <[**priority**](claim-definitions.html#Claim.priority)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Desired processing ugency](valueset-process-priority.html) --></priority>
 <[**fundsReserve**](claim-definitions.html#Claim.fundsReserve)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [For whom to reserve funds](valueset-fundsreserve.html) --></fundsReserve>
 <[**related**](claim-definitions.html#Claim.related)> <!-- **0..*** Prior or corollary claims -->
 <[**claim**](claim-definitions.html#Claim.related.claim)><!-- **0..1** [Reference](references.html#Reference)([Claim](claim.html#Claim)) [Reference to the related claim](terminologies.html#unbound) --></claim>
 <[**relationship**](claim-definitions.html#Claim.related.relationship)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [How the reference claim is related](valueset-related-claim-relationship.html) --></relationship>
 <[**reference**](claim-definitions.html#Claim.related.reference)><!-- **0..1** [Identifier](datatypes.html#Identifier) [File or case reference](terminologies.html#unbound) --></reference>
 </related>
 <[**prescription**](claim-definitions.html#Claim.prescription)><!-- **0..1** [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) [Prescription authorizing services and products](terminologies.html#unbound) --></prescription>
 <[**originalPrescription**](claim-definitions.html#Claim.originalPrescription)><!-- **0..1** [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) [Original prescription if superseded by fulfiller](terminologies.html#unbound) --></originalPrescription>
 <[**payee**](claim-definitions.html#Claim.payee)> <!-- **0..1** Recipient of benefits payable -->
 <[**type**](claim-definitions.html#Claim.payee.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Category of recipient](valueset-payeetype.html) --></type>
 <[**party**](claim-definitions.html#Claim.payee.party)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)) [Recipient reference](terminologies.html#unbound) --></party>
 </payee>
 <[**referral**](claim-definitions.html#Claim.referral)><!-- **0..1** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [Treatment referral](terminologies.html#unbound) --></referral>
 <[**facility**](claim-definitions.html#Claim.facility)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)) [Servicing facility](terminologies.html#unbound) --></facility>
 <[**careTeam**](claim-definitions.html#Claim.careTeam)> <!-- **0..*** Members of the care team -->
 <[**sequence**](claim-definitions.html#Claim.careTeam.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Order of care team](terminologies.html#unbound) -->
 <[**provider**](claim-definitions.html#Claim.careTeam.provider)><!-- **1..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) [Practitioner or organization](terminologies.html#unbound) --></provider>
 <[**responsible**](claim-definitions.html#Claim.careTeam.responsible) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Indicator of the lead practitioner](terminologies.html#unbound) -->
 <[**role**](claim-definitions.html#Claim.careTeam.role)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Function within the team](valueset-claim-careteamrole.html) --></role>
 <[**qualification**](claim-definitions.html#Claim.careTeam.qualification)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Practitioner credential or specialization](valueset-provider-qualification.html) --></qualification>
 </careTeam>
 <[**supportingInfo**](claim-definitions.html#Claim.supportingInfo)> <!-- **0..*** Supporting information -->
 <[**sequence**](claim-definitions.html#Claim.supportingInfo.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Information instance identifier](terminologies.html#unbound) -->
 <[**category**](claim-definitions.html#Claim.supportingInfo.category)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Classification of the supplied information](valueset-claim-informationcategory.html) --></category>
 <[**code**](claim-definitions.html#Claim.supportingInfo.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Type of information](valueset-claim-exception.html) --></code>
 <[**timing[x]**](claim-definitions.html#Claim.supportingInfo.timing[x])><!-- **0..1** [date](datatypes.html#date)|[Period](datatypes.html#Period) [When it occurred](terminologies.html#unbound) --></timing[x]>
 <[**value[x]**](claim-definitions.html#Claim.supportingInfo.value[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[string](datatypes.html#string)|[Quantity](datatypes.html#Quantity)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html)) [Data to be provided](terminologies.html#unbound) --></value[x]>
 <[**reason**](claim-definitions.html#Claim.supportingInfo.reason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Explanation for the information](valueset-missing-tooth-reason.html) --></reason>
 </supportingInfo>
 <[**diagnosis**](claim-definitions.html#Claim.diagnosis)> <!-- **0..*** Pertinent diagnosis information -->
 <[**sequence**](claim-definitions.html#Claim.diagnosis.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Diagnosis instance identifier](terminologies.html#unbound) -->
 <[**diagnosis[x]**](claim-definitions.html#Claim.diagnosis.diagnosis[x])><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Condition](condition.html#Condition)) [Nature of illness or problem](valueset-icd-10.html) --></diagnosis[x]>
 <[**type**](claim-definitions.html#Claim.diagnosis.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Timing or nature of the diagnosis](valueset-ex-diagnosistype.html) --></type>
 <[**onAdmission**](claim-definitions.html#Claim.diagnosis.onAdmission)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Present on admission](valueset-ex-diagnosis-on-admission.html) --></onAdmission>
 <[**packageCode**](claim-definitions.html#Claim.diagnosis.packageCode)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Package billing code](valueset-ex-diagnosisrelatedgroup.html) --></packageCode>
 </diagnosis>
 <[**procedure**](claim-definitions.html#Claim.procedure)> <!-- **0..*** Clinical procedures performed -->
 <[**sequence**](claim-definitions.html#Claim.procedure.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Procedure instance identifier](terminologies.html#unbound) -->
 <[**type**](claim-definitions.html#Claim.procedure.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Category of Procedure](valueset-ex-procedure-type.html) --></type>
 <[**date**](claim-definitions.html#Claim.procedure.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When the procedure was performed](terminologies.html#unbound) -->
 <[**procedure[x]**](claim-definitions.html#Claim.procedure.procedure[x])><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Procedure](procedure.html#Procedure)) [Specific clinical procedure](valueset-icd-10-procedures.html) --></procedure[x]>
 <[**udi**](claim-definitions.html#Claim.procedure.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 </procedure>
 <[**insurance**](claim-definitions.html#Claim.insurance)> <!-- **1..*** Patient insurance information -->
 <[**sequence**](claim-definitions.html#Claim.insurance.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Insurance instance identifier](terminologies.html#unbound) -->
 <[**focal**](claim-definitions.html#Claim.insurance.focal) value="[[boolean](datatypes.html#boolean)]"/><!-- **1..1** [Coverage to be used for adjudication](terminologies.html#unbound) -->
 <[**identifier**](claim-definitions.html#Claim.insurance.identifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Pre-assigned Claim number](terminologies.html#unbound) --></identifier>
 <[**coverage**](claim-definitions.html#Claim.insurance.coverage)><!-- **1..1** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) [Insurance information](terminologies.html#unbound) --></coverage>
 <[**businessArrangement**](claim-definitions.html#Claim.insurance.businessArrangement) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional provider contract number](terminologies.html#unbound) -->
 <[**preAuthRef**](claim-definitions.html#Claim.insurance.preAuthRef) value="[[string](datatypes.html#string)]"/><!-- **0..*** [Prior authorization reference number](terminologies.html#unbound) -->
 <[**claimResponse**](claim-definitions.html#Claim.insurance.claimResponse)><!-- **0..1** [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) [Adjudication results](terminologies.html#unbound) --></claimResponse>
 </insurance>
 <[**accident**](claim-definitions.html#Claim.accident)> <!-- **0..1** Details of the event -->
 <[**date**](claim-definitions.html#Claim.accident.date) value="[[date](datatypes.html#date)]"/><!-- **1..1** [When the incident occurred](terminologies.html#unbound) -->
 <[**type**](claim-definitions.html#Claim.accident.type)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The nature of the accident](v3/ActIncidentCode/vs.html) --></type>
 <[**location[x]**](claim-definitions.html#Claim.accident.location[x])><!-- **0..1** [Address](datatypes.html#Address)|[Reference](references.html#Reference)([Location](location.html#Location)) [Where the event occurred](terminologies.html#unbound) --></location[x]>
 </accident>
 <[**item**](claim-definitions.html#Claim.item)> <!-- **0..*** Product or service provided -->
 <[**sequence**](claim-definitions.html#Claim.item.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Item instance identifier](terminologies.html#unbound) -->
 <[**careTeamSequence**](claim-definitions.html#Claim.item.careTeamSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable careTeam members](terminologies.html#unbound) -->
 <[**diagnosisSequence**](claim-definitions.html#Claim.item.diagnosisSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable diagnoses](terminologies.html#unbound) -->
 <[**procedureSequence**](claim-definitions.html#Claim.item.procedureSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable procedures](terminologies.html#unbound) -->
 <[**informationSequence**](claim-definitions.html#Claim.item.informationSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable exception and supporting information](terminologies.html#unbound) -->
 <[**revenue**](claim-definitions.html#Claim.item.revenue)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Revenue or cost center code](valueset-ex-revenue-center.html) --></revenue>
 <[**category**](claim-definitions.html#Claim.item.category)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Benefit classification](valueset-ex-benefitcategory.html) --></category>
 <[**productOrService**](claim-definitions.html#Claim.item.productOrService)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Billing, service, product, or drug code](valueset-service-uscls.html) --></productOrService>
 <[**modifier**](claim-definitions.html#Claim.item.modifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Product or service billing modifiers](valueset-claim-modifiers.html) --></modifier>
 <[**programCode**](claim-definitions.html#Claim.item.programCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Program the product or service is provided under](valueset-ex-program-code.html) --></programCode>
 <[**serviced[x]**](claim-definitions.html#Claim.item.serviced[x])><!-- **0..1** [date](datatypes.html#date)|[Period](datatypes.html#Period) [Date or dates of service or product delivery](terminologies.html#unbound) --></serviced[x]>
 <[**location[x]**](claim-definitions.html#Claim.item.location[x])><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Address](datatypes.html#Address)|[Reference](references.html#Reference)([Location](location.html#Location)) [Place of service or where product was supplied](valueset-service-place.html) --></location[x]>
 <[**quantity**](claim-definitions.html#Claim.item.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Count of products or services](terminologies.html#unbound) --></quantity>
 <[**unitPrice**](claim-definitions.html#Claim.item.unitPrice)><!-- **0..1** [Money](datatypes.html#Money) [Fee, charge or cost per item](terminologies.html#unbound) --></unitPrice>
 <[**factor**](claim-definitions.html#Claim.item.factor) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Price scaling factor](terminologies.html#unbound) -->
 <[**net**](claim-definitions.html#Claim.item.net)><!-- **0..1** [Money](datatypes.html#Money) [Total item cost](terminologies.html#unbound) --></net>
 <[**udi**](claim-definitions.html#Claim.item.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 <[**bodySite**](claim-definitions.html#Claim.item.bodySite)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Anatomical location](valueset-tooth.html) --></bodySite>
 <[**subSite**](claim-definitions.html#Claim.item.subSite)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Anatomical sub-location](valueset-surface.html) --></subSite>
 <[**encounter**](claim-definitions.html#Claim.item.encounter)><!-- **0..*** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounters related to this billed item](terminologies.html#unbound) --></encounter>
 <[**detail**](claim-definitions.html#Claim.item.detail)> <!-- **0..*** Product or service provided -->
 <[**sequence**](claim-definitions.html#Claim.item.detail.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Item instance identifier](terminologies.html#unbound) -->
 <[**revenue**](claim-definitions.html#Claim.item.detail.revenue)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Revenue or cost center code](valueset-ex-revenue-center.html) --></revenue>
 <[**category**](claim-definitions.html#Claim.item.detail.category)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Benefit classification](valueset-ex-benefitcategory.html) --></category>
 <[**productOrService**](claim-definitions.html#Claim.item.detail.productOrService)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Billing, service, product, or drug code](valueset-service-uscls.html) --></productOrService>
 <[**modifier**](claim-definitions.html#Claim.item.detail.modifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Service/Product billing modifiers](valueset-claim-modifiers.html) --></modifier>
 <[**programCode**](claim-definitions.html#Claim.item.detail.programCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Program the product or service is provided under](valueset-ex-program-code.html) --></programCode>
 <[**quantity**](claim-definitions.html#Claim.item.detail.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Count of products or services](terminologies.html#unbound) --></quantity>
 <[**unitPrice**](claim-definitions.html#Claim.item.detail.unitPrice)><!-- **0..1** [Money](datatypes.html#Money) [Fee, charge or cost per item](terminologies.html#unbound) --></unitPrice>
 <[**factor**](claim-definitions.html#Claim.item.detail.factor) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Price scaling factor](terminologies.html#unbound) -->
 <[**net**](claim-definitions.html#Claim.item.detail.net)><!-- **0..1** [Money](datatypes.html#Money) [Total item cost](terminologies.html#unbound) --></net>
 <[**udi**](claim-definitions.html#Claim.item.detail.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 <[**subDetail**](claim-definitions.html#Claim.item.detail.subDetail)> <!-- **0..*** Product or service provided -->
 <[**sequence**](claim-definitions.html#Claim.item.detail.subDetail.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Item instance identifier](terminologies.html#unbound) -->
 <[**revenue**](claim-definitions.html#Claim.item.detail.subDetail.revenue)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Revenue or cost center code](valueset-ex-revenue-center.html) --></revenue>
 <[**category**](claim-definitions.html#Claim.item.detail.subDetail.category)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Benefit classification](valueset-ex-benefitcategory.html) --></category>
 <[**productOrService**](claim-definitions.html#Claim.item.detail.subDetail.productOrService)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Billing, service, product, or drug code](valueset-service-uscls.html) --></productOrService>
 <[**modifier**](claim-definitions.html#Claim.item.detail.subDetail.modifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Service/Product billing modifiers](valueset-claim-modifiers.html) --></modifier>
 <[**programCode**](claim-definitions.html#Claim.item.detail.subDetail.programCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Program the product or service is provided under](valueset-ex-program-code.html) --></programCode>
 <[**quantity**](claim-definitions.html#Claim.item.detail.subDetail.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Count of products or services](terminologies.html#unbound) --></quantity>
 <[**unitPrice**](claim-definitions.html#Claim.item.detail.subDetail.unitPrice)><!-- **0..1** [Money](datatypes.html#Money) [Fee, charge or cost per item](terminologies.html#unbound) --></unitPrice>
 <[**factor**](claim-definitions.html#Claim.item.detail.subDetail.factor) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Price scaling factor](terminologies.html#unbound) -->
 <[**net**](claim-definitions.html#Claim.item.detail.subDetail.net)><!-- **0..1** [Money](datatypes.html#Money) [Total item cost](terminologies.html#unbound) --></net>
 <[**udi**](claim-definitions.html#Claim.item.detail.subDetail.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 </subDetail>
 </detail>
 </item>
 <[**total**](claim-definitions.html#Claim.total)><!-- **0..1** [Money](datatypes.html#Money) [Total claim cost](terminologies.html#unbound) --></total>
</Claim>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Claim**](claim-definitions.html#Claim)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](claim-definitions.html#Claim.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business Identifier for claim](terminologies.html#unbound)
 "[status](claim-definitions.html#Claim.status)" : "<[code](datatypes.html#code)>", // **R!** [active | cancelled | draft | entered-in-error](valueset-fm-status.html)
 "[type](claim-definitions.html#Claim.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Category or discipline](valueset-claim-type.html)
 "[subType](claim-definitions.html#Claim.subType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [More granular claim type](valueset-claim-subtype.html)
 "[use](claim-definitions.html#Claim.use)" : "<[code](datatypes.html#code)>", // **R!** [claim | preauthorization | predetermination](valueset-claim-use.html)
 "[patient](claim-definitions.html#Claim.patient)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) }, // **R!** [The recipient of the products and services](terminologies.html#unbound)
 "[billablePeriod](claim-definitions.html#Claim.billablePeriod)" : { [Period](datatypes.html#Period) }, // [Relevant time frame for the claim](terminologies.html#unbound)
 "[created](claim-definitions.html#Claim.created)" : "<[dateTime](datatypes.html#dateTime)>", // **R!** [Resource creation date](terminologies.html#unbound)
 "[enterer](claim-definitions.html#Claim.enterer)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [Author of the claim](terminologies.html#unbound)
 "[insurer](claim-definitions.html#Claim.insurer)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Target](terminologies.html#unbound)
 "[provider](claim-definitions.html#Claim.provider)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }, // **R!** [Party responsible for the claim](terminologies.html#unbound)
 "[priority](claim-definitions.html#Claim.priority)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Desired processing ugency](valueset-process-priority.html)
 "[fundsReserve](claim-definitions.html#Claim.fundsReserve)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [For whom to reserve funds](valueset-fundsreserve.html)
 "[related](claim-definitions.html#Claim.related)" : [{ // [Prior or corollary claims](terminologies.html#unbound)
 "[claim](claim-definitions.html#Claim.related.claim)" : { [Reference](references.html#Reference)([Claim](claim.html#Claim)) }, // [Reference to the related claim](terminologies.html#unbound)
 "[relationship](claim-definitions.html#Claim.related.relationship)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [How the reference claim is related](valueset-related-claim-relationship.html)
 "[reference](claim-definitions.html#Claim.related.reference)" : { [Identifier](datatypes.html#Identifier) } // [File or case reference](terminologies.html#unbound)
 }],
 "[prescription](claim-definitions.html#Claim.prescription)" : { [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) }, // [Prescription authorizing services and products](terminologies.html#unbound)
 "[originalPrescription](claim-definitions.html#Claim.originalPrescription)" : { [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) }, // [Original prescription if superseded by fulfiller](terminologies.html#unbound)
 "[payee](claim-definitions.html#Claim.payee)" : { // [Recipient of benefits payable](terminologies.html#unbound)
 "[type](claim-definitions.html#Claim.payee.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Category of recipient](valueset-payeetype.html)
 "[party](claim-definitions.html#Claim.payee.party)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)) } // [Recipient reference](terminologies.html#unbound)
 },
 "[referral](claim-definitions.html#Claim.referral)" : { [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }, // [Treatment referral](terminologies.html#unbound)
 "[facility](claim-definitions.html#Claim.facility)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // [Servicing facility](terminologies.html#unbound)
 "[careTeam](claim-definitions.html#Claim.careTeam)" : [{ // [Members of the care team](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.careTeam.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Order of care team](terminologies.html#unbound)
 "[provider](claim-definitions.html#Claim.careTeam.provider)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }, // **R!** [Practitioner or organization](terminologies.html#unbound)
 "[responsible](claim-definitions.html#Claim.careTeam.responsible)" : <[boolean](datatypes.html#boolean)>, // [Indicator of the lead practitioner](terminologies.html#unbound)
 "[role](claim-definitions.html#Claim.careTeam.role)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Function within the team](valueset-claim-careteamrole.html)
 "[qualification](claim-definitions.html#Claim.careTeam.qualification)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Practitioner credential or specialization](valueset-provider-qualification.html)
 }],
 "[supportingInfo](claim-definitions.html#Claim.supportingInfo)" : [{ // [Supporting information](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.supportingInfo.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Information instance identifier](terminologies.html#unbound)
 "[category](claim-definitions.html#Claim.supportingInfo.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Classification of the supplied information](valueset-claim-informationcategory.html)
 "[code](claim-definitions.html#Claim.supportingInfo.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Type of information](valueset-claim-exception.html)
 // timing[x]: When it occurred. One of these 2:
 "[timingDate](claim-definitions.html#Claim.supportingInfo.timingDate)" : "<[date](datatypes.html#date)>",
 "[timingPeriod](claim-definitions.html#Claim.supportingInfo.timingPeriod)" : { [Period](datatypes.html#Period) },
 // value[x]: Data to be provided. One of these 5:
 "[valueBoolean](claim-definitions.html#Claim.supportingInfo.valueBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[valueString](claim-definitions.html#Claim.supportingInfo.valueString)" : "<[string](datatypes.html#string)>",
 "[valueQuantity](claim-definitions.html#Claim.supportingInfo.valueQuantity)" : { [Quantity](datatypes.html#Quantity) },
 "[valueAttachment](claim-definitions.html#Claim.supportingInfo.valueAttachment)" : { [Attachment](datatypes.html#Attachment) },
 "[valueReference](claim-definitions.html#Claim.supportingInfo.valueReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) },
 "[reason](claim-definitions.html#Claim.supportingInfo.reason)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Explanation for the information](valueset-missing-tooth-reason.html)
 }],
 "[diagnosis](claim-definitions.html#Claim.diagnosis)" : [{ // [Pertinent diagnosis information](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.diagnosis.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Diagnosis instance identifier](terminologies.html#unbound)
 // diagnosis[x]: Nature of illness or problem. One of these 2:
 "[diagnosisCodeableConcept](claim-definitions.html#Claim.diagnosis.diagnosisCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[diagnosisReference](claim-definitions.html#Claim.diagnosis.diagnosisReference)" : { [Reference](references.html#Reference)([Condition](condition.html#Condition)) },
 "[type](claim-definitions.html#Claim.diagnosis.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Timing or nature of the diagnosis](valueset-ex-diagnosistype.html)
 "[onAdmission](claim-definitions.html#Claim.diagnosis.onAdmission)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Present on admission](valueset-ex-diagnosis-on-admission.html)
 "[packageCode](claim-definitions.html#Claim.diagnosis.packageCode)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Package billing code](valueset-ex-diagnosisrelatedgroup.html)
 }],
 "[procedure](claim-definitions.html#Claim.procedure)" : [{ // [Clinical procedures performed](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.procedure.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Procedure instance identifier](terminologies.html#unbound)
 "[type](claim-definitions.html#Claim.procedure.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Category of Procedure](valueset-ex-procedure-type.html)
 "[date](claim-definitions.html#Claim.procedure.date)" : "<[dateTime](datatypes.html#dateTime)>", // [When the procedure was performed](terminologies.html#unbound)
 // procedure[x]: Specific clinical procedure. One of these 2:
 "[procedureCodeableConcept](claim-definitions.html#Claim.procedure.procedureCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[procedureReference](claim-definitions.html#Claim.procedure.procedureReference)" : { [Reference](references.html#Reference)([Procedure](procedure.html#Procedure)) },
 "[udi](claim-definitions.html#Claim.procedure.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }] // [Unique device identifier](terminologies.html#unbound)
 }],
 "[insurance](claim-definitions.html#Claim.insurance)" : [{ // **R!** [Patient insurance information](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.insurance.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Insurance instance identifier](terminologies.html#unbound)
 "[focal](claim-definitions.html#Claim.insurance.focal)" : <[boolean](datatypes.html#boolean)>, // **R!** [Coverage to be used for adjudication](terminologies.html#unbound)
 "[identifier](claim-definitions.html#Claim.insurance.identifier)" : { [Identifier](datatypes.html#Identifier) }, // [Pre-assigned Claim number](terminologies.html#unbound)
 "[coverage](claim-definitions.html#Claim.insurance.coverage)" : { [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) }, // **R!** [Insurance information](terminologies.html#unbound)
 "[businessArrangement](claim-definitions.html#Claim.insurance.businessArrangement)" : "<[string](datatypes.html#string)>", // [Additional provider contract number](terminologies.html#unbound)
 "[preAuthRef](claim-definitions.html#Claim.insurance.preAuthRef)" : ["<[string](datatypes.html#string)>"], // [Prior authorization reference number](terminologies.html#unbound)
 "[claimResponse](claim-definitions.html#Claim.insurance.claimResponse)" : { [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) } // [Adjudication results](terminologies.html#unbound)
 }],
 "[accident](claim-definitions.html#Claim.accident)" : { // [Details of the event](terminologies.html#unbound)
 "[date](claim-definitions.html#Claim.accident.date)" : "<[date](datatypes.html#date)>", // **R!** [When the incident occurred](terminologies.html#unbound)
 "[type](claim-definitions.html#Claim.accident.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The nature of the accident](v3/ActIncidentCode/vs.html)
 // location[x]: Where the event occurred. One of these 2:
 "[locationAddress](claim-definitions.html#Claim.accident.locationAddress)" : { [Address](datatypes.html#Address) }
 "[locationReference](claim-definitions.html#Claim.accident.locationReference)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }
 },
 "[item](claim-definitions.html#Claim.item)" : [{ // [Product or service provided](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.item.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Item instance identifier](terminologies.html#unbound)
 "[careTeamSequence](claim-definitions.html#Claim.item.careTeamSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable careTeam members](terminologies.html#unbound)
 "[diagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable diagnoses](terminologies.html#unbound)
 "[procedureSequence](claim-definitions.html#Claim.item.procedureSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable procedures](terminologies.html#unbound)
 "[informationSequence](claim-definitions.html#Claim.item.informationSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable exception and supporting information](terminologies.html#unbound)
 "[revenue](claim-definitions.html#Claim.item.revenue)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Revenue or cost center code](valueset-ex-revenue-center.html)
 "[category](claim-definitions.html#Claim.item.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Benefit classification](valueset-ex-benefitcategory.html)
 "[productOrService](claim-definitions.html#Claim.item.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claim-definitions.html#Claim.item.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Product or service billing modifiers](valueset-claim-modifiers.html)
 "[programCode](claim-definitions.html#Claim.item.programCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Program the product or service is provided under](valueset-ex-program-code.html)
 // serviced[x]: Date or dates of service or product delivery. One of these 2:
 "[servicedDate](claim-definitions.html#Claim.item.servicedDate)" : "<[date](datatypes.html#date)>",
 "[servicedPeriod](claim-definitions.html#Claim.item.servicedPeriod)" : { [Period](datatypes.html#Period) },
 // location[x]: Place of service or where product was supplied. One of these 3:
 "[locationCodeableConcept](claim-definitions.html#Claim.item.locationCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[locationAddress](claim-definitions.html#Claim.item.locationAddress)" : { [Address](datatypes.html#Address) },
 "[locationReference](claim-definitions.html#Claim.item.locationReference)" : { [Reference](references.html#Reference)([Location](location.html#Location)) },
 "[quantity](claim-definitions.html#Claim.item.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claim-definitions.html#Claim.item.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claim-definitions.html#Claim.item.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claim-definitions.html#Claim.item.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[udi](claim-definitions.html#Claim.item.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }], // [Unique device identifier](terminologies.html#unbound)
 "[bodySite](claim-definitions.html#Claim.item.bodySite)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Anatomical location](valueset-tooth.html)
 "[subSite](claim-definitions.html#Claim.item.subSite)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Anatomical sub-location](valueset-surface.html)
 "[encounter](claim-definitions.html#Claim.item.encounter)" : [{ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }], // [Encounters related to this billed item](terminologies.html#unbound)
 "[detail](claim-definitions.html#Claim.item.detail)" : [{ // [Product or service provided](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.item.detail.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Item instance identifier](terminologies.html#unbound)
 "[revenue](claim-definitions.html#Claim.item.detail.revenue)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Revenue or cost center code](valueset-ex-revenue-center.html)
 "[category](claim-definitions.html#Claim.item.detail.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Benefit classification](valueset-ex-benefitcategory.html)
 "[productOrService](claim-definitions.html#Claim.item.detail.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claim-definitions.html#Claim.item.detail.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Service/Product billing modifiers](valueset-claim-modifiers.html)
 "[programCode](claim-definitions.html#Claim.item.detail.programCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Program the product or service is provided under](valueset-ex-program-code.html)
 "[quantity](claim-definitions.html#Claim.item.detail.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claim-definitions.html#Claim.item.detail.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claim-definitions.html#Claim.item.detail.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claim-definitions.html#Claim.item.detail.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[udi](claim-definitions.html#Claim.item.detail.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }], // [Unique device identifier](terminologies.html#unbound)
 "[subDetail](claim-definitions.html#Claim.item.detail.subDetail)" : [{ // [Product or service provided](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.item.detail.subDetail.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Item instance identifier](terminologies.html#unbound)
 "[revenue](claim-definitions.html#Claim.item.detail.subDetail.revenue)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Revenue or cost center code](valueset-ex-revenue-center.html)
 "[category](claim-definitions.html#Claim.item.detail.subDetail.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Benefit classification](valueset-ex-benefitcategory.html)
 "[productOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claim-definitions.html#Claim.item.detail.subDetail.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Service/Product billing modifiers](valueset-claim-modifiers.html)
 "[programCode](claim-definitions.html#Claim.item.detail.subDetail.programCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Program the product or service is provided under](valueset-ex-program-code.html)
 "[quantity](claim-definitions.html#Claim.item.detail.subDetail.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claim-definitions.html#Claim.item.detail.subDetail.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claim-definitions.html#Claim.item.detail.subDetail.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[udi](claim-definitions.html#Claim.item.detail.subDetail.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }] // [Unique device identifier](terminologies.html#unbound)
 }]
 }]
 }],
 "[total](claim-definitions.html#Claim.total)" : { [Money](datatypes.html#Money) } // [Total claim cost](terminologies.html#unbound)
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Claim**](claim-definitions.html#Claim);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Claim.identifier](claim-definitions.html#Claim.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for claim
 fhir:[Claim.status](claim-definitions.html#Claim.status) [ [code](datatypes.html#code) ]; # 1..1 active | cancelled | draft | entered-in-error
 fhir:[Claim.type](claim-definitions.html#Claim.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Category or discipline
 fhir:[Claim.subType](claim-definitions.html#Claim.subType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 More granular claim type
 fhir:[Claim.use](claim-definitions.html#Claim.use) [ [code](datatypes.html#code) ]; # 1..1 claim | preauthorization | predetermination
 fhir:[Claim.patient](claim-definitions.html#Claim.patient) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 1..1 The recipient of the products and services
 fhir:[Claim.billablePeriod](claim-definitions.html#Claim.billablePeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Relevant time frame for the claim
 fhir:[Claim.created](claim-definitions.html#Claim.created) [ [dateTime](datatypes.html#dateTime) ]; # 1..1 Resource creation date
 fhir:[Claim.enterer](claim-definitions.html#Claim.enterer) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 Author of the claim
 fhir:[Claim.insurer](claim-definitions.html#Claim.insurer) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Target
 fhir:[Claim.provider](claim-definitions.html#Claim.provider) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 1..1 Party responsible for the claim
 fhir:[Claim.priority](claim-definitions.html#Claim.priority) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Desired processing ugency
 fhir:[Claim.fundsReserve](claim-definitions.html#Claim.fundsReserve) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 For whom to reserve funds
 fhir:[Claim.related](claim-definitions.html#Claim.related) [ # 0..* Prior or corollary claims
 fhir:[Claim.related.claim](claim-definitions.html#Claim.related.claim) [ [Reference](references.html#Reference)([Claim](claim.html#Claim)) ]; # 0..1 Reference to the related claim
 fhir:[Claim.related.relationship](claim-definitions.html#Claim.related.relationship) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 How the reference claim is related
 fhir:[Claim.related.reference](claim-definitions.html#Claim.related.reference) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 File or case reference
 ], ...;
 fhir:[Claim.prescription](claim-definitions.html#Claim.prescription) [ [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[VisionPrescription](visionprescription.html#VisionPrescription)) ]; # 0..1 Prescription authorizing services and products
 fhir:[Claim.originalPrescription](claim-definitions.html#Claim.originalPrescription) [ [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[VisionPrescription](visionprescription.html#VisionPrescription)) ]; # 0..1 Original prescription if superseded by fulfiller
 fhir:[Claim.payee](claim-definitions.html#Claim.payee) [ # 0..1 Recipient of benefits payable
 fhir:[Claim.payee.type](claim-definitions.html#Claim.payee.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Category of recipient
 fhir:[Claim.payee.party](claim-definitions.html#Claim.payee.party) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Recipient reference
 ];
 fhir:[Claim.referral](claim-definitions.html#Claim.referral) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ]; # 0..1 Treatment referral
 fhir:[Claim.facility](claim-definitions.html#Claim.facility) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 0..1 Servicing facility
 fhir:[Claim.careTeam](claim-definitions.html#Claim.careTeam) [ # 0..* Members of the care team
 fhir:[Claim.careTeam.sequence](claim-definitions.html#Claim.careTeam.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Order of care team
 fhir:[Claim.careTeam.provider](claim-definitions.html#Claim.careTeam.provider) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 1..1 Practitioner or organization
 fhir:[Claim.careTeam.responsible](claim-definitions.html#Claim.careTeam.responsible) [ [boolean](datatypes.html#boolean) ]; # 0..1 Indicator of the lead practitioner
 fhir:[Claim.careTeam.role](claim-definitions.html#Claim.careTeam.role) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Function within the team
 fhir:[Claim.careTeam.qualification](claim-definitions.html#Claim.careTeam.qualification) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Practitioner credential or specialization
 ], ...;
 fhir:[Claim.supportingInfo](claim-definitions.html#Claim.supportingInfo) [ # 0..* Supporting information
 fhir:[Claim.supportingInfo.sequence](claim-definitions.html#Claim.supportingInfo.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Information instance identifier
 fhir:[Claim.supportingInfo.category](claim-definitions.html#Claim.supportingInfo.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Classification of the supplied information
 fhir:[Claim.supportingInfo.code](claim-definitions.html#Claim.supportingInfo.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Type of information
 # [Claim.supportingInfo.timing[x]](claim-definitions.html#Claim.supportingInfo.timing[x]) : 0..1 When it occurred. One of these 2
 fhir:[Claim.supportingInfo.timingDate](claim-definitions.html#Claim.supportingInfo.timingDate) [ [date](datatypes.html#date) ]
 fhir:[Claim.supportingInfo.timingPeriod](claim-definitions.html#Claim.supportingInfo.timingPeriod) [ [Period](datatypes.html#Period) ]
 # [Claim.supportingInfo.value[x]](claim-definitions.html#Claim.supportingInfo.value[x]) : 0..1 Data to be provided. One of these 5
 fhir:[Claim.supportingInfo.valueBoolean](claim-definitions.html#Claim.supportingInfo.valueBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Claim.supportingInfo.valueString](claim-definitions.html#Claim.supportingInfo.valueString) [ [string](datatypes.html#string) ]
 fhir:[Claim.supportingInfo.valueQuantity](claim-definitions.html#Claim.supportingInfo.valueQuantity) [ [Quantity](datatypes.html#Quantity) ]
 fhir:[Claim.supportingInfo.valueAttachment](claim-definitions.html#Claim.supportingInfo.valueAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Claim.supportingInfo.valueReference](claim-definitions.html#Claim.supportingInfo.valueReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]
 fhir:[Claim.supportingInfo.reason](claim-definitions.html#Claim.supportingInfo.reason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Explanation for the information
 ], ...;
 fhir:[Claim.diagnosis](claim-definitions.html#Claim.diagnosis) [ # 0..* Pertinent diagnosis information
 fhir:[Claim.diagnosis.sequence](claim-definitions.html#Claim.diagnosis.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Diagnosis instance identifier
 # [Claim.diagnosis.diagnosis[x]](claim-definitions.html#Claim.diagnosis.diagnosis[x]) : 1..1 Nature of illness or problem. One of these 2
 fhir:[Claim.diagnosis.diagnosisCodeableConcept](claim-definitions.html#Claim.diagnosis.diagnosisCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Claim.diagnosis.diagnosisReference](claim-definitions.html#Claim.diagnosis.diagnosisReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)) ]
 fhir:[Claim.diagnosis.type](claim-definitions.html#Claim.diagnosis.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Timing or nature of the diagnosis
 fhir:[Claim.diagnosis.onAdmission](claim-definitions.html#Claim.diagnosis.onAdmission) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Present on admission
 fhir:[Claim.diagnosis.packageCode](claim-definitions.html#Claim.diagnosis.packageCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Package billing code
 ], ...;
 fhir:[Claim.procedure](claim-definitions.html#Claim.procedure) [ # 0..* Clinical procedures performed
 fhir:[Claim.procedure.sequence](claim-definitions.html#Claim.procedure.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Procedure instance identifier
 fhir:[Claim.procedure.type](claim-definitions.html#Claim.procedure.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Category of Procedure
 fhir:[Claim.procedure.date](claim-definitions.html#Claim.procedure.date) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the procedure was performed
 # [Claim.procedure.procedure[x]](claim-definitions.html#Claim.procedure.procedure[x]) : 1..1 Specific clinical procedure. One of these 2
 fhir:[Claim.procedure.procedureCodeableConcept](claim-definitions.html#Claim.procedure.procedureCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Claim.procedure.procedureReference](claim-definitions.html#Claim.procedure.procedureReference) [ [Reference](references.html#Reference)([Procedure](procedure.html#Procedure)) ]
 fhir:[Claim.procedure.udi](claim-definitions.html#Claim.procedure.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 ], ...;
 fhir:[Claim.insurance](claim-definitions.html#Claim.insurance) [ # 1..* Patient insurance information
 fhir:[Claim.insurance.sequence](claim-definitions.html#Claim.insurance.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Insurance instance identifier
 fhir:[Claim.insurance.focal](claim-definitions.html#Claim.insurance.focal) [ [boolean](datatypes.html#boolean) ]; # 1..1 Coverage to be used for adjudication
 fhir:[Claim.insurance.identifier](claim-definitions.html#Claim.insurance.identifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Pre-assigned Claim number
 fhir:[Claim.insurance.coverage](claim-definitions.html#Claim.insurance.coverage) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) ]; # 1..1 Insurance information
 fhir:[Claim.insurance.businessArrangement](claim-definitions.html#Claim.insurance.businessArrangement) [ [string](datatypes.html#string) ]; # 0..1 Additional provider contract number
 fhir:[Claim.insurance.preAuthRef](claim-definitions.html#Claim.insurance.preAuthRef) [ [string](datatypes.html#string) ], ... ; # 0..* Prior authorization reference number
 fhir:[Claim.insurance.claimResponse](claim-definitions.html#Claim.insurance.claimResponse) [ [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) ]; # 0..1 Adjudication results
 ], ...;
 fhir:[Claim.accident](claim-definitions.html#Claim.accident) [ # 0..1 Details of the event
 fhir:[Claim.accident.date](claim-definitions.html#Claim.accident.date) [ [date](datatypes.html#date) ]; # 1..1 When the incident occurred
 fhir:[Claim.accident.type](claim-definitions.html#Claim.accident.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The nature of the accident
 # [Claim.accident.location[x]](claim-definitions.html#Claim.accident.location[x]) : 0..1 Where the event occurred. One of these 2
 fhir:[Claim.accident.locationAddress](claim-definitions.html#Claim.accident.locationAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Claim.accident.locationReference](claim-definitions.html#Claim.accident.locationReference) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]
 ];
 fhir:[Claim.item](claim-definitions.html#Claim.item) [ # 0..* Product or service provided
 fhir:[Claim.item.sequence](claim-definitions.html#Claim.item.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Item instance identifier
 fhir:[Claim.item.careTeamSequence](claim-definitions.html#Claim.item.careTeamSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable careTeam members
 fhir:[Claim.item.diagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable diagnoses
 fhir:[Claim.item.procedureSequence](claim-definitions.html#Claim.item.procedureSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable procedures
 fhir:[Claim.item.informationSequence](claim-definitions.html#Claim.item.informationSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable exception and supporting information
 fhir:[Claim.item.revenue](claim-definitions.html#Claim.item.revenue) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Revenue or cost center code
 fhir:[Claim.item.category](claim-definitions.html#Claim.item.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Benefit classification
 fhir:[Claim.item.productOrService](claim-definitions.html#Claim.item.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[Claim.item.modifier](claim-definitions.html#Claim.item.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Product or service billing modifiers
 fhir:[Claim.item.programCode](claim-definitions.html#Claim.item.programCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Program the product or service is provided under
 # [Claim.item.serviced[x]](claim-definitions.html#Claim.item.serviced[x]) : 0..1 Date or dates of service or product delivery. One of these 2
 fhir:[Claim.item.servicedDate](claim-definitions.html#Claim.item.servicedDate) [ [date](datatypes.html#date) ]
 fhir:[Claim.item.servicedPeriod](claim-definitions.html#Claim.item.servicedPeriod) [ [Period](datatypes.html#Period) ]
 # [Claim.item.location[x]](claim-definitions.html#Claim.item.location[x]) : 0..1 Place of service or where product was supplied. One of these 3
 fhir:[Claim.item.locationCodeableConcept](claim-definitions.html#Claim.item.locationCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Claim.item.locationAddress](claim-definitions.html#Claim.item.locationAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Claim.item.locationReference](claim-definitions.html#Claim.item.locationReference) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]
 fhir:[Claim.item.quantity](claim-definitions.html#Claim.item.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[Claim.item.unitPrice](claim-definitions.html#Claim.item.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[Claim.item.factor](claim-definitions.html#Claim.item.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[Claim.item.net](claim-definitions.html#Claim.item.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[Claim.item.udi](claim-definitions.html#Claim.item.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 fhir:[Claim.item.bodySite](claim-definitions.html#Claim.item.bodySite) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Anatomical location
 fhir:[Claim.item.subSite](claim-definitions.html#Claim.item.subSite) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Anatomical sub-location
 fhir:[Claim.item.encounter](claim-definitions.html#Claim.item.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ], ... ; # 0..* Encounters related to this billed item
 fhir:[Claim.item.detail](claim-definitions.html#Claim.item.detail) [ # 0..* Product or service provided
 fhir:[Claim.item.detail.sequence](claim-definitions.html#Claim.item.detail.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Item instance identifier
 fhir:[Claim.item.detail.revenue](claim-definitions.html#Claim.item.detail.revenue) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Revenue or cost center code
 fhir:[Claim.item.detail.category](claim-definitions.html#Claim.item.detail.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Benefit classification
 fhir:[Claim.item.detail.productOrService](claim-definitions.html#Claim.item.detail.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[Claim.item.detail.modifier](claim-definitions.html#Claim.item.detail.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Service/Product billing modifiers
 fhir:[Claim.item.detail.programCode](claim-definitions.html#Claim.item.detail.programCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Program the product or service is provided under
 fhir:[Claim.item.detail.quantity](claim-definitions.html#Claim.item.detail.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[Claim.item.detail.unitPrice](claim-definitions.html#Claim.item.detail.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[Claim.item.detail.factor](claim-definitions.html#Claim.item.detail.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[Claim.item.detail.net](claim-definitions.html#Claim.item.detail.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[Claim.item.detail.udi](claim-definitions.html#Claim.item.detail.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 fhir:[Claim.item.detail.subDetail](claim-definitions.html#Claim.item.detail.subDetail) [ # 0..* Product or service provided
 fhir:[Claim.item.detail.subDetail.sequence](claim-definitions.html#Claim.item.detail.subDetail.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Item instance identifier
 fhir:[Claim.item.detail.subDetail.revenue](claim-definitions.html#Claim.item.detail.subDetail.revenue) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Revenue or cost center code
 fhir:[Claim.item.detail.subDetail.category](claim-definitions.html#Claim.item.detail.subDetail.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Benefit classification
 fhir:[Claim.item.detail.subDetail.productOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[Claim.item.detail.subDetail.modifier](claim-definitions.html#Claim.item.detail.subDetail.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Service/Product billing modifiers
 fhir:[Claim.item.detail.subDetail.programCode](claim-definitions.html#Claim.item.detail.subDetail.programCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Program the product or service is provided under
 fhir:[Claim.item.detail.subDetail.quantity](claim-definitions.html#Claim.item.detail.subDetail.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[Claim.item.detail.subDetail.unitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[Claim.item.detail.subDetail.factor](claim-definitions.html#Claim.item.detail.subDetail.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[Claim.item.detail.subDetail.net](claim-definitions.html#Claim.item.detail.subDetail.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[Claim.item.detail.subDetail.udi](claim-definitions.html#Claim.item.detail.subDetail.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 ], ...;
 ], ...;
 ], ...;
 fhir:[Claim.total](claim-definitions.html#Claim.total) [ [Money](datatypes.html#Money) ]; # 0..1 Total claim cost
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Claim](claim.html#Claim)
 | 
 | 
 |

 | 
 Claim.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/fm-status to http://hl7.org/fhir/ValueSet/fm-status|4.0.1

 

 | 
 |

 | 
 Claim.type | 
 
 

 - Min Cardinality changed from 0 to 1

 - Change binding strength from required to extensible

 

 | 
 |

 | 
 Claim.subType | 
 
 

 - Max Cardinality changed from * to 1

 

 | 
 |

 | 
 Claim.use | 
 
 

 - Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/claim-use to http://hl7.org/fhir/ValueSet/claim-use|4.0.1

 

 | 
 |

 | 
 Claim.patient | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.created | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.enterer | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Claim.provider | 
 
 

 - Min Cardinality changed from 0 to 1

 - Type Reference: Added Target Types PractitionerRole, Organization

 

 | 
 |

 | 
 Claim.priority | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.prescription | 
 
 

 - Type Reference: Added Target Type DeviceRequest

 

 | 
 |

 | 
 Claim.originalPrescription | 
 
 

 - Type Reference: Added Target Types DeviceRequest, VisionPrescription

 

 | 
 |

 | 
 Claim.payee.party | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Claim.referral | 
 
 

 - Type Reference: Added Target Type ServiceRequest

 - Type Reference: Removed Target Type ReferralRequest

 

 | 
 |

 | 
 Claim.careTeam.provider | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Claim.supportingInfo | 
 
 

 - Renamed from information to supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.sequence | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.category | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.code | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.timing[x] | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.value[x] | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 - Add Type boolean

 

 | 
 |

 | 
 Claim.supportingInfo.reason | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.diagnosis.onAdmission | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.procedure.type | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.procedure.udi | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.insurance | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.insurance.identifier | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.accident.type | 
 
 

 - Change binding strength from required to extensible

 

 | 
 |

 | 
 Claim.item.careTeamSequence | 
 
 

 - Renamed from careTeamLinkId to careTeamSequence

 

 | 
 |

 | 
 Claim.item.diagnosisSequence | 
 
 

 - Renamed from diagnosisLinkId to diagnosisSequence

 

 | 
 |

 | 
 Claim.item.procedureSequence | 
 
 

 - Renamed from procedureLinkId to procedureSequence

 

 | 
 |

 | 
 Claim.item.informationSequence | 
 
 

 - Renamed from informationLinkId to informationSequence

 

 | 
 |

 | 
 Claim.item.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.item.detail.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.item.detail.subDetail.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.organization | 
 
 

 - deleted

 

 | 
 |

 | 
 Claim.payee.resourceType | 
 
 

 - deleted

 

 | 
 |

 | 
 Claim.employmentImpacted | 
 
 

 - deleted

 

 | 
 |

 | 
 Claim.hospitalization | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](claim.diff.xml) or [JSON](claim.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](claim-version-maps.html) (status = 16 tests of which 3 fail to execute. 13 fail round-trip testing and 3 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Claim](claim-definitions.html#Claim) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Claim, Pre-determination or Pre-authorization**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](claim-definitions.html#Claim.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for claim
 | |

| [status](claim-definitions.html#Claim.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | cancelled | draft | entered-in-error
[Financial Resource Status Codes](valueset-fm-status.html) ([Required](terminologies.html#required)) | |

| [type](claim-definitions.html#Claim.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category or discipline
[Claim Type Codes](valueset-claim-type.html) ([Extensible](terminologies.html#extensible)) | |

| [subType](claim-definitions.html#Claim.subType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | More granular claim type
[Example Claim SubType Codes](valueset-claim-subtype.html) ([Example](terminologies.html#example)) | |

| [use](claim-definitions.html#Claim.use) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | claim | preauthorization | predetermination
[Use](valueset-claim-use.html) ([Required](terminologies.html#required)) | |

| [patient](claim-definitions.html#Claim.patient) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | The recipient of the products and services | |

| [billablePeriod](claim-definitions.html#Claim.billablePeriod) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Relevant time frame for the claim | |

| [created](claim-definitions.html#Claim.created) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [dateTime](datatypes.html#dateTime) | Resource creation date | |

| [enterer](claim-definitions.html#Claim.enterer) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html)) | Author of the claim | |

| [insurer](claim-definitions.html#Claim.insurer) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Target | |

| [provider](claim-definitions.html#Claim.provider) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Party responsible for the claim | |

| [priority](claim-definitions.html#Claim.priority) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Desired processing ugency
[Process Priority Codes](valueset-process-priority.html) ([Example](terminologies.html#example)) | |

| [fundsReserve](claim-definitions.html#Claim.fundsReserve) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | For whom to reserve funds
[FundsReserve](valueset-fundsreserve.html) ([Example](terminologies.html#example)) | |

| [related](claim-definitions.html#Claim.related) | | 0..* | [BackboneElement](backboneelement.html) | Prior or corollary claims
 | |

| [claim](claim-definitions.html#Claim.related.claim) | | 0..1 | [Reference](references.html#Reference)([Claim](claim.html)) | Reference to the related claim | |

| [relationship](claim-definitions.html#Claim.related.relationship) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How the reference claim is related
[Example Related Claim Relationship Codes](valueset-related-claim-relationship.html) ([Example](terminologies.html#example)) | |

| [reference](claim-definitions.html#Claim.related.reference) | | 0..1 | [Identifier](datatypes.html#Identifier) | File or case reference | |

| [prescription](claim-definitions.html#Claim.prescription) | | 0..1 | [Reference](references.html#Reference)([DeviceRequest](devicerequest.html) | [MedicationRequest](medicationrequest.html) | [VisionPrescription](visionprescription.html)) | Prescription authorizing services and products | |

| [originalPrescription](claim-definitions.html#Claim.originalPrescription) | | 0..1 | [Reference](references.html#Reference)([DeviceRequest](devicerequest.html) | [MedicationRequest](medicationrequest.html) | [VisionPrescription](visionprescription.html)) | Original prescription if superseded by fulfiller | |

| [payee](claim-definitions.html#Claim.payee) | | 0..1 | [BackboneElement](backboneelement.html) | Recipient of benefits payable | |

| [type](claim-definitions.html#Claim.payee.type) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Category of recipient
[PayeeType](valueset-payeetype.html) ([Example](terminologies.html#example)) | |

| [party](claim-definitions.html#Claim.payee.party) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Recipient reference | |

| [referral](claim-definitions.html#Claim.referral) | | 0..1 | [Reference](references.html#Reference)([ServiceRequest](servicerequest.html)) | Treatment referral | |

| [facility](claim-definitions.html#Claim.facility) | | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Servicing facility | |

| [careTeam](claim-definitions.html#Claim.careTeam) | | 0..* | [BackboneElement](backboneelement.html) | Members of the care team
 | |

| [sequence](claim-definitions.html#Claim.careTeam.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Order of care team | |

| [provider](claim-definitions.html#Claim.careTeam.provider) | | 1..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Practitioner or organization | |

| [responsible](claim-definitions.html#Claim.careTeam.responsible) | | 0..1 | [boolean](datatypes.html#boolean) | Indicator of the lead practitioner | |

| [role](claim-definitions.html#Claim.careTeam.role) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Function within the team
[Claim Care Team Role Codes](valueset-claim-careteamrole.html) ([Example](terminologies.html#example)) | |

| [qualification](claim-definitions.html#Claim.careTeam.qualification) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Practitioner credential or specialization
[Example Provider Qualification Codes](valueset-provider-qualification.html) ([Example](terminologies.html#example)) | |

| [supportingInfo](claim-definitions.html#Claim.supportingInfo) | | 0..* | [BackboneElement](backboneelement.html) | Supporting information
 | |

| [sequence](claim-definitions.html#Claim.supportingInfo.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Information instance identifier | |

| [category](claim-definitions.html#Claim.supportingInfo.category) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of the supplied information
[Claim Information Category Codes](valueset-claim-informationcategory.html) ([Example](terminologies.html#example)) | |

| [code](claim-definitions.html#Claim.supportingInfo.code) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of information
[Exception Codes](valueset-claim-exception.html) ([Example](terminologies.html#example)) | |

| [timing[x]](claim-definitions.html#Claim.supportingInfo.timing_x_) | | 0..1 | | When it occurred | |

| timingDate | | | [date](datatypes.html#date) | | |

| timingPeriod | | | [Period](datatypes.html#Period) | | |

| [value[x]](claim-definitions.html#Claim.supportingInfo.value_x_) | | 0..1 | | Data to be provided | |

| valueBoolean | | | [boolean](datatypes.html#boolean) | | |

| valueString | | | [string](datatypes.html#string) | | |

| valueQuantity | | | [Quantity](datatypes.html#Quantity) | | |

| valueAttachment | | | [Attachment](datatypes.html#Attachment) | | |

| valueReference | | | [Reference](references.html#Reference)([Any](resourcelist.html)) | | |

| [reason](claim-definitions.html#Claim.supportingInfo.reason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Explanation for the information
[Missing Tooth Reason Codes](valueset-missing-tooth-reason.html) ([Example](terminologies.html#example)) | |

| [diagnosis](claim-definitions.html#Claim.diagnosis) | | 0..* | [BackboneElement](backboneelement.html) | Pertinent diagnosis information
 | |

| [sequence](claim-definitions.html#Claim.diagnosis.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Diagnosis instance identifier | |

| [diagnosis[x]](claim-definitions.html#Claim.diagnosis.diagnosis_x_) | | 1..1 | | Nature of illness or problem
[ICD-10 Codes](valueset-icd-10.html) ([Example](terminologies.html#example)) | |

| diagnosisCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| diagnosisReference | | | [Reference](references.html#Reference)([Condition](condition.html)) | | |

| [type](claim-definitions.html#Claim.diagnosis.type) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Timing or nature of the diagnosis
[Example Diagnosis Type Codes](valueset-ex-diagnosistype.html) ([Example](terminologies.html#example))
 | |

| [onAdmission](claim-definitions.html#Claim.diagnosis.onAdmission) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Present on admission
[Example Diagnosis on Admission Codes](valueset-ex-diagnosis-on-admission.html) ([Example](terminologies.html#example)) | |

| [packageCode](claim-definitions.html#Claim.diagnosis.packageCode) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Package billing code
[Example Diagnosis Related Group Codes](valueset-ex-diagnosisrelatedgroup.html) ([Example](terminologies.html#example)) | |

| [procedure](claim-definitions.html#Claim.procedure) | | 0..* | [BackboneElement](backboneelement.html) | Clinical procedures performed
 | |

| [sequence](claim-definitions.html#Claim.procedure.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Procedure instance identifier | |

| [type](claim-definitions.html#Claim.procedure.type) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Category of Procedure
[Example Procedure Type Codes](valueset-ex-procedure-type.html) ([Example](terminologies.html#example))
 | |

| [date](claim-definitions.html#Claim.procedure.date) | | 0..1 | [dateTime](datatypes.html#dateTime) | When the procedure was performed | |

| [procedure[x]](claim-definitions.html#Claim.procedure.procedure_x_) | | 1..1 | | Specific clinical procedure
[ICD-10 Procedure Codes](valueset-icd-10-procedures.html) ([Example](terminologies.html#example)) | |

| procedureCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| procedureReference | | | [Reference](references.html#Reference)([Procedure](procedure.html)) | | |

| [udi](claim-definitions.html#Claim.procedure.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [insurance](claim-definitions.html#Claim.insurance) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..* | [BackboneElement](backboneelement.html) | Patient insurance information
 | |

| [sequence](claim-definitions.html#Claim.insurance.sequence) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [positiveInt](datatypes.html#positiveInt) | Insurance instance identifier | |

| [focal](claim-definitions.html#Claim.insurance.focal) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [boolean](datatypes.html#boolean) | Coverage to be used for adjudication | |

| [identifier](claim-definitions.html#Claim.insurance.identifier) | | 0..1 | [Identifier](datatypes.html#Identifier) | Pre-assigned Claim number | |

| [coverage](claim-definitions.html#Claim.insurance.coverage) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Coverage](coverage.html)) | Insurance information | |

| [businessArrangement](claim-definitions.html#Claim.insurance.businessArrangement) | | 0..1 | [string](datatypes.html#string) | Additional provider contract number | |

| [preAuthRef](claim-definitions.html#Claim.insurance.preAuthRef) | | 0..* | [string](datatypes.html#string) | Prior authorization reference number
 | |

| [claimResponse](claim-definitions.html#Claim.insurance.claimResponse) | | 0..1 | [Reference](references.html#Reference)([ClaimResponse](claimresponse.html)) | Adjudication results | |

| [accident](claim-definitions.html#Claim.accident) | | 0..1 | [BackboneElement](backboneelement.html) | Details of the event | |

| [date](claim-definitions.html#Claim.accident.date) | | 1..1 | [date](datatypes.html#date) | When the incident occurred | |

| [type](claim-definitions.html#Claim.accident.type) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The nature of the accident
[V3 Value SetActIncidentCode](v3/ActIncidentCode/vs.html) ([Extensible](terminologies.html#extensible)) | |

| [location[x]](claim-definitions.html#Claim.accident.location_x_) | | 0..1 | | Where the event occurred | |

| locationAddress | | | [Address](datatypes.html#Address) | | |

| locationReference | | | [Reference](references.html#Reference)([Location](location.html)) | | |

| [item](claim-definitions.html#Claim.item) | | 0..* | [BackboneElement](backboneelement.html) | Product or service provided
 | |

| [sequence](claim-definitions.html#Claim.item.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Item instance identifier | |

| [careTeamSequence](claim-definitions.html#Claim.item.careTeamSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable careTeam members
 | |

| [diagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable diagnoses
 | |

| [procedureSequence](claim-definitions.html#Claim.item.procedureSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable procedures
 | |

| [informationSequence](claim-definitions.html#Claim.item.informationSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable exception and supporting information
 | |

| [revenue](claim-definitions.html#Claim.item.revenue) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Revenue or cost center code
[Example Revenue Center Codes](valueset-ex-revenue-center.html) ([Example](terminologies.html#example)) | |

| [category](claim-definitions.html#Claim.item.category) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Benefit classification
[Benefit Category Codes](valueset-ex-benefitcategory.html) ([Example](terminologies.html#example)) | |

| [productOrService](claim-definitions.html#Claim.item.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claim-definitions.html#Claim.item.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Product or service billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [programCode](claim-definitions.html#Claim.item.programCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Program the product or service is provided under
[Example Program Reason Codes](valueset-ex-program-code.html) ([Example](terminologies.html#example))
 | |

| [serviced[x]](claim-definitions.html#Claim.item.serviced_x_) | | 0..1 | | Date or dates of service or product delivery | |

| servicedDate | | | [date](datatypes.html#date) | | |

| servicedPeriod | | | [Period](datatypes.html#Period) | | |

| [location[x]](claim-definitions.html#Claim.item.location_x_) | | 0..1 | | Place of service or where product was supplied
[Example Service Place Codes](valueset-service-place.html) ([Example](terminologies.html#example)) | |

| locationCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| locationAddress | | | [Address](datatypes.html#Address) | | |

| locationReference | | | [Reference](references.html#Reference)([Location](location.html)) | | |

| [quantity](claim-definitions.html#Claim.item.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claim-definitions.html#Claim.item.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claim-definitions.html#Claim.item.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claim-definitions.html#Claim.item.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [udi](claim-definitions.html#Claim.item.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [bodySite](claim-definitions.html#Claim.item.bodySite) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location
[Oral Site Codes](valueset-tooth.html) ([Example](terminologies.html#example)) | |

| [subSite](claim-definitions.html#Claim.item.subSite) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical sub-location
[Surface Codes](valueset-surface.html) ([Example](terminologies.html#example))
 | |

| [encounter](claim-definitions.html#Claim.item.encounter) | | 0..* | [Reference](references.html#Reference)([Encounter](encounter.html)) | Encounters related to this billed item
 | |

| [detail](claim-definitions.html#Claim.item.detail) | | 0..* | [BackboneElement](backboneelement.html) | Product or service provided
 | |

| [sequence](claim-definitions.html#Claim.item.detail.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Item instance identifier | |

| [revenue](claim-definitions.html#Claim.item.detail.revenue) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Revenue or cost center code
[Example Revenue Center Codes](valueset-ex-revenue-center.html) ([Example](terminologies.html#example)) | |

| [category](claim-definitions.html#Claim.item.detail.category) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Benefit classification
[Benefit Category Codes](valueset-ex-benefitcategory.html) ([Example](terminologies.html#example)) | |

| [productOrService](claim-definitions.html#Claim.item.detail.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claim-definitions.html#Claim.item.detail.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Service/Product billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [programCode](claim-definitions.html#Claim.item.detail.programCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Program the product or service is provided under
[Example Program Reason Codes](valueset-ex-program-code.html) ([Example](terminologies.html#example))
 | |

| [quantity](claim-definitions.html#Claim.item.detail.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claim-definitions.html#Claim.item.detail.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claim-definitions.html#Claim.item.detail.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claim-definitions.html#Claim.item.detail.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [udi](claim-definitions.html#Claim.item.detail.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [subDetail](claim-definitions.html#Claim.item.detail.subDetail) | | 0..* | [BackboneElement](backboneelement.html) | Product or service provided
 | |

| [sequence](claim-definitions.html#Claim.item.detail.subDetail.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Item instance identifier | |

| [revenue](claim-definitions.html#Claim.item.detail.subDetail.revenue) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Revenue or cost center code
[Example Revenue Center Codes](valueset-ex-revenue-center.html) ([Example](terminologies.html#example)) | |

| [category](claim-definitions.html#Claim.item.detail.subDetail.category) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Benefit classification
[Benefit Category Codes](valueset-ex-benefitcategory.html) ([Example](terminologies.html#example)) | |

| [productOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claim-definitions.html#Claim.item.detail.subDetail.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Service/Product billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [programCode](claim-definitions.html#Claim.item.detail.subDetail.programCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Program the product or service is provided under
[Example Program Reason Codes](valueset-ex-program-code.html) ([Example](terminologies.html#example))
 | |

| [quantity](claim-definitions.html#Claim.item.detail.subDetail.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claim-definitions.html#Claim.item.detail.subDetail.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claim-definitions.html#Claim.item.detail.subDetail.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [udi](claim-definitions.html#Claim.item.detail.subDetail.udi) | | 0..* | [Reference](references.html#Reference)([Device](device.html)) | Unique device identifier
 | |

| [total](claim-definitions.html#Claim.total) | | 0..1 | [Money](datatypes.html#Money) | Total claim cost | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Claim ([DomainResource](domainresource.html))[A unique identifier assigned to this claimidentifier](claim-definitions.html#Claim.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The status of the resource instance (this element modifies the meaning of other elements)status](claim-definitions.html#Claim.status) : [code](datatypes.html#code) [1..1] « [A code specifying the state of the resource instance. (Strength=Required)FinancialResourceStatusCodes](valueset-fm-status.html)! »[The category of claim, e.g. oral, pharmacy, vision, institutional, professionaltype](claim-definitions.html#Claim.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The type or discipline-style of the claim. (Strength=Extensible)ClaimTypeCodes](valueset-claim-type.html)+ »[A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty servicesubType](claim-definitions.html#Claim.subType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A more granular claim typecode. (Strength=Example)ExampleClaimSubTypeCodes](valueset-claim-subtype.html)?? »[A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the futureuse](claim-definitions.html#Claim.use) : [code](datatypes.html#code) [1..1] « [The purpose of the Claim: predetermination, preauthorization, claim. (Strength=Required)Use](valueset-claim-use.html)! »[The party to whom the professional services and/or products have been supplied or are being considered and for whom actual or forecast reimbursement is soughtpatient](claim-definitions.html#Claim.patient) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient) »[The period for which charges are being submittedbillablePeriod](claim-definitions.html#Claim.billablePeriod) : [Period](datatypes.html#Period) [0..1][The date this resource was createdcreated](claim-definitions.html#Claim.created) : [dateTime](datatypes.html#dateTime) [1..1][Individual who created the claim, predetermination or preauthorizationenterer](claim-definitions.html#Claim.enterer) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole) »[The Insurer who is target of the requestinsurer](claim-definitions.html#Claim.insurer) : [Reference](references.html#Reference) [0..1] « [Organization](organization.html#Organization) »[The provider which is responsible for the claim, predetermination or preauthorizationprovider](claim-definitions.html#Claim.provider) : [Reference](references.html#Reference) [1..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[The provider-required urgency of processing the request. Typical values include: stat, routine deferredpriority](claim-definitions.html#Claim.priority) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The timeliness with which processing is required: stat, normal, deferred. (Strength=Example)ProcessPriorityCodes](valueset-process-priority.html)?? »[A code to indicate whether and for whom funds are to be reserved for future claimsfundsReserve](claim-definitions.html#Claim.fundsReserve) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [For whom funds are to be reserved: (Patient, Provider, None). (Strength=Example)Funds Reservation ](valueset-fundsreserve.html)?? »[Prescription to support the dispensing of pharmacy, device or vision productsprescription](claim-definitions.html#Claim.prescription) : [Reference](references.html#Reference) [0..1] « [DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)| [VisionPrescription](visionprescription.html#VisionPrescription) »[Original prescription which has been superseded by this prescription to support the dispensing of pharmacy services, medications or productsoriginalPrescription](claim-definitions.html#Claim.originalPrescription) : [Reference](references.html#Reference) [0..1] « [DeviceRequest](devicerequest.html#DeviceRequest)| [MedicationRequest](medicationrequest.html#MedicationRequest)|[VisionPrescription](visionprescription.html#VisionPrescription) »[A reference to a referral resourcereferral](claim-definitions.html#Claim.referral) : [Reference](references.html#Reference) [0..1] « [ServiceRequest](servicerequest.html#ServiceRequest) »[Facility where the services were providedfacility](claim-definitions.html#Claim.facility) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location) »[The total value of the all the items in the claimtotal](claim-definitions.html#Claim.total) : [Money](datatypes.html#Money) [0..1]RelatedClaim[Reference to a related claimclaim](claim-definitions.html#Claim.related.claim) : [Reference](references.html#Reference) [0..1] « [Claim](claim.html#Claim) »[A code to convey how the claims are relatedrelationship](claim-definitions.html#Claim.related.relationship) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Relationship of this claim to a related Claim. (Strength=Example)](valueset-related-claim-relationship.html) [ExampleRelatedClaimRelationsh...](valueset-related-claim-relationship.html)?? »[An alternate organizational reference to the case or file to which this particular claim pertainsreference](claim-definitions.html#Claim.related.reference) : [Identifier](datatypes.html#Identifier) [0..1]Payee[Type of Party to be reimbursed: subscriber, provider, othertype](claim-definitions.html#Claim.payee.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [A code for the party to be reimbursed. (Strength=Example)Claim Payee Type ](valueset-payeetype.html)?? »[Reference to the individual or organization to whom any payment will be madeparty](claim-definitions.html#Claim.payee.party) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson) »CareTeam[A number to uniquely identify care team entriessequence](claim-definitions.html#Claim.careTeam.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][Member of the team who provided the product or serviceprovider](claim-definitions.html#Claim.careTeam.provider) : [Reference](references.html#Reference) [1..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[The party who is billing and/or responsible for the claimed products or servicesresponsible](claim-definitions.html#Claim.careTeam.responsible) : [boolean](datatypes.html#boolean) [0..1][The lead, assisting or supervising practitioner and their discipline if a multidisciplinary teamrole](claim-definitions.html#Claim.careTeam.role) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The role codes for the care team members. (Strength=Example)ClaimCareTeamRoleCodes](valueset-claim-careteamrole.html)?? »[The qualification of the practitioner which is applicable for this servicequalification](claim-definitions.html#Claim.careTeam.qualification) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Provider professional qualifications. (Strength=Example)](valueset-provider-qualification.html) [ExampleProviderQualificationC...](valueset-provider-qualification.html)?? »SupportingInformation[A number to uniquely identify supporting information entriessequence](claim-definitions.html#Claim.supportingInfo.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The general class of the information supplied: information; exception; accident, employment; onset, etccategory](claim-definitions.html#Claim.supportingInfo.category) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The valuset used for additional information category codes. (Strength=Example)ClaimInformationCategoryCodes](valueset-claim-informationcategory.html)?? »[System and code pertaining to the specific information regarding special conditions relating to the setting, treatment or patient for which care is soughtcode](claim-definitions.html#Claim.supportingInfo.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The valuset used for additional information codes. (Strength=Example)ExceptionCodes](valueset-claim-exception.html)?? »[The date when or period to which this information referstiming[x]](claim-definitions.html#Claim.supportingInfo.timing_x_) : [Type](formats.html#umlchoice) [0..1] « [date](datatypes.html#date)|[Period](datatypes.html#Period) »[Additional data or information such as resources, documents, images etc. including references to the data or the actual inclusion of the datavalue[x]](claim-definitions.html#Claim.supportingInfo.value_x_) : [Type](formats.html#umlchoice) [0..1] « [boolean](datatypes.html#boolean)|[string](datatypes.html#string)|[Quantity](datatypes.html#Quantity)|[Attachment](datatypes.html#Attachment)| [Reference](references.html#Reference)([Any](resourcelist.html#Any)) »[Provides the reason in the situation where a reason code is required in addition to the contentreason](claim-definitions.html#Claim.supportingInfo.reason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Reason codes for the missing teeth. (Strength=Example)MissingToothReasonCodes](valueset-missing-tooth-reason.html)?? »Diagnosis[A number to uniquely identify diagnosis entriessequence](claim-definitions.html#Claim.diagnosis.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The nature of illness or problem in a coded form or as a reference to an external defined Conditiondiagnosis[x]](claim-definitions.html#Claim.diagnosis.diagnosis_x_) : [Type](formats.html#umlchoice) [1..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Condition](condition.html#Condition)); [Example ICD10 Diagnostic codes. (Strength=Example)](valueset-icd-10.html) [ICD-10Codes](valueset-icd-10.html)?? »[When the condition was observed or the relative rankingtype](claim-definitions.html#Claim.diagnosis.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The type of the diagnosis: admitting, principal, discharge. (Strength=Example)ExampleDiagnosisTypeCodes](valueset-ex-diagnosistype.html)?? »[Indication of whether the diagnosis was present on admission to a facilityonAdmission](claim-definitions.html#Claim.diagnosis.onAdmission) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Present on admission. (Strength=Example)](valueset-ex-diagnosis-on-admission.html) [ExampleDiagnosisOnAdmissionCo...](valueset-ex-diagnosis-on-admission.html)?? »[A package billing code or bundle code used to group products and services to a particular health condition (such as heart attack) which is based on a predetermined grouping code systempackageCode](claim-definitions.html#Claim.diagnosis.packageCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The DRG codes associated with the diagnosis. (Strength=Example)](valueset-ex-diagnosisrelatedgroup.html) [ExampleDiagnosisRelatedGroupC...](valueset-ex-diagnosisrelatedgroup.html)?? »Procedure[A number to uniquely identify procedure entriessequence](claim-definitions.html#Claim.procedure.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][When the condition was observed or the relative rankingtype](claim-definitions.html#Claim.procedure.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Example procedure type codes. (Strength=Example)ExampleProcedureTypeCodes](valueset-ex-procedure-type.html)?? »[Date and optionally time the procedure was performeddate](claim-definitions.html#Claim.procedure.date) : [dateTime](datatypes.html#dateTime) [0..1][The code or reference to a Procedure resource which identifies the clinical intervention performedprocedure[x]](claim-definitions.html#Claim.procedure.procedure_x_) : [Type](formats.html#umlchoice) [1..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Procedure](procedure.html#Procedure)); [Example ICD10 Procedure codes. (Strength=Example)](valueset-icd-10-procedures.html) [ICD-10ProcedureCodes](valueset-icd-10-procedures.html)?? »[Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.procedure.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »Insurance[A number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit ordersequence](claim-definitions.html#Claim.insurance.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][A flag to indicate that this Coverage is to be used for adjudication of this claim when set to truefocal](claim-definitions.html#Claim.insurance.focal) : [boolean](datatypes.html#boolean) [1..1][The business identifier to be used when the claim is sent for adjudication against this insurance policyidentifier](claim-definitions.html#Claim.insurance.identifier) : [Identifier](datatypes.html#Identifier) [0..1][Reference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information systemcoverage](claim-definitions.html#Claim.insurance.coverage) : [Reference](references.html#Reference) [1..1] « [Coverage](coverage.html#Coverage) »[A business agreement number established between the provider and the insurer for special business processing purposesbusinessArrangement](claim-definitions.html#Claim.insurance.businessArrangement) : [string](datatypes.html#string) [0..1][Reference numbers previously provided by the insurer to the provider to be quoted on subsequent claims containing services or products related to the prior authorizationpreAuthRef](claim-definitions.html#Claim.insurance.preAuthRef) : [string](datatypes.html#string) [0..*][The result of the adjudication of the line items for the Coverage specified in this insuranceclaimResponse](claim-definitions.html#Claim.insurance.claimResponse) : [Reference](references.html#Reference) [0..1] « [ClaimResponse](claimresponse.html#ClaimResponse) »Accident[Date of an accident event related to the products and services contained in the claimdate](claim-definitions.html#Claim.accident.date) : [date](datatypes.html#date) [1..1][The type or context of the accident event for the purposes of selection of potential insurance coverages and determination of coordination between insurerstype](claim-definitions.html#Claim.accident.type) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Type of accident: work place, auto, etc. (Strength=Extensible)v3.ActIncidentCode](v3/ActIncidentCode/vs.html)+ »[The physical location of the accident eventlocation[x]](claim-definitions.html#Claim.accident.location_x_) : [Type](formats.html#umlchoice) [0..1] « [Address](datatypes.html#Address)|[Reference](references.html#Reference)([Location](location.html#Location)) »Item[A number to uniquely identify item entriessequence](claim-definitions.html#Claim.item.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][CareTeam members related to this service or productcareTeamSequence](claim-definitions.html#Claim.item.careTeamSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][Diagnosis applicable for this service or productdiagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][Procedures applicable for this service or productprocedureSequence](claim-definitions.html#Claim.item.procedureSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][Exceptions, special conditions and supporting information applicable for this service or productinformationSequence](claim-definitions.html#Claim.item.informationSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][The type of revenue or cost center providing the product and/or servicerevenue](claim-definitions.html#Claim.item.revenue) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the revenue or cost centers supplying the service and/or products. (Strength=Example)ExampleRevenueCenterCodes](valueset-ex-revenue-center.html)?? »[Code to identify the general type of benefits under which products and services are providedcategory](claim-definitions.html#Claim.item.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Benefit categories such as: oral-basic, major, glasses. (Strength=Example)BenefitCategoryCodes](valueset-ex-benefitcategory.html)?? »[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claim-definitions.html#Claim.item.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claim-definitions.html#Claim.item.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[Identifies the program under which this may be recoveredprogramCode](claim-definitions.html#Claim.item.programCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Program specific reason codes. (Strength=Example)ExampleProgramReasonCodes](valueset-ex-program-code.html)?? »[The date or dates when the service or product was supplied, performed or completedserviced[x]](claim-definitions.html#Claim.item.serviced_x_) : [Type](formats.html#umlchoice) [0..1] « [date](datatypes.html#date)|[Period](datatypes.html#Period) »[Where the product or service was providedlocation[x]](claim-definitions.html#Claim.item.location_x_) : [Type](formats.html#umlchoice) [0..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Address](datatypes.html#Address)|[Reference](references.html#Reference)( [Location](location.html#Location)); [Place of service: pharmacy, school, prison, etc. (Strength=Example)ExampleServicePlaceCodes](valueset-service-place.html)?? »[The number of repetitions of a service or productquantity](claim-definitions.html#Claim.item.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claim-definitions.html#Claim.item.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claim-definitions.html#Claim.item.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claim-definitions.html#Claim.item.net) : [Money](datatypes.html#Money) [0..1][Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.item.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »[Physical service site on the patient (limb, tooth, etc.)bodySite](claim-definitions.html#Claim.item.bodySite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The code for the teeth, quadrant, sextant and arch. (Strength=Example)OralSiteCodes](valueset-tooth.html)?? »[A region or surface of the bodySite, e.g. limb region or tooth surface(s)subSite](claim-definitions.html#Claim.item.subSite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The code for the tooth surface and surface combinations. (Strength=Example)SurfaceCodes](valueset-surface.html)?? »[The Encounters during which this Claim was created or to which the creation of this record is tightly associatedencounter](claim-definitions.html#Claim.item.encounter) : [Reference](references.html#Reference) [0..*] « [Encounter](encounter.html#Encounter) »Detail[A number to uniquely identify item entriessequence](claim-definitions.html#Claim.item.detail.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The type of revenue or cost center providing the product and/or servicerevenue](claim-definitions.html#Claim.item.detail.revenue) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the revenue or cost centers supplying the service and/or products. (Strength=Example)ExampleRevenueCenterCodes](valueset-ex-revenue-center.html)?? »[Code to identify the general type of benefits under which products and services are providedcategory](claim-definitions.html#Claim.item.detail.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Benefit categories such as: oral-basic, major, glasses. (Strength=Example)BenefitCategoryCodes](valueset-ex-benefitcategory.html)?? »[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claim-definitions.html#Claim.item.detail.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claim-definitions.html#Claim.item.detail.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[Identifies the program under which this may be recoveredprogramCode](claim-definitions.html#Claim.item.detail.programCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Program specific reason codes. (Strength=Example)ExampleProgramReasonCodes](valueset-ex-program-code.html)?? »[The number of repetitions of a service or productquantity](claim-definitions.html#Claim.item.detail.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claim-definitions.html#Claim.item.detail.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claim-definitions.html#Claim.item.detail.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claim-definitions.html#Claim.item.detail.net) : [Money](datatypes.html#Money) [0..1][Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.item.detail.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »SubDetail[A number to uniquely identify item entriessequence](claim-definitions.html#Claim.item.detail.subDetail.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The type of revenue or cost center providing the product and/or servicerevenue](claim-definitions.html#Claim.item.detail.subDetail.revenue) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes for the revenue or cost centers supplying the service and/or products. (Strength=Example)ExampleRevenueCenterCodes](valueset-ex-revenue-center.html)?? »[Code to identify the general type of benefits under which products and services are providedcategory](claim-definitions.html#Claim.item.detail.subDetail.category) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Benefit categories such as: oral-basic, major, glasses. (Strength=Example)BenefitCategoryCodes](valueset-ex-benefitcategory.html)?? »[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claim-definitions.html#Claim.item.detail.subDetail.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[Identifies the program under which this may be recoveredprogramCode](claim-definitions.html#Claim.item.detail.subDetail.programCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Program specific reason codes. (Strength=Example)ExampleProgramReasonCodes](valueset-ex-program-code.html)?? »[The number of repetitions of a service or productquantity](claim-definitions.html#Claim.item.detail.subDetail.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claim-definitions.html#Claim.item.detail.subDetail.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claim-definitions.html#Claim.item.detail.subDetail.net) : [Money](datatypes.html#Money) [0..1][Unique Device Identifiers associated with this line itemudi](claim-definitions.html#Claim.item.detail.subDetail.udi) : [Reference](references.html#Reference) [0..*] « [Device](device.html#Device) »
[Other claims which are related to this claim such as prior submissions or claims for related services or for the same eventrelated](claim-definitions.html#Claim.related)[0..*][The party to be reimbursed for cost of the products and services according to the terms of the policypayee](claim-definitions.html#Claim.payee)[0..1][The members of the team who provided the products and servicescareTeam](claim-definitions.html#Claim.careTeam)[0..*][Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issuessupportingInfo](claim-definitions.html#Claim.supportingInfo)[0..*][Information about diagnoses relevant to the claim itemsdiagnosis](claim-definitions.html#Claim.diagnosis)[0..*][Procedures performed on the patient relevant to the billing items with the claimprocedure](claim-definitions.html#Claim.procedure)[0..*][Financial instruments for reimbursement for the health care products and services specified on the claiminsurance](claim-definitions.html#Claim.insurance)[1..*][Details of an accident which resulted in injuries which required the products and services listed in the claimaccident](claim-definitions.html#Claim.accident)[0..1][A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemssubDetail](claim-definitions.html#Claim.item.detail.subDetail)[0..*][A claim detail line. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsdetail](claim-definitions.html#Claim.item.detail)[0..*][A claim line. Either a simple product or service or a 'group' of details which can each be a simple items or groups of sub-detailsitem](claim-definitions.html#Claim.item)[0..*]
 

**XML Template**

 

 
```
<[**Claim**](claim-definitions.html#Claim) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](claim-definitions.html#Claim.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Business Identifier for claim](terminologies.html#unbound) --></identifier>
 <[**status**](claim-definitions.html#Claim.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [active | cancelled | draft | entered-in-error](valueset-fm-status.html) -->
 <[**type**](claim-definitions.html#Claim.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Category or discipline](valueset-claim-type.html) --></type>
 <[**subType**](claim-definitions.html#Claim.subType)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [More granular claim type](valueset-claim-subtype.html) --></subType>
 <[**use**](claim-definitions.html#Claim.use) value="[[code](datatypes.html#code)]"/><!-- **1..1** [claim | preauthorization | predetermination](valueset-claim-use.html) -->
 <[**patient**](claim-definitions.html#Claim.patient)><!-- **1..1** [Reference](references.html#Reference)([Patient](patient.html#Patient)) [The recipient of the products and services](terminologies.html#unbound) --></patient>
 <[**billablePeriod**](claim-definitions.html#Claim.billablePeriod)><!-- **0..1** [Period](datatypes.html#Period) [Relevant time frame for the claim](terminologies.html#unbound) --></billablePeriod>
 <[**created**](claim-definitions.html#Claim.created) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **1..1** [Resource creation date](terminologies.html#unbound) -->
 <[**enterer**](claim-definitions.html#Claim.enterer)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) [Author of the claim](terminologies.html#unbound) --></enterer>
 <[**insurer**](claim-definitions.html#Claim.insurer)><!-- **0..1** [Reference](references.html#Reference)([Organization](organization.html#Organization)) [Target](terminologies.html#unbound) --></insurer>
 <[**provider**](claim-definitions.html#Claim.provider)><!-- **1..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) [Party responsible for the claim](terminologies.html#unbound) --></provider>
 <[**priority**](claim-definitions.html#Claim.priority)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Desired processing ugency](valueset-process-priority.html) --></priority>
 <[**fundsReserve**](claim-definitions.html#Claim.fundsReserve)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [For whom to reserve funds](valueset-fundsreserve.html) --></fundsReserve>
 <[**related**](claim-definitions.html#Claim.related)> <!-- **0..*** Prior or corollary claims -->
 <[**claim**](claim-definitions.html#Claim.related.claim)><!-- **0..1** [Reference](references.html#Reference)([Claim](claim.html#Claim)) [Reference to the related claim](terminologies.html#unbound) --></claim>
 <[**relationship**](claim-definitions.html#Claim.related.relationship)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [How the reference claim is related](valueset-related-claim-relationship.html) --></relationship>
 <[**reference**](claim-definitions.html#Claim.related.reference)><!-- **0..1** [Identifier](datatypes.html#Identifier) [File or case reference](terminologies.html#unbound) --></reference>
 </related>
 <[**prescription**](claim-definitions.html#Claim.prescription)><!-- **0..1** [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) [Prescription authorizing services and products](terminologies.html#unbound) --></prescription>
 <[**originalPrescription**](claim-definitions.html#Claim.originalPrescription)><!-- **0..1** [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) [Original prescription if superseded by fulfiller](terminologies.html#unbound) --></originalPrescription>
 <[**payee**](claim-definitions.html#Claim.payee)> <!-- **0..1** Recipient of benefits payable -->
 <[**type**](claim-definitions.html#Claim.payee.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Category of recipient](valueset-payeetype.html) --></type>
 <[**party**](claim-definitions.html#Claim.payee.party)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)) [Recipient reference](terminologies.html#unbound) --></party>
 </payee>
 <[**referral**](claim-definitions.html#Claim.referral)><!-- **0..1** [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) [Treatment referral](terminologies.html#unbound) --></referral>
 <[**facility**](claim-definitions.html#Claim.facility)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)) [Servicing facility](terminologies.html#unbound) --></facility>
 <[**careTeam**](claim-definitions.html#Claim.careTeam)> <!-- **0..*** Members of the care team -->
 <[**sequence**](claim-definitions.html#Claim.careTeam.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Order of care team](terminologies.html#unbound) -->
 <[**provider**](claim-definitions.html#Claim.careTeam.provider)><!-- **1..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) [Practitioner or organization](terminologies.html#unbound) --></provider>
 <[**responsible**](claim-definitions.html#Claim.careTeam.responsible) value="[[boolean](datatypes.html#boolean)]"/><!-- **0..1** [Indicator of the lead practitioner](terminologies.html#unbound) -->
 <[**role**](claim-definitions.html#Claim.careTeam.role)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Function within the team](valueset-claim-careteamrole.html) --></role>
 <[**qualification**](claim-definitions.html#Claim.careTeam.qualification)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Practitioner credential or specialization](valueset-provider-qualification.html) --></qualification>
 </careTeam>
 <[**supportingInfo**](claim-definitions.html#Claim.supportingInfo)> <!-- **0..*** Supporting information -->
 <[**sequence**](claim-definitions.html#Claim.supportingInfo.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Information instance identifier](terminologies.html#unbound) -->
 <[**category**](claim-definitions.html#Claim.supportingInfo.category)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Classification of the supplied information](valueset-claim-informationcategory.html) --></category>
 <[**code**](claim-definitions.html#Claim.supportingInfo.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Type of information](valueset-claim-exception.html) --></code>
 <[**timing[x]**](claim-definitions.html#Claim.supportingInfo.timing[x])><!-- **0..1** [date](datatypes.html#date)|[Period](datatypes.html#Period) [When it occurred](terminologies.html#unbound) --></timing[x]>
 <[**value[x]**](claim-definitions.html#Claim.supportingInfo.value[x])><!-- **0..1** [boolean](datatypes.html#boolean)|[string](datatypes.html#string)|[Quantity](datatypes.html#Quantity)|[Attachment](datatypes.html#Attachment)|[Reference](references.html#Reference)([Any](resourcelist.html)) [Data to be provided](terminologies.html#unbound) --></value[x]>
 <[**reason**](claim-definitions.html#Claim.supportingInfo.reason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Explanation for the information](valueset-missing-tooth-reason.html) --></reason>
 </supportingInfo>
 <[**diagnosis**](claim-definitions.html#Claim.diagnosis)> <!-- **0..*** Pertinent diagnosis information -->
 <[**sequence**](claim-definitions.html#Claim.diagnosis.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Diagnosis instance identifier](terminologies.html#unbound) -->
 <[**diagnosis[x]**](claim-definitions.html#Claim.diagnosis.diagnosis[x])><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Condition](condition.html#Condition)) [Nature of illness or problem](valueset-icd-10.html) --></diagnosis[x]>
 <[**type**](claim-definitions.html#Claim.diagnosis.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Timing or nature of the diagnosis](valueset-ex-diagnosistype.html) --></type>
 <[**onAdmission**](claim-definitions.html#Claim.diagnosis.onAdmission)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Present on admission](valueset-ex-diagnosis-on-admission.html) --></onAdmission>
 <[**packageCode**](claim-definitions.html#Claim.diagnosis.packageCode)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Package billing code](valueset-ex-diagnosisrelatedgroup.html) --></packageCode>
 </diagnosis>
 <[**procedure**](claim-definitions.html#Claim.procedure)> <!-- **0..*** Clinical procedures performed -->
 <[**sequence**](claim-definitions.html#Claim.procedure.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Procedure instance identifier](terminologies.html#unbound) -->
 <[**type**](claim-definitions.html#Claim.procedure.type)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Category of Procedure](valueset-ex-procedure-type.html) --></type>
 <[**date**](claim-definitions.html#Claim.procedure.date) value="[[dateTime](datatypes.html#dateTime)]"/><!-- **0..1** [When the procedure was performed](terminologies.html#unbound) -->
 <[**procedure[x]**](claim-definitions.html#Claim.procedure.procedure[x])><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Reference](references.html#Reference)([Procedure](procedure.html#Procedure)) [Specific clinical procedure](valueset-icd-10-procedures.html) --></procedure[x]>
 <[**udi**](claim-definitions.html#Claim.procedure.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 </procedure>
 <[**insurance**](claim-definitions.html#Claim.insurance)> <!-- **1..*** Patient insurance information -->
 <[**sequence**](claim-definitions.html#Claim.insurance.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Insurance instance identifier](terminologies.html#unbound) -->
 <[**focal**](claim-definitions.html#Claim.insurance.focal) value="[[boolean](datatypes.html#boolean)]"/><!-- **1..1** [Coverage to be used for adjudication](terminologies.html#unbound) -->
 <[**identifier**](claim-definitions.html#Claim.insurance.identifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Pre-assigned Claim number](terminologies.html#unbound) --></identifier>
 <[**coverage**](claim-definitions.html#Claim.insurance.coverage)><!-- **1..1** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) [Insurance information](terminologies.html#unbound) --></coverage>
 <[**businessArrangement**](claim-definitions.html#Claim.insurance.businessArrangement) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Additional provider contract number](terminologies.html#unbound) -->
 <[**preAuthRef**](claim-definitions.html#Claim.insurance.preAuthRef) value="[[string](datatypes.html#string)]"/><!-- **0..*** [Prior authorization reference number](terminologies.html#unbound) -->
 <[**claimResponse**](claim-definitions.html#Claim.insurance.claimResponse)><!-- **0..1** [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) [Adjudication results](terminologies.html#unbound) --></claimResponse>
 </insurance>
 <[**accident**](claim-definitions.html#Claim.accident)> <!-- **0..1** Details of the event -->
 <[**date**](claim-definitions.html#Claim.accident.date) value="[[date](datatypes.html#date)]"/><!-- **1..1** [When the incident occurred](terminologies.html#unbound) -->
 <[**type**](claim-definitions.html#Claim.accident.type)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [The nature of the accident](v3/ActIncidentCode/vs.html) --></type>
 <[**location[x]**](claim-definitions.html#Claim.accident.location[x])><!-- **0..1** [Address](datatypes.html#Address)|[Reference](references.html#Reference)([Location](location.html#Location)) [Where the event occurred](terminologies.html#unbound) --></location[x]>
 </accident>
 <[**item**](claim-definitions.html#Claim.item)> <!-- **0..*** Product or service provided -->
 <[**sequence**](claim-definitions.html#Claim.item.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Item instance identifier](terminologies.html#unbound) -->
 <[**careTeamSequence**](claim-definitions.html#Claim.item.careTeamSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable careTeam members](terminologies.html#unbound) -->
 <[**diagnosisSequence**](claim-definitions.html#Claim.item.diagnosisSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable diagnoses](terminologies.html#unbound) -->
 <[**procedureSequence**](claim-definitions.html#Claim.item.procedureSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable procedures](terminologies.html#unbound) -->
 <[**informationSequence**](claim-definitions.html#Claim.item.informationSequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..*** [Applicable exception and supporting information](terminologies.html#unbound) -->
 <[**revenue**](claim-definitions.html#Claim.item.revenue)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Revenue or cost center code](valueset-ex-revenue-center.html) --></revenue>
 <[**category**](claim-definitions.html#Claim.item.category)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Benefit classification](valueset-ex-benefitcategory.html) --></category>
 <[**productOrService**](claim-definitions.html#Claim.item.productOrService)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Billing, service, product, or drug code](valueset-service-uscls.html) --></productOrService>
 <[**modifier**](claim-definitions.html#Claim.item.modifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Product or service billing modifiers](valueset-claim-modifiers.html) --></modifier>
 <[**programCode**](claim-definitions.html#Claim.item.programCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Program the product or service is provided under](valueset-ex-program-code.html) --></programCode>
 <[**serviced[x]**](claim-definitions.html#Claim.item.serviced[x])><!-- **0..1** [date](datatypes.html#date)|[Period](datatypes.html#Period) [Date or dates of service or product delivery](terminologies.html#unbound) --></serviced[x]>
 <[**location[x]**](claim-definitions.html#Claim.item.location[x])><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept)|[Address](datatypes.html#Address)|[Reference](references.html#Reference)([Location](location.html#Location)) [Place of service or where product was supplied](valueset-service-place.html) --></location[x]>
 <[**quantity**](claim-definitions.html#Claim.item.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Count of products or services](terminologies.html#unbound) --></quantity>
 <[**unitPrice**](claim-definitions.html#Claim.item.unitPrice)><!-- **0..1** [Money](datatypes.html#Money) [Fee, charge or cost per item](terminologies.html#unbound) --></unitPrice>
 <[**factor**](claim-definitions.html#Claim.item.factor) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Price scaling factor](terminologies.html#unbound) -->
 <[**net**](claim-definitions.html#Claim.item.net)><!-- **0..1** [Money](datatypes.html#Money) [Total item cost](terminologies.html#unbound) --></net>
 <[**udi**](claim-definitions.html#Claim.item.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 <[**bodySite**](claim-definitions.html#Claim.item.bodySite)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Anatomical location](valueset-tooth.html) --></bodySite>
 <[**subSite**](claim-definitions.html#Claim.item.subSite)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Anatomical sub-location](valueset-surface.html) --></subSite>
 <[**encounter**](claim-definitions.html#Claim.item.encounter)><!-- **0..*** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Encounters related to this billed item](terminologies.html#unbound) --></encounter>
 <[**detail**](claim-definitions.html#Claim.item.detail)> <!-- **0..*** Product or service provided -->
 <[**sequence**](claim-definitions.html#Claim.item.detail.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Item instance identifier](terminologies.html#unbound) -->
 <[**revenue**](claim-definitions.html#Claim.item.detail.revenue)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Revenue or cost center code](valueset-ex-revenue-center.html) --></revenue>
 <[**category**](claim-definitions.html#Claim.item.detail.category)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Benefit classification](valueset-ex-benefitcategory.html) --></category>
 <[**productOrService**](claim-definitions.html#Claim.item.detail.productOrService)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Billing, service, product, or drug code](valueset-service-uscls.html) --></productOrService>
 <[**modifier**](claim-definitions.html#Claim.item.detail.modifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Service/Product billing modifiers](valueset-claim-modifiers.html) --></modifier>
 <[**programCode**](claim-definitions.html#Claim.item.detail.programCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Program the product or service is provided under](valueset-ex-program-code.html) --></programCode>
 <[**quantity**](claim-definitions.html#Claim.item.detail.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Count of products or services](terminologies.html#unbound) --></quantity>
 <[**unitPrice**](claim-definitions.html#Claim.item.detail.unitPrice)><!-- **0..1** [Money](datatypes.html#Money) [Fee, charge or cost per item](terminologies.html#unbound) --></unitPrice>
 <[**factor**](claim-definitions.html#Claim.item.detail.factor) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Price scaling factor](terminologies.html#unbound) -->
 <[**net**](claim-definitions.html#Claim.item.detail.net)><!-- **0..1** [Money](datatypes.html#Money) [Total item cost](terminologies.html#unbound) --></net>
 <[**udi**](claim-definitions.html#Claim.item.detail.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 <[**subDetail**](claim-definitions.html#Claim.item.detail.subDetail)> <!-- **0..*** Product or service provided -->
 <[**sequence**](claim-definitions.html#Claim.item.detail.subDetail.sequence) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **1..1** [Item instance identifier](terminologies.html#unbound) -->
 <[**revenue**](claim-definitions.html#Claim.item.detail.subDetail.revenue)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Revenue or cost center code](valueset-ex-revenue-center.html) --></revenue>
 <[**category**](claim-definitions.html#Claim.item.detail.subDetail.category)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Benefit classification](valueset-ex-benefitcategory.html) --></category>
 <[**productOrService**](claim-definitions.html#Claim.item.detail.subDetail.productOrService)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Billing, service, product, or drug code](valueset-service-uscls.html) --></productOrService>
 <[**modifier**](claim-definitions.html#Claim.item.detail.subDetail.modifier)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Service/Product billing modifiers](valueset-claim-modifiers.html) --></modifier>
 <[**programCode**](claim-definitions.html#Claim.item.detail.subDetail.programCode)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Program the product or service is provided under](valueset-ex-program-code.html) --></programCode>
 <[**quantity**](claim-definitions.html#Claim.item.detail.subDetail.quantity)><!-- **0..1** [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [Count of products or services](terminologies.html#unbound) --></quantity>
 <[**unitPrice**](claim-definitions.html#Claim.item.detail.subDetail.unitPrice)><!-- **0..1** [Money](datatypes.html#Money) [Fee, charge or cost per item](terminologies.html#unbound) --></unitPrice>
 <[**factor**](claim-definitions.html#Claim.item.detail.subDetail.factor) value="[[decimal](datatypes.html#decimal)]"/><!-- **0..1** [Price scaling factor](terminologies.html#unbound) -->
 <[**net**](claim-definitions.html#Claim.item.detail.subDetail.net)><!-- **0..1** [Money](datatypes.html#Money) [Total item cost](terminologies.html#unbound) --></net>
 <[**udi**](claim-definitions.html#Claim.item.detail.subDetail.udi)><!-- **0..*** [Reference](references.html#Reference)([Device](device.html#Device)) [Unique device identifier](terminologies.html#unbound) --></udi>
 </subDetail>
 </detail>
 </item>
 <[**total**](claim-definitions.html#Claim.total)><!-- **0..1** [Money](datatypes.html#Money) [Total claim cost](terminologies.html#unbound) --></total>
</Claim>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Claim**](claim-definitions.html#Claim)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](claim-definitions.html#Claim.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business Identifier for claim](terminologies.html#unbound)
 "[status](claim-definitions.html#Claim.status)" : "<[code](datatypes.html#code)>", // **R!** [active | cancelled | draft | entered-in-error](valueset-fm-status.html)
 "[type](claim-definitions.html#Claim.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Category or discipline](valueset-claim-type.html)
 "[subType](claim-definitions.html#Claim.subType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [More granular claim type](valueset-claim-subtype.html)
 "[use](claim-definitions.html#Claim.use)" : "<[code](datatypes.html#code)>", // **R!** [claim | preauthorization | predetermination](valueset-claim-use.html)
 "[patient](claim-definitions.html#Claim.patient)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) }, // **R!** [The recipient of the products and services](terminologies.html#unbound)
 "[billablePeriod](claim-definitions.html#Claim.billablePeriod)" : { [Period](datatypes.html#Period) }, // [Relevant time frame for the claim](terminologies.html#unbound)
 "[created](claim-definitions.html#Claim.created)" : "<[dateTime](datatypes.html#dateTime)>", // **R!** [Resource creation date](terminologies.html#unbound)
 "[enterer](claim-definitions.html#Claim.enterer)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) }, // [Author of the claim](terminologies.html#unbound)
 "[insurer](claim-definitions.html#Claim.insurer)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // [Target](terminologies.html#unbound)
 "[provider](claim-definitions.html#Claim.provider)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }, // **R!** [Party responsible for the claim](terminologies.html#unbound)
 "[priority](claim-definitions.html#Claim.priority)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Desired processing ugency](valueset-process-priority.html)
 "[fundsReserve](claim-definitions.html#Claim.fundsReserve)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [For whom to reserve funds](valueset-fundsreserve.html)
 "[related](claim-definitions.html#Claim.related)" : [{ // [Prior or corollary claims](terminologies.html#unbound)
 "[claim](claim-definitions.html#Claim.related.claim)" : { [Reference](references.html#Reference)([Claim](claim.html#Claim)) }, // [Reference to the related claim](terminologies.html#unbound)
 "[relationship](claim-definitions.html#Claim.related.relationship)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [How the reference claim is related](valueset-related-claim-relationship.html)
 "[reference](claim-definitions.html#Claim.related.reference)" : { [Identifier](datatypes.html#Identifier) } // [File or case reference](terminologies.html#unbound)
 }],
 "[prescription](claim-definitions.html#Claim.prescription)" : { [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) }, // [Prescription authorizing services and products](terminologies.html#unbound)
 "[originalPrescription](claim-definitions.html#Claim.originalPrescription)" : { [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|
 [VisionPrescription](visionprescription.html#VisionPrescription)) }, // [Original prescription if superseded by fulfiller](terminologies.html#unbound)
 "[payee](claim-definitions.html#Claim.payee)" : { // [Recipient of benefits payable](terminologies.html#unbound)
 "[type](claim-definitions.html#Claim.payee.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Category of recipient](valueset-payeetype.html)
 "[party](claim-definitions.html#Claim.payee.party)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|
 [RelatedPerson](relatedperson.html#RelatedPerson)) } // [Recipient reference](terminologies.html#unbound)
 },
 "[referral](claim-definitions.html#Claim.referral)" : { [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) }, // [Treatment referral](terminologies.html#unbound)
 "[facility](claim-definitions.html#Claim.facility)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // [Servicing facility](terminologies.html#unbound)
 "[careTeam](claim-definitions.html#Claim.careTeam)" : [{ // [Members of the care team](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.careTeam.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Order of care team](terminologies.html#unbound)
 "[provider](claim-definitions.html#Claim.careTeam.provider)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }, // **R!** [Practitioner or organization](terminologies.html#unbound)
 "[responsible](claim-definitions.html#Claim.careTeam.responsible)" : <[boolean](datatypes.html#boolean)>, // [Indicator of the lead practitioner](terminologies.html#unbound)
 "[role](claim-definitions.html#Claim.careTeam.role)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Function within the team](valueset-claim-careteamrole.html)
 "[qualification](claim-definitions.html#Claim.careTeam.qualification)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Practitioner credential or specialization](valueset-provider-qualification.html)
 }],
 "[supportingInfo](claim-definitions.html#Claim.supportingInfo)" : [{ // [Supporting information](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.supportingInfo.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Information instance identifier](terminologies.html#unbound)
 "[category](claim-definitions.html#Claim.supportingInfo.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Classification of the supplied information](valueset-claim-informationcategory.html)
 "[code](claim-definitions.html#Claim.supportingInfo.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Type of information](valueset-claim-exception.html)
 // timing[x]: When it occurred. One of these 2:
 "[timingDate](claim-definitions.html#Claim.supportingInfo.timingDate)" : "<[date](datatypes.html#date)>",
 "[timingPeriod](claim-definitions.html#Claim.supportingInfo.timingPeriod)" : { [Period](datatypes.html#Period) },
 // value[x]: Data to be provided. One of these 5:
 "[valueBoolean](claim-definitions.html#Claim.supportingInfo.valueBoolean)" : <[boolean](datatypes.html#boolean)>,
 "[valueString](claim-definitions.html#Claim.supportingInfo.valueString)" : "<[string](datatypes.html#string)>",
 "[valueQuantity](claim-definitions.html#Claim.supportingInfo.valueQuantity)" : { [Quantity](datatypes.html#Quantity) },
 "[valueAttachment](claim-definitions.html#Claim.supportingInfo.valueAttachment)" : { [Attachment](datatypes.html#Attachment) },
 "[valueReference](claim-definitions.html#Claim.supportingInfo.valueReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) },
 "[reason](claim-definitions.html#Claim.supportingInfo.reason)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Explanation for the information](valueset-missing-tooth-reason.html)
 }],
 "[diagnosis](claim-definitions.html#Claim.diagnosis)" : [{ // [Pertinent diagnosis information](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.diagnosis.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Diagnosis instance identifier](terminologies.html#unbound)
 // diagnosis[x]: Nature of illness or problem. One of these 2:
 "[diagnosisCodeableConcept](claim-definitions.html#Claim.diagnosis.diagnosisCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[diagnosisReference](claim-definitions.html#Claim.diagnosis.diagnosisReference)" : { [Reference](references.html#Reference)([Condition](condition.html#Condition)) },
 "[type](claim-definitions.html#Claim.diagnosis.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Timing or nature of the diagnosis](valueset-ex-diagnosistype.html)
 "[onAdmission](claim-definitions.html#Claim.diagnosis.onAdmission)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Present on admission](valueset-ex-diagnosis-on-admission.html)
 "[packageCode](claim-definitions.html#Claim.diagnosis.packageCode)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Package billing code](valueset-ex-diagnosisrelatedgroup.html)
 }],
 "[procedure](claim-definitions.html#Claim.procedure)" : [{ // [Clinical procedures performed](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.procedure.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Procedure instance identifier](terminologies.html#unbound)
 "[type](claim-definitions.html#Claim.procedure.type)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Category of Procedure](valueset-ex-procedure-type.html)
 "[date](claim-definitions.html#Claim.procedure.date)" : "<[dateTime](datatypes.html#dateTime)>", // [When the procedure was performed](terminologies.html#unbound)
 // procedure[x]: Specific clinical procedure. One of these 2:
 "[procedureCodeableConcept](claim-definitions.html#Claim.procedure.procedureCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[procedureReference](claim-definitions.html#Claim.procedure.procedureReference)" : { [Reference](references.html#Reference)([Procedure](procedure.html#Procedure)) },
 "[udi](claim-definitions.html#Claim.procedure.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }] // [Unique device identifier](terminologies.html#unbound)
 }],
 "[insurance](claim-definitions.html#Claim.insurance)" : [{ // **R!** [Patient insurance information](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.insurance.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Insurance instance identifier](terminologies.html#unbound)
 "[focal](claim-definitions.html#Claim.insurance.focal)" : <[boolean](datatypes.html#boolean)>, // **R!** [Coverage to be used for adjudication](terminologies.html#unbound)
 "[identifier](claim-definitions.html#Claim.insurance.identifier)" : { [Identifier](datatypes.html#Identifier) }, // [Pre-assigned Claim number](terminologies.html#unbound)
 "[coverage](claim-definitions.html#Claim.insurance.coverage)" : { [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) }, // **R!** [Insurance information](terminologies.html#unbound)
 "[businessArrangement](claim-definitions.html#Claim.insurance.businessArrangement)" : "<[string](datatypes.html#string)>", // [Additional provider contract number](terminologies.html#unbound)
 "[preAuthRef](claim-definitions.html#Claim.insurance.preAuthRef)" : ["<[string](datatypes.html#string)>"], // [Prior authorization reference number](terminologies.html#unbound)
 "[claimResponse](claim-definitions.html#Claim.insurance.claimResponse)" : { [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) } // [Adjudication results](terminologies.html#unbound)
 }],
 "[accident](claim-definitions.html#Claim.accident)" : { // [Details of the event](terminologies.html#unbound)
 "[date](claim-definitions.html#Claim.accident.date)" : "<[date](datatypes.html#date)>", // **R!** [When the incident occurred](terminologies.html#unbound)
 "[type](claim-definitions.html#Claim.accident.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [The nature of the accident](v3/ActIncidentCode/vs.html)
 // location[x]: Where the event occurred. One of these 2:
 "[locationAddress](claim-definitions.html#Claim.accident.locationAddress)" : { [Address](datatypes.html#Address) }
 "[locationReference](claim-definitions.html#Claim.accident.locationReference)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }
 },
 "[item](claim-definitions.html#Claim.item)" : [{ // [Product or service provided](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.item.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Item instance identifier](terminologies.html#unbound)
 "[careTeamSequence](claim-definitions.html#Claim.item.careTeamSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable careTeam members](terminologies.html#unbound)
 "[diagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable diagnoses](terminologies.html#unbound)
 "[procedureSequence](claim-definitions.html#Claim.item.procedureSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable procedures](terminologies.html#unbound)
 "[informationSequence](claim-definitions.html#Claim.item.informationSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable exception and supporting information](terminologies.html#unbound)
 "[revenue](claim-definitions.html#Claim.item.revenue)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Revenue or cost center code](valueset-ex-revenue-center.html)
 "[category](claim-definitions.html#Claim.item.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Benefit classification](valueset-ex-benefitcategory.html)
 "[productOrService](claim-definitions.html#Claim.item.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claim-definitions.html#Claim.item.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Product or service billing modifiers](valueset-claim-modifiers.html)
 "[programCode](claim-definitions.html#Claim.item.programCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Program the product or service is provided under](valueset-ex-program-code.html)
 // serviced[x]: Date or dates of service or product delivery. One of these 2:
 "[servicedDate](claim-definitions.html#Claim.item.servicedDate)" : "<[date](datatypes.html#date)>",
 "[servicedPeriod](claim-definitions.html#Claim.item.servicedPeriod)" : { [Period](datatypes.html#Period) },
 // location[x]: Place of service or where product was supplied. One of these 3:
 "[locationCodeableConcept](claim-definitions.html#Claim.item.locationCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[locationAddress](claim-definitions.html#Claim.item.locationAddress)" : { [Address](datatypes.html#Address) },
 "[locationReference](claim-definitions.html#Claim.item.locationReference)" : { [Reference](references.html#Reference)([Location](location.html#Location)) },
 "[quantity](claim-definitions.html#Claim.item.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claim-definitions.html#Claim.item.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claim-definitions.html#Claim.item.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claim-definitions.html#Claim.item.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[udi](claim-definitions.html#Claim.item.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }], // [Unique device identifier](terminologies.html#unbound)
 "[bodySite](claim-definitions.html#Claim.item.bodySite)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Anatomical location](valueset-tooth.html)
 "[subSite](claim-definitions.html#Claim.item.subSite)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Anatomical sub-location](valueset-surface.html)
 "[encounter](claim-definitions.html#Claim.item.encounter)" : [{ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }], // [Encounters related to this billed item](terminologies.html#unbound)
 "[detail](claim-definitions.html#Claim.item.detail)" : [{ // [Product or service provided](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.item.detail.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Item instance identifier](terminologies.html#unbound)
 "[revenue](claim-definitions.html#Claim.item.detail.revenue)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Revenue or cost center code](valueset-ex-revenue-center.html)
 "[category](claim-definitions.html#Claim.item.detail.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Benefit classification](valueset-ex-benefitcategory.html)
 "[productOrService](claim-definitions.html#Claim.item.detail.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claim-definitions.html#Claim.item.detail.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Service/Product billing modifiers](valueset-claim-modifiers.html)
 "[programCode](claim-definitions.html#Claim.item.detail.programCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Program the product or service is provided under](valueset-ex-program-code.html)
 "[quantity](claim-definitions.html#Claim.item.detail.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claim-definitions.html#Claim.item.detail.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claim-definitions.html#Claim.item.detail.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claim-definitions.html#Claim.item.detail.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[udi](claim-definitions.html#Claim.item.detail.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }], // [Unique device identifier](terminologies.html#unbound)
 "[subDetail](claim-definitions.html#Claim.item.detail.subDetail)" : [{ // [Product or service provided](terminologies.html#unbound)
 "[sequence](claim-definitions.html#Claim.item.detail.subDetail.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Item instance identifier](terminologies.html#unbound)
 "[revenue](claim-definitions.html#Claim.item.detail.subDetail.revenue)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Revenue or cost center code](valueset-ex-revenue-center.html)
 "[category](claim-definitions.html#Claim.item.detail.subDetail.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Benefit classification](valueset-ex-benefitcategory.html)
 "[productOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claim-definitions.html#Claim.item.detail.subDetail.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Service/Product billing modifiers](valueset-claim-modifiers.html)
 "[programCode](claim-definitions.html#Claim.item.detail.subDetail.programCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Program the product or service is provided under](valueset-ex-program-code.html)
 "[quantity](claim-definitions.html#Claim.item.detail.subDetail.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claim-definitions.html#Claim.item.detail.subDetail.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claim-definitions.html#Claim.item.detail.subDetail.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[udi](claim-definitions.html#Claim.item.detail.subDetail.udi)" : [{ [Reference](references.html#Reference)([Device](device.html#Device)) }] // [Unique device identifier](terminologies.html#unbound)
 }]
 }]
 }],
 "[total](claim-definitions.html#Claim.total)" : { [Money](datatypes.html#Money) } // [Total claim cost](terminologies.html#unbound)
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Claim**](claim-definitions.html#Claim);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Claim.identifier](claim-definitions.html#Claim.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for claim
 fhir:[Claim.status](claim-definitions.html#Claim.status) [ [code](datatypes.html#code) ]; # 1..1 active | cancelled | draft | entered-in-error
 fhir:[Claim.type](claim-definitions.html#Claim.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Category or discipline
 fhir:[Claim.subType](claim-definitions.html#Claim.subType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 More granular claim type
 fhir:[Claim.use](claim-definitions.html#Claim.use) [ [code](datatypes.html#code) ]; # 1..1 claim | preauthorization | predetermination
 fhir:[Claim.patient](claim-definitions.html#Claim.patient) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 1..1 The recipient of the products and services
 fhir:[Claim.billablePeriod](claim-definitions.html#Claim.billablePeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Relevant time frame for the claim
 fhir:[Claim.created](claim-definitions.html#Claim.created) [ [dateTime](datatypes.html#dateTime) ]; # 1..1 Resource creation date
 fhir:[Claim.enterer](claim-definitions.html#Claim.enterer) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)) ]; # 0..1 Author of the claim
 fhir:[Claim.insurer](claim-definitions.html#Claim.insurer) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 0..1 Target
 fhir:[Claim.provider](claim-definitions.html#Claim.provider) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 1..1 Party responsible for the claim
 fhir:[Claim.priority](claim-definitions.html#Claim.priority) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Desired processing ugency
 fhir:[Claim.fundsReserve](claim-definitions.html#Claim.fundsReserve) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 For whom to reserve funds
 fhir:[Claim.related](claim-definitions.html#Claim.related) [ # 0..* Prior or corollary claims
 fhir:[Claim.related.claim](claim-definitions.html#Claim.related.claim) [ [Reference](references.html#Reference)([Claim](claim.html#Claim)) ]; # 0..1 Reference to the related claim
 fhir:[Claim.related.relationship](claim-definitions.html#Claim.related.relationship) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 How the reference claim is related
 fhir:[Claim.related.reference](claim-definitions.html#Claim.related.reference) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 File or case reference
 ], ...;
 fhir:[Claim.prescription](claim-definitions.html#Claim.prescription) [ [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[VisionPrescription](visionprescription.html#VisionPrescription)) ]; # 0..1 Prescription authorizing services and products
 fhir:[Claim.originalPrescription](claim-definitions.html#Claim.originalPrescription) [ [Reference](references.html#Reference)([DeviceRequest](devicerequest.html#DeviceRequest)|[MedicationRequest](medicationrequest.html#MedicationRequest)|[VisionPrescription](visionprescription.html#VisionPrescription)) ]; # 0..1 Original prescription if superseded by fulfiller
 fhir:[Claim.payee](claim-definitions.html#Claim.payee) [ # 0..1 Recipient of benefits payable
 fhir:[Claim.payee.type](claim-definitions.html#Claim.payee.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Category of recipient
 fhir:[Claim.payee.party](claim-definitions.html#Claim.payee.party) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Recipient reference
 ];
 fhir:[Claim.referral](claim-definitions.html#Claim.referral) [ [Reference](references.html#Reference)([ServiceRequest](servicerequest.html#ServiceRequest)) ]; # 0..1 Treatment referral
 fhir:[Claim.facility](claim-definitions.html#Claim.facility) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 0..1 Servicing facility
 fhir:[Claim.careTeam](claim-definitions.html#Claim.careTeam) [ # 0..* Members of the care team
 fhir:[Claim.careTeam.sequence](claim-definitions.html#Claim.careTeam.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Order of care team
 fhir:[Claim.careTeam.provider](claim-definitions.html#Claim.careTeam.provider) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 1..1 Practitioner or organization
 fhir:[Claim.careTeam.responsible](claim-definitions.html#Claim.careTeam.responsible) [ [boolean](datatypes.html#boolean) ]; # 0..1 Indicator of the lead practitioner
 fhir:[Claim.careTeam.role](claim-definitions.html#Claim.careTeam.role) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Function within the team
 fhir:[Claim.careTeam.qualification](claim-definitions.html#Claim.careTeam.qualification) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Practitioner credential or specialization
 ], ...;
 fhir:[Claim.supportingInfo](claim-definitions.html#Claim.supportingInfo) [ # 0..* Supporting information
 fhir:[Claim.supportingInfo.sequence](claim-definitions.html#Claim.supportingInfo.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Information instance identifier
 fhir:[Claim.supportingInfo.category](claim-definitions.html#Claim.supportingInfo.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Classification of the supplied information
 fhir:[Claim.supportingInfo.code](claim-definitions.html#Claim.supportingInfo.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Type of information
 # [Claim.supportingInfo.timing[x]](claim-definitions.html#Claim.supportingInfo.timing[x]) : 0..1 When it occurred. One of these 2
 fhir:[Claim.supportingInfo.timingDate](claim-definitions.html#Claim.supportingInfo.timingDate) [ [date](datatypes.html#date) ]
 fhir:[Claim.supportingInfo.timingPeriod](claim-definitions.html#Claim.supportingInfo.timingPeriod) [ [Period](datatypes.html#Period) ]
 # [Claim.supportingInfo.value[x]](claim-definitions.html#Claim.supportingInfo.value[x]) : 0..1 Data to be provided. One of these 5
 fhir:[Claim.supportingInfo.valueBoolean](claim-definitions.html#Claim.supportingInfo.valueBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Claim.supportingInfo.valueString](claim-definitions.html#Claim.supportingInfo.valueString) [ [string](datatypes.html#string) ]
 fhir:[Claim.supportingInfo.valueQuantity](claim-definitions.html#Claim.supportingInfo.valueQuantity) [ [Quantity](datatypes.html#Quantity) ]
 fhir:[Claim.supportingInfo.valueAttachment](claim-definitions.html#Claim.supportingInfo.valueAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Claim.supportingInfo.valueReference](claim-definitions.html#Claim.supportingInfo.valueReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]
 fhir:[Claim.supportingInfo.reason](claim-definitions.html#Claim.supportingInfo.reason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Explanation for the information
 ], ...;
 fhir:[Claim.diagnosis](claim-definitions.html#Claim.diagnosis) [ # 0..* Pertinent diagnosis information
 fhir:[Claim.diagnosis.sequence](claim-definitions.html#Claim.diagnosis.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Diagnosis instance identifier
 # [Claim.diagnosis.diagnosis[x]](claim-definitions.html#Claim.diagnosis.diagnosis[x]) : 1..1 Nature of illness or problem. One of these 2
 fhir:[Claim.diagnosis.diagnosisCodeableConcept](claim-definitions.html#Claim.diagnosis.diagnosisCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Claim.diagnosis.diagnosisReference](claim-definitions.html#Claim.diagnosis.diagnosisReference) [ [Reference](references.html#Reference)([Condition](condition.html#Condition)) ]
 fhir:[Claim.diagnosis.type](claim-definitions.html#Claim.diagnosis.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Timing or nature of the diagnosis
 fhir:[Claim.diagnosis.onAdmission](claim-definitions.html#Claim.diagnosis.onAdmission) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Present on admission
 fhir:[Claim.diagnosis.packageCode](claim-definitions.html#Claim.diagnosis.packageCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Package billing code
 ], ...;
 fhir:[Claim.procedure](claim-definitions.html#Claim.procedure) [ # 0..* Clinical procedures performed
 fhir:[Claim.procedure.sequence](claim-definitions.html#Claim.procedure.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Procedure instance identifier
 fhir:[Claim.procedure.type](claim-definitions.html#Claim.procedure.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Category of Procedure
 fhir:[Claim.procedure.date](claim-definitions.html#Claim.procedure.date) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 When the procedure was performed
 # [Claim.procedure.procedure[x]](claim-definitions.html#Claim.procedure.procedure[x]) : 1..1 Specific clinical procedure. One of these 2
 fhir:[Claim.procedure.procedureCodeableConcept](claim-definitions.html#Claim.procedure.procedureCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Claim.procedure.procedureReference](claim-definitions.html#Claim.procedure.procedureReference) [ [Reference](references.html#Reference)([Procedure](procedure.html#Procedure)) ]
 fhir:[Claim.procedure.udi](claim-definitions.html#Claim.procedure.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 ], ...;
 fhir:[Claim.insurance](claim-definitions.html#Claim.insurance) [ # 1..* Patient insurance information
 fhir:[Claim.insurance.sequence](claim-definitions.html#Claim.insurance.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Insurance instance identifier
 fhir:[Claim.insurance.focal](claim-definitions.html#Claim.insurance.focal) [ [boolean](datatypes.html#boolean) ]; # 1..1 Coverage to be used for adjudication
 fhir:[Claim.insurance.identifier](claim-definitions.html#Claim.insurance.identifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Pre-assigned Claim number
 fhir:[Claim.insurance.coverage](claim-definitions.html#Claim.insurance.coverage) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) ]; # 1..1 Insurance information
 fhir:[Claim.insurance.businessArrangement](claim-definitions.html#Claim.insurance.businessArrangement) [ [string](datatypes.html#string) ]; # 0..1 Additional provider contract number
 fhir:[Claim.insurance.preAuthRef](claim-definitions.html#Claim.insurance.preAuthRef) [ [string](datatypes.html#string) ], ... ; # 0..* Prior authorization reference number
 fhir:[Claim.insurance.claimResponse](claim-definitions.html#Claim.insurance.claimResponse) [ [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) ]; # 0..1 Adjudication results
 ], ...;
 fhir:[Claim.accident](claim-definitions.html#Claim.accident) [ # 0..1 Details of the event
 fhir:[Claim.accident.date](claim-definitions.html#Claim.accident.date) [ [date](datatypes.html#date) ]; # 1..1 When the incident occurred
 fhir:[Claim.accident.type](claim-definitions.html#Claim.accident.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 The nature of the accident
 # [Claim.accident.location[x]](claim-definitions.html#Claim.accident.location[x]) : 0..1 Where the event occurred. One of these 2
 fhir:[Claim.accident.locationAddress](claim-definitions.html#Claim.accident.locationAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Claim.accident.locationReference](claim-definitions.html#Claim.accident.locationReference) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]
 ];
 fhir:[Claim.item](claim-definitions.html#Claim.item) [ # 0..* Product or service provided
 fhir:[Claim.item.sequence](claim-definitions.html#Claim.item.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Item instance identifier
 fhir:[Claim.item.careTeamSequence](claim-definitions.html#Claim.item.careTeamSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable careTeam members
 fhir:[Claim.item.diagnosisSequence](claim-definitions.html#Claim.item.diagnosisSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable diagnoses
 fhir:[Claim.item.procedureSequence](claim-definitions.html#Claim.item.procedureSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable procedures
 fhir:[Claim.item.informationSequence](claim-definitions.html#Claim.item.informationSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable exception and supporting information
 fhir:[Claim.item.revenue](claim-definitions.html#Claim.item.revenue) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Revenue or cost center code
 fhir:[Claim.item.category](claim-definitions.html#Claim.item.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Benefit classification
 fhir:[Claim.item.productOrService](claim-definitions.html#Claim.item.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[Claim.item.modifier](claim-definitions.html#Claim.item.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Product or service billing modifiers
 fhir:[Claim.item.programCode](claim-definitions.html#Claim.item.programCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Program the product or service is provided under
 # [Claim.item.serviced[x]](claim-definitions.html#Claim.item.serviced[x]) : 0..1 Date or dates of service or product delivery. One of these 2
 fhir:[Claim.item.servicedDate](claim-definitions.html#Claim.item.servicedDate) [ [date](datatypes.html#date) ]
 fhir:[Claim.item.servicedPeriod](claim-definitions.html#Claim.item.servicedPeriod) [ [Period](datatypes.html#Period) ]
 # [Claim.item.location[x]](claim-definitions.html#Claim.item.location[x]) : 0..1 Place of service or where product was supplied. One of these 3
 fhir:[Claim.item.locationCodeableConcept](claim-definitions.html#Claim.item.locationCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Claim.item.locationAddress](claim-definitions.html#Claim.item.locationAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Claim.item.locationReference](claim-definitions.html#Claim.item.locationReference) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]
 fhir:[Claim.item.quantity](claim-definitions.html#Claim.item.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[Claim.item.unitPrice](claim-definitions.html#Claim.item.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[Claim.item.factor](claim-definitions.html#Claim.item.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[Claim.item.net](claim-definitions.html#Claim.item.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[Claim.item.udi](claim-definitions.html#Claim.item.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 fhir:[Claim.item.bodySite](claim-definitions.html#Claim.item.bodySite) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Anatomical location
 fhir:[Claim.item.subSite](claim-definitions.html#Claim.item.subSite) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Anatomical sub-location
 fhir:[Claim.item.encounter](claim-definitions.html#Claim.item.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ], ... ; # 0..* Encounters related to this billed item
 fhir:[Claim.item.detail](claim-definitions.html#Claim.item.detail) [ # 0..* Product or service provided
 fhir:[Claim.item.detail.sequence](claim-definitions.html#Claim.item.detail.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Item instance identifier
 fhir:[Claim.item.detail.revenue](claim-definitions.html#Claim.item.detail.revenue) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Revenue or cost center code
 fhir:[Claim.item.detail.category](claim-definitions.html#Claim.item.detail.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Benefit classification
 fhir:[Claim.item.detail.productOrService](claim-definitions.html#Claim.item.detail.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[Claim.item.detail.modifier](claim-definitions.html#Claim.item.detail.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Service/Product billing modifiers
 fhir:[Claim.item.detail.programCode](claim-definitions.html#Claim.item.detail.programCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Program the product or service is provided under
 fhir:[Claim.item.detail.quantity](claim-definitions.html#Claim.item.detail.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[Claim.item.detail.unitPrice](claim-definitions.html#Claim.item.detail.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[Claim.item.detail.factor](claim-definitions.html#Claim.item.detail.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[Claim.item.detail.net](claim-definitions.html#Claim.item.detail.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[Claim.item.detail.udi](claim-definitions.html#Claim.item.detail.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 fhir:[Claim.item.detail.subDetail](claim-definitions.html#Claim.item.detail.subDetail) [ # 0..* Product or service provided
 fhir:[Claim.item.detail.subDetail.sequence](claim-definitions.html#Claim.item.detail.subDetail.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Item instance identifier
 fhir:[Claim.item.detail.subDetail.revenue](claim-definitions.html#Claim.item.detail.subDetail.revenue) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Revenue or cost center code
 fhir:[Claim.item.detail.subDetail.category](claim-definitions.html#Claim.item.detail.subDetail.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Benefit classification
 fhir:[Claim.item.detail.subDetail.productOrService](claim-definitions.html#Claim.item.detail.subDetail.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[Claim.item.detail.subDetail.modifier](claim-definitions.html#Claim.item.detail.subDetail.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Service/Product billing modifiers
 fhir:[Claim.item.detail.subDetail.programCode](claim-definitions.html#Claim.item.detail.subDetail.programCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Program the product or service is provided under
 fhir:[Claim.item.detail.subDetail.quantity](claim-definitions.html#Claim.item.detail.subDetail.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[Claim.item.detail.subDetail.unitPrice](claim-definitions.html#Claim.item.detail.subDetail.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[Claim.item.detail.subDetail.factor](claim-definitions.html#Claim.item.detail.subDetail.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[Claim.item.detail.subDetail.net](claim-definitions.html#Claim.item.detail.subDetail.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[Claim.item.detail.subDetail.udi](claim-definitions.html#Claim.item.detail.subDetail.udi) [ [Reference](references.html#Reference)([Device](device.html#Device)) ], ... ; # 0..* Unique device identifier
 ], ...;
 ], ...;
 ], ...;
 fhir:[Claim.total](claim-definitions.html#Claim.total) [ [Money](datatypes.html#Money) ]; # 0..1 Total claim cost
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Claim](claim.html#Claim)
 | 
 | 
 |

 | 
 Claim.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/fm-status to http://hl7.org/fhir/ValueSet/fm-status|4.0.1

 

 | 
 |

 | 
 Claim.type | 
 
 

 - Min Cardinality changed from 0 to 1

 - Change binding strength from required to extensible

 

 | 
 |

 | 
 Claim.subType | 
 
 

 - Max Cardinality changed from * to 1

 

 | 
 |

 | 
 Claim.use | 
 
 

 - Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/claim-use to http://hl7.org/fhir/ValueSet/claim-use|4.0.1

 

 | 
 |

 | 
 Claim.patient | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.created | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.enterer | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Claim.provider | 
 
 

 - Min Cardinality changed from 0 to 1

 - Type Reference: Added Target Types PractitionerRole, Organization

 

 | 
 |

 | 
 Claim.priority | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.prescription | 
 
 

 - Type Reference: Added Target Type DeviceRequest

 

 | 
 |

 | 
 Claim.originalPrescription | 
 
 

 - Type Reference: Added Target Types DeviceRequest, VisionPrescription

 

 | 
 |

 | 
 Claim.payee.party | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Claim.referral | 
 
 

 - Type Reference: Added Target Type ServiceRequest

 - Type Reference: Removed Target Type ReferralRequest

 

 | 
 |

 | 
 Claim.careTeam.provider | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Claim.supportingInfo | 
 
 

 - Renamed from information to supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.sequence | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.category | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.code | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.timing[x] | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.supportingInfo.value[x] | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 - Add Type boolean

 

 | 
 |

 | 
 Claim.supportingInfo.reason | 
 
 

 - Moved from Claim.information to Claim.supportingInfo

 

 | 
 |

 | 
 Claim.diagnosis.onAdmission | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.procedure.type | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.procedure.udi | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.insurance | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.insurance.identifier | 
 
 

 - Added Element

 

 | 
 |

 | 
 Claim.accident.type | 
 
 

 - Change binding strength from required to extensible

 

 | 
 |

 | 
 Claim.item.careTeamSequence | 
 
 

 - Renamed from careTeamLinkId to careTeamSequence

 

 | 
 |

 | 
 Claim.item.diagnosisSequence | 
 
 

 - Renamed from diagnosisLinkId to diagnosisSequence

 

 | 
 |

 | 
 Claim.item.procedureSequence | 
 
 

 - Renamed from procedureLinkId to procedureSequence

 

 | 
 |

 | 
 Claim.item.informationSequence | 
 
 

 - Renamed from informationLinkId to informationSequence

 

 | 
 |

 | 
 Claim.item.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.item.detail.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.item.detail.subDetail.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 Claim.organization | 
 
 

 - deleted

 

 | 
 |

 | 
 Claim.payee.resourceType | 
 
 

 - deleted

 

 | 
 |

 | 
 Claim.employmentImpacted | 
 
 

 - deleted

 

 | 
 |

 | 
 Claim.hospitalization | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](claim.diff.xml) or [JSON](claim.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](claim-version-maps.html) (status = 16 tests of which 3 fail to execute. 13 fail round-trip testing and 3 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](claim-profiles.html) and the alternate definitions:
Master Definition [XML](claim.profile.xml.html) + [JSON](claim.profile.json.html),
[XML](xml.html) [Schema](claim.xsd)/[Schematron](claim.sch) + [JSON](json.html) 
[Schema](claim.schema.json.html), [ShEx](claim.shex.html) (for [Turtle](rdf.html)) + [see the extensions](claim-profiles.html) & the [dependency analysis](claim-dependencies.html)

### 13.6.3.1 
Terminology Bindings
 [
](claim.html#tx)

 | Path | Definition | Type | Reference | |

 | Claim.status | A code specifying the state of the resource instance. | [Required](terminologies.html#required) | [FinancialResourceStatusCodes](valueset-fm-status.html) | |

 | Claim.type | The type or discipline-style of the claim. | [Extensible](terminologies.html#extensible) | [ClaimTypeCodes](valueset-claim-type.html) | |

 | Claim.subType | A more granular claim typecode. | [Example](terminologies.html#example) | [ExampleClaimSubTypeCodes](valueset-claim-subtype.html) | |

 | Claim.use | The purpose of the Claim: predetermination, preauthorization, claim. | [Required](terminologies.html#required) | [Use](valueset-claim-use.html) | |

 | Claim.priority | The timeliness with which processing is required: stat, normal, deferred. | [Example](terminologies.html#example) | [ProcessPriorityCodes](valueset-process-priority.html) | |

 | Claim.fundsReserve | For whom funds are to be reserved: (Patient, Provider, None). | [Example](terminologies.html#example) | [Funds Reservation Codes](valueset-fundsreserve.html) | |

 | Claim.related.relationship | Relationship of this claim to a related Claim. | [Example](terminologies.html#example) | [ExampleRelatedClaimRelationshipCodes](valueset-related-claim-relationship.html) | |

 | Claim.payee.type | A code for the party to be reimbursed. | [Example](terminologies.html#example) | [Claim Payee Type Codes](valueset-payeetype.html) | |

 | Claim.careTeam.role | The role codes for the care team members. | [Example](terminologies.html#example) | [ClaimCareTeamRoleCodes](valueset-claim-careteamrole.html) | |

 | Claim.careTeam.qualification | Provider professional qualifications. | [Example](terminologies.html#example) | [ExampleProviderQualificationCodes](valueset-provider-qualification.html) | |

 | Claim.supportingInfo.category | The valuset used for additional information category codes. | [Example](terminologies.html#example) | [ClaimInformationCategoryCodes](valueset-claim-informationcategory.html) | |

 | Claim.supportingInfo.code | The valuset used for additional information codes. | [Example](terminologies.html#example) | [ExceptionCodes](valueset-claim-exception.html) | |

 | Claim.supportingInfo.reason | Reason codes for the missing teeth. | [Example](terminologies.html#example) | [MissingToothReasonCodes](valueset-missing-tooth-reason.html) | |

 | Claim.diagnosis.diagnosis[x] | Example ICD10 Diagnostic codes. | [Example](terminologies.html#example) | [ICD-10Codes](valueset-icd-10.html) | |

 | Claim.diagnosis.type | The type of the diagnosis: admitting, principal, discharge. | [Example](terminologies.html#example) | [ExampleDiagnosisTypeCodes](valueset-ex-diagnosistype.html) | |

 | Claim.diagnosis.onAdmission | Present on admission. | [Example](terminologies.html#example) | [ExampleDiagnosisOnAdmissionCodes](valueset-ex-diagnosis-on-admission.html) | |

 | Claim.diagnosis.packageCode | The DRG codes associated with the diagnosis. | [Example](terminologies.html#example) | [ExampleDiagnosisRelatedGroupCodes](valueset-ex-diagnosisrelatedgroup.html) | |

 | Claim.procedure.type | Example procedure type codes. | [Example](terminologies.html#example) | [ExampleProcedureTypeCodes](valueset-ex-procedure-type.html) | |

 | Claim.procedure.procedure[x] | Example ICD10 Procedure codes. | [Example](terminologies.html#example) | [ICD-10ProcedureCodes](valueset-icd-10-procedures.html) | |

 | Claim.accident.type | Type of accident: work place, auto, etc. | [Extensible](terminologies.html#extensible) | [v3.ActIncidentCode](v3/ActIncidentCode/vs.html) | |

 | Claim.item.revenue**Claim.item.detail.revenue
Claim.item.detail.subDetail.revenue | Codes for the revenue or cost centers supplying the service and/or products. | [Example](terminologies.html#example) | [ExampleRevenueCenterCodes](valueset-ex-revenue-center.html) | |

 | Claim.item.category
Claim.item.detail.category
Claim.item.detail.subDetail.category | Benefit categories such as: oral-basic, major, glasses. | [Example](terminologies.html#example) | [BenefitCategoryCodes](valueset-ex-benefitcategory.html) | |

 | Claim.item.productOrService
Claim.item.detail.productOrService
Claim.item.detail.subDetail.productOrService | Allowable service and product codes. | [Example](terminologies.html#example) | [USCLSCodes](valueset-service-uscls.html) | |

 | Claim.item.modifier
Claim.item.detail.modifier
Claim.item.detail.subDetail.modifier | Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. | [Example](terminologies.html#example) | [ModifierTypeCodes](valueset-claim-modifiers.html) | |

 | Claim.item.programCode
Claim.item.detail.programCode
Claim.item.detail.subDetail.programCode | Program specific reason codes. | [Example](terminologies.html#example) | [ExampleProgramReasonCodes](valueset-ex-program-code.html) | |

 | Claim.item.location[x] | Place of service: pharmacy, school, prison, etc. | [Example](terminologies.html#example) | [ExampleServicePlaceCodes](valueset-service-place.html) | |

 | Claim.item.bodySite | The code for the teeth, quadrant, sextant and arch. | [Example](terminologies.html#example) | [OralSiteCodes](valueset-tooth.html) | |

 | Claim.item.subSite | The code for the tooth surface and surface combinations. | [Example](terminologies.html#example) | [SurfaceCodes](valueset-surface.html) | |

 

 

## 13.6.4 Search Parameters [
](claim.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| Name** | **Type** | **Description** | **Expression** | **In Common** | |

| care-team | [reference](search.html#reference) | Member of the CareTeam | Claim.careTeam.provider
([Practitioner](practitioner.html), [Organization](organization.html), [PractitionerRole](practitionerrole.html)) | | |

| created | [date](search.html#date) | The creation date for the Claim | Claim.created | | |

| detail-udi | [reference](search.html#reference) | UDI associated with a line item, detail product or service | Claim.item.detail.udi
([Device](device.html)) | | |

| encounter | [reference](search.html#reference) | Encounters associated with a billed line item | Claim.item.encounter
([Encounter](encounter.html)) | | |

| enterer | [reference](search.html#reference) | The party responsible for the entry of the Claim | Claim.enterer
([Practitioner](practitioner.html), [PractitionerRole](practitionerrole.html)) | | |

| facility | [reference](search.html#reference) | Facility where the products or services have been or will be provided | Claim.facility
([Location](location.html)) | | |

| identifier | [token](search.html#token) | The primary identifier of the financial resource | Claim.identifier | | |

| insurer | [reference](search.html#reference) | The target payor/insurer for the Claim | Claim.insurer
([Organization](organization.html)) | | |

| item-udi | [reference](search.html#reference) | UDI associated with a line item product or service | Claim.item.udi
([Device](device.html)) | | |

| patient | [reference](search.html#reference) | Patient receiving the products or services | Claim.patient
([Patient](patient.html)) | | |

| payee | [reference](search.html#reference) | The party receiving any payment for the Claim | Claim.payee.party
([Practitioner](practitioner.html), [Organization](organization.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| priority | [token](search.html#token) | Processing priority requested | Claim.priority | | |

| procedure-udi | [reference](search.html#reference) | UDI associated with a procedure | Claim.procedure.udi
([Device](device.html)) | | |

| provider | [reference](search.html#reference) | Provider responsible for the Claim | Claim.provider
([Practitioner](practitioner.html), [Organization](organization.html), [PractitionerRole](practitionerrole.html)) | | |

| status | [token](search.html#token) | The status of the Claim instance. | Claim.status | | |

| subdetail-udi | [reference](search.html#reference) | UDI associated with a line item, detail, subdetail product or service | Claim.item.detail.subDetail.udi
([Device](device.html)) | | |

| use | [token](search.html#token) | The kind of financial resource | Claim.use | | |