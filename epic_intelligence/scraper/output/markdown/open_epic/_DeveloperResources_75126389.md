# open.epic :: Developer Resources

> Source: https://open.epic.com/DeveloperResources

---

- 

 

 
# Developer Resources

 

 Epic supports a wide variety of data exchange technologies. This guide provides an overview of the options to work with Epic, types of data exchange technologies, and processes for taking your app from a concept to live with an Epic customer.
 

 

 

 
## 
 Things to be aware of while planning your data sharing strategy with Epic customers:
 

 

 

 
### Connect Directly to Each Epic Customer

 

 

 Epic uses a federated model: every customer runs their own independent Epic
 instance and decides which apps can connect. There is no central Epic endpoint.
 To exchange data with organizations using Epic, you'll need to establish connections directly with individual
 organizations. Epic provides the software platform and standard APIs, while
 customers control how and with whom they connect.

 

 
 

 

 

 

 
### Build and Deploy Connections Using Self-Service Tools

 

 

 Epic is vendor-neutral, and no special relationship is required to develop or
 deploy an app. Using Open.Epic's standards-based tech, developers can use public
 documentation, sandbox, self-service tools to register apps, connect to customer
 systems, and go live – all without needing Epic's involvement.

 

 
 

 

 

 

 
### Get Support If You Need It

 

 

 Contact us via the
 [Technology Guidance](/Contact#DataSharingGuidance)
 form if you need broad guidance on what technology to use. Visit our
 [Developer Support](/EpicSupport)
 page for information on the resources and programs available to assist
 you, such as
 [Vendor Services](https://vendorservices.epic.com).
 Products in specific categories can receive the Toolbox designation and additional
 support services.

 

 
 

 

 

 

 

 

 For additional recommendations about how to work with an Epic community member to develop your
 product's connection to Epic, see
 our [Strategies to Effectively Collaborate page](https://fhir.epic.com/Documentation?docId=eofcollaborate).
 

 

 
## Epic's Developer Guide

 

 Depending on the technologies used, most applications will require a client ID that is issued
 from Epic. Developers may obtain client IDs from open.epic.com. Customers may then request that
 the client ID be synced to their instance, and app developers may directly approve these, without
 involvement from Epic. Here's a guide to get you started:
 

 

 

 
 

 [1](#step-1)

 - [2](#step-2)

 - [3](#step-3)

 - [4](#step-4)

 - [5](#step-5)

 

 
 

 
 

 - Data Sharing Design

 - Register a Client Record

 - Develop and Test

 - Customer Implementation
and Going Live

 - Request Showroom Listing

 

 

 
 

 - 
 [1](#step-1)
 
Data Sharing Design

 

 - 
 [2](#step-2)
 
Register a Client Record

 

 - 
 [3](#step-3)
 
Develop and Test

 

 - 
 [4](#step-4)
 
Customer Implementation
and Going Live

 

 - 
 [5](#step-5)
 
Request Showroom Listing

 

 

 

 

 
 

 
 
 
 
 
 
 
 
 
 
 

 
 

 

 
 

 
 
1

 
 
### 1.Data Sharing Design

 
 Start by reviewing Epic's [data sharing playbooks,](/Playbooks) which outline recommended
 connection practices built on industry-standard, publicly available technologies. These playbooks are
 a great starting point for products that align with one of the available product categories.
 

 

 If you are working in another area or innovating with
 additional technologies, review our
 [data sharing design overview](/DesignOverview) and
 [specifications](/TechnicalSpecifications) to find interfaces, APIs, and other
 tech that meet the needs of your use case.
 

 

 Finally, healthcare data is inherently sensitive and
 complex, so we recommend reviewing Epic's
 [developer guidelines](https://fhir.epic.com/Documentation?docId=developerguidelines)
 to help you ensure that your design
 meets customer expectations in terms of safety, security, privacy, reliability,
 scalability, and data integrity.
 

 

 If you don't find what you're looking for, contact us via the
 [Technology Guidance](/Contact) form.
 

 
 

 
 

 
 
 
### 2.Register a Client Record

 

 The first step in authorizing your product to exchange data with an Epic
 customer environment is to
 [register the product with Epic](https://fhir.epic.com/Documentation?docId=epiconfhirrequestprocess&section=devclient).
 A client ID
 identifies an associated application requesting access to an organization's
 Epic environment and tells the system the scope of data that the application
 is authorized to access.
 [Following these steps](https://fhir.epic.com/Documentation?docId=epiconfhirrequestprocess),
 self-service for most use cases, you
 will add the APIs your product needs, and you will receive a production and
 non-production identifier (client ID). When
 creating your app, it's important that you only include the APIs you plan to
 use in a customer's production system so each customer can assess the security,
 privacy, and licensing implications of implementing your app.
 

 

 If you are creating a patient-authorized app, you may have
 additional client ID creation and distribution options,
 for example via TEFCA IAS. Review the
 [Automatic Client Record Distribution](https://fhir.epic.com/Documentation?docId=patientfacingfhirapps&section=AutomaticClientDistribution)
 section of the Patient-Facing Apps Using FHIR tutorial and our
 [Patient-Facing Consumer Health Apps playbook](https://fhir.epic.com/Documentation?docId=patient_facing_apps)
 for additional details.
 

 
 
2

 

 
 

 

 
 

 

 
 

 
 
3

 
 
### 3.Develop and Test

 

 As you begin to develop your app, you can test no-code API calls with the
 Sandbox through our Try It feature available on many
 [API specifications](https://fhir.epic.com/Sandbox),
 query the system from an API client using our
 [Sandbox test patients and endpoints](https://fhir.epic.com/Documentation?docId=testpatients),
 and then begin to make calls directly from
 your application code when you're ready. If you plan to have your app launch
 from Epic, use the
 [SMART on FHIR testing feature](https://fhir.epic.com/Documentation?docId=launching)
 to test your app launch via
 OAuth2. If you are writing a web-based application that you intend to embed in
 Epic or use technologies to communicate directly with Epic's client
 application, check out your options for
 [testing connections in Hyperdrive](/Hyperdrive/Hyperdrive). For more details on testing options, check out
 our [Developer testing page](https://fhir.epic.com/Documentation?docId=testingguide).
 

 

 When your product is ready to deploy to a customer testing
 environment, activate the app for customer distribution by marking it ready for
 production use.
 

 
 

 
 

 
 
 
### 4.Customer Implementation and Going Live

 

 When you've licensed your product directly to a customer,
 share your client IDs with them and the customer will
 [request the client ID](https://fhir.epic.com/Documentation?docId=epiconfhirrequestprocess&section=custreq)
 to be delivered to their
 environments. You will then
 [enable any keys](https://fhir.epic.com/Documentation?docId=epiconfhirrequestprocess&section=devapprove)
 specific to their
 implementation and the implementation work can begin! Take ownership of your
 app's success through your
 [collaboration directly with your customer](https://fhir.epic.com/Documentation?docId=eofcollaborate). We
 recommend a kickoff discussion of your
 [implementation project plan](https://fhir.epic.com/Documentation?docId=implementing),
 setting expectations of task ownership and timelines. You'll
 work to deploy your software, configure and localize your product to the
 customer's specific workflows and settings, complete non-production testing,
 and [troubleshoot](https://fhir.epic.com/Documentation?docId=troubleshooting_eof)
 when needed.
 

 

 If you are deploying an automatically-distributed patient-authorized app,
 you can connect directly to customer endpoints [listed here](/MyApps/Endpoints).
 

 
Congratulations on your go-live!

 
 
4

 

 
 

 

 
 

 

 
 

 
 
5

 
 
### 5.Request Showroom Listing

 

 Once your app is live with an Epic customer, you may
 [choose to list your app](https://fhir.epic.com/Documentation?docId=chlistingrequest)
 in Connection Hub on Showroom. This
 optional app listing can add visibility to your product, but it is not needed
 for additional customers to connect with your product; subsequent customers can
 also follow step 4 above.
 

 

 Additionally, if you choose to create a press release, web
 page, social media post, or other marketing materials about your app and
 mention your connection with Epic, keep [these guidelines](https://fhir.epic.com/Resources/openepic_marketing) in mind to
 help you accurately represent your relationship with Epic.