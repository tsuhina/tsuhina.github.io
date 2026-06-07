Title: Projects
Slug: projects

A selection of what I've built and delivered, described at a high level. The specifics of client engagements are kept in confidence, so these focus on the problem, the approach and the outcome rather than naming names.


## Featured

### Bayesian Media Mix Modeling
Technical lead of a 15+ person interdisciplinary team (data scientists, data and MLOps engineers, front end) delivering a Bayesian marketing-mix model for budget allocation and ROI optimisation. It captured value at tens-of-millions scale in its first year and is still used for strategic marketing decisions today.

*Stack: PyMC, Bayesian modelling, causal inference, marketing analytics*

### Agentic Management-Reporting System
An autonomous agent that lets managers interrogate live project status: surfacing blockers and at-risk workstreams, and flagging team members who are over- or under-utilised. The hard part was trust. I instrumented it with MLflow execution tracing to see exactly how it retrieves context and reasons, and an LLM-as-a-judge evaluation harness to test its answers against baselines before relying on them. Designed around small, granular, verifiable tasks so its behaviour stays reliable in production.

*Stack: LangGraph / PydanticAI, RAG, MLflow Tracing, LLM-as-a-judge*

### Data-Science Excellence Standard & Maturity Assessment
Authored the methodology an organisation uses to score how mature a data product is and to benchmark projects against each other on a common scale. A structured, unambiguous assessment spanning problem scoping (is the goal clear, what KPIs are we moving, what change counts as success), engineering maturity (version control, CI/CD, dev/test/acceptance/production hygiene, monitoring, drift detection, data-quality reporting, MLOps automation), modelling rigour (baselines, reconstruction of the KPIs a project claims to move) and stakeholder management. It turns "how good is this, really?" into something measurable and repeatable, and lets very different projects be compared fairly.

*Focus: standards, benchmarking, data-science governance*


## GenAI & Agents

### Production RAG for Decision Support
A retrieval system that gives front-line decision-makers fast, current answers drawn from a large and complex body of internal policy and external regulatory guidance, built to speed up a high-volume approval workflow. The hard parts were document parsing and the retrieval quality that depends on it. Working with the business, I assembled a validated "golden set" of question-answer pairs and ran it through an LLM-as-a-judge harness, which let the team keep improving the system against a fixed, trusted benchmark. I delivered the MVP that became the basis for the full product launch after my assignment ended.

*Stack: LangChain, ChromaDB / FAISS, document parsing, LLM-as-a-judge, custom evals*


## Predictive & Causal ML

### Causal & Classification for Industrial Equipment Monitoring
Two models working together on a production line. A classifier automatically assigns each production-loss event to a standard taxonomy (breakdown, minor stop, slow-down, changeover and so on), removing manual tagging by operators and standardising how losses are reported across sites that previously labelled the same events differently, which had undermined the credibility of reporting. A causal model then identifies which machine is the true root cause of a given loss, for example tracing a detected minor stop back to the upstream machine actually responsible for it. Together they make production-loss reporting both automatic and trustworthy. Deployed to production with drift detection.

*Stack: Scikit-learn, XGBoost, causal inference, Evidently, MLflow*

### Customer Retention Modelling with Experimentation
Designed the model and the A/B testing methodology end to end, to flag customers at risk of leaving or non-payment so the business could intervene proactively. It showed a statistically significant uplift versus control; I estimated the monetary value of that uplift and set the whole thing up as a reproducible pipeline that ran live throughout the pilot, rather than as a one-off analysis.

*Stack: XGBoost, A/B testing, Databricks, MLflow*

### Financial KPI Forecasting & Time-Series Standards
Built end to end with full ownership, and established the time-series practices that became the organisation's standard approach. The system lets a central team deep-dive into the forecasts of individual subsidiaries, compare them against the model's, and use the gap to drive a better planning dialogue across the group. Still in use today for global financial planning.

*Stack: Prophet, PyMC, time-series modelling, statistical forecasting*


## Optimisation & Decision Science

### Spare-Parts Allocation & Master-Data Quality
An optimisation system that helps sites share spare parts and position them at strategic locations for rapid transport in an emergency, cutting the amount of expensive spare stock that has to be held globally. I later returned to extend it with entity deduplication and master-data quality work: cleaning and matching records so that even more parts could be reliably shared and pooled, pushing global stock down further.

*Stack: optimisation, RecordLinkage / Dedupe, PySpark, master data management*

### Transportation Optimiser (Advisory)
Brought in to shape a transportation-optimiser initiative. I defined and protected the scope, produced documentation that all stakeholders signed off on, and explained the limitations, possibilities and trade-offs the business had to weigh to deliver within its budget and resources. The value here was as much about discipline as algorithms: without a clear, agreed scope the project risked drifting in endless modification and dying when the funding ran out.

*Focus: problem framing, scoping, stakeholder alignment, delivery strategy*


## Exploration

Alongside the work above I've explored a wide range of applied ML: real-time anomaly detection for manufacturing equipment, automated data-quality validation, a product-design recommender, warehouse bin allocation, delivery-route optimisation and churn prediction. Some became tools that are still in use; all of it sharpened a sense of what actually survives contact with production.
