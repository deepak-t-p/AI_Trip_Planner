from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState,END,START
from langgraph.prebuilt import ToolNode, tools_condition



class GraphBuilder():
    def __init__(self):

        self.tools=[
            #WeatherInfoTool(),
            #PlaceSearchTool(),
            #CalculatorTool(),
            #CurrencyConvertorTool()
        ]

    def agent_function(self):
        pass

    def build_graph(self):
       graph_builder= StateGraph(MessagesState)
       
       graph_builder.add_node("agent", self.agent_function)
       graph_builder.add_node("tools",ToolNode(tools=self.tools))
       graph_builder.add_edge(START,"agent")
       graph_builder.add_conditional_edges("agent", tools_condition)
       graph_builder.add_edge("tools","agent")
       graph_builder.add_edge("agent",END)

    def __call__(self):
        pass