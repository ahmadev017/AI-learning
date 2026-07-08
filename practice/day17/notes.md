# Overview

Today we learned the fundamentals of LangGraph, a framework for building stateful, controllable AI workflows.

Unlike ReAct agents that focus on reasoning and tool usage, LangGraph focuses on workflow orchestration, allowing AI agents to maintain state, make routing decisions, loop, branch, and execute complex workflows.

# Key Concepts
1. State

State is the shared memory of the workflow.

Every node:

Reads state
Updates state
Returns state

Instead of passing many independent variables, LangGraph passes a single state object through the workflow.

Example:

state = {
    "query": "...",
    "context": [],
    "answer": "",
    "needs_more": False
}
2. TypedDict

Used to define the schema of the state.

Example:

class AgentState(TypedDict):
    query: str
    context: list[str]
    answer: str
    needs_more: bool

Benefits:

Type safety
Better autocomplete
Easier debugging
Clear contract between nodes
3. Nodes

A node is simply a Python function.

General pattern:

def node(state):
    ...
    return state

Responsibilities:

Perform one task
Update state
Never decide workflow execution

Nodes should follow the Single Responsibility Principle (SRP).

4. Edges

Edges define the execution flow.

Example:

graph.add_edge("search", "generate")

Meaning:

Always execute generate after search.

5. Conditional Edges

Conditional edges allow dynamic execution.

Instead of always following one path, LangGraph asks a router function which node should execute next.

Example:

graph.add_conditional_edges(
    "generate",
    router
)
6. Router

A router is another Python function.

Its only responsibility is deciding the next node.

Example:

def router(state):

    if state["needs_more"]:
        return "search"

    return END
7. START and END

Every graph requires:

START

↓

Workflow

↓

END

START defines the entry point.

END terminates execution.

8. StateGraph

Creates the workflow object.

graph = StateGraph(AgentState)

Think of it as an empty factory waiting for nodes and edges.

9. Compile
app = graph.compile()

Compile validates the graph and converts it into an executable workflow.

10. Invoke
result = app.invoke(initial_state)

Execution begins at START.

LangGraph automatically:

Executes nodes
Passes state
Follows edges
Stops at END
Internal Workflow
State

↓

Node

↓

Updated State

↓

Router

↓

Next Node

↓

Updated State

↓

END
Why LangGraph Exists

ReAct answers:

"What should I do next?"

LangGraph answers:

"How should the entire workflow be organized?"

ReAct = Reasoning

LangGraph = Orchestration

Real-world Analogy

Package Delivery

Package = State

Warehouse = Node

Road = Edge

Traffic Signal = Router

Destination = END

The package stays the same.

Only its contents and labels change.

Engineering Lessons Learned

Nodes should never call other nodes.

Bad:

Search Node

↓

Generate Node

↓

Search Node

Good:

Node updates state.

Router decides the next node.

Graph executes it.

# Important Functions
StateGraph()

add_node()

add_edge()

add_conditional_edges()

compile()

invoke()
Advantages of LangGraph
Stateful workflows
Branching
Loops
Retry logic
Human-in-the-loop
Multi-agent systems
Easy debugging
Modular architecture

# Limitations

Requires careful workflow design.

Poor routing logic can create infinite loops.

Termination conditions must always be considered.

# Real-world Applications
AI Research Agents
Customer Support Agents
RAG Pipelines
Autonomous Agents
Multi-step Document Analysis
AI Coding Assistants
Search Systems
Key Takeaways
State is the single source of truth.
Nodes update state.
Routers decide workflow.
Graph executes router decisions.
LangGraph orchestrates the entire workflow