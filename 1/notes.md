## NIST Background
- https://www.youtube.com/watch?v=VMUy5QKSPHA
- Cloud computing is a model for enabling ubiquitous convenient on demand services. Delivery of computer services over the internet "the cloud"
- Characteristics of cloud computing:
  - On demand, self service provisioning automatically and as needed
  - Broad network access - resources available over the network supporting heterogenous platforms like desktop/mobile
  - Shared pool of resources: pooled to consumers using multi-tenant model
  - Rapidly provisioned and released - eslastic proviisoning and release
  - Measured service, resource usage monitored then billed
- Advantages: streamlined work, backup and recovery, near unlimited storage, cost efficient, network available, automatic software integration, collaboration across geographies, eslastic
- Downsides are loss of control, security being held by someone else, transparency

## Cloud Computing Service Models
- SaaS - Software as a Service: deliver software and applications through the internet
  - subscription Models
  - users don't have to manage install or upgrade
  - data is in the cloud, equipment failure doesn't result in a loss of data
  - scalable based on service need
  - software/applications accessible fro mmost internet connected devices
- PaaS - Access to cloud based environments where users can build and deliver applications
  - Platform with tools to test develop and host appliations in the same environment
  - enables development without having to worry about underlying infrastructure
  - Security, operating systems, server software, and backups handled by provider
- IaaS - Access to storage, networking, servers, and other computing resources in the cloud
  - example would be backup and recovery services on servers or desktop systems
  - server resources for running cloud based systems that can be dynamically provisioned and configured as needed

## Cloud computing deployment models
- https://www.youtube.com/watch?v=G1ODXYT9SWM
- Public cloud: resources owned and operated by a third party and delivered over the internet
- Private cloud: cloud infrastructure provisioned for use by a single organization
- Hybrid Cloud: combine on prem with public to reap the advantages of both
- Community Cloud: Infrastructure provisioned for exclusive use by a community of consumers from orgs that have similar concerns
- Public cloud:
  - Costs: no need to purchase hardware/software, pay for what you need
  - No maintenance: service provider does that
  - Scalability
  - High reliability: many redundant servers is a good failsafe
- Private Cloud:
  - Flexibility: customize cloud environment to meet specific business needs
  - Improved Security: resources not shared with others
  - High scalability: on demand resources are available when needed(? yeah but don't you have to buy them lol)
- Hybrid Cloud:
  - Control over sensitive assets
  - Best of both worlds
  - Very populat

## Cloud Computing Reference Architecture
 - https://www.youtube.com/watch?v=qcl_VGIjS2g
 - Security:
   - sppans all layers of the reference model, ranging from physical to application
   - Includes providers AND consumers in a shared consumer model
   - Needs to address authentication, authorization, availability, confidentiality, identity management, integrity, audit, security monitoring, incident response, and security policy management
- NIST provided the CCRA in 2011 as a high level of functions and capabilities, definitions of actors acitivities and functions used in developing cloud computing architectures, a tool for discussing system specific architecture using a common framework, and a high level model of requirements, structures and operations of cloud computing
- CCRA actors:
  1. Cloud Consumer: uses provider services
  2. Provider: makes services available to consumers
  3. Carrier: Provides connectivity and transport of cloud services from cloud providers to cloud consumers
  4. Auditor: Conducts independent assessment of services, information system operations, performance and security of the cloud implementation
  5. Broker: Manages use, performance, delivery of cloud services and negotiates relationship between provider/consumer
- SLAs are agreements between consumer and provider including error rates, uptime percentages, credits and other information
- PII is personally identifiable information that can be used to distinguish or trace identity
- Service orchestration includes
  - servie layers: IaaS, PaaS, SaaS
  - Resource abstraction and control layer - provide and manage access to the physical computing resources through software abstraction (eg virtual machines, hypervisors, virtual storage)
- Physical resource layer - includes physical computing resources and facilities
- Cloud services management:
  - Business Support: business related services supporting clients & processes
  - Provisioning/Configuration: rapid provisioning of services and monitoring to alert users of resource issues
  - Portability/interoperability: movement of data or applications across multiple cloud environments at low cost and minimal disruption
  - Rapid provisioning: deploys based on parameters
  - Adjusting resources for usage, changes, and new nodes
  - monitoring/reporting - generating logging monitoring performance etc
- Portability/Interoperability
  - Data portability: move dat a in or out of the cloud or use a disk for bulk data transfer
  - Service interoperability: use data across multiple cloud providers with a unified management interface
  - System portability: migration of machine images between providers or migration applications, services and contents from one provider to another 
