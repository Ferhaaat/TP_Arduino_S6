import numpy as np
import streamlit as st
import plotly.graph_objects as go



st.image('enspima.svg')
st.balloons()
st.markdown("# Magnetometer data visualisation App, made by Ferhat and Valentin")

st.write("We are so glad to see you here. ✨ " 
         "You can visualise our data here")

st.markdown('**the navigation is better in paysage mode or on a computer**')


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
