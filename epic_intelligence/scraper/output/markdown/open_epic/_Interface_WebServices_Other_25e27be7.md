# open.epic :: Explore By Interface Type

> Source: https://open.epic.com/Interface/WebServices/Other

---

# 
 By Interface Type

 

 

 
 

 

 
 

 
 

 
 
 

## Web Services

 
In some cases, we've found that standards didn't exist, weren't sufficient, or were too complicated technically for our customers' use cases. In those cases, we've developed purpose-built Epic-specific web services to serve those needs.

All web services [require a client ID](/Tech/GetTechSpec?spec=Client ID tutorial.pdf) to identify the calling application as part of the Epic authorization framework. When you are ready to use the web services listed below with an Epic customer, review [Creating, Activating, and Licensing an App](https://fhir.epic.com/Documentation?docId=epiconfhirrequestprocess&section=creating) to create a new client ID. Then [submit an email request](mailto:open@epic.com?subject=Request%20to%20add%20API(s)%20to%20client%20ID&body=Please%20add%20the%20following%20APIs%20to%20my%20existing%20client%20ID%20for%20the%20application%20below%3A%0D%0A%0D%0AApplication%20Information%0D%0A%E2%80%A2%20Application%20name%3A%20%0D%0A%E2%80%A2%20Link%20to%20app%20from%20FHIR.epic.com%3A%20%0D%0A%E2%80%A2%20Brief%20summary%20of%20what%20the%20app%20does%20and%20the%20functionality%20the%20integration%20provides%3A%20%0D%0A%0D%0AWeb%20Service%20or%20Subspace%20Communication%20Framework%20Information%0D%0A%E2%80%A2%20If%20using%20web%20services%2C%20which%20web%20services%20the%20application%20is%20using%20(from%20the%20Epic%20Public%20section%20on%20https%3A%2F%2Fopen.epic.com%2FoeAPIlist)%3A%20%0D%0A%E2%80%A2%20If%20using%20Subspace%2C%20which%20Subspace%20scopes%20the%20application%20is%20using%20(from%20the%20specifications%20on%20https%3A%2F%2Fopen.epic.com%2FHyperdrive%2FHyperdrive)%3A%20) to have these web services added to your app. 

You may apply to [Vendor Services](https://vendorservices.epic.com) for access to a sandbox or to receive Epic support for these Web Services.

### 
 Encoder Interface API
 [read the spec](/Tech/TechSpec?spec=5458)

 

 

 

The GetEncoderMessage and SetEncoderMessage APIs are used to integrate with encoders and computer-assisted coding systems to exchange information for Hospital Coding workflows. Epic offers front-end integrations through web services as well as back-end integration methods. To see the HL7 payload, check out the [HL7v2 - Coding-Bidirectional spec](../Interface/HL7v2#Coding-Bidirectional).

 

 

### 
 Patient Lookup and Identifiers
 [read the spec](/Tech/TechSpec?spec=5454)

 

 

 

Search for patients and obtain or assign identifiers. If no patient can be found for the given criteria, a patient record can be created.

 

 

### 
 Personnel Management
 [read the spec](/Tech/TechSpec?spec=5453)

 

 

 

Create, update, and delete user records in Epic. With this suite of services, you can also view and update user groups, pager IDs, user login departments, and departments the user has access to.

 

 

### 
 Phone System Pause/Resume
 [read the spec](/Tech/TechSpec?spec=5452)

 

 

 

When collecting credit card payments over the phone, you may not want the credit card number (as read by the patient) to be contained in the customer service recording files. This web service can be setup to send a request to the phone system to pause the recording when the staff's credit card entry form opens, and send another request to the phone system to resume the recording when the credit card form closes.

 

 

### 
 Print Job Status
 [read the spec](/Tech/TechSpec?spec=5451)

 

 

 

Use the UpdatePrintJobStatus API to send back information about the status of the print job that you received from Epic through Epic Print Service (EPS).

 

 

### 
 Release of Information
 [read the spec](/Tech/TechSpec?spec=5450)

 

 

 

Create and update release of information (ROI) requests.

 

 

### 
 Utilization Management
 [read the spec](/Tech/TechSpec?spec=5448)

 

 

 

The CriteriaReview web service retrieves data from a criteria review record. A ReviewCollection groups together CriteriaReview resources that have been created for a patient previously.

 

 

### 
 Scan Signature Deficiencies
 [read the spec](/Tech/TechSpec?spec=5449)

 

 

 

When using a document management system (DMS) to manage scans on a patient's chart, it's also possible to track signature requirements for those scans in Epic. DMS applications can use these web services to create and update signature deficiencies in Epic. These signature deficiencies will notify the signing users and let them launch directly into the DMS's signing application.

 

 

### 
 Outgoing SMS
 [read the spec](/Tech/TechSpec?spec=5455)

 

 

 

You may want to send text messages to patients or proxies for a variety of reasons, such as to remind them of upcoming appointments or surgeries, send notifications about their MyChart account, or update visitors about a patient’s surgery. Epic’s SMS (Short Message Service) web service enables you to pass a phone number and simple message data to a SMS web service vendor, which will send a text message directly to a patient’s mobile phone over a cellular network.

 

 

### 
 MyChart Bedside MDM Patient Data Wipe
 [read the spec](/Tech/TechSpec?spec=5456)

 

 

 

Epic sends requests to Mobile Device Management (MDM) vendors so they can wipe data corresponding to discharge and/or transfer workflows. The requests include an MDM-managed device's identifier to the MDM vendor's endpoint so that the MDM vendor can then clear data from the device remotely.

 

 

### 
 Embedded Context-Aware Linking for Epic Monitor
 [read the spec](/Tech/TechSpec?spec=5459)

 

 

 

Epic's Remote Sitter solution allows organizations to engage in continuous video surveillance of multiple patients (typically 12 a time), be it for COVID, fall risk, or behavioral disorders. It’s a grid of videos embedded in our Epic Monitor platform and surrounded with contextual information from the EMR. Our plan is to embed web browser controls, each containing a CAL video feed, so that customers can engage with any video vendor on Vendor Services. We call it ECAL (Embedded CAL).

 

 

### 
 Enterprise Image Access

 

 

 This web integration API provides the ability to generate dynamic, secure, contextual links used to launch the appropriate context in an enterprise image viewer. You can use [our simple testing harness](/Tech/TechSpec?spec=TestingHarness.zip) to help you validate that your web application can be successfully embedded.
 

 

 [Current integrations include ](#)
 

 - Ambra

 - BRIT

 - Change Healthcare

 - Client Outlook

 - Epiphany Healthcare

 - Fuji

 - GE

 - HeartIT

 - Hyland

 - IBM

 - Philips

 - Sectra

 - Siemens

 - Vital Images

 

 

 

### 
 Content Linking
 [read the spec](/Tech/TechSpec?spec=5426)

 

 

 The patient portal provides patients with a view into the medical chart maintained by their healthcare organization. This information can be supplemented by educational materials that are specific to a patient's problems, medications, and other information. This functionality is called Content Linking. While many approaches have been used to achieve this integration in the past, Epic recommends that new organizations use the Infobutton APIs as they are implemented through the National Library of Medicine and [MedlinePlus](http://www.nlm.nih.gov/medlineplus/connect/overview.html). 
 

 

 [Current integrations include ](#)
 

 - A.D.A.M.

 - Elsevier

 - Healthwise

 - KidsHealth

 - Krames-Staywell

 - Lab Tests Online

 - McKesson

 - National Library of Medicine MedlinePlus

 

 

 

### 
 E-Signature
 [read the spec](/Tech/TechSpec?spec=5404)

 

 

 Epic's kiosk software can be used to collect signatures for consent or other purposes. These signatures can then be sent to an external document management system. The kiosk sends an image of the signature to the document management system, which in turn creates a reference to the signature document within the EHR. 
 

 

### 
 Credit Card and Bank Account Integration
 [read the spec](/Tech/TechSpec?spec=5408)

 

 

 Epic provides support for credit cards to be used with the Epic system to pay copays, hospital and outpatient bills, and for medications. This integration is handled through credit card gateway systems, which send payment data to processing services that verify the payments with appropriate banks. The gateway then sends the verified payment information back to the Epic system to post the payment. This integration is handled through the patient portal and patient kiosk software as well as in over-the-phone and billing-office use cases. Epic software for credit card processing follows the PA-DSS requirements in its development. 
 

 

 [Current integrations include ](#)
 

 - ABILITY Network

 - AxiaMed

 - Bluefin Payment Systems

 - ClaimsXpress

 - CORE Business Technologies

 - DivDat Healthcare Solutions

 - eBizCharge

 - Elavon

 - Experian Health

 - HealthPay24

 - InstaMed, a J.P. Morgan Company

 - iPayX

 - Merchant e-Solutions 

 - MyVirtualMerchant

 - Patientco

 - Paymentus

 - PayPal

 - Phreesia

 - RevSpring

 - Salucro

 - Tempus Technologies

 - TrustCommerce

 - US Bank

 - VirtualMerchant 

 - WayStar

 - Wells Fargo

 

 

 

### 
 Tapestry Document Linker DMS Integration
 [read the spec](/Tech/TechSpec?spec=5393)

 

 

 This web service allows third-party DMS vendors to launch activities within a pre-existing Hyperspace instance to link documents to records in Epic such as claims or coverages. Information about the document in the third-party database will be populated in the activity launched, and users can complete the linking workflow from the Hyperspace session. The web service can also launch a new Hyperspace instance if one is not open when the web service is called. 
 

 

### 
 Credit Card and Check Scanning Device Integration
 [read the spec](/Tech/TechSpec?spec=5412)

 

 

 In addition to the Credit Card and Bank Account Integration specification, Epic provides separate and additional support for non-keyboard emulation credit card devices. This integration is handled through an interface between Epic and your gateway software. The gateway software integrates with the device and provides Epic with transaction results for the credit card payment. This integration is handled through the patient kiosk and by front desk personnel during check-in or check-out. This interface is supplemental to the generic credit card interface described above and should be implemented in addition to that interface if you want to provide support for EMV devices.
 

 

 [Current integrations include ](#)
 

 - AxiaMed

 - Bluefin

 - CORE Business Technologies

 - DivDat Healthcare Solutions

 - Elavon

 - Experian

 - HealthPay 24

 - InstaMed, a J.P. Morgan Company

 - Patientco

 - Salucro

 - Tempus Technologies

 - TrustCommerce

 

 

 

### 
 Incoming Computer-Telephony Integration
 [read the spec](/Tech/TechSpec?spec=5376)

 

 

 Epic integrates with your organization’s phone system to automatically open the appropriate chart or another activity in Epic when calls are received.
 

 

 [Current integrations include ](#)
 

 - Avaya

 - TalkDesk

 

 

 

### 
 Outgoing Computer-Telephony Integration
 [read the spec](/Tech/TechSpec?spec=5283)

 

 

 Epic integrates with your organization’s phone system so users can place or end a call directly from a patient chart or another activity in Epic, and details about the call are logged. Your phone system can also update Epic with the call identifier after the call. 
 

 

 [Current integrations include ](#)
 

 - TalkDesk

 

 

 

### 
 Outbound Fax Services with Epic Print Service
 [read the spec](/Tech/TechSpec?spec=5308)

 

 

 Epic integrates with fax management systems using the outbound faxing web service. This web service allows Epic community members to fax documents generated by various applications from their instance of Epic, and receive back information about whether the transmission was successful.
 

 

### 
 SAML 2.0 Reauthentication for Haiku and Canto EPCS
 [read the spec](/Tech/TechSpec?spec=5422)

 

 

 Haiku and Canto, Epic's mobile apps for physicians on iOS and Android devices, support launching a web portal during e-prescribing controlled substances (EPCS) to verify the physician's identity with an EPCS-qualified identity provider (IdP). The IdP returns a valid SAML assertion to Haiku or Canto, which allows the physician to continue placing orders. This process follows the SP-initiated Web Browser SSO profile defined in the OASIS SAML 2.0 specification. The workflow is also supported in Rover, Epic's mobile app for nurses, on iOS devices only. 
 

 

### 
 Binary Data Retrieval
 [read the spec](/Tech/TechSpec?spec=5392)

 

 

 This web integration enables Epic to request image and document files from an external system. Epic will then display these images inline within the user's workflow. 
 

 

### 
 Outgoing MDS Data for MDS Scrubbers
 [read the spec](/Tech/TechSpec?spec=5307)

 

 

 The Minimum Data Set (MDS) scrubber interface allows MDS coordinators to send in-progress and completed [MDS assessments](https://www.cms.gov/Medicare/Quality-Initiatives-Patient-Assessment-Instruments/NursingHomeQualityInits/NHQIMDS30) electronically to a 3rd-party MDS scrubbing vendor and receive real-time feedback. 
 

 

### 
 EPS Document Retrieval Web Service
 [read the spec](/Tech/TechSpec?spec=5405)

 

 

 This web service integration enables Epic print services (EPS) to query a document management system (DMS) for images or documents to insert into a print job. This is useful when you want a scan to be stored in your DMS, but want to include that scan in something you print. 
 

 

### 
 Wait Time APIs
 [read the spec](/Tech/TechSpec?spec=5760)

 

 

 This set of APIs returns estimated wait time information. Select the appropriate API to retrieve wait time information for a given emergency department, urgent care clinic, ambulatory clinic, or outpatient provider.
 

 

### 
 Print Test Page
 [read the spec](/Tech/TechSpec?spec=5803)

 

 

 Use the PrintTestPage API to trigger test print jobs from a specified printer device. 
 

 

### 
 Output Management Web Service
 [read the spec](/Tech/TechSpec?spec=5806)

 

 

 Epic integrates with third-party output management systems using the outbound print job web services. These web services allow Epic community members to send print requests to a third-party output management server and receive back information about whether the print job was successful.
 

 

### 
 Encryption Guide
 [read the spec](/Tech/TechSpec?spec=6055)

 

 

 PACS integrations use encryption to protect confidential information sent between systems. This guide describes the technical details of Epic’s supported encryption algorithms, including step-by-step instructions and sample encrypted payloads.
 

 

### 
 Tapestry Generic Code Editor
 [read the spec](/Tech/TechSpec?spec=5164)

 

 

 Bi-directional claim code editing integration with Tapestry
 

 

### 
 Disassociate Mobile Device
 [read the spec](/Tech/TechSpec?spec=10323)

 

 

 
Use the DisassociateMobileDevice API to disassociate a mobile device from the server using its Install ID. After disassociation, the device no longer receives push notifications or VoIP calls, and users on shared devices no longer receive notifications from previously logged-in users.