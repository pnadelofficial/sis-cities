import streamlit as st
import pandas as pd
import networkx as nx
import random

st.title("Six Degrees of Sister City-peration")
st.subheader("A Sister Cities Game")

def get_subgraph(G, n=6):
    start_node = random.choice(list(G.nodes()))
    subgraph_nodes = {start_node}
    subgraph_list = [start_node]

    while len(subgraph_nodes) < n:
        candidates = set()
        for node in subgraph_nodes:
            candidates.update(G.neighbors(node))
        candidates -= subgraph_nodes
        if not candidates:
            break
        new_node = random.choice(list(candidates))
        subgraph_nodes.add(new_node)
        subgraph_list.append(new_node)

    return subgraph_list

@st.cache_data
def load_data():
    df = pd.read_csv("sister_cities.csv")
    G = nx.Graph()
    for i, row in df.iterrows():
        G.add_node(row["city"], country=row['country'])
        G.add_node(row['sister'])
        G.add_edge(row['city'], row["sister"])

    return df, G
df, G = load_data()

if "response" not in st.session_state:
    st.session_state['response'] = {}
if "graph" not in st.session_state:
    init_graph = get_subgraph(G)
    while len(init_graph) < 6:
        init_graph = get_subgraph(G)
    st.session_state['graph'] = init_graph

#st.write(st.session_state['graph'])

city_1 = st.text_input(f"Guess a sister city of {st.session_state['graph'][0]}...")
if city_1:
    if city_1 == st.session_state['graph'][1]:
        st.session_state['response']['city_1'] = city_1
        st.success("Nice! 1/6")
    else:
        st.error("Wrong!")
    
    city_2 = st.text_input(f"Guess a sister city of {st.session_state['graph'][1]}...")
    if city_2:
        if city_2 == st.session_state['graph'][2]:
            st.session_state['response']['city_2'] = city_2
            st.success("Good job! 2/6")
        else:
            st.error("Wrong!")
    
        city_3 = st.text_input(f"Guess a sister city of {st.session_state['graph'][2]}...")
        if city_3:
            if city_3 == st.session_state['graph'][3]:
                st.session_state['response']['city_3'] = city_3
                st.success("Wow! 3/6")
            else:
                st.error("Wrong!")
            
            city_4 = st.text_input(f"Guess a sister city of {st.session_state['graph'][3]}...")
            if city_4:
                if city_4 == st.session_state['graph'][4]:
                    st.session_state['response']['city_4'] = city_4
                    st.success("Hell yeah! 4/6")
                else:
                    st.error("Wrong!")
                
                city_5 = st.text_input(f"Guess a sister city of {st.session_state['graph'][4]}...")
                if city_5:
                    if city_5 == st.session_state['graph'][5]:
                        st.session_state['response']['city_5'] = city_5
                        st.success("OMG! 5/6")
                    else:
                        st.error("Wrong!")
                    
                    city_6 = st.text_input(f"Guess a sister city of {st.session_state['graph'][5]}...")
                    if city_6:
                        if city_6 == st.session_state['graph'][6]:
                            st.session_state['response']['city_6'] = city_6
                            st.success("You did it! 6/6")
                        else:
                            st.error("Wrong!")
    
if st.button("Play again"):
    st.cache_data.clear()
    del st.session_state['response']
    del st.session_state['graph']
    df, G = load_data()