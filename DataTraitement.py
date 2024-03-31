import numpy as np
import streamlit as st
import plotly.graph_objects as go



st.image('enspima.svg')

# Charger les données
data = np.loadtxt("data.txt")

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Créer le graphe 3D avec Plotly
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                   marker=dict(size=5, color='orange'))])

# Ajouter des titres aux axes
fig.update_layout(scene = dict(
                    xaxis_title='x',
                    yaxis_title='y',
                    zaxis_title='z'),
                  width=700, height=700)

# Afficher le graphe dans Streamlit
st.plotly_chart(fig)
