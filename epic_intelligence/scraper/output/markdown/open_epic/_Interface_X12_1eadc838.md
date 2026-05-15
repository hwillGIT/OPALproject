# open.epic :: Explore By Interface Type

> Source: https://open.epic.com/Interface/X12

---

# 
 By Interface Type

 

 

 
 

 

 
 

 
 

 
 
 

## ASC X12

 
ASC X12 standards are used for facilitating electronic interchange relating to business processes, in both healthcare and other industries. You can learn more from [ASC X12](http://www.x12.org). 

### 
 Incoming Healthcare Claim Repricing Request (X12 837)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20Incoming%20Health%20Care%20Claim%20Repricing%20Request%20-%20837.zip)

 

 

 Tapestry receives incoming claim repricing requests through ANSI ASC X12 837 transactions.
 

 

### 
 Incoming External Paid Medical Claims (X12 837)

 

 

 Loads external paid medical claims messages into Epic Payer Platform, using flat files in the 837 format.
 

 

 [Current integrations include ](#)
 

 - HUMANA

 

 

 

### 
 Incoming Pharmacy Price Sales Catalog to Willow Inventory Interface
 [read the spec](/Tech/TechSpec?spec=5337)

 

 

 Updates purchase contract records with up-to-date pricing and supplier item ID information.
 

 

 [Current integrations include ](#)
 

 - AMERISOURCE BERGEN

 - Anda

 - Auburn Pharmaceutical

 - BD

 - Cardinal Health WaveMark

 - CENCORA

 - KeySource

 - McKesson

 - Medline

 - Morris & Dickson

 - Parmed 

 - Smith Drug Company

 - Swisslog

 - TOPRX

 

 

 

### 
 Outgoing Additional Information to Support a Health Care Services Authorization
 [read the spec](/Tech/TechSpec?spec=staged%2FEpic%20005010X211%20Companion%20Guide.pdf)

 

 

 Used in conjunction with an Outgoing Authorization Request for Review - 278R, provides supporting clinical documentation for the request. Follows ANSI X12 specification 005010X211, ANSI X12 275 for Authorization, Additional Information to Support a Health Care Services Review (275)
 

 

 [Current integrations include ](#)
 

 - Aetna

 - Anthem

 - HUMANA

 - INFINX

 - Optum

 - Rhyme

 - Samaritan Health Plans

 - United Healthcare

 - VOLUWARE, INC.

 

 

 

### 
 Incoming Claim File Acknowledgment Interface – 999
 [read the spec](/Tech/TechSpec?spec=staged%2FResolute%20Incoming%20ANSI%20X12%20999%20Interface%20Specification.pdf)

 

 

 This incoming interface loads claim file acknowledgment responses using industry standard ANSI ASC X12N 999 transactions.
 

 

 [Current integrations include ](#)
 

 - BLUE CROSS AND BLUE SHIELD OF NORTH CAROLINA

 - Optum

 

 

 

### 
 Outgoing Authorization Request as Notification (X12 278R)
 [read the spec](/Tech/TechSpec?spec=staged%5CTapestry%20ANSI%20X12%20278R%20Request%20as%20Notification%20Technical%20Specifications.pdf)

 

 

 Sends authorization decisions for covered patient referrals to third-party AP claims systems using the 278R format rather than 278N. Required by Texas Medicaid.
 

 

 [Current integrations include ](#)
 

 - Texas - Public Health Agencies

 

 

 

### 
 Tapestry Incoming Marketplace Benefit Enrollment and Maintenance

 

 

 Receives eligibility information to create, term, and update Marketplace coverage information.
 

 

### 
 Tapestry Incoming Marketplace Premium Payment Information

 

 

 Receives and processes premium payments associated with Marketplace coverages in Epic
 

 

 [Current integrations include ](#)
 

 - CMS

 

 

 

### 
 Tapestry Outgoing Marketplace Benefit Enrollment and Maintenance

 

 

 Sends marketplace coverage enrollment information government agencies or other entities.
 

 

### 
 Tapestry Incoming Referral Transfer Attachment (X12 275)

 

 

 Receives electronic attachments and links them to Tapestry claims.
 

 

### 
 Incoming Additional Information to Support a Health Care Services Review - 275

 

 

 Used in conjunction with an Incoming Referral Request for Review - 278R, provides supporting documents for the referral request. Follows ANSI X12 Specification 005010X211, ANSI X12 275 for Authorization, Additional Information to Support a Health Care Services Review.
 

 

 [Current integrations include ](#)
 

 - Johns Hopkins HealthCare LLC

 

 

 

### 
 Outgoing Additional Information for Health Care Claim (X12 275)

 

 

 Sends additional information to support a Healthcare Claim from Epic's billing module, Resolute
 

 

 [Current integrations include ](#)
 

 - AVAILITY

 - Blue Cross Blue Shield of Massachusetts

 - Cirius

 - EXPERIAN HEALTH, INC.

 - FinThrive

 - Healthcare IP

 - Optum

 - Trubridge

 - Waystar

 

 

 

### 
 Tapestry Outgoing Healthcare Claim: Dental (X12 837)

 

 

 Sends dental claim information to payers. The 837 transmits claim information either for the purpose of payment, such as a provider sending a bill to a payer, or for the purpose of reporting, such as a delegated risk payer sending payment information to a health plan or the government.
 

 

### 
 Outgoing Pharmacy Purchase Order from Willow Inventory
 [read the spec](/Tech/TechSpec?spec=5261)

 

 

 Sends medication purchase order requests to a supplier. The interface uses the ANSI X12 850 transaction set or GS1 for the request.
 

 

 [Current integrations include ](#)
 

 - Alliance Healthcare

 - AMERISOURCE BERGEN

 - Anda

 - Auburn Pharmaceutical

 - AutoMed

 - Baxter

 - BD

 - Brocacef

 - Cardinal Health WaveMark

 - CENCORA

 - CenterX

 - CuraScript

 - E.Novation

 - Fagron

 - FFF Enterprises

 - Global Healthcare Exchange

 - Independent Pharmacy Distributor

 - Infor Global Solutions

 - KeySource

 - McKesson

 - Morris & Dickson

 - ORACLE

 - Parata

 - Parmed 

 - SAP

 - Smith Drug Company

 - Tecsys

 - TOPRX

 

 

 

### 
 Incoming Pharmacy Purchase Order Invoice to Willow Inventory
 [read the spec](/Tech/TechSpec?spec=5329)

 

 

 Receives invoices from a supplier for purchase orders placed in Willow Inventory, Epic's medication inventory management system. The interface uses the ANSI X12 810 transaction set for the response.
 

 

 [Current integrations include ](#)
 

 - AMERISOURCE BERGEN

 - Anda

 - Auburn Pharmaceutical

 - AutoMed

 - Baxter

 - BD

 - Cardinal Health WaveMark

 - CENCORA

 - CenterX

 - Global Healthcare Exchange

 - KeySource

 - Macro Helix

 - McKesson

 - Medline

 - Morris & Dickson

 - ORACLE

 - Parmed 

 - SAP

 - Smith Drug Company

 - SURESCRIPTS

 - TOPRX

 

 

 

### 
 Outgoing Healthcare Claim: Professional (X12 837 Batch)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20Outgoing%20Health%20Care%20Data%20Reporting%20Claims.zip)

 

 

 Sends professional claim information to payers. The 837 transmits claim information either for the purpose of payment, such as a provider sending a bill to a payer, or for the purpose of reporting, such as a delegated risk payer sending payment information to a health plan or the government.
 

 

 [Current integrations include ](#)
 

 - Change Healthcare

 - Gateway

 - McKesson

 - Santa Clara County (CA) - Public Health Agencies

 - Texas Medicaid & Healthcare Partnership

 

 

 

### 
 Incoming Healthcare Claim: Professional (X12 837)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20Health%20Care%20Claims%20-%20Incoming%20837.zip)

 

 

 Tapestry receives incoming professional, institutional, or dental claims through ANSI ASC X12 837 transactions. Standard version is batch with a real time option in upcoming version.
 

 

 [Current integrations include ](#)
 

 - Amisys Synertech Inc

 - AVAILITY

 - Change Healthcare

 - CMS

 - DSG (Data Systems Group)

 - Humata Health

 - McKesson

 - Optum

 - Oscar Insurance

 - Relay Health

 - Smart Data Solutions

 - Waystar

 

 

 

### 
 Outgoing Healthcare Claim Payment/Advice (X12 835)
 [read the spec](/Tech/TechSpec?spec=5157)

 

 

 Sends claim payment and remittance information to health care providers. The 835 lets providers know which claims are paid and whether there is any difference between the payment amount and the billed amount. This is a batch interface, with a real time option available in an upcoming version.
 

 

 [Current integrations include ](#)
 

 - DSG (Data Systems Group)

 - McKesson

 - Utah - Public Health Agencies

 

 

 

### 
 Incoming Benefit Enrollment and Maintenance (X12 834)
 [read the spec](/Tech/TechSpec?spec=5175)

 

 

 Receives enrollment information from employers or other sponsors of coverage. Health plans and employers send 834s to inform a payer about members who are being enrolled in the payer's insurance plan or for whom the payer is otherwise taking on risk.
 

 

### 
 Incoming Claim Status Inquiry (X12 276/277)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20Health%20Care%20Claim%20Status%20-%20Incoming%20276%20277.zip)

 

 

 Receives requests from health care providers for status information about claims, including whether the claim was paid or unpaid and why. Tapestry supports the batch interface by default, with a real-time interface available. Returns response (X12 277).
 

 

### 
 Incoming Payment Order/Remittance Advice (X12 820 Batch)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20ANSI%20X12%20820%20Interface%20Specification%20-%20Third%20Party%20Implementation%20Guide.pdf)

 

 

 Receives payment and remittance information. Tapestry supports an incoming 820 for the purpose of posting payment information against premium billing accounts.
 

 

### 
 Outgoing Benefit Enrollment and Maintenance (X12 834)
 [read the spec](/Tech/TechSpec?spec=5167)

 

 

 Sends enrollment information to health plans, government agencies, or other entities. Payers send 834s for reporting purposes to list all members for whom they have taken on risk.
 

 

 [Current integrations include ](#)
 

 - MedImpact

 - Navitus

 

 

 

### 
 Incoming Eligibility Verification Query (X12 270/271)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20Eligibility%2C%20Coverage%2C%20or%20Benefit%20Inquiry%20-%20Incoming%20270%20271.zip)

 

 

 Receives requests from health care providers for member eligibility and benefits information in the form of a 270, and sends a response in the form of a 271. This is a real-time interface.
 

 

 [Current integrations include ](#)
 

 - AVAILITY

 - Change Healthcare

 - HDX

 - Post-n-track

 - Relay Health

 - TransUnion

 

 

 

### 
 Incoming Referral Request for Review (X12 278R)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20ANSI%20X12%20278R%20Request%20for%20Review%20Technical%20Specification.zip)

 

 

 Receives a referral request from a provider or provider group so that Epic's managed care system can perform utilization management and approve or deny the service request. A response message is sent to inform the provider of the authorization decision.
 

 

 [Current integrations include ](#)
 

 - Johns Hopkins HealthCare LLC

 

 

 

### 
 Outgoing Unsolcited Healthcare Claim Pending Status Notification (X12 277P)
 [read the spec](/Tech/TechSpec?spec=%2Fstaged%2FTapestry%20ANSI%20X12%20Outgoing%20277P%20Interface%20Specification%20-%20Third%20Party%20Implementation%20Guide.pdf)

 

 

 Sends information to a health care provider about the status of all non-finalized claims received from that provider. The 277P is an unsolicited message that is similar to the 277 response to the 276. It is sent so that the provider doesn't have to continually send 276 requests to the payer.
 

 

 [Current integrations include ](#)
 

 - 3M

 

 

 

### 
 Incoming Authorization Notification (X12 278N)
 [read the spec](/Tech/TechSpec?spec=staged%2FTapestry%20ANSI%20X12%20278%20Incoming%20Notification%20Technical%20Specification.zip)

 

 

 Receives unsolicited, completed referral information (usually with authorization numbers) from an external utilization management system so that Epic' Managed Care system can pay Accounts Payable (AP) claims. Sends an acknowledgment of the receipt of the information (or errors if any occur during message processing).
 

 

 [Current integrations include ](#)
 

 - Cigna

 - Evicore

 - Johns Hopkins HealthCare LLC

 - Magellan

 

 

 

### 
 Tapestry Incoming Referral Transfer Attachment (X12 275)

 

 

 Receives electronic attachments and links them to claims in Epic's managed care product, Tapestry.
 

 

 [Current integrations include ](#)
 

 - MGC Diagnostics

 

 

 

### 
 Outgoing Eligibility Verification Query (X12 270/271)
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Eligibility%20Verification%20Query%20-%20270_271%20%28Bidirectional%29%20Interface%20Technical%20Specification.pdf)

 

 

 Used to verify eligibility with clearinghouses and payers. Uses ANSI X12 270/271 transactions.
 

 

 [Current integrations include ](#)
 

 - 3M

 - AccuMed

 - AccuReg

 - AMERISOURCE BERGEN

 - Arizona - Public Health Agencies

 - ATHENAHEALTH, INC.

 - AVAILITY

 - CareSource

 - Change Healthcare

 - Cigna

 - Clinical Computer Systems, Inc.

 - CMS

 - Conifer Health Solutions

 - DECOS

 - E-Insights

 - EXPERIAN HEALTH, INC.

 - ezVerify

 - FinThrive

 - HDX

 - Health Resources and Services Administration

 - Healthcare IP

 - HealthNautica

 - Helfo

 - Highmark

 - Humata Health

 - Inland Empire Health Plan

 - INOVALON, INC.

 - InstaMed, a J.P. Morgan Company

 - Jorie AI

 - Loxogon

 - MaxRTE

 - MEDEANALYTICS

 - Medicaid

 - Moda

 - MULESOFT, INC.

 - Navicure

 - NEBO

 - NEHEN

 - Ontario Ministry of Health

 - Optum

 - Pelitas

 - Post-n-track

 - Presbyterian Health Plans

 - Quadax

 - RealMed

 - Recondo

 - REDOX

 - Relay Health

 - Rycan

 - Signify Health

 - SURESCRIPTS

 - The Advisory Board

 - The SSI Group

 - TransUnion

 - TriZetto Provider Solutions, a Cognizant Company

 - United Healthcare

 - VisionShare

 - Waystar

 - WNY HealtheNet

 

 

 

### 
 Outgoing Claims Status Request (X12 276/277)
 [read the spec](/Tech/TechSpec?spec=staged%2FOutgoing%20Claims%20Status%20Request%20276_277.zip)

 

 

 Sends requests and receives responses from payers and intermediary systems about claim statuses using industry standard ANSI ASC X12N 276/277 transactions. Epic uses web services to send and receive the X12 messages.
 

 

 [Current integrations include ](#)
 

 - Aetna

 - Anthem

 - AVAILITY

 - Change Healthcare

 - EXPERIAN HEALTH, INC.

 - FinThrive

 - Healthcare IP

 - HEALTHPARTNERS

 - NEHEN

 - Optum

 - Quadax

 - SSi Healthcare

 - The SSI Group

 - TriZetto Provider Solutions, a Cognizant Company

 - United Healthcare

 - Waystar

 

 

 

### 
 Outgoing Authorization Request for Review and Response (X12 278R)
 [read the spec](/Tech/TechSpec?spec=5439)

 

 

 Transmits patient referral or authorization information to a third-party system. The referral/authorization information is sent in order to obtain authorization for health care services (such as specialty referrals and procedures) with clearing houses and payers. It uses ANSI X12 278 transactions.
 

 

 [Current integrations include ](#)
 

 - AccuReg

 - Aetna

 - Anthem

 - ATHENAHEALTH, INC.

 - AVAILITY

 - Blue Cross Blue Shield of Michigan

 - Change Healthcare

 - Citra Health Solutions

 - Elevance

 - Emblem

 - Ensemble Health Partners

 - Evicore

 - EXPERIAN HEALTH, INC.

 - GE

 - Glidian

 - Health Care Service Corporation

 - HUMANA

 - Humata Health

 - INFINX

 - Janus

 - Notable

 - Optum

 - Recondo

 - REDOX

 - Rhyme

 - STANSON HEALTH, INC.

 - SYMPLR

 - Texas - Public Health Agencies

 - United Healthcare

 - UPMC Pinnacle Health Plan

 - VOLUWARE, INC.

 - Waystar

 

 

 

### 
 Outgoing Pharmacy Benefit Eligibility Query - 270/271
 [read the spec](/Tech/TechSpec?spec=5228)

 

 

 E-Prescribing functionality when Epic is the Prescriber. Initiates pharmacy benefit eligibility queries.
 

 

 [Current integrations include ](#)
 

 - AVAILITY

 - Cardinal Health WaveMark

 - Change Healthcare

 - EXPERIAN HEALTH, INC.

 - MetroPlus

 - SURESCRIPTS

 

 

 

### 
 Outgoing Admission Notification (X12 278)
 [read the spec](/Tech/TechSpec?spec=5300)

 

 

 Used to notify a payer or health plan about an admission for one of their covered a patients. The ANSI X12 278 transaction is used for both the original notification of the admission and the payer response that might follow. Such a response might contain the reference/authorization number to be sent later on the claim.
 

 

 [Current integrations include ](#)
 

 - Aetna

 - AMERISOURCE BERGEN

 - AVAILITY

 - Change Healthcare

 - Cigna

 - Clinical Computer Systems, Inc.

 - EXPERIAN HEALTH, INC.

 - FinThrive

 - Horizon

 - HUMANA

 - Janus

 - NAS United Healthcare Services

 - Notable

 - Ohio - Public Health Agencies

 - Optum

 - Post-n-track

 - Quartz

 - Relay Health

 - The Advisory Board

 - TriZetto Provider Solutions, a Cognizant Company

 - United Healthcare

 - Waystar

 

 

 

### 
 Outgoing Authorization Notification (X12 278N)
 [read the spec](/Tech/TechSpec?spec=5172)

 

 

 Sends authorization decisions for covered patient referrals to third-party AP claims systems. The response from the third-party AP claims system is the acknowledgement of the information received.
 

 

 [Current integrations include ](#)
 

 - AVAILITY

 - Brightree

 - EXPERIAN HEALTH, INC.

 - Health Choices

 - Johns Hopkins HealthCare LLC

 - Natus

 - TriZetto Provider Solutions, a Cognizant Company

 - United Healthcare

 

 

 

### 
 Incoming Purchase Order Acknowledgement to Willow Inventory
 [read the spec](/Tech/TechSpec?spec=5361)

 

 

 Receives acknowledgements from a supplier for purchase orders placed in Willow Inventory. The interface uses the ANSI X12 855 transaction set for the response.
 

 

 [Current integrations include ](#)
 

 - Alliance Healthcare

 - AMERISOURCE BERGEN

 - Anda

 - Auburn Pharmaceutical

 - BD

 - Cardinal Health WaveMark

 - CENCORA

 - Global Healthcare Exchange

 - Macro Helix

 - McKesson

 - Morris & Dickson

 - ORACLE

 - Parmed 

 - Smith Drug Company

 - SURESCRIPTS

 - TOPRX

 

 

 

### 
 Incoming Shipment Notification to Willow Inventory
 [read the spec](/Tech/TechSpec?spec=5321)

 

 

 Receives information about items sent by a supplier to fill a purchase order from Willow Inventory medication inventory management. This interface uses the ANSI X12 856 transaction set or European GS1.
 

 

 [Current integrations include ](#)
 

 - AMERISOURCE BERGEN

 - Anda

 - AutoMed

 - Baxter

 - BD

 - Cardinal Health WaveMark

 - CENCORA

 - CenterX

 - CuraScript

 - Global Healthcare Exchange

 - Infor Global Solutions

 - KeySource

 - McKesson

 - Medline

 - Morris & Dickson

 - ORACLE

 - Parmed 

 - Smith Drug Company

 - SURESCRIPTS

 - Tecsys

 - TOPRX

 

 

 

### 
 Outgoing Health Care Claims for Institutional, Professional, and Dental Services
 [read the spec](/Tech/TechSpec?spec=5268)

 

 

 This outgoing batch interface sends insurance claim information to payers and intermediary systems using industry standard ANSI ASC X12N 837 transactions (institutional, professional and dental). 
 

 

 [Current integrations include ](#)
 

 - Availity

 - Carisk Intelligent Clearinghouse

 - Change Healthcare

 - Cirius

 - ClaimLynx

 - efficientC

 - Experian Health

 - Healthcare IP

 - Inovalon

 - nThrive

 - Optum

 - Quadax

 - SSI

 - TriZetto Provider Solutions, a Cognizant Company

 - WayStar

 

 

 

### 
 Outgoing Health Care Data Reporting Claims
 [read the spec](/Tech/TechSpec?spec=5156)

 

 

 This outgoing batch interface sends insurance claim information to government and intermediary systems using the industry standard ANSI ASC X12N 837 data reporting transaction.
 

 

### 
 Rapid Retest 
 [read the spec](/Tech/TechSpec?spec=6443)

 

 

 This bi-directional interface builds upon the use of standard Claim Reconciliation and sends individual claims to intermediary systems using industry standard ANSI ASC X12N 837 transactions (institutional, professional, and dental) and loads information about claim status back using industry standard ANSI ASC X12N 277CA transactions. This interface updates the status of errored claims in the system. 
 

 

 [Current integrations include ](#)
 

 - Availity

 - Change Healthcare

 - Cirius

 - Experian Health

 - Healthcare IP

 - nThrive

 - Quadax

 - The SSI Group

 - TriZetto Provider Solutions, a Cognizant Company

 - WayStar

 

 

 

### 
 Incoming Health Care Claim Payment/Advice
 [read the spec](/Tech/TechSpec?spec=5194)

 

 

 This incoming batch interface posts insurance claim payment information received directly from payers and content aggregators, such as claims clearinghouses and banks, using standard ANSI ASC X12N 835 transactions. 
 

 

 [Current integrations include ](#)
 

 - Availity

 - Bank of America

 - BBVA

 - Change Healthcare

 - Cirius

 - ClaimLynx

 - efficientC

 - Experian Health

 - Fifth Third

 - Healthcare IP

 - Huntington Bank

 - Inovalon

 - J.P Morgan Chase

 - nThrive

 - Optum

 - Patientco

 - PNC

 - Quadax

 - Quadax

 - SSI

 - TD Bank, N.A.

 - Texas Capital Bank

 - TriZetto Provider Solutions, a Cognizant Company

 - US Bank

 - WayStar

 - Wells Fargo

 

 

 

### 
 Outgoing Health Care Claim Acknowledgement
 [read the spec](/Tech/TechSpec?spec=5174)

 

 

 This outgoing batch interface sends claim acknowledgement responses to incoming ANSI 837 files using ANSI ASC X12N 277CA transactions. 
 

 

### 
 Tapestry Outgoing X12 Acknowledgment (X12 999)
 [read the spec](/Tech/TechSpec?spec=5178)

 

 

 This message is sent in response to incoming healthcare services messages. It acknowledges the receipt of the message and, if necessary, reports any formatting errors in the file. It is an ANSI ASC X12N 999 transaction. 
 

 

### 
 Tapestry Outgoing Front-End Claim Status Acknowledgment (X12 277CA)
 [read the spec](/Tech/TechSpec?spec=5177)

 

 

 Tapestry Outgoing Front-End Claim Status Acknowledgment (X12 277CA).
 

 

### 
 Incoming Marketplace Benefit Enrollment and Maintenance (HIX 834)
 [read the spec](/Tech/TechSpec?spec=5176)

 

 

 Standard X12 format for loading marketplace information.
 

 

### 
 Incoming X12 HIX 820
 [read the spec](/Tech/TechSpec?spec=5161)

 

 

 Incoming Standard X12 format for loading Marketplace Premium Payment Information.
 

 

### 
 Tapestry Outgoing Marketplace Benefit Enrollment (X12 834)
 [read the spec](/Tech/TechSpec?spec=5170)

 

 

 Standard X12 format for sending out marketplace coverage information
 

 

### 
 Outgoing Authorization Inquiry (X12 278I)
 [read the spec](/Tech/TechSpec?spec=5440)

 

 

 Provides the ability to inquire about the status of an existing authorization request. It uses ANSI X12 278 transactions and is used in conjunction with an Outgoing Authorization Request for Review - Outgoing Request (X12 278R) interface.
 

 

 [Current integrations include ](#)
 

 - Blue Cross/Blue Shield

 - Change Healthcare

 - Humana

 - Olive

 - Recondo

 - Relay Health

 - United Healthcare

 - WayStar

 

 

 

### 
 Incoming Claim Status Batch (X12 277)
 [read the spec](/Tech/TechSpec?spec=9398)

 

 

 This incoming batch interface loads information about claim acknowledgments using industry standard ANSI ASC X12N 277CA transactions. This interface can update the status of claims in the system and is able to load claim error information from payer and intermediary systems.
 

 

### 
 X12 278 Endpoint Specifications
 [read the spec](/Tech/TechSpec?spec=8001)

 

 

 Describes JSON Wrapped RESTful endpoint for sending and receiving X12 278 interface messages.
 

 

### 
 Payer Platform Outgoing Claims Status Request (X12 276/277)
 [read the spec](/Tech/TechSpec?spec=9924)

 

 

 Sends requests and receives responses from payers and intermediary systems about claim statuses using industry standard ANSI ASC X12N 276/277 transactions. Epic uses web services to send and receive the X12 messages.