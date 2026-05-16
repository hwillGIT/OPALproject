# Task - FHIR v4.0.1The business identifier for this taskThe URL pointing to a *FHIR*-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskThe URL pointing to an *externally* maintained  protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskBasedOn refers to a higher-level authorization that triggered the creation of the task.  It references a "request" resource such as a ServiceRequest, MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the "request" resource the task is seeking to fulfill.  This latter resource is referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a task is created to fulfill a procedureRequest ( = FocusOn ) to collect a specimen from a patientAn identifier that links together multiple tasks and other requests that were created in the same contextTask that this particular task is part ofThe current status of the task (this element modifies the meaning of other elements)The current status of the task. (Strength=Required)An explanation as to why this task is held, failed, was refused, etcContains business-specific nuances of the business stateIndicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs this a proposed task, a planned task, an actionable task, etcDistinguishes whether the task is a proposal, plan or full order. (Strength=Required)Indicates how quickly the Task should be addressed with respect to other requestsThe task's priority. (Strength=Required)A name or code (or both) briefly describing what the task involvesCodes to identify what the task involves.  These will typically be specific to a particular workflow. (Strength=Example)A free-text description of what is to be performedThe request being actioned or the resource being manipulated by this taskThe entity who benefits from the performance of the service specified in the task (e.g., the patient)The healthcare event  (e.g. a patient and healthcare provider interaction) during which this task was createdIdentifies the time action was first taken against the task (start) and/or the time final action was taken against the task prior to marking it as completed (end)The date and time this task was createdThe date and time of last modification to this taskThe creator of the taskThe kind of participant that should perform the taskThe type(s) of task performers allowed. (Strength=Preferred)Individual organization or Device currently responsible for task executionPrincipal physical location where the this task is performedA description or code indicating why this task needs to be performedA resource reference indicating why this task needs to be performedInsurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be relevant to the TaskFree-text information captured about the task as it progressesLinks to Provenance records for past versions of this Task that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the taskIndicates the number of times the requested action should occurOver what time-period is fulfillment soughtFor requests that are targeted to more than on potential recipient/target, for whom is fulfillment sought?A code or description indicating how the input is intended to be used as part of the task executionThe value of the input parameter as a basic typeThe name of the Output parameterThe value of the Output parameter as a basic typeIf the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actionedAdditional information that may be needed in the execution of the taskOutputs produced by the TaskThe business identifier for this taskThe URL pointing to a *FHIR*-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskThe URL pointing to an *externally* maintained  protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskBasedOn refers to a higher-level authorization that triggered the creation of the task.  It references a "request" resource such as a ServiceRequest, MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the "request" resource the task is seeking to fulfill.  This latter resource is referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a task is created to fulfill a procedureRequest ( = FocusOn ) to collect a specimen from a patientAn identifier that links together multiple tasks and other requests that were created in the same contextTask that this particular task is part ofThe current status of the task (this element modifies the meaning of other elements)The current status of the task. (Strength=Required)An explanation as to why this task is held, failed, was refused, etcContains business-specific nuances of the business stateIndicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs this a proposed task, a planned task, an actionable task, etcDistinguishes whether the task is a proposal, plan or full order. (Strength=Required)Indicates how quickly the Task should be addressed with respect to other requestsThe task's priority. (Strength=Required)A name or code (or both) briefly describing what the task involvesCodes to identify what the task involves.  These will typically be specific to a particular workflow. (Strength=Example)A free-text description of what is to be performedThe request being actioned or the resource being manipulated by this taskThe entity who benefits from the performance of the service specified in the task (e.g., the patient)The healthcare event  (e.g. a patient and healthcare provider interaction) during which this task was createdIdentifies the time action was first taken against the task (start) and/or the time final action was taken against the task prior to marking it as completed (end)The date and time this task was createdThe date and time of last modification to this taskThe creator of the taskThe kind of participant that should perform the taskThe type(s) of task performers allowed. (Strength=Preferred)Individual organization or Device currently responsible for task executionPrincipal physical location where the this task is performedA description or code indicating why this task needs to be performedA resource reference indicating why this task needs to be performedInsurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be relevant to the TaskFree-text information captured about the task as it progressesLinks to Provenance records for past versions of this Task that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the taskIndicates the number of times the requested action should occurOver what time-period is fulfillment soughtFor requests that are targeted to more than on potential recipient/target, for whom is fulfillment sought?A code or description indicating how the input is intended to be used as part of the task executionThe value of the input parameter as a basic typeThe name of the Output parameterThe value of the Output parameter as a basic typeIf the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actionedAdditional information that may be needed in the execution of the taskOutputs produced by the Task

> Source: https://hl7.org/fhir/R4/task.html

---

This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting) and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting)) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/task.html) [R4B](http://hl7.org/fhir/R4B/task.html) **R4** [R3](http://hl7.org/fhir/STU3/task.html)
 

# 12.1 Resource Task - Content [
](task.html#12.1)

| [Orders and Observations ](http://www.hl7.org/Special/committees/orders/index.cfm) Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process) | [Security Category](security.html#SecPrivConsiderations): Not Classified | [Compartments](compartmentdefinition.html): Not linked to any defined compartments | |

A task to be performed.

 
 
## 12.1.1 Scope and Usage [
](task.html#scope)

 
 A task resource describes an activity that can be performed and tracks the state of
 completion of that activity. It is a representation that an activity should be or has been
 initiated, and eventually, represents the successful or unsuccessful completion of that
 activity.
 

 
 Note that there are a variety of processes associated with making and processing orders.
 Some orders may be handled immediately by automated systems but most require real world
 actions by one or more humans. Some orders can only be processed when other real world actions
 happen, such as a patient presenting themselves so that the action to be performed
 can actually be performed. Often these real world dependencies are only implicit in the order
 details. 

 

 

 
 
## 12.1.2 Background and Context [
](task.html#bnc)

 
### 12.1.2.1 Using Tasks in a RESTful context [](task.html#12.1.2.1)

 In a RESTful context, a server functions as a repository of tasks. The server itself, or
 other agents are expected to monitor task activity and initiate appropriate actions to ensure
 task completion, updating the status of the task as it proceeds through its various stages of
 completion. These agents can be coordinated, following well choreographed business logic to
 ensure that tasks are completed. Task management may also be centrally controlled using some
 form of a workflow engine, in which case, the workflow engine itself may update and maintain the
 task resources in the server, and through its orchestration activities ensure that tasks are
 completed. The task resource enables either model of task management yet provides a
 consistent view of the status of tasks being executed in support of healthcare workflows. 

 
The assignment of tasks into categories by type of task, type of performer and task status
 enable the server to function as a queue of work items. This queue can be polled or subscribed
 to by various agents, enabling automation of workflows in FHIR using existing search and subscription
 mechanisms. Owners, requesters, other agents (e.g. workflow managers) can thus be ready to
 initiate the next steps in a complex workflow.

 
### 12.1.2.2 Tasks State Machine [
](task.html#12.1.2.2)

 Tasks start in a Created state. Once they have been assigned to an owner they transition to
 the Ready state, indicating that they are ready to be performed. Once the owner initiates
 activity on the task, the task transitions to the In Progress state, indicating that work is
 being performed. Upon normal completion, the task enters the Completed state. If there is a
 failure during the task execution that prevents the task from being completed, it can also
 enter a Failed state, indicating an abnormal termination of the task. A task in any
 non-terminal state may also be Cancelled, representing an abnormal termination of the task due
 to external forces, rather than an error condition.

 
Tasks in any non-terminal state (Created, Ready, In Progress) can be suspended and resumed.
 When a task is suspended, it is typically resumed in the state it was in when it was
 originally suspended. Suspending a task suspends all of its children as well. Resuming a task
 resumes all of its children.

 
An In-progress task can also be stopped, returning it to a Ready state. This may be in
 preparation for delegation or reassignment (e.g., because it cannot be completed by the
 current owner), to restart a task due to a temporary failure (e.g., to reattempt completion of
 the activity), or in preparation to allow others to claim the task.

 
 
The task history allows applications monitoring the state of a workflow to identify tasks
 that are long running, perhaps stuck in some queue, to enable management activities that could
 ensure completion. It also enables tracking of task statistics such as wait time, or time in
 progress, or time to completion, enabling capture of important task metrics in support of
 optimization and quality improvement. 

 **
 
 

 Note:** Currently, task pre-requisites can be represented using Task's `description` element or the [RequestGroup](requestgroup.html) resource. We are seeking input from the implementer community in evaluating whether there is need for adding another mechanism to this resource for this purpose.**
 

 

 Feedback [here ](https://chat.fhir.org/#narrow/stream/103-Orders-and.20Observation.20WG).
 

 

 

 

 
 
## 12.1.3 Boundaries and Relationships [
](task.html#bnr)

 Task spans both intent and event and tracks the execution through to
 completion. A Task is a workflow step such as cancelling an order,
 fulfilling an order, signing an order, merging a set of records, admitting a
 patient. In contrast, [Procedures](procedure.html) are actions
 that are intended to result in a physical or mental change to or for the
 subject (for example, surgery, physiotherapy, training, counseling). A Task resource
 often exists in parallel with clinical resources. For example, a Task could
 request fulfillment of a [ServiceRequest](servicerequest.html)
 ordering a Procedure that would result in a Procedure, [Observation](observation.html), [DiagnosticReport](diagnosticreport.html), [ImagingStudy](imagingstudy.html) or similar resource. Another
 example would be a Task that requests fulfillment of a [CommunicationRequest](communicationrequest.html) to be performed
 between various actors.

 
As stated above, the task resource tracks the state of a task, enabling
 systems to ensure that tasks are completed. This information is kept
 separate from the operational details necessary to complete the task, as
 those details vary across and even within workflows. That detail is expected
 to be carried in the referenced `focus` of the task. 

 
Tasks may have named inputs and outputs. Inputs represent
 information that may or must be present in order for a task to
 complete. Outputs represent intermediate or final results produced by a
 task. For example, in a task supporting reading of radiology image, the
 inputs might include both the imaging study to be read, as well as
 relevant prior images. Outputs could represent radiology measurements
 as well as the Radiologist's diagnostic report. 

 
Inputs and outputs are tracked by the task because workflow
 management activity may automate the transfer of outputs from one task
 to inputs to a subsequent task. 

 
To facilitate the integration of off the shelf workflow applications
 with FHIR, the task resource may reference a definition. This
 definition can represent a description of the workflow activity to be
 performed, using a standard workflow description language such as BPEL,
 BPMN, or XPDL, a workflow definition such as those defined in IHE
 profiles, or even simple written instructions explaining a process to be
 performed.

 

This resource is referenced by [CarePlan](careplan.html#CarePlan), [ImagingStudy](imagingstudy.html#ImagingStudy), [PaymentReconciliation](paymentreconciliation.html#PaymentReconciliation) and itself

## 12.1.4 
Resource Content
 [
](task.html#resource)

 

 - [Structure](#tabs-struc)

 - [UML](#tabs-uml)

 - [XML](#tabs-xml)

 - [JSON](#tabs-json)

 - [Turtle](#tabs-ttl)

 - [R3 Diff](#tabs-diff)

 - [All](#tabs-all)

 

 

Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Task](task-definitions.html#Task) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A task to be performed**+ Rule: Last modified date must be greater than or equal to authored-on date.
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](task-definitions.html#Task.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | Task Instance Identifier
 | |

| [instantiatesCanonical](task-definitions.html#Task.instantiatesCanonical) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html)) | Formal definition of task | |

| [instantiatesUri](task-definitions.html#Task.instantiatesUri) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [uri](datatypes.html#uri) | Formal definition of task | |

| [basedOn](task-definitions.html#Task.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Request fulfilled by this task
 | |

| [groupIdentifier](task-definitions.html#Task.groupIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Requisition or grouper id | |

| [partOf](task-definitions.html#Task.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Task](task.html)) | Composite task
 | |

| [status](task-definitions.html#Task.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | draft | requested | received | accepted | +
[TaskStatus](valueset-task-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](task-definitions.html#Task.statusReason) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status | |

| [businessStatus](task-definitions.html#Task.businessStatus) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | E.g. "Specimen collected", "IV prepped" | |

| [intent](task-definitions.html#Task.intent) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
[TaskIntent](valueset-task-intent.html) ([Required](terminologies.html#required)) | |

| [priority](task-definitions.html#Task.priority) | | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [code](task-definitions.html#Task.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Task Type
[Task Codes](valueset-task-code.html) ([Example](terminologies.html#example)) | |

| [description](task-definitions.html#Task.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human-readable explanation of task | |

| [focus](task-definitions.html#Task.focus) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | What task is acting on | |

| [for](task-definitions.html#Task.for) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Beneficiary of the Task | |

| [encounter](task-definitions.html#Task.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Healthcare event during which this task originated | |

| [executionPeriod](task-definitions.html#Task.executionPeriod) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Start and end time of execution | |

| [authoredOn](task-definitions.html#Task.authoredOn) | [I](conformance-rules.html#constraints) | 0..1 | [dateTime](datatypes.html#dateTime) | Task Creation Date | |

| [lastModified](task-definitions.html#Task.lastModified) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..1 | [dateTime](datatypes.html#dateTime) | Task Last Modified Date | |

| [requester](task-definitions.html#Task.requester) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html)) | Who is asking for task to be done | |

| [performerType](task-definitions.html#Task.performerType) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Requested performer
[Procedure Performer Role Codes](valueset-performer-role.html) ([Preferred](terminologies.html#preferred))
 | |

| [owner](task-definitions.html#Task.owner) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [CareTeam](careteam.html) | [HealthcareService](healthcareservice.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html)) | Responsible individual | |

| [location](task-definitions.html#Task.location) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Where task occurs | |

| [reasonCode](task-definitions.html#Task.reasonCode) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why task is needed | |

| [reasonReference](task-definitions.html#Task.reasonReference) | | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Why task is needed | |

| [insurance](task-definitions.html#Task.insurance) | | 0..* | [Reference](references.html#Reference)([Coverage](coverage.html) | [ClaimResponse](claimresponse.html)) | Associated insurance coverage
 | |

| [note](task-definitions.html#Task.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the task
 | |

| [relevantHistory](task-definitions.html#Task.relevantHistory) | | 0..* | [Reference](references.html#Reference)([Provenance](provenance.html)) | Key events in history of the Task
 | |

| [restriction](task-definitions.html#Task.restriction) | | 0..1 | [BackboneElement](backboneelement.html) | Constraints on fulfillment tasks | |

| [repetitions](task-definitions.html#Task.restriction.repetitions) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | How many times to repeat | |

| [period](task-definitions.html#Task.restriction.period) | | 0..1 | [Period](datatypes.html#Period) | When fulfillment sought | |

| [recipient](task-definitions.html#Task.restriction.recipient) | | 0..* | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Group](group.html) | [Organization](organization.html)) | For whom is fulfillment sought?
 | |

| [input](task-definitions.html#Task.input) | | 0..* | [BackboneElement](backboneelement.html) | Information used to perform task
 | |

| [type](task-definitions.html#Task.input.type) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Label for the input | |

| [value[x]](task-definitions.html#Task.input.value_x_) | | 1..1 | [*](datatypes.html#open) | Content to use in performing the task | |

| [output](task-definitions.html#Task.output) | | 0..* | [BackboneElement](backboneelement.html) | Information produced as part of task
 | |

| [type](task-definitions.html#Task.output.type) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Label for output | |

| [value[x]](task-definitions.html#Task.output.value_x_) | | 1..1 | [*](datatypes.html#open) | Result of output | |

| 
[ Documentation for this format](formats.html#table) | |

 

 

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Task ([DomainResource](domainresource.html))[The business identifier for this taskidentifier](task-definitions.html#Task.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskinstantiatesCanonical](task-definitions.html#Task.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..1] « [ActivityDefinition](activitydefinition.html#ActivityDefinition) »[The URL pointing to an *externally* maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskinstantiatesUri](task-definitions.html#Task.instantiatesUri) : [uri](datatypes.html#uri) [0..1][BasedOn refers to a higher-level authorization that triggered the creation of the task. It references a "request" resource such as a ServiceRequest, MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the "request" resource the task is seeking to fulfill. This latter resource is referenced by FocusOn. For example, based on a ServiceRequest (= BasedOn), a task is created to fulfill a procedureRequest ( = FocusOn ) to collect a specimen from a patientbasedOn](task-definitions.html#Task.basedOn) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[An identifier that links together multiple tasks and other requests that were created in the same contextgroupIdentifier](task-definitions.html#Task.groupIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][Task that this particular task is part ofpartOf](task-definitions.html#Task.partOf) : [Reference](references.html#Reference) [0..*] « [Task](task.html#Task) »[The current status of the task (this element modifies the meaning of other elements)status](task-definitions.html#Task.status) : [code](datatypes.html#code) [1..1] « [The current status of the task. (Strength=Required)TaskStatus](valueset-task-status.html)! »[An explanation as to why this task is held, failed, was refused, etcstatusReason](task-definitions.html#Task.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Contains business-specific nuances of the business statebusinessStatus](task-definitions.html#Task.businessStatus) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs this a proposed task, a planned task, an actionable task, etcintent](task-definitions.html#Task.intent) : [code](datatypes.html#code) [1..1] « [Distinguishes whether the task is a proposal, plan or full order. (Strength=Required)TaskIntent](valueset-task-intent.html)! »[Indicates how quickly the Task should be addressed with respect to other requestspriority](task-definitions.html#Task.priority) : [code](datatypes.html#code) [0..1] « [The task's priority. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[A name or code (or both) briefly describing what the task involvescode](task-definitions.html#Task.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes to identify what the task involves. These will typically be specific to a particular workflow. (Strength=Example)TaskCode](valueset-task-code.html)?? »[A free-text description of what is to be performeddescription](task-definitions.html#Task.description) : [string](datatypes.html#string) [0..1][The request being actioned or the resource being manipulated by this taskfocus](task-definitions.html#Task.focus) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[The entity who benefits from the performance of the service specified in the task (e.g., the patient)for](task-definitions.html#Task.for) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[The healthcare event (e.g. a patient and healthcare provider interaction) during which this task was createdencounter](task-definitions.html#Task.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Identifies the time action was first taken against the task (start) and/or the time final action was taken against the task prior to marking it as completed (end)executionPeriod](task-definitions.html#Task.executionPeriod) : [Period](datatypes.html#Period) [0..1][The date and time this task was createdauthoredOn](task-definitions.html#Task.authoredOn) : [dateTime](datatypes.html#dateTime) [0..1][The date and time of last modification to this tasklastModified](task-definitions.html#Task.lastModified) : [dateTime](datatypes.html#dateTime) [0..1][The creator of the taskrequester](task-definitions.html#Task.requester) : [Reference](references.html#Reference) [0..1] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)| [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson) »[The kind of participant that should perform the taskperformerType](task-definitions.html#Task.performerType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The type(s) of task performers allowed. (Strength=Preferred)ProcedurePerformerRoleCodes](valueset-performer-role.html)? »[Individual organization or Device currently responsible for task executionowner](task-definitions.html#Task.owner) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|[Device](device.html#Device)| [RelatedPerson](relatedperson.html#RelatedPerson) »[Principal physical location where the this task is performedlocation](task-definitions.html#Task.location) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location) »[A description or code indicating why this task needs to be performedreasonCode](task-definitions.html#Task.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][A resource reference indicating why this task needs to be performedreasonReference](task-definitions.html#Task.reasonReference) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be relevant to the Taskinsurance](task-definitions.html#Task.insurance) : [Reference](references.html#Reference) [0..*] « [Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse) »[Free-text information captured about the task as it progressesnote](task-definitions.html#Task.note) : [Annotation](datatypes.html#Annotation) [0..*][Links to Provenance records for past versions of this Task that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the taskrelevantHistory](task-definitions.html#Task.relevantHistory) : [Reference](references.html#Reference) [0..*] « [Provenance](provenance.html#Provenance) »Restriction[Indicates the number of times the requested action should occurrepetitions](task-definitions.html#Task.restriction.repetitions) : [positiveInt](datatypes.html#positiveInt) [0..1][Over what time-period is fulfillment soughtperiod](task-definitions.html#Task.restriction.period) : [Period](datatypes.html#Period) [0..1][For requests that are targeted to more than on potential recipient/target, for whom is fulfillment sought?recipient](task-definitions.html#Task.restriction.recipient) : [Reference](references.html#Reference) [0..*] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization) »Parameter[A code or description indicating how the input is intended to be used as part of the task executiontype](task-definitions.html#Task.input.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1][The value of the input parameter as a basic typevalue[x]](task-definitions.html#Task.input.value_x_) : [*](datatypes.html#open) [1..1]Output[The name of the Output parametertype](task-definitions.html#Task.output.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1][The value of the Output parameter as a basic typevalue[x]](task-definitions.html#Task.output.value_x_) : [*](datatypes.html#open) [1..1]
[If the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actionedrestriction](task-definitions.html#Task.restriction)[0..1][Additional information that may be needed in the execution of the taskinput](task-definitions.html#Task.input)[0..*][Outputs produced by the Taskoutput](task-definitions.html#Task.output)[0..*]
 

 

 

**XML Template**

 

 
```
<[**Task**](task-definitions.html#Task) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](task-definitions.html#Task.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Task Instance Identifier](terminologies.html#unbound) --></identifier>
 <[**instantiatesCanonical**](task-definitions.html#Task.instantiatesCanonical)><!-- **0..1** [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html#ActivityDefinition)) [Formal definition of task](terminologies.html#unbound) --></instantiatesCanonical>
 <[**instantiatesUri**](task-definitions.html#Task.instantiatesUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..1** [Formal definition of task](terminologies.html#unbound) -->
 <[**basedOn**](task-definitions.html#Task.basedOn)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Request fulfilled by this task](terminologies.html#unbound) --></basedOn>
 <[**groupIdentifier**](task-definitions.html#Task.groupIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Requisition or grouper id](terminologies.html#unbound) --></groupIdentifier>
 <[**partOf**](task-definitions.html#Task.partOf)><!-- **0..*** [Reference](references.html#Reference)([Task](task.html#Task)) [Composite task](terminologies.html#unbound) --></partOf>
 <[**status**](task-definitions.html#Task.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [draft | requested | received | accepted | +](valueset-task-status.html) -->
 <[**statusReason**](task-definitions.html#Task.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](terminologies.html#unbound) --></statusReason>
 <[**businessStatus**](task-definitions.html#Task.businessStatus)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [E.g. "Specimen collected", "IV prepped"](terminologies.html#unbound) --></businessStatus>
 <[**intent**](task-definitions.html#Task.intent) value="[[code](datatypes.html#code)]"/><!-- **1..1** [unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-task-intent.html) -->
 <[**priority**](task-definitions.html#Task.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**code**](task-definitions.html#Task.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Task Type](valueset-task-code.html) --></code>
 <[**description**](task-definitions.html#Task.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Human-readable explanation of task](terminologies.html#unbound) -->
 <[**focus**](task-definitions.html#Task.focus)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [What task is acting on](terminologies.html#unbound) --></focus>
 <[**for**](task-definitions.html#Task.for)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Beneficiary of the Task](terminologies.html#unbound) --></for>
 <[**encounter**](task-definitions.html#Task.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Healthcare event during which this task originated](terminologies.html#unbound) --></encounter>
 <[**executionPeriod**](task-definitions.html#Task.executionPeriod)><!-- **0..1** [Period](datatypes.html#Period) [Start and end time of execution](terminologies.html#unbound) --></executionPeriod>
 <[**authoredOn**](task-definitions.html#Task.authoredOn) value="[[dateTime](datatypes.html#dateTime)]"/><!-- ** 0..1** [Task Creation Date](terminologies.html#unbound) -->
 <[**lastModified**](task-definitions.html#Task.lastModified) value="[[dateTime](datatypes.html#dateTime)]"/><!-- ** 0..1** [Task Last Modified Date](terminologies.html#unbound) -->
 <[**requester**](task-definitions.html#Task.requester)><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Who is asking for task to be done](terminologies.html#unbound) --></requester>
 <[**performerType**](task-definitions.html#Task.performerType)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Requested performer](valueset-performer-role.html) --></performerType>
 <[**owner**](task-definitions.html#Task.owner)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Responsible individual](terminologies.html#unbound) --></owner>
 <[**location**](task-definitions.html#Task.location)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)) [Where task occurs](terminologies.html#unbound) --></location>
 <[**reasonCode**](task-definitions.html#Task.reasonCode)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Why task is needed](terminologies.html#unbound) --></reasonCode>
 <[**reasonReference**](task-definitions.html#Task.reasonReference)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Why task is needed](terminologies.html#unbound) --></reasonReference>
 <[**insurance**](task-definitions.html#Task.insurance)><!-- **0..*** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) [Associated insurance coverage](terminologies.html#unbound) --></insurance>
 <[**note**](task-definitions.html#Task.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the task](terminologies.html#unbound) --></note>
 <[**relevantHistory**](task-definitions.html#Task.relevantHistory)><!-- **0..*** [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) [Key events in history of the Task](terminologies.html#unbound) --></relevantHistory>
 <[**restriction**](task-definitions.html#Task.restriction)> <!-- **0..1** Constraints on fulfillment tasks -->
 <[**repetitions**](task-definitions.html#Task.restriction.repetitions) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [How many times to repeat](terminologies.html#unbound) -->
 <[**period**](task-definitions.html#Task.restriction.period)><!-- **0..1** [Period](datatypes.html#Period) [When fulfillment sought](terminologies.html#unbound) --></period>
 <[**recipient**](task-definitions.html#Task.restriction.recipient)><!-- **0..*** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization)) [For whom is fulfillment sought?](terminologies.html#unbound) --></recipient>
 </restriction>
 <[**input**](task-definitions.html#Task.input)> <!-- **0..*** Information used to perform task -->
 <[**type**](task-definitions.html#Task.input.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Label for the input](terminologies.html#unbound) --></type>
 <[**value[x]**](task-definitions.html#Task.input.value[x])><!-- **1..1** [*](datatypes.html#open) [Content to use in performing the task](terminologies.html#unbound) --></value[x]>
 </input>
 <[**output**](task-definitions.html#Task.output)> <!-- **0..*** Information produced as part of task -->
 <[**type**](task-definitions.html#Task.output.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Label for output](terminologies.html#unbound) --></type>
 <[**value[x]**](task-definitions.html#Task.output.value[x])><!-- **1..1** [*](datatypes.html#open) [Result of output](terminologies.html#unbound) --></value[x]>
 </output>
</Task>

```

 

 

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Task**](task-definitions.html#Task)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](task-definitions.html#Task.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Task Instance Identifier](terminologies.html#unbound)
 "[instantiatesCanonical](task-definitions.html#Task.instantiatesCanonical)" : { [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html#ActivityDefinition)) }, // [Formal definition of task](terminologies.html#unbound)
 "[instantiatesUri](task-definitions.html#Task.instantiatesUri)" : "<[uri](datatypes.html#uri)>", // [Formal definition of task](terminologies.html#unbound)
 "[basedOn](task-definitions.html#Task.basedOn)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Request fulfilled by this task](terminologies.html#unbound)
 "[groupIdentifier](task-definitions.html#Task.groupIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Requisition or grouper id](terminologies.html#unbound)
 "[partOf](task-definitions.html#Task.partOf)" : [{ [Reference](references.html#Reference)([Task](task.html#Task)) }], // [Composite task](terminologies.html#unbound)
 "[status](task-definitions.html#Task.status)" : "<[code](datatypes.html#code)>", // **R!** [draft | requested | received | accepted | +](valueset-task-status.html)
 "[statusReason](task-definitions.html#Task.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](terminologies.html#unbound)
 "[businessStatus](task-definitions.html#Task.businessStatus)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [E.g. "Specimen collected", "IV prepped"](terminologies.html#unbound)
 "[intent](task-definitions.html#Task.intent)" : "<[code](datatypes.html#code)>", // **R!** [unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-task-intent.html)
 "[priority](task-definitions.html#Task.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[code](task-definitions.html#Task.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Task Type](valueset-task-code.html)
 "[description](task-definitions.html#Task.description)" : "<[string](datatypes.html#string)>", // [Human-readable explanation of task](terminologies.html#unbound)
 "[focus](task-definitions.html#Task.focus)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [What task is acting on](terminologies.html#unbound)
 "[for](task-definitions.html#Task.for)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Beneficiary of the Task](terminologies.html#unbound)
 "[encounter](task-definitions.html#Task.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Healthcare event during which this task originated](terminologies.html#unbound)
 "[executionPeriod](task-definitions.html#Task.executionPeriod)" : { [Period](datatypes.html#Period) }, // [Start and end time of execution](terminologies.html#unbound)
 "[authoredOn](task-definitions.html#Task.authoredOn)" : "<[dateTime](datatypes.html#dateTime)>", // **C?** [Task Creation Date](terminologies.html#unbound)
 "[lastModified](task-definitions.html#Task.lastModified)" : "<[dateTime](datatypes.html#dateTime)>", // **C?** [Task Last Modified Date](terminologies.html#unbound)
 "[requester](task-definitions.html#Task.requester)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Who is asking for task to be done](terminologies.html#unbound)
 "[performerType](task-definitions.html#Task.performerType)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Requested performer](valueset-performer-role.html)
 "[owner](task-definitions.html#Task.owner)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Responsible individual](terminologies.html#unbound)
 "[location](task-definitions.html#Task.location)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // [Where task occurs](terminologies.html#unbound)
 "[reasonCode](task-definitions.html#Task.reasonCode)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Why task is needed](terminologies.html#unbound)
 "[reasonReference](task-definitions.html#Task.reasonReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Why task is needed](terminologies.html#unbound)
 "[insurance](task-definitions.html#Task.insurance)" : [{ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) }], // [Associated insurance coverage](terminologies.html#unbound)
 "[note](task-definitions.html#Task.note)" : [{ [Annotation](datatypes.html#Annotation) }], // [Comments made about the task](terminologies.html#unbound)
 "[relevantHistory](task-definitions.html#Task.relevantHistory)" : [{ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) }], // [Key events in history of the Task](terminologies.html#unbound)
 "[restriction](task-definitions.html#Task.restriction)" : { // [Constraints on fulfillment tasks](terminologies.html#unbound)
 "[repetitions](task-definitions.html#Task.restriction.repetitions)" : "<[positiveInt](datatypes.html#positiveInt)>", // [How many times to repeat](terminologies.html#unbound)
 "[period](task-definitions.html#Task.restriction.period)" : { [Period](datatypes.html#Period) }, // [When fulfillment sought](terminologies.html#unbound)
 "[recipient](task-definitions.html#Task.restriction.recipient)" : [{ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization)) }] // [For whom is fulfillment sought?](terminologies.html#unbound)
 },
 "[input](task-definitions.html#Task.input)" : [{ // [Information used to perform task](terminologies.html#unbound)
 "[type](task-definitions.html#Task.input.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Label for the input](terminologies.html#unbound)
 // value[x]: Content to use in performing the task. One of these 50:
 "[valueBase64Binary](task-definitions.html#Task.input.valueBase64Binary)" : "<[base64Binary](datatypes.html#base64Binary)>"
 "[valueBoolean](task-definitions.html#Task.input.valueBoolean)" : <[boolean](datatypes.html#boolean)>
 "[valueCanonical](task-definitions.html#Task.input.valueCanonical)" : "<[canonical](datatypes.html#canonical)>"
 "[valueCode](task-definitions.html#Task.input.valueCode)" : "<[code](datatypes.html#code)>"
 "[valueDate](task-definitions.html#Task.input.valueDate)" : "<[date](datatypes.html#date)>"
 "[valueDateTime](task-definitions.html#Task.input.valueDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[valueDecimal](task-definitions.html#Task.input.valueDecimal)" : <[decimal](datatypes.html#decimal)>
 "[valueId](task-definitions.html#Task.input.valueId)" : "<[id](datatypes.html#id)>"
 "[valueInstant](task-definitions.html#Task.input.valueInstant)" : "<[instant](datatypes.html#instant)>"
 "[valueInteger](task-definitions.html#Task.input.valueInteger)" : <[integer](datatypes.html#integer)>
 "[valueMarkdown](task-definitions.html#Task.input.valueMarkdown)" : "<[markdown](datatypes.html#markdown)>"
 "[valueOid](task-definitions.html#Task.input.valueOid)" : "<[oid](datatypes.html#oid)>"
 "[valuePositiveInt](task-definitions.html#Task.input.valuePositiveInt)" : "<[positiveInt](datatypes.html#positiveInt)>"
 "[valueString](task-definitions.html#Task.input.valueString)" : "<[string](datatypes.html#string)>"
 "[valueTime](task-definitions.html#Task.input.valueTime)" : "<[time](datatypes.html#time)>"
 "[valueUnsignedInt](task-definitions.html#Task.input.valueUnsignedInt)" : "<[unsignedInt](datatypes.html#unsignedInt)>"
 "[valueUri](task-definitions.html#Task.input.valueUri)" : "<[uri](datatypes.html#uri)>"
 "[valueUrl](task-definitions.html#Task.input.valueUrl)" : "<[url](datatypes.html#url)>"
 "[valueUuid](task-definitions.html#Task.input.valueUuid)" : "<[uuid](datatypes.html#uuid)>"
 "[valueAddress](task-definitions.html#Task.input.valueAddress)" : { [Address](datatypes.html#Address) }
 "[valueAge](task-definitions.html#Task.input.valueAge)" : { [Age](datatypes.html#Age) }
 "[valueAnnotation](task-definitions.html#Task.input.valueAnnotation)" : { [Annotation](datatypes.html#Annotation) }
 "[valueAttachment](task-definitions.html#Task.input.valueAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[valueCodeableConcept](task-definitions.html#Task.input.valueCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) }
 "[valueCoding](task-definitions.html#Task.input.valueCoding)" : { [Coding](datatypes.html#Coding) }
 "[valueContactPoint](task-definitions.html#Task.input.valueContactPoint)" : { [ContactPoint](datatypes.html#ContactPoint) }
 "[valueCount](task-definitions.html#Task.input.valueCount)" : { [Count](datatypes.html#Count) }
 "[valueDistance](task-definitions.html#Task.input.valueDistance)" : { [Distance](datatypes.html#Distance) }
 "[valueDuration](task-definitions.html#Task.input.valueDuration)" : { [Duration](datatypes.html#Duration) }
 "[valueHumanName](task-definitions.html#Task.input.valueHumanName)" : { [HumanName](datatypes.html#HumanName) }
 "[valueIdentifier](task-definitions.html#Task.input.valueIdentifier)" : { [Identifier](datatypes.html#Identifier) }
 "[valueMoney](task-definitions.html#Task.input.valueMoney)" : { [Money](datatypes.html#Money) }
 "[valuePeriod](task-definitions.html#Task.input.valuePeriod)" : { [Period](datatypes.html#Period) }
 "[valueQuantity](task-definitions.html#Task.input.valueQuantity)" : { [Quantity](datatypes.html#Quantity) }
 "[valueRange](task-definitions.html#Task.input.valueRange)" : { [Range](datatypes.html#Range) }
 "[valueRatio](task-definitions.html#Task.input.valueRatio)" : { [Ratio](datatypes.html#Ratio) }
 "[valueReference](task-definitions.html#Task.input.valueReference)" : { [Reference](references.html#Reference) }
 "[valueSampledData](task-definitions.html#Task.input.valueSampledData)" : { [SampledData](datatypes.html#SampledData) }
 "[valueSignature](task-definitions.html#Task.input.valueSignature)" : { [Signature](datatypes.html#Signature) }
 "[valueTiming](task-definitions.html#Task.input.valueTiming)" : { [Timing](datatypes.html#Timing) }
 "[valueContactDetail](task-definitions.html#Task.input.valueContactDetail)" : { [ContactDetail](metadatatypes.html#ContactDetail) }
 "[valueContributor](task-definitions.html#Task.input.valueContributor)" : { [Contributor](metadatatypes.html#Contributor) }
 "[valueDataRequirement](task-definitions.html#Task.input.valueDataRequirement)" : { [DataRequirement](metadatatypes.html#DataRequirement) }
 "[valueExpression](task-definitions.html#Task.input.valueExpression)" : { [Expression](metadatatypes.html#Expression) }
 "[valueParameterDefinition](task-definitions.html#Task.input.valueParameterDefinition)" : { [ParameterDefinition](metadatatypes.html#ParameterDefinition) }
 "[valueRelatedArtifact](task-definitions.html#Task.input.valueRelatedArtifact)" : { [RelatedArtifact](metadatatypes.html#RelatedArtifact) }
 "[valueTriggerDefinition](task-definitions.html#Task.input.valueTriggerDefinition)" : { [TriggerDefinition](metadatatypes.html#TriggerDefinition) }
 "[valueUsageContext](task-definitions.html#Task.input.valueUsageContext)" : { [UsageContext](metadatatypes.html#UsageContext) }
 "[valueDosage](task-definitions.html#Task.input.valueDosage)" : { [Dosage](dosage.html#Dosage) }
 "[valueMeta](task-definitions.html#Task.input.valueMeta)" : { [Meta](resource.html#Meta) }
 }],
 "[output](task-definitions.html#Task.output)" : [{ // [Information produced as part of task](terminologies.html#unbound)
 "[type](task-definitions.html#Task.output.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Label for output](terminologies.html#unbound)
 // value[x]: Result of output. One of these 50:
 "[valueBase64Binary](task-definitions.html#Task.output.valueBase64Binary)" : "<[base64Binary](datatypes.html#base64Binary)>"
 "[valueBoolean](task-definitions.html#Task.output.valueBoolean)" : <[boolean](datatypes.html#boolean)>
 "[valueCanonical](task-definitions.html#Task.output.valueCanonical)" : "<[canonical](datatypes.html#canonical)>"
 "[valueCode](task-definitions.html#Task.output.valueCode)" : "<[code](datatypes.html#code)>"
 "[valueDate](task-definitions.html#Task.output.valueDate)" : "<[date](datatypes.html#date)>"
 "[valueDateTime](task-definitions.html#Task.output.valueDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[valueDecimal](task-definitions.html#Task.output.valueDecimal)" : <[decimal](datatypes.html#decimal)>
 "[valueId](task-definitions.html#Task.output.valueId)" : "<[id](datatypes.html#id)>"
 "[valueInstant](task-definitions.html#Task.output.valueInstant)" : "<[instant](datatypes.html#instant)>"
 "[valueInteger](task-definitions.html#Task.output.valueInteger)" : <[integer](datatypes.html#integer)>
 "[valueMarkdown](task-definitions.html#Task.output.valueMarkdown)" : "<[markdown](datatypes.html#markdown)>"
 "[valueOid](task-definitions.html#Task.output.valueOid)" : "<[oid](datatypes.html#oid)>"
 "[valuePositiveInt](task-definitions.html#Task.output.valuePositiveInt)" : "<[positiveInt](datatypes.html#positiveInt)>"
 "[valueString](task-definitions.html#Task.output.valueString)" : "<[string](datatypes.html#string)>"
 "[valueTime](task-definitions.html#Task.output.valueTime)" : "<[time](datatypes.html#time)>"
 "[valueUnsignedInt](task-definitions.html#Task.output.valueUnsignedInt)" : "<[unsignedInt](datatypes.html#unsignedInt)>"
 "[valueUri](task-definitions.html#Task.output.valueUri)" : "<[uri](datatypes.html#uri)>"
 "[valueUrl](task-definitions.html#Task.output.valueUrl)" : "<[url](datatypes.html#url)>"
 "[valueUuid](task-definitions.html#Task.output.valueUuid)" : "<[uuid](datatypes.html#uuid)>"
 "[valueAddress](task-definitions.html#Task.output.valueAddress)" : { [Address](datatypes.html#Address) }
 "[valueAge](task-definitions.html#Task.output.valueAge)" : { [Age](datatypes.html#Age) }
 "[valueAnnotation](task-definitions.html#Task.output.valueAnnotation)" : { [Annotation](datatypes.html#Annotation) }
 "[valueAttachment](task-definitions.html#Task.output.valueAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[valueCodeableConcept](task-definitions.html#Task.output.valueCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) }
 "[valueCoding](task-definitions.html#Task.output.valueCoding)" : { [Coding](datatypes.html#Coding) }
 "[valueContactPoint](task-definitions.html#Task.output.valueContactPoint)" : { [ContactPoint](datatypes.html#ContactPoint) }
 "[valueCount](task-definitions.html#Task.output.valueCount)" : { [Count](datatypes.html#Count) }
 "[valueDistance](task-definitions.html#Task.output.valueDistance)" : { [Distance](datatypes.html#Distance) }
 "[valueDuration](task-definitions.html#Task.output.valueDuration)" : { [Duration](datatypes.html#Duration) }
 "[valueHumanName](task-definitions.html#Task.output.valueHumanName)" : { [HumanName](datatypes.html#HumanName) }
 "[valueIdentifier](task-definitions.html#Task.output.valueIdentifier)" : { [Identifier](datatypes.html#Identifier) }
 "[valueMoney](task-definitions.html#Task.output.valueMoney)" : { [Money](datatypes.html#Money) }
 "[valuePeriod](task-definitions.html#Task.output.valuePeriod)" : { [Period](datatypes.html#Period) }
 "[valueQuantity](task-definitions.html#Task.output.valueQuantity)" : { [Quantity](datatypes.html#Quantity) }
 "[valueRange](task-definitions.html#Task.output.valueRange)" : { [Range](datatypes.html#Range) }
 "[valueRatio](task-definitions.html#Task.output.valueRatio)" : { [Ratio](datatypes.html#Ratio) }
 "[valueReference](task-definitions.html#Task.output.valueReference)" : { [Reference](references.html#Reference) }
 "[valueSampledData](task-definitions.html#Task.output.valueSampledData)" : { [SampledData](datatypes.html#SampledData) }
 "[valueSignature](task-definitions.html#Task.output.valueSignature)" : { [Signature](datatypes.html#Signature) }
 "[valueTiming](task-definitions.html#Task.output.valueTiming)" : { [Timing](datatypes.html#Timing) }
 "[valueContactDetail](task-definitions.html#Task.output.valueContactDetail)" : { [ContactDetail](metadatatypes.html#ContactDetail) }
 "[valueContributor](task-definitions.html#Task.output.valueContributor)" : { [Contributor](metadatatypes.html#Contributor) }
 "[valueDataRequirement](task-definitions.html#Task.output.valueDataRequirement)" : { [DataRequirement](metadatatypes.html#DataRequirement) }
 "[valueExpression](task-definitions.html#Task.output.valueExpression)" : { [Expression](metadatatypes.html#Expression) }
 "[valueParameterDefinition](task-definitions.html#Task.output.valueParameterDefinition)" : { [ParameterDefinition](metadatatypes.html#ParameterDefinition) }
 "[valueRelatedArtifact](task-definitions.html#Task.output.valueRelatedArtifact)" : { [RelatedArtifact](metadatatypes.html#RelatedArtifact) }
 "[valueTriggerDefinition](task-definitions.html#Task.output.valueTriggerDefinition)" : { [TriggerDefinition](metadatatypes.html#TriggerDefinition) }
 "[valueUsageContext](task-definitions.html#Task.output.valueUsageContext)" : { [UsageContext](metadatatypes.html#UsageContext) }
 "[valueDosage](task-definitions.html#Task.output.valueDosage)" : { [Dosage](dosage.html#Dosage) }
 "[valueMeta](task-definitions.html#Task.output.valueMeta)" : { [Meta](resource.html#Meta) }
 }]
}

```

 

 

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Task**](task-definitions.html#Task);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Task.identifier](task-definitions.html#Task.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Task Instance Identifier
 fhir:[Task.instantiatesCanonical](task-definitions.html#Task.instantiatesCanonical) [ [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html#ActivityDefinition)) ]; # 0..1 Formal definition of task
 fhir:[Task.instantiatesUri](task-definitions.html#Task.instantiatesUri) [ [uri](datatypes.html#uri) ]; # 0..1 Formal definition of task
 fhir:[Task.basedOn](task-definitions.html#Task.basedOn) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Request fulfilled by this task
 fhir:[Task.groupIdentifier](task-definitions.html#Task.groupIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Requisition or grouper id
 fhir:[Task.partOf](task-definitions.html#Task.partOf) [ [Reference](references.html#Reference)([Task](task.html#Task)) ], ... ; # 0..* Composite task
 fhir:[Task.status](task-definitions.html#Task.status) [ [code](datatypes.html#code) ]; # 1..1 draft | requested | received | accepted | +
 fhir:[Task.statusReason](task-definitions.html#Task.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[Task.businessStatus](task-definitions.html#Task.businessStatus) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 E.g. "Specimen collected", "IV prepped"
 fhir:[Task.intent](task-definitions.html#Task.intent) [ [code](datatypes.html#code) ]; # 1..1 unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
 fhir:[Task.priority](task-definitions.html#Task.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[Task.code](task-definitions.html#Task.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Task Type
 fhir:[Task.description](task-definitions.html#Task.description) [ [string](datatypes.html#string) ]; # 0..1 Human-readable explanation of task
 fhir:[Task.focus](task-definitions.html#Task.focus) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 What task is acting on
 fhir:[Task.for](task-definitions.html#Task.for) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Beneficiary of the Task
 fhir:[Task.encounter](task-definitions.html#Task.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Healthcare event during which this task originated
 fhir:[Task.executionPeriod](task-definitions.html#Task.executionPeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Start and end time of execution
 fhir:[Task.authoredOn](task-definitions.html#Task.authoredOn) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Task Creation Date
 fhir:[Task.lastModified](task-definitions.html#Task.lastModified) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Task Last Modified Date
 fhir:[Task.requester](task-definitions.html#Task.requester) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Who is asking for task to be done
 fhir:[Task.performerType](task-definitions.html#Task.performerType) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Requested performer
 fhir:[Task.owner](task-definitions.html#Task.owner) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|
 [Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Responsible individual
 fhir:[Task.location](task-definitions.html#Task.location) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 0..1 Where task occurs
 fhir:[Task.reasonCode](task-definitions.html#Task.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Why task is needed
 fhir:[Task.reasonReference](task-definitions.html#Task.reasonReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Why task is needed
 fhir:[Task.insurance](task-definitions.html#Task.insurance) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) ], ... ; # 0..* Associated insurance coverage
 fhir:[Task.note](task-definitions.html#Task.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the task
 fhir:[Task.relevantHistory](task-definitions.html#Task.relevantHistory) [ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) ], ... ; # 0..* Key events in history of the Task
 fhir:[Task.restriction](task-definitions.html#Task.restriction) [ # 0..1 Constraints on fulfillment tasks
 fhir:[Task.restriction.repetitions](task-definitions.html#Task.restriction.repetitions) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 How many times to repeat
 fhir:[Task.restriction.period](task-definitions.html#Task.restriction.period) [ [Period](datatypes.html#Period) ]; # 0..1 When fulfillment sought
 fhir:[Task.restriction.recipient](task-definitions.html#Task.restriction.recipient) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization)) ], ... ; # 0..* For whom is fulfillment sought?
 ];
 fhir:[Task.input](task-definitions.html#Task.input) [ # 0..* Information used to perform task
 fhir:[Task.input.type](task-definitions.html#Task.input.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Label for the input
 # [Task.input.value[x]](task-definitions.html#Task.input.value[x]) : 1..1 Content to use in performing the task. One of these 50
 fhir:[Task.input.valueBase64Binary](task-definitions.html#Task.input.valueBase64Binary) [ [base64Binary](datatypes.html#base64Binary) ]
 fhir:[Task.input.valueBoolean](task-definitions.html#Task.input.valueBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Task.input.valueCanonical](task-definitions.html#Task.input.valueCanonical) [ [canonical](datatypes.html#canonical) ]
 fhir:[Task.input.valueCode](task-definitions.html#Task.input.valueCode) [ [code](datatypes.html#code) ]
 fhir:[Task.input.valueDate](task-definitions.html#Task.input.valueDate) [ [date](datatypes.html#date) ]
 fhir:[Task.input.valueDateTime](task-definitions.html#Task.input.valueDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Task.input.valueDecimal](task-definitions.html#Task.input.valueDecimal) [ [decimal](datatypes.html#decimal) ]
 fhir:[Task.input.valueId](task-definitions.html#Task.input.valueId) [ [id](datatypes.html#id) ]
 fhir:[Task.input.valueInstant](task-definitions.html#Task.input.valueInstant) [ [instant](datatypes.html#instant) ]
 fhir:[Task.input.valueInteger](task-definitions.html#Task.input.valueInteger) [ [integer](datatypes.html#integer) ]
 fhir:[Task.input.valueMarkdown](task-definitions.html#Task.input.valueMarkdown) [ [markdown](datatypes.html#markdown) ]
 fhir:[Task.input.valueOid](task-definitions.html#Task.input.valueOid) [ [oid](datatypes.html#oid) ]
 fhir:[Task.input.valuePositiveInt](task-definitions.html#Task.input.valuePositiveInt) [ [positiveInt](datatypes.html#positiveInt) ]
 fhir:[Task.input.valueString](task-definitions.html#Task.input.valueString) [ [string](datatypes.html#string) ]
 fhir:[Task.input.valueTime](task-definitions.html#Task.input.valueTime) [ [time](datatypes.html#time) ]
 fhir:[Task.input.valueUnsignedInt](task-definitions.html#Task.input.valueUnsignedInt) [ [unsignedInt](datatypes.html#unsignedInt) ]
 fhir:[Task.input.valueUri](task-definitions.html#Task.input.valueUri) [ [uri](datatypes.html#uri) ]
 fhir:[Task.input.valueUrl](task-definitions.html#Task.input.valueUrl) [ [url](datatypes.html#url) ]
 fhir:[Task.input.valueUuid](task-definitions.html#Task.input.valueUuid) [ [uuid](datatypes.html#uuid) ]
 fhir:[Task.input.valueAddress](task-definitions.html#Task.input.valueAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Task.input.valueAge](task-definitions.html#Task.input.valueAge) [ [Age](datatypes.html#Age) ]
 fhir:[Task.input.valueAnnotation](task-definitions.html#Task.input.valueAnnotation) [ [Annotation](datatypes.html#Annotation) ]
 fhir:[Task.input.valueAttachment](task-definitions.html#Task.input.valueAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Task.input.valueCodeableConcept](task-definitions.html#Task.input.valueCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Task.input.valueCoding](task-definitions.html#Task.input.valueCoding) [ [Coding](datatypes.html#Coding) ]
 fhir:[Task.input.valueContactPoint](task-definitions.html#Task.input.valueContactPoint) [ [ContactPoint](datatypes.html#ContactPoint) ]
 fhir:[Task.input.valueCount](task-definitions.html#Task.input.valueCount) [ [Count](datatypes.html#Count) ]
 fhir:[Task.input.valueDistance](task-definitions.html#Task.input.valueDistance) [ [Distance](datatypes.html#Distance) ]
 fhir:[Task.input.valueDuration](task-definitions.html#Task.input.valueDuration) [ [Duration](datatypes.html#Duration) ]
 fhir:[Task.input.valueHumanName](task-definitions.html#Task.input.valueHumanName) [ [HumanName](datatypes.html#HumanName) ]
 fhir:[Task.input.valueIdentifier](task-definitions.html#Task.input.valueIdentifier) [ [Identifier](datatypes.html#Identifier) ]
 fhir:[Task.input.valueMoney](task-definitions.html#Task.input.valueMoney) [ [Money](datatypes.html#Money) ]
 fhir:[Task.input.valuePeriod](task-definitions.html#Task.input.valuePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[Task.input.valueQuantity](task-definitions.html#Task.input.valueQuantity) [ [Quantity](datatypes.html#Quantity) ]
 fhir:[Task.input.valueRange](task-definitions.html#Task.input.valueRange) [ [Range](datatypes.html#Range) ]
 fhir:[Task.input.valueRatio](task-definitions.html#Task.input.valueRatio) [ [Ratio](datatypes.html#Ratio) ]
 fhir:[Task.input.valueReference](task-definitions.html#Task.input.valueReference) [ [Reference](references.html#Reference) ]
 fhir:[Task.input.valueSampledData](task-definitions.html#Task.input.valueSampledData) [ [SampledData](datatypes.html#SampledData) ]
 fhir:[Task.input.valueSignature](task-definitions.html#Task.input.valueSignature) [ [Signature](datatypes.html#Signature) ]
 fhir:[Task.input.valueTiming](task-definitions.html#Task.input.valueTiming) [ [Timing](datatypes.html#Timing) ]
 fhir:[Task.input.valueContactDetail](task-definitions.html#Task.input.valueContactDetail) [ [ContactDetail](metadatatypes.html#ContactDetail) ]
 fhir:[Task.input.valueContributor](task-definitions.html#Task.input.valueContributor) [ [Contributor](metadatatypes.html#Contributor) ]
 fhir:[Task.input.valueDataRequirement](task-definitions.html#Task.input.valueDataRequirement) [ [DataRequirement](metadatatypes.html#DataRequirement) ]
 fhir:[Task.input.valueExpression](task-definitions.html#Task.input.valueExpression) [ [Expression](metadatatypes.html#Expression) ]
 fhir:[Task.input.valueParameterDefinition](task-definitions.html#Task.input.valueParameterDefinition) [ [ParameterDefinition](metadatatypes.html#ParameterDefinition) ]
 fhir:[Task.input.valueRelatedArtifact](task-definitions.html#Task.input.valueRelatedArtifact) [ [RelatedArtifact](metadatatypes.html#RelatedArtifact) ]
 fhir:[Task.input.valueTriggerDefinition](task-definitions.html#Task.input.valueTriggerDefinition) [ [TriggerDefinition](metadatatypes.html#TriggerDefinition) ]
 fhir:[Task.input.valueUsageContext](task-definitions.html#Task.input.valueUsageContext) [ [UsageContext](metadatatypes.html#UsageContext) ]
 fhir:[Task.input.valueDosage](task-definitions.html#Task.input.valueDosage) [ [Dosage](dosage.html#Dosage) ]
 fhir:[Task.input.valueMeta](task-definitions.html#Task.input.valueMeta) [ [Meta](resource.html#Meta) ]
 ], ...;
 fhir:[Task.output](task-definitions.html#Task.output) [ # 0..* Information produced as part of task
 fhir:[Task.output.type](task-definitions.html#Task.output.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Label for output
 # [Task.output.value[x]](task-definitions.html#Task.output.value[x]) : 1..1 Result of output. One of these 50
 fhir:[Task.output.valueBase64Binary](task-definitions.html#Task.output.valueBase64Binary) [ [base64Binary](datatypes.html#base64Binary) ]
 fhir:[Task.output.valueBoolean](task-definitions.html#Task.output.valueBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Task.output.valueCanonical](task-definitions.html#Task.output.valueCanonical) [ [canonical](datatypes.html#canonical) ]
 fhir:[Task.output.valueCode](task-definitions.html#Task.output.valueCode) [ [code](datatypes.html#code) ]
 fhir:[Task.output.valueDate](task-definitions.html#Task.output.valueDate) [ [date](datatypes.html#date) ]
 fhir:[Task.output.valueDateTime](task-definitions.html#Task.output.valueDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Task.output.valueDecimal](task-definitions.html#Task.output.valueDecimal) [ [decimal](datatypes.html#decimal) ]
 fhir:[Task.output.valueId](task-definitions.html#Task.output.valueId) [ [id](datatypes.html#id) ]
 fhir:[Task.output.valueInstant](task-definitions.html#Task.output.valueInstant) [ [instant](datatypes.html#instant) ]
 fhir:[Task.output.valueInteger](task-definitions.html#Task.output.valueInteger) [ [integer](datatypes.html#integer) ]
 fhir:[Task.output.valueMarkdown](task-definitions.html#Task.output.valueMarkdown) [ [markdown](datatypes.html#markdown) ]
 fhir:[Task.output.valueOid](task-definitions.html#Task.output.valueOid) [ [oid](datatypes.html#oid) ]
 fhir:[Task.output.valuePositiveInt](task-definitions.html#Task.output.valuePositiveInt) [ [positiveInt](datatypes.html#positiveInt) ]
 fhir:[Task.output.valueString](task-definitions.html#Task.output.valueString) [ [string](datatypes.html#string) ]
 fhir:[Task.output.valueTime](task-definitions.html#Task.output.valueTime) [ [time](datatypes.html#time) ]
 fhir:[Task.output.valueUnsignedInt](task-definitions.html#Task.output.valueUnsignedInt) [ [unsignedInt](datatypes.html#unsignedInt) ]
 fhir:[Task.output.valueUri](task-definitions.html#Task.output.valueUri) [ [uri](datatypes.html#uri) ]
 fhir:[Task.output.valueUrl](task-definitions.html#Task.output.valueUrl) [ [url](datatypes.html#url) ]
 fhir:[Task.output.valueUuid](task-definitions.html#Task.output.valueUuid) [ [uuid](datatypes.html#uuid) ]
 fhir:[Task.output.valueAddress](task-definitions.html#Task.output.valueAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Task.output.valueAge](task-definitions.html#Task.output.valueAge) [ [Age](datatypes.html#Age) ]
 fhir:[Task.output.valueAnnotation](task-definitions.html#Task.output.valueAnnotation) [ [Annotation](datatypes.html#Annotation) ]
 fhir:[Task.output.valueAttachment](task-definitions.html#Task.output.valueAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Task.output.valueCodeableConcept](task-definitions.html#Task.output.valueCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Task.output.valueCoding](task-definitions.html#Task.output.valueCoding) [ [Coding](datatypes.html#Coding) ]
 fhir:[Task.output.valueContactPoint](task-definitions.html#Task.output.valueContactPoint) [ [ContactPoint](datatypes.html#ContactPoint) ]
 fhir:[Task.output.valueCount](task-definitions.html#Task.output.valueCount) [ [Count](datatypes.html#Count) ]
 fhir:[Task.output.valueDistance](task-definitions.html#Task.output.valueDistance) [ [Distance](datatypes.html#Distance) ]
 fhir:[Task.output.valueDuration](task-definitions.html#Task.output.valueDuration) [ [Duration](datatypes.html#Duration) ]
 fhir:[Task.output.valueHumanName](task-definitions.html#Task.output.valueHumanName) [ [HumanName](datatypes.html#HumanName) ]
 fhir:[Task.output.valueIdentifier](task-definitions.html#Task.output.valueIdentifier) [ [Identifier](datatypes.html#Identifier) ]
 fhir:[Task.output.valueMoney](task-definitions.html#Task.output.valueMoney) [ [Money](datatypes.html#Money) ]
 fhir:[Task.output.valuePeriod](task-definitions.html#Task.output.valuePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[Task.output.valueQuantity](task-definitions.html#Task.output.valueQuantity) [ [Quantity](datatypes.html#Quantity) ]
 fhir:[Task.output.valueRange](task-definitions.html#Task.output.valueRange) [ [Range](datatypes.html#Range) ]
 fhir:[Task.output.valueRatio](task-definitions.html#Task.output.valueRatio) [ [Ratio](datatypes.html#Ratio) ]
 fhir:[Task.output.valueReference](task-definitions.html#Task.output.valueReference) [ [Reference](references.html#Reference) ]
 fhir:[Task.output.valueSampledData](task-definitions.html#Task.output.valueSampledData) [ [SampledData](datatypes.html#SampledData) ]
 fhir:[Task.output.valueSignature](task-definitions.html#Task.output.valueSignature) [ [Signature](datatypes.html#Signature) ]
 fhir:[Task.output.valueTiming](task-definitions.html#Task.output.valueTiming) [ [Timing](datatypes.html#Timing) ]
 fhir:[Task.output.valueContactDetail](task-definitions.html#Task.output.valueContactDetail) [ [ContactDetail](metadatatypes.html#ContactDetail) ]
 fhir:[Task.output.valueContributor](task-definitions.html#Task.output.valueContributor) [ [Contributor](metadatatypes.html#Contributor) ]
 fhir:[Task.output.valueDataRequirement](task-definitions.html#Task.output.valueDataRequirement) [ [DataRequirement](metadatatypes.html#DataRequirement) ]
 fhir:[Task.output.valueExpression](task-definitions.html#Task.output.valueExpression) [ [Expression](metadatatypes.html#Expression) ]
 fhir:[Task.output.valueParameterDefinition](task-definitions.html#Task.output.valueParameterDefinition) [ [ParameterDefinition](metadatatypes.html#ParameterDefinition) ]
 fhir:[Task.output.valueRelatedArtifact](task-definitions.html#Task.output.valueRelatedArtifact) [ [RelatedArtifact](metadatatypes.html#RelatedArtifact) ]
 fhir:[Task.output.valueTriggerDefinition](task-definitions.html#Task.output.valueTriggerDefinition) [ [TriggerDefinition](metadatatypes.html#TriggerDefinition) ]
 fhir:[Task.output.valueUsageContext](task-definitions.html#Task.output.valueUsageContext) [ [UsageContext](metadatatypes.html#UsageContext) ]
 fhir:[Task.output.valueDosage](task-definitions.html#Task.output.valueDosage) [ [Dosage](dosage.html#Dosage) ]
 fhir:[Task.output.valueMeta](task-definitions.html#Task.output.valueMeta) [ [Meta](resource.html#Meta) ]
 ], ...;
]

```

 

 

 

**Changes since R3**

 

 

 | 
 
 [Task](task.html#Task)
 | 
 | 
 |

 | 
 Task.instantiatesCanonical | 
 
 

 Added Element

 

 | 
 |

 | 
 Task.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/task-status to http://hl7.org/fhir/ValueSet/task-status|4.0.1

 - Now marked as Modifier

 

 | 
 |

 | 
 Task.intent | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/request-intent to http://hl7.org/fhir/ValueSet/task-intent|4.0.1

 

 | 
 |

 | 
 Task.priority | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/request-priority to http://hl7.org/fhir/ValueSet/request-priority|4.0.1

 

 | 
 |

 | 
 Task.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.requester | 
 
 

 - Type changed from BackboneElement to Reference(Device | Organization | Patient | Practitioner | PractitionerRole | RelatedPerson)

 

 | 
 |

 | 
 Task.owner | 
 
 

 - Type Reference: Added Target Types PractitionerRole, CareTeam, HealthcareService

 

 | 
 |

 | 
 Task.location | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.reasonCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.reasonReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.insurance | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.restriction.recipient | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Task.input.value[x] | 
 
 

 - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage

 

 | 
 |

 | 
 Task.output.value[x] | 
 
 

 - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage

 

 | 
 |

 | 
 Task.definition[x] | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.context | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.requester.agent | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.requester.onBehalfOf | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.reason | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](task.diff.xml) or [JSON](task.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](task-version-maps.html) (status = 6 tests that all execute ok. 3 fail round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

**Structure**

 

 
| [Name](formats.html#table) | [Flags](formats.html#table) | [Card.](formats.html#table) | [Type](formats.html#table) | [Description & Constraints](formats.html#table)[](formats.html#table) | |
| [Task](task-definitions.html#Task) | [I](conformance-rules.html#constraints)[TU](versions.html#std-process) | | [DomainResource](domainresource.html) | A task to be performed**+ Rule: Last modified date must be greater than or equal to authored-on date.
Elements defined in Ancestors: [id](resource.html#Resource), [meta](resource.html#Resource), [implicitRules](resource.html#Resource), [language](resource.html#Resource), [text](domainresource.html#DomainResource), [contained](domainresource.html#DomainResource), [extension](domainresource.html#DomainResource), [modifierExtension](domainresource.html#DomainResource) | |

| [identifier](task-definitions.html#Task.identifier) | | 0..* | [Identifier](datatypes.html#Identifier) | Task Instance Identifier
 | |

| [instantiatesCanonical](task-definitions.html#Task.instantiatesCanonical) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html)) | Formal definition of task | |

| [instantiatesUri](task-definitions.html#Task.instantiatesUri) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [uri](datatypes.html#uri) | Formal definition of task | |

| [basedOn](task-definitions.html#Task.basedOn) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Any](resourcelist.html)) | Request fulfilled by this task
 | |

| [groupIdentifier](task-definitions.html#Task.groupIdentifier) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Identifier](datatypes.html#Identifier) | Requisition or grouper id | |

| [partOf](task-definitions.html#Task.partOf) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..* | [Reference](references.html#Reference)([Task](task.html)) | Composite task
 | |

| [status](task-definitions.html#Task.status) | [?!](conformance-rules.html#isModifier)[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | draft | requested | received | accepted | +
[TaskStatus](valueset-task-status.html) ([Required](terminologies.html#required)) | |

| [statusReason](task-definitions.html#Task.statusReason) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Reason for current status | |

| [businessStatus](task-definitions.html#Task.businessStatus) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | E.g. "Specimen collected", "IV prepped" | |

| [intent](task-definitions.html#Task.intent) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 1..1 | [code](datatypes.html#code) | unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
[TaskIntent](valueset-task-intent.html) ([Required](terminologies.html#required)) | |

| [priority](task-definitions.html#Task.priority) | | 0..1 | [code](datatypes.html#code) | routine | urgent | asap | stat
[Request priority](valueset-request-priority.html) ([Required](terminologies.html#required)) | |

| [code](task-definitions.html#Task.code) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Task Type
[Task Codes](valueset-task-code.html) ([Example](terminologies.html#example)) | |

| [description](task-definitions.html#Task.description) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [string](datatypes.html#string) | Human-readable explanation of task | |

| [focus](task-definitions.html#Task.focus) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | What task is acting on | |

| [for](task-definitions.html#Task.for) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Beneficiary of the Task | |

| [encounter](task-definitions.html#Task.encounter) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Encounter](encounter.html)) | Healthcare event during which this task originated | |

| [executionPeriod](task-definitions.html#Task.executionPeriod) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Period](datatypes.html#Period) | Start and end time of execution | |

| [authoredOn](task-definitions.html#Task.authoredOn) | [I](conformance-rules.html#constraints) | 0..1 | [dateTime](datatypes.html#dateTime) | Task Creation Date | |

| [lastModified](task-definitions.html#Task.lastModified) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary)[I](conformance-rules.html#constraints) | 0..1 | [dateTime](datatypes.html#dateTime) | Task Last Modified Date | |

| [requester](task-definitions.html#Task.requester) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Device](device.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html)) | Who is asking for task to be done | |

| [performerType](task-definitions.html#Task.performerType) | | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Requested performer
[Procedure Performer Role Codes](valueset-performer-role.html) ([Preferred](terminologies.html#preferred))
 | |

| [owner](task-definitions.html#Task.owner) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [Organization](organization.html) | [CareTeam](careteam.html) | [HealthcareService](healthcareservice.html) | [Patient](patient.html) | [Device](device.html) | [RelatedPerson](relatedperson.html)) | Responsible individual | |

| [location](task-definitions.html#Task.location) | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary) | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Where task occurs | |

| [reasonCode](task-definitions.html#Task.reasonCode) | | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Why task is needed | |

| [reasonReference](task-definitions.html#Task.reasonReference) | | 0..1 | [Reference](references.html#Reference)([Any](resourcelist.html)) | Why task is needed | |

| [insurance](task-definitions.html#Task.insurance) | | 0..* | [Reference](references.html#Reference)([Coverage](coverage.html) | [ClaimResponse](claimresponse.html)) | Associated insurance coverage
 | |

| [note](task-definitions.html#Task.note) | | 0..* | [Annotation](datatypes.html#Annotation) | Comments made about the task
 | |

| [relevantHistory](task-definitions.html#Task.relevantHistory) | | 0..* | [Reference](references.html#Reference)([Provenance](provenance.html)) | Key events in history of the Task
 | |

| [restriction](task-definitions.html#Task.restriction) | | 0..1 | [BackboneElement](backboneelement.html) | Constraints on fulfillment tasks | |

| [repetitions](task-definitions.html#Task.restriction.repetitions) | | 0..1 | [positiveInt](datatypes.html#positiveInt) | How many times to repeat | |

| [period](task-definitions.html#Task.restriction.period) | | 0..1 | [Period](datatypes.html#Period) | When fulfillment sought | |

| [recipient](task-definitions.html#Task.restriction.recipient) | | 0..* | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [PractitionerRole](practitionerrole.html) | [RelatedPerson](relatedperson.html) | [Group](group.html) | [Organization](organization.html)) | For whom is fulfillment sought?
 | |

| [input](task-definitions.html#Task.input) | | 0..* | [BackboneElement](backboneelement.html) | Information used to perform task
 | |

| [type](task-definitions.html#Task.input.type) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Label for the input | |

| [value[x]](task-definitions.html#Task.input.value_x_) | | 1..1 | [*](datatypes.html#open) | Content to use in performing the task | |

| [output](task-definitions.html#Task.output) | | 0..* | [BackboneElement](backboneelement.html) | Information produced as part of task
 | |

| [type](task-definitions.html#Task.output.type) | | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Label for output | |

| [value[x]](task-definitions.html#Task.output.value_x_) | | 1..1 | [*](datatypes.html#open) | Result of output | |

| 
[ Documentation for this format](formats.html#table) | |

 

UML Diagram** ([Legend](formats.html#uml))

 

 
 
 
 
 
 
 
 - Task ([DomainResource](domainresource.html))[The business identifier for this taskidentifier](task-definitions.html#Task.identifier) : [Identifier](datatypes.html#Identifier) [0..*][The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskinstantiatesCanonical](task-definitions.html#Task.instantiatesCanonical) : [canonical](datatypes.html#canonical) [0..1] « [ActivityDefinition](activitydefinition.html#ActivityDefinition) »[The URL pointing to an *externally* maintained protocol, guideline, orderset or other definition that is adhered to in whole or in part by this TaskinstantiatesUri](task-definitions.html#Task.instantiatesUri) : [uri](datatypes.html#uri) [0..1][BasedOn refers to a higher-level authorization that triggered the creation of the task. It references a "request" resource such as a ServiceRequest, MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the "request" resource the task is seeking to fulfill. This latter resource is referenced by FocusOn. For example, based on a ServiceRequest (= BasedOn), a task is created to fulfill a procedureRequest ( = FocusOn ) to collect a specimen from a patientbasedOn](task-definitions.html#Task.basedOn) : [Reference](references.html#Reference) [0..*] « [Any](resourcelist.html#Any) »[An identifier that links together multiple tasks and other requests that were created in the same contextgroupIdentifier](task-definitions.html#Task.groupIdentifier) : [Identifier](datatypes.html#Identifier) [0..1][Task that this particular task is part ofpartOf](task-definitions.html#Task.partOf) : [Reference](references.html#Reference) [0..*] « [Task](task.html#Task) »[The current status of the task (this element modifies the meaning of other elements)status](task-definitions.html#Task.status) : [code](datatypes.html#code) [1..1] « [The current status of the task. (Strength=Required)TaskStatus](valueset-task-status.html)! »[An explanation as to why this task is held, failed, was refused, etcstatusReason](task-definitions.html#Task.statusReason) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Contains business-specific nuances of the business statebusinessStatus](task-definitions.html#Task.businessStatus) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs this a proposed task, a planned task, an actionable task, etcintent](task-definitions.html#Task.intent) : [code](datatypes.html#code) [1..1] « [Distinguishes whether the task is a proposal, plan or full order. (Strength=Required)TaskIntent](valueset-task-intent.html)! »[Indicates how quickly the Task should be addressed with respect to other requestspriority](task-definitions.html#Task.priority) : [code](datatypes.html#code) [0..1] « [The task's priority. (Strength=Required)RequestPriority](valueset-request-priority.html)! »[A name or code (or both) briefly describing what the task involvescode](task-definitions.html#Task.code) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1] « [Codes to identify what the task involves. These will typically be specific to a particular workflow. (Strength=Example)TaskCode](valueset-task-code.html)?? »[A free-text description of what is to be performeddescription](task-definitions.html#Task.description) : [string](datatypes.html#string) [0..1][The request being actioned or the resource being manipulated by this taskfocus](task-definitions.html#Task.focus) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[The entity who benefits from the performance of the service specified in the task (e.g., the patient)for](task-definitions.html#Task.for) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[The healthcare event (e.g. a patient and healthcare provider interaction) during which this task was createdencounter](task-definitions.html#Task.encounter) : [Reference](references.html#Reference) [0..1] « [Encounter](encounter.html#Encounter) »[Identifies the time action was first taken against the task (start) and/or the time final action was taken against the task prior to marking it as completed (end)executionPeriod](task-definitions.html#Task.executionPeriod) : [Period](datatypes.html#Period) [0..1][The date and time this task was createdauthoredOn](task-definitions.html#Task.authoredOn) : [dateTime](datatypes.html#dateTime) [0..1][The date and time of last modification to this tasklastModified](task-definitions.html#Task.lastModified) : [dateTime](datatypes.html#dateTime) [0..1][The creator of the taskrequester](task-definitions.html#Task.requester) : [Reference](references.html#Reference) [0..1] « [Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)| [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson) »[The kind of participant that should perform the taskperformerType](task-definitions.html#Task.performerType) : [CodeableConcept](datatypes.html#CodeableConcept) [0..*] « [The type(s) of task performers allowed. (Strength=Preferred)ProcedurePerformerRoleCodes](valueset-performer-role.html)? »[Individual organization or Device currently responsible for task executionowner](task-definitions.html#Task.owner) : [Reference](references.html#Reference) [0..1] « [Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|[Device](device.html#Device)| [RelatedPerson](relatedperson.html#RelatedPerson) »[Principal physical location where the this task is performedlocation](task-definitions.html#Task.location) : [Reference](references.html#Reference) [0..1] « [Location](location.html#Location) »[A description or code indicating why this task needs to be performedreasonCode](task-definitions.html#Task.reasonCode) : [CodeableConcept](datatypes.html#CodeableConcept) [0..1][A resource reference indicating why this task needs to be performedreasonReference](task-definitions.html#Task.reasonReference) : [Reference](references.html#Reference) [0..1] « [Any](resourcelist.html#Any) »[Insurance plans, coverage extensions, pre-authorizations and/or pre-determinations that may be relevant to the Taskinsurance](task-definitions.html#Task.insurance) : [Reference](references.html#Reference) [0..*] « [Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse) »[Free-text information captured about the task as it progressesnote](task-definitions.html#Task.note) : [Annotation](datatypes.html#Annotation) [0..*][Links to Provenance records for past versions of this Task that identify key state transitions or updates that are likely to be relevant to a user looking at the current version of the taskrelevantHistory](task-definitions.html#Task.relevantHistory) : [Reference](references.html#Reference) [0..*] « [Provenance](provenance.html#Provenance) »Restriction[Indicates the number of times the requested action should occurrepetitions](task-definitions.html#Task.restriction.repetitions) : [positiveInt](datatypes.html#positiveInt) [0..1][Over what time-period is fulfillment soughtperiod](task-definitions.html#Task.restriction.period) : [Period](datatypes.html#Period) [0..1][For requests that are targeted to more than on potential recipient/target, for whom is fulfillment sought?recipient](task-definitions.html#Task.restriction.recipient) : [Reference](references.html#Reference) [0..*] « [Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)| [RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization) »Parameter[A code or description indicating how the input is intended to be used as part of the task executiontype](task-definitions.html#Task.input.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1][The value of the input parameter as a basic typevalue[x]](task-definitions.html#Task.input.value_x_) : [*](datatypes.html#open) [1..1]Output[The name of the Output parametertype](task-definitions.html#Task.output.type) : [CodeableConcept](datatypes.html#CodeableConcept) [1..1][The value of the Output parameter as a basic typevalue[x]](task-definitions.html#Task.output.value_x_) : [*](datatypes.html#open) [1..1]
[If the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actionedrestriction](task-definitions.html#Task.restriction)[0..1][Additional information that may be needed in the execution of the taskinput](task-definitions.html#Task.input)[0..*][Outputs produced by the Taskoutput](task-definitions.html#Task.output)[0..*]
 

**XML Template**

 

 
```
<[**Task**](task-definitions.html#Task) xmlns="http://hl7.org/fhir"> [](xml.html)
 <!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) -->
 <!-- from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension) -->
 <[**identifier**](task-definitions.html#Task.identifier)><!-- **0..*** [Identifier](datatypes.html#Identifier) [Task Instance Identifier](terminologies.html#unbound) --></identifier>
 <[**instantiatesCanonical**](task-definitions.html#Task.instantiatesCanonical)><!-- **0..1** [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html#ActivityDefinition)) [Formal definition of task](terminologies.html#unbound) --></instantiatesCanonical>
 <[**instantiatesUri**](task-definitions.html#Task.instantiatesUri) value="[[uri](datatypes.html#uri)]"/><!-- **0..1** [Formal definition of task](terminologies.html#unbound) -->
 <[**basedOn**](task-definitions.html#Task.basedOn)><!-- **0..*** [Reference](references.html#Reference)([Any](resourcelist.html)) [Request fulfilled by this task](terminologies.html#unbound) --></basedOn>
 <[**groupIdentifier**](task-definitions.html#Task.groupIdentifier)><!-- **0..1** [Identifier](datatypes.html#Identifier) [Requisition or grouper id](terminologies.html#unbound) --></groupIdentifier>
 <[**partOf**](task-definitions.html#Task.partOf)><!-- **0..*** [Reference](references.html#Reference)([Task](task.html#Task)) [Composite task](terminologies.html#unbound) --></partOf>
 <[**status**](task-definitions.html#Task.status) value="[[code](datatypes.html#code)]"/><!-- **1..1** [draft | requested | received | accepted | +](valueset-task-status.html) -->
 <[**statusReason**](task-definitions.html#Task.statusReason)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Reason for current status](terminologies.html#unbound) --></statusReason>
 <[**businessStatus**](task-definitions.html#Task.businessStatus)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [E.g. "Specimen collected", "IV prepped"](terminologies.html#unbound) --></businessStatus>
 <[**intent**](task-definitions.html#Task.intent) value="[[code](datatypes.html#code)]"/><!-- **1..1** [unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-task-intent.html) -->
 <[**priority**](task-definitions.html#Task.priority) value="[[code](datatypes.html#code)]"/><!-- **0..1** [routine | urgent | asap | stat](valueset-request-priority.html) -->
 <[**code**](task-definitions.html#Task.code)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Task Type](valueset-task-code.html) --></code>
 <[**description**](task-definitions.html#Task.description) value="[[string](datatypes.html#string)]"/><!-- **0..1** [Human-readable explanation of task](terminologies.html#unbound) -->
 <[**focus**](task-definitions.html#Task.focus)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [What task is acting on](terminologies.html#unbound) --></focus>
 <[**for**](task-definitions.html#Task.for)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Beneficiary of the Task](terminologies.html#unbound) --></for>
 <[**encounter**](task-definitions.html#Task.encounter)><!-- **0..1** [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) [Healthcare event during which this task originated](terminologies.html#unbound) --></encounter>
 <[**executionPeriod**](task-definitions.html#Task.executionPeriod)><!-- **0..1** [Period](datatypes.html#Period) [Start and end time of execution](terminologies.html#unbound) --></executionPeriod>
 <[**authoredOn**](task-definitions.html#Task.authoredOn) value="[[dateTime](datatypes.html#dateTime)]"/><!-- ** 0..1** [Task Creation Date](terminologies.html#unbound) -->
 <[**lastModified**](task-definitions.html#Task.lastModified) value="[[dateTime](datatypes.html#dateTime)]"/><!-- ** 0..1** [Task Last Modified Date](terminologies.html#unbound) -->
 <[**requester**](task-definitions.html#Task.requester)><!-- **0..1** [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Who is asking for task to be done](terminologies.html#unbound) --></requester>
 <[**performerType**](task-definitions.html#Task.performerType)><!-- **0..*** [CodeableConcept](datatypes.html#CodeableConcept) [Requested performer](valueset-performer-role.html) --></performerType>
 <[**owner**](task-definitions.html#Task.owner)><!-- **0..1** [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) [Responsible individual](terminologies.html#unbound) --></owner>
 <[**location**](task-definitions.html#Task.location)><!-- **0..1** [Reference](references.html#Reference)([Location](location.html#Location)) [Where task occurs](terminologies.html#unbound) --></location>
 <[**reasonCode**](task-definitions.html#Task.reasonCode)><!-- **0..1** [CodeableConcept](datatypes.html#CodeableConcept) [Why task is needed](terminologies.html#unbound) --></reasonCode>
 <[**reasonReference**](task-definitions.html#Task.reasonReference)><!-- **0..1** [Reference](references.html#Reference)([Any](resourcelist.html)) [Why task is needed](terminologies.html#unbound) --></reasonReference>
 <[**insurance**](task-definitions.html#Task.insurance)><!-- **0..*** [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) [Associated insurance coverage](terminologies.html#unbound) --></insurance>
 <[**note**](task-definitions.html#Task.note)><!-- **0..*** [Annotation](datatypes.html#Annotation) [Comments made about the task](terminologies.html#unbound) --></note>
 <[**relevantHistory**](task-definitions.html#Task.relevantHistory)><!-- **0..*** [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) [Key events in history of the Task](terminologies.html#unbound) --></relevantHistory>
 <[**restriction**](task-definitions.html#Task.restriction)> <!-- **0..1** Constraints on fulfillment tasks -->
 <[**repetitions**](task-definitions.html#Task.restriction.repetitions) value="[[positiveInt](datatypes.html#positiveInt)]"/><!-- **0..1** [How many times to repeat](terminologies.html#unbound) -->
 <[**period**](task-definitions.html#Task.restriction.period)><!-- **0..1** [Period](datatypes.html#Period) [When fulfillment sought](terminologies.html#unbound) --></period>
 <[**recipient**](task-definitions.html#Task.restriction.recipient)><!-- **0..*** [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization)) [For whom is fulfillment sought?](terminologies.html#unbound) --></recipient>
 </restriction>
 <[**input**](task-definitions.html#Task.input)> <!-- **0..*** Information used to perform task -->
 <[**type**](task-definitions.html#Task.input.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Label for the input](terminologies.html#unbound) --></type>
 <[**value[x]**](task-definitions.html#Task.input.value[x])><!-- **1..1** [*](datatypes.html#open) [Content to use in performing the task](terminologies.html#unbound) --></value[x]>
 </input>
 <[**output**](task-definitions.html#Task.output)> <!-- **0..*** Information produced as part of task -->
 <[**type**](task-definitions.html#Task.output.type)><!-- **1..1** [CodeableConcept](datatypes.html#CodeableConcept) [Label for output](terminologies.html#unbound) --></type>
 <[**value[x]**](task-definitions.html#Task.output.value[x])><!-- **1..1** [*](datatypes.html#open) [Result of output](terminologies.html#unbound) --></value[x]>
 </output>
</Task>

```

 

**JSON Template**

 

 
```
{[](json.html)
 "resourceType" : "[**Task**](task-definitions.html#Task)",
 // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)
 // from [DomainResource](domainresource.html): [text](narrative.html#Narrative), [contained](references.html#contained), [extension](extensibility.html), and [modifierExtension](extensibility.html#modifierExtension)
 "[identifier](task-definitions.html#Task.identifier)" : [{ [Identifier](datatypes.html#Identifier) }], // [Task Instance Identifier](terminologies.html#unbound)
 "[instantiatesCanonical](task-definitions.html#Task.instantiatesCanonical)" : { [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html#ActivityDefinition)) }, // [Formal definition of task](terminologies.html#unbound)
 "[instantiatesUri](task-definitions.html#Task.instantiatesUri)" : "<[uri](datatypes.html#uri)>", // [Formal definition of task](terminologies.html#unbound)
 "[basedOn](task-definitions.html#Task.basedOn)" : [{ [Reference](references.html#Reference)([Any](resourcelist.html)) }], // [Request fulfilled by this task](terminologies.html#unbound)
 "[groupIdentifier](task-definitions.html#Task.groupIdentifier)" : { [Identifier](datatypes.html#Identifier) }, // [Requisition or grouper id](terminologies.html#unbound)
 "[partOf](task-definitions.html#Task.partOf)" : [{ [Reference](references.html#Reference)([Task](task.html#Task)) }], // [Composite task](terminologies.html#unbound)
 "[status](task-definitions.html#Task.status)" : "<[code](datatypes.html#code)>", // **R!** [draft | requested | received | accepted | +](valueset-task-status.html)
 "[statusReason](task-definitions.html#Task.statusReason)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Reason for current status](terminologies.html#unbound)
 "[businessStatus](task-definitions.html#Task.businessStatus)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [E.g. "Specimen collected", "IV prepped"](terminologies.html#unbound)
 "[intent](task-definitions.html#Task.intent)" : "<[code](datatypes.html#code)>", // **R!** [unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option](valueset-task-intent.html)
 "[priority](task-definitions.html#Task.priority)" : "<[code](datatypes.html#code)>", // [routine | urgent | asap | stat](valueset-request-priority.html)
 "[code](task-definitions.html#Task.code)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Task Type](valueset-task-code.html)
 "[description](task-definitions.html#Task.description)" : "<[string](datatypes.html#string)>", // [Human-readable explanation of task](terminologies.html#unbound)
 "[focus](task-definitions.html#Task.focus)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [What task is acting on](terminologies.html#unbound)
 "[for](task-definitions.html#Task.for)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Beneficiary of the Task](terminologies.html#unbound)
 "[encounter](task-definitions.html#Task.encounter)" : { [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) }, // [Healthcare event during which this task originated](terminologies.html#unbound)
 "[executionPeriod](task-definitions.html#Task.executionPeriod)" : { [Period](datatypes.html#Period) }, // [Start and end time of execution](terminologies.html#unbound)
 "[authoredOn](task-definitions.html#Task.authoredOn)" : "<[dateTime](datatypes.html#dateTime)>", // **C?** [Task Creation Date](terminologies.html#unbound)
 "[lastModified](task-definitions.html#Task.lastModified)" : "<[dateTime](datatypes.html#dateTime)>", // **C?** [Task Last Modified Date](terminologies.html#unbound)
 "[requester](task-definitions.html#Task.requester)" : { [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|
 [PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Who is asking for task to be done](terminologies.html#unbound)
 "[performerType](task-definitions.html#Task.performerType)" : [{ [CodeableConcept](datatypes.html#CodeableConcept) }], // [Requested performer](valueset-performer-role.html)
 "[owner](task-definitions.html#Task.owner)" : { [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|
 [HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|[Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) }, // [Responsible individual](terminologies.html#unbound)
 "[location](task-definitions.html#Task.location)" : { [Reference](references.html#Reference)([Location](location.html#Location)) }, // [Where task occurs](terminologies.html#unbound)
 "[reasonCode](task-definitions.html#Task.reasonCode)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // [Why task is needed](terminologies.html#unbound)
 "[reasonReference](task-definitions.html#Task.reasonReference)" : { [Reference](references.html#Reference)([Any](resourcelist.html)) }, // [Why task is needed](terminologies.html#unbound)
 "[insurance](task-definitions.html#Task.insurance)" : [{ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) }], // [Associated insurance coverage](terminologies.html#unbound)
 "[note](task-definitions.html#Task.note)" : [{ [Annotation](datatypes.html#Annotation) }], // [Comments made about the task](terminologies.html#unbound)
 "[relevantHistory](task-definitions.html#Task.relevantHistory)" : [{ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) }], // [Key events in history of the Task](terminologies.html#unbound)
 "[restriction](task-definitions.html#Task.restriction)" : { // [Constraints on fulfillment tasks](terminologies.html#unbound)
 "[repetitions](task-definitions.html#Task.restriction.repetitions)" : "<[positiveInt](datatypes.html#positiveInt)>", // [How many times to repeat](terminologies.html#unbound)
 "[period](task-definitions.html#Task.restriction.period)" : { [Period](datatypes.html#Period) }, // [When fulfillment sought](terminologies.html#unbound)
 "[recipient](task-definitions.html#Task.restriction.recipient)" : [{ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|
 [RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization)) }] // [For whom is fulfillment sought?](terminologies.html#unbound)
 },
 "[input](task-definitions.html#Task.input)" : [{ // [Information used to perform task](terminologies.html#unbound)
 "[type](task-definitions.html#Task.input.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Label for the input](terminologies.html#unbound)
 // value[x]: Content to use in performing the task. One of these 50:
 "[valueBase64Binary](task-definitions.html#Task.input.valueBase64Binary)" : "<[base64Binary](datatypes.html#base64Binary)>"
 "[valueBoolean](task-definitions.html#Task.input.valueBoolean)" : <[boolean](datatypes.html#boolean)>
 "[valueCanonical](task-definitions.html#Task.input.valueCanonical)" : "<[canonical](datatypes.html#canonical)>"
 "[valueCode](task-definitions.html#Task.input.valueCode)" : "<[code](datatypes.html#code)>"
 "[valueDate](task-definitions.html#Task.input.valueDate)" : "<[date](datatypes.html#date)>"
 "[valueDateTime](task-definitions.html#Task.input.valueDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[valueDecimal](task-definitions.html#Task.input.valueDecimal)" : <[decimal](datatypes.html#decimal)>
 "[valueId](task-definitions.html#Task.input.valueId)" : "<[id](datatypes.html#id)>"
 "[valueInstant](task-definitions.html#Task.input.valueInstant)" : "<[instant](datatypes.html#instant)>"
 "[valueInteger](task-definitions.html#Task.input.valueInteger)" : <[integer](datatypes.html#integer)>
 "[valueMarkdown](task-definitions.html#Task.input.valueMarkdown)" : "<[markdown](datatypes.html#markdown)>"
 "[valueOid](task-definitions.html#Task.input.valueOid)" : "<[oid](datatypes.html#oid)>"
 "[valuePositiveInt](task-definitions.html#Task.input.valuePositiveInt)" : "<[positiveInt](datatypes.html#positiveInt)>"
 "[valueString](task-definitions.html#Task.input.valueString)" : "<[string](datatypes.html#string)>"
 "[valueTime](task-definitions.html#Task.input.valueTime)" : "<[time](datatypes.html#time)>"
 "[valueUnsignedInt](task-definitions.html#Task.input.valueUnsignedInt)" : "<[unsignedInt](datatypes.html#unsignedInt)>"
 "[valueUri](task-definitions.html#Task.input.valueUri)" : "<[uri](datatypes.html#uri)>"
 "[valueUrl](task-definitions.html#Task.input.valueUrl)" : "<[url](datatypes.html#url)>"
 "[valueUuid](task-definitions.html#Task.input.valueUuid)" : "<[uuid](datatypes.html#uuid)>"
 "[valueAddress](task-definitions.html#Task.input.valueAddress)" : { [Address](datatypes.html#Address) }
 "[valueAge](task-definitions.html#Task.input.valueAge)" : { [Age](datatypes.html#Age) }
 "[valueAnnotation](task-definitions.html#Task.input.valueAnnotation)" : { [Annotation](datatypes.html#Annotation) }
 "[valueAttachment](task-definitions.html#Task.input.valueAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[valueCodeableConcept](task-definitions.html#Task.input.valueCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) }
 "[valueCoding](task-definitions.html#Task.input.valueCoding)" : { [Coding](datatypes.html#Coding) }
 "[valueContactPoint](task-definitions.html#Task.input.valueContactPoint)" : { [ContactPoint](datatypes.html#ContactPoint) }
 "[valueCount](task-definitions.html#Task.input.valueCount)" : { [Count](datatypes.html#Count) }
 "[valueDistance](task-definitions.html#Task.input.valueDistance)" : { [Distance](datatypes.html#Distance) }
 "[valueDuration](task-definitions.html#Task.input.valueDuration)" : { [Duration](datatypes.html#Duration) }
 "[valueHumanName](task-definitions.html#Task.input.valueHumanName)" : { [HumanName](datatypes.html#HumanName) }
 "[valueIdentifier](task-definitions.html#Task.input.valueIdentifier)" : { [Identifier](datatypes.html#Identifier) }
 "[valueMoney](task-definitions.html#Task.input.valueMoney)" : { [Money](datatypes.html#Money) }
 "[valuePeriod](task-definitions.html#Task.input.valuePeriod)" : { [Period](datatypes.html#Period) }
 "[valueQuantity](task-definitions.html#Task.input.valueQuantity)" : { [Quantity](datatypes.html#Quantity) }
 "[valueRange](task-definitions.html#Task.input.valueRange)" : { [Range](datatypes.html#Range) }
 "[valueRatio](task-definitions.html#Task.input.valueRatio)" : { [Ratio](datatypes.html#Ratio) }
 "[valueReference](task-definitions.html#Task.input.valueReference)" : { [Reference](references.html#Reference) }
 "[valueSampledData](task-definitions.html#Task.input.valueSampledData)" : { [SampledData](datatypes.html#SampledData) }
 "[valueSignature](task-definitions.html#Task.input.valueSignature)" : { [Signature](datatypes.html#Signature) }
 "[valueTiming](task-definitions.html#Task.input.valueTiming)" : { [Timing](datatypes.html#Timing) }
 "[valueContactDetail](task-definitions.html#Task.input.valueContactDetail)" : { [ContactDetail](metadatatypes.html#ContactDetail) }
 "[valueContributor](task-definitions.html#Task.input.valueContributor)" : { [Contributor](metadatatypes.html#Contributor) }
 "[valueDataRequirement](task-definitions.html#Task.input.valueDataRequirement)" : { [DataRequirement](metadatatypes.html#DataRequirement) }
 "[valueExpression](task-definitions.html#Task.input.valueExpression)" : { [Expression](metadatatypes.html#Expression) }
 "[valueParameterDefinition](task-definitions.html#Task.input.valueParameterDefinition)" : { [ParameterDefinition](metadatatypes.html#ParameterDefinition) }
 "[valueRelatedArtifact](task-definitions.html#Task.input.valueRelatedArtifact)" : { [RelatedArtifact](metadatatypes.html#RelatedArtifact) }
 "[valueTriggerDefinition](task-definitions.html#Task.input.valueTriggerDefinition)" : { [TriggerDefinition](metadatatypes.html#TriggerDefinition) }
 "[valueUsageContext](task-definitions.html#Task.input.valueUsageContext)" : { [UsageContext](metadatatypes.html#UsageContext) }
 "[valueDosage](task-definitions.html#Task.input.valueDosage)" : { [Dosage](dosage.html#Dosage) }
 "[valueMeta](task-definitions.html#Task.input.valueMeta)" : { [Meta](resource.html#Meta) }
 }],
 "[output](task-definitions.html#Task.output)" : [{ // [Information produced as part of task](terminologies.html#unbound)
 "[type](task-definitions.html#Task.output.type)" : { [CodeableConcept](datatypes.html#CodeableConcept) }, // **R!** [Label for output](terminologies.html#unbound)
 // value[x]: Result of output. One of these 50:
 "[valueBase64Binary](task-definitions.html#Task.output.valueBase64Binary)" : "<[base64Binary](datatypes.html#base64Binary)>"
 "[valueBoolean](task-definitions.html#Task.output.valueBoolean)" : <[boolean](datatypes.html#boolean)>
 "[valueCanonical](task-definitions.html#Task.output.valueCanonical)" : "<[canonical](datatypes.html#canonical)>"
 "[valueCode](task-definitions.html#Task.output.valueCode)" : "<[code](datatypes.html#code)>"
 "[valueDate](task-definitions.html#Task.output.valueDate)" : "<[date](datatypes.html#date)>"
 "[valueDateTime](task-definitions.html#Task.output.valueDateTime)" : "<[dateTime](datatypes.html#dateTime)>"
 "[valueDecimal](task-definitions.html#Task.output.valueDecimal)" : <[decimal](datatypes.html#decimal)>
 "[valueId](task-definitions.html#Task.output.valueId)" : "<[id](datatypes.html#id)>"
 "[valueInstant](task-definitions.html#Task.output.valueInstant)" : "<[instant](datatypes.html#instant)>"
 "[valueInteger](task-definitions.html#Task.output.valueInteger)" : <[integer](datatypes.html#integer)>
 "[valueMarkdown](task-definitions.html#Task.output.valueMarkdown)" : "<[markdown](datatypes.html#markdown)>"
 "[valueOid](task-definitions.html#Task.output.valueOid)" : "<[oid](datatypes.html#oid)>"
 "[valuePositiveInt](task-definitions.html#Task.output.valuePositiveInt)" : "<[positiveInt](datatypes.html#positiveInt)>"
 "[valueString](task-definitions.html#Task.output.valueString)" : "<[string](datatypes.html#string)>"
 "[valueTime](task-definitions.html#Task.output.valueTime)" : "<[time](datatypes.html#time)>"
 "[valueUnsignedInt](task-definitions.html#Task.output.valueUnsignedInt)" : "<[unsignedInt](datatypes.html#unsignedInt)>"
 "[valueUri](task-definitions.html#Task.output.valueUri)" : "<[uri](datatypes.html#uri)>"
 "[valueUrl](task-definitions.html#Task.output.valueUrl)" : "<[url](datatypes.html#url)>"
 "[valueUuid](task-definitions.html#Task.output.valueUuid)" : "<[uuid](datatypes.html#uuid)>"
 "[valueAddress](task-definitions.html#Task.output.valueAddress)" : { [Address](datatypes.html#Address) }
 "[valueAge](task-definitions.html#Task.output.valueAge)" : { [Age](datatypes.html#Age) }
 "[valueAnnotation](task-definitions.html#Task.output.valueAnnotation)" : { [Annotation](datatypes.html#Annotation) }
 "[valueAttachment](task-definitions.html#Task.output.valueAttachment)" : { [Attachment](datatypes.html#Attachment) }
 "[valueCodeableConcept](task-definitions.html#Task.output.valueCodeableConcept)" : { [CodeableConcept](datatypes.html#CodeableConcept) }
 "[valueCoding](task-definitions.html#Task.output.valueCoding)" : { [Coding](datatypes.html#Coding) }
 "[valueContactPoint](task-definitions.html#Task.output.valueContactPoint)" : { [ContactPoint](datatypes.html#ContactPoint) }
 "[valueCount](task-definitions.html#Task.output.valueCount)" : { [Count](datatypes.html#Count) }
 "[valueDistance](task-definitions.html#Task.output.valueDistance)" : { [Distance](datatypes.html#Distance) }
 "[valueDuration](task-definitions.html#Task.output.valueDuration)" : { [Duration](datatypes.html#Duration) }
 "[valueHumanName](task-definitions.html#Task.output.valueHumanName)" : { [HumanName](datatypes.html#HumanName) }
 "[valueIdentifier](task-definitions.html#Task.output.valueIdentifier)" : { [Identifier](datatypes.html#Identifier) }
 "[valueMoney](task-definitions.html#Task.output.valueMoney)" : { [Money](datatypes.html#Money) }
 "[valuePeriod](task-definitions.html#Task.output.valuePeriod)" : { [Period](datatypes.html#Period) }
 "[valueQuantity](task-definitions.html#Task.output.valueQuantity)" : { [Quantity](datatypes.html#Quantity) }
 "[valueRange](task-definitions.html#Task.output.valueRange)" : { [Range](datatypes.html#Range) }
 "[valueRatio](task-definitions.html#Task.output.valueRatio)" : { [Ratio](datatypes.html#Ratio) }
 "[valueReference](task-definitions.html#Task.output.valueReference)" : { [Reference](references.html#Reference) }
 "[valueSampledData](task-definitions.html#Task.output.valueSampledData)" : { [SampledData](datatypes.html#SampledData) }
 "[valueSignature](task-definitions.html#Task.output.valueSignature)" : { [Signature](datatypes.html#Signature) }
 "[valueTiming](task-definitions.html#Task.output.valueTiming)" : { [Timing](datatypes.html#Timing) }
 "[valueContactDetail](task-definitions.html#Task.output.valueContactDetail)" : { [ContactDetail](metadatatypes.html#ContactDetail) }
 "[valueContributor](task-definitions.html#Task.output.valueContributor)" : { [Contributor](metadatatypes.html#Contributor) }
 "[valueDataRequirement](task-definitions.html#Task.output.valueDataRequirement)" : { [DataRequirement](metadatatypes.html#DataRequirement) }
 "[valueExpression](task-definitions.html#Task.output.valueExpression)" : { [Expression](metadatatypes.html#Expression) }
 "[valueParameterDefinition](task-definitions.html#Task.output.valueParameterDefinition)" : { [ParameterDefinition](metadatatypes.html#ParameterDefinition) }
 "[valueRelatedArtifact](task-definitions.html#Task.output.valueRelatedArtifact)" : { [RelatedArtifact](metadatatypes.html#RelatedArtifact) }
 "[valueTriggerDefinition](task-definitions.html#Task.output.valueTriggerDefinition)" : { [TriggerDefinition](metadatatypes.html#TriggerDefinition) }
 "[valueUsageContext](task-definitions.html#Task.output.valueUsageContext)" : { [UsageContext](metadatatypes.html#UsageContext) }
 "[valueDosage](task-definitions.html#Task.output.valueDosage)" : { [Dosage](dosage.html#Dosage) }
 "[valueMeta](task-definitions.html#Task.output.valueMeta)" : { [Meta](resource.html#Meta) }
 }]
}

```

 

**Turtle Template**

 

 
```
@prefix fhir: <http://hl7.org/fhir/> .[](rdf.html)

[ a fhir:[**Task**](task-definitions.html#Task);
 fhir:nodeRole fhir:treeRoot; # if this is the parser root

 # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)
 # from [DomainResource](domainresource.html): [.text](narrative.html#Narrative), [.contained](references.html#contained), [.extension](extensibility.html), and [.modifierExtension](extensibility.html#modifierExtension)
 fhir:[Task.identifier](task-definitions.html#Task.identifier) [ [Identifier](datatypes.html#Identifier) ], ... ; # 0..* Task Instance Identifier
 fhir:[Task.instantiatesCanonical](task-definitions.html#Task.instantiatesCanonical) [ [canonical](datatypes.html#canonical)([ActivityDefinition](activitydefinition.html#ActivityDefinition)) ]; # 0..1 Formal definition of task
 fhir:[Task.instantiatesUri](task-definitions.html#Task.instantiatesUri) [ [uri](datatypes.html#uri) ]; # 0..1 Formal definition of task
 fhir:[Task.basedOn](task-definitions.html#Task.basedOn) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ], ... ; # 0..* Request fulfilled by this task
 fhir:[Task.groupIdentifier](task-definitions.html#Task.groupIdentifier) [ [Identifier](datatypes.html#Identifier) ]; # 0..1 Requisition or grouper id
 fhir:[Task.partOf](task-definitions.html#Task.partOf) [ [Reference](references.html#Reference)([Task](task.html#Task)) ], ... ; # 0..* Composite task
 fhir:[Task.status](task-definitions.html#Task.status) [ [code](datatypes.html#code) ]; # 1..1 draft | requested | received | accepted | +
 fhir:[Task.statusReason](task-definitions.html#Task.statusReason) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Reason for current status
 fhir:[Task.businessStatus](task-definitions.html#Task.businessStatus) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 E.g. "Specimen collected", "IV prepped"
 fhir:[Task.intent](task-definitions.html#Task.intent) [ [code](datatypes.html#code) ]; # 1..1 unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
 fhir:[Task.priority](task-definitions.html#Task.priority) [ [code](datatypes.html#code) ]; # 0..1 routine | urgent | asap | stat
 fhir:[Task.code](task-definitions.html#Task.code) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Task Type
 fhir:[Task.description](task-definitions.html#Task.description) [ [string](datatypes.html#string) ]; # 0..1 Human-readable explanation of task
 fhir:[Task.focus](task-definitions.html#Task.focus) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 What task is acting on
 fhir:[Task.for](task-definitions.html#Task.for) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Beneficiary of the Task
 fhir:[Task.encounter](task-definitions.html#Task.encounter) [ [Reference](references.html#Reference)([Encounter](encounter.html#Encounter)) ]; # 0..1 Healthcare event during which this task originated
 fhir:[Task.executionPeriod](task-definitions.html#Task.executionPeriod) [ [Period](datatypes.html#Period) ]; # 0..1 Start and end time of execution
 fhir:[Task.authoredOn](task-definitions.html#Task.authoredOn) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Task Creation Date
 fhir:[Task.lastModified](task-definitions.html#Task.lastModified) [ [dateTime](datatypes.html#dateTime) ]; # 0..1 Task Last Modified Date
 fhir:[Task.requester](task-definitions.html#Task.requester) [ [Reference](references.html#Reference)([Device](device.html#Device)|[Organization](organization.html#Organization)|[Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Who is asking for task to be done
 fhir:[Task.performerType](task-definitions.html#Task.performerType) [ [CodeableConcept](datatypes.html#CodeableConcept) ], ... ; # 0..* Requested performer
 fhir:[Task.owner](task-definitions.html#Task.owner) [ [Reference](references.html#Reference)([Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[Organization](organization.html#Organization)|[CareTeam](careteam.html#CareTeam)|[HealthcareService](healthcareservice.html#HealthcareService)|[Patient](patient.html#Patient)|
 [Device](device.html#Device)|[RelatedPerson](relatedperson.html#RelatedPerson)) ]; # 0..1 Responsible individual
 fhir:[Task.location](task-definitions.html#Task.location) [ [Reference](references.html#Reference)([Location](location.html#Location)) ]; # 0..1 Where task occurs
 fhir:[Task.reasonCode](task-definitions.html#Task.reasonCode) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 0..1 Why task is needed
 fhir:[Task.reasonReference](task-definitions.html#Task.reasonReference) [ [Reference](references.html#Reference)([Any](resourcelist.html)) ]; # 0..1 Why task is needed
 fhir:[Task.insurance](task-definitions.html#Task.insurance) [ [Reference](references.html#Reference)([Coverage](coverage.html#Coverage)|[ClaimResponse](claimresponse.html#ClaimResponse)) ], ... ; # 0..* Associated insurance coverage
 fhir:[Task.note](task-definitions.html#Task.note) [ [Annotation](datatypes.html#Annotation) ], ... ; # 0..* Comments made about the task
 fhir:[Task.relevantHistory](task-definitions.html#Task.relevantHistory) [ [Reference](references.html#Reference)([Provenance](provenance.html#Provenance)) ], ... ; # 0..* Key events in history of the Task
 fhir:[Task.restriction](task-definitions.html#Task.restriction) [ # 0..1 Constraints on fulfillment tasks
 fhir:[Task.restriction.repetitions](task-definitions.html#Task.restriction.repetitions) [ [positiveInt](datatypes.html#positiveInt) ]; # 0..1 How many times to repeat
 fhir:[Task.restriction.period](task-definitions.html#Task.restriction.period) [ [Period](datatypes.html#Period) ]; # 0..1 When fulfillment sought
 fhir:[Task.restriction.recipient](task-definitions.html#Task.restriction.recipient) [ [Reference](references.html#Reference)([Patient](patient.html#Patient)|[Practitioner](practitioner.html#Practitioner)|[PractitionerRole](practitionerrole.html#PractitionerRole)|[RelatedPerson](relatedperson.html#RelatedPerson)|[Group](group.html#Group)|[Organization](organization.html#Organization)) ], ... ; # 0..* For whom is fulfillment sought?
 ];
 fhir:[Task.input](task-definitions.html#Task.input) [ # 0..* Information used to perform task
 fhir:[Task.input.type](task-definitions.html#Task.input.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Label for the input
 # [Task.input.value[x]](task-definitions.html#Task.input.value[x]) : 1..1 Content to use in performing the task. One of these 50
 fhir:[Task.input.valueBase64Binary](task-definitions.html#Task.input.valueBase64Binary) [ [base64Binary](datatypes.html#base64Binary) ]
 fhir:[Task.input.valueBoolean](task-definitions.html#Task.input.valueBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Task.input.valueCanonical](task-definitions.html#Task.input.valueCanonical) [ [canonical](datatypes.html#canonical) ]
 fhir:[Task.input.valueCode](task-definitions.html#Task.input.valueCode) [ [code](datatypes.html#code) ]
 fhir:[Task.input.valueDate](task-definitions.html#Task.input.valueDate) [ [date](datatypes.html#date) ]
 fhir:[Task.input.valueDateTime](task-definitions.html#Task.input.valueDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Task.input.valueDecimal](task-definitions.html#Task.input.valueDecimal) [ [decimal](datatypes.html#decimal) ]
 fhir:[Task.input.valueId](task-definitions.html#Task.input.valueId) [ [id](datatypes.html#id) ]
 fhir:[Task.input.valueInstant](task-definitions.html#Task.input.valueInstant) [ [instant](datatypes.html#instant) ]
 fhir:[Task.input.valueInteger](task-definitions.html#Task.input.valueInteger) [ [integer](datatypes.html#integer) ]
 fhir:[Task.input.valueMarkdown](task-definitions.html#Task.input.valueMarkdown) [ [markdown](datatypes.html#markdown) ]
 fhir:[Task.input.valueOid](task-definitions.html#Task.input.valueOid) [ [oid](datatypes.html#oid) ]
 fhir:[Task.input.valuePositiveInt](task-definitions.html#Task.input.valuePositiveInt) [ [positiveInt](datatypes.html#positiveInt) ]
 fhir:[Task.input.valueString](task-definitions.html#Task.input.valueString) [ [string](datatypes.html#string) ]
 fhir:[Task.input.valueTime](task-definitions.html#Task.input.valueTime) [ [time](datatypes.html#time) ]
 fhir:[Task.input.valueUnsignedInt](task-definitions.html#Task.input.valueUnsignedInt) [ [unsignedInt](datatypes.html#unsignedInt) ]
 fhir:[Task.input.valueUri](task-definitions.html#Task.input.valueUri) [ [uri](datatypes.html#uri) ]
 fhir:[Task.input.valueUrl](task-definitions.html#Task.input.valueUrl) [ [url](datatypes.html#url) ]
 fhir:[Task.input.valueUuid](task-definitions.html#Task.input.valueUuid) [ [uuid](datatypes.html#uuid) ]
 fhir:[Task.input.valueAddress](task-definitions.html#Task.input.valueAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Task.input.valueAge](task-definitions.html#Task.input.valueAge) [ [Age](datatypes.html#Age) ]
 fhir:[Task.input.valueAnnotation](task-definitions.html#Task.input.valueAnnotation) [ [Annotation](datatypes.html#Annotation) ]
 fhir:[Task.input.valueAttachment](task-definitions.html#Task.input.valueAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Task.input.valueCodeableConcept](task-definitions.html#Task.input.valueCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Task.input.valueCoding](task-definitions.html#Task.input.valueCoding) [ [Coding](datatypes.html#Coding) ]
 fhir:[Task.input.valueContactPoint](task-definitions.html#Task.input.valueContactPoint) [ [ContactPoint](datatypes.html#ContactPoint) ]
 fhir:[Task.input.valueCount](task-definitions.html#Task.input.valueCount) [ [Count](datatypes.html#Count) ]
 fhir:[Task.input.valueDistance](task-definitions.html#Task.input.valueDistance) [ [Distance](datatypes.html#Distance) ]
 fhir:[Task.input.valueDuration](task-definitions.html#Task.input.valueDuration) [ [Duration](datatypes.html#Duration) ]
 fhir:[Task.input.valueHumanName](task-definitions.html#Task.input.valueHumanName) [ [HumanName](datatypes.html#HumanName) ]
 fhir:[Task.input.valueIdentifier](task-definitions.html#Task.input.valueIdentifier) [ [Identifier](datatypes.html#Identifier) ]
 fhir:[Task.input.valueMoney](task-definitions.html#Task.input.valueMoney) [ [Money](datatypes.html#Money) ]
 fhir:[Task.input.valuePeriod](task-definitions.html#Task.input.valuePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[Task.input.valueQuantity](task-definitions.html#Task.input.valueQuantity) [ [Quantity](datatypes.html#Quantity) ]
 fhir:[Task.input.valueRange](task-definitions.html#Task.input.valueRange) [ [Range](datatypes.html#Range) ]
 fhir:[Task.input.valueRatio](task-definitions.html#Task.input.valueRatio) [ [Ratio](datatypes.html#Ratio) ]
 fhir:[Task.input.valueReference](task-definitions.html#Task.input.valueReference) [ [Reference](references.html#Reference) ]
 fhir:[Task.input.valueSampledData](task-definitions.html#Task.input.valueSampledData) [ [SampledData](datatypes.html#SampledData) ]
 fhir:[Task.input.valueSignature](task-definitions.html#Task.input.valueSignature) [ [Signature](datatypes.html#Signature) ]
 fhir:[Task.input.valueTiming](task-definitions.html#Task.input.valueTiming) [ [Timing](datatypes.html#Timing) ]
 fhir:[Task.input.valueContactDetail](task-definitions.html#Task.input.valueContactDetail) [ [ContactDetail](metadatatypes.html#ContactDetail) ]
 fhir:[Task.input.valueContributor](task-definitions.html#Task.input.valueContributor) [ [Contributor](metadatatypes.html#Contributor) ]
 fhir:[Task.input.valueDataRequirement](task-definitions.html#Task.input.valueDataRequirement) [ [DataRequirement](metadatatypes.html#DataRequirement) ]
 fhir:[Task.input.valueExpression](task-definitions.html#Task.input.valueExpression) [ [Expression](metadatatypes.html#Expression) ]
 fhir:[Task.input.valueParameterDefinition](task-definitions.html#Task.input.valueParameterDefinition) [ [ParameterDefinition](metadatatypes.html#ParameterDefinition) ]
 fhir:[Task.input.valueRelatedArtifact](task-definitions.html#Task.input.valueRelatedArtifact) [ [RelatedArtifact](metadatatypes.html#RelatedArtifact) ]
 fhir:[Task.input.valueTriggerDefinition](task-definitions.html#Task.input.valueTriggerDefinition) [ [TriggerDefinition](metadatatypes.html#TriggerDefinition) ]
 fhir:[Task.input.valueUsageContext](task-definitions.html#Task.input.valueUsageContext) [ [UsageContext](metadatatypes.html#UsageContext) ]
 fhir:[Task.input.valueDosage](task-definitions.html#Task.input.valueDosage) [ [Dosage](dosage.html#Dosage) ]
 fhir:[Task.input.valueMeta](task-definitions.html#Task.input.valueMeta) [ [Meta](resource.html#Meta) ]
 ], ...;
 fhir:[Task.output](task-definitions.html#Task.output) [ # 0..* Information produced as part of task
 fhir:[Task.output.type](task-definitions.html#Task.output.type) [ [CodeableConcept](datatypes.html#CodeableConcept) ]; # 1..1 Label for output
 # [Task.output.value[x]](task-definitions.html#Task.output.value[x]) : 1..1 Result of output. One of these 50
 fhir:[Task.output.valueBase64Binary](task-definitions.html#Task.output.valueBase64Binary) [ [base64Binary](datatypes.html#base64Binary) ]
 fhir:[Task.output.valueBoolean](task-definitions.html#Task.output.valueBoolean) [ [boolean](datatypes.html#boolean) ]
 fhir:[Task.output.valueCanonical](task-definitions.html#Task.output.valueCanonical) [ [canonical](datatypes.html#canonical) ]
 fhir:[Task.output.valueCode](task-definitions.html#Task.output.valueCode) [ [code](datatypes.html#code) ]
 fhir:[Task.output.valueDate](task-definitions.html#Task.output.valueDate) [ [date](datatypes.html#date) ]
 fhir:[Task.output.valueDateTime](task-definitions.html#Task.output.valueDateTime) [ [dateTime](datatypes.html#dateTime) ]
 fhir:[Task.output.valueDecimal](task-definitions.html#Task.output.valueDecimal) [ [decimal](datatypes.html#decimal) ]
 fhir:[Task.output.valueId](task-definitions.html#Task.output.valueId) [ [id](datatypes.html#id) ]
 fhir:[Task.output.valueInstant](task-definitions.html#Task.output.valueInstant) [ [instant](datatypes.html#instant) ]
 fhir:[Task.output.valueInteger](task-definitions.html#Task.output.valueInteger) [ [integer](datatypes.html#integer) ]
 fhir:[Task.output.valueMarkdown](task-definitions.html#Task.output.valueMarkdown) [ [markdown](datatypes.html#markdown) ]
 fhir:[Task.output.valueOid](task-definitions.html#Task.output.valueOid) [ [oid](datatypes.html#oid) ]
 fhir:[Task.output.valuePositiveInt](task-definitions.html#Task.output.valuePositiveInt) [ [positiveInt](datatypes.html#positiveInt) ]
 fhir:[Task.output.valueString](task-definitions.html#Task.output.valueString) [ [string](datatypes.html#string) ]
 fhir:[Task.output.valueTime](task-definitions.html#Task.output.valueTime) [ [time](datatypes.html#time) ]
 fhir:[Task.output.valueUnsignedInt](task-definitions.html#Task.output.valueUnsignedInt) [ [unsignedInt](datatypes.html#unsignedInt) ]
 fhir:[Task.output.valueUri](task-definitions.html#Task.output.valueUri) [ [uri](datatypes.html#uri) ]
 fhir:[Task.output.valueUrl](task-definitions.html#Task.output.valueUrl) [ [url](datatypes.html#url) ]
 fhir:[Task.output.valueUuid](task-definitions.html#Task.output.valueUuid) [ [uuid](datatypes.html#uuid) ]
 fhir:[Task.output.valueAddress](task-definitions.html#Task.output.valueAddress) [ [Address](datatypes.html#Address) ]
 fhir:[Task.output.valueAge](task-definitions.html#Task.output.valueAge) [ [Age](datatypes.html#Age) ]
 fhir:[Task.output.valueAnnotation](task-definitions.html#Task.output.valueAnnotation) [ [Annotation](datatypes.html#Annotation) ]
 fhir:[Task.output.valueAttachment](task-definitions.html#Task.output.valueAttachment) [ [Attachment](datatypes.html#Attachment) ]
 fhir:[Task.output.valueCodeableConcept](task-definitions.html#Task.output.valueCodeableConcept) [ [CodeableConcept](datatypes.html#CodeableConcept) ]
 fhir:[Task.output.valueCoding](task-definitions.html#Task.output.valueCoding) [ [Coding](datatypes.html#Coding) ]
 fhir:[Task.output.valueContactPoint](task-definitions.html#Task.output.valueContactPoint) [ [ContactPoint](datatypes.html#ContactPoint) ]
 fhir:[Task.output.valueCount](task-definitions.html#Task.output.valueCount) [ [Count](datatypes.html#Count) ]
 fhir:[Task.output.valueDistance](task-definitions.html#Task.output.valueDistance) [ [Distance](datatypes.html#Distance) ]
 fhir:[Task.output.valueDuration](task-definitions.html#Task.output.valueDuration) [ [Duration](datatypes.html#Duration) ]
 fhir:[Task.output.valueHumanName](task-definitions.html#Task.output.valueHumanName) [ [HumanName](datatypes.html#HumanName) ]
 fhir:[Task.output.valueIdentifier](task-definitions.html#Task.output.valueIdentifier) [ [Identifier](datatypes.html#Identifier) ]
 fhir:[Task.output.valueMoney](task-definitions.html#Task.output.valueMoney) [ [Money](datatypes.html#Money) ]
 fhir:[Task.output.valuePeriod](task-definitions.html#Task.output.valuePeriod) [ [Period](datatypes.html#Period) ]
 fhir:[Task.output.valueQuantity](task-definitions.html#Task.output.valueQuantity) [ [Quantity](datatypes.html#Quantity) ]
 fhir:[Task.output.valueRange](task-definitions.html#Task.output.valueRange) [ [Range](datatypes.html#Range) ]
 fhir:[Task.output.valueRatio](task-definitions.html#Task.output.valueRatio) [ [Ratio](datatypes.html#Ratio) ]
 fhir:[Task.output.valueReference](task-definitions.html#Task.output.valueReference) [ [Reference](references.html#Reference) ]
 fhir:[Task.output.valueSampledData](task-definitions.html#Task.output.valueSampledData) [ [SampledData](datatypes.html#SampledData) ]
 fhir:[Task.output.valueSignature](task-definitions.html#Task.output.valueSignature) [ [Signature](datatypes.html#Signature) ]
 fhir:[Task.output.valueTiming](task-definitions.html#Task.output.valueTiming) [ [Timing](datatypes.html#Timing) ]
 fhir:[Task.output.valueContactDetail](task-definitions.html#Task.output.valueContactDetail) [ [ContactDetail](metadatatypes.html#ContactDetail) ]
 fhir:[Task.output.valueContributor](task-definitions.html#Task.output.valueContributor) [ [Contributor](metadatatypes.html#Contributor) ]
 fhir:[Task.output.valueDataRequirement](task-definitions.html#Task.output.valueDataRequirement) [ [DataRequirement](metadatatypes.html#DataRequirement) ]
 fhir:[Task.output.valueExpression](task-definitions.html#Task.output.valueExpression) [ [Expression](metadatatypes.html#Expression) ]
 fhir:[Task.output.valueParameterDefinition](task-definitions.html#Task.output.valueParameterDefinition) [ [ParameterDefinition](metadatatypes.html#ParameterDefinition) ]
 fhir:[Task.output.valueRelatedArtifact](task-definitions.html#Task.output.valueRelatedArtifact) [ [RelatedArtifact](metadatatypes.html#RelatedArtifact) ]
 fhir:[Task.output.valueTriggerDefinition](task-definitions.html#Task.output.valueTriggerDefinition) [ [TriggerDefinition](metadatatypes.html#TriggerDefinition) ]
 fhir:[Task.output.valueUsageContext](task-definitions.html#Task.output.valueUsageContext) [ [UsageContext](metadatatypes.html#UsageContext) ]
 fhir:[Task.output.valueDosage](task-definitions.html#Task.output.valueDosage) [ [Dosage](dosage.html#Dosage) ]
 fhir:[Task.output.valueMeta](task-definitions.html#Task.output.valueMeta) [ [Meta](resource.html#Meta) ]
 ], ...;
]

```

 

**Changes since Release 3**

 

 

 | 
 
 [Task](task.html#Task)
 | 
 | 
 |

 | 
 Task.instantiatesCanonical | 
 
 

 Added Element

 

 | 
 |

 | 
 Task.instantiatesUri | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.status | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/task-status to http://hl7.org/fhir/ValueSet/task-status|4.0.1

 - Now marked as Modifier

 

 | 
 |

 | 
 Task.intent | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/request-intent to http://hl7.org/fhir/ValueSet/task-intent|4.0.1

 

 | 
 |

 | 
 Task.priority | 
 
 

 - Change value set from http://hl7.org/fhir/ValueSet/request-priority to http://hl7.org/fhir/ValueSet/request-priority|4.0.1

 

 | 
 |

 | 
 Task.encounter | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.requester | 
 
 

 - Type changed from BackboneElement to Reference(Device | Organization | Patient | Practitioner | PractitionerRole | RelatedPerson)

 

 | 
 |

 | 
 Task.owner | 
 
 

 - Type Reference: Added Target Types PractitionerRole, CareTeam, HealthcareService

 

 | 
 |

 | 
 Task.location | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.reasonCode | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.reasonReference | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.insurance | 
 
 

 - Added Element

 

 | 
 |

 | 
 Task.restriction.recipient | 
 
 

 - Type Reference: Added Target Type PractitionerRole

 

 | 
 |

 | 
 Task.input.value[x] | 
 
 

 - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage

 

 | 
 |

 | 
 Task.output.value[x] | 
 
 

 - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage

 

 | 
 |

 | 
 Task.definition[x] | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.context | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.requester.agent | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.requester.onBehalfOf | 
 
 

 - deleted

 

 | 
 |

 | 
 Task.reason | 
 
 

 - deleted

 

 | 
 |

See the [Full Difference](diff.html) for further information

 

 This analysis is available as [XML](task.diff.xml) or [JSON](task.diff.json).
 

 
See [R3 <--> R4 Conversion Maps](task-version-maps.html) (status = 6 tests that all execute ok. 3 fail round-trip testing and 1 r3 resources are invalid (0 errors).)

 

 

 

See the [Profiles & Extensions](task-profiles.html) and the alternate definitions:
Master Definition [XML](task.profile.xml.html) + [JSON](task.profile.json.html),
[XML](xml.html) [Schema](task.xsd)/[Schematron](task.sch) + [JSON](json.html) 
[Schema](task.schema.json.html), [ShEx](task.shex.html) (for [Turtle](rdf.html)) + [see the extensions](task-profiles.html) & the [dependency analysis](task-dependencies.html)

### 12.1.4.1 
Terminology Bindings
 [
](task.html#tx)

 | Path | Definition | Type | Reference | |

 | Task.status | The current status of the task. | [Required](terminologies.html#required) | [TaskStatus](valueset-task-status.html) | |

 | Task.statusReason | Codes to identify the reason for current status. These will typically be specific to a particular workflow. | Unknown | No details provided yet | |

 | Task.businessStatus | The domain-specific business-contextual sub-state of the task. For example: "Blood drawn", "IV inserted", "Awaiting physician signature", etc. | Unknown | No details provided yet | |

 | Task.intent | Distinguishes whether the task is a proposal, plan or full order. | [Required](terminologies.html#required) | [TaskIntent](valueset-task-intent.html) | |

 | Task.priority | The task's priority. | [Required](terminologies.html#required) | [RequestPriority](valueset-request-priority.html) | |

 | Task.code | Codes to identify what the task involves. These will typically be specific to a particular workflow. | [Example](terminologies.html#example) | [TaskCode](valueset-task-code.html) | |

 | Task.performerType | The type(s) of task performers allowed. | [Preferred](terminologies.html#preferred) | [ProcedurePerformerRoleCodes](valueset-performer-role.html) | |

 | Task.reasonCode | Indicates why the task is needed. E.g. Suspended because patient admitted to hospital. | Unknown | No details provided yet | |

 | Task.input.type | Codes to identify types of input parameters. These will typically be specific to a particular workflow. E.g. "Comparison source", "Applicable consent", "Concomitent Medications", etc. | Unknown | No details provided yet | |

 | Task.output.type | Codes to identify types of input parameters. These will typically be specific to a particular workflow. E.g. "Identified issues", "Preliminary results", "Filler order", "Final results", etc. | Unknown | No details provided yet | |

 

 

### 12.1.4.2 Constraints [
](task.html#invs)

| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** | |
| **inv-1** | [Rule](conformance-rules.html#rule) | (base) | Last modified date must be greater than or equal to authored-on date. | lastModified.exists().not() or authoredOn.exists().not() or lastModified >= authoredOn | |

 
## 12.1.5 Task Titles [](task.html#titles)

 
 Tasks often have titles (eg "My Tasks", "Outstanding Tasks for Patient X") which can be presented in a list. The task title should go into the Task.code as a coded concept and/or text.
 

 
 
## 12.1.6 Task state machine [
](task.html#statemachine)

 
 The following diagram reflects the "typical" state machine for Task. Note that not all states will be supported by all workflows
 and that some workflows may support additional transitions, including transitions from terminal states (e.g. back to "in-progress"
 from "failed" or "completed").
 

 

 
 
## 12.1.7 The Cancelled state [
](task.html#cancelled)

 
 While the intention of a "cancelled" task is that all work authorized by the task should cease, this
 might not always be possible practice. It is possible that the originally requested action could still
 be completed and still attached to the Task but this would not change the status of the task. If the
 placer cancels a task, it signals they no longer care about the outcome of the task.
 

## 12.1.8 Search Parameters [
](task.html#search)

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

| **Name** | **Type** | **Description** | **Expression** | **In Common** | |

| authored-on | [date](search.html#date) | Search by creation date | Task.authoredOn | | |

| based-on | [reference](search.html#reference) | Search by requests this task is based on | Task.basedOn
(Any) | | |

| business-status | [token](search.html#token) | Search by business status | Task.businessStatus | | |

| code | [token](search.html#token) | Search by task code | Task.code | | |

| encounter | [reference](search.html#reference) | Search by encounter | Task.encounter
([Encounter](encounter.html)) | | |

| focus | [reference](search.html#reference) | Search by task focus | Task.focus
(Any) | | |

| group-identifier | [token](search.html#token) | Search by group identifier | Task.groupIdentifier | | |

| identifier | [token](search.html#token) | Search for a task instance by its business identifier | Task.identifier | | |

| intent | [token](search.html#token) | Search by task intent | Task.intent | | |

| modified | [date](search.html#date) | Search by last modification date | Task.lastModified | | |

| owner | [reference](search.html#reference) | Search by task owner | Task.owner
([Practitioner](practitioner.html), [Organization](organization.html), [CareTeam](careteam.html), [Device](device.html), [Patient](patient.html), [HealthcareService](healthcareservice.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| part-of | [reference](search.html#reference) | Search by task this task is part of | Task.partOf
([Task](task.html)) | | |

| patient | [reference](search.html#reference) | Search by patient | Task.for.where(resolve() is Patient)
([Patient](patient.html)) | | |

| performer | [token](search.html#token) | Search by recommended type of performer (e.g., Requester, Performer, Scheduler). | Task.performerType | | |

| period | [date](search.html#date) | Search by period Task is/was underway | Task.executionPeriod | | |

| priority | [token](search.html#token) | Search by task priority | Task.priority | | |

| requester | [reference](search.html#reference) | Search by task requester | Task.requester
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) | | |

| status | [token](search.html#token) | Search by task status | Task.status | | |

| subject | [reference](search.html#reference) | Search by subject | Task.for
(Any) | | |