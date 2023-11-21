import streamlit as st

def plot_rgb_color(r, g, b, plot_size=1):
    color = f"rgb({r}, {g}, {b})"
    st.markdown(f'<div style="background-color: {color}; width: {plot_size}rem; height: {plot_size}rem;"></div>', unsafe_allow_html=True)

def explore_rgb_colors(plot_size=0.5):
    for r in range(0, 256, 126):
        for g in range(0, 256, 126):
            for b in range(0, 256, 126):
                plot_rgb_color(r, g, b, plot_size)
                st.write(f'RGB: {r}, {g}, {b}')

if __name__ == "__main__":
    st.title("RGB Color Explorer")
    plot_size = st.slider("Adjust Plot Size:", 0.1, 2.0, 0.5, 0.1)
    explore_rgb_colors(plot_size)
