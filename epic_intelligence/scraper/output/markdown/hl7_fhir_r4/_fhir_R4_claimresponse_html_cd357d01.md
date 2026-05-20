# ClaimResponse - FHIR v4.0.1A unique identifier assigned to this claim responseThe status of the resource instance (this element modifies the meaning of other elements)A code specifying the state of the resource instance. (Strength=Required)A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty serviceThe type or discipline-style of the claim. (Strength=Extensible)A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty serviceA more granular claim typecode. (Strength=Example)A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the futureClaim, preauthorization, predetermination. (Strength=Required)The party to whom the professional services and/or products have been supplied or are being considered and for whom actual for facast reimbursement is soughtThe date this resource was createdThe party responsible for authorization, adjudication and reimbursementThe provider which is responsible for the claim, predetermination or preauthorizationOriginal request resource referenceThe outcome of the claim, predetermination, or preauthorization processingThe result of the claim processing. (Strength=Required)A human readable description of the status of the adjudicationReference from the Insurer which is used in later communications which refers to this adjudicationThe time frame during which this authorization is effectiveType of Party to be reimbursed: subscriber, provider, otherA code for the party to be reimbursed. (Strength=Example)A code, used only on a response to a preauthorization, to indicate whether the benefits payable have been reserved and for whomFor whom funds are to be reserved: (Patient, Provider, None). (Strength=Example)A code for the form to be used for printing the contentThe forms codes. (Strength=Example)The actual form, by reference or inclusion, for printing the content or an EOBRequest for additional supporting or authorizing informationA number to uniquely reference the claim item entriesThe numbers associated with notes below which apply to the adjudication of this itemA code to indicate the information type of this adjudication record. Information types may include the value submitted, maximum values or percentages allowed or payable under the plan, amounts that: the patient is responsible for in aggregate or pertaining to this item; amounts paid by other coverages; and, the benefit payable for this itemThe adjudication codes. (Strength=Example)A code supporting the understanding of the adjudication result and explaining variance from expected amountThe adjudication reason codes. (Strength=Example)Monetary amount associated with the categoryA non-monetary value associated with the category. Mutually exclusive to the amount element aboveA number to uniquely reference the claim detail entryThe numbers associated with notes below which apply to the adjudication of this itemA number to uniquely reference the claim sub-detail entryThe numbers associated with notes below which apply to the adjudication of this itemClaim items which this service line is intended to replaceThe sequence number of the details within the claim item which this line is intended to replaceThe sequence number of the sub-details within the details within the claim item which this line is intended to replaceThe providers who are authorized for the services rendered to the patientWhen the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The date or dates when the service or product was supplied, performed or completedWhere the product or service was providedPlace of service: pharmacy, school, prison, etc. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargePhysical service site on the patient (limb, tooth, etc.)The code for the teeth, quadrant, sextant and arch. (Strength=Example)A region or surface of the bodySite, e.g. limb region or tooth surface(s)The code for the tooth surface and surface combinations. (Strength=Example)The numbers associated with notes below which apply to the adjudication of this itemWhen the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeThe numbers associated with notes below which apply to the adjudication of this itemWhen the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeThe numbers associated with notes below which apply to the adjudication of this itemA code to indicate the information type of this adjudication record. Information types may include: the value submitted, maximum values or percentages allowed or payable under the plan, amounts that the patient is responsible for in aggregate or pertaining to this item, amounts paid by other coverages, and the benefit payable for this itemThe adjudication codes. (Strength=Example)Monetary total amount associated with the categoryWhether this represents partial or complete payment of the benefits payableThe type (partial, complete) of the payment. (Strength=Example)Total amount of all adjustments to this payment included in this transaction which are not related to this claim's adjudicationReason for the payment adjustmentPayment Adjustment reason codes. (Strength=Example)Estimated date the payment will be issued or the actual issue date of paymentBenefits payable less any payment adjustmentIssuer's unique identifier for the payment instrumentA number to uniquely identify a note entryThe business purpose of the note textThe presentation types of notes. (Strength=Required)The explanation or description associated with the processingA code to define the language used in the text of the noteA human language. (Strength=Preferred)A number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit orderA flag to indicate that this Coverage is to be used for adjudication of this claim when set to trueReference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information systemA business agreement number established between the provider and the insurer for special business processing purposesThe result of the adjudication of the line items for the Coverage specified in this insuranceThe sequence number of the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structureThe sequence number of the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structureThe sequence number of the sub-detail within the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structureAn error code, from a specified code system, which details why the claim could not be adjudicatedThe adjudication error codes. (Strength=Example)If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this itemThe adjudication resultsThe adjudication resultsA sub-detail adjudication of a simple product or serviceA claim detail. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsA claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-detailsThe adjudication resultsThe adjudication resultsThe adjudication resultsThe third-tier service adjudications for payor added servicesThe second-tier service adjudications for payor added servicesThe first-tier service adjudications for payor added product or service linesThe adjudication results which are presented at the header level rather than at the line-item or add-item levelsCategorized monetary totals for the adjudicationPayment details for the adjudication of the claimA note that describes or explains adjudication results in a human readable formFinancial instruments for reimbursement for the health care products and services specified on the claimErrors encountered during the processing of the adjudicationA unique identifier assigned to this claim responseThe status of the resource instance (this element modifies the meaning of other elements)A code specifying the state of the resource instance. (Strength=Required)A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty serviceThe type or discipline-style of the claim. (Strength=Extensible)A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty serviceA more granular claim typecode. (Strength=Example)A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the futureClaim, preauthorization, predetermination. (Strength=Required)The party to whom the professional services and/or products have been supplied or are being considered and for whom actual for facast reimbursement is soughtThe date this resource was createdThe party responsible for authorization, adjudication and reimbursementThe provider which is responsible for the claim, predetermination or preauthorizationOriginal request resource referenceThe outcome of the claim, predetermination, or preauthorization processingThe result of the claim processing. (Strength=Required)A human readable description of the status of the adjudicationReference from the Insurer which is used in later communications which refers to this adjudicationThe time frame during which this authorization is effectiveType of Party to be reimbursed: subscriber, provider, otherA code for the party to be reimbursed. (Strength=Example)A code, used only on a response to a preauthorization, to indicate whether the benefits payable have been reserved and for whomFor whom funds are to be reserved: (Patient, Provider, None). (Strength=Example)A code for the form to be used for printing the contentThe forms codes. (Strength=Example)The actual form, by reference or inclusion, for printing the content or an EOBRequest for additional supporting or authorizing informationA number to uniquely reference the claim item entriesThe numbers associated with notes below which apply to the adjudication of this itemA code to indicate the information type of this adjudication record. Information types may include the value submitted, maximum values or percentages allowed or payable under the plan, amounts that: the patient is responsible for in aggregate or pertaining to this item; amounts paid by other coverages; and, the benefit payable for this itemThe adjudication codes. (Strength=Example)A code supporting the understanding of the adjudication result and explaining variance from expected amountThe adjudication reason codes. (Strength=Example)Monetary amount associated with the categoryA non-monetary value associated with the category. Mutually exclusive to the amount element aboveA number to uniquely reference the claim detail entryThe numbers associated with notes below which apply to the adjudication of this itemA number to uniquely reference the claim sub-detail entryThe numbers associated with notes below which apply to the adjudication of this itemClaim items which this service line is intended to replaceThe sequence number of the details within the claim item which this line is intended to replaceThe sequence number of the sub-details within the details within the claim item which this line is intended to replaceThe providers who are authorized for the services rendered to the patientWhen the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)Identifies the program under which this may be recoveredProgram specific reason codes. (Strength=Example)The date or dates when the service or product was supplied, performed or completedWhere the product or service was providedPlace of service: pharmacy, school, prison, etc. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargePhysical service site on the patient (limb, tooth, etc.)The code for the teeth, quadrant, sextant and arch. (Strength=Example)A region or surface of the bodySite, e.g. limb region or tooth surface(s)The code for the tooth surface and surface combinations. (Strength=Example)The numbers associated with notes below which apply to the adjudication of this itemWhen the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeThe numbers associated with notes below which apply to the adjudication of this itemWhen the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemAllowable service and product codes. (Strength=Example)Item typification or modifiers codes to convey additional context for the product or serviceItem type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)The number of repetitions of a service or productIf the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupA real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountThe quantity times the unit price for an additional service or product or chargeThe numbers associated with notes below which apply to the adjudication of this itemA code to indicate the information type of this adjudication record. Information types may include: the value submitted, maximum values or percentages allowed or payable under the plan, amounts that the patient is responsible for in aggregate or pertaining to this item, amounts paid by other coverages, and the benefit payable for this itemThe adjudication codes. (Strength=Example)Monetary total amount associated with the categoryWhether this represents partial or complete payment of the benefits payableThe type (partial, complete) of the payment. (Strength=Example)Total amount of all adjustments to this payment included in this transaction which are not related to this claim's adjudicationReason for the payment adjustmentPayment Adjustment reason codes. (Strength=Example)Estimated date the payment will be issued or the actual issue date of paymentBenefits payable less any payment adjustmentIssuer's unique identifier for the payment instrumentA number to uniquely identify a note entryThe business purpose of the note textThe presentation types of notes. (Strength=Required)The explanation or description associated with the processingA code to define the language used in the text of the noteA human language. (Strength=Preferred)A number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit orderA flag to indicate that this Coverage is to be used for adjudication of this claim when set to trueReference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information systemA business agreement number established between the provider and the insurer for special business processing purposesThe result of the adjudication of the line items for the Coverage specified in this insuranceThe sequence number of the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structureThe sequence number of the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structureThe sequence number of the sub-detail within the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structureAn error code, from a specified code system, which details why the claim could not be adjudicatedThe adjudication error codes. (Strength=Example)If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this itemThe adjudication resultsThe adjudication resultsA sub-detail adjudication of a simple product or serviceA claim detail. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsA claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-detailsThe adjudication resultsThe adjudication resultsThe adjudication resultsThe third-tier service adjudications for payor added servicesThe second-tier service adjudications for payor added servicesThe first-tier service adjudications for payor added product or service linesThe adjudication results which are presented at the header level rather than at the line-item or add-item levelsCategorized monetary totals for the adjudicationPayment details for the adjudication of the claimA note that describes or explains adjudication results in a human readable formFinancial instruments for reimbursement for the health care products and services specified on the claimErrors encountered during the processing of the adjudication

> Source: https://hl7.org/fhir/R4/claimresponse.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/claimresponse.html) [R4B](http://hl7.org/fhir/R4B/claimresponse.html) **R4** [R3](http://hl7.org/fhir/STU3/claimresponse.html) [R2](http://hl7.org/fhir/DSTU2/claimresponse.html)
 

# 13.7 Resource ClaimResponse - Content [
](claimresponse.html#13.7)

| [Financial Management ](http://www.hl7.org/Special/committees/fm/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html) | |

This resource provides the adjudication details from the processing of a Claim resource.

## 13.7.1 Scope and Usage [
](claimresponse.html#scope)

The ClaimResponse resource provides application level adjudication results, or an application level error,
 which are the result of processing a submitted Claim resource where that Claim may be the functional corollary of 
 a Claim, Predetermination or a Preauthorization.This resource is the only appropriate response to a Claim which a
 processing system recognizes as a Claim resource.
 

 

 This is the adjudicated response to a Claim, Predetermination or Preauthorization. The strength 
 of the payment aspect of the response is matching to the strength of the original request. For a 
 Claim the adjudication indicates payment which is intended to be made. For Preauthorization no payment will
 actually be made however funds may be reserved to settle a claim submitted later. For 
 Predetermination no payment will actually be made and no assurance is given that the adjudication of a claim submitted later will
 match the adjudication provided, for example funds may have been exhausted in the interim. 
 Only an actual claim may be expected to result in actual payment.
 

The ClaimResponse resource may also be returned with the response for the submission of: Re-adjudication and Reversals.

The ClaimResponse resource is an "event" resource from a FHIR workflow perspective - see [Workflow Event.](workflow.html#event)

### 13.7.1.1 Additional Information [
](claimresponse.html#13.7.1.1)

Additional information regarding electronic claims content and usage may be found at:

 

- [Financial Resource Status Lifecycle](financial-module.html#resource-status): how .status is used in the financial resources.

- [Secondary Use of Resources](financial-module.html#secondary-use): how resources such as Claim, ClaimResponse and ExplanationOfBenefit 
may be used for 
 reporting and data exchange for analytics, not just for eClaims exchange between providers and payors.

- [Subrogation](financial-module.html#subrogation): how eClaims may handle patient insurance coverages when another insurer rather than 
the provider will settle the claim and potentially recover costs against specified coverages.

- [Coordination of Benefit](financial-module.html#cob): how eClaims may handle multiple patient insurance coverages.

- [RealTime Exchange and Obtaining Deferred Responsess](financial-module.html#real-time): ClaimResponses may be obtained using Polling or FHIR REST (SEARCH).

- [Attachments and Supporting Information](financial-module.html#attachments): how eClaims may handle the provision of supporting
 information, whether provided by content or reference, within the eClaim resource when submitted to the payor or later in a resource which refers
 to the subject eClaim resource. This also includes how payors may request additional supporting information from providers.

 
 

 
 
## 13.7.2 Boundaries and Relationships [
](claimresponse.html#bnr)

 The ClaimResponse resource is used to provide the results of the adjudication and/or authorization of a set of healthcare-related
 products and services for a patient against the patient's insurance coverages, or to respond with what the adjudication would be for
 a supplied set of products or services should they be actually supplied to the patient.
 

 
The [ExplanationOfBenefit](explanationofbenefit.html) resource is for reporting out to patients or transferring data to patient centered applications, such as patient
 health Record (PHR) application, the [ExplanationOfBenefit](explanationofbenefit.html) 
 should be used instead of the [Claim](claim.html) and [ClaimResponse](claimresponse.html) resources as those
 resources may contain provider and payer specific information which is not appropriate for sharing with the patient.
 
 
When using the resources for reporting and transferring claims data, which may have originated in some standard other than FHIR, the Claim resource is useful if only the
 request side of the information exchange is of interest. If, however, both the request and the adjudication information is to be reported then the 
 [ExplanationOfBenefit](explanationofbenefit.html) should be used instead.
 

 
 
When responding whether the patient's coverage is inforce, whether it is valid at this or a specified date, or returning
 the benefit details or preauthorization requirements associated with a coverage 
 [CoverageEligibilityResponse](coverageeligibilityresponse.html) should be used instead and be the response to a
 [CoverageEligibilityRequest](coverageeligibilityrequest.html).
 

 **The eClaim domain includes a number of related resources**

 

 | 
 ClaimResponse | 
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
 
 | 
 [Claim](claim.html) | 
 A suite of goods and services and insurances coverages under which adjudication or authorization is requested. | 
 |

 | 
 [CoverageEligibilityResponse](coverageeligibilityresponse.html) | 
 The response to a request to a payor, a [CoverageEligibilityRequest](coverageeligibilityrequest.html),
 to: ascertain whether a coverage is in-force at the current or at a specified time; list the table of benefits;
 determine whether coverage is provided for specified categories or specific services; and whether preauthorization is required, and if so
 what supporting information would be required. | 
 |

 

 

 

This resource is referenced by [Claim](claim.html#Claim), itself, [DeviceRequest](devicerequest.html#DeviceRequest), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [MedicationRequest](medicationrequest.html#MedicationRequest), [ServiceRequest](servicerequest.html#ServiceRequest) and [Task](task.html#Task)

## 13.7.3 
Resource Content
 [
](claimresponse.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [ClaimResponse](claimresponse-definitions.html#ClaimResponse) | [TU](versions.html#std-process) | | [DomainResource](domainresource.html) | Response to a claim predetermination or preauthorization**Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](claimresponse-definitions.html#ClaimResponse.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for a claim response
 | |

| [status](claimresponse-definitions.html#ClaimResponse.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | active | cancelled | draft | entered-in-error
[Financial Resource Status Codes](valueset-fm-status.html) ([Required](terminologies.html#required)) | |

| [type](claimresponse-definitions.html#ClaimResponse.type) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | More granular claim type
[Claim Type Codes](valueset-claim-type.html) ([Extensible](terminologies.html#extensible)) | |

| [subType](claimresponse-definitions.html#ClaimResponse.subType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | More granular claim type
[Example Claim SubType Codes](valueset-claim-subtype.html) ([Example](terminologies.html#example)) | |

| [use](claimresponse-definitions.html#ClaimResponse.use) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | claim | preauthorization | predetermination
[Use](valueset-claim-use.html) ([Required](terminologies.html#required)) | |

| [patient](claimresponse-definitions.html#ClaimResponse.patient) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | The recipient of the products and services | |

| [created](claimresponse-definitions.html#ClaimResponse.created) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [dateTime](datatypes.html#dateTime) | Response creation date | |

| [insurer](claimresponse-definitions.html#ClaimResponse.insurer) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Party responsible for reimbursement | |

| [requestor](claimresponse-definitions.html#ClaimResponse.requestor) | | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Party responsible for the claim | |

| [request](claimresponse-definitions.html#ClaimResponse.request) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Claim](claim.html)) | Id of resource triggering adjudication | |

| [outcome](claimresponse-definitions.html#ClaimResponse.outcome) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | queued | complete | error | partial
[Claim Processing Codes](valueset-remittance-outcome.html) ([Required](terminologies.html#required)) | |

| [disposition](claimresponse-definitions.html#ClaimResponse.disposition) | | 0..1 | [string](datatypes.html#string) | Disposition Message | |

| [preAuthRef](claimresponse-definitions.html#ClaimResponse.preAuthRef) | | 0..1 | [string](datatypes.html#string) | Preauthorization reference | |

| [preAuthPeriod](claimresponse-definitions.html#ClaimResponse.preAuthPeriod) | | 0..1 | [Period](datatypes.html#Period) | Preauthorization reference effective period | |

| [payeeType](claimresponse-definitions.html#ClaimResponse.payeeType) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Party to be paid any benefits payable
[PayeeType](valueset-payeetype.html) ([Example](terminologies.html#example)) | |

| [item](claimresponse-definitions.html#ClaimResponse.item) | | 0..* | [BackboneElement](backboneelement.html) | Adjudication for claim line items
 | |

| [itemSequence](claimresponse-definitions.html#ClaimResponse.item.itemSequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Claim item instance identifier | |

| [noteNumber](claimresponse-definitions.html#ClaimResponse.item.noteNumber) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable note numbers
 | |

| [adjudication](claimresponse-definitions.html#ClaimResponse.item.adjudication) | | 1..* | [BackboneElement](backboneelement.html) | Adjudication details
 | |

| [category](claimresponse-definitions.html#ClaimResponse.item.adjudication.category) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of adjudication information
[Adjudication Value Codes](valueset-adjudication.html) ([Example](terminologies.html#example)) | |

| [reason](claimresponse-definitions.html#ClaimResponse.item.adjudication.reason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Explanation of adjudication outcome
[Adjudication Reason Codes](valueset-adjudication-reason.html) ([Example](terminologies.html#example)) | |

| [amount](claimresponse-definitions.html#ClaimResponse.item.adjudication.amount) | | 0..1 | [Money](datatypes.html#Money) | Monetary amount | |

| [value](claimresponse-definitions.html#ClaimResponse.item.adjudication.value) | | 0..1 | [decimal](datatypes.html#decimal) | Non-monetary value | |

| [detail](claimresponse-definitions.html#ClaimResponse.item.detail) | | 0..* | [BackboneElement](backboneelement.html) | Adjudication for claim details
 | |

| [detailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.detailSequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Claim detail instance identifier | |

| [noteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.noteNumber) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable note numbers
 | |

| [adjudication](claimresponse-definitions.html#ClaimResponse.item.detail.adjudication) | | 1..* | see [adjudication](#ClaimResponse.item.adjudication) | Detail level adjudication details
 | |

| [subDetail](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail) | | 0..* | [BackboneElement](backboneelement.html) | Adjudication for claim sub-details
 | |

| [subDetailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.subDetailSequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Claim sub-detail instance identifier | |

| [noteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.noteNumber) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable note numbers
 | |

| [adjudication](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.adjudication) | | 0..* | see [adjudication](#ClaimResponse.item.adjudication) | Subdetail level adjudication details
 | |

| [addItem](claimresponse-definitions.html#ClaimResponse.addItem) | | 0..* | [BackboneElement](backboneelement.html) | Insurer added line items
 | |

| [itemSequence](claimresponse-definitions.html#ClaimResponse.addItem.itemSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Item sequence number
 | |

| [detailSequence](claimresponse-definitions.html#ClaimResponse.addItem.detailSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Detail sequence number
 | |

| [subdetailSequence](claimresponse-definitions.html#ClaimResponse.addItem.subdetailSequence) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Subdetail sequence number
 | |

| [provider](claimresponse-definitions.html#ClaimResponse.addItem.provider) | | 0..* | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html)) | Authorized providers
 | |

| [productOrService](claimresponse-definitions.html#ClaimResponse.addItem.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claimresponse-definitions.html#ClaimResponse.addItem.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Service/Product billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [programCode](claimresponse-definitions.html#ClaimResponse.addItem.programCode) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Program the product or service is provided under
[Example Program Reason Codes](valueset-ex-program-code.html) ([Example](terminologies.html#example))
 | |

| [serviced[x]](claimresponse-definitions.html#ClaimResponse.addItem.serviced_x_) | | 0..1 | | Date or dates of service or product delivery | |

| servicedDate | | | [date](datatypes.html#date) | | |

| servicedPeriod | | | [Period](datatypes.html#Period) | | |

| [location[x]](claimresponse-definitions.html#ClaimResponse.addItem.location_x_) | | 0..1 | | Place of service or where product was supplied
[Example Service Place Codes](valueset-service-place.html) ([Example](terminologies.html#example)) | |

| locationCodeableConcept | | | [CodeableConcept](datatypes.html#CodeableConcept) | | |

| locationAddress | | | [Address](datatypes.html#Address) | | |

| locationReference | | | [Reference](references.html#Reference)([Location](location.html)) | | |

| [quantity](claimresponse-definitions.html#ClaimResponse.addItem.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claimresponse-definitions.html#ClaimResponse.addItem.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claimresponse-definitions.html#ClaimResponse.addItem.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [bodySite](claimresponse-definitions.html#ClaimResponse.addItem.bodySite) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical location
[Oral Site Codes](valueset-tooth.html) ([Example](terminologies.html#example)) | |

| [subSite](claimresponse-definitions.html#ClaimResponse.addItem.subSite) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Anatomical sub-location
[Surface Codes](valueset-surface.html) ([Example](terminologies.html#example))
 | |

| [noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.noteNumber) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable note numbers
 | |

| [adjudication](claimresponse-definitions.html#ClaimResponse.addItem.adjudication) | | 1..* | see [adjudication](#ClaimResponse.item.adjudication) | Added items adjudication
 | |

| [detail](claimresponse-definitions.html#ClaimResponse.addItem.detail) | | 0..* | [BackboneElement](backboneelement.html) | Insurer added line details
 | |

| [productOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Service/Product billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [quantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claimresponse-definitions.html#ClaimResponse.addItem.detail.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claimresponse-definitions.html#ClaimResponse.addItem.detail.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.noteNumber) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable note numbers
 | |

| [adjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.adjudication) | | 1..* | see [adjudication](#ClaimResponse.item.adjudication) | Added items detail adjudication
 | |

| [subDetail](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail) | | 0..* | [BackboneElement](backboneelement.html) | Insurer added line items
 | |

| [productOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.productOrService) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Billing, service, product, or drug code
[USCLS Codes](valueset-service-uscls.html) ([Example](terminologies.html#example)) | |

| [modifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.modifier) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Service/Product billing modifiers
[Modifier type Codes](valueset-claim-modifiers.html) ([Example](terminologies.html#example))
 | |

| [quantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.quantity) | | 0..1 | [SimpleQuantity](datatypes.html#SimpleQuantity) | Count of products or services | |

| [unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.unitPrice) | | 0..1 | [Money](datatypes.html#Money) | Fee, charge or cost per item | |

| [factor](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.factor) | | 0..1 | [decimal](datatypes.html#decimal) | Price scaling factor | |

| [net](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.net) | | 0..1 | [Money](datatypes.html#Money) | Total item cost | |

| [noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.noteNumber) | | 0..* | [positiveInt](datatypes.html#positiveInt) | Applicable note numbers
 | |

| [adjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.adjudication) | | 1..* | see [adjudication](#ClaimResponse.item.adjudication) | Added items detail adjudication
 | |

| [adjudication](claimresponse-definitions.html#ClaimResponse.adjudication) | | 0..* | see [adjudication](#ClaimResponse.item.adjudication) | Header-level adjudication
 | |

| [total](claimresponse-definitions.html#ClaimResponse.total) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [BackboneElement](backboneelement.html) | Adjudication totals
 | |

| [category](claimresponse-definitions.html#ClaimResponse.total.category) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of adjudication information
[Adjudication Value Codes](valueset-adjudication.html) ([Example](terminologies.html#example)) | |

| [amount](claimresponse-definitions.html#ClaimResponse.total.amount) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [Money](datatypes.html#Money) | Financial total for the category | |

| [payment](claimresponse-definitions.html#ClaimResponse.payment) | | 0..1 | [BackboneElement](backboneelement.html) | Payment Details | |

| [type](claimresponse-definitions.html#ClaimResponse.payment.type) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Partial or complete payment
[Example Payment Type Codes](valueset-ex-paymenttype.html) ([Example](terminologies.html#example)) | |

| [adjustment](claimresponse-definitions.html#ClaimResponse.payment.adjustment) | | 0..1 | [Money](datatypes.html#Money) | Payment adjustment for non-claim issues | |

| [adjustmentReason](claimresponse-definitions.html#ClaimResponse.payment.adjustmentReason) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Explanation for the adjustment
[Payment Adjustment Reason Codes](valueset-payment-adjustment-reason.html) ([Example](terminologies.html#example)) | |

| [date](claimresponse-definitions.html#ClaimResponse.payment.date) | | 0..1 | [date](datatypes.html#date) | Expected date of payment | |

| [amount](claimresponse-definitions.html#ClaimResponse.payment.amount) | | 1..1 | [Money](datatypes.html#Money) | Payable amount after adjustment | |

| [identifier](claimresponse-definitions.html#ClaimResponse.payment.identifier) | | 0..1 | [Identifier](datatypes.html#Identifier) | Business identifier for the payment | |

| [fundsReserve](claimresponse-definitions.html#ClaimResponse.fundsReserve) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Funds reserved status
[FundsReserve](valueset-fundsreserve.html) ([Example](terminologies.html#example)) | |

| [formCode](claimresponse-definitions.html#ClaimResponse.formCode) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Printed form identifier
[Forms](valueset-forms.html) ([Example](terminologies.html#example)) | |

| [form](claimresponse-definitions.html#ClaimResponse.form) | | 0..1 | [Attachment](datatypes.html#Attachment) | Printed reference or actual form | |

| [processNote](claimresponse-definitions.html#ClaimResponse.processNote) | | 0..* | [BackboneElement](backboneelement.html) | Note concerning adjudication
 | |

| [number](claimresponse-definitions.html#ClaimResponse.processNote.number) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Note instance identifier | |

| [type](claimresponse-definitions.html#ClaimResponse.processNote.type) | | 0..1 | [code](datatypes.html#code) | display | print | printoper
[NoteType](valueset-note-type.html) ([Required](terminologies.html#required)) | |

| [text](claimresponse-definitions.html#ClaimResponse.processNote.text) | | 1..1 | [string](datatypes.html#string) | Note explanatory text | |

| [language](claimresponse-definitions.html#ClaimResponse.processNote.language) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Language of the text
[Common Languages](valueset-languages.html) ([Preferred](terminologies.html#preferred) but limited to [AllLanguages](valueset-all-languages.html)) | |

| [communicationRequest](claimresponse-definitions.html#ClaimResponse.communicationRequest) | | 0..* | [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html)) | Request for additional information
 | |

| [insurance](claimresponse-definitions.html#ClaimResponse.insurance) | | 0..* | [BackboneElement](backboneelement.html) | Patient insurance information
 | |

| [sequence](claimresponse-definitions.html#ClaimResponse.insurance.sequence) | | 1..1 | [positiveInt](datatypes.html#positiveInt) | Insurance instance identifier | |

| [focal](claimresponse-definitions.html#ClaimResponse.insurance.focal) | | 1..1 | [boolean](datatypes.html#boolean) | Coverage to be used for adjudication | |

| [coverage](claimresponse-definitions.html#ClaimResponse.insurance.coverage) | | 1..1 | [Reference](references.html#Reference)([Coverage](coverage.html)) | Insurance information | |

| [businessArrangement](claimresponse-definitions.html#ClaimResponse.insurance.businessArrangement) | | 0..1 | [string](datatypes.html#string) | Additional provider contract number | |

| [claimResponse](claimresponse-definitions.html#ClaimResponse.insurance.claimResponse) | | 0..1 | [Reference](references.html#Reference)([ClaimResponse](claimresponse.html)) | Adjudication results | |

| [error](claimresponse-definitions.html#ClaimResponse.error) | | 0..* | [BackboneElement](backboneelement.html) | Processing errors
 | |

| [itemSequence](claimresponse-definitions.html#ClaimResponse.error.itemSequence) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Item sequence number | |

| [detailSequence](claimresponse-definitions.html#ClaimResponse.error.detailSequence) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Detail sequence number | |

| [subDetailSequence](claimresponse-definitions.html#ClaimResponse.error.subDetailSequence) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | Subdetail sequence number | |

| [code](claimresponse-definitions.html#ClaimResponse.error.code) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Error code detailing processing issues
[AdjudicationError](valueset-adjudication-error.html) ([Example](terminologies.html#example)) | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - ClaimResponse ([DomainResource](domainresource.html))[A unique identifier assigned to this claim responseidentifier](claimresponse-definitions.html#ClaimResponse.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The status of the resource instance (this element modifies the meaning of other elements)status](claimresponse-definitions.html#ClaimResponse.status) : [code](datatypes.html#code) [1..1] « [A code specifying the state of the resource instance. (Strength=Required)FinancialResourceStatusCodes](valueset-fm-status.html)! »[A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty servicetype](claimresponse-definitions.html#ClaimResponse.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The type or discipline-style of the claim. (Strength=Extensible)ClaimTypeCodes](valueset-claim-type.html)+ »[A finer grained suite of claim type codes which may convey additional information such as Inpatient vs Outpatient and/or a specialty servicesubType](claimresponse-definitions.html#ClaimResponse.subType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A more granular claim typecode. (Strength=Example)ExampleClaimSubTypeCodes](valueset-claim-subtype.html)?? »[A code to indicate whether the nature of the request is: to request adjudication of products and services previously rendered; or requesting authorization and adjudication for provision in the future; or requesting the non-binding adjudication of the listed products and services which could be provided in the futureuse](claimresponse-definitions.html#ClaimResponse.use) : [code](datatypes.html#code) [1..1] « [Claim, preauthorization, predetermination. (Strength=Required)Use](valueset-claim-use.html)! »[The party to whom the professional services and/or products have been supplied or are being considered and for whom actual for facast reimbursement is soughtpatient](claimresponse-definitions.html#ClaimResponse.patient) : [Reference](references.html#Reference) [1..1] « [Patient](patient.html#Patient) »[The date this resource was createdcreated](claimresponse-definitions.html#ClaimResponse.created) : [dateTime](datatypes.html#dateTime) [1..1][The party responsible for authorization, adjudication and reimbursementinsurer](claimresponse-definitions.html#ClaimResponse.insurer) : [Reference](references.html#Reference) [1..1] « [Organization](organization.html#Organization) »[The provider which is responsible for the claim, predetermination or preauthorizationrequestor](claimresponse-definitions.html#ClaimResponse.requestor) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[Original request resource referencerequest](claimresponse-definitions.html#ClaimResponse.request) : [Reference](references.html#Reference) [0..1] « [Claim](claim.html#Claim) »[The outcome of the claim, predetermination, or preauthorization processingoutcome](claimresponse-definitions.html#ClaimResponse.outcome) : [code](datatypes.html#code) [1..1] « [The result of the claim processing. (Strength=Required)ClaimProcessingCodes](valueset-remittance-outcome.html)! »[A human readable description of the status of the adjudicationdisposition](claimresponse-definitions.html#ClaimResponse.disposition) : [string](datatypes.html#string) [0..1][Reference from the Insurer which is used in later communications which refers to this adjudicationpreAuthRef](claimresponse-definitions.html#ClaimResponse.preAuthRef) : [string](datatypes.html#string) [0..1][The time frame during which this authorization is effectivepreAuthPeriod](claimresponse-definitions.html#ClaimResponse.preAuthPeriod) : [Period](datatypes.html#Period) [0..1][Type of Party to be reimbursed: subscriber, provider, otherpayeeType](claimresponse-definitions.html#ClaimResponse.payeeType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A code for the party to be reimbursed. (Strength=Example)Claim Payee Type ](valueset-payeetype.html)?? »[A code, used only on a response to a preauthorization, to indicate whether the benefits payable have been reserved and for whomfundsReserve](claimresponse-definitions.html#ClaimResponse.fundsReserve) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [For whom funds are to be reserved: (Patient, Provider, None). (Strength=Example)Funds Reservation ](valueset-fundsreserve.html)?? »[A code for the form to be used for printing the contentformCode](claimresponse-definitions.html#ClaimResponse.formCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The forms codes. (Strength=Example)Form ](valueset-forms.html)?? »[The actual form, by reference or inclusion, for printing the content or an EOBform](claimresponse-definitions.html#ClaimResponse.form) : [Attachment](datatypes.html#Attachment) [0..1][Request for additional supporting or authorizing informationcommunicationRequest](claimresponse-definitions.html#ClaimResponse.communicationRequest) : [Reference](references.html#Reference) [0..*] « [CommunicationRequest](communicationrequest.html#CommunicationRequest) »Item[A number to uniquely reference the claim item entriesitemSequence](claimresponse-definitions.html#ClaimResponse.item.itemSequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The numbers associated with notes below which apply to the adjudication of this itemnoteNumber](claimresponse-definitions.html#ClaimResponse.item.noteNumber) : [positiveInt](datatypes.html#positiveInt) [0..*]Adjudication[A code to indicate the information type of this adjudication record. Information types may include the value submitted, maximum values or percentages allowed or payable under the plan, amounts that: the patient is responsible for in aggregate or pertaining to this item; amounts paid by other coverages; and, the benefit payable for this itemcategory](claimresponse-definitions.html#ClaimResponse.item.adjudication.category) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The adjudication codes. (Strength=Example)AdjudicationValueCodes](valueset-adjudication.html)?? »[A code supporting the understanding of the adjudication result and explaining variance from expected amountreason](claimresponse-definitions.html#ClaimResponse.item.adjudication.reason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The adjudication reason codes. (Strength=Example)AdjudicationReasonCodes](valueset-adjudication-reason.html)?? »[Monetary amount associated with the categoryamount](claimresponse-definitions.html#ClaimResponse.item.adjudication.amount) : [Money](datatypes.html#Money) [0..1][A non-monetary value associated with the category. Mutually exclusive to the amount element abovevalue](claimresponse-definitions.html#ClaimResponse.item.adjudication.value) : [decimal](datatypes.html#decimal) [0..1]ItemDetail[A number to uniquely reference the claim detail entrydetailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.detailSequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The numbers associated with notes below which apply to the adjudication of this itemnoteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.noteNumber) : [positiveInt](datatypes.html#positiveInt) [0..*]SubDetail[A number to uniquely reference the claim sub-detail entrysubDetailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.subDetailSequence) : [positiveInt](datatypes.html#positiveInt) [1..1][The numbers associated with notes below which apply to the adjudication of this itemnoteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.noteNumber) : [positiveInt](datatypes.html#positiveInt) [0..*]AddedItem[Claim items which this service line is intended to replaceitemSequence](claimresponse-definitions.html#ClaimResponse.addItem.itemSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][The sequence number of the details within the claim item which this line is intended to replacedetailSequence](claimresponse-definitions.html#ClaimResponse.addItem.detailSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][The sequence number of the sub-details within the details within the claim item which this line is intended to replacesubdetailSequence](claimresponse-definitions.html#ClaimResponse.addItem.subdetailSequence) : [positiveInt](datatypes.html#positiveInt) [0..*][The providers who are authorized for the services rendered to the patientprovider](claimresponse-definitions.html#ClaimResponse.addItem.provider) : [Reference](references.html#Reference) [0..*] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization) »[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claimresponse-definitions.html#ClaimResponse.addItem.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claimresponse-definitions.html#ClaimResponse.addItem.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[Identifies the program under which this may be recoveredprogramCode](claimresponse-definitions.html#ClaimResponse.addItem.programCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Program specific reason codes. (Strength=Example)ExampleProgramReasonCodes](valueset-ex-program-code.html)?? »[The date or dates when the service or product was supplied, performed or completedserviced[x]](claimresponse-definitions.html#ClaimResponse.addItem.serviced_x_) : [Type](formats.html#umlchoice) [0..1] « [date](datatypes.html#date)|[Period](datatypes.html#Period) »[Where the product or service was providedlocation[x]](claimresponse-definitions.html#ClaimResponse.addItem.location_x_) : [Type](formats.html#umlchoice) [0..1] « [CodeableConcept](datatypes.html#CodeableConcept)|[Address](datatypes.html#Address)|[Reference](references.html#Reference)( [Location](location.html#Location)); [Place of service: pharmacy, school, prison, etc. (Strength=Example)ExampleServicePlaceCodes](valueset-service-place.html)?? »[The number of repetitions of a service or productquantity](claimresponse-definitions.html#ClaimResponse.addItem.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claimresponse-definitions.html#ClaimResponse.addItem.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claimresponse-definitions.html#ClaimResponse.addItem.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claimresponse-definitions.html#ClaimResponse.addItem.net) : [Money](datatypes.html#Money) [0..1][Physical service site on the patient (limb, tooth, etc.)bodySite](claimresponse-definitions.html#ClaimResponse.addItem.bodySite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [The code for the teeth, quadrant, sextant and arch. (Strength=Example)OralSiteCodes](valueset-tooth.html)?? »[A region or surface of the bodySite, e.g. limb region or tooth surface(s)subSite](claimresponse-definitions.html#ClaimResponse.addItem.subSite) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The code for the tooth surface and surface combinations. (Strength=Example)SurfaceCodes](valueset-surface.html)?? »[The numbers associated with notes below which apply to the adjudication of this itemnoteNumber](claimresponse-definitions.html#ClaimResponse.addItem.noteNumber) : [positiveInt](datatypes.html#positiveInt) [0..*]AddedItemDetail[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[The number of repetitions of a service or productquantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claimresponse-definitions.html#ClaimResponse.addItem.detail.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claimresponse-definitions.html#ClaimResponse.addItem.detail.net) : [Money](datatypes.html#Money) [0..1][The numbers associated with notes below which apply to the adjudication of this itemnoteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.noteNumber) : [positiveInt](datatypes.html#positiveInt) [0..*]AddedItemSubDetail[When the value is a group code then this item collects a set of related claim details, otherwise this contains the product, service, drug or other billing code for the itemproductOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.productOrService) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [Allowable service and product codes. (Strength=Example)USCLSCodes](valueset-service-uscls.html)?? »[Item typification or modifiers codes to convey additional context for the product or servicemodifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.modifier) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. (Strength=Example)ModifierTypeCodes](valueset-claim-modifiers.html)?? »[The number of repetitions of a service or productquantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.quantity) : [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) [0..1][If the item is not a group then this is the fee for the product or service, otherwise this is the total of the fees for the details of the groupunitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.unitPrice) : [Money](datatypes.html#Money) [0..1][A real number that represents a multiplier used in determining the overall value of services delivered and/or goods received. The concept of a Factor allows for a discount or surcharge multiplier to be applied to a monetary amountfactor](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.factor) : [decimal](datatypes.html#decimal) [0..1][The quantity times the unit price for an additional service or product or chargenet](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.net) : [Money](datatypes.html#Money) [0..1][The numbers associated with notes below which apply to the adjudication of this itemnoteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.noteNumber) : [positiveInt](datatypes.html#positiveInt) [0..*]Total[A code to indicate the information type of this adjudication record. Information types may include: the value submitted, maximum values or percentages allowed or payable under the plan, amounts that the patient is responsible for in aggregate or pertaining to this item, amounts paid by other coverages, and the benefit payable for this itemcategory](claimresponse-definitions.html#ClaimResponse.total.category) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The adjudication codes. (Strength=Example)AdjudicationValueCodes](valueset-adjudication.html)?? »[Monetary total amount associated with the categoryamount](claimresponse-definitions.html#ClaimResponse.total.amount) : [Money](datatypes.html#Money) [1..1]Payment[Whether this represents partial or complete payment of the benefits payabletype](claimresponse-definitions.html#ClaimResponse.payment.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The type (partial, complete) of the payment. (Strength=Example)ExamplePaymentTypeCodes](valueset-ex-paymenttype.html)?? »[Total amount of all adjustments to this payment included in this transaction which are not related to this claim's adjudicationadjustment](claimresponse-definitions.html#ClaimResponse.payment.adjustment) : [Money](datatypes.html#Money) [0..1][Reason for the payment adjustmentadjustmentReason](claimresponse-definitions.html#ClaimResponse.payment.adjustmentReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Payment Adjustment reason codes. (Strength=Example)](valueset-payment-adjustment-reason.html) [PaymentAdjustmentReasonCodes](valueset-payment-adjustment-reason.html)?? »[Estimated date the payment will be issued or the actual issue date of paymentdate](claimresponse-definitions.html#ClaimResponse.payment.date) : [date](datatypes.html#date) [0..1][Benefits payable less any payment adjustmentamount](claimresponse-definitions.html#ClaimResponse.payment.amount) : [Money](datatypes.html#Money) [1..1][Issuer's unique identifier for the payment instrumentidentifier](claimresponse-definitions.html#ClaimResponse.payment.identifier) : [Identifier](datatypes.html#Identifier) [0..1]Note[A number to uniquely identify a note entrynumber](claimresponse-definitions.html#ClaimResponse.processNote.number) : [positiveInt](datatypes.html#positiveInt) [0..1][The business purpose of the note texttype](claimresponse-definitions.html#ClaimResponse.processNote.type) : [code](datatypes.html#code) [0..1] « [The presentation types of notes. (Strength=Required)NoteType](valueset-note-type.html)! »[The explanation or description associated with the processingtext](claimresponse-definitions.html#ClaimResponse.processNote.text) : [string](datatypes.html#string) [1..1][A code to define the language used in the text of the notelanguage](claimresponse-definitions.html#ClaimResponse.processNote.language) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [A human language. (Strength=Preferred)CommonLanguages](valueset-languages.html)? »Insurance[A number to uniquely identify insurance entries and provide a sequence of coverages to convey coordination of benefit ordersequence](claimresponse-definitions.html#ClaimResponse.insurance.sequence) : [positiveInt](datatypes.html#positiveInt) [1..1][A flag to indicate that this Coverage is to be used for adjudication of this claim when set to truefocal](claimresponse-definitions.html#ClaimResponse.insurance.focal) : [boolean](datatypes.html#boolean) [1..1][Reference to the insurance card level information contained in the Coverage resource. The coverage issuing insurer will use these details to locate the patient's actual coverage within the insurer's information systemcoverage](claimresponse-definitions.html#ClaimResponse.insurance.coverage) : [Reference](references.html#Reference) [1..1] « [Coverage](coverage.html#Coverage) »[A business agreement number established between the provider and the insurer for special business processing purposesbusinessArrangement](claimresponse-definitions.html#ClaimResponse.insurance.businessArrangement) : [string](datatypes.html#string) [0..1][The result of the adjudication of the line items for the Coverage specified in this insuranceclaimResponse](claimresponse-definitions.html#ClaimResponse.insurance.claimResponse) : [Reference](references.html#Reference) [0..1] « [ClaimResponse](claimresponse.html#ClaimResponse) »Error[The sequence number of the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structureitemSequence](claimresponse-definitions.html#ClaimResponse.error.itemSequence) : [positiveInt](datatypes.html#positiveInt) [0..1][The sequence number of the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structuredetailSequence](claimresponse-definitions.html#ClaimResponse.error.detailSequence) : [positiveInt](datatypes.html#positiveInt) [0..1][The sequence number of the sub-detail within the detail within the line item submitted which contains the error. This value is omitted when the error occurs outside of the item structuresubDetailSequence](claimresponse-definitions.html#ClaimResponse.error.subDetailSequence) : [positiveInt](datatypes.html#positiveInt) [0..1][An error code, from a specified code system, which details why the claim could not be adjudicatedcode](claimresponse-definitions.html#ClaimResponse.error.code) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1] « [The adjudication error codes. (Strength=Example)Adjudication Error ](valueset-adjudication-error.html)?? »
[If this item is a group then the values here are a summary of the adjudication of the detail items. If this item is a simple product or service then this is the result of the adjudication of this itemadjudication](claimresponse-definitions.html#ClaimResponse.item.adjudication)[1..*][The adjudication resultsadjudication](claimresponse-definitions.html#ClaimResponse.item.detail.adjudication)[1..*][The adjudication resultsadjudication](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.adjudication)[0..*][A sub-detail adjudication of a simple product or servicesubDetail](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail)[0..*][A claim detail. Either a simple (a product or service) or a 'group' of sub-details which are simple itemsdetail](claimresponse-definitions.html#ClaimResponse.item.detail)[0..*][A claim line. Either a simple (a product or service) or a 'group' of details which can also be a simple items or groups of sub-detailsitem](claimresponse-definitions.html#ClaimResponse.item)[0..*][The adjudication resultsadjudication](claimresponse-definitions.html#ClaimResponse.addItem.adjudication)[1..*][The adjudication resultsadjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.adjudication)[1..*][The adjudication resultsadjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.adjudication)[1..*][The third-tier service adjudications for payor added servicessubDetail](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail)[0..*][The second-tier service adjudications for payor added servicesdetail](claimresponse-definitions.html#ClaimResponse.addItem.detail)[0..*][The first-tier service adjudications for payor added product or service linesaddItem](claimresponse-definitions.html#ClaimResponse.addItem)[0..*][The adjudication results which are presented at the header level rather than at the line-item or add-item levelsadjudication](claimresponse-definitions.html#ClaimResponse.adjudication)[0..*][Categorized monetary totals for the adjudicationtotal](claimresponse-definitions.html#ClaimResponse.total)[0..*][Payment details for the adjudication of the claimpayment](claimresponse-definitions.html#ClaimResponse.payment)[0..1][A note that describes or explains adjudication results in a human readable formprocessNote](claimresponse-definitions.html#ClaimResponse.processNote)[0..*][Financial instruments for reimbursement for the health care products and services specified on the claiminsurance](claimresponse-definitions.html#ClaimResponse.insurance)[0..*][Errors encountered during the processing of the adjudicationerror](claimresponse-definitions.html#ClaimResponse.error)[0..*]
 

 

 

**XML Template**

 

 
```
http://hl7.org/fhir/ValueSet/remittance-outcome|4.0.1
```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**ClaimResponse**](claimresponse-definitions.html#ClaimResponse)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](claimresponse-definitions.html#ClaimResponse.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Business Identifier for a claim response](terminologies.html#unbound)
 "[status](claimresponse-definitions.html#ClaimResponse.status)" : "<[code](datatypes.html#code)>", // **R!** [active | cancelled | draft | entered-in-error](valueset-fm-status.html)
 "[type](claimresponse-definitions.html#ClaimResponse.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [More granular claim type](valueset-claim-type.html)
 "[subType](claimresponse-definitions.html#ClaimResponse.subType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [More granular claim type](valueset-claim-subtype.html)
 "[use](claimresponse-definitions.html#ClaimResponse.use)" : "<[code](datatypes.html#code)>", // **R!** [claim | preauthorization | predetermination](valueset-claim-use.html)
 "[patient](claimresponse-definitions.html#ClaimResponse.patient)" : { [Reference](references.html#Reference)([Patient](patient.html#Patient)) }, // **R!** [The recipient of the products and services](terminologies.html#unbound)
 "[created](claimresponse-definitions.html#ClaimResponse.created)" : "<[dateTime](datatypes.html#dateTime)>", // **R!** [Response creation date](terminologies.html#unbound)
 "[insurer](claimresponse-definitions.html#ClaimResponse.insurer)" : { [Reference](references.html#Reference)([Organization](organization.html#Organization)) }, // **R!** [Party responsible for reimbursement](terminologies.html#unbound)
 "[requestor](claimresponse-definitions.html#ClaimResponse.requestor)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }, // [Party responsible for the claim](terminologies.html#unbound)
 "[request](claimresponse-definitions.html#ClaimResponse.request)" : { [Reference](references.html#Reference)([Claim](claim.html#Claim)) }, // [Id of resource triggering adjudication](terminologies.html#unbound)
 "[outcome](claimresponse-definitions.html#ClaimResponse.outcome)" : "<[code](datatypes.html#code)>", // **R!** [queued | complete | error | partial](valueset-remittance-outcome.html)
 "[disposition](claimresponse-definitions.html#ClaimResponse.disposition)" : "<[string](datatypes.html#string)>", // [Disposition Message](terminologies.html#unbound)
 "[preAuthRef](claimresponse-definitions.html#ClaimResponse.preAuthRef)" : "<[string](datatypes.html#string)>", // [Preauthorization reference](terminologies.html#unbound)
 "[preAuthPeriod](claimresponse-definitions.html#ClaimResponse.preAuthPeriod)" : { [Period](datatypes.html#Period) }, // [Preauthorization reference effective period](terminologies.html#unbound)
 "[payeeType](claimresponse-definitions.html#ClaimResponse.payeeType)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Party to be paid any benefits payable](valueset-payeetype.html)
 "[item](claimresponse-definitions.html#ClaimResponse.item)" : [{ // [Adjudication for claim line items](terminologies.html#unbound)
 "[itemSequence](claimresponse-definitions.html#ClaimResponse.item.itemSequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Claim item instance identifier](terminologies.html#unbound)
 "[noteNumber](claimresponse-definitions.html#ClaimResponse.item.noteNumber)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable note numbers](terminologies.html#unbound)
 "[adjudication](claimresponse-definitions.html#ClaimResponse.item.adjudication)" : [{ // **R!** [Adjudication details](terminologies.html#unbound)
 "[category](claimresponse-definitions.html#ClaimResponse.item.adjudication.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Type of adjudication information](valueset-adjudication.html)
 "[reason](claimresponse-definitions.html#ClaimResponse.item.adjudication.reason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Explanation of adjudication outcome](valueset-adjudication-reason.html)
 "[amount](claimresponse-definitions.html#ClaimResponse.item.adjudication.amount)" : { [Money](datatypes.html#Money) }, // [Monetary amount](terminologies.html#unbound)
 "[value](claimresponse-definitions.html#ClaimResponse.item.adjudication.value)" : <[decimal](datatypes.html#decimal)> // [Non-monetary value](terminologies.html#unbound)
 }],
 "[detail](claimresponse-definitions.html#ClaimResponse.item.detail)" : [{ // [Adjudication for claim details](terminologies.html#unbound)
 "[detailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.detailSequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Claim detail instance identifier](terminologies.html#unbound)
 "[noteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.noteNumber)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable note numbers](terminologies.html#unbound)
 "[adjudication](claimresponse-definitions.html#ClaimResponse.item.detail.adjudication)" : [{ Content as for ClaimResponse.item.adjudication }], // **R!** [Detail level adjudication details](terminologies.html#unbound)
 "[subDetail](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail)" : [{ // [Adjudication for claim sub-details](terminologies.html#unbound)
 "[subDetailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.subDetailSequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Claim sub-detail instance identifier](terminologies.html#unbound)
 "[noteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.noteNumber)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable note numbers](terminologies.html#unbound)
 "[adjudication](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.adjudication)" : [{ Content as for ClaimResponse.item.adjudication }] // [Subdetail level adjudication details](terminologies.html#unbound)
 }]
 }]
 }],
 "[addItem](claimresponse-definitions.html#ClaimResponse.addItem)" : [{ // [Insurer added line items](terminologies.html#unbound)
 "[itemSequence](claimresponse-definitions.html#ClaimResponse.addItem.itemSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Item sequence number](terminologies.html#unbound)
 "[detailSequence](claimresponse-definitions.html#ClaimResponse.addItem.detailSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Detail sequence number](terminologies.html#unbound)
 "[subdetailSequence](claimresponse-definitions.html#ClaimResponse.addItem.subdetailSequence)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Subdetail sequence number](terminologies.html#unbound)
 "[provider](claimresponse-definitions.html#ClaimResponse.addItem.provider)" : [{ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) }], // [Authorized providers](terminologies.html#unbound)
 "[productOrService](claimresponse-definitions.html#ClaimResponse.addItem.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claimresponse-definitions.html#ClaimResponse.addItem.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Service/Product billing modifiers](valueset-claim-modifiers.html)
 "[programCode](claimresponse-definitions.html#ClaimResponse.addItem.programCode)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Program the product or service is provided under](valueset-ex-program-code.html)
 // serviced[x]: Date or dates of service or product delivery. One of these 2:
 "[servicedDate](claimresponse-definitions.html#ClaimResponse.addItem.servicedDate)" : "<[date](datatypes.html#date)>",
 "[servicedPeriod](claimresponse-definitions.html#ClaimResponse.addItem.servicedPeriod)" : { [Period](datatypes.html#Period) },
 // location[x]: Place of service or where product was supplied. One of these 3:
 "[locationCodeableConcept](claimresponse-definitions.html#ClaimResponse.addItem.locationCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) },
 "[locationAddress](claimresponse-definitions.html#ClaimResponse.addItem.locationAddress)" : { [Address](datatypes.html#Address) },
 "[locationReference](claimresponse-definitions.html#ClaimResponse.addItem.locationReference)" : { [Reference](references.html#Reference)([Location](location.html#Location)) },
 "[quantity](claimresponse-definitions.html#ClaimResponse.addItem.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claimresponse-definitions.html#ClaimResponse.addItem.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claimresponse-definitions.html#ClaimResponse.addItem.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[bodySite](claimresponse-definitions.html#ClaimResponse.addItem.bodySite)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Anatomical location](valueset-tooth.html)
 "[subSite](claimresponse-definitions.html#ClaimResponse.addItem.subSite)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Anatomical sub-location](valueset-surface.html)
 "[noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.noteNumber)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable note numbers](terminologies.html#unbound)
 "[adjudication](claimresponse-definitions.html#ClaimResponse.addItem.adjudication)" : [{ Content as for ClaimResponse.item.adjudication }], // **R!** [Added items adjudication](terminologies.html#unbound)
 "[detail](claimresponse-definitions.html#ClaimResponse.addItem.detail)" : [{ // [Insurer added line details](terminologies.html#unbound)
 "[productOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Service/Product billing modifiers](valueset-claim-modifiers.html)
 "[quantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claimresponse-definitions.html#ClaimResponse.addItem.detail.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claimresponse-definitions.html#ClaimResponse.addItem.detail.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.noteNumber)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable note numbers](terminologies.html#unbound)
 "[adjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.adjudication)" : [{ Content as for ClaimResponse.item.adjudication }], // **R!** [Added items detail adjudication](terminologies.html#unbound)
 "[subDetail](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail)" : [{ // [Insurer added line items](terminologies.html#unbound)
 "[productOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.productOrService)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Billing, service, product, or drug code](valueset-service-uscls.html)
 "[modifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.modifier)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Service/Product billing modifiers](valueset-claim-modifiers.html)
 "[quantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.quantity)" : { [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) }, // [Count of products or services](terminologies.html#unbound)
 "[unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.unitPrice)" : { [Money](datatypes.html#Money) }, // [Fee, charge or cost per item](terminologies.html#unbound)
 "[factor](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.factor)" : <[decimal](datatypes.html#decimal)>, // [Price scaling factor](terminologies.html#unbound)
 "[net](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.net)" : { [Money](datatypes.html#Money) }, // [Total item cost](terminologies.html#unbound)
 "[noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.noteNumber)" : ["<[positiveInt](datatypes.html#positiveInt)>"], // [Applicable note numbers](terminologies.html#unbound)
 "[adjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.adjudication)" : [{ Content as for ClaimResponse.item.adjudication }] // **R!** [Added items detail adjudication](terminologies.html#unbound)
 }]
 }]
 }],
 "[adjudication](claimresponse-definitions.html#ClaimResponse.adjudication)" : [{ Content as for ClaimResponse.item.adjudication }], // [Header-level adjudication](terminologies.html#unbound)
 "[total](claimresponse-definitions.html#ClaimResponse.total)" : [{ // [Adjudication totals](terminologies.html#unbound)
 "[category](claimresponse-definitions.html#ClaimResponse.total.category)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Type of adjudication information](valueset-adjudication.html)
 "[amount](claimresponse-definitions.html#ClaimResponse.total.amount)" : { [Money](datatypes.html#Money) } // **R!** [Financial total for the category](terminologies.html#unbound)
 }],
 "[payment](claimresponse-definitions.html#ClaimResponse.payment)" : { // [Payment Details](terminologies.html#unbound)
 "[type](claimresponse-definitions.html#ClaimResponse.payment.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Partial or complete payment](valueset-ex-paymenttype.html)
 "[adjustment](claimresponse-definitions.html#ClaimResponse.payment.adjustment)" : { [Money](datatypes.html#Money) }, // [Payment adjustment for non-claim issues](terminologies.html#unbound)
 "[adjustmentReason](claimresponse-definitions.html#ClaimResponse.payment.adjustmentReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Explanation for the adjustment](valueset-payment-adjustment-reason.html)
 "[date](claimresponse-definitions.html#ClaimResponse.payment.date)" : "<[date](datatypes.html#date)>", // [Expected date of payment](terminologies.html#unbound)
 "[amount](claimresponse-definitions.html#ClaimResponse.payment.amount)" : { [Money](datatypes.html#Money) }, // **R!** [Payable amount after adjustment](terminologies.html#unbound)
 "[identifier](claimresponse-definitions.html#ClaimResponse.payment.identifier)" : { [Identifier](datatypes.html#Identifier) } // [Business identifier for the payment](terminologies.html#unbound)
 },
 "[fundsReserve](claimresponse-definitions.html#ClaimResponse.fundsReserve)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Funds reserved status](valueset-fundsreserve.html)
 "[formCode](claimresponse-definitions.html#ClaimResponse.formCode)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Printed form identifier](valueset-forms.html)
 "[form](claimresponse-definitions.html#ClaimResponse.form)" : { [Attachment](datatypes.html#Attachment) }, // [Printed reference or actual form](terminologies.html#unbound)
 "[processNote](claimresponse-definitions.html#ClaimResponse.processNote)" : [{ // [Note concerning adjudication](terminologies.html#unbound)
 "[number](claimresponse-definitions.html#ClaimResponse.processNote.number)" : "<[positiveInt](datatypes.html#positiveInt)>", // [Note instance identifier](terminologies.html#unbound)
 "[type](claimresponse-definitions.html#ClaimResponse.processNote.type)" : "<[code](datatypes.html#code)>", // [display | print | printoper](valueset-note-type.html)
 "[text](claimresponse-definitions.html#ClaimResponse.processNote.text)" : "<[string](datatypes.html#string)>", // **R!** [Note explanatory text](terminologies.html#unbound)
 "[language](claimresponse-definitions.html#ClaimResponse.processNote.language)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // [Language of the text](valueset-languages.html)
 }],
 "[communicationRequest](claimresponse-definitions.html#ClaimResponse.communicationRequest)" : [{ [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) }], // [Request for additional information](terminologies.html#unbound)
 "[insurance](claimresponse-definitions.html#ClaimResponse.insurance)" : [{ // [Patient insurance information](terminologies.html#unbound)
 "[sequence](claimresponse-definitions.html#ClaimResponse.insurance.sequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // **R!** [Insurance instance identifier](terminologies.html#unbound)
 "[focal](claimresponse-definitions.html#ClaimResponse.insurance.focal)" : <[boolean](datatypes.html#boolean)>, // **R!** [Coverage to be used for adjudication](terminologies.html#unbound)
 "[coverage](claimresponse-definitions.html#ClaimResponse.insurance.coverage)" : { [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) }, // **R!** [Insurance information](terminologies.html#unbound)
 "[businessArrangement](claimresponse-definitions.html#ClaimResponse.insurance.businessArrangement)" : "<[string](datatypes.html#string)>", // [Additional provider contract number](terminologies.html#unbound)
 "[claimResponse](claimresponse-definitions.html#ClaimResponse.insurance.claimResponse)" : { [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) } // [Adjudication results](terminologies.html#unbound)
 }],
 "[error](claimresponse-definitions.html#ClaimResponse.error)" : [{ // [Processing errors](terminologies.html#unbound)
 "[itemSequence](claimresponse-definitions.html#ClaimResponse.error.itemSequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // [Item sequence number](terminologies.html#unbound)
 "[detailSequence](claimresponse-definitions.html#ClaimResponse.error.detailSequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // [Detail sequence number](terminologies.html#unbound)
 "[subDetailSequence](claimresponse-definitions.html#ClaimResponse.error.subDetailSequence)" : "<[positiveInt](datatypes.html#positiveInt)>", // [Subdetail sequence number](terminologies.html#unbound)
 "[code](claimresponse-definitions.html#ClaimResponse.error.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) } // **R!** [Error code detailing processing issues](valueset-adjudication-error.html)
 }]
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**ClaimResponse**](claimresponse-definitions.html#ClaimResponse);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[ClaimResponse.identifier](claimresponse-definitions.html#ClaimResponse.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for a claim response
 fhir:[ClaimResponse.status](claimresponse-definitions.html#ClaimResponse.status) [ [code](datatypes.html#code) ]; # 1..1 active | cancelled | draft | entered-in-error
 fhir:[ClaimResponse.type](claimresponse-definitions.html#ClaimResponse.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 More granular claim type
 fhir:[ClaimResponse.subType](claimresponse-definitions.html#ClaimResponse.subType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 More granular claim type
 fhir:[ClaimResponse.use](claimresponse-definitions.html#ClaimResponse.use) [ [code](datatypes.html#code) ]; # 1..1 claim | preauthorization | predetermination
 fhir:[ClaimResponse.patient](claimresponse-definitions.html#ClaimResponse.patient) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)) ]; # 1..1 The recipient of the products and services
 fhir:[ClaimResponse.created](claimresponse-definitions.html#ClaimResponse.created) [ [dateTime](datatypes.html#dateTime) ]; # 1..1 Response creation date
 fhir:[ClaimResponse.insurer](claimresponse-definitions.html#ClaimResponse.insurer) [ [Reference](references.html#Reference)([Organization](organization.html#Organization)) ]; # 1..1 Party responsible for reimbursement
 fhir:[ClaimResponse.requestor](claimresponse-definitions.html#ClaimResponse.requestor) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ]; # 0..1 Party responsible for the claim
 fhir:[ClaimResponse.request](claimresponse-definitions.html#ClaimResponse.request) [ [Reference](references.html#Reference)([Claim](claim.html#Claim)) ]; # 0..1 Id of resource triggering adjudication
 fhir:[ClaimResponse.outcome](claimresponse-definitions.html#ClaimResponse.outcome) [ [code](datatypes.html#code) ]; # 1..1 queued | complete | error | partial
 fhir:[ClaimResponse.disposition](claimresponse-definitions.html#ClaimResponse.disposition) [ [string](datatypes.html#string) ]; # 0..1 Disposition Message
 fhir:[ClaimResponse.preAuthRef](claimresponse-definitions.html#ClaimResponse.preAuthRef) [ [string](datatypes.html#string) ]; # 0..1 Preauthorization reference
 fhir:[ClaimResponse.preAuthPeriod](claimresponse-definitions.html#ClaimResponse.preAuthPeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Preauthorization reference effective period
 fhir:[ClaimResponse.payeeType](claimresponse-definitions.html#ClaimResponse.payeeType) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Party to be paid any benefits payable
 fhir:[ClaimResponse.item](claimresponse-definitions.html#ClaimResponse.item) [ # 0..* Adjudication for claim line items
 fhir:[ClaimResponse.item.itemSequence](claimresponse-definitions.html#ClaimResponse.item.itemSequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Claim item instance identifier
 fhir:[ClaimResponse.item.noteNumber](claimresponse-definitions.html#ClaimResponse.item.noteNumber) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable note numbers
 fhir:[ClaimResponse.item.adjudication](claimresponse-definitions.html#ClaimResponse.item.adjudication) [ # 1..* Adjudication details
 fhir:[ClaimResponse.item.adjudication.category](claimresponse-definitions.html#ClaimResponse.item.adjudication.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Type of adjudication information
 fhir:[ClaimResponse.item.adjudication.reason](claimresponse-definitions.html#ClaimResponse.item.adjudication.reason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Explanation of adjudication outcome
 fhir:[ClaimResponse.item.adjudication.amount](claimresponse-definitions.html#ClaimResponse.item.adjudication.amount) [ [Money](datatypes.html#Money) ]; # 0..1 Monetary amount
 fhir:[ClaimResponse.item.adjudication.value](claimresponse-definitions.html#ClaimResponse.item.adjudication.value) [ [decimal](datatypes.html#decimal) ]; # 0..1 Non-monetary value
 ], ...;
 fhir:[ClaimResponse.item.detail](claimresponse-definitions.html#ClaimResponse.item.detail) [ # 0..* Adjudication for claim details
 fhir:[ClaimResponse.item.detail.detailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.detailSequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Claim detail instance identifier
 fhir:[ClaimResponse.item.detail.noteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.noteNumber) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable note numbers
 fhir:[ClaimResponse.item.detail.adjudication](claimresponse-definitions.html#ClaimResponse.item.detail.adjudication) [ [See ClaimResponse.item.adjudication](#ttl-ClaimResponse.item.adjudication) ], ... ; # 1..* Detail level adjudication details
 fhir:[ClaimResponse.item.detail.subDetail](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail) [ # 0..* Adjudication for claim sub-details
 fhir:[ClaimResponse.item.detail.subDetail.subDetailSequence](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.subDetailSequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Claim sub-detail instance identifier
 fhir:[ClaimResponse.item.detail.subDetail.noteNumber](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.noteNumber) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable note numbers
 fhir:[ClaimResponse.item.detail.subDetail.adjudication](claimresponse-definitions.html#ClaimResponse.item.detail.subDetail.adjudication) [ [See ClaimResponse.item.adjudication](#ttl-ClaimResponse.item.adjudication) ], ... ; # 0..* Subdetail level adjudication details
 ], ...;
 ], ...;
 ], ...;
 fhir:[ClaimResponse.addItem](claimresponse-definitions.html#ClaimResponse.addItem) [ # 0..* Insurer added line items
 fhir:[ClaimResponse.addItem.itemSequence](claimresponse-definitions.html#ClaimResponse.addItem.itemSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Item sequence number
 fhir:[ClaimResponse.addItem.detailSequence](claimresponse-definitions.html#ClaimResponse.addItem.detailSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Detail sequence number
 fhir:[ClaimResponse.addItem.subdetailSequence](claimresponse-definitions.html#ClaimResponse.addItem.subdetailSequence) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Subdetail sequence number
 fhir:[ClaimResponse.addItem.provider](claimresponse-definitions.html#ClaimResponse.addItem.provider) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)) ], ... ; # 0..* Authorized providers
 fhir:[ClaimResponse.addItem.productOrService](claimresponse-definitions.html#ClaimResponse.addItem.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[ClaimResponse.addItem.modifier](claimresponse-definitions.html#ClaimResponse.addItem.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Service/Product billing modifiers
 fhir:[ClaimResponse.addItem.programCode](claimresponse-definitions.html#ClaimResponse.addItem.programCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Program the product or service is provided under
 # [ClaimResponse.addItem.serviced[x]](claimresponse-definitions.html#ClaimResponse.addItem.serviced[x]) : 0..1 Date or dates of service or product delivery. One of these 2
 fhir:[ClaimResponse.addItem.servicedDate](claimresponse-definitions.html#ClaimResponse.addItem.servicedDate) [ [date](datatypes.html#date) ]
 fhir:[ClaimResponse.addItem.servicedPeriod](claimresponse-definitions.html#ClaimResponse.addItem.servicedPeriod) [ [Period](datatypes.html#Period) ]
 # [ClaimResponse.addItem.location[x]](claimresponse-definitions.html#ClaimResponse.addItem.location[x]) : 0..1 Place of service or where product was supplied. One of these 3
 fhir:[ClaimResponse.addItem.locationCodeableConcept](claimresponse-definitions.html#ClaimResponse.addItem.locationCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[ClaimResponse.addItem.locationAddress](claimresponse-definitions.html#ClaimResponse.addItem.locationAddress) [ [Address](datatypes.html#Address) ]
 fhir:[ClaimResponse.addItem.locationReference](claimresponse-definitions.html#ClaimResponse.addItem.locationReference) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]
 fhir:[ClaimResponse.addItem.quantity](claimresponse-definitions.html#ClaimResponse.addItem.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[ClaimResponse.addItem.unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[ClaimResponse.addItem.factor](claimresponse-definitions.html#ClaimResponse.addItem.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[ClaimResponse.addItem.net](claimresponse-definitions.html#ClaimResponse.addItem.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[ClaimResponse.addItem.bodySite](claimresponse-definitions.html#ClaimResponse.addItem.bodySite) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Anatomical location
 fhir:[ClaimResponse.addItem.subSite](claimresponse-definitions.html#ClaimResponse.addItem.subSite) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Anatomical sub-location
 fhir:[ClaimResponse.addItem.noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.noteNumber) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable note numbers
 fhir:[ClaimResponse.addItem.adjudication](claimresponse-definitions.html#ClaimResponse.addItem.adjudication) [ [See ClaimResponse.item.adjudication](#ttl-ClaimResponse.item.adjudication) ], ... ; # 1..* Added items adjudication
 fhir:[ClaimResponse.addItem.detail](claimresponse-definitions.html#ClaimResponse.addItem.detail) [ # 0..* Insurer added line details
 fhir:[ClaimResponse.addItem.detail.productOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[ClaimResponse.addItem.detail.modifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Service/Product billing modifiers
 fhir:[ClaimResponse.addItem.detail.quantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[ClaimResponse.addItem.detail.unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[ClaimResponse.addItem.detail.factor](claimresponse-definitions.html#ClaimResponse.addItem.detail.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[ClaimResponse.addItem.detail.net](claimresponse-definitions.html#ClaimResponse.addItem.detail.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[ClaimResponse.addItem.detail.noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.noteNumber) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable note numbers
 fhir:[ClaimResponse.addItem.detail.adjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.adjudication) [ [See ClaimResponse.item.adjudication](#ttl-ClaimResponse.item.adjudication) ], ... ; # 1..* Added items detail adjudication
 fhir:[ClaimResponse.addItem.detail.subDetail](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail) [ # 0..* Insurer added line items
 fhir:[ClaimResponse.addItem.detail.subDetail.productOrService](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.productOrService) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Billing, service, product, or drug code
 fhir:[ClaimResponse.addItem.detail.subDetail.modifier](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.modifier) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Service/Product billing modifiers
 fhir:[ClaimResponse.addItem.detail.subDetail.quantity](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.quantity) [ [Quantity](datatypes.html#Quantity)([SimpleQuantity](datatypes.html#SimpleQuantity)) ]; # 0..1 Count of products or services
 fhir:[ClaimResponse.addItem.detail.subDetail.unitPrice](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.unitPrice) [ [Money](datatypes.html#Money) ]; # 0..1 Fee, charge or cost per item
 fhir:[ClaimResponse.addItem.detail.subDetail.factor](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.factor) [ [decimal](datatypes.html#decimal) ]; # 0..1 Price scaling factor
 fhir:[ClaimResponse.addItem.detail.subDetail.net](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.net) [ [Money](datatypes.html#Money) ]; # 0..1 Total item cost
 fhir:[ClaimResponse.addItem.detail.subDetail.noteNumber](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.noteNumber) [ [positiveInt](datatypes.html#positiveInt) ], ... ; # 0..* Applicable note numbers
 fhir:[ClaimResponse.addItem.detail.subDetail.adjudication](claimresponse-definitions.html#ClaimResponse.addItem.detail.subDetail.adjudication) [ [See ClaimResponse.item.adjudication](#ttl-ClaimResponse.item.adjudication) ], ... ; # 1..* Added items detail adjudication
 ], ...;
 ], ...;
 ], ...;
 fhir:[ClaimResponse.adjudication](claimresponse-definitions.html#ClaimResponse.adjudication) [ [See ClaimResponse.item.adjudication](#ttl-ClaimResponse.item.adjudication) ], ... ; # 0..* Header-level adjudication
 fhir:[ClaimResponse.total](claimresponse-definitions.html#ClaimResponse.total) [ # 0..* Adjudication totals
 fhir:[ClaimResponse.total.category](claimresponse-definitions.html#ClaimResponse.total.category) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Type of adjudication information
 fhir:[ClaimResponse.total.amount](claimresponse-definitions.html#ClaimResponse.total.amount) [ [Money](datatypes.html#Money) ]; # 1..1 Financial total for the category
 ], ...;
 fhir:[ClaimResponse.payment](claimresponse-definitions.html#ClaimResponse.payment) [ # 0..1 Payment Details
 fhir:[ClaimResponse.payment.type](claimresponse-definitions.html#ClaimResponse.payment.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Partial or complete payment
 fhir:[ClaimResponse.payment.adjustment](claimresponse-definitions.html#ClaimResponse.payment.adjustment) [ [Money](datatypes.html#Money) ]; # 0..1 Payment adjustment for non-claim issues
 fhir:[ClaimResponse.payment.adjustmentReason](claimresponse-definitions.html#ClaimResponse.payment.adjustmentReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Explanation for the adjustment
 fhir:[ClaimResponse.payment.date](claimresponse-definitions.html#ClaimResponse.payment.date) [ [date](datatypes.html#date) ]; # 0..1 Expected date of payment
 fhir:[ClaimResponse.payment.amount](claimresponse-definitions.html#ClaimResponse.payment.amount) [ [Money](datatypes.html#Money) ]; # 1..1 Payable amount after adjustment
 fhir:[ClaimResponse.payment.identifier](claimresponse-definitions.html#ClaimResponse.payment.identifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Business identifier for the payment
 ];
 fhir:[ClaimResponse.fundsReserve](claimresponse-definitions.html#ClaimResponse.fundsReserve) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Funds reserved status
 fhir:[ClaimResponse.formCode](claimresponse-definitions.html#ClaimResponse.formCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Printed form identifier
 fhir:[ClaimResponse.form](claimresponse-definitions.html#ClaimResponse.form) [ [Attachment](datatypes.html#Attachment) ]; # 0..1 Printed reference or actual form
 fhir:[ClaimResponse.processNote](claimresponse-definitions.html#ClaimResponse.processNote) [ # 0..* Note concerning adjudication
 fhir:[ClaimResponse.processNote.number](claimresponse-definitions.html#ClaimResponse.processNote.number) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Note instance identifier
 fhir:[ClaimResponse.processNote.type](claimresponse-definitions.html#ClaimResponse.processNote.type) [ [code](datatypes.html#code) ]; # 0..1 display | print | printoper
 fhir:[ClaimResponse.processNote.text](claimresponse-definitions.html#ClaimResponse.processNote.text) [ [string](datatypes.html#string) ]; # 1..1 Note explanatory text
 fhir:[ClaimResponse.processNote.language](claimresponse-definitions.html#ClaimResponse.processNote.language) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Language of the text
 ], ...;
 fhir:[ClaimResponse.communicationRequest](claimresponse-definitions.html#ClaimResponse.communicationRequest) [ [Reference](references.html#Reference)([CommunicationRequest](communicationrequest.html#CommunicationRequest)) ], ... ; # 0..* Request for additional information
 fhir:[ClaimResponse.insurance](claimresponse-definitions.html#ClaimResponse.insurance) [ # 0..* Patient insurance information
 fhir:[ClaimResponse.insurance.sequence](claimresponse-definitions.html#ClaimResponse.insurance.sequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 1..1 Insurance instance identifier
 fhir:[ClaimResponse.insurance.focal](claimresponse-definitions.html#ClaimResponse.insurance.focal) [ [boolean](datatypes.html#boolean) ]; # 1..1 Coverage to be used for adjudication
 fhir:[ClaimResponse.insurance.coverage](claimresponse-definitions.html#ClaimResponse.insurance.coverage) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)) ]; # 1..1 Insurance information
 fhir:[ClaimResponse.insurance.businessArrangement](claimresponse-definitions.html#ClaimResponse.insurance.businessArrangement) [ [string](datatypes.html#string) ]; # 0..1 Additional provider contract number
 fhir:[ClaimResponse.insurance.claimResponse](claimresponse-definitions.html#ClaimResponse.insurance.claimResponse) [ [Reference](references.html#Reference)([ClaimResponse](claimresponse.html#ClaimResponse)) ]; # 0..1 Adjudication results
 ], ...;
 fhir:[ClaimResponse.error](claimresponse-definitions.html#ClaimResponse.error) [ # 0..* Processing errors
 fhir:[ClaimResponse.error.itemSequence](claimresponse-definitions.html#ClaimResponse.error.itemSequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Item sequence number
 fhir:[ClaimResponse.error.detailSequence](claimresponse-definitions.html#ClaimResponse.error.detailSequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Detail sequence number
 fhir:[ClaimResponse.error.subDetailSequence](claimresponse-definitions.html#ClaimResponse.error.subDetailSequence) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 Subdetail sequence number
 fhir:[ClaimResponse.error.code](claimresponse-definitions.html#ClaimResponse.error.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Error code detailing processing issues
 ], ...;
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [ClaimResponse](claimresponse.html#ClaimResponse)
 | 
 | 
 |

 | 
 ClaimResponse.status | 
 
 

 Min Cardinality changed from 0 to 1

 - Change value set from http://hl7.org/fhir/ValueSet/fm-status to http://hl7.org/fhir/ValueSet/fm-status|4.0.1

 

 | 
 |

 | 
 ClaimResponse.type | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ClaimResponse.subType | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.use | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ClaimResponse.patient | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.created | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.insurer | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.requestor | 
 
 

 - Renamed from requestProvider to requestor

 - Type Reference: Added Target Types PractitionerRole, Organization

 

 | 
 |

 | 
 ClaimResponse.outcome | 
 
 

 - Min Cardinality changed from 0 to 1

 - Type changed from CodeableConcept to code

 - 
Add Binding `http://hl7.org/fhir/ValueSet/remittance-outcome|4.0.1` (required)
 

 

 | 
 |

 | 
 ClaimResponse.preAuthRef | 
 
 

 - Moved from ClaimResponse.insurance to ClaimResponse

 - Max Cardinality changed from * to 1

 

 | 
 |

 | 
 ClaimResponse.preAuthPeriod | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.item.itemSequence | 
 
 

 - Renamed from sequenceLinkId to itemSequence

 

 | 
 |

 | 
 ClaimResponse.item.adjudication | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.item.detail.detailSequence | 
 
 

 - Renamed from sequenceLinkId to detailSequence

 

 | 
 |

 | 
 ClaimResponse.item.detail.adjudication | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.item.detail.subDetail.subDetailSequence | 
 
 

 - Renamed from sequenceLinkId to subDetailSequence

 

 | 
 |

 | 
 ClaimResponse.addItem.itemSequence | 
 
 

 - Renamed from sequenceLinkId to itemSequence

 

 | 
 |

 | 
 ClaimResponse.addItem.detailSequence | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.subdetailSequence | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.provider | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.addItem.programCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.serviced[x] | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.location[x] | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.quantity | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.unitPrice | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.factor | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.net | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.bodySite | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.subSite | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.adjudication | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.productOrService | 
 
 

 - Renamed from service to productOrService

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.quantity | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.unitPrice | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.factor | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.net | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.adjudication | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.productOrService | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.modifier | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.quantity | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.unitPrice | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.factor | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.net | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.noteNumber | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.subDetail.adjudication | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ClaimResponse.adjudication | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.total | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.total.category | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ClaimResponse.total.amount | 
 
 

 - 
 **Added Mandatory Element**
 

 

 | 
 |

 | 
 ClaimResponse.payment.type | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.payment.amount | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.fundsReserve | 
 
 

 - Renamed from reserved to fundsReserve

 - Type changed from Coding to CodeableConcept

 

 | 
 |

 | 
 ClaimResponse.formCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 ClaimResponse.form | 
 
 

 - Type changed from CodeableConcept to Attachment

 

 | 
 |

 | 
 ClaimResponse.processNote.type | 
 
 

 - Type changed from CodeableConcept to code

 - Change value set from http://hl7.org/fhir/ValueSet/note-type to http://hl7.org/fhir/ValueSet/note-type|4.0.1

 

 | 
 |

 | 
 ClaimResponse.processNote.text | 
 
 

 - Min Cardinality changed from 0 to 1

 

 | 
 |

 | 
 ClaimResponse.processNote.language | 
 
 

 - Change binding strength from extensible to preferred

 

 | 
 |

 | 
 ClaimResponse.error.itemSequence | 
 
 

 - Renamed from sequenceLinkId to itemSequence

 

 | 
 |

 | 
 ClaimResponse.error.detailSequence | 
 
 

 - Renamed from detailSequenceLinkId to detailSequence

 

 | 
 |

 | 
 ClaimResponse.error.subDetailSequence | 
 
 

 - Renamed from subdetailSequenceLinkId to subDetailSequence

 

 | 
 |

 | 
 ClaimResponse.requestOrganization | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.addItem.revenue | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.addItem.category | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.addItem.fee | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.revenue | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.category | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.addItem.detail.fee | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.totalCost | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.unallocDeductable | 
 
 

 - deleted

 

 | 
 |

 | 
 ClaimResponse.totalBenefit | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](claimresponse.diff.xml) or [JSON](claimresponse.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](claimresponse-version-maps.html) (status = 1 test that all execute ok. 1 fail round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](claimresponse-profiles.html) and the alternate definitions:
Master Definition [XML](claimresponse.profile.xml.html) + [JSON](claimresponse.profile.json.html),
[XML](xml.html) [Schema](claimresponse.xsd)/[Schematron](claimresponse.sch) + [JSON](json.html) 
[Schema](claimresponse.schema.json.html), [ShEx](claimresponse.shex.html) (for [Turtle](rdf.html)) + [see the extensions](claimresponse-profiles.html) & the [dependency analysis](claimresponse-dependencies.html)

### 13.7.3.1 
Terminology Bindings
 [
](claimresponse.html#tx)

 | Path | Definition | Type | Reference | |

 | ClaimResponse.status | A code specifying the state of the resource instance. | [Required](terminologies.html#required) | [FinancialResourceStatusCodes](valueset-fm-status.html) | |

 | ClaimResponse.type | The type or discipline-style of the claim. | [Extensible](terminologies.html#extensible) | [ClaimTypeCodes](valueset-claim-type.html) | |

 | ClaimResponse.subType | A more granular claim typecode. | [Example](terminologies.html#example) | [ExampleClaimSubTypeCodes](valueset-claim-subtype.html) | |

 | ClaimResponse.use | Claim, preauthorization, predetermination. | [Required](terminologies.html#required) | [Use](valueset-claim-use.html) | |

 | ClaimResponse.outcome | The result of the claim processing. | [Required](terminologies.html#required) | [ClaimProcessingCodes](valueset-remittance-outcome.html) | |

 | ClaimResponse.payeeType | A code for the party to be reimbursed. | [Example](terminologies.html#example) | [Claim Payee Type Codes](valueset-payeetype.html) | |

 | ClaimResponse.item.adjudication.category**ClaimResponse.total.category | The adjudication codes. | [Example](terminologies.html#example) | [AdjudicationValueCodes](valueset-adjudication.html) | |

 | ClaimResponse.item.adjudication.reason | The adjudication reason codes. | [Example](terminologies.html#example) | [AdjudicationReasonCodes](valueset-adjudication-reason.html) | |

 | ClaimResponse.addItem.productOrService
ClaimResponse.addItem.detail.productOrService
ClaimResponse.addItem.detail.subDetail.productOrService | Allowable service and product codes. | [Example](terminologies.html#example) | [USCLSCodes](valueset-service-uscls.html) | |

 | ClaimResponse.addItem.modifier
ClaimResponse.addItem.detail.modifier
ClaimResponse.addItem.detail.subDetail.modifier | Item type or modifiers codes, eg for Oral whether the treatment is cosmetic or associated with TMJ, or an appliance was lost or stolen. | [Example](terminologies.html#example) | [ModifierTypeCodes](valueset-claim-modifiers.html) | |

 | ClaimResponse.addItem.programCode | Program specific reason codes. | [Example](terminologies.html#example) | [ExampleProgramReasonCodes](valueset-ex-program-code.html) | |

 | ClaimResponse.addItem.location[x] | Place of service: pharmacy, school, prison, etc. | [Example](terminologies.html#example) | [ExampleServicePlaceCodes](valueset-service-place.html) | |

 | ClaimResponse.addItem.bodySite | The code for the teeth, quadrant, sextant and arch. | [Example](terminologies.html#example) | [OralSiteCodes](valueset-tooth.html) | |

 | ClaimResponse.addItem.subSite | The code for the tooth surface and surface combinations. | [Example](terminologies.html#example) | [SurfaceCodes](valueset-surface.html) | |

 | ClaimResponse.payment.type | The type (partial, complete) of the payment. | [Example](terminologies.html#example) | [ExamplePaymentTypeCodes](valueset-ex-paymenttype.html) | |

 | ClaimResponse.payment.adjustmentReason | Payment Adjustment reason codes. | [Example](terminologies.html#example) | [PaymentAdjustmentReasonCodes](valueset-payment-adjustment-reason.html) | |

 | ClaimResponse.fundsReserve | For whom funds are to be reserved: (Patient, Provider, None). | [Example](terminologies.html#example) | [Funds Reservation Codes](valueset-fundsreserve.html) | |

 | ClaimResponse.formCode | The forms codes. | [Example](terminologies.html#example) | [Form Codes](valueset-forms.html) | |

 | ClaimResponse.processNote.type | The presentation types of notes. | [Required](terminologies.html#required) | [NoteType](valueset-note-type.html) | |

 | ClaimResponse.processNote.language | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) | |

 | ClaimResponse.error.code | The adjudication error codes. | [Example](terminologies.html#example) | [Adjudication Error Codes](valueset-adjudication-error.html) | |

 

 

## 13.7.4 Search Parameters [
](claimresponse.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| Name** | **Type** | **Description** | **Expression** | **In Common** | |

| created | [date](search.html#date) | The creation date | ClaimResponse.created | | |

| disposition | [string](search.html#string) | The contents of the disposition message | ClaimResponse.disposition | | |

| identifier | [token](search.html#token) | The identity of the ClaimResponse | ClaimResponse.identifier | | |

| insurer | [reference](search.html#reference) | The organization which generated this resource | ClaimResponse.insurer
([Organization](organization.html)) | | |

| outcome | [token](search.html#token) | The processing outcome | ClaimResponse.outcome | | |

| patient | [reference](search.html#reference) | The subject of care | ClaimResponse.patient
([Patient](patient.html)) | | |

| payment-date | [date](search.html#date) | The expected payment date | ClaimResponse.payment.date | | |

| request | [reference](search.html#reference) | The claim reference | ClaimResponse.request
([Claim](claim.html)) | | |

| requestor | [reference](search.html#reference) | The Provider of the claim | ClaimResponse.requestor
([Practitioner](practitioner.html), [Organization](organization.html), [PractitionerRole](practitionerrole.html)) | | |

| status | [token](search.html#token) | The status of the ClaimResponse | ClaimResponse.status | | |

| use | [token](search.html#token) | The type of claim | ClaimResponse.use | | |