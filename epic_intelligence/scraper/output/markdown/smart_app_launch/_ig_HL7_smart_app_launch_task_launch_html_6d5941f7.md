# Task profile for requesting SMART launch (Experimental) - SMART App Launch v2.2.0

> Source: https://build.fhir.org/ig/HL7/smart-app-launch/task-launch.html

---

SMART App Launch, published by HL7 International / FHIR Infrastructure. This guide is not an authorized publication; it is the continuous build for version 2.2.0 built by the FHIR (HL7® FHIR® Standard) CI Build. This version is based on the current content of [https://github.com/HL7/smart-app-launch/](https://github.com/HL7/smart-app-launch/) and changes regularly. See the [Directory of published versions](http://hl7.org/fhir/smart-app-launch/history.html)

 
## Task profile for requesting SMART launch (Experimental)

 

 

 - [Requesting an EHR launch](#requesting-an-ehr-launch)

 - [Requesting an standalone launch](#requesting-an-standalone-launch)

This section defines a set of profiles of the FHIR Task resource that requests launch of a SMART application. These tasks could be used to recommend an application for staff to launch, e.g. as a result of a Clinical Reasoning deployment.

Two profiles are defined:

 - [task-ehr-launch](StructureDefinition-task-ehr-launch.html), requests an EHR launch with optional appContext.

 - [task-standalone-launch](StructureDefinition-task-standalone-launch.html), requests a standalone launch.

### Requesting an EHR launch

A Task with the profile [task-ehr-launch](StructureDefinition-task-ehr-launch.html), requests an EHR launch with optional `appContext`.

The `Task.for` field, if present, indicates the Patient resource to be used in the launch context.

The `Task.encounter` field, if present, indicates the Encounter resource to be used in the launch context.

The input field contains:

 - the url of the application to be launched

 - optional appContext to be included in the token response as is specified in a [CDShooks Link](https://cds-hooks.org/specification/current/#link)

An example of such Task is presented below:

```
{
 "resourceType": "Task",
 "id": "task-for-ehr-launch",
 "status": "requested",
 "intent": "proposal",
 "code": {
 "coding": [{
 "system": "http://hl7.org/fhir/smart-app-launch/CodeSystem/smart-codes",
 "code": "launch-app-ehr",
 "display": "Launch application using the SMART EHR launch"
 }]
 },
 "for": {"reference": "https://example.org/fhir/Patient/123"},
 "encounter": {"reference": "https://example.org/fhir/Encounter/456"},
 "input": [
 {
 "type": {
 "coding":[{
 "system": "http://hl7.org/fhir/smart-app-launch/CodeSystem/smart-codes",
 "code": "smartonfhir-application",
 "display": "SMART on FHIR application URL."
 }]
 },
 "valueUrl": "https://www.example.org/myapplication"
 },
 {
 "type": {
 "coding":[{
 "system": "http://hl7.org/fhir/smart-app-launch/CodeSystem/smart-codes",
 "code": "smartonfhir-appcontext",
 "display": "Application context related to this launch."
 }]
 },
 "valueString": "{\"field1\":\"value\"}"
 }

```

### Requesting an standalone launch

A Task according to the profile [task-standalone-launch](StructureDefinition-task-standalone-launch.html), requests an standalone launch.

The input field contains:

 - the url of the application to be launched

An example of such Task is presented below:

```
{
 "resourceType": "Task",
 "id": "task-for-standalone-launch",
 "status": "requested",
 "intent": "proposal",
 "code": 
 {
 "coding": [{
 "system": "http://hl7.org/fhir/smart-app-launch/CodeSystem/smart-codes",
 "code": "launch-app-standalone",
 "display": "Launch application using the SMART standalone launch"
 }]
 },
 "for": {"reference": "https://example.org/fhir/Patient/123"},
 "encounter": {"reference": "https://example.org/fhir/Encounter/456"},
 "input": [
 {
 "type": {
 "coding":[{
 "system": "http://hl7.org/fhir/smart-app-launch/CodeSystem/smart-codes",
 "code": "smartonfhir-application",
 "display": "SMART on FHIR application URL."
 }]
 },
 "valueUrl": "https://www.example.org/myapplication"
 }]
}

```