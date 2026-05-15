# open.epic :: Hyperdrive

> Source: https://open.epic.com/Hyperdrive/Hyperdrive

---

# 
 Hyperdrive

 

 

 
 Epic's web-based end user client application

 

 
 

 
 

 
 
 

## 

 Epic has moved its primary end user application, Hyperspace, to a web-based framework called Hyperdrive. Hyperdrive is a secure, Epic-specific web browser and code-level changes are required for web- and desktop-based Hyperspace integrations in order to integrate wth Hyperdrive. Many Epic workflows rely on integrations with other products for users to complete a task. Hyperdrive is essential for almost all end users largely because it includes a Windows-native plugin infrastructure that enables integrations with other products. 
### Changes for Integrations
Existing products integrating with Epic Hyperspace via COM-based APIs will need to be updated to work with Hyperdrive. Web applications hosted within, or launched from, Hyperspace may require changes to work with Hyperdrive. HL7, Web Services, DICOM, XML file drop, SMART on FHIR, and outgoing command line integrations will not require changes. 

If your integration is a website, the [Prepare Web Content for Hyperdrive](../Tech/TechSpec?spec=staged/Prepare for Hyperdrive Transition.pdf) document summarizes changes that may be necessary to make your integration Hyperdrive-ready. This reference can help you evaluate if changes are needed for your application. 

 The details of our new API specifications can be found in the sections below. As you evaluate these APIs keep in mind that integrations developed for Hyperdrive may not work with the current Hyperspace client. Your application should support integration with both clients, or be side-by-side compatible with your current application, on the same workstation or server until all customers have transitioned off of Hyperspace. 
### Testing Integrations in Hyperdrive
We have developed testing harnesses to help you validate that your integration is successful with Hyperdrive: 

- The [Hyperdrive Client Test Harness](/Hyperdrive/HyperdriveDownload) allows you to ensure your development is compatible with Hyperdrive. 
Supported workflows currently include: E-Signature, Login, Voice Recognition, Scan Acquisition, Scan Viewing, Scan Signature Deficiencies, FHIRcast, XML, and web content integration workflows. 
- Functionality of this harness will be updated as we release additional features and enhancements.
- When Hyperdrive is used as a published application, Slingshot can make some integrations available on the endpoint device. Further detail can be found in the test harness documentation.

- The [Hyperdrive Web Developer Test Harness](../Tech/TechSpec?spec=HyperdriveWebDeveloperTestHarness.zip) allows you to validate that your website renders and functions correctly when hosted inside of Hyperdrive before it enters production. It allows you to see how a site will present either in an iframe or in a Hyperdrive embedded window. 
- The client testing harness can also be accessed via Hyperspace for Mac. When using Hyperspace for Mac, keep in mind that most client integrations will only work on a Windows OS. Testing integrations via Hyperspace for Mac should be focused on URL launches for SMART on FHIR, HTTP GET, and SAML. If your integration requires more bespoke client integration technology that is supported by the test harness, you should test using Hyperdrive on a Windows workstation or VM. 
[Hyperspace for Mac Download](https://apps.apple.com/us/app/epic-hyperspace/id6472198304)

When installing Hyperspace for Mac, you will be prompted to configure a Hyperspace Web URL to connect to the fhir.epic sandbox.
- URL: https://fhir.epic.com/HSWeb_uscdi 

 

### Timelines
Most organizations transitioned their users to Hyperdrive in 2022 and 2023, though a few may not have completed this transition until later. During the transition, most organizations will have some users using Hyperspace and others using Hyperdrive, and both clients will be installed on the same workstations. 

### 
 Tapestry Document Linker DMS Integration
 [read the spec](/Tech/TechSpec?spec=5393)

 

 

 This web service allows third-party DMS vendors to launch activities within a pre-existing Hyperspace instance to link documents to records in Epic such as claims or coverages. Information about the document in the third-party database will be populated in the activity launched, and users can complete the linking workflow from the Hyperspace session. The web service can also launch a new Hyperspace instance if one is not open when the web service is called. 
 

 

### 
 Desktop Generic Authentication
 [read the spec](/Tech/TechSpec?spec=5421)

 

 

 This interface allows external authentication software to implement authentication devices for use in Epic. The external authentication software can write installable devices that can be configured for use as devices to authenticate a user for login into Epic, to re-authenticate the user after login (for example, to sign off on medications), or to identify a patient (for example, to check into an appointment). 
 

 

### 
 Subspace Communication Framework
 [read the spec](/Tech/TechSpec?spec=5185)

 

 

 The Subspace Communication Framework is a pattern for asynchronous, semi-event-driven integrations between Epic and external applications. This document outlines the steps that an external application must take to initiate and communicate with Epic via a Subspace integration. 
 

 

### 
 Subspace User Session Management
 [read the spec](/Tech/TechSpec?spec=5184)

 

 

 This API allows other applications to receive events about and request changes to be made to a user's session in Epic. This includes information about logging in, logging out, securing, and shutting down. The API uses the Subspace Communication Framework. 
 

 

### 
 Other Subspace APIs
 [read the spec](/Tech/TechSpec?spec=5304)

 

 

 This API contains information about various requests that can be made using the Subspace Communication Framework that do not directly manipulate the user session state. These requests include launching activities and moving or resizing the Hyperspace window. 
 

 

### 
 E-Signature
 [read the spec](/Tech/TechSpec?spec=5403)

 

 

 This API provides information about two workflows where e-signing functionality is used within Epic: Document Collection and Signature Authentication/Reconstruction. During Document Collection workflows, one or more individuals can sign an electronic document and their signatures will be stored into Epic. Signature Authentication workflows allow a user to authenticate the validity of a signature, and Signature Reconstruction workflows reconstruct signature images from discreetly stored data. 
 

 

### 
 Scan Acquisition
 [read the spec](/Tech/TechSpec?spec=5395)

 

 

 Epic has the ability to allow end users to acquire scanned documents via a Document Management System (DMS). This API specifies how to integrate an external desktop scan acquisition application with Epic to allow end users to perform the scanning work and file the documents’ metadata to Epic. 
 

 

### 
 Scan Viewing
 [read the spec](/Tech/TechSpec?spec=5394)

 

 

 Epic provides ways for users to view scans acquired via a Document Management System (DMS). This API specifies how to integrate a web-based external scan viewing application with Epic for end users to view acquired scans. 
 

 

### 
 XML Context Synchronization

 

 

 This document contains APIs that can be used for single sign-on, patient context synchronization, study context synchronization, and real-time measurement exchange. These APIs are commonly used with PACS and CPACS vendors, but may have other uses as well. We additionally have an [encryption utility](../Tech/TechSpec?spec=Epic.EncryptionValidator.exe) for use with our XML integration (identical to URL encryption). We expect this functionality to work identically with Hyperdrive [as it does with Hyperspace](../Ancillary/Imaging#ImagingIntegration). 
 

 

### 
 Speech Recognition
 [read the spec](/Tech/TechSpec?spec=7215)

 

 

 This API allows speech recognition systems to interact with controls and views within Epic. The speech recognition system can receive information about and make changes to the content of a control as well as execute commands on an activity. Note that a specification for embedded applications also exists, under the section Speech Recognition for Embedded Applications.
 

 

### 
 FHIRcast
 [read the spec](/Tech/TechSpec?spec=5402)

 

 

 FHIRcast is a web based integration method used for context synchronization between Epic and other applications. This API is used to ensure that all applications display the same patient or study. 
 

 

### 
 Credit Card and Bank Account Integration

 

 

 This interface communicates with payment gateways to integrate credit card and bank account payments directly into Epic. Payment methods can be saved and used for automatic payment plans. We expect this functionality to work identically with Hyperdrive [as it does with Hyperspace](../Interface/WebServices#CreditCardandBankAccountIntegration). 
 

 

### 
 Subspace Encoder
 [read the spec](/Tech/TechSpec?spec=5401)

 

 

 Epic has the ability to allow users to work in an external encoder application and file the results to Epic when the user is finished. This API specifies how to integrate an external encoder application using the Subspace Communication Framework. 
 

 

### 
 Web Services Encoder
 [read the spec](/Tech/TechSpec?spec=5400)

 

 

 Epic has the ability to allow users to work in an external encoder application and file the results to Epic when the user is finished. This API enables integration with an external encoder application using web services. 
 

 

### 
 Kiosk Generic Authentication
 [read the spec](/Tech/TechSpec?spec=7517)

 

 

 Allows external authentication software to implement authentication devices for use in Epic’s self-arrival kiosk software. The external authentication software can write installable devices that can be configured to identify a patient or to enroll a patient for future identifications.
 

 

### 
 OpenID Connect
 [read the spec](/Tech/TechSpec?spec=7988)

 

 

 Epic’s Hyperspace application now supports the OpenID Connect (OIDC) authorization code flow as a means of authenticating users for logging in to Hyperspace as well as authentication within Hyperspace workflows.
 

 

### 
 Speech Recognition for Embedded Applications
 [read the spec](/Tech/TechSpec?spec=8293)

 

 

 This API allows speech recognition systems to interact with controls embedded within non-Epic web applications embedded (iframed) within Hyperdrive. For embedded applications, Hyperdrive effectively relays the incoming messages from speech recognition systems to the embedded application and also relays responses from the embedded application back to the speech recognition system. An accompanying sample, sample-main.ts shows how this spec can be implemented by the embedded web application with minimal effort. 
 

 

### 
 FHIRcast Content Sharing in Subspace
 [read the spec](/Tech/TechSpec?spec=10307)

 

 

 
FHIRcast Content Sharing enables external applications to share clinical information and measurements with Epic through a Subspace integration. This API describes how Subspace implements that content sharing using the Subspace Communication Framework.