# WorkflowGen AI: Autonomous Workflow Agent

**Transform natural language into executable workflows**  
An end-to-end AI system that compresses text instructions into structured workflows (JSON/YAML/BPMN) with dependencies, conditions, and actions.

![Workflow Visualization Example](docs/workflow_example.png)  
*Example: Generated workflow from text instructions*

## Key Features

- **Text-to-Workflow Compression**: Convert prose into step-by-step workflows
- **Multi-Format Output**: JSON, YAML, or BPMN diagrams
- **Context-Aware**: Handles dependencies, conditions, and loops
- **Extensible Architecture**: Plugins for 50+ tools (n8n, Zapier, Airflow)
- **Enterprise-Ready**: RBAC, audit logging, and versioning

## Quick Start

```bash
# Install (Python 3.10+)
pip install -r requirements.txt

# Generate a workflow
python -m src.cli --text "First collect user data, then validate if email exists, else retry"

# Output:
{
  "workflow_name": "user_data_validation",
  "steps": [
    {
      "step_id": "collect_data",
      "actions": ["requests.get"],
      "dependencies": []
    },
    {
      "step_id": "validate_email",
      "conditions": "if email is None: retry",
      "dependencies": ["collect_data"]
    }
  ]
}

graph TD
    A[Natural Language Input] --> B(Text Preprocessor)
    B --> C[Transformer Encoder]
    C --> D[Workflow Decoder Head]
    D --> E{Output Format}
    E --> F[JSON]
    E --> G[YAML]
    E --> H[BPMN]