from string import Template
import json
from datetime import datetime
import uuid
import time

class ComprehensiveISO27001Generator:
    def __init__(self):
        # Mandatory clauses (4-10) template
        self.base_template = """
INFORMATION SECURITY MANAGEMENT SYSTEM DOCUMENTATION

Document ID: $doc_id
Document Title: $doc_title
Version: $version
Classification: $classification
Last Updated: $date
Document Owner: $owner
Approved By: $approver

==========================================
MANDATORY SECTIONS (ISO 27001:2022)
==========================================

4. CONTEXT OF THE ORGANIZATION
=============================
4.1 Understanding the Organization and its Context
------------------------------------------------
Internal Issues:
$internal_issues

External Issues:
$external_issues

4.2 Understanding the Needs and Expectations of Interested Parties
---------------------------------------------------------------
Interested Parties Analysis:
$interested_parties

4.3 Determining the Scope of the ISMS
------------------------------------
Scope Statement:
$scope_statement

Scope Boundaries and Applicability:
$scope_boundaries

4.4 Information Security Management System
----------------------------------------
ISMS Process Interactions:
$isms_processes

5. LEADERSHIP
============
5.1 Leadership and Commitment
----------------------------
Management Commitment Evidence:
$leadership_commitment

5.2 Information Security Policy
------------------------------
Policy Statement:
$security_policy

Policy Communication Methods:
$policy_communication

5.3 Organizational Roles, Responsibilities and Authorities
-------------------------------------------------------
Key Roles and Responsibilities:
$roles_responsibilities

6. PLANNING
==========
6.1 Actions to Address Risks and Opportunities
--------------------------------------------
6.1.1 Risk Assessment Process:
$risk_assessment_process

6.1.2 Information Security Risk Treatment:
$risk_treatment

6.1.3 Information Security Risk Treatment Plan:
$risk_treatment_plan

6.2 Information Security Objectives
---------------------------------
Security Objectives:
$security_objectives

Measurement Methods:
$objective_measurements

7. SUPPORT
=========
7.1 Resources
------------
Required Resources:
$resources

7.2 Competence
-------------
Competence Requirements:
$competence_requirements

Training Program:
$training_program

7.3 Awareness
------------
Awareness Program:
$awareness_program

7.4 Communication
----------------
Communication Matrix:
$communication_matrix

7.5 Documented Information
-------------------------
Documentation Controls:
$documentation_controls

8. OPERATION
===========
8.1 Operational Planning and Control
----------------------------------
Operational Procedures:
$operational_procedures

8.2 Information Security Risk Assessment
--------------------------------------
Risk Assessment Schedule:
$risk_assessment_schedule

8.3 Information Security Risk Treatment
-------------------------------------
Risk Treatment Implementation:
$risk_treatment_implementation

9. PERFORMANCE EVALUATION
=======================
9.1 Monitoring, Measurement, Analysis and Evaluation
-------------------------------------------------
Monitoring Program:
$monitoring_program

Evaluation Criteria:
$evaluation_criteria

9.2 Internal Audit
-----------------
Audit Program:
$audit_program

9.3 Management Review
--------------------
Review Schedule:
$management_review

10. IMPROVEMENT
=============
10.1 Nonconformity and Corrective Action
---------------------------------------
Corrective Action Process:
$corrective_action

10.2 Continual Improvement
-------------------------
Improvement Methodology:
$improvement_methodology

MANDATORY RECORDS AND EVIDENCE
============================
$mandatory_records

STATEMENT OF APPLICABILITY
=========================
$statement_applicability
"""

    def explain_mandatory_requirements(self):
        """Explain ISO 27001 mandatory requirements"""
        print("""
============================================
ISO 27001:2022 MANDATORY REQUIREMENTS GUIDE
============================================

ISO 27001 has specific mandatory requirements that must be met for certification:

1. MANDATORY DOCUMENTS
---------------------
You must have the following documents:
- Information security policy
- ISMS scope
- Risk assessment and treatment process
- Statement of Applicability (SoA)
- Information security objectives
- Evidence of competence
- Documented operational controls
- Risk assessment results
- Risk treatment results
- Monitoring and measurement results

2. MANDATORY PROCESSES
--------------------
You must implement these processes:
- Risk assessment
- Risk treatment
- Competence determination
- Operation control
- Monitoring, measurement, analysis and evaluation
- Internal audit
- Management review
- Nonconformity and corrective action
- Continual improvement

3. MANDATORY RECORDS
------------------
You must maintain records of:
- Training, skills, experience and qualifications
- Monitoring and measurement results
- Internal audit program
- Results of management reviews
- Nature of nonconformities and subsequent actions
- Results of corrective actions

Press Enter to continue...""")
        input()

    def guide_scope_definition(self):
        """Guide through mandatory scope definition"""
        print("""
DEFINING ISMS SCOPE (Mandatory Requirement)
----------------------------------------
Your scope must clearly define the boundaries of your ISMS.

Consider:
1. Core Business Processes
   - What are your main business activities?
   - Which processes handle sensitive information?

2. Organizational Units
   - Which departments are included?
   - Any excluded departments?

3. Physical Locations
   - Which sites are covered?
   - Remote working considerations?

4. Technology Scope
   - Which systems are included?
   - Cloud services coverage?
   - Network boundaries?

5. Third-party Interfaces
   - Supplier connections?
   - Customer interfaces?
   - Partner systems?

Example Scope Statement:
"The ISMS covers all business processes, information assets, and technology 
infrastructure supporting the provision of [service/product] at [location], 
including cloud-based services and remote working arrangements."
""")
        return self.guided_input(
            "ISMS Scope",
            "Define your ISMS scope: ",
            "Be specific about inclusions and exclusions"
        )

    def guide_risk_assessment_process(self):
        """Guide through mandatory risk assessment process"""
        print("""
RISK ASSESSMENT PROCESS (Mandatory Requirement)
-------------------------------------------
You must document your risk assessment methodology:

1. Risk Identification
   - Asset inventory
   - Threat identification
   - Vulnerability assessment
   - Impact analysis

2. Risk Analysis
   - Likelihood determination
   - Impact evaluation
   - Risk level calculation
   - Risk prioritization

3. Risk Evaluation
   - Risk acceptance criteria
   - Risk appetite definition
   - Treatment priorities

Required Elements:
a) Risk assessment methodology
b) Risk acceptance criteria
c) Impact levels definition
d) Likelihood criteria
e) Risk matrix/scoring system

Example Process:
"Risk levels are calculated by multiplying impact (1-5) by likelihood (1-5).
Risks scoring >15 require immediate treatment, 10-15 require action plan,
<10 may be accepted with monitoring."
""")
        return {
            'methodology': self.guided_input(
                "Risk Assessment Methodology",
                "Describe your risk assessment method: ",
                "Example: 5x5 risk matrix with defined criteria"
            ),
            'criteria': self.guided_input(
                "Risk Acceptance Criteria",
                "Define your risk acceptance criteria: ",
                "Example: Risks scored below 10 may be accepted"
            ),
            'process': self.guided_input(
                "Assessment Process",
                "Describe your assessment process: ",
                "Example: Quarterly reviews with stakeholders"
            )
        }

    def guide_mandatory_policy(self):
        """Guide through mandatory security policy creation"""
        print("""
INFORMATION SECURITY POLICY (Mandatory Requirement)
-----------------------------------------------
Your security policy must include:

1. Strategic Elements:
   - Purpose and objectives
   - Management commitment
   - Scope and boundaries
   - Principles and standards

2. Operational Elements:
   - Roles and responsibilities
   - Compliance requirements
   - Consequences of violations
   - Incident reporting

3. Communication Requirements:
   - Policy distribution
   - Training requirements
   - Review frequency
   - Version control

Key Policy Components:
a) Clear objectives aligned with business
b) Definition of security principles
c) Framework for setting controls
d) Commitment to satisfy requirements
e) Commitment to continual improvement

Example Policy Statement:
"[Organization] is committed to protecting the confidentiality, integrity,
and availability of all information assets through risk-based controls,
regular training, and continuous improvement..."
""")
        return self.guided_input(
            "Security Policy",
            "Draft your security policy statement: ",
            "Include commitment, scope, and objectives"
        )

    def generate_mandatory_documentation(self):
        """Generate all mandatory documentation"""
        print("\nGenerating Mandatory ISO 27001:2022 Documentation")
        
        self.explain_mandatory_requirements()
        
        # Collect mandatory elements
        scope = self.guide_scope_definition()
        risk_process = self.guide_risk_assessment_process()
        policy = self.guide_mandatory_policy()
        
        # Generate Statement of Applicability
        soa = self.generate_soa()
        
        # Collect all mandatory records
        mandatory_records = {
            'scope': scope,
            'risk_process': risk_process,
            'policy': policy,
            'soa': soa,
            'objectives': self.guide_security_objectives(),
            'competence': self.guide_competence_records(),
            'operational_controls': self.guide_operational_controls(),
            'monitoring': self.guide_monitoring_requirements(),
            'audit': self.guide_audit_program(),
            'management_review': self.guide_management_review(),
            'corrective_actions': self.guide_corrective_actions()
        }
        
        return self.compile_mandatory_documentation(mandatory_records)

    def guide_security_objectives(self):
        """Guide through setting mandatory security objectives"""
        print("""
SECURITY OBJECTIVES (Mandatory Requirement)
---------------------------------------
Your security objectives must be:
- Measurable
- Monitored
- Communicated
- Updated as needed

Examples:
1. "Achieve 99.9% system availability"
2. "Zero critical security incidents"
3. "100% staff security training completion"
""")
        return self.guided_input(
            "Security Objectives",
            "Define your security objectives: ",
            "Include metrics and timeframes"
        )

    # [Additional methods would continue with similar detailed guidance for each mandatory element]

def main():
    print("Starting Comprehensive ISO 27001:2022 Documentation Generator...")
    generator = ComprehensiveISO27001Generator()
    
    print("""
Welcome to the ISO 27001:2022 Documentation Generator
This tool will guide you through creating all mandatory documentation
required for ISO 27001:2022 certification.

Would you like to:
1. Get an overview of mandatory requirements
2. Start generating documentation
3. See example documents
""")
    
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        generator.explain_mandatory_requirements()
    
    documentation = generator.generate_mandatory_documentation()
    
    # Save documentation
    filename = f"ISO27001_Mandatory_Documentation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as f:
        f.write(documentation)
    
    print(f"\nMandatory documentation generated and saved as {filename}")
    print("\nNext steps:")
    print("1. Review all mandatory documents")
    print("2. Get management approval")
    print("3. Implement documented processes")
    print("4. Begin collecting required records")
    print("5. Schedule internal audit")

if __name__ == "__main__":
    main()
