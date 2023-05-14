import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
from hydralit import HydraHeadApp
import altair as alt


class HomeApp(HydraHeadApp):
     
    def run(self):
        # st.set_page_config(layout="wide")
        with open('C:\\Users\\DC\\Documents\\MachVIS\\FYP\\hydralit_app\\farm-dashboard\\apps\\styles.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.markdown('### Metrics')
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Area", "11 Acres")
        col2.metric("Average NDVI", "0.155", "-2%")
        col3.metric("Phenotypes", "100 +")

        # Row B

        data = pd.DataFrame(
                [[0.01,0.02], 
                [0.25,0.03], 
                [0.5,0.5], 
                [0.17,0.25]], index= ['26-12-22', '20-01-23', '24-02-23', '20-04-23'],
                columns=['NDVI', 'SAVI'])
        data.index = pd.to_datetime(data.index, format='%d-%m-%y')

        @st.cache_data()
        def get_temperature_chart():
            daily_temp = pd.read_csv('C:\\Users\\DC\\Documents\\MachVIS\\FYP\\hydralit_app\\farm-dashboard\\data\\daily_temerature.csv')
            scale = alt.Scale(
                domain=["Sunny", "Clear", "Partly cloudy ", "Patchy rain possible", "Cloudy"],
                range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
            )
            color = alt.Color("weather:N", scale=scale)
            brush = alt.selection_interval(encodings=["x"])
            click = alt.selection_multi(encodings=["color"])
            points = (
                alt.Chart(daily_temp, title="Temperature and Rainfall Analysis")
                .mark_point()
                .encode(
                    alt.X("Date:T", title="Date"),
                    alt.Y(
                        "Hourly Temperature:Q",
                        title="Average Daily Temperature (C)",
                        scale=alt.Scale(domain=[5, 30]),
                    ),
                    # color=alt.condition(brush, color, alt.value("lightgray")),
                    size=alt.Size("Hourly Precipitation:Q", scale=alt.Scale(range=[5, 200]), title = "Daily Precipitation (mm)"),
                )
                # .properties(width=550, height=300)
                # .add_selection(brush)
                # .transform_filter(click)
            )
            areas = (
                alt.Chart(daily_temp, title=f"Humidity Analysis")
                .mark_area(
                    interpolate='monotone',
                    line={'color':'#e7ba52'},
                    color=alt.Gradient(
                        gradient='linear',
                        stops=[alt.GradientStop(color='white', offset=0),
                            alt.GradientStop(color='#aec7e8', offset=1)],
                        x1=1,
                        x2=1,
                        y1=1,
                        y2=0
                    )
                ).encode(
                    alt.X('Date:T'),
                    alt.Y('Hourly Humidity:Q', title="Daily Humidity (%)")
                )
            )



            return points, areas
        
        def get_chart(data, indice, line_color, gradient_color):
            hover = alt.selection_single(
                fields=["index"],
                nearest=True,
                on="mouseover",
                empty="none",
            )

            areas = (
                alt.Chart(data.reset_index(), title=f"Evolution of {indice}")
                .mark_area(
                    interpolate='monotone',
                    line={'color':f'{line_color}'},
                    color=alt.Gradient(
                        gradient='linear',
                        stops=[alt.GradientStop(color='white', offset=0),
                            alt.GradientStop(color=f'{gradient_color}', offset=1)],
                        x1=1,
                        x2=1,
                        y1=1,
                        y2=0
                    )
                ).encode(
                    alt.X('index:T'),
                    alt.Y(f'{indice}:Q')
                )
            )

            points = (
                alt.Chart(data.reset_index())
                .mark_point(size=50, filled=True, color='red')
                .encode(
                    x='index:T',
                    y=f'{indice}:Q'
                )
            )
        


            return (areas + points).interactive()

        
        c1, c2 = st.columns((7,5))
        c3, c4 = st.columns((7,5))
        with st.container():
            with c1:
                chart = get_chart(data, 'NDVI', '#7fc97f', '#fa8d0b')
                st.altair_chart(
                    chart.interactive(),
                    theme="streamlit",
                    use_container_width=True
                    )
            with c2:
                chart, _ = get_temperature_chart()
                st.altair_chart(
                    chart,
                    theme="streamlit",
                    use_container_width=True
                    )


            

        with st.container():
            with c3:
                chart = get_chart(data, 'SAVI', '#7fc97f', '#43ff64d9')
                st.altair_chart(
                    chart.interactive(),
                    theme="streamlit",
                    use_container_width=True
                    )
            with c4:
                _, chart = get_temperature_chart()
                st.altair_chart(
                    chart,
                    theme="streamlit",
                    use_container_width=True
                    )               


