from typing import TypedDict

from langgraph.graph import StateGraph, START, END


# =====================================================
# STATE
# =====================================================

class AgentState(TypedDict):
    query: str
    context: list[str]
    answer: str
    needs_more: bool
    search_count: int


# =====================================================
# NODE 1
# =====================================================

def understand_node(state: AgentState):

    print("\n Understanding User Query")

    state["query"] = state["query"].strip()

    return state


# =====================================================
# NODE 2
# =====================================================

def search_node(state: AgentState):

    print("\n Searching Knowledge Base")

    state["search_count"] += 1

    if state["search_count"] == 1:

        state["context"] = [
            "LangGraph is a framework for stateful AI workflows."
        ]

    else:

        state["context"].append(
            "LangGraph supports loops, conditional edges and human-in-the-loop."
        )

    return state


# =====================================================
# NODE 3
# =====================================================

def generate_node(state: AgentState):

    print("\n Generating Answer")

    state["answer"] = (
        f"I found {len(state['context'])} document(s)."
    )

    if len(state["context"]) < 2:

        print(" Not enough information.")

        state["needs_more"] = True

    else:

        print(" Enough information.")

        state["needs_more"] = False

    return state


# =====================================================
# ROUTER
# =====================================================

def router(state: AgentState):

    print("\n Router Checking State")

    if state["needs_more"]:

        print(" Going back to Search Node\n")

        return "search"

    print(" Ending Graph\n")

    return END


# =====================================================
# CREATE GRAPH
# =====================================================

graph = StateGraph(AgentState)


# =====================================================
# REGISTER NODES
# =====================================================

graph.add_node("understand", understand_node)
graph.add_node("search", search_node)
graph.add_node("generate", generate_node)


# =====================================================
# CONNECT GRAPH
# =====================================================

graph.add_edge(START, "understand")

graph.add_edge("understand", "search")

graph.add_edge("search", "generate")


graph.add_conditional_edges(
    "generate",
    router
)


# =====================================================
# COMPILE
# =====================================================

app = graph.compile()


# =====================================================
# INITIAL STATE
# =====================================================

initial_state = {
    "query": "What is LangGraph?",
    "context": [],
    "answer": "",
    "needs_more": False,
    "search_count": 0,
}


# =====================================================
# RUN
# =====================================================

result = app.invoke(initial_state)


print("\n==========================")
print("FINAL STATE")
print("==========================")

print(result)