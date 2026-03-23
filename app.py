import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AeroInsight | UAE Aerospace Analytics",
    page_icon="✈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3, .big-title {
    font-family: 'Syne', sans-serif !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0f1e 0%, #0d1b2a 100%);
    border-right: 1px solid #1e3a5f;
}
[data-testid="stSidebar"] * {
    color: #c8d8e8 !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label {
    color: #7eb8d4 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* Main background */
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* Hero header */
.hero-header {
    background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 50%, #0f2440 100%);
    border: 1px solid #1e3a5f;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(30,120,200,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    color: #ffffff;
    margin: 0;
    letter-spacing: -0.02em;
}
.hero-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.95rem;
    color: #7eb8d4;
    margin: 0.4rem 0 0 0;
    font-weight: 300;
}
.hero-badge {
    display: inline-block;
    background: rgba(30,120,200,0.2);
    border: 1px solid #1e78c8;
    color: #7eb8d4;
    font-size: 0.72rem;
    padding: 3px 12px;
    border-radius: 20px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}

/* Metric cards */
.metric-card {
    background: linear-gradient(135deg, #0d1b2a, #0f2440);
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    text-align: center;
}
.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #4fc3f7;
    line-height: 1;
}
.metric-label {
    font-size: 0.75rem;
    color: #7eb8d4;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.4rem;
}

/* Section headers */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #ffffff;
    padding: 0.5rem 0;
    border-bottom: 2px solid #1e78c8;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-tag {
    font-size: 0.65rem;
    background: #1e78c8;
    color: white;
    padding: 2px 8px;
    border-radius: 4px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-family: 'DM Sans', sans-serif;
}

/* Algorithm tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: #0a0f1e;
    padding: 4px;
    border-radius: 10px;
    border: 1px solid #1e3a5f;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #7eb8d4;
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0.5rem 1.2rem;
}
.stTabs [aria-selected="true"] {
    background: #1e78c8 !important;
    color: white !important;
}

/* Result boxes */
.result-box {
    background: #0d1b2a;
    border: 1px solid #1e3a5f;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin: 0.5rem 0;
}
.result-box h4 {
    font-family: 'Syne', sans-serif;
    color: #4fc3f7;
    margin: 0 0 0.5rem 0;
    font-size: 0.95rem;
}

/* Insight pills */
.insight-pill {
    display: inline-block;
    background: rgba(30,120,200,0.15);
    border: 1px solid #1e78c8;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.8rem;
    color: #7eb8d4;
    margin: 3px 3px 3px 0;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0a0f1e; }
::-webkit-scrollbar-thumb { background: #1e3a5f; border-radius: 3px; }

/* Stmetric override */
[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    color: #4fc3f7 !important;
    font-size: 1.8rem !important;
}
[data-testid="stMetricLabel"] {
    color: #7eb8d4 !important;
    font-size: 0.78rem !important;
}
</style>
""", unsafe_allow_html=True)

# ── Data loader ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("uae_aerospace_survey_2000_respondents.csv")
    return df

df = load_data()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0 1.5rem;'>
        <div style='font-family:Syne,sans-serif; font-size:1.4rem; font-weight:800; color:#ffffff;'>✈ AeroInsight</div>
        <div style='font-size:0.72rem; color:#7eb8d4; letter-spacing:0.1em; text-transform:uppercase; margin-top:4px;'>UAE Aerospace Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='font-size:0.7rem;color:#4fc3f7;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.5rem;'>Global Filters</div>", unsafe_allow_html=True)

    personas = ["All"] + sorted(df["persona"].unique().tolist())
    sel_persona = st.selectbox("Persona", personas)

    org_types = ["All"] + sorted(df["q2_org_type"].unique().tolist())
    sel_org = st.selectbox("Organisation Type", org_types)

    locations = ["All"] + sorted(df["q5_location"].unique().tolist())
    sel_loc = st.selectbox("Location", locations)

    fleet_sizes = ["All"] + ["1-10", "11-30", "31-80", "81-200", "200+"]
    sel_fleet = st.selectbox("Fleet Size", fleet_sizes)

    st.markdown("---")
    st.markdown("<div style='font-size:0.7rem;color:#4fc3f7;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.5rem;'>Algorithm Settings</div>", unsafe_allow_html=True)
    n_clusters = st.slider("K-Means Clusters", 2, 8, 4)
    min_support = st.slider("ARM Min Support", 0.05, 0.4, 0.1, 0.01)
    min_confidence = st.slider("ARM Min Confidence", 0.3, 0.9, 0.5, 0.05)
    test_size = st.slider("Train/Test Split", 0.1, 0.4, 0.2, 0.05)

    st.markdown("---")
    st.markdown("<div style='font-size:0.65rem;color:#1e3a5f;text-align:center;'>Built by Aakash · AeroInsight v1.0</div>", unsafe_allow_html=True)

# ── Apply filters ─────────────────────────────────────────────────────────────
dff = df.copy()
if sel_persona != "All":
    dff = dff[dff["persona"] == sel_persona]
if sel_org != "All":
    dff = dff[dff["q2_org_type"] == sel_org]
if sel_loc != "All":
    dff = dff[dff["q5_location"] == sel_loc]
if sel_fleet != "All":
    dff = dff[dff["q3_fleet_size"] == sel_fleet]

# ── Hero header ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-header">
    <div class="hero-badge">Data-Driven Decision Making · UAE Aerospace</div>
    <div class="hero-title">AeroInsight Analytics Dashboard</div>
    <div class="hero-subtitle">Predictive Maintenance Intelligence Platform · Survey Analysis · 2000 Respondents · UAE & GCC Aerospace Sector</div>
</div>
""", unsafe_allow_html=True)

# ── KPI row ───────────────────────────────────────────────────────────────────
k1, k2, k3, k4, k5, k6 = st.columns(6)
hot_pct = round((dff["lead_label"] == "Hot").mean() * 100, 1)
warm_pct = round((dff["lead_label"] == "Warm").mean() * 100, 1)
avg_spend = dff["annual_spend_usd"].mean()
avg_bpa = dff["budget_per_aircraft_usd"].mean()
avg_dm = round(dff["q11_digital_maturity"].mean(), 1)
total = len(dff)

with k1:
    st.metric("Respondents", f"{total:,}")
with k2:
    st.metric("Hot Leads", f"{hot_pct}%")
with k3:
    st.metric("Warm Leads", f"{warm_pct}%")
with k4:
    st.metric("Avg MRO Spend", f"${avg_spend/1e6:.1f}M")
with k5:
    st.metric("Avg Budget/AC", f"${avg_bpa:,.0f}")
with k6:
    st.metric("Avg Digital Maturity", f"{avg_dm}/10")

st.markdown("<br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════════
# TABS
# ════════════════════════════════════════════════════════════════════════════════
tab0, tab1, tab2, tab3, tab4 = st.tabs([
    "📊  Overview",
    "🤖  Classification",
    "🔵  Clustering",
    "🔗  Association Rules",
    "📈  Regression"
])

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 0 — OVERVIEW
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab0:
    st.markdown('<div class="section-header">Survey Overview <span class="section-tag">Demographics</span></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        lead_counts = dff["lead_label"].value_counts().reset_index()
        lead_counts.columns = ["Lead Label", "Count"]
        color_map = {"Hot": "#ef5350", "Warm": "#42a5f5", "Exploring": "#ffa726", "Not Interested": "#78909c"}
        fig = px.pie(lead_counts, names="Lead Label", values="Count",
                     color="Lead Label", color_discrete_map=color_map,
                     title="Lead Label Distribution (Q25 — Classification Target)",
                     hole=0.45)
        fig.update_traces(textposition='outside', textinfo='percent+label')
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            legend=dict(orientation="h", yanchor="bottom", y=-0.15),
            margin=dict(t=60, b=60)
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        persona_counts = dff["persona"].value_counts().reset_index()
        persona_counts.columns = ["Persona", "Count"]
        persona_counts["Persona"] = persona_counts["Persona"].str.replace("_", " ")
        fig2 = px.bar(persona_counts, x="Count", y="Persona", orientation="h",
                      title="Respondents by Persona",
                      color="Count", color_continuous_scale="Blues")
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            coloraxis_showscale=False,
            yaxis=dict(gridcolor='#1e3a5f'),
            xaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=20)
        )
        st.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        org_counts = dff["q2_org_type"].value_counts().reset_index()
        org_counts.columns = ["Org Type", "Count"]
        fig3 = px.bar(org_counts, x="Org Type", y="Count",
                      title="Organisation Type Breakdown",
                      color="Count", color_continuous_scale="Teal")
        fig3.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            coloraxis_showscale=False, xaxis_tickangle=-30,
            yaxis=dict(gridcolor='#1e3a5f'), xaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=80)
        )
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        fleet_order = ["1-10", "11-30", "31-80", "81-200", "200+"]
        fleet_counts = dff["q3_fleet_size"].value_counts().reindex(fleet_order).reset_index()
        fleet_counts.columns = ["Fleet Size", "Count"]
        fig4 = px.bar(fleet_counts, x="Fleet Size", y="Count",
                      title="Fleet Size Distribution",
                      color="Count", color_continuous_scale="Oranges")
        fig4.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            coloraxis_showscale=False,
            yaxis=dict(gridcolor='#1e3a5f'), xaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=20)
        )
        st.plotly_chart(fig4, use_container_width=True)

    c5, c6 = st.columns(2)
    with c5:
        maint_counts = dff["q6_maintenance_strategy"].value_counts().reset_index()
        maint_counts.columns = ["Strategy", "Count"]
        fig5 = px.pie(maint_counts, names="Strategy", values="Count",
                      title="Current Maintenance Strategy", hole=0.35,
                      color_discrete_sequence=px.colors.sequential.Blues_r)
        fig5.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', font_color='#c8d8e8',
            title_font_family='Syne', margin=dict(t=60, b=20)
        )
        st.plotly_chart(fig5, use_container_width=True)

    with c6:
        loc_counts = dff["q5_location"].value_counts().reset_index()
        loc_counts.columns = ["Location", "Count"]
        fig6 = px.bar(loc_counts, x="Location", y="Count",
                      title="Respondents by Location",
                      color="Count", color_continuous_scale="Purples")
        fig6.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            coloraxis_showscale=False,
            yaxis=dict(gridcolor='#1e3a5f'), xaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=20)
        )
        st.plotly_chart(fig6, use_container_width=True)

    # Heatmap: lead label vs digital maturity
    st.markdown('<div class="section-header">Lead Quality vs Digital Maturity <span class="section-tag">Insight</span></div>', unsafe_allow_html=True)
    heat_data = dff.groupby(["q6_maintenance_strategy", "lead_label"]).size().unstack(fill_value=0)
    fig7 = px.imshow(heat_data, text_auto=True, aspect="auto",
                     color_continuous_scale="Blues",
                     title="Maintenance Strategy vs Lead Label Heatmap")
    fig7.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color='#c8d8e8', title_font_family='Syne',
        margin=dict(t=60, b=20)
    )
    st.plotly_chart(fig7, use_container_width=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1 — CLASSIFICATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab1:
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                                  f1_score, classification_report,
                                  confusion_matrix, roc_curve, auc)
    from sklearn.preprocessing import label_binarize

    st.markdown('<div class="section-header">Lead Classification Model <span class="section-tag">Supervised Learning</span></div>', unsafe_allow_html=True)
    st.markdown("**Goal:** Predict whether a customer will be a Hot / Warm / Exploring / Not Interested lead. Target variable: `lead_label` (Q25)")

    # Feature selection
    clf_features = [
        "q11_digital_maturity", "q21_current_tool_satisfaction",
        "q22_switching_likelihood", "q29_data_comfort",
        "q26_attitude_early_adopter", "q26_attitude_leadership_champ",
        "q26_attitude_switch_for_ai", "q26_attitude_wait_for_peers",
        "budget_per_aircraft_usd", "annual_spend_usd",
    ]
    # Add ordinal encodings
    fleet_map = {"1-10": 1, "11-30": 2, "31-80": 3, "81-200": 4, "200+": 5}
    spend_map = {"<$500K": 1, "$500K-$2M": 2, "$2M-$10M": 3, "$10M-$50M": 4, ">$50M": 5}
    aog_map = {"0": 0, "1-2": 1, "3-5": 2, "6-10": 3, "10+": 4}
    proc_map = {"<1 month": 1, "1-3 months": 2, "3-6 months": 3, "6-12 months": 4, ">12 months": 5}

    clf_df = dff.copy()
    clf_df["fleet_enc"] = clf_df["q3_fleet_size"].map(fleet_map)
    clf_df["spend_enc"] = clf_df["q8_annual_mro_spend"].map(spend_map)
    clf_df["aog_enc"] = clf_df["q7_aog_per_month"].map(aog_map)
    clf_df["proc_enc"] = clf_df["q18_procurement_cycle"].map(proc_map)

    all_features = clf_features + ["fleet_enc", "spend_enc", "aog_enc", "proc_enc"]
    clf_df_clean = clf_df[all_features + ["lead_label"]].dropna()

    le = LabelEncoder()
    y = le.fit_transform(clf_df_clean["lead_label"])
    X = clf_df_clean[all_features].fillna(0)

    col_model, col_run = st.columns([3, 1])
    with col_model:
        model_choice = st.selectbox("Select Classifier",
            ["Random Forest", "Gradient Boosting", "Logistic Regression"])
    with col_run:
        st.markdown("<br>", unsafe_allow_html=True)
        run_clf = st.button("▶  Train Model", type="primary", use_container_width=True)

    if run_clf or True:  # auto-run
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y)

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        if model_choice == "Random Forest":
            model = RandomForestClassifier(n_estimators=150, max_depth=8, random_state=42, n_jobs=-1)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)
        elif model_choice == "Gradient Boosting":
            model = GradientBoostingClassifier(n_estimators=100, max_depth=4, random_state=42)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)
        else:
            model = LogisticRegression(max_iter=1000, random_state=42, multi_class='ovr')
            model.fit(X_train_s, y_train)
            y_pred = model.predict(X_test_s)
            y_prob = model.predict_proba(X_test_s)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

        # Metrics row
        st.markdown("#### Performance Metrics")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Accuracy", f"{acc:.3f}")
        m2.metric("Precision (weighted)", f"{prec:.3f}")
        m3.metric("Recall (weighted)", f"{rec:.3f}")
        m4.metric("F1-Score (weighted)", f"{f1:.3f}")

        st.markdown("<br>", unsafe_allow_html=True)
        c_left, c_right = st.columns(2)

        # Confusion matrix
        with c_left:
            cm = confusion_matrix(y_test, y_pred)
            class_names = le.classes_
            fig_cm = px.imshow(cm, text_auto=True,
                               x=class_names, y=class_names,
                               color_continuous_scale="Blues",
                               title="Confusion Matrix",
                               labels=dict(x="Predicted", y="Actual"))
            fig_cm.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font_color='#c8d8e8', title_font_family='Syne',
                margin=dict(t=60, b=20)
            )
            st.plotly_chart(fig_cm, use_container_width=True)

        # Feature importance
        with c_right:
            if hasattr(model, "feature_importances_"):
                imp = pd.DataFrame({
                    "Feature": all_features,
                    "Importance": model.feature_importances_
                }).sort_values("Importance", ascending=True).tail(12)
                fig_imp = px.bar(imp, x="Importance", y="Feature", orientation="h",
                                 title="Feature Importance",
                                 color="Importance", color_continuous_scale="Blues")
            else:
                # Logistic regression coefficients
                coef_mean = np.abs(model.coef_).mean(axis=0)
                imp = pd.DataFrame({
                    "Feature": all_features,
                    "Importance": coef_mean
                }).sort_values("Importance", ascending=True).tail(12)
                fig_imp = px.bar(imp, x="Importance", y="Feature", orientation="h",
                                 title="Feature Importance (|Coef| mean)",
                                 color="Importance", color_continuous_scale="Blues")

            fig_imp.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font_color='#c8d8e8', title_font_family='Syne',
                coloraxis_showscale=False,
                yaxis=dict(gridcolor='#1e3a5f'),
                xaxis=dict(gridcolor='#1e3a5f'),
                margin=dict(t=60, b=20)
            )
            st.plotly_chart(fig_imp, use_container_width=True)

        # ROC Curve — one-vs-rest
        st.markdown("#### ROC Curves (One-vs-Rest per Class)")
        classes = le.classes_
        n_classes = len(classes)
        y_test_bin = label_binarize(y_test, classes=list(range(n_classes)))

        fig_roc = go.Figure()
        colors_roc = ["#ef5350", "#42a5f5", "#ffa726", "#78909c"]
        for i, cls_name in enumerate(classes):
            if y_test_bin.shape[1] > 1:
                fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_prob[:, i])
                roc_auc = auc(fpr, tpr)
                fig_roc.add_trace(go.Scatter(
                    x=fpr, y=tpr,
                    name=f"{cls_name} (AUC={roc_auc:.3f})",
                    mode='lines',
                    line=dict(color=colors_roc[i % len(colors_roc)], width=2.5)
                ))
        fig_roc.add_trace(go.Scatter(
            x=[0, 1], y=[0, 1], mode='lines',
            line=dict(dash='dash', color='#444', width=1),
            showlegend=False
        ))
        fig_roc.update_layout(
            title="ROC Curve — Multi-Class One-vs-Rest",
            xaxis_title="False Positive Rate",
            yaxis_title="True Positive Rate",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            legend=dict(bgcolor='rgba(0,0,0,0)'),
            xaxis=dict(gridcolor='#1e3a5f'),
            yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=40)
        )
        st.plotly_chart(fig_roc, use_container_width=True)

        # Per-class metrics table
        st.markdown("#### Per-Class Classification Report")
        report = classification_report(y_test, y_pred,
                                       target_names=le.classes_,
                                       output_dict=True, zero_division=0)
        report_df = pd.DataFrame(report).T.round(3)
        report_df = report_df.loc[le.classes_]
        st.dataframe(
            report_df.style.background_gradient(cmap='Blues', axis=None),
            use_container_width=True
        )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2 — CLUSTERING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab2:
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.metrics import silhouette_score

    st.markdown('<div class="section-header">Customer Persona Clustering <span class="section-tag">Unsupervised Learning</span></div>', unsafe_allow_html=True)
    st.markdown("**Goal:** Segment customers into actionable personas for targeted discounting and bundle packaging.")

    clust_features = [
        "q11_digital_maturity", "q21_current_tool_satisfaction",
        "q22_switching_likelihood", "q29_data_comfort",
        "budget_per_aircraft_usd", "annual_spend_usd",
        "q26_attitude_early_adopter", "q26_attitude_leadership_champ",
        "q26_attitude_switch_for_ai",
    ]
    clust_df = dff.copy()
    clust_df["fleet_enc"] = clust_df["q3_fleet_size"].map(fleet_map)
    clust_df["aog_enc"] = clust_df["q7_aog_per_month"].map(aog_map)
    clust_features_all = clust_features + ["fleet_enc", "aog_enc"]
    clust_data = clust_df[clust_features_all].dropna()

    scaler_c = StandardScaler()
    X_clust = scaler_c.fit_transform(clust_data)

    # Elbow + Silhouette
    sse, sil_scores = [], []
    k_range = range(2, 9)
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels_tmp = km.fit_predict(X_clust)
        sse.append(km.inertia_)
        sil_scores.append(silhouette_score(X_clust, labels_tmp))

    col_elbow, col_sil = st.columns(2)
    with col_elbow:
        fig_elbow = go.Figure()
        fig_elbow.add_trace(go.Scatter(
            x=list(k_range), y=sse, mode='lines+markers',
            line=dict(color='#4fc3f7', width=2.5),
            marker=dict(size=8, color='#4fc3f7')
        ))
        fig_elbow.update_layout(
            title="Elbow Method — Optimal K",
            xaxis_title="Number of Clusters (K)",
            yaxis_title="SSE (Inertia)",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=40)
        )
        st.plotly_chart(fig_elbow, use_container_width=True)

    with col_sil:
        fig_sil = go.Figure()
        fig_sil.add_trace(go.Scatter(
            x=list(k_range), y=sil_scores, mode='lines+markers',
            line=dict(color='#ffa726', width=2.5),
            marker=dict(size=8, color='#ffa726')
        ))
        fig_sil.update_layout(
            title="Silhouette Score by K",
            xaxis_title="Number of Clusters (K)",
            yaxis_title="Silhouette Score",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=40)
        )
        st.plotly_chart(fig_sil, use_container_width=True)

    # Fit chosen K
    km_final = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clust_data = clust_data.copy()
    clust_data["Cluster"] = km_final.fit_predict(X_clust).astype(str)

    sil_final = silhouette_score(X_clust, km_final.labels_)
    st.metric(f"Silhouette Score (K={n_clusters})", f"{sil_final:.4f}")

    # PCA scatter
    pca = PCA(n_components=2, random_state=42)
    pca_coords = pca.fit_transform(X_clust)
    clust_data["PCA_1"] = pca_coords[:, 0]
    clust_data["PCA_2"] = pca_coords[:, 1]

    fig_pca = px.scatter(
        clust_data, x="PCA_1", y="PCA_2", color="Cluster",
        title=f"Customer Clusters (PCA 2D Projection) — K={n_clusters}",
        color_discrete_sequence=px.colors.qualitative.Bold,
        opacity=0.7
    )
    fig_pca.update_traces(marker=dict(size=5))
    fig_pca.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color='#c8d8e8', title_font_family='Syne',
        xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
        margin=dict(t=60, b=40)
    )
    st.plotly_chart(fig_pca, use_container_width=True)

    # Cluster profile radar
    st.markdown("#### Cluster Profiles — Radar Chart")
    radar_features = ["q11_digital_maturity", "q22_switching_likelihood",
                       "q29_data_comfort", "q26_attitude_early_adopter",
                       "q26_attitude_leadership_champ", "fleet_enc"]
    radar_labels = ["Digital Maturity", "Switch Likelihood", "Data Comfort",
                     "Early Adopter", "Leadership Champ", "Fleet Size"]

    cluster_means = clust_data.groupby("Cluster")[radar_features].mean()
    # Normalize 0-1
    for col in radar_features:
        mn, mx = clust_data[col].min(), clust_data[col].max()
        if mx > mn:
            cluster_means[col] = (cluster_means[col] - mn) / (mx - mn)

    fig_radar = go.Figure()
    colors_radar = px.colors.qualitative.Bold
    for i, (idx, row) in enumerate(cluster_means.iterrows()):
        vals = row.tolist()
        vals += [vals[0]]
        lbls = radar_labels + [radar_labels[0]]
        fig_radar.add_trace(go.Scatterpolar(
            r=vals, theta=lbls,
            fill='toself', name=f"Cluster {idx}",
            line=dict(color=colors_radar[i % len(colors_radar)]),
            fillcolor=colors_radar[i % len(colors_radar)].replace('rgb', 'rgba').replace(')', ',0.15)') if 'rgb' in colors_radar[i % len(colors_radar)] else colors_radar[i % len(colors_radar)]
        ))
    fig_radar.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 1], gridcolor='#1e3a5f', color='#7eb8d4'),
            angularaxis=dict(gridcolor='#1e3a5f', color='#7eb8d4')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#c8d8e8', title_font_family='Syne',
        title="Cluster Characteristic Profiles",
        margin=dict(t=80, b=40)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # Cluster size + budget comparison
    col_cs, col_cb = st.columns(2)
    with col_cs:
        cs = clust_data["Cluster"].value_counts().reset_index()
        cs.columns = ["Cluster", "Count"]
        fig_cs = px.bar(cs, x="Cluster", y="Count",
                        color="Cluster", title="Cluster Sizes",
                        color_discrete_sequence=px.colors.qualitative.Bold)
        fig_cs.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            showlegend=False,
            xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=20)
        )
        st.plotly_chart(fig_cs, use_container_width=True)

    with col_cb:
        cb = clust_data.groupby("Cluster")["budget_per_aircraft_usd"].mean().reset_index()
        cb.columns = ["Cluster", "Avg Budget/AC"]
        fig_cb = px.bar(cb, x="Cluster", y="Avg Budget/AC",
                        color="Cluster", title="Avg Budget per Aircraft by Cluster",
                        color_discrete_sequence=px.colors.qualitative.Bold)
        fig_cb.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            showlegend=False,
            xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=20)
        )
        st.plotly_chart(fig_cb, use_container_width=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3 — ASSOCIATION RULES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab3:
    from mlxtend.frequent_patterns import apriori, association_rules
    from mlxtend.preprocessing import TransactionEncoder

    st.markdown('<div class="section-header">Association Rule Mining <span class="section-tag">Market Basket Analysis</span></div>', unsafe_allow_html=True)
    st.markdown("**Goal:** Discover which products, features, and value outcomes are purchased/chosen together — enabling bundle packaging and cross-sell strategies.")

    arm_type = st.radio("Select basket type for ARM",
        ["Product Module Interest (Q19)", "Desired Features (Q13)",
         "Value Outcomes (Q20)", "Systems with Unplanned Maintenance (Q9)"],
        horizontal=True
    )

    prefix_map = {
        "Product Module Interest (Q19)": "q19_",
        "Desired Features (Q13)": "q13_",
        "Value Outcomes (Q20)": "q20_",
        "Systems with Unplanned Maintenance (Q9)": "q9_",
    }
    prefix = prefix_map[arm_type]
    arm_cols = [c for c in dff.columns if c.startswith(prefix)]

    if len(arm_cols) < 2:
        st.warning("Not enough columns found for this basket type. Try another.")
    else:
        basket_df = dff[arm_cols].fillna(0).astype(bool)
        basket_df.columns = [c.replace(prefix, "").replace("_", " ").title() for c in basket_df.columns]

        # Remove all-false rows
        basket_df = basket_df[basket_df.any(axis=1)]

        try:
            freq_items = apriori(basket_df, min_support=min_support,
                                  use_colnames=True, max_len=4)

            if len(freq_items) == 0:
                st.warning(f"No frequent itemsets found at support={min_support:.2f}. Try lowering the Min Support slider.")
            else:
                rules = association_rules(freq_items, metric="confidence",
                                           min_threshold=min_confidence)
                rules = rules.sort_values("lift", ascending=False)
                rules["antecedents"] = rules["antecedents"].apply(lambda x: ", ".join(list(x)))
                rules["consequents"] = rules["consequents"].apply(lambda x: ", ".join(list(x)))

                st.success(f"Found **{len(freq_items)}** frequent itemsets and **{len(rules)}** rules at support≥{min_support:.2f}, confidence≥{min_confidence:.2f}")

                # Top metrics
                a1, a2, a3, a4 = st.columns(4)
                a1.metric("Total Rules", len(rules))
                a2.metric("Max Lift", f"{rules['lift'].max():.3f}" if len(rules) else "—")
                a3.metric("Max Confidence", f"{rules['confidence'].max():.3f}" if len(rules) else "—")
                a4.metric("Max Support", f"{rules['support'].max():.3f}" if len(rules) else "—")

                if len(rules) > 0:
                    # Scatter: support vs confidence coloured by lift
                    fig_arm = px.scatter(
                        rules.head(80), x="support", y="confidence",
                        color="lift", size="lift",
                        hover_data=["antecedents", "consequents", "lift"],
                        color_continuous_scale="Blues",
                        title="Support vs Confidence (bubble size & colour = Lift)",
                        labels={"support": "Support", "confidence": "Confidence", "lift": "Lift"}
                    )
                    fig_arm.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                        font_color='#c8d8e8', title_font_family='Syne',
                        xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
                        margin=dict(t=60, b=40)
                    )
                    st.plotly_chart(fig_arm, use_container_width=True)

                    # Top rules by lift
                    col_r1, col_r2 = st.columns(2)
                    with col_r1:
                        st.markdown("#### Top 15 Rules by Lift")
                        top_rules = rules[["antecedents", "consequents",
                                            "support", "confidence", "lift"]].head(15)
                        top_rules = top_rules.round(4)
                        st.dataframe(
                            top_rules.style.background_gradient(subset=["lift"], cmap="Blues"),
                            use_container_width=True, height=420
                        )
                    with col_r2:
                        st.markdown("#### Top 15 Rules by Confidence")
                        top_conf = rules[["antecedents", "consequents",
                                           "support", "confidence", "lift"]].sort_values(
                            "confidence", ascending=False).head(15).round(4)
                        st.dataframe(
                            top_conf.style.background_gradient(subset=["confidence"], cmap="Purples"),
                            use_container_width=True, height=420
                        )

                    # Lift heatmap (top antecedents vs consequents)
                    st.markdown("#### Lift Heatmap — Top Rule Pairs")
                    top_h = rules.head(25)
                    pivot = top_h.pivot_table(
                        index="antecedents", columns="consequents",
                        values="lift", aggfunc="mean"
                    ).fillna(0)
                    fig_heat = px.imshow(
                        pivot, text_auto=".2f", aspect="auto",
                        color_continuous_scale="Blues",
                        title="Lift Heatmap — Antecedents vs Consequents"
                    )
                    fig_heat.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                        font_color='#c8d8e8', title_font_family='Syne',
                        margin=dict(t=60, b=80),
                        xaxis_tickangle=-35
                    )
                    st.plotly_chart(fig_heat, use_container_width=True)

                    # Bar: top consequents by avg lift
                    st.markdown("#### Most Frequently Implied Products (by Avg Lift)")
                    cons_lift = rules.groupby("consequents")["lift"].mean().sort_values(ascending=False).head(12).reset_index()
                    cons_lift.columns = ["Product / Feature", "Avg Lift"]
                    fig_cons = px.bar(cons_lift, x="Avg Lift", y="Product / Feature",
                                      orientation="h", color="Avg Lift",
                                      color_continuous_scale="Blues",
                                      title="Top Consequents by Average Lift")
                    fig_cons.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                        font_color='#c8d8e8', title_font_family='Syne',
                        coloraxis_showscale=False,
                        yaxis=dict(gridcolor='#1e3a5f'),
                        xaxis=dict(gridcolor='#1e3a5f'),
                        margin=dict(t=60, b=20)
                    )
                    st.plotly_chart(fig_cons, use_container_width=True)

        except Exception as e:
            st.error(f"ARM Error: {e}. Try lowering the minimum support threshold.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4 — REGRESSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab4:
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler

    st.markdown('<div class="section-header">Spending Power & Budget Regression <span class="section-tag">Predictive Modelling</span></div>', unsafe_allow_html=True)
    st.markdown("**Goal:** Predict a customer's annual spending power (`annual_spend_usd`) and budget per aircraft (`budget_per_aircraft_usd`) to enable custom pricing and discount tiers.")

    reg_target = st.selectbox("Regression Target",
        ["annual_spend_usd", "budget_per_aircraft_usd"])

    reg_model_choice = st.selectbox("Select Regressor",
        ["Gradient Boosting", "Random Forest", "Ridge Regression", "Linear Regression", "Lasso"])

    reg_features = [
        "q11_digital_maturity", "q21_current_tool_satisfaction",
        "q22_switching_likelihood", "q29_data_comfort",
        "q26_attitude_early_adopter", "q26_attitude_leadership_champ",
    ]
    reg_df = dff.copy()
    reg_df["fleet_enc"] = reg_df["q3_fleet_size"].map(fleet_map)
    reg_df["spend_cat_enc"] = reg_df["q8_annual_mro_spend"].map(spend_map)
    reg_df["aog_enc"] = reg_df["q7_aog_per_month"].map(aog_map)
    reg_df["proc_enc"] = reg_df["q18_procurement_cycle"].map(proc_map)
    reg_all_feat = reg_features + ["fleet_enc", "spend_cat_enc", "aog_enc", "proc_enc"]

    reg_clean = reg_df[reg_all_feat + [reg_target]].dropna()
    Xr = reg_clean[reg_all_feat].fillna(0)
    yr = reg_clean[reg_target]

    Xr_train, Xr_test, yr_train, yr_test = train_test_split(
        Xr, yr, test_size=test_size, random_state=42)

    scaler_r = StandardScaler()
    Xr_train_s = scaler_r.fit_transform(Xr_train)
    Xr_test_s = scaler_r.transform(Xr_test)

    if reg_model_choice == "Gradient Boosting":
        reg_model = GradientBoostingRegressor(n_estimators=150, max_depth=4, random_state=42)
        reg_model.fit(Xr_train, yr_train)
        yr_pred = reg_model.predict(Xr_test)
    elif reg_model_choice == "Random Forest":
        reg_model = RandomForestRegressor(n_estimators=150, max_depth=8, random_state=42, n_jobs=-1)
        reg_model.fit(Xr_train, yr_train)
        yr_pred = reg_model.predict(Xr_test)
    elif reg_model_choice == "Ridge Regression":
        reg_model = Ridge(alpha=1.0)
        reg_model.fit(Xr_train_s, yr_train)
        yr_pred = reg_model.predict(Xr_test_s)
    elif reg_model_choice == "Lasso":
        reg_model = Lasso(alpha=0.5, max_iter=5000)
        reg_model.fit(Xr_train_s, yr_train)
        yr_pred = reg_model.predict(Xr_test_s)
    else:
        reg_model = LinearRegression()
        reg_model.fit(Xr_train_s, yr_train)
        yr_pred = reg_model.predict(Xr_test_s)

    mae = mean_absolute_error(yr_test, yr_pred)
    rmse = np.sqrt(mean_squared_error(yr_test, yr_pred))
    r2 = r2_score(yr_test, yr_pred)
    mape = np.mean(np.abs((yr_test - yr_pred) / (yr_test + 1))) * 100

    r1c, r2c, r3c, r4c = st.columns(4)
    r1c.metric("R² Score", f"{r2:.4f}")
    r2c.metric("MAE", f"${mae:,.0f}")
    r3c.metric("RMSE", f"${rmse:,.0f}")
    r4c.metric("MAPE", f"{mape:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)
    rc1, rc2 = st.columns(2)

    # Actual vs Predicted
    with rc1:
        sample_n = min(300, len(yr_test))
        idx_sample = np.random.choice(len(yr_test), sample_n, replace=False)
        fig_avp = go.Figure()
        fig_avp.add_trace(go.Scatter(
            x=yr_test.iloc[idx_sample].values,
            y=yr_pred[idx_sample],
            mode='markers',
            marker=dict(color='#4fc3f7', opacity=0.5, size=5),
            name='Predictions'
        ))
        mn_val = min(yr_test.min(), yr_pred.min())
        mx_val = max(yr_test.max(), yr_pred.max())
        fig_avp.add_trace(go.Scatter(
            x=[mn_val, mx_val], y=[mn_val, mx_val],
            mode='lines', line=dict(color='#ef5350', dash='dash', width=2),
            name='Perfect fit'
        ))
        fig_avp.update_layout(
            title="Actual vs Predicted",
            xaxis_title="Actual", yaxis_title="Predicted",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=40)
        )
        st.plotly_chart(fig_avp, use_container_width=True)

    # Residuals
    with rc2:
        residuals = yr_test.values - yr_pred
        fig_res = go.Figure()
        fig_res.add_trace(go.Scatter(
            x=yr_pred, y=residuals,
            mode='markers',
            marker=dict(color='#ffa726', opacity=0.5, size=5),
            name='Residuals'
        ))
        fig_res.add_hline(y=0, line_dash='dash', line_color='#ef5350', line_width=1.5)
        fig_res.update_layout(
            title="Residual Plot",
            xaxis_title="Predicted", yaxis_title="Residuals",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=40)
        )
        st.plotly_chart(fig_res, use_container_width=True)

    # Feature importance / coefficients
    rc3, rc4 = st.columns(2)
    with rc3:
        if hasattr(reg_model, "feature_importances_"):
            fi_df = pd.DataFrame({
                "Feature": reg_all_feat,
                "Importance": reg_model.feature_importances_
            }).sort_values("Importance", ascending=True)
            fig_fi = px.bar(fi_df, x="Importance", y="Feature", orientation="h",
                            title="Feature Importance",
                            color="Importance", color_continuous_scale="Teal")
        else:
            coef = reg_model.coef_
            fi_df = pd.DataFrame({
                "Feature": reg_all_feat,
                "Coefficient": coef
            }).sort_values("Coefficient", ascending=True)
            fig_fi = px.bar(fi_df, x="Coefficient", y="Feature", orientation="h",
                            title="Regression Coefficients",
                            color="Coefficient", color_continuous_scale="RdBu")
        fig_fi.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            coloraxis_showscale=False,
            yaxis=dict(gridcolor='#1e3a5f'), xaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=20)
        )
        st.plotly_chart(fig_fi, use_container_width=True)

    with rc4:
        # Distribution of predicted vs actual
        fig_dist = go.Figure()
        fig_dist.add_trace(go.Histogram(
            x=yr_test.values, name="Actual",
            opacity=0.65, nbinsx=30,
            marker_color='#4fc3f7'
        ))
        fig_dist.add_trace(go.Histogram(
            x=yr_pred, name="Predicted",
            opacity=0.65, nbinsx=30,
            marker_color='#ffa726'
        ))
        fig_dist.update_layout(
            barmode='overlay',
            title="Distribution: Actual vs Predicted",
            xaxis_title=reg_target,
            yaxis_title="Count",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#c8d8e8', title_font_family='Syne',
            legend=dict(bgcolor='rgba(0,0,0,0)'),
            xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
            margin=dict(t=60, b=40)
        )
        st.plotly_chart(fig_dist, use_container_width=True)

    # Predicted spend buckets — for discount targeting
    st.markdown("#### Predicted Spending Buckets — Discount Tier Targeting")
    pred_all = reg_model.predict(
        scaler_r.transform(Xr) if reg_model_choice in
        ["Ridge Regression", "Lasso", "Linear Regression"] else Xr
    )
    bucket_df = reg_clean[[reg_target]].copy()
    bucket_df["Predicted"] = pred_all

    def assign_tier(val):
        if val < 500000:   return "Tier 1 — Entry (<$500K)"
        elif val < 2000000: return "Tier 2 — Growth ($500K–$2M)"
        elif val < 10000000: return "Tier 3 — Mid ($2M–$10M)"
        elif val < 50000000: return "Tier 4 — Enterprise ($10M–$50M)"
        else:               return "Tier 5 — Elite (>$50M)"

    bucket_df["Predicted Tier"] = bucket_df["Predicted"].apply(assign_tier)
    tier_counts = bucket_df["Predicted Tier"].value_counts().reset_index()
    tier_counts.columns = ["Tier", "Count"]
    tier_order = ["Tier 1 — Entry (<$500K)", "Tier 2 — Growth ($500K–$2M)",
                  "Tier 3 — Mid ($2M–$10M)", "Tier 4 — Enterprise ($10M–$50M)",
                  "Tier 5 — Elite (>$50M)"]
    tier_counts["Tier"] = pd.Categorical(tier_counts["Tier"], categories=tier_order, ordered=True)
    tier_counts = tier_counts.sort_values("Tier")

    fig_tiers = px.bar(tier_counts, x="Tier", y="Count",
                       color="Tier", title="Customer Spending Tier Distribution (Predicted)",
                       color_discrete_sequence=["#78909c","#42a5f5","#ffa726","#ef5350","#ab47bc"])
    fig_tiers.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color='#c8d8e8', title_font_family='Syne',
        showlegend=False, xaxis_tickangle=-20,
        xaxis=dict(gridcolor='#1e3a5f'), yaxis=dict(gridcolor='#1e3a5f'),
        margin=dict(t=60, b=100)
    )
    st.plotly_chart(fig_tiers, use_container_width=True)
