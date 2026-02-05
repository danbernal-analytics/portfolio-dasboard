import streamlit as st
import base64
import os

# =====================================================
# 1. CONFIGURACIÓN DE PÁGINA
# =====================================================
st.set_page_config(
    page_title="Un poco de mi:",
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# 2. ESTILOS CSS (TIPOGRAFÍA INTER + GLASSMORPHISM)
# =====================================================
def set_custom_design(image_relative_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_path, image_relative_path)
    
    background_style = "linear-gradient(135deg, #1a1a1a 0%, #0f1c15 100%)" 
    
    if os.path.exists(image_path):
        try:
            with open(image_path, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            background_style = f'url("data:image/jpeg;base64,{data}")'
        except:
            pass

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif !important;
        }}

        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.8)),
                        {background_style};
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        h1, h2, h3 {{
            color: #ffffff !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }}
        
        p, li, label, .stMarkdown {{
            color: #e0e0e0 !important;
            font-weight: 300;
            line-height: 1.6;
        }}

        /* TARJETAS GLASSMORPHISM */
        .card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 16px;
            padding: 24px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            margin-bottom: 20px;
            transition: transform 0.2s ease-in-out;
        }}
        
        .card:hover {{
            border: 1px solid rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
            background: rgba(255, 255, 255, 0.08);
        }}

        /* BOTONES */
        .stButton > button {{
            background: transparent;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            padding: 12px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
            width: 100%;
        }}
        
        .stButton > button:hover {{
            background: rgba(85, 123, 85, 0.6);
            border-color: #557B55;
            color: white;
        }}

        /* SIDEBAR */
        [data-testid="stSidebar"] {{
            background-color: rgba(10, 10, 10, 0.3) !important;
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255,255,255,0.05);
        }}

        /* ACENTOS */
        .highlight {{
            color: #4ade80; 
            font-weight: 600;
        }}
        
        .metric-value {{
            font-size: 1.5rem;
            font-weight: bold;
            color: #4ade80;
        }}

        /* --- ETIQUETA DE CORREO (GLASSMORPHISM) --- */
        .email-display {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            padding: 12px 24px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #4ade80 !important;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.3rem;
            transition: all 0.3s ease;
        }}
        
        .email-display:hover {{
            background: rgba(74, 222, 128, 0.05);
            border: 1px solid rgba(74, 222, 128, 0.2);
            transform: translateY(-1px);
        }}
        
        /* Skills Bars */
        .skill-bar {{
            background: rgba(255,255,255,0.1);
            border-radius: 4px;
            height: 8px;
            width: 100%;
            margin-top: 8px;
        }}
        .skill-fill {{
            background: #4ade80;
            height: 100%;
            border-radius: 4px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_custom_design("Assets/background.jpeg")

# =====================================================
# 3. NAVEGACIÓN
# =====================================================
def create_navigation():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
    
    with st.sidebar:
        st.image("Assets/Dan.png", use_container_width=True)
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown("## DAN BERNAL")
        # Cambio: Rol unificado según CV
        st.markdown("**Data & Football Analyst | Tactical, Performance & Growth Analytics | Applied Statistics**")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")
        
        options = {
            "🏠 Inicio": "home",
            "📊 Proyectos": "projects",
            "💼 Experiencia": "experience",
            "🛠 Stack Técnico": "skills",
            "⚡ Mi Enfoque": "proposal",
            "📬 Contacto": "contact"
        }
        
        for label, page in options.items():
            if st.button(label, key=f"nav_{page}", use_container_width=True):
                st.session_state.current_page = page
                st.rerun()

        st.markdown("---")
        # Botón de Descarga de CV
        cv_path = "assets/CV_Dan_Bernal.pdf" 
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 Descargar CV (PDF)",
                    data=pdf_file,
                    file_name="CV_Dan_Bernal.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        
        st.markdown("**Ubicación:** Toluca, México")

# =====================================================
# 4. PÁGINAS
# =====================================================

def home_page():
    st.markdown("# Del caos creativo a la <span class='highlight'>precisión analítica</span>", unsafe_allow_html=True)
    
    col_text, col_card = st.columns([1.5, 1])
    
    with col_text:
        # Cambio: Título alineado con CV
        st.markdown("""
        ### Data Analyst & Football Performance Analyst
        Mi formación diversa desarrolló una sensibilidad única para detectar patrones donde todo parece caos. 
        Transformo datos complejos y desestructurados en estrategias accionables para el fútbol y los negocios.
        """)
        
        st.markdown("""
        Mi diferencial único: **La capacidad de ser puente entre dominios** - traduciendo necesidades cualitativas 
        en métricas cuantificables y hallazgos técnicos en narrativas estratégicas.
        """)

    with col_card:
        st.markdown("""
        <div class='card'>
            <h4>Especialidades</h4>
            <ul style="list-style-type: none; padding: 0;">
                <li style="margin-bottom: 15px;">⚽ <strong>Tactical & Football Analytics:</strong> Modelado predictivo (Log Loss) y métricas avanzadas de rendimiento deportivo.</li>
                <li style="margin-bottom: 15px;">📈 <strong>Growth Analytics:</strong> Optimización de Funnels, KPIs y toma de decisiones estratégica basada en datos.</li>
                <li style="margin-bottom: 5px;">🎨 <strong>Applied Statistics & Storytelling:</strong> Reducción de incertidumbre mediante estadística inferencial y narrativas visuales de impacto.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Impacto Reciente")
    c1, c2, c3 = st.columns(3)
    with c1:
        # Cambio: Log Loss 1.01 (Promedio Notebook/LinkedIn)
        st.markdown("""
        <div class='card'>
            <div class='metric-value'>1.01</div>
            <p><strong>Log Loss</strong> en modelo predictivo Liga MX, superando benchmarks de mercado.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='card'>
            <div class='metric-value'>95%</div>
            <p><strong>Satisfacción de cliente</strong> en gestión de proyectos complejos y traducción de necesidades.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class='card'>
            <div class='metric-value'>100%</div>
            <p><strong>Puntualidad</strong> en la ejecución de timelines y dependencias críticas en producción.</p>
        </div>
        """, unsafe_allow_html=True)

def projects_page():
    st.title("Portfolio de Proyectos")
    st.markdown("Una selección de análisis aplicado a deportes y negocios.")
    
    # --------------------------------------------------------------------------------
    # PROYECTO 1: LIGA MX (FLAGSHIP)
    # --------------------------------------------------------------------------------
    with st.expander("⚽ **Liga MX Match Predictor (Machine Learning)**", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Objetivo:** Cuantificar la incertidumbre en el fútbol mexicano mediante análisis probabilístico por partido. 
                        
            El fútbol es un deporte de baja frecuencia de eventos y alta varianza. El objetivo de este proyecto no es realizar predicciones deterministas (ganar/perder), sino construir un modelo estadístico calibrado que estime probabilidades reales para los resultados: Victoria Local, Empate y Victoria Visitante.
            
            **Solución Técnica:**
            * Feature Engineering: Ventanas móviles de forma (últimos 5 partidos) y **Tiering Histórico** de plantillas.
            * Comparativa: Validación de **Regresión Logística** calibrada vs XGBoost para asegurar generalización.
            
            **Resultado:**
            Alcance de un **Log Loss de 1.01**, superando el baseline de mercado de 1.05.
            """)
            st.link_button("🔗 Ver Dashboard en Vivo", "https://ligamx-predictor.streamlit.app/")
            st.link_button("📂 Ver Notebook en GitHub", "https://github.com/danbernal-analytics/liga-mx-match-prediction")
            st.image("Assets/Liga.png", use_container_width=True)
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("**Stack:**")
            st.markdown("`Python` `Scikit-learn` `XGBoost` `LogisticRegression` ")
            st.markdown("`Streamlit` `Plotly` `Pandas`")
            st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------------
    # PROYECTO 2: LIGAS EUROPEAS
    # --------------------------------------------------------------------------------
    with st.expander("🌍 **Análisis de Rendimiento Ofensivo y Modelado Predictivo en las 5 Grandes Ligas Europeas**"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Objetivo:** Identificar ineficiencias en el mercado evaluando el rendimiento real vs los goles anotados. 
            
            El fútbol moderno se caracteriza por la búsqueda constante de ventajas competitivas a través del análisis de datos. Mientras que la predicción de resultados es una aplicación valiosa, entender los procesos subyacentes que generan esos resultados es igualmente crucial. Este proyecto se enfoca en analizar la relación entre el volumen ofensivo (tiros) y la eficiencia en la conversión a goles en las cinco principales ligas europeas de fútbol.
            
            **Solución Técnica:**
            * Análisis Exploratorio de Datos (EDA) exhaustivo para definir métricas de creación y conversión.
            * Entrenamiento de modelo **XGBoost** optimizado para predecir Goles Esperados (xG).
            
            **Impacto:**
            Detección de equipos y jugadores subvalorados con métricas de "Rendimiento Real vs Observado" para scouting táctico. 
                        
           La contundencia es una habilidad táctica independiente. Para un club, es más sostenible y económico entrenar la calidad del tiro y la toma de decisiones que simplemente intentar comprar más volumen de juego. **En el fútbol moderno, no gana quien más dispara, sino quien mejor elige cuándo hacerlo.**
            """)
            st.link_button("📂 Ver Notebook en GitHub", "https://github.com/danbernal-analytics/european-football-performance")
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("**Stack:**")
            st.markdown("`Python` `XGBoost` `Matplotlib`")
            st.markdown("`EDA` `Feature Engineering`")
            st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------------
    # PROYECTO 3: ROI & LTV
    # --------------------------------------------------------------------------------
    with st.expander("💰 **Optimización de ROI vía Análisis LTV/CAC**"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Objetivo:** Reasignación estratégica de presupuesto de marketing digital para maximizar rentabilidad.
            
            **Solución Técnica:**
            * Modelo de **Análisis de Cohortes** utilizando SQL y Python.
            * Proyección de LTV (Lifetime Value) futuro basado en curvas de retención históricas.
            
            **Resultado:**
            **+18% en eficiencia de gasto** y +15% de aumento en ROI global al identificar los 3 canales de adquisición más rentables.
            """)
            st.link_button("📂 Ver Notebook en GitHub", "https://github.com/danbernal-analytics/growth-analytics-ltv-cac")
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("**Stack:**")
            st.markdown("`Python` `SQL` `Cohort Analysis`")
            st.markdown("`Seaborn` `Business Intelligence`")
            st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------------
    # PROYECTO 4: A/B TESTING
    # --------------------------------------------------------------------------------
    with st.expander("🧪 **Incremento de Ingresos con A/B Testing**"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Objetivo:** Validar cambios en el flujo de producto para incrementar ingresos sin afectar la retención.
            
            **Solución Técnica:**
            * Diseño experimental A/A/B y cálculo de tamaño de muestra.
            * Ejecución de pruebas de hipótesis estadísticas (**Z-test**) utilizando la librería SciPy.
            
            **Resultado:**
            Validación estadística de una variante ganadora que aumentó la conversión en **1.2%**, proyectando **$5K USD** mensuales adicionales.
            """)
            st.link_button("📂 Ver Notebook en GitHub", "https://github.com/danbernal-analytics/ab-testing-conversion")
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("**Stack:**")
            st.markdown("`Python` `SciPy` `Statsmodels`")
            st.markdown("`Experiment Design` `Inferencia`")
            st.markdown("</div>", unsafe_allow_html=True)

def experience_page():
    st.title("Experiencia Profesional")
    
    st.markdown("""
    <div class='card'>
        <h3 class='highlight'>Gestor de Operaciones & Análisis Comercial</h3>
        <p style='margin-bottom:5px;'><strong>Purple Outfit</strong> | Toluca, México | 2017 - 2024</p>
        <p><em>E-commerce de moda y retail</em></p>
        <ul style='margin-top:10px;'>
            <li>Optimicé procesos logísticos con gestión basada en datos, mejorando la <strong>eficiencia operativa en un 15%</strong>.</li>
            <li>Lideré estrategias de retención posventa logrando una tasa de <strong>retención del 90%</strong>.</li>
            <li>Análisis de tendencias para optimización de inventario, reduciendo costos en un 10%.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
            <h4 class='highlight'>Líder de Proyectos & QA</h4>
            <p><strong>Foto Rivero</strong> | 2011 - 2017</p>
            <ul>
                <li>Ejecución de proyectos con entrega <strong>100% puntual</strong>.</li>
                <li>Establecí métodos rigurosos de evaluación de material visual (Habilidad transferible a Data Cleaning).</li>
                <li>Logré un <strong>95% de satisfacción</strong> del cliente mediante traducción de necesidades.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='card'>
            <h4 class='highlight'>Productor & Gestor de Eventos</h4>
            <p><strong>Quattro Presenta</strong> | 2009 - 2011</p>
            <ul>
                <li>Gestión de presupuesto y recursos logrando <strong>100% de cumplimiento del budget</strong>.</li>
                <li>Coordinación de logística compleja para más de 50 eventos (Gestión de Riesgos).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def skills_page():
    st.title("Arsenal Técnico")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💻 Lenguajes & Herramientas")
        st.markdown("""
        <div class='card'>
            <p><strong>Python:</strong> Pandas, NumPy, Scikit-learn, SciPy</p>
            <div class='skill-bar'><div class='skill-fill' style='width: 81%;'></div></div>
            <br>
            <p><strong>SQL:</strong> PostgreSQL, MySQL</p>
            <div class='skill-bar'><div class='skill-fill' style='width: 75%;'></div></div>
            <br>
            <p><strong>Visualización:</strong> Tableau, Matplotlib, Seaborn, Streamlit</p>
            <div class='skill-bar'><div class='skill-fill' style='width: 80%;'></div></div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### 🧠 Metodologías de Negocio")
        st.markdown("""
        <div class='card'>
            <p><strong>Growth Analytics:</strong> Cohortes, Segmentación</p>
            <div class='skill-bar'><div class='skill-fill' style='width: 85%;'></div></div>
            <br>
            <p><strong>Experimentación:</strong> A/B Testing, Diseño de Experimentos</p>
            <div class='skill-bar'><div class='skill-fill' style='width: 88%;'></div></div>
            <br>
            <p><strong>Football Analytics:</strong> Modelado Probabilístico, xG</p>
            <div class='skill-bar'><div class='skill-fill' style='width: 92%;'></div></div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("### 🎓 Educación")
    st.markdown("""
    * **Data Analyst Certificate** - TripleTen (2025)
    * **Carrera en Fotografía** - Escuela Activa de Fotografía (2006-2008)
    """)

def proposal_page():
    st.title("Mi Enfoque Único")
    
    st.image("Assets/workflow.jpeg", use_container_width=True)

    st.markdown("""
    ### El Puente entre Dominios
    
    Mi valor no reside solo en escribir código, sino en mi capacidad de **traducir**.
    """)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class='card'>
            <h4>Sensibilidad Visual</h4>
            <p>Años en fotografía me dieron la capacidad de detectar <strong>patrones, ritmo y espacio</strong>. Aplico esta visión para crear narrativas visuales e identificar anomalías que podrían pasarse por alto.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class='card'>
            <h4>Orden en el Caos</h4>
            <p>Mi experiencia en producción musical y eventos me enseñó que la curiosidad disciplinada crea orden. Busco generar <strong>paz operativa</strong> a través de datos estructurados y procesos eficientes.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class='card'>
            <h4>Dimensión Táctica</h4>
            <p>Entiendo el contexto del juego. Traduzco métricas complejas en <strong>insights estratégicos</strong> accionables, hablando el lenguaje que la dirección deportiva necesita para decidir.</p>
        </div>
        """, unsafe_allow_html=True)

def contact_page():
    st.title("Contacto")
    
    c1, c2 = st.columns([1.5, 1])
    
    with c1:
        st.markdown("""
        <div class='card'>
            <h3>¿Hablamos de datos?</h3>
            <p>Estoy disponible para oportunidades como <strong>Data Analyst</strong> o <strong>Football Performance Analyst</strong> (Presencial/Remoto/Híbrido).</p>
            <p style='margin-bottom: 15px;'>Puedes contactarme directamente en:</p>
            <a href="mailto:danbernal.analytics@gmail.com" class="email-display">
                danbernal.analytics@gmail.com
            </a>
        </div>
    """, unsafe_allow_html=True)

    with c2:
        st.markdown("### Descargar CV")
        
        # Ruta al archivo PDF (Asegúrate de que el archivo esté en esta ruta)
        cv_path = "Assets/Dan_Bernal_CV.pdf" 
        
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 Descargar CV (PDF)",
                    data=pdf_file,
                    file_name="Dan_Bernal_CV.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        else:
            st.warning("⚠️ CV no disponible por el momento. Por favor contáctame por correo.")
            
        st.markdown("---")
        st.markdown("**Ubicación:** Toluca, México")
        st.markdown("**Tel:** (+52) 7228 259397")

# =====================================================
# MAIN
# =====================================================
def main():
    create_navigation()
    
    if st.session_state.current_page == "home": home_page()
    elif st.session_state.current_page == "projects": projects_page()
    elif st.session_state.current_page == "experience": experience_page()
    elif st.session_state.current_page == "skills": skills_page()
    elif st.session_state.current_page == "proposal": proposal_page()
    elif st.session_state.current_page == "contact": contact_page()

if __name__ == "__main__":
    main()

    ### Agregar link del dashboard

    ### tal vez algunas imagenes de los proyectos